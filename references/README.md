# Sources and citation

## Source register

| ID | Source | Use and verification limit |
|---|---|---|
| P1 | Owner-supplied nine-page PDF, internal title: *Enhancing Classroom Monitoring in Science Experiments Using Synthetic Videos* | Primary source for methodology, dataset design and results; text and all page layouts inspected; final publisher equivalence unverified |
| G1 | [Repository base commit](https://github.com/Yufei1230/synthetic-video-generation-benchmark/tree/dd16e40f6828803cf3d13bffc4f3fe48c473cabf) | Entire tracked tree and 19-commit history inspected; benchmark static code and stored output, not rerun |
| A1 | Author clarification on 2026-10-21: accuracy is based on frames, not videos | Corrects how metrics are described; exact evaluator and counts still need code verification |
| T1 | Owner's attached task specification | Scope, preservation requirement, requested Drive folder categories and publication limits; not experimental evidence |
| B1 | [NIE repository record](https://repository.nie.edu.sg/entities/publication/a68ec781-5cdd-4edc-b5c2-d908d8ce10a1) | Search-indexed institutional record confirms title/DOI; full page returned HTTP 405 during audit |
| B2 | [JST J-GLOBAL bibliographic record](https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202602230116779954) | Corroborates six authors, IEEE conference proceedings, ICIET 2026 and pp. 65–73; bibliographic metadata, not experiment verification |
| B3 | [Official ICIET conference program](https://www.iciet.org/Koriyama-Program.pdf) | Indexed program lists this title, paper C257, Yufei Li and Edwin Chng; supports conference association, not an execution record |

P1 was uploaded under the filename `ClassLab__Enhancing_Classroom_Monitoring_for_Science_Experiments_with_Synthetic_Data_and_Visual_Analytics__Copy_(3).pdf`. Its SHA-256 is `3d2b80492d3969bb8abd5b50e06510d7d48e59686ecfda15d8c778e91f52ba54`. The title in that filename differs from the title page; citations use the title page. The PDF is not redistributed here.

All page numbers in these documents refer to P1's PDF pages 1–9. Sources B1–B3 were checked on 2026-10-21. Direct retrieval of the DOI/publisher record and Crossref API was unavailable in this audit. Bibliographic corroboration should not be confused with independent experimental validation, and the supplied file was not byte-compared to the version of record.

## Citation

Bibliographic records associate the work with the following citation. Verify against a publisher citation export before formal reuse:

Yufei Li, Edwin Chng, Megani Rajendran, Aik Beng Ng, Yong Leng Kelvin Tan, and Simon See. “Enhancing Classroom Monitoring in Science Experiments Using Synthetic Videos.” *2026 14th International Conference on Information and Education Technology (ICIET)*, pp. 65–73, 2026. DOI: [10.1109/ICIET69664.2026.11561646](https://doi.org/10.1109/ICIET69664.2026.11561646).

[BibTeX](paper.bib)

## Framework sources

- SlowFast: P1 reference [3], [original paper](https://openaccess.thecvf.com/content_ICCV_2019/html/Feichtenhofer_SlowFast_Networks_for_Video_Recognition_ICCV_2019_paper.html). The project-specific implementation/version is not recovered.
- SynthDa: P1 reference [12], [publication](https://doi.org/10.1145/3610543.3626168). The project's exact source revision and integration scripts are not recovered.
- Google AI Studio and Kling: named by P1; service/model versions and generation logs are unavailable.
- The benchmark's original references and acknowledgements remain in the [main README](../README.md); additional source-level dependencies are listed in the [notebook audit](../docs/BENCHMARK_AUDIT.md).

Links identify the cited frameworks; no claim is made that each current linked implementation was run or that its license covers the original project assets.
