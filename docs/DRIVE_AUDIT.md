# Drive evidence and paper reconciliation

Audit date: 2026-10-21. Drive access is now available. This supersedes the initial documentation-only audit's access blocker. Results below are **recomputed from saved CSVs**, not new training or checkpoint inference. Source locations and SHA-256 values are recorded in [drive_evidence.json](../references/drive_evidence.json).

## Recovered results

| Experiment | Paper Top-1 (%) | Saved predictions Top-1 (%) | Comparison |
|---|---:|---:|---|
| Real only | 77.78 | 77.78 | Matches |
| Camera angle | 57.78 | 48.89 | Different record |
| Clothing | 93.33 | 93.33 | Matches |
| Background | 88.89 | 88.89 | Matches |
| Hairstyle | 95.56 | 95.56 | Matches |
| Camera + Clothing | 53.33 | 80.00 | Different record |
| Camera + Clothing + Background | 91.11 | 91.11 / 68.89 | Two versions |
| Camera + Clothing + Background + Hairstyle | 81.11 | — | Prediction export not recovered |

The five matching conditions also match all three paper-reported per-class percentages. Matching numbers corroborate the reported aggregate; they do not establish clean splits, deterministic evaluation, or exact checkpoint lineage.

| Source condition / run directory | Correct scored rows | Total rows | Saved Top-1 (%) |
|---|---:|---:|---:|
| baseline / 10-12-2025-07-55-58 | 2240 | 2880 | 77.78 |
| camera_angle / undated model_evaluation | 1408 | 2880 | 48.89 |
| clothes / 10-13-2025-07-13-54 | 2688 | 2880 | 93.33 |
| background / 10-12-2025-17-19-15 | 2560 | 2880 | 88.89 |
| hairstyle / 10-13-2025-18-36-40 | 2752 | 2880 | 95.56 |
| camera_clothes / 10-15-2025-07-10-07 | 2304 | 2880 | 80.00 |
| camera_clothes_background / 10-21-2025-16-01-50 | 2624 | 2880 | 91.11 |
| camera_clothes_background2 / 10-15-2025-21-08-53 | 1984 | 2880 | 68.89 |

The `camera_clothes_background2` argument file still names paths without the `2` suffix. The current notebook's stored output also shows 68.89% and an October 15 checkpoint. These are evidence of historical versions; they are not grounds for replacing the paper's 91.11% with 68.89%.

The four-factor directory (spelled `camera_clothes_background_hairsytle` in Drive) contains arguments, a TensorBoard event file and three weights, but its `model_evaluation` folder is empty. The 81.11% paper row remains uncorroborated by a prediction export. The missing 57.78% camera and 53.33% two-factor records must likewise remain distinct from the recovered alternatives.

## What “frame-based accuracy” means here

All eight CSVs contain the same class totals: **544 shaking, 928 swirling, 1,408 buretting**, totaling 2,880 rows. Every 32 consecutive rows share a label and prediction; all stored correct/incorrect flags agree with direct label comparison. The resulting per-class and overall rates also reconcile with the adjacent `class_accuracy_test.csv` and `top1_accuracy_test.csv`.

The recovered code produces a clip-level class prediction and repeats it across 32 sampled frame labels. Dividing the counts by 32 gives **17, 29 and 44 clips**, totaling 90. This resolves the earlier numerical denominator hypothesis for the recovered records. It does not prove the missing paper runs used the identical evaluator or establish 2,880 independent observations.

Six recovered test-annotation files each contain 3,285 frame annotations from 21 videos. Applying the source uniform sampler's stopping rule reproduces 544/928/1,408 scored rows. The 405-row difference comes from its unscored tails; at exact frame-count multiples its stopping condition can omit a full final block. See [source-level details](../action_recognition/README.md).

## Dataset versions and separation

These are counts in **current directory manifests**, not automatically the data used by every adjacent checkpoint:

| Directory | Train | Validation | Test | Development pool | Paper's intended pool |
|---|---:|---:|---:|---:|---:|
| baseline | 72 | 18 | 21 | 90 | 90 |
| clothes | 120 | 30 | 21 | 150 | 150 |
| background | 120 | 30 | 21 | 150 | 150 |
| hairstyle | 120 | 30 | 21 | 150 | 150 |
| camera_angle | 216 | 54 | 21 | 270 | 150 |
| camera_clothes | 264 | 66 | 21 | 330 | 210 |
| camera_clothes_background2 | 312 | 78 | 21 | 390 | 270 |

The camera directory has two `video_info.csv` files with the same hash; these are one distinct manifest. The later October 21 three-factor and four-factor configurations reference separate personal-Drive data paths that were not recovered from this shared folder. Their exact development memberships remain unknown.

All seven distinct manifests use seven test videos per class and the same set of class+test-basename pairs. Every manifest has **four class+basename collisions between test and train/validation**. Train/validation basename sets are disjoint. Basename collisions are a leakage warning, not proof of byte-identical footage; no media hashes, subject/session groups or synthetic-parent mapping were recovered. Private paths and filenames are withheld. The [aggregate manifest summary](../experiments/recovered/dataset_summary.csv) records the collision counts.

## Configuration and training-record limits

The ten argument files specify SlowFast, 32 frames, three classes, batch 1, 50 epochs, learning rate 0.001, frozen body parameters and seed 17. The inspected model factory uses pretrained PyTorchVideo SlowFast R50 and Adam. The paper's 16-frame statement differs from the code/configs' 32 fast + 8 slow frames.

Thirteen small TensorBoard files were read for stored scalar fields. The primary baseline stream contains 47 validation steps (0–46), clothing 37 (0–36), and four-factor 43 (0–42); background, hairstyle, two-factor and both three-factor runs have streams reaching step 49. A 50-epoch setting is therefore not proof that every recovered stream records 50 completed epochs. Restarts/partial streams must not be counted as independent random-seed repetitions. No conclusion about why a stream ends is asserted.

No saved event file here proves which weights produced a particular prediction CSV. Current notebook paths conflict, evaluation applies random crop/scale/flip, and prediction rows omit video/window IDs. These limitations prevent a claim that all experiments had identical realized evaluation conditions.

## Public evidence and rerunning this audit

- [results.csv](../experiments/recovered/results.csv): eight source-versioned results and per-class rates.
- [confusion_counts.csv](../experiments/recovered/confusion_counts.csv): nine aggregate class/prediction counts per run; no student, source-video or frame identifiers.
- [recovered configurations](../action_recognition/configs/recovered_configs.json): numeric/model settings only.
- [provenance hashes](../references/drive_evidence.json): originals can be checked privately without releasing paths to student media.

Run `python3 scripts/audit_drive_results.py` to reproduce released aggregates. The optional `--predictions` mode verifies an authorized original export, checks uniform 32-row blocks and reports its SHA-256. This utility is newly written audit tooling, not the original training pipeline.
