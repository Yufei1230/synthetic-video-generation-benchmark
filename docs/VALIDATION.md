# Validation record

Audit date: 2026-10-21. Base: `main` at `dd16e40f6828803cf3d13bffc4f3fe48c473cabf`. Working branch: `docs/complete-research-project-20261021`. These are documentation and integrity checks, not experimental reproduction.

## Executed checks

| Check | Outcome | Practical scope |
|---|---|---|
| Full repository clone and history inspection | Pass; 19 pre-existing commits, seven tracked files | Current original tree contains five notebooks, README, and one-newline results file |
| PDF text and visual inspection | Nine pages read; page contact sheet and method/result figures inspected | Source methods, tables, people-containing images and editorial issues reviewed |
| `python3 scripts/audit_results.py` | Pass | Eight rows, dataset arithmetic, pp/relative changes, and compatible denominators checked |
| `python3 scripts/verify_repository.py` | Pass | Six protected files plus original README text retain SHA-256 values; 57 local Markdown links resolve; table values reconcile |
| `python3 -m unittest discover -s tests -v` | **8 tests passed** | Includes mutation detection, bad-data rejection, rounding and denominator ambiguity |
| `python3 scripts/plot_results.py` | Pass | Two SVG charts generated from the source CSV |
| Repeated figure generation | Identical SVG SHA-256 values in the tested environment | Deterministic documentation export; not deterministic model inference |
| Figure visual review | Pass | PNG renders of the same Matplotlib figures inspected for labels, scale, values and clipping |
| Notebook format check | Five parse as nbformat 4 JSON | Syntax/structure only; no notebook execution or schema-completeness claim |
| Original benchmark Git diff | Empty for `notebooks/` and `results/` | Original source and stored outputs unchanged |
| `git diff --check` | Pass | No whitespace errors in the reviewed diff |
| New-content secret/PII/size scan | No matches from the checks described below; largest changed/new file under 12 KB | Scope is newly authored content; inherited concerns tracked separately |

Environment: Python 3.12.14, Matplotlib 3.10.8. Checks ran without student data, generation-service credentials, GPU inference or model training.

## Content and disclosure review

New files are Markdown, JSON, CSV, BibTeX, Python, SVG, a requirements file and ignore rules. The changed-file list was inspected. No manuscript PDF, raw video, raster student image, checkpoint, archive, internal form or ethics document is included.

The new-content scan checked private-key headers, common GitHub/Hugging Face/AWS credential patterns, email addresses, signed/token query patterns and files exceeding 1 MB. It found no matches. Pattern scans are not comprehensive proof of absence; the final source/diff review complements them. The preserved historical README was checked by hash separately. Pre-existing notebook token-like download material and temporary service URLs are flagged in [privacy review](DATA_PRIVACY.md); their values are not reproduced in new documentation.

The new Mermaid flowchart source was manually checked for the two generation branches, reconvergence and five-stage horizontal flow. A live GitHub rendering of that Mermaid diagram was not inspected. SVG figures were inspected through renders of the same plotted figures; external links were not exhaustively tested, and historical benchmark links are intentionally preserved.

## What these checks do not establish

No original experiment was independently reproduced. No prediction log, dataset membership, checkpoint, random seed, exact SlowFast implementation or generation-service version was recovered. Frame-level accuracy is an author clarification; 17/29/44 is an arithmetic-compatible count construction, not recovered observations. Training/test overlap, classroom generalization, privacy protection, significance and deployment claims remain unverified.

Drive recursion, file-by-file deduplication, source ownership/licensing and paper-versus-log reconciliation are blocked by unavailable Drive access. Bibliographic records were corroborated, but direct publisher retrieval and comparison with the version of record were unavailable. See [source inventory](SOURCE_INVENTORY.md), [discrepancies](DISCREPANCIES.md), and [reproducibility](REPRODUCIBILITY.md).
