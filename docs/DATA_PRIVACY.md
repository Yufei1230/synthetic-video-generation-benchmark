# Data privacy and publication review

Research access to student recordings and collaborator material does not itself authorize public redistribution. This release records decisions for the repository; it does not assert institutional clearance or a demonstrated privacy guarantee.

## Included in this update

Public additions are explanatory documentation, paper-reported tables, aggregate recovered confusion/result counts, numeric configurations without data paths, provenance hashes, figures, audit utilities, and one sanitized historical recognition notebook with attribution/license. No student/video/frame identifier is included in released result tables.

The new notebook removes all stored outputs, execution counts and Colab user metadata, and replaces private shared-drive roots. Its original code logic remains visible, including known defects. The five pre-existing benchmark notebooks are unchanged as requested; inherited token-like links and old temporary URLs remain a separate owner-review issue in the [benchmark audit](BENCHMARK_AUDIT.md).

## Inspected privacy context

Relevant sections of a Forms data-management document and a native SDG Ethics research document were read privately. They discuss data ownership/access, consent and secondary uses, identifiable information and re-identification risk. Their presence is not evidence that public release of particular recordings, derivatives or participant images was authorized. Templates and research questions are not signed consent records or completed privacy tests. Internal document bodies and participant/candidate lists are not reproduced.

## Withheld material and unresolved release decisions

| Material | Decision | Before any later release |
|---|---|---|
| Student recordings, extracted frames and identifiable paper illustrations | Not downloaded for this audit or published | Verify consent scope, ownership and institutional release approval |
| Generated images/videos based on real people | Not published | Review retained identity, source ancestry, permission and service terms |
| Manifests containing source paths/video names | Private originals; aggregate counts only | Use an authorized private media/subject audit; do not expose identifiers |
| Raw prediction sequences | Private originals; public aggregate counts only | Review source-linkability before any per-example release |
| Checkpoint/model/body-mesh assets | Metadata only; not loaded or uploaded | Asset license, data rights, appropriate model/privacy review |
| Internal forms, ethics proposals, notes, interview lists and unpublished collaborator papers | Not published | Explicit owner and applicable participant/publication approval |
| Collaborator scripts | Referenced/inventoried rather than copied | File-level ownership and applicable license |
| Supplied manuscript PDF | Not uploaded | Author/publisher version and redistribution terms |

The new recovered recognition notebook's substantial upstream reuse is covered by the included [NVIDIA SynthDa license and attribution](../references/THIRD_PARTY_NOTICES.md). That license does not establish rights to school data or external models. No blanket license is assigned to the entire repository.

## Remaining research risks

Four class+basename development/test collisions in each recovered manifest need investigation; filenames alone cannot prove leakage or its absence. Student/session and generated-parent groupings are still missing. Synthetic appearance changes are not evidence of anonymity. No completed re-identification attack, fairness evaluation, field deployment, educational-outcome study or safety validation was recovered.
