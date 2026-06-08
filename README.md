# Synthetic Video Generation Benchmark

A qualitative comparison of synthetic video generation techniques, covering Text-to-Video models, Generative AI LLMs, First Order Motion Models, Diffusion Models, and Video-to-Video translation methods.

---

## Overview

This repository documents hands-on experiments with various synthetic video generation tools and models. Some models were tested online like Kling, Ying, Vidu, and Jimeng; other tools were explored through Colab notebooks included in this repo.

The goal is to provide a practical reference for researchers and practitioners choosing between synthetic video generation approaches.

---

## Techniques Compared

| Type | Technique | Advantages | Limitations |
|------|-----------|------------|-------------|
| Text-to-Video Models | [Text2Video-Zero](https://github.com/Picsart-AI-Research/Text2Video-Zero) | Fast, highly flexible and customized, high quality | Requires detailed and accurate text input |
| | [CogVideo](https://github.com/THUDM/CogVideo) | Fast, highly flexible and customized, high quality | Requires detailed and accurate text input |
| Gen AI LLMs | [Kuaishou's Kling](https://kling.kuaishou.com) | High quality, highly customizable, very mature | Can be costly |
| | [Zhipu AI's Ying](https://ying.zhipuai.cn) | High quality, highly customizable, very mature | Can be costly |
| | [Shengshu AI's Vidu](https://www.vidu.studio) | High quality, highly customizable, very mature | Can be costly |
| | [Jimeng AI](https://jimeng.jianying.com) | High quality, highly customizable, very mature | Can be costly |
| First Order Motion Models | [First Order Model](https://github.com/AliaksandrSiarohin/first-order-model) | Good for generating motion from static images, relatively simple | Limited to single-image input and simple scenes |
| Diffusion Models | [VideoCrafter](https://github.com/AILab-CVC/VideoCrafter) | High quality, fast | Computationally intensive, requires substantial data |
| | [DynamiCrafter](https://github.com/Doubiiu/DynamiCrafter) | High quality, fast | Computationally intensive, requires substantial data |
| Video-to-Video Translation | [Vid2Vid](https://github.com/NVIDIA/vid2vid) | Effective for video-to-video translation | Requires high-quality input for best results, complex setup |

---

## Repository Structure

```
synthetic-video-generation-benchmark/
├── README.md
├── notebooks/
   ├── cogvideox.ipynb
   ├── dynamicrafter.ipynb
   ├── vid2vid.ipynb
   ├── text2video.ipynb
   └── first_order_model.ipynb

```
---
## Acknowledgements

This project references and builds upon the following open-source works:

- [Text2Video-Zero](https://github.com/Picsart-AI-Research/Text2Video-Zero) by Picsart AI Research
- [CogVideo](https://github.com/THUDM/CogVideo) by THUDM
- [First Order Motion Model](https://github.com/AliaksandrSiarohin/first-order-model) by Aliaksandr Siarohin et al.
- [VideoCrafter](https://github.com/AILab-CVC/VideoCrafter) by AILab-CVC (Tencent)
- [DynamiCrafter](https://github.com/Doubiiu/DynamiCrafter) by Doubiiu et al. (ECCV 2024 Oral)
- [Vid2Vid](https://github.com/NVIDIA/vid2vid) by NVIDIA
