# Video-based generation and earlier prototypes

The paper describes SynthDa reconstruction of seven selected source videos per action, followed by front, side and top-45-degree renders. Excluding one front view per action gives 6 front + 7 side + 7 elevated = 20 per action (60 total). Exact source selection and final rendering configuration are not linked to a released run manifest.

## Implementation evidence

The private `Documentation/Yufei/Synthda.ipynb` was inspected (29 cells). It clones NVIDIA SynthDa, StridedTransformer-Pose3D, text-to-motion, joints2smpl and SlowFast; installs Blender 3.0.0; stages SMPL assets; runs pose/motion/mesh commands; renders through `animation_pose.py`; and encodes an example at 27 FPS with FFmpeg. It also invokes `components/running.py --pipeline real2synth --weight 0.5 --num-videos 3`. These are exploratory commands, not proof that this exact notebook produced the paper's 60 selected camera clips.

`synthda_loop_noCV.ipynb` was also inspected (155 cells). It contains pose extraction, H36M-to-SMPL mapping calls, motion-length alignment, weighted motion mixtures, joints2smpl fitting, PyRender rendering and FFmpeg assembly. It explores iterative mixture-weight updates and classifier integration. **It contains sample metric generation, TODOs and fall-action examples**, so its sample metrics must not be represented as the laboratory-action paper's results. The final inspected loop uses initial weight 0.5, step 0.1, tolerance 0.001 and maximum 20 iterations; these describe that version only.

Both notebooks depend substantially on [NVIDIA SynthDa](https://github.com/NVIDIA/synthda). Public upstream starting points are [the generation loop](https://github.com/NVIDIA/synthda/blob/main/colab/synthda_loop_noCV.ipynb), [rendering](https://github.com/NVIDIA/synthda/blob/main/components/animation_pose.py) and [pipeline entry point](https://github.com/NVIDIA/synthda/blob/main/components/running.py). They are references to external implementations, not code authored by this repository.

## Earlier reconstruction explorations

Weekly research notes document trials of HybrIK, FrankMocap, VideoPose3D, StridedTransformer, joints2smpl, HuMoR, projection, MotionFix and TailorNet. Notes identify difficulties with half-body inputs, subtle action motion and lower-body completion. Code/model folders were inventoried, but not every exploratory script or model was imported or run. These trials are distinct from the final controlled augmentation comparisons.

Raw mesh/model assets, student media and collaborator modifications remain private or externally licensed. The exact deployed joint mapping, body model variant, camera transforms and source ancestry for the published samples still need a run-level manifest. [Source inventory](../../docs/SOURCE_INVENTORY.md) · [Licenses](../../references/THIRD_PARTY_NOTICES.md).
