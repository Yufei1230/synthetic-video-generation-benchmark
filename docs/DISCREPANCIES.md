# Discrepancies, ambiguities, and missing evidence

Audit date: 2026-10-21. Drive access is now available. [The source audit](DRIVE_AUDIT.md) distinguishes the supplied manuscript, original code, saved outputs and current manifests. “Confirmed” means observed in those sources, not independently rerun model performance.

| ID | Observation | Status / implication | Required resolution |
|---|---|---|---|
| D01 | Paper: 21 test videos, seven/action; percentages are not video-count multiples | Recovered evaluator repeats each clip prediction over 32 sampled-frame rows; eight exports contain 2,880 rows | Retain frame-based wording with clip-repetition explanation; do not call them independent frame predictions |
| D02 | Earlier arithmetic search gave 17/29/44 class denominators | Recovered row counts 544/928/1,408 divide by 32 into exactly 17/29/44 clip blocks | Resolved for recovered exports; missing paper runs remain unverified |
| D03 | Paper separates 90 real development and 21 test videos | Baseline manifest contains 72 train + 18 val + 21 test; four class+basename test/development collisions occur in all seven distinct manifests | Privately compare media hashes and subject/session/synthetic ancestry; names do not prove identical footage |
| D04 | Table VIII lists 40/60/80 synthetic clips; Table VI adds 120/180/240 | Resolved at the paper-description level: IV-D specifies the former per action | Confirm file counts in original datasets |
| D05 | Table IX calls Combo-B the best combination under fixed budget | Budgets differ across combinations; matched-budget attribution unsupported | Equal-size controls or corrected wording |
| D06 | IV-D says both camera and clothing performed well individually | Camera Top-1 is 57.78%, below 77.78% baseline | Qualify the narrative by metric/class; do not repeat it as an overall improvement |
| D07 | V-B says shaking is perfect across settings | Table VII gives camera-condition shaking 76.47% | Restrict perfect-shaking wording to the conditions whose table entries are 100% |
| D08 | Paper says SlowFast and 16 input frames | Recovered source/configs select PyTorchVideo SlowFast R50 with 32 fast / 8 slow frames, frozen non-projection parameters and Adam | Resolve paper wording and bind each run to exact source/checkpoint |
| D09 | Original README cites Text2Video-Zero; Text2Video.ipynb loads CLIP and CycleGAN | Confirmed source identity mismatch; original content intentionally preserved | Recover original notebook provenance before renaming/relabeling historical work |
| D10 | Original README's folder illustration uses names/case that differ from actual notebook paths | Confirmed; new navigation uses real paths while archived original text remains exact | No notebook renames needed |
| D11 | Uploaded filename uses “ClassLab … Visual Analytics,” but the PDF title is “Enhancing Classroom Monitoring in Science Experiments Using Synthetic Videos” | Confirmed title-page reading | Cite the internal title; do not treat filename as another verified publication |
| D12 | P1 uses privacy/deployment language beyond the available code and evaluation evidence | No measured re-identification test, teacher evaluation, production app or deployment validation recovered | Scope repository claims to synthesis/recognition experiments |
| D13 | Image path described as comparable to camera path | Budget is 20/action **per factor**, not 60 image/action versus 20 camera/action | Use per-factor comparisons, and make total pool sizes explicit |
| D14 | P1 has percent-change rounding and a stray “44cm” in Table I | Editorial issues; no numerical source replacement warranted | Preserve source transcription; compute clearly labeled pp/relative changes from displayed rates |
| D15 | Initial audit lacked Drive access | Resolved for shared root and inspected research sources; shortcut target still returns 403; media/weight subtrees not exhaustively expanded | See bounded source inventory; no claim of reading inaccessible/metadata-only contents |
| D16 | Original Text2Video notebook contains a long token-like download URL; older notebook outputs include temporary service links | Pre-existing publication concern; not copied into new docs or renewed/tested | Owner review and, if needed, a separate explicitly approved cleanup that preserves historical provenance |

## Additional code and record findings

| ID | Observation | Status / implication | Required resolution |
|---|---|---|---|
| D17 | Camera saved result 48.89% versus paper 57.78%; camera+clothing 80.00% versus 53.33% | Confirmed from eight prediction/summary exports; do not replace either source | Locate exact paper-run records |
| D18 | Three-factor exports show 91.11% (October 21) and 68.89% (October 15, renamed `background2`) | Separate versions retained; current notebook contains older output | Keep distinct run IDs and recover final memberships |
| D19 | Four-factor model-evaluation folder is empty | Paper 81.11% not prediction-verified; arguments/logs/weights exist | Locate prediction export and selected checkpoint linkage |
| D20 | Current camera/two-factor/earlier three-factor manifests have 270/330/390 development rows | Larger than paper's 150/210/270; later October 21 data paths were not recovered | Match data/version to each paper experiment |
| D21 | Uniform sampler stops when end + duration reaches video length | Omits tails, and final full block at exact multiples; 3,285 annotated frames yield 2,880 scored rows | Preserve historical behavior; fix only in a new labeled experiment |
| D22 | Same random scale/crop/flip is used in validation/test | Fixed membership does not establish identical realized evaluation inputs | Add deterministic evaluation and record repeated seeds in a new run |
| D23 | Notebook preparation, output and weight paths name different conditions | Possible output misfiling; adjacent files alone do not establish exact checkpoint provenance | Reconcile every path; export run/checkpoint IDs with predictions |
| D24 | Source extraction uses 30 FPS; timestamp labels use source FPS; FFmpeg failures/stale frame folders are unchecked | Timing and stale-data risk | Validate extraction and timestamp basis in a new version |
| D25 | Per-class table includes Overall and the next cell sums all rows | Counts double but accuracy ratio stays unchanged | Use original scored rows for denominators, not the double-summed table |
| D26 | Config says 50 epochs but primary streams show 47 baseline / 37 clothing / 43 four-factor validation steps | Incomplete/restarted record coverage; no claim about why streams end | Recover complete logs and selected epochs; do not count restarts as independent seeds |
| D27 | AutoSynthDa prototype contains fabricated sample metrics and TODOs already in the source | It is an exploratory integration, not evidence for paper laboratory-action performance | Keep separate; never present sample metrics as observed research results |

## Resolution order

1. Audit private media/source ancestry for the filename collisions and identify final memberships.
2. Recover missing paper-run exports and bind each record to source revision, configuration and checkpoint hash.
3. Correct evaluation/dependency/path issues in a separate run version, with deterministic evaluation and video/window IDs.
4. Confirm publisher-file equivalence and review any additional code/media release permissions.

No paper value is silently replaced with a conflicting historical record. Five matching paper conditions corroborate aggregates; they do not establish leakage-free or production-ready performance.
