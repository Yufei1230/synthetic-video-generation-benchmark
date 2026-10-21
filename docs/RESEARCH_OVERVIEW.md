# Research overview

## Purpose and scope

Science teachers need to observe many students at once, while fine-grained laboratory actions can be difficult to distinguish. The project investigates synthetic video augmentation as a way to expand training diversity when real recordings are difficult to collect or share. The evaluated labels are **shaking, swirling, and buretting**. Sources: [P1, Sections I and III](../references/README.md).

The available study concerns video synthesis and action recognition. It does not demonstrate a production teacher dashboard, real-time safety intervention, improved learning outcomes, or a validated privacy guarantee. Those are possible downstream applications, not verified deliverables in this repository.

## Research progression

1. **Explore generation techniques.** The existing benchmark compares practical generation approaches through historical Colab notebooks and qualitative notes. It is not a unified quantitative benchmark with a shared test protocol.
2. **Construct appearance variants.** The paper describes first-frame editing in Google AI Studio followed by Kling animation, varying background, clothing, or hairstyle.
3. **Construct viewpoint variants.** The paper describes SynthDa mesh reconstruction and multi-view rendering, including a lower-body completion workaround for upper-body inputs.
4. **Assemble augmentation conditions.** Keep 90 real training videos and add one or several synthetic factor pools.
5. **Compare action recognition.** Recovered code uses pretrained PyTorchVideo SlowFast R50, 32 fast-path frames and Adam. The paper says 16 frames; the difference is documented rather than hidden.
6. **Reconcile evidence.** Recompute eight saved prediction exports, keep paper values separate, and document conflicting versions, split concerns and correlated sampled-frame scoring.

## Contribution boundaries

| Area | Supported attribution | What is not established |
|---|---|---|
| Research design and integration | The paper's authors report adapting existing generation tools to laboratory actions and evaluating augmentation factors | Sole authorship of every component or an independently novel backbone |
| Benchmark exploration | Existing notebooks and qualitative comparison are in this repository | A common runtime/quality metric or independent reproduction in this audit |
| Image generation | Application of Google AI Studio and Kling to controlled appearance edits | A locally implemented generative model or recovered batch-generation service |
| Video generation | Use/adaptation of SynthDa for multi-view human representations, as described in P1 | Ownership of SynthDa or complete source-to-render lineage for the final selected clips |
| Recognition | Original three-class notebook and saved SlowFast configuration/results, with substantial upstream helper reuse | New recognition architecture, leakage-free evaluation, or production deployment |

Individual contributions beyond the paper's author list require collaborator confirmation. Frameworks, pretrained weights, demos, and generation services retain their own ownership and terms.

## Reading paths

- **Recruiters:** [main README](../README.md), contribution table above, and [results](RESULTS_AND_ANALYSIS.md).
- **Researchers:** [methodology](METHODOLOGY.md), [experiments](EXPERIMENTS.md), and [discrepancies](DISCREPANCIES.md).
- **Reproduction or continuation:** [reproducibility](REPRODUCIBILITY.md), [source inventory](SOURCE_INVENTORY.md), and [privacy review](DATA_PRIVACY.md).
