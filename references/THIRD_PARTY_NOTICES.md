# Third-party attribution and scope

## Recovered recognition notebook

`action_recognition/notebooks/slowfast_research.ipynb` is derived from the owner's research source and NVIDIA SynthDa. Static AST comparison against the inspected public `colab/synthda_slowfast.ipynb` found **38 matching functions/classes**, four changed definitions and one additional FFmpeg helper. Whitespace/comments are not part of that AST comparison. This is substantial reuse, not an original recognition framework claimed by this repository.

Upstream: [NVIDIA SynthDa](https://github.com/NVIDIA/synthda), [recognition notebook](https://github.com/NVIDIA/synthda/blob/main/colab/synthda_slowfast.ipynb). A complete copy of the inspected [NVIDIA SynthDa NSCL v2 license](licenses/NVIDIA-SynthDa-NSCLv2.md) accompanies the derivative notebook. Its stated use limitation is non-commercial research/evaluation with NVIDIA processors; this is not an unrestricted general-purpose license. Original notebook source contained no separate copyright/attribution notice to remove. A new attribution cell identifies the derivative and the sanitation performed.

The license file's source was the `NVIDIA/synthda` repository, `license (NSCLv2).md`, Git blob `e80732747e9e400300c0366a8737e24bbc323216`, read on 2026-10-21. The source license text is preserved, with trailing whitespace normalized. No repository-wide relicensing is applied to the existing benchmark or unrelated original audit utilities.

## Referenced dependencies and assets

The notebook imports PyTorch, torchvision, PyTorchVideo, fvcore, scikit-learn, OpenCV, NumPy, pandas, TensorBoard, iopath and torchinfo; it invokes FFmpeg. Those packages and pretrained model assets retain their own terms. Their implementations and weight files are not vendored here.

The generation prototypes additionally invoke StridedTransformer-Pose3D, text-to-motion, joints2smpl, SMPL-family assets, Blender and PyRender. Their code/model/dataset permissions must be checked separately before downloading or redistribution; the SynthDa license does not grant universal rights to dependent assets. Collaborator modifications and body-model binaries were not imported.

The original benchmark's acknowledgements and bytes remain unchanged. Its older licensing/provenance issues are recorded in [the benchmark audit](../docs/BENCHMARK_AUDIT.md) and [privacy/release review](../docs/DATA_PRIVACY.md).
