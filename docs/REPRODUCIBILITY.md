# Reproducibility

| Component | Status | Boundary |
|---|---|---|
| Paper table arithmetic and charts | Executed locally | Preserves the manuscript's values and intended budgets |
| Eight prediction exports | Recomputed locally | All result flags, class totals and adjacent summary rates reconcile; no inference rerun |
| Dataset manifest and sampler arithmetic | Audited locally | Seven distinct manifests; six test-annotation files reproduce scored-row counts; no media deduplication |
| Recovered SlowFast source | Present, statically inspected | Actual research logic retained with known issues; no end-to-end run |
| Saved settings and training logs | Read | Ten argument files, thirteen event files; incomplete checkpoint/source binding |
| Historical generation benchmark | Preserved, statically inspected | Not rerun; external/legacy dependencies remain |
| Image generation | Manual external-service workflow | Complete prompts, exact service versions and job records unavailable |
| SynthDa integrations | Original notebooks inspected and upstream referenced | Dependencies/model assets and final rendering lineage incomplete |

## Run the public checks

Python 3.10+; tested with Python 3.12.14. Audit and unit-test code uses only the standard library.

```bash
python3 scripts/audit_results.py
python3 scripts/audit_drive_results.py
python3 scripts/verify_repository.py
python3 -m unittest discover -s tests -v
```

To inspect an authorized private prediction export without publishing it:

```bash
python3 scripts/audit_drive_results.py --predictions /path/to/predictions_test.csv
```

This checks class values, correct/incorrect flags, complete uniform 32-row blocks and a SHA-256 fingerprint. Output is aggregate only.

For charts, create an isolated environment and install the tested Matplotlib version:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-docs.txt
python3 scripts/plot_results.py
python3 scripts/plot_drive_comparison.py
```

Windows activation is `.venv\Scripts\Activate.ps1`. Plot scripts overwrite only the documented SVGs; they do not access private data or a model.

## Research execution

Read the [recovered notebook guide](../action_recognition/README.md) for historical pins, directory conventions, cell references, required assets and the actual training/evaluation sequence. The old Torch wheel install failed in stored Python 3.12 output; there is no validated research-environment lock. Path conflicts and random test transforms must be addressed in a new run version before executing the whole workflow. The release does not silently fix the original evaluator and then attribute new behavior to old results.

Original benchmark environments are separate; see [their audit](BENCHMARK_AUDIT.md). External repositories and services may differ from the versions used historically.

## Remaining requirements for experimental replication

1. Resolve development/test basename collisions with authorized media hashes, subject/session grouping and synthetic-parent mappings.
2. Recover missing camera (57.78%), two-factor (53.33%) and four-factor (81.11%) prediction/run records; identify final data memberships for the October 21 runs.
3. Bind source revision, dependency lock, configuration, selected checkpoint hash and predictions with video/window IDs to each run.
4. Record deterministic evaluation transforms and repeat seeds in a new experiment version; do not treat restarted logs as independent repetitions.
5. Recover generation-service job settings, accepted/rejected samples, source ancestry and exact SynthDa camera/mesh configuration.
6. Review data/asset release permissions independently of research access.

No GPU retraining, checkpoint loading or synthetic video generation was performed in this repository update. [Validation record](VALIDATION.md).
