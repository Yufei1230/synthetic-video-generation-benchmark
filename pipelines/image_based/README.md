# Image-based generation

Evidence: paper Sections III-C and V-D; the inspected research procedure document; metadata for `Experiment/data/<action>/{background,clothes,hairstyle}` image/video folders. This was a manual external-service workflow, not a recovered API batch-generation pipeline.

1. Select a representative real video per action and extract its first frame.
2. Edit background, clothing or hairstyle in Google AI Studio, keeping the laboratory action context.
3. Animate the edited image in Kling with the action prompt.
4. Organize accepted outputs by action and factor for the recognition experiment.

The paper specifies 20 videos per action/factor: 60 for each factor and 180 for all three appearance factors. Reported animation prompts are “He is shaking the flask.”, “He is swirling the flask.”, and “He is filling the burette with liquid.” These are manuscript examples, not a complete recovered job manifest.

Research notes also mention using AI Studio/Kling to make motions larger before SynthDa because small upper-body movements were difficult to reconstruct. It is not established which final camera samples followed that alternative path. Source lineage must distinguish direct-real from generated-intermediate inputs.

Exact service versions, seeds, full prompt list, rejected generations and acceptance records were not recovered. No new generation script, API wrapper or example footage is invented. Original media and prompts containing personal information are not published. See [methods](../../docs/METHODOLOGY.md) and [privacy](../../docs/DATA_PRIVACY.md).
