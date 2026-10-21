# Discrepancies, ambiguities, and missing evidence

Audit date: 2026-10-21. Sources: [P1, G1, A1 and public bibliographic records](../references/README.md). “Confirmed” below means confirmed in those sources, not experimentally reproduced. No Drive logs were accessible, so this is **not** a completed paper-versus-log reconciliation.

| ID | Observation | Status / implication | Required resolution |
|---|---|---|---|
| D01 | P1 describes 21 test videos and seven/action, but the percentages are not multiples of 1/21 or 1/7 | Confirmed arithmetic; author says accuracy is per frame, so source-video counts must not be used as metric denominators | Original evaluator, scored-frame manifest, predictions and aggregation rules |
| D02 | All class/overall rates admit a common 17/29/44-class-count construction (90 total) | Mathematical compatibility only; actual frame counts remain unverified | Recover counts rather than assuming these are observed |
| D03 | Table V lists 90 real + 240 synthetic = 330; Section III-E separately mentions 21 test videos | Training and test membership/overlap unresolved | Split and source-ancestry manifests; group by student/session where available |
| D04 | Table VIII lists 40/60/80 synthetic clips; Table VI adds 120/180/240 | Resolved at the paper-description level: IV-D specifies the former per action | Confirm file counts in original datasets |
| D05 | Table IX calls Combo-B the best combination under fixed budget | Budgets differ across combinations; matched-budget attribution unsupported | Equal-size controls or corrected wording |
| D06 | IV-D says both camera and clothing performed well individually | Camera Top-1 is 57.78%, below 77.78% baseline | Qualify the narrative by metric/class; do not repeat it as an overall improvement |
| D07 | V-B says shaking is perfect across settings | Table VII gives camera-condition shaking 76.47% | Restrict perfect-shaking wording to the conditions whose table entries are 100% |
| D08 | SlowFast and 16 sampled frames are named, but no recognizer implementation is in G1 | Architecture family and reported sampling are known; variant, packing, optimizer, preprocessing and inference are not | Training/evaluation source, configs, environment and checkpoint provenance |
| D09 | Original README cites Text2Video-Zero; Text2Video.ipynb loads CLIP and CycleGAN | Confirmed source identity mismatch; original content intentionally preserved | Recover original notebook provenance before renaming/relabeling historical work |
| D10 | Original README's folder illustration uses names/case that differ from actual notebook paths | Confirmed; new navigation uses real paths while archived original text remains exact | No notebook renames needed |
| D11 | Uploaded filename uses “ClassLab … Visual Analytics,” but the PDF title is “Enhancing Classroom Monitoring in Science Experiments Using Synthetic Videos” | Confirmed title-page reading | Cite the internal title; do not treat filename as another verified publication |
| D12 | P1 uses privacy/deployment language beyond the available code and evaluation evidence | No measured re-identification test, teacher evaluation, production app or deployment validation recovered | Scope repository claims to synthesis/recognition experiments |
| D13 | Image path described as comparable to camera path | Budget is 20/action **per factor**, not 60 image/action versus 20 camera/action | Use per-factor comparisons, and make total pool sizes explicit |
| D14 | P1 has percent-change rounding and a stray “44cm” in Table I | Editorial issues; no numerical source replacement warranted | Preserve source transcription; compute clearly labeled pp/relative changes from displayed rates |
| D15 | Google Drive materials, including Experiment and ethics folders, are unavailable | No file-level inventory, log reconciliation, ownership review, or privacy clearance can be completed | Authorized connection or owner-provided export |
| D16 | Original Text2Video notebook contains a long token-like download URL; older notebook outputs include temporary service links | Pre-existing publication concern; not copied into new docs or renewed/tested | Owner review and, if needed, a separate explicitly approved cleanup that preserves historical provenance |

## Resolution order

1. Obtain the evaluator, predictions and split/ancestry records to establish the metric and exclude leakage.
2. Recover exact training configs and original scripts; map each run to a paper row without merging historical versions.
3. Obtain publisher citation export and compare the supplied manuscript with the version of record.
4. Review ownership/licensing and image-release permissions before importing source code or media.

The audit never silently replaces paper values with earlier values mentioned in project discussions. Any later recovered runs should receive their own IDs, source paths and discrepancy entries.
