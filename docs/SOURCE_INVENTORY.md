# Source inventory and integration decisions

Audit date: 2026-10-21. Original repository base: `dd16e40f6828803cf3d13bffc4f3fe48c473cabf`. The earlier Drive connection blocker is resolved. This inventory distinguishes content read, directory metadata, and uninspected material.

## Coverage

The shared root and research subdirectories were traversed to locate implementation, configurations, manifests, logs and results. The bounded inventory contains **5,417 observed items** and **365 listed folders**. Raw-frame subtrees, third-party dataset/weight subtrees and other media assets were not exhaustively expanded or content-inspected (**1,786 observed asset folders remain unexpanded**). This is not a claim to have read every file in the shared drive.

The `NVAITC-NIE SDG Project Materials` entry is a shortcut. Its target could not be fetched (403), and an exact-name folder search returned no accessible target. Its contents remain uninspected. Native Google Docs were read as text; embedded images and visual tables were not fully extracted. Large model archives and student media were not downloaded.

No private root URL, Drive file ID, student-media filename, participant list or internal document body is published. Duplicate folder names were tracked by Drive ID during the private inventory so that empty/nonempty baseline folders were not conflated.

## Content-level sources

| Source / original location | Type / purpose | Evidence and duplication | Publication decision | Destination |
|---|---|---|---|---|
| Original README, five `notebooks/*.ipynb`, `results/video.md` | Existing benchmark | Full static source/output audit; already tracked | Preserve bytes and original README block | Original paths |
| Supplied nine-page paper (P1) | Manuscript | Methods, tables, figures; not an execution log | Summarize; withhold PDF and identifiable examples | Research docs and paper CSV/charts |
| `Experiment/slowfast.ipynb` | 97-cell research notebook | Actual three-class source and saved outputs; new to this repo; 38 function/class definitions match public SynthDa ASTs | Strip outputs/user metadata/private path roots; retain research logic and license | `action_recognition/notebooks/slowfast_research.ipynb` |
| `Documentation/Yufei/action recognition/slowfast.ipynb` | Earlier 90-cell notebook | Separate exploratory version; inspected settings use two classes and one epoch | Reference as earlier work; do not merge settings with three-class experiments | Inventory / version boundary |
| `Documentation/Yufei/Synthda.ipynb` | 29-cell notebook | Actual framework setup, reconstruction/rendering commands and sample integration | Reference; do not copy asset links or private output | Video-generation guide |
| `Documentation/Yufei/synthda_loop_noCV.ipynb` | 155-cell notebook | Generation/optimization prototype, sample metrics, fall examples and TODOs | Reference; no claim of completed laboratory optimization result | Video-generation guide |
| `Experiment/action recognition/**/predictions_test.csv` | Eight CSV exports | All 23,040 scored rows compared; no video/window IDs; no duplicate result versions collapsed | Release aggregate class/prediction counts only | `experiments/recovered/` |
| Adjacent `class_accuracy_test.csv`, `top1_accuracy_test.csv`, `confusion_test.csv` | Summary CSVs | Eight class and Top-1 reports reconcile with prediction-derived values; confusion files inspected | Release derived aggregates with hashes | Result audit / provenance |
| `Experiment/action recognition/**/args.json` | Ten JSON files | Saved numeric/model settings; camera's undated evaluation lacks adjacent arguments | Remove all private paths | `action_recognition/configs/recovered_configs.json` |
| `Experiment/action recognition/*/training_data/video_info.csv` | Eight files, seven distinct hashes | Current memberships/counts; camera duplicate files are byte-identical; not unique-media proof | Aggregate fold counts and basename-collision totals only | `dataset_summary.csv` |
| Six `test.tsv` and six `test_predicted_boxes.csv` files | Frame lists / annotations | 21 videos and 3,285 frame labels per annotation file; source sampler arithmetic gives 2,880 scored rows | Original paths/IDs withheld | Evaluation audit |
| `Experiment/action recognition/**/logs/events.out.*` | Thirteen TensorBoard files | Stored scalar fields and validation-step coverage; restarts/partial logs exist | Coverage summary only; host/file names withheld | `training_log_summary.csv` |
| Research Journal and Yufei Weekly Updates | Native Docs | Text read; chronology of reconstruction trials and limitations; image examples not reproduced | Technical summary only | Pipeline and overview docs |
| Experiments Procedure and Plan for IEEE PacificViz | Native Doc | Text/table values read; matches paper aggregate table but contains older 20-video/two-class wording | Source cross-check only; original internal document withheld | Methods / discrepancy audit |
| Forms data-management document | Word template/plan | Relevant ownership/access/sharing sections read; not proof of signed participant release | Withhold original | Privacy decision |
| SDG Ethics research document | Native Doc | Relevant consent, secondary-use and re-identification questions read; not completed privacy validation | Withhold original and research/interview material | Privacy decision |
| NVIDIA SynthDa license and two public notebooks | Public upstream sources | License terms read; function/class provenance compared; upstream loop is not identical to local extended notebook | License copy + attribution; upstream links | `references/`, model/pipeline guides |

The exact 63 numeric/config/manifest source files are listed with hashes and source locations in [drive_evidence.json](../references/drive_evidence.json). Sources have not been inferred from paper values. The [notebook transformation manifest](../references/recovered_notebook_integrity.json) records every original/published cell hash. Original benchmark hashes remain in [benchmark_integrity.json](../references/benchmark_integrity.json).

## Metadata-only and release-review material

| Area | Observed material | Review/publication decision |
|---|---|---|
| Documentation reconstruction folders | MotionFix, TailorNet, Projection, VideoPose3D, StridedTransformer, HuMoR, joints2smpl notebooks, scripts, outputs and model assets | Inventoried; most source contents not audited. Do not assign these exact versions to final paper runs without lineage |
| Collaborator modifications | Animation, fitting, plotting and TailorNet scripts | No copying without file-level provenance/license review |
| Experiment media | Action/factor folders, raw videos, generated images/videos, extracted frames | Metadata only; no public media release |
| Checkpoint folders | Saved accuracy/loss/F1 weight files, including four-factor run | Metadata only; binaries not loaded or published; no checkpoint hashes claimed |
| Papers | Related synthetic-human-action framework PDF | Metadata only; not copied or treated as this paper's implementation evidence |
| Forms and SDG Ethics | Consent/recruitment material, internal proposals, journals, literature, interview materials | Originals private; participant/candidate lists not content-inspected |
| Project Materials shortcut | Inaccessible target | Explicit unresolved coverage gap |

## Source-to-addition mapping

The paper supplies the intended design and immutable paper table. The three-class notebook supplies the recovered implementation. Prediction/summary exports supply recomputed numerical aggregates. Manifests and configs supply actual version differences. Logs supply recorded validation-step coverage only. Journals and prototype notebooks supply the generation history. New audit/plot/test scripts are authored for this repository update, not represented as recovered research code.
