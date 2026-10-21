# Source inventory and integration decisions

Audit date: 2026-10-21. Repository: `Yufei1230/synthetic-video-generation-benchmark`; base branch `main`, commit `dd16e40f6828803cf3d13bffc4f3fe48c473cabf`. Files below were read in full, including notebook source and stored outputs. No benchmark notebook was executed.

## Inspected sources

| File / original location | Type and purpose | Implementation / result evidence | Duplicates existing GitHub? | Publication decision | Destination |
|---|---|---|---|---|---|
| G1: README.md | Markdown; preliminary qualitative benchmark | Documentation, comparisons, links, acknowledgements | Already tracked | Preserve all original text as historical content; add accurate research navigation | README.md |
| G1: notebooks/CogVideoX.ipynb | Colab; image-to-video exploration | Actual generation code and stored outputs | Already tracked | Preserve bytes; external asset rights not re-cleared | Same path |
| G1: notebooks/DynamiCraft.ipynb | Colab; diffusion exploration | Actual setup/inference/training invocations and stored failures | Already tracked | Preserve bytes; document limitations | Same path |
| G1: notebooks/Text2Video.ipynb | Colab; CLIP/CycleGAN exploration | Actual code; no stored run outputs | Already tracked | Preserve bytes; flag provenance and token-like URL review | Same path |
| G1: notebooks/first_order_model.ipynb | Colab; image animation demo | Actual code; no stored run outputs | Already tracked | Preserve bytes; inherited demo licensing review remains | Same path |
| G1: notebooks/vid2vid.ipynb | Colab; generic vid2vid demo | Actual commands; no stored run outputs | Already tracked | Preserve bytes; document legacy dependencies | Same path |
| G1: results/video.md | Markdown, one newline | No experimental results or demo links | Already tracked | Preserve bytes | Same path |
| P1: supplied ClassLab-named PDF | Nine-page manuscript; methods, tables, figures | Documentation and aggregate reported results, not run logs | Partial conceptual overlap with benchmark; not same file | Summarize methods and aggregate facts; withhold PDF and identifiable images | docs/, CSV, aggregate charts, references/ |
| T1: Pasted text(4).txt | Owner's task instructions | Scope only | No | Do not publish the instruction attachment | Informs release scope |
| A1: owner frame-level clarification | Conversation statement | Metric-definition context, not recovered evaluator | No | Attribute as author clarification | README, results, discrepancies |
| B1–B3: bibliographic sources | Public institutional/index/program records | Citation evidence, not methods verification | No | Link and cite, with access limitations | references/README.md, paper.bib |

Original byte hashes are recorded in [benchmark_integrity.json](../references/benchmark_integrity.json). P1's filename and checksum are in the [source register](../references/README.md).

## Requested Drive sources: inaccessible, not inventoried recursively

The supplied root folder could not be read through the available retrieval route. Plugin discovery reported Google Drive not installed/connected; no authorized connected Drive file listing or owner-provided local export was available in this task. These are **requested categories from T1**, not observed directories or verified file contents. The private root link is omitted from public documentation.

| Requested location | Intended research purpose | Actual file types/content | Duplicate/implementation/result status | Publication decision / future destination |
|---|---|---|---|---|
| Documentation | Protocols, prompts, notes | Unknown; uninspected | Unknown | Review sanitized documentation before docs/ integration |
| Experiment | Training, evaluation, logs, predictions | Unknown; uninspected | Unknown | Recover genuine code/results; no folder scaffold created yet |
| NVAITC-NIE SDG Project Materials | Collaboration/generation materials | Unknown; uninspected | Unknown | Ownership and confidentiality review before any import |
| Papers | Manuscript versions/references | Unknown; uninspected | Unknown | Establish version and redistribution rights |
| Forms | Consent / study forms | Unknown; uninspected | Unknown | Do not publish originals |
| SDG Ethics | Ethics and data-sharing constraints | Unknown; uninspected | Unknown | Do not publish originals; owner-approved summary only |

A complete filename/location/type inventory, deduplication check, privacy review and paper-versus-log reconciliation remains blocked until those materials are accessible. No existence or implementation detail is inferred from these labels.

## Major additions and their sources

| Addition | Sources |
|---|---|
| Research overview and contribution boundaries | P1 Sections I, III and V; G1 |
| Methodology and dataset account | P1 Figure 1, Tables II–VI and Section III |
| Experiment register, result CSV and figures | P1 IV-B, Tables V–VIII; A1 for frame clarification |
| Discrepancies | Direct comparisons within P1, static G1 inspection, arithmetic diagnostics; no Drive-log comparison |
| Reproducibility and benchmark audit | Actual G1 notebook cells; missing-code distinction; executed new utility checks |
| Privacy/release decisions | Identifiable P1 examples, T1 restrictions, static G1 review |
| New audit/plot/check utilities | Newly written documentation tooling; not original research implementation |
| Citation | P1 title/authors, B1–B3 bibliographic corroboration |
