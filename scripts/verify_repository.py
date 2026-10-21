#!/usr/bin/env python3
"""Check preserved bytes, local Markdown targets, and displayed source values."""
import hashlib
import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
from audit_results import ROOT, load_results


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check_preservation(root=ROOT):
    manifest = json.loads((root / "references/benchmark_integrity.json").read_text())
    errors = []
    for name, expected in manifest["files"].items():
        path = root / name
        if not path.is_file() or digest(path.read_bytes()) != expected:
            errors.append(f"Preserved file changed or missing: {name}")
    text = (root / "README.md").read_text()
    start = "<!-- BEGIN ORIGINAL BENCHMARK README -->\n"
    end = "<!-- END ORIGINAL BENCHMARK README -->"
    if text.count(start) != 1 or text.count(end) != 1:
        errors.append("Original README boundary markers missing or duplicated")
    else:
        original = text.split(start, 1)[1].split(end, 1)[0]
        if digest(original.encode()) != manifest["original_readme_sha256"]:
            errors.append("Original README content changed")
    return errors


def check_local_links(root=ROOT):
    errors, count = [], 0
    for path in sorted(root.rglob("*.md")):
        if any(part in (".git", ".venv") for part in path.parts):
            continue
        text = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
        for match in re.finditer(r"!?\[[^\]]*\]\(([^\s)]+)\)", text):
            target = match.group(1)
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("//"):
                continue
            local = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            count += 1
            if not local.exists():
                errors.append(f"Broken local link in {path.relative_to(root)}: {target}")
            # Current authored links use file destinations, not section fragments.
            if parsed.fragment:
                errors.append(f"Fragment target needs explicit review: {path.name}: {target}")
    return errors, count


def check_result_tables(root=ROOT):
    rows = load_results(root / "experiments/paper_reported_results.csv")
    errors = []
    for name in ("docs/EXPERIMENTS.md", "docs/RESULTS_AND_ANALYSIS.md"):
        text = (root / name).read_text()
        for r in rows:
            pp = r["top1_pct"] - rows[0]["top1_pct"]
            line = (f'| {r["label"]} | 90 + {r["synthetic_training_videos"]} | '
                    f'{r["top1_pct"]:.2f} | {pp:+.2f} |')
            if line not in text:
                errors.append(f"Result row missing/inconsistent: {name}: {r['experiment_id']}")
    text = (root / "docs/RESULTS_AND_ANALYSIS.md").read_text()
    for r in rows:
        line = f'| {r["label"]} | {r["shaking_pct"]:.2f} | {r["swirling_pct"]:.2f} | {r["buretting_pct"]:.2f} |'
        if line not in text:
            errors.append(f"Per-class result row missing/inconsistent: {r['experiment_id']}")
    with (root / "experiments/recovered/results.csv").open(newline="") as f:
        recovered = list(csv.DictReader(f))
    for name in ("README.md", "docs/DRIVE_AUDIT.md"):
        text = (root / name).read_text()
        for r in rows:
            values = [s["top1_pct"] for s in recovered if s["paper_experiment_id"] == r["experiment_id"]]
            saved = " / ".join(values) if values else "—"
            status = ("Prediction export not recovered" if not values else "Two versions" if len(values) > 1
                      else "Matches" if values[0] == f'{r["top1_pct"]:.2f}' else "Different record")
            line = f'| {r["label"]} | {r["top1_pct"]:.2f} | {saved} | {status} |'
            if line not in text:
                errors.append(f"Paper/saved comparison mismatch: {name}: {r['experiment_id']}")
    return errors


def check_recovered_notebook(root=ROOT):
    manifest = json.loads((root / "references/recovered_notebook_integrity.json").read_text())
    path = root / manifest["published_file"]
    errors = []
    if digest(path.read_bytes()) != manifest["published_sha256"]:
        errors.append("Recovered notebook changed without an updated provenance record")
    notebook = json.loads(path.read_text())
    if len(notebook["cells"]) != len(manifest["cells"]) + 1:
        errors.append("Recovered notebook cell count differs from provenance")
        return errors
    for entry in manifest["cells"]:
        cell = notebook["cells"][entry["published_cell_index"]]
        if digest("".join(cell["source"]).encode()) != entry["published_source_sha256"]:
            errors.append(f"Recovered cell source changed: {entry['published_cell_index']}")
        if cell.get("outputs") or cell.get("execution_count") is not None or cell.get("metadata"):
            errors.append(f"Recovered cell contains stored execution data: {entry['published_cell_index']}")
    return errors


def main():
    errors = check_preservation()
    link_errors, count = check_local_links()
    errors += link_errors + check_result_tables() + check_recovered_notebook()
    for path in sorted((ROOT / "notebooks").glob("*.ipynb")):
        notebook = json.loads(path.read_text())
        if notebook.get("nbformat") != 4 or not isinstance(notebook.get("cells"), list):
            errors.append(f"Unexpected notebook structure: {path.name}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: six original files and original README bytes preserved; {count} local links resolve.")
    print("PASS: paper tables and paper/saved comparisons match CSVs; recovered notebook integrity matches.")
    print("No external links, notebook execution, or model inference verified by this check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
