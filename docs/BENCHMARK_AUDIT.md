# Preserved benchmark: source-level audit

Inspected base commit: `dd16e40f6828803cf3d13bffc4f3fe48c473cabf` on `main`. The full cloned history contains 19 commits, from the initial commit on 2026-06-02 through the README correction on 2026-06-08. The source tree contains five notebooks, the README and a one-newline results file; no recognizer, configs, checkpoints or model evaluation logs are present. No repository AGENTS.md or LICENSE file was found.

Cell indices below are **zero based**, matching each notebook's `cells` array. Stored output is historical evidence, not proof of execution during this audit. All original notebook bytes and `results/video.md` are preserved, checked by the [integrity manifest](../references/benchmark_integrity.json).

| Notebook | Contents actually found | Important limits |
|---|---|---|
| [CogVideoX](../notebooks/CogVideoX.ipynb) (24 cells) | `THUDM/CogVideoX-5b-I2V` (10); float16 transformer/T5/VAE (11–12); sequential CPU offload (14); uploaded image and swirling prompt (16–18); guidance 6 and 50 steps (19); export at 8 FPS (20) | `accelerate==0.33.0` is pinned but main installs are not; output says upload saved as `image (1).jpeg` while code opens `image.jpeg`; identity/resolution and outputs are not independently validated |
| [DynamiCrafter](../notebooks/DynamiCraft.ipynb) (21 cells) | Upstream clone, 512 model download, run script/Gradio (2–10); WebVid loader and upstream training command (13–18); alternate `camenduru/DynamiCrafter-hf` dev application (20) | Stored output includes a killed inference process, training SIGKILL, and a 404 for a sample image; exact causes were not reproduced |
| [Text2Video](../notebooks/Text2Video.ipynb) (13 cells) | CLIP ViT-B/32 and ViT-B/16 (2); CycleGAN model setup and external weights (5); latent optimization across prompts (6–9); generic car/frog examples (11–12) | Not verified as Picsart Text2Video-Zero; contains external download and provenance/licensing concerns, including token-like URL material in cell 5 |
| [First Order Motion Model](../notebooks/first_order_model.ipynb) (2 cells) | Clones upstream plus `graphemecluster/first-order-model-demo` (0); interactive image/driving-video selection, model checkpoints, `make_animation`, 256×256 preprocessing and video output (1) | Demo dependency and upstream revisions unpinned; no stored execution evidence; reads external assets |
| [Vid2Vid](../notebooks/vid2vid.ipynb) (11 cells) | NVIDIA vid2vid clone; dataset/FlowNet/model downloads; old torch/torchvision installation; `label2city_2048` inference command | Generic street-scene demo, not a recovered laboratory-action model; legacy Python/CUDA constraints; no stored outputs |

## Evidence boundaries

The original comparison table is qualitative and retained verbatim in the main README. Its categories, claims and links are historical notes, not newly benchmarked or scientifically standardized comparisons. No common hardware, generation budget, visual-quality scores, timing measurements, or matched task prompts were recovered across the notebooks.

The presence of inference code or a stored output does not prove that a corresponding clip is available for public redistribution. `results/video.md` currently contains only a newline. No representative clips are introduced in this update.

## Third-party attribution

The original README acknowledges Text2Video-Zero, CogVideo, First Order Motion Model, VideoCrafter, DynamiCrafter and Vid2Vid. These acknowledgements are preserved. The notebooks also reference the First Order Model demo, a DynamiCrafter community application, CLIP, CycleGAN/pix2pix and STROTSS-derived distance code. They should be included in any future provenance/license review.

This audit does not grant new licenses to inherited content. No third-party implementation has been newly copied, and no repository-wide license has been imposed without owner review.
