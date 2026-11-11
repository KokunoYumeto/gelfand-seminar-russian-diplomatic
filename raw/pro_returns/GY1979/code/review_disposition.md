# Final review disposition

**Review and disposition date:** 2026-11-10. This document closes the six findings in `integration_review.md`, records the independent mathematical reviews, and resolves the three bibliography annotation alternatives. It was checked against the final integrated JSON, TeX, bibliography, report, saved configuration and build outputs. This documentation pass made no semantic data edits and did not rebuild the chapter.

Final inventory: **27 records, 252 items, 10 problem threads, 104 references, 106 correction/provenance rows**; classes **A12/B7/C3/D0/E203/F27**.

## The six integration-review findings

| Finding | Disposition | Final evidence |
|---|---|---|
| 1. Kallosh record 465 omitted the programme at the foot of P000848 from its source range. | **Resolved.** The critical span is now `P000848-P000853`, while the supplied catalogue envelope remains preserved separately. | `GY1979_talks.json`, record 465; `code/editorial_config.json`, `source_span_overrides`; `code/catalog_crosswalk.csv`. |
| 2. Normal-form item 468.11 was marked merely annotated despite its substantive proved development. | **Resolved.** `development` is now `developed in this chapter`; its historical class remains B. This records work supplied here, without asserting novelty. | `GY1979_items.json`, 1979-468.11; `GY1979_development.tex`, `dev:berezin-normal`; saved item override. |
| 3. Energy-proof wording could imply an erratum by the original author or an exhaustive search for repairs. | **Resolved.** The report identifies later primary diagnoses rather than claiming a Shimada author correction. The overview now says “a published proof claim with a documented gap.” The item retains the bounded retrieval status and distinguishes Hasebe/Ando's criticism from a counterexample to irreducibility. | `GY1979_report.md`, principal findings; `GY1979_overview.tex`, remaining questions; item 1979-470.7 and `dev:energy-diagnostic`. |
| 4. Overview named translation/transcription correction types absent from the CSV. | **Resolved.** The overview now names faithfully transcribed mathematical errors, unresolved readings and provenance discrepancies. The actual counts are 75 `faithful_error`, 17 `ambiguity`, 14 `provenance`. | `GY1979_overview.tex`, continuity/corrections paragraph; `GY1979_report.md`, correction profile; `GY1979_corrections.csv`. |
| 5. Report's conference-list counting rule did not account for F occurrences 462.2–4. | **Resolved.** The rule now distinguishes bare contextual lists from mathematically intended but underdetermined reports preserved as F items. No item was removed or renumbered. | `GY1979_report.md`, coverage/counting decisions; items 1979-462.2–4. |
| 6. Exact 463.2 formula evidence was originally limited to 1988 although class A referred to soon-after publication. | **Resolved by stronger primary evidence.** The original 1980 paper has now been read and its formula pages visually checked. Items 463.1/.2 have exact matches with `read the result`; 463.6 explicitly separates the early kinetic criterion from the stronger later Hamiltonian theorem and has a partial publication match. | Items 1979-463.1, .2 and .6; final bibliography annotation for `zakharovschulman1980degenerative`; `code/root_research_log.md`, final chronology check; report chronology and class-limit discussions. |

### The chronology evidence that supersedes the early access limit

The final independent check opened Zakharov and Schulman's original *Degenerative dispersion laws, motion invariants and kinetic equations*, Physica D 1(2), 192–202, at:

https://zakharov75.itp.ac.ru/static/local/zve75/zakharov/1980/1980-05-1980_PD_ZS.pdf

Section 1, pp. 192–195, was read; equations (12)–(13), p. 193, give the difference-curve parametrization and credit the general example to **S. V. Manakov, private communication**. The manuscript was **received 1 September 1979** and the article **published June 1980**. Receipt is not asserted to be a public circulation date. The kinetic obstruction on p. 195 excludes singular delta-type kernels. The general quadratic-leading Hamiltonian-invariant theorem is separately identified in the 1988 paper, Theorem 3.1, pp. 291–293, whose introduction also notes a brief 1985 announcement. No 1988 theorem is silently backdated to the 1980 article.

Accordingly, the earlier metadata-only statement in the early research log is retained as audit history and explicitly superseded by the final source check. The six original findings are closed; their presence in the preserved review does not imply that they remain defects in the delivered chapter.

## Independent mathematical reviews

### Middle-record reviewer: analytical calculations and hypotheses

