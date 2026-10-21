#!/usr/bin/env python3
"""Recompute recovered metrics from aggregate counts or a private prediction CSV.

This audits saved outputs. It does not load a checkpoint or execute a model.
"""
import argparse
from collections import Counter, defaultdict
import csv
from decimal import Decimal, ROUND_HALF_UP
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = (0, 1, 2)


def percent(correct, total):
    if total <= 0 or not 0 <= correct <= total:
        raise ValueError("Invalid correct/total counts")
    return (Decimal(correct) * 100 / Decimal(total)).quantize(Decimal(".01"), rounding=ROUND_HALF_UP)


def summarize_counts(counts):
    if set(counts) != {(a, b) for a in LABELS for b in LABELS}:
        raise ValueError("Expected all nine label/prediction pairs")
    if any(type(n) is not int or n < 0 for n in counts.values()):
        raise ValueError("Counts must be nonnegative integers")
    total = sum(counts.values())
    correct = sum(counts[(a, a)] for a in LABELS)
    per_class = {}
    for a in LABELS:
        n = sum(counts[(a, b)] for b in LABELS)
        per_class[str(a)] = {"total": n, "correct": counts[(a, a)],
                             "accuracy_pct": str(percent(counts[(a, a)], n))}
    return {"scored_rows": total, "correct_rows": correct,
            "top1_pct": str(percent(correct, total)), "per_class": per_class}


def read_predictions(path, frames_per_clip=32):
    if frames_per_clip < 1:
        raise ValueError("frames_per_clip must be positive")
    path = Path(path)
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != ["label", "prediction", "result"]:
            raise ValueError("Unexpected prediction schema")
        rows = list(reader)
    if not rows or len(rows) % frames_per_clip:
        raise ValueError("Incomplete sampled-frame blocks")
    pairs = []
    for r in rows:
        a, b = int(r["label"]), int(r["prediction"])
        if a not in LABELS or b not in LABELS:
            raise ValueError("Unknown class")
        if r["result"] != ("correct" if a == b else "incorrect"):
            raise ValueError("Stored result flag disagrees with label/prediction")
        pairs.append((a, b))
    if any(len(set(pairs[i:i + frames_per_clip])) != 1
           for i in range(0, len(pairs), frames_per_clip)):
        raise ValueError("A sampled-frame block contains differing predictions or labels")
    observed = Counter(pairs)
    counts = {(a, b): observed[(a, b)] for a in LABELS for b in LABELS}
    result = summarize_counts(counts)
    result.update(source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  frames_per_clip=frames_per_clip, uniform_blocks=len(rows) // frames_per_clip)
    return result, counts


def audit_released_counts(root=ROOT):
    grouped = defaultdict(dict)
    with (root / "experiments/recovered/confusion_counts.csv").open(newline="") as f:
        for r in csv.DictReader(f):
            key = int(r["label"]), int(r["prediction"])
            if key in grouped[r["run_id"]]:
                raise ValueError("Duplicate confusion-matrix cell")
            grouped[r["run_id"]][key] = int(r["count"])
    with (root / "experiments/recovered/results.csv").open(newline="") as f:
        rows = list(csv.DictReader(f))
    if len({r["run_id"] for r in rows}) != len(rows) or set(grouped) != {r["run_id"] for r in rows}:
        raise ValueError("Run IDs are duplicated or do not match")
    summaries = []
    for r in rows:
        s = summarize_counts(grouped[r["run_id"]])
        for field in ("scored_rows", "correct_rows", "top1_pct"):
            if Decimal(r[field]) != Decimal(s[field]):
                raise ValueError(f"Summary mismatch: {r['run_id']}: {field}")
        for label, name in enumerate(("shaking_pct", "swirling_pct", "buretting_pct")):
            if Decimal(r[name]) != Decimal(s["per_class"][str(label)]["accuracy_pct"]):
                raise ValueError(f"Per-class mismatch: {r['run_id']}: {name}")
        summaries.append({"run_id": r["run_id"], **s})
    return summaries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--predictions", type=Path, help="Private original predictions_test.csv; read only")
    args = parser.parse_args()
    if args.predictions:
        summary, counts = read_predictions(args.predictions)
        summary["confusion_counts"] = [{"label": a, "prediction": b, "count": n}
                                        for (a, b), n in counts.items()]
        print(json.dumps(summary, indent=2))
    else:
        for s in audit_released_counts():
            print(f"{s['run_id']}: {s['correct_rows']}/{s['scored_rows']} = {s['top1_pct']}%")
        print("PASS: released aggregates reconcile. Saved-output audit only; no model rerun.")


if __name__ == "__main__":
    main()
