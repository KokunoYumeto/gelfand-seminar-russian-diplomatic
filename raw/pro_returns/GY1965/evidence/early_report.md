# Records 53–68: completed critical inventory

Status date: **9 November 2026**.

The tranche contains **16 record entries, 102 mathematical occurrences, 20 correction rows, 16 bibliography entries, and one precisely formulated resolved problem**. The classifications are **95 E and 7 F**. There are no C or D entries: missing hypotheses, cancelled notation, or unsuccessful full-text access have not been converted into claims of undeveloped research problems.

## Files

- early_talks.json
- early_items.json
- early_problems.json
- early_corrections.csv
- early_references.bib
- early_evidence.json
- early_build.py, the reproducible constructor of the structured records

The frozen data are supplied under **code/parts/**, the authoring script under **code/research/**, and the report and evidence ledger under **evidence/**. The bibliography and evidence ledger are separate from the constructor and are not overwritten by it.

## Physical source order and coverage

The actual order is **53, 54, 55, 56, 57, 58, 59, 60, 62, 61, 63, 64, 66, 67, 65, 68**. This preserves the catalogue numbers while following the headings in the scans.

| Record | Actual pages | Items |
|---|---|---:|
| 53, Kohn | P000090–P000091 | 9 |
| 54, Finn | P000091–P000092 | 3 |
| 55, Gelfand on Atiyah–Bott | P000092–P000093 | 11 |
| 56, Gelfand continuation | P000093–P000095 | 13 |
| 57, seminar plan | P000096 | 0 |
| 58, Kazhdan | P000096–P000100 | 16 |
| 59, Gelfand | P000101–P000102 | 7 |
| 60, Dynin intervention | P000102 | 1 |
| 62, Bernstein intervention | P000102 | 1 |
| 61, Gelfand again | P000102–P000104 | 8 |
| 63, Gelfand continuation | P000104–P000105 | 8 |
| 64, Kazhdan | P000105–P000106 | 5 |
| 66, S. Gelfand | P000106 | 5 |
| 67, Smirnov | P000106 | 2 |
| 65, Gelfand again on Atiyah | P000106–P000107 | 7 |
| 68, Kazhdan | P000107–P000108 | 6 |

P000088–P000089 are excluded: they belong to the preceding invariant-subspace discussion. Record 68 stops before Matsaev's dated heading on P000108. The plan receives its own complete record summary; its reading assignments are not promoted to theorem assertions.

Every assigned scan, P000090 through P000108, was visually opened. The ledger records the precise heading boundaries and the important handwritten readings.

## Main editorial findings

**The Atiyah–Bott sequence is expository.** The opened Russian translation explicitly identifies the Harvard notes of autumn 1964. The principal definitions, fixed-point formula, spectral compression, and transverse entire-continuation theorem were therefore not newly announced by Gelfand merely because the journal paper appeared in 1967. The speaker attribution of record 55 remains Gelfand.

**The entire-continuation statement is not a mathematical error.** Section 9 of the Harvard text gives precisely the transverse geometric-operator result. The manuscript's separate, unassigned “pole at zero” parenthesis is retained as F; the ordinary divergence of an unsmoothed trace is not equated with a pole of its analytic continuation.

**Dynin's displayed shortcut is invalid; Bernstein's repair is complete.** The scan really identifies eigenspace cohomology with the kernel of the shifted Laplacian. That kernel is the eigenspace, often nonzero, whereas its positive-eigenvalue complex is acyclic. Bernstein's \(s=d(d^*s/\lambda)\) supplies the correct proof. Both interventions retain their own record entries.

**Smirnov is a close but incomplete publication match.** The original two-page 1966 paper was read, not just its metadata. It begins by requiring normalized *central* positive-definite functions, and its theorem uses the discrete characteristic-zero field setting. Those conditions are absent from the notebook. Record 67 consequently retains an F question with a partial publication match; no extra A theorem has been invented. The Russian abbreviation for representations does not decide between “continuous” and “irreducible.”

**The algebraic-geometry notes contain substantive omissions.** The classical coordinate ring needs a radical ideal. Closed diagonal is a separation criterion for the prevariety, not the sheaf axiom. The final linear \(K(X)\to A(X)\) map cannot be confidently identified with total Chern classes or the rational Chern character because the first axiom is cancelled. The \(E(X)\) finite-module question is likewise insufficiently specified. The independently supplied noncoherent-ring and dual-number examples are marked as checks proved in the companion, without a novelty claim.

**Several tempting “corrections” would be unjustified.** The factor two in the Laplace symbol is correct under the notebook's unnormalized \(f^m\) convention. The uncertain complex-case prefactor is not silently read as a definite digit. The source's inverse-map conventions are documented as inconsistent rather than replaced by a single allegedly certain transcription.

## Validation and limits

The structured audit checked all mandatory fields and allowed values, consecutive item IDs within each record, all 16 record numbers, citation-key coverage, reference existence, problem-occurrence links, balanced inline/display math delimiters, and absence of control characters. It passed with the counts above. The combined chapter's successful XeLaTeX/BibTeX check is recorded in `build_validation.md`.

The final problem ID is **GP-1965-01**, for the resolved strongly pseudoconvex d-bar/Levi construction, occurring at **1965-53.1 and 1965-53.4**. Assembly has completed the final renumbering. The previous index supplies thematic or direct exposition links for symbols and elliptic finiteness (1964-28.2–28.5), derived functors (1964-49.8), and normalized central functions (1964-13.1). The last is explicitly not treated as identity of Smirnov's unspecified question.

Verification levels remain conservative. Kohn's survey, the Harvard notes, Cohn–Vossen, Serre, Borel–Serre, and Smirnov were read at result level. Kohn–Rossi and Swan use checked author bibliographies; Finn and the first installment of Grothendieck's Tohoku paper use publisher metadata where full-text retrieval failed. Grothendieck's issue-2 pages **119–183** are correct for the first installment; the complete two-installment work spans **119–221**.

## Principal opened sources

The full 16-entry opening ledger is in **early_evidence.json**. Especially consequential sources are:

- Kohn, original survey: https://www.numdam.org/item/ASNSP_1963_3_17_4_373_0.pdf
- Cohn–Vossen, original article: https://www.numdam.org/article/CM_1935__2__69_0.pdf
- Finn, publisher record: https://link.springer.com/article/10.1007/BF02564362
- Atiyah–Bott, Harvard text in the published Russian translation: https://www.mathnet.ru/php/getFT.phtml?jrnid=mat&option_lang=eng&paperid=403&what=fullt
- Atiyah–Bott, 1967 publisher record: https://annals.math.princeton.edu/1967/86-2/p07
- Serre, original paper: https://www.college-de-france.fr/media/jean-pierre-serre/UPL5435398796951750634_Serre_FAC.pdf
- Borel–Serre, original exposition: https://www.numdam.org/article/BSMF_1958__86__97_0.pdf
- Smirnov, original theorem: https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=32570&what=fullt
- Grothendieck, first-installment publisher record: https://www.jstage.jst.go.jp/article/tmj1949/9/2/9_2_119/_article

Fresh raw-URL retries to the Math-Net PDF endpoints briefly failed, but reopening the already retrieved references succeeded. The ledger distinguishes those access events from the earlier successful full-text reading.

## Final independent review

`early_proof_review.md` checks the explanatory arguments; `root_annotation_review.md` records the separate checks of the noncoherent-ring and dual-number examples. The corrected weighted-count wording and repeated algebraically closed field hypothesis are incorporated in the final catalogue. The original data tranche remains frozen for provenance.
