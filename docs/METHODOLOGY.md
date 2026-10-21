# Methodology and implementation evidence

This document reconstructs the workflow **described in the supplied paper**, not missing source code. References to sections and tables use [P1](../references/README.md). The available implementation evidence is limited to the separate preliminary benchmark notebooks.

## Real data and split boundaries

P1 Tables V–VI list 30 real training videos for each of shaking, swirling, and buretting: 90 in total. Section III-E separately describes a fixed real test set of 21 videos, seven per action. Table V's 330-video total equals 90 real plus 240 synthetic and does not include another 21 test videos in that arithmetic. Whether those test videos were independently held out, selected from the 90, or counted elsewhere cannot be determined without a manifest. Do not claim 351 unique videos or confirmed split separation.

No dataset files, validation split, student/session identifiers, label-to-index mapping, deduplication records, or train/test ancestry manifests were available. Clip duration, frame rate, resolution, crop/resize rules, normalization, and temporal sampling implementation remain unknown. File/folder conventions must be recovered from the original loader rather than invented here.

## Image-based synthesis

P1 Section III-C and Tables II–III describe:

1. Select one representative real video per action and extract its first frame.
2. Apply 60 appearance prompts per action: 20 background, 20 clothing, and 20 hairstyle variants, using Google AI Studio.
3. Animate each edited image with Kling AI and an action-specific prompt.
4. Obtain 60 videos per action (180 overall), with 20 per action allocated to each appearance factor.

The three animation prompts reported in P1 are “He is shaking the flask.”, “He is swirling the flask.”, and “He is filling the burette with liquid.” These are reported prompts, not a recovered prompt manifest. Whether the last phrase matches the complete operational definition of buretting needs annotation/protocol review.

| Item | Evidence/status |
|---|---|
| Frame extraction | Described in P1; extraction script not recovered |
| Appearance editing | External service workflow described; exact model/version, prompts, edit settings, and job records unavailable |
| Animation | External Kling workflow described; model/version, duration, seed, and generation settings unavailable |
| Manual work | P1 Section V-D explicitly describes action-by-action generation and manual prompt design |
| Output organization and quality control | Original folder structure, acceptance criteria, rejected outputs, and review logs unavailable |
| Automated visibility checks | Proposed practical guidance in P1 Section V-C; no implementation established |

P1 provides only example appearance prompts, not all 60. No new prompt collection or synthetic samples are invented for this release. Possible motion/tool artifacts and retention of source identity must be assessed before any release or training use.

## Video-based synthesis

P1 Section III-C and Table IV describe seven selected real videos per action processed by **SynthDa**, yielding reconstructed 3D human meshes. Because inputs show the upper body, lower-body keypoints are estimated from upper-body proportions and fixed to maintain a mesh prior.

Three viewpoints are rendered for each selected source: front, side, and top 45 degrees. This produces 21 candidates per action; one front-view output is randomly excluded to retain **6 front + 7 side + 7 elevated = 20 per action**, or 60 overall. The random seed and source membership are not available.

The equal budget is **per individual factor**: each appearance factor and the camera factor contribute 60 videos overall. The entire image path contributes 180, so the two complete paths have different totals.

Exact pose detection, joint mapping, mesh model, reconstruction optimization, rendering engine, camera coordinates, lighting, textures, and intermediate file formats are not established by the inspected code. Frameworks mentioned in other project discussions cannot be assigned to this exact experiment without provenance. No third-party implementation is copied into this repository.

The paper discusses occlusion, loss of fine tool/hand cues, and reconstruction artifacts as possible reasons for lower accuracy. These explanations are not independently isolated causal effects.

## Action recognition

| Component | What P1 reports | What code must confirm |
|---|---|---|
| Architecture | SlowFast, with slow appearance and fast motion pathways | Backbone depth, pathway packing/temporal ratio, classifier head, implementation and commit |
| Sampling | 16 uniformly sampled frames per clip | Whether 16 refers to one pathway or input before packing; clip duration, stride, padding, duplicates |
| Training | 50 epochs; learning rate 0.001; cross-entropy | Optimizer, batch size, scheduler, weight decay, augmentation, initialization, pretraining, device |
| Validation | Not specified | Validation membership, tuning protocol, early stopping |
| Checkpoints | Not specified | Save criteria, chosen epoch, checkpoint hashes, loading/inference commands |
| Evaluation | Top-1 and per-class accuracy; fixed 21 real test videos | Prediction unit, frame/window selection, aggregation, class counts, weighting, thresholds |
| Repeated runs | No seed/repetition protocol reported | Seeds, repeat count, variability, deterministic settings |

The author has clarified **frame-level accuracy**. A model consuming multiple frames and a metric reported per frame can coexist, but the mapping from temporal model outputs to scored frames must be recovered. Do not equate 16 input frames with 16 independent predictions.

## Combination semantics

Tables V–VI and Section IV-D describe increasing pools of factor-specific clips: camera + clothing, then background, then hairstyle. They do not establish that each generated video underwent every edit simultaneously. Documentation therefore uses **combined factor pools**. Neither additive accuracy gains nor equal-budget causal comparisons follow from this design.
