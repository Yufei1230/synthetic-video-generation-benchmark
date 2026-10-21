# Reproducibility

## What can be reproduced now?

| Component | Status | Scope |
|---|---|---|
| Result transcription and arithmetic audit | Executed locally | Reads paper-derived CSV, checks budgets, computes deltas and denominator compatibility |
| Result charts | Executed locally | Matplotlib export from the CSV, with paper-reported labels |
| Preservation / link checks and utility tests | Executed locally; see validation record | Protects original benchmark and documentation consistency |
| Historical benchmark notebooks | Present, statically inspected, not rerun | Require Colab/CUDA, downloads, and their own dependencies |
| Google AI Studio / Kling research generation | Paper description only; external services/manual prompt work | Exact versions, prompts, jobs and accepted outputs missing |
| SynthDa reconstruction / rendering | Paper description only | Original scripts, model assets, licenses and renderer config missing |
| SlowFast training / inference / metric evaluation | Missing implementation | No training, inference, or experimental reproduction claimed |

## Documentation environment

Tested with Python 3.12.14 and Matplotlib 3.10.8. The arithmetic, integrity checks and unit tests use only the Python standard library and target Python 3.10+. `requirements-docs.txt` pins the charting library tested here; it is **not** the environment for the research models.

From the repository root:

```bash
python3 scripts/audit_results.py
python3 scripts/verify_repository.py
python3 -m unittest discover -s tests -v
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-docs.txt
python3 scripts/plot_results.py
```

On Windows, activate with `.venv\Scripts\Activate.ps1` and use `python` if `python3` is unavailable. Plotting overwrites only the two documented SVG figures. SVG timestamps are suppressed, with stable SVG IDs in the tested Matplotlib environment.

These commands do not require school data, GPU access, model downloads, or service keys. They do not validate the model's accuracy. [Validation record](VALIDATION.md).

## Historical notebook execution cautions

See the [cell-specific notebook audit](BENCHMARK_AUDIT.md). Each notebook is its own exploratory environment; do not install all notebooks' requirements into one environment. In particular, the Vid2Vid Python 3.6 / torch 1.0 / CUDA 10 wheel is a historical dependency, not a modern installation instruction. External repositories and unpinned packages may have changed since the stored runs.

Do not execute a notebook automatically simply because its JSON is valid. Review mounts, downloads, third-party terms, retained notebook outputs, paths and GPU requirements first. No claim is made that current services reproduce the original generations.

## Missing inputs required for actual research reproduction

| Priority | Material | What it establishes |
|---|---|---|
| 1 | Evaluation source plus prediction export containing source video ID, frame/time or window ID, true label, predicted label and run ID | Frame-level metric, denominator, aggregation and per-class weighting |
| 1 | Training/test/validation membership and synthetic parent-source manifests | Unique videos, source reuse and leakage boundaries |
| 1 | Original SlowFast source/configs and checkpoint hashes | Model identity, loader/transforms, optimizer, batch size, schedule, selection and inference |
| 2 | Per-condition logs and random seeds | Run-to-table correspondence and repeatability |
| 2 | Complete prompt manifest and accepted/rejected generation records | Generation settings, service/model versions, QC and source lineage |
| 2 | SynthDa integration scripts, environment, reconstruction and camera settings | Exact human/pose pipeline and renderer |
| 3 | Dataset/asset sharing permissions and third-party licenses | What may be released or redistributed |

A sanitized code/log export is sufficient to continue many checks; raw student videos need not be uploaded publicly. Paths, credentials, student identifiers and signed links should be reviewed before an export is committed.

## Recovery procedure

Retain original scripts and names when feasible. Record source file hashes and ownership; map configs/logs/checkpoints to experiments; document original commands; then run small utilities or mock-based tests where meaningful. Keep historical results separate if they disagree with the supplied manuscript. GPU model retraining is outside this documentation update.
