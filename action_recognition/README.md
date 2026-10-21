# Recovered action-recognition implementation

[slowfast_research.ipynb](notebooks/slowfast_research.ipynb) is a sanitized archival copy of `Experiment/slowfast.ipynb`. It contains the actual loader, model, training and evaluation code. It was **statically inspected, not executed end to end**. Research logic and known defects are retained rather than silently modernized.

The original has 97 cells; the release adds one explanatory cell. References below are **original zero-based cell numbers**; add one for the released notebook. [Transformation and hashes](../references/recovered_notebook_integrity.json).

## Model and configuration

| Component | Recovered implementation |
|---|---|
| Backbone | `pytorchvideo.models.hub.slowfast_r50(pretrained=True)`; saved output names `SLOWFAST_8x8_R50.pyth` (26, 76) |
| Head | Replace `blocks[6].proj` with a linear layer for three classes (26) |
| Class mapping | 0 shaking, 1 swirling, 2 buretting (43 and saved class reports) |
| Freezing | Parameters whose names do not contain `proj` get `requires_grad=False` (25); training mode can still update batch-normalization running statistics |
| Temporal input | 32 fast-path frames, 8 slow-path frames; alpha 4 (22, 38). The paper says 16 frames |
| Input size | Random short side 256–320, random 244-square crop, horizontal flip probability 0.5 (22, 32, 38) |
| Normalization | Divide pixels by 255; mean `[0.45]*3`, standard deviation `[0.225]*3` (22, 38) |
| Optimizer / loss | Adam, learning rate 0.001; cross-entropy with the first sampled frame label, one-hot encoded (28, 76) |
| Batch / workers | Batch size 1; workers 0 (38); loss and prediction repetition assume this batch size |
| Epoch setting | 50 (38 and ten saved argument files); stored event streams do not all reach 50 logged validation steps |
| Seeds | Python, NumPy, Torch seeded 17 (39); stratified train/validation split uses a separate fixed seed 297 (10) |
| Checkpoints | Save best validation loss, accuracy and macro-F1 separately; ties overwrite the prior file (31) |

Ten [saved configurations](configs/recovered_configs.json) retain observed numeric/model settings and omit private paths. No `args.json` was found alongside the undated camera evaluation. Do not assign another condition's config to that record.

## Data flow and expected layout

The source paths were mapped to `/content/research_data/action_recognition`. This is a redaction, not a supplied dataset. For a chosen condition, source cells expect:

- `raw_data/<action>/*`: development videos.
- A shared `test_data/<action>/*`: held-out video directory used by cell 51.
- `training_data/video_info.csv`: video metadata, class and fold.
- `training_data/frames/<vid_id>/<frame_id>.jpg`: extracted frames.
- `training_data/frame_lists/{train,val,test}.tsv`: headerless video ID, frame ID and relative image path.
- `training_data/annotations/{train,val,test}_predicted_boxes.csv`: despite the filename, this code writes class labels and timestamps, not detected boxes.
- `training_data/annotations/action_list.pbtxt`: label map.
- `checkpoint/<run>/saved_models/`, `logs/`, `model_evaluation/`: outputs.

Cell 47 splits the development pool 80/20 with class stratification, then cell 51 appends the separate test directory. The recovered manifests all have 21 test rows, seven per class. They also have four class+basename collisions between test and development; matching names alone cannot establish identical video content. A subject/session and media-hash audit is still needed.

Frame extraction (11) invokes FFmpeg with CUDA decoding and `fps=30`, while annotation timestamps (13) use the source video's recorded FPS. This can misrepresent timing when source FPS differs. FFmpeg return codes are not checked and existing frame directories are not cleared; stale frames can survive re-extraction.

## Clip sampling and metrics

Training requests five random clips per source video. Validation/test use the uniform sampler in cell 14. Its stop condition `clip_end + CLIP_DURATION >= number_of_frames` omits the remaining tail; at an exact multiple of 32 it also skips the final complete block. For example, a 128-frame input yields three clips, while the `num_clips` property reports four. Tests preserve and demonstrate this behavior; it has not been repaired in the archival source.

Cell 22 uses the **same random spatial transforms for training, validation and test**. Cell 24 also selects videos with `RandomSampler` for all folds. Consequently, equal source-video membership does not establish identical evaluation crops or repeated-run reproducibility.

Cells 28 and 33 yield one class prediction per clip, then repeat it to match the sampled frame labels. The eight saved exports each have 2,880 rows arranged in 90 uniform 32-row blocks. Their class totals are 544, 928 and 1,408. Replaying only the pure uniform-sampler arithmetic on six recovered annotation files (3,285 frames across 21 videos) reproduces those totals. No image decoding or model inference was performed.

The predictions do not contain video/window IDs, so a particular correct/incorrect block cannot be assigned back to a student or video. With constant labels and equal block lengths, the scored-row rate also equals the rate over these 90 blocks; neither is the equally weighted accuracy across 21 source videos.

## Known execution and provenance issues

1. Cell 3 pins Torch 1.11.0+cu113, torchvision 0.12.0+cu113, torchaudio 0.11.0, PyTorchVideo 0.1.5, fvcore 0.1.5.post20221221 and setuptools 59.5.0. The stored output shows the Torch wheel installation failed under Python 3.12. These are historical attempted pins, not a validated environment lock.
2. Cells 37, 78, 79 and 89 point to different condition/output/checkpoint locations. Running all cells can evaluate one checkpoint and write to another condition. Choose and reconcile all paths explicitly before any run; the historical mismatch remains visible.
3. `temporal_subsample` and transform helpers are redefined in cell 32. Sequential execution uses the later definitions. Non-SlowFast branches have different tuple expectations in the collator and were not validated.
4. The notebook adds an `Overall` row to class counts, then cell 94 sums all rows, doubling numerator and denominator. The accuracy ratio is unchanged, but those summed values must not be reported as the real scored-row count.
5. Saved weights were inventoried but not downloaded or loaded. A mutable notebook and adjacent CSV are not a cryptographically proven run/checkpoint pairing.

## How to continue the research

For a historical read-through, open the notebook and follow preparation → loaders → model → training → evaluation. For an actual run, first create an isolated compatible GPU environment, obtain authorized data/model assets, reconcile the paths above, and audit split ancestry. Save all fixes in a new experimental version and export prediction video/window IDs. Do not overwrite these historical results with repaired-run metrics.

The public repository can already verify saved aggregates without model dependencies:

```bash
python3 scripts/audit_drive_results.py
# Optional: verify an authorized private export without publishing it.
python3 scripts/audit_drive_results.py --predictions /path/to/predictions_test.csv
```

The original helper code has substantial overlap with NVIDIA SynthDa's public notebook. [Attribution and license](../references/THIRD_PARTY_NOTICES.md) are part of this release.
