# Methodology and implementation evidence

The study has three evidence layers: the supplied manuscript's intended design, original research source code, and saved data/results. They are reconciled rather than silently merged. See [source register](../references/README.md) and [Drive audit](DRIVE_AUDIT.md).

## Real data and splits

The paper describes 30 real development videos per action (90 total), plus 21 real test videos (seven per action). Its 330-video maximum counts 90 real + 240 synthetic development videos, excluding the separately described test set.

The recovered baseline manifest contains 72 train + 18 validation + 21 test rows. The three appearance manifests contain 120 train + 30 validation + 21 test rows each. The source implements an 80/20 stratified development split with seed 297; model randomness is separately seeded 17. Test membership is appended from its own directory.

Camera-related historical manifests have larger development pools than the paper's design. Four class+basename collisions occur between test and development in each distinct manifest. These do not prove identical content, but source/subject separation cannot be assumed. Source filenames and paths remain private; [aggregate counts](../experiments/recovered/dataset_summary.csv) are published.

## Image-based synthesis

The paper describes taking the first frame from one representative real video per action, editing appearance with Google AI Studio, then animating with Kling. Each action receives 20 background, 20 clothing and 20 hairstyle videos: 180 across three actions. Research procedures and folder metadata corroborate this organization; exact generation jobs and QC/ancestry manifests were not recovered.

The reported action prompts are “He is shaking the flask.”, “He is swirling the flask.”, and “He is filling the burette with liquid.” They are not a full prompt inventory. Human-selected prompts and commercial-service settings remain manual/external components. [Image workflow](../pipelines/image_based/README.md).

## Video-based synthesis

The paper describes seven source videos per action processed by SynthDa, estimated/fixed lower-body joints for upper-body inputs, and three viewpoints. After removing one front render per action, 6 front + 7 side + 7 top-45-degree views give 20 per action and 60 total.

Recovered exploratory notebooks invoke StridedTransformer-Pose3D, joints2smpl, Blender and PyRender through SynthDa-related workflows. Research notes also describe alternative generation-before-reconstruction trials. They establish actual integration work, but do not identify the exact code revision and inputs for every selected paper clip. [Video workflow and prototype boundaries](../pipelines/video_based/README.md).

Camera changes can co-occur with geometry, texture, hand/tool and motion artifacts. The paper's occlusion/reconstruction explanations are hypotheses; no causal ablation isolates them.

## Recognition and evaluation

The recovered model factory selects pretrained PyTorchVideo SlowFast R50, replaces its classifier for three actions, freezes non-projection parameters, and uses Adam with learning rate 0.001 and cross-entropy. Batch size is 1; the configured epoch count is 50. The implementation uses **32 fast-path and 8 slow-path frames**, unlike the paper's 16-frame description. Exact preprocessing, cell references, checkpoint selection and known issues are in the [implementation guide](../action_recognition/README.md).

The same random spatial transforms are applied at test time. Test videos are uniformly windowed with a tail-skipping stopping rule. One clip prediction is repeated over its sampled frame labels. Eight recovered exports each contain 2,880 scored rows (544/928/1,408 by class), equivalent in rate to 90 equal-size prediction blocks. These are not independent frame predictions and not equally weighted source-video accuracy.

Saved argument files and CSVs corroborate several details, but a full execution environment, stable source/checkpoint binding and prediction-to-video mapping remain missing. All numerical recomputation in this update uses stored exports; no model is trained or rerun.

## Combination semantics

The paper combines factor-specific pools rather than establishing that every synthetic clip received all edits. Its combinations add 120, 180 and 240 synthetic videos in total. These are unequal budgets; changes cannot be attributed purely to interaction between factors. Historical manifests and multiple run versions must be considered separately.