`code/independent_early_review.md` independently confirms the Gaussian/quartic calculations, the exact resonance-coefficient counterexample, the four-sphere heat/zeta values and the symplectic self-adjoint form. Its executable checks and output are packaged as:

- `code/authoring/middle/independent_early_checks.py`
- `code/authoring/middle/independent_early_checks.json`

Both suggested precision changes are visible in the final JSON:

- **465.21:** a nonnegative self-adjoint Laplace-type operator on a **closed smooth four-dimensional Riemannian manifold**, with zeta formed from **positive eigenvalues**, is stated explicitly before `zeta_P(0)=B4−dim ker P`.
- **466.4:** the symplectic vector space is explicitly **finite-dimensional** and the statement is over the complex numbers.

The numerical qualification remains intact: an analytic bound on discarded tails or a Taylor remainder is not by itself an interval certificate for floating-point quadrature. No numerical correction was required.

### Late-record reviewer: development proof pass

`code/proof_review.md` independently rederives the regular-representation reduction, semisimple-body dual-number form, three-generator matrix-pair embedding, complete `n=2, N=4` even commutant and compactly supported SU(2) diagnostic. Its verdict is **correct under the stated hypotheses; no mathematical correction required**. The complex field used in the general canonical-algebra reduction is distinguished from the real-or-complex coefficient field of the explicit commutant calculation. Ordinary commutation, supermatrix parity and proof failure versus reducibility are kept separate.

The saved computations agree with the proof scope: two exact implementations match on 36 cases, every kernel vector is substituted back, and 1,706 ordered basis products are checked in three representative cases. Those finite checks support the proofs; they do not replace the proofs for all matrices.

## Bibliography merge alternatives: all three resolved

The three entries in `code/bibliography_merge_conflicts.json` are same-work annotation/link differences. They do not identify competing publications, duplicate bibliography keys or unresolved mathematical claims. **Disposition for each: retain the fuller annotation selected in the final bibliography.** The original alternatives remain in the JSON as an audit record.

| Key | Retained final annotation and reason | Status |
|---|---|---|
| `wilson1974confinement` | Retain the full-original scope: Sections II and IV and the limitations in VI; publication 15 October 1974 and receipt 12 June 1974. Preserve the explicit qualification that the cumulative February 1974 preprint lead was not independently reverified. This is more informative than the alternative publisher-abstract-only access note and preserves the lattice/continuum distinction. | **Resolved — fuller full-text annotation retained.** |
| `jaffewitten2000yangmills` | Retain the opened official problem description with locators in Sections 1–2, 5 and 6.5, especially Section 5's separation of confinement from existence and mass gap. Preserve `year={n.d.}`: the key's 2000 component is the Millennium announcement convention, not a verified circulation date for the undated PDF. | **Resolved — fuller official-source annotation retained.** |
| `sergeichuk2000canonical` | Retain the root annotation verifying Theorems 1.1 and 1.3, Section 1.4 and reference 32's 1999 Bielefeld preprint. Preserve journal publication 2000, repository deposit 2007, and the explicit statement that the supermatrix application is the chapter's regular-representation reduction. The retained entry also supplies issue numbers 1–3. | **Resolved — root's fuller theorem/chronology annotation retained.** |

All three final entries were compared with the retained alternatives. No bibliography edit was needed in this documentation pass. The merger may continue to report three historical alternatives when rerun; this disposition is the human review outcome for that log.

## Packaging and build disposition

Historical `parts/early`, `parts/middle` and `parts/late` paths in research notes correspond to packaged `code/authoring/early`, `code/authoring/middle` and `code/authoring/late`. Source scans, source transcriptions and public-paper downloads are intentionally not redistributed. The final chapter is rebuildable from the seven delivered inputs and included build support; repeating the source audit requires the original inputs.

The final integrated build recorded in `code/build_status.json` passed the builder, independent audit and all XeLaTeX/BibTeX stages. At this review checkpoint the PDF was **747,477 bytes**. A subsequent typographic pass expanded compressed prose in correction cells; its before/after changes are recorded in `corrections_typesetting_output.json`. The final PDF hash, size and page count are recorded in `pdf_qa_output.json`. There were no LaTeX errors, undefined references/citations, missing-character warnings or overfull boxes. Remaining underfull-box diagnostics are preserved in the build log. This documentation task did not modify final JSON/TeX/BibTeX, rerun searches, or rebuild the PDF.
