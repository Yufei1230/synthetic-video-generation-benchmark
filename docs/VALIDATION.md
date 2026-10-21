# Validation record

Audit date: 2026-10-21. Original base: `main` at `dd16e40f6828803cf3d13bffc4f3fe48c473cabf`. Delivery branch: `docs/complete-research-project-20261021`, draft PR #1. This Drive follow-up replaces the earlier access-blocked assessment.

## Executed checks

| Check | Outcome and scope |
|---|---|
| Original repository and manuscript | Seven-file tree/19-commit history and all nine manuscript pages inspected in the initial audit |
| Benchmark preservation | Six protected notebook/result SHA-256 values and the embedded original README text unchanged |
| Eight prediction exports | 23,040 rows audited; result flags, uniform 32-row blocks, class counts and adjacent class/Top-1 reports reconcile |
| Public aggregates | `audit_drive_results.py` recomputes eight run summaries, retaining conflicting versions |
| Video manifests | Eight files, seven distinct hashes; fold counts and four class+basename test/development collisions per manifest recorded |
| Frame-list/annotation audit | Six pairs agree on all 3,285 video/frame keys; source sampler arithmetic reproduces 2,880 scored rows |
| Settings and logs | Ten argument files and thirteen event files read; stored validation-step coverage summarized |
| Upstream comparison | 38 function/class ASTs match NVIDIA SynthDa; four differ and one additional FFmpeg helper exists |
| Recovered notebook | All source/cell hashes recorded; outputs, execution counts and user metadata removed; private roots replaced |
| Notebook syntax | 74 Python cells parse; one Colab shell-install cell preserved separately; no whole-notebook execution |
| Unit tests | **18 tests passed**: malformed evidence, aggregate mutation, preservation and source sampler edge cases |
| Tables and links | Paper tables, comparison tables and authored local Markdown destinations pass `verify_repository.py` |
| Figures | Three SVGs regenerated; corresponding Matplotlib PNGs visually inspected for values, labels, scale and clipping |
| Disclosure and size | Changed/new content scanned for credentials, email addresses, signed links, private Drive paths and embedded raster data; no matches; largest added file 98,243 bytes |
| Git review | No original `notebooks/` or `results/` diff; intended file changes and whitespace checked before publication |

Commands run from the repository root:

```bash
python3 scripts/audit_results.py
python3 scripts/audit_drive_results.py
python3 scripts/verify_repository.py
python3 -m unittest discover -s tests -v
python3 scripts/plot_results.py
python3 scripts/plot_drive_comparison.py
git diff --check
```

Environment: Python 3.12.14, Matplotlib 3.10.8. Public tests/audits use the standard library; plotting uses Matplotlib. Private CSV/config/log files were used for reconciliation. No raw student media, checkpoint, body-model asset, generation API or GPU model was executed or loaded.

## Limits

These checks establish source-file arithmetic, code behavior and preservation, not model replication, clean subject/source splits, checkpoint provenance, identical evaluation crops, statistical significance, privacy protection or classroom deployment. Prediction files lack video/window IDs; notebook environment/path/sampling issues remain documented.

Drive traversal is bounded: raw-frame and third-party dataset/weight subtrees were not exhaustively expanded; the project-materials shortcut target remains inaccessible. Native documents were read as text, not rendered with all embedded media. See docs/SOURCE_INVENTORY.md for coverage.

Mermaid source was checked for two branches and five stages; a live GitHub render was not inspected. Figures were reviewed through renders from the same plotting code. External links were not exhaustively retested. Publisher/manuscript equivalence is unverified.

Pattern-based credential checks are not proof of absence. Source/diff review complements them, and pre-existing benchmark concerns remain recorded separately without silently altering preserved files.
