# Recovered experiment evidence

These are audit derivatives of original Drive records, kept separate from [paper-reported results](../paper_reported_results.csv). No model inference was rerun.

| File | Contents |
|---|---|
| [results.csv](results.csv) | Eight source-versioned prediction-export summaries; per-class and overall rates |
| [confusion_counts.csv](confusion_counts.csv) | Aggregate ground-truth/prediction counts, nine cells per run |
| [dataset_summary.csv](dataset_summary.csv) | Seven distinct current video-manifest counts and basename collision totals |
| [training_log_summary.csv](training_log_summary.csv) | Validation-step coverage in thirteen stored event files; not checkpoint provenance |

`recomputed_from_saved_predictions` means that the saved labels/predictions were compared and counted. It does not mean the source footage was inspected, a model was rerun, or the test split was proven clean. No student/video/frame identifiers or raw media are released. Hashes refer to the original private files in [the evidence register](../../references/drive_evidence.json).

Each prediction export has 2,880 scored rows, with one clip prediction repeated across each 32-row block. Both conflicting three-factor versions are retained. No result row is invented for the four-factor experiment whose evaluation directory is empty.

Run `python3 scripts/audit_drive_results.py` from the repository root. [Detailed interpretation](../../docs/DRIVE_AUDIT.md).
