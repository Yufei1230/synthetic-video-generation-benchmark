# Experiment register

The table below preserves the paper's intended design and reported results. It is not a substitute for the original run records. The paper specifies 90 real development videos, 60 synthetic videos per factor, SlowFast, 16 sampled frames and 21 real test videos. Recovered code/configs instead use 32 fast-path frames, an 80/20 development split, and several historical data versions. [Full reconciliation](DRIVE_AUDIT.md).

| Experiment | Real + synthetic training videos | Top-1 (%) | Change (pp) |
|---|---:|---:|---:|
| Real only | 90 + 0 | 77.78 | +0.00 |
| Camera angle | 90 + 60 | 57.78 | -20.00 |
| Clothing | 90 + 60 | 93.33 | +15.55 |
| Background | 90 + 60 | 88.89 | +11.11 |
| Hairstyle | 90 + 60 | 95.56 | +17.78 |
| Camera + Clothing | 90 + 120 | 53.33 | -24.45 |
| Camera + Clothing + Background | 90 + 180 | 91.11 | +13.33 |
| Camera + Clothing + Background + Hairstyle | 90 + 240 | 81.11 | +3.33 |

## Questions and interpretations

| ID | Question | Added data and generation method | Paper-reported observation | Main limitation |
|---|---|---|---|---|
| baseline | What performance is reported using only real training data? | None | 77.78% overall; buretting lowest at 63.64% | Filename-level split manifest recovered; media ancestry and exact checkpoint pairing unverified |
| aug_a | Does viewpoint diversity help? | 60 SynthDa camera renders | 57.78%; buretting 27.27% | Geometry/rendering changes are bundled with viewpoint |
| aug_b | Does clothing diversity help? | 60 Google AI Studio + Kling clips | 93.33%; shaking/swirl 100% | No repeated-run uncertainty; service settings unavailable |
| aug_c | Does background diversity help? | 60 Google AI Studio + Kling clips | 88.89%; buretting 95.45%, swirling 72.41% | Overall improvement conceals a class-specific decline |
| aug_d | Does hairstyle diversity help? | 60 Google AI Studio + Kling clips | 95.56%, highest reported overall | Small source base; identity and leakage controls not recovered |
| combo_a | What happens when camera and clothing pools are combined? | 120 total synthetic; 40/action | 53.33%, below both individual conditions | Count and factor composition differ from single-factor runs |
| combo_b | What happens when background clips are added? | 180 total synthetic; 60/action | 91.11%; buretting 93.18% | Count and composition both change; no matched-size control |
| combo_c | What happens when hairstyle clips are also added? | 240 total synthetic; 80/action | 81.11%; swirling 55.17% | More data and more factor types cannot be disentangled |

The 40/60/80 “Synthetic Clips” in P1 Table VIII are **per action**, as explained in Section IV-D. They are not the total numbers of synthetic training clips.

## Recovered run evidence

Eight original prediction exports are now available for private audit; public aggregate counts and source hashes are in [experiments/recovered](../experiments/recovered/README.md). Five conditions corroborate the paper's overall and class rates. Camera and two-factor results differ; three-factor has two versions; four-factor has no recovered prediction export. Ten argument files and thirteen event files add configuration and training-history evidence. None is an independent model rerun.

Keep the [paper CSV](../experiments/paper_reported_results.csv) and [recovered result CSV](../experiments/recovered/results.csv) separate. The original paper table above remains an exact transcription. Selected checkpoint hashes and complete source-video ancestry are still missing.

## Needed controls before stronger claims

Recover source-video ancestry and subject/session grouping to audit leakage, including the one representative image source per action and the seven SynthDa sources. Confirm that no test video or derived frame seeded training synthesis. Compare equal synthetic budgets if attributing changes specifically to factor combinations, and repeat runs across recorded seeds before claiming stability or significance. These are proposed next steps, not completed experiments.
