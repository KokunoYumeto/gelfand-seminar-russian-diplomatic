# Records 428–436: research and source audit

Status date: **10 November 2026**. These files are a contribution to the GY1977 chapter, not a separate claim that every event in a catalogue page envelope occurred in 1977. The supplied chapter format was read before writing the structured data. The authoritative outputs in this directory are `talks.json`, `items.json`, `problems.json`, `areas.json`, `corrections.csv`, `references.bib`, `references.json` and `development.tex`. The generation scripts and downloaded materials are working evidence.

## Scope and boundaries

The English and Russian transcriptions of the assigned pages were read as source material. All mathematical paragraphs, definitions, formulas, constructions, questions and historical assertions were considered; unsupported fragments were retained as class F rather than converted into invented open problems. The source-page windows in the catalogue overlap and are not attribution boundaries.

| Record | Actual source content assigned here | Items | Boundary decision |
|---|---|---:|---|
| 428 | S. I. Gelfand, 3 October 1977, P000719–P000720 | 7 | P000718 is preceding Dickey–Novikov material, handled by the early-record editor. |
| 429 | S. I. Gelfand, 10 October 1977, P000721–P000724 | 11 | The complete P000722 scan was recovered before finalizing the formulas. |
| 430 | S. I. Gelfand, 24 October 1977, P000725 to the Krichever heading on P000729 | 15 | The second speaker on P000729 begins a separate record. |
| 431 | I. M. Krichever, 24 October 1977, P000729 to the Novikov heading on P000730 | 4 | The text explicitly discusses relatively prime orders; it is not a new higher-rank construction. |
| 432 | S. P. Novikov, 31 October 1977, P000730–P000734 | 16 | Yang–Mills critical connections and instantons are indexed separately. |
| 433 | Béla Sz.-Nagy, 15 November 1977, P000735 to the Krichever heading on P000736 | 8 | The generic-combination lemma precedes the rational-KP talk on the same page. |
| 434 | I. M. Krichever, 15 November 1977, P000736–P000737 | 6 | Literal KP signs are retained in the normalization calculation. |
| 435 | Yu. I. Manin, source date 21 November 1977, P000738–P000745 | 19 | The catalogue says 21 September. `talk.date` retains catalogue metadata; the summary and correction give the unambiguous source date 21/XI/77. |
| 436 | L. D. Faddeev, 28 November 1977, P000746–P000752 | 27 | P000753–P000754 begin an adjacent S. I. Gelfand talk dated 13 February 1978. The late-record editor includes it with its continuation under record 438. |

Total: **113 occurrences**, including **27 A, 4 B, 2 C, 0 D, 72 E and 8 F**; **8 definite problem entries**, **45 correction/provenance entries**, **29 cited works**, and **30 reference-audit rows**. One work has separate metadata and primary-text-reproduction audit rows. `validation.json` records the final schema and citation checks.

## Scans and recovery

Decisive visual checks include the recovered P000722; P000723–P000724 matrix orders and quiver; P000726–P000729 Casimir, compact weights, normalizer and principal-series conventions; P000730–P000734 instanton diagrams, signs and dimensions; P000735–P000737 inner-factor and KP formulas; P000738–P000745 dates, tensor dimensions, quaternionic map, Gram blocks and local frame; and P000746–P000752 quantum formulas and the final handwritten verb. Derived RGB previews in `scan_views/` were used for legibility without modifying the source files. The extensive blank region on P000735 is part of the page, not missing source content.

The uploaded P000722 file was genuinely truncated, not merely refused by an image viewer. The assembler fetched the complete original from:

https://old.mccme.ru/gelfand/notes/chapter_011/11_part_000018.png

The 10,722-byte supplied file is an exact prefix of the 169,042-byte original. Downloaded neighboring P000721 and P000723 files were byte-for-byte identical to their supplied counterparts, confirming the page mapping. Recovery evidence is in `work/code/output/scan_722_recovery.json`; the complete page is `work/recovered_scans/GELFAND-P000722.png`. The recovered page was then visually inspected, including the natural-isomorphism sign and the standard positive lower-triangular generator. **No unresolved missing-pixels limitation remains for P000722.**

On P000752, both record editor and assembler independently read **«Массивные частицы рассеиваются как солитоны»**. Both supplied transcriptions have the different verb “appear.” This is a genuine transcription/translation correction: the intended comparison concerns scattering. Other corrected mathematical signs and coefficients are usually faithful notebook errors, not defects introduced by the transcribers. The CSV distinguishes these categories.

The three-page BGG I and II papers were each downloaded, rendered and read in full. All three pages of Krichever's rational-KP announcement were likewise rendered and inspected. Both primary PNAS scan pages of Atiyah–Hitchin–Singer were read directly after the PDF endpoint returned challenge HTML. Files with `.pdf` extensions produced by failed downloads (`ahs1977.pdf`, `faddeevkorepin1978.pdf`) are not evidence of a successfully read PDF; the audit names the actual page images or readable reproduction used instead.

## Search and retrieval trail

Search was used to find primary papers, author archives and publisher metadata. Technical conclusions rely on primary material or explicit editorial calculations. The following records group the query subjects and retrieval paths; they are normalized query descriptions, not a fabricated verbatim export of every search request. Exact URLs and the level and locator of each opened result are in `references.json`.

| Query subject / search terms | Primary retrieval and result |
|---|---|
| Bernstein Gelfand Gelfand local structure Harish-Chandra modules; nice algebras; normalizer quotient | Bernstein's author archive, `BGG_Harish-Chandra_modules_1.pdf` and `_2.pdf`. Read all six pages. First theorem is for bounded central support and a finite-over-center algebra. The nice analytic order theorem requires regular infinitesimal character and a sufficiently small neighborhood. Generic Weyl equivalence is an assertion about irreducibles, not arbitrary extensions. |
| Krichever commuting differential operators; Burchnall–Chaundy; theta reconstruction | Author-hosted 1978 commuting-rings paper, 1977 Methods survey, and Math-Net `dan40219` for the 1976 announcement. Read the indicated theorems, theta construction and historical discussion. A 1939 reference and the notebook's almost-commuting fragment remain unidentified. |
| Krichever rational KP Moser poles Hamiltonian | Author-hosted 1978 rational-KP announcement; all three pages read. Theorems 2–3 and Corollary 1 establish the pole/particle and commuting-flow correspondence. Notebook normalization checked independently instead of silently transferring a differently normalized Hamiltonian. |
| Sz.-Nagy diagonalization matrices H-infinity Sherman lemma | Primary 1976 Acta paper at the Hungarian Academy repository. Lemma 2 and proof, Main Lemma, and matrix quasi-equivalence scope read. The polynomial moment-curve version is distinguished from the paper's stated simultaneous coefficient lemma. |
| Instantons deformations 8k-3; charge-one moduli; t Hooft Jackiw Nohl Rebbi | PNAS 1977 Atiyah–Hitchin–Singer article. The two primary page images give the deformation-complex proof, the hyperbolic five-space charge-one case, and the explicit distinction between the 5n and 5n+4 parameter families. |
| Atiyah Ward instantons algebraic geometry 1977 | Springer publisher abstract and dates opened. Full article was not read; missing reality and real-line-triviality conditions are explicitly modern reconstruction, not asserted to have been checked in that full text. |
| Uhlenbeck removable singularities finite action Yang Mills | Springer 1982 publisher abstract read. It explicitly states compactification/removal; no upgrade to full-proof verification. The cited 1979 announcement was a lead, not a separately verified reference. |
| Instanton connectedness Taubes Donaldson SU(r); finite-action nonminimal critical points | Dayaprema–Waldron's open-access 2026 primary article. Theorems 1.1–1.2 and section 3.3 read. The article gives a new connectedness proof, distinguishes historical SU(2)/SU(3) and general-rank arguments, and does not classify all nonminimal Yang–Mills critical points. |
| Drinfeld Manin self-dual sphere Gram matrix; instantons CP3 bundles monads | Math-Net `faa1991` and `faa1899`, including full primary Russian PDFs. Read the entire short 1978 announcement and the 1979 admissibility definitions, monad theorem and proof, plus indicated surrounding sections. The title of the latter is “Instantons and bundles on CP3,” checked against its metadata. |
| Narasimhan Ramanan universal connections canonical Stiefel | Primary one-page Narasimhan announcement in the 1962 Prague proceedings, p.286. Read in full, including compact-group and finite-base-dimension scope and the unitary Stiefel example. The unavailable original AJM paper is not added as a separately verified citation. |
| Gelfand Ponomarev quadruples subspaces automorphism Hermitian | Math-Net `dan36010` metadata opened. The 1971 complex quadruples paper is a thematic lead. The additional unpublished automorphism and Hermitian-duality assertion in the notebook was not identified or claimed solved. |
| “Faddeev Korepin Quantum theory solitons pdf” | Primary institutional metadata at Stony Brook; direct publisher PDF failed. A public reproduction of the original 1978 article was opened, with original title, receipt date and page headers. Introduction and section 2.1 read; damaged mathematical OCR does not certify exact normalization. |
| Takhtajan Faddeev 1974 essentially nonlinear classical field; Korepin Faddeev 1975 quantization | Math-Net `tmf3879` and `tmf4060`, with full primary PDFs. Read classical Hamiltonian/scattering assumptions and kink/breather energies; then zero-mode treatment, determinant, renormalization, one-loop mass, phase and Bohr–Sommerfeld rule. Most of Faddeev's examples were already published before the seminar. |
| “Sklyanin Faddeev 1978 Quantum approach completely integrable” | Math-Net `dan42231`, full four-page primary paper. Explicit quantum nonlinear-Schrödinger construction read; the authors say the parallel sine-Gordon comparison was not yet completed. This is a precise early solution of the model-specific method problem, not universal quantization. |
| Zamolodchikov 1977 exact sine-Gordon S matrix; transmission reflection; mass ratios | Springer CMP metadata plus a full primary JETP Letters PDF at Freie Universität Berlin. The latter gives both channels, exact breather mass ratios, renormalized coupling and reflectionless values. Receipt, publication and first-appearance dates are kept separate. |
| “Higher order correction sine-Gordon soliton mass de Vega Verwaest” | Search located J. Verwaest's 1977 article and publisher metadata, but the full publisher page was inaccessible. It is not cited as a verified calculation. The displayed physical-mass expansion instead follows algebraically from the separately read exact mass-ratio formula. |
| Fröhlich quantized sine-Gordon nonvanishing mass; Coleman massive Thirring equivalence | APS primary abstracts and metadata opened. Their exact full hypotheses are not inferred from a partially rendered abstract. The coupling threshold is distinguished from the breathers' bound-state threshold and from the vague claim that solitons disappear. |
| Short-range wave operators asymptotic completeness Yafaev | Primary author lecture notes, arXiv `math/0403213`, Theorem 2.4 and proof and equation (2.8). Used for precise hypotheses of an older scattering result, not historical priority. |
| Pohlmeyer quadratic constraints sphere sigma model; Zakharov Mikhailov relativistic models | Pohlmeyer publisher abstract/dates and the full Zakharov–Mikhailov author-archive PDF. Introduction and sections 1–3 read; Grassmann versus general Stiefel scope and section 6 checked. The source does not prove all homogeneous-space models integrable. |
| O(N) factorized S matrix Zamolodchikov 1978 | Full primary Nuclear Physics B article in university-hosted PDF. Introduction and sections 2–3 read. Authors' own distinction between the algebraic S matrix and evidence for sigma-model identification is retained. |
| Chen Liu Lu sine-Gordon long-time asymptotics soliton resolution | Primary arXiv `2009.04260`, version 2. Theorems 1.1/10.1, Definition 2.6 and weighted spaces read. Requires generic scattering data, weighted regularity and distinct speeds; radiation has modified scattering. |

The final recency-filtered search was exactly **`"sine-Gordon" "soliton resolution" "finite energy" 2025 2026`**, with a 1000-day recency setting. It returned, among other results, Jendrej's 2025 EMS survey, a 2023 kink-stability paper, a wormhole problem and a 2026 finite-volume sine-Gordon comparison. None was used as evidence of an all-finite-energy flat-space resolution theorem. Those different questions do not upgrade the checked Chen–Liu–Lu theorem. Search failure is recorded as a limitation of verification, not proof that a result does not exist.

## Chronology and exactness decisions

The BGG papers were presented to the Academy on 9 January 1978 and published in March 1978. The theorem data distinguish bounded central support, regularity and neighborhood size. These are class A results with explicit restrictions. Elementary category definitions and Morita examples are class E. A wrong notebook Casimir is a faithful error within class E background, with a partial publication match rather than a claim that the published theorem repeats the error. Elementary normalizer and annihilator identities and the familiar reducible principal series are also E; the later block-equivalence theorem is A. The KP equation and compatibility method are E, whereas the rational-pole classification and commuting particle flows are A.

Krichever's effective rank-one construction was already announced in 1976; the 1977 Methods survey was received on 24 March 1977 and explicitly contains the theta and Jacobian formulas. The occurrence is therefore class E, even though the closest historical discussion is in the 1978 paper. A submission date is evidence of submission, not by itself evidence of public circulation. The log and data do not convert every receipt date into a first-publication date.

The AHS deformation theorem and the Atiyah–Ward announcement appeared before Novikov's talk. Drinfeld–Manin's short construction was received 27 November 1977, six days after the source date of Manin's talk, and published in 1978; the longer monad paper was received 26 May 1978 and published in 1979. The later monad statement is checked under its admissibility hypotheses, not imposed on all bundles on projective three-space.

Takhtajan–Faddeev 1974, Korepin–Faddeev 1975 and Zamolodchikov 1977 already contain much of the sine-Gordon material. The 1978 review is not treated as the first publication of the one-loop mass or breather rule. Its receipt date is 4 July 1977. The quantum inverse-scattering announcement is later in 1978. The O(N) S-matrix paper was received in August 1977, revised in November and published in February 1978; its relation to the final notebook remark is partial and its authors' own field-theory qualification is preserved.

## Earlier-year links

The supplied earlier index was searched for exact recurrences and related constructions, including the relevant GP identifiers and occurrence titles. Decisions:

* **GP-1975-26 is not reused for record 431.** It concerns reconstruction of higher-rank commuting ordinary differential operators. The actual short 1977 text explicitly discusses scalar operators of relatively prime orders and a historical comparison; expanding it to a higher-rank theorem would alter the source.
* **GP-1975-14 and occurrences 1975-383.9–383.12, 1975-385.4–385.8** concern the rank-one pointed-curve inverse correspondence. Item 431.2 links them as closely related prior construction data, while retaining the distinction between a historical classification assertion and an explicitly restated inverse problem. Earlier 1975-374.5 and 1975-380.2 are also noted. No new identifier is fabricated for a historical theorem.
* **1975-382.5**, the tautological universal connection and its correct base, has no GP identifier. Item 435.6 explicitly records that earlier construction. The 1977 bracketed universality question has the stated quantifiers and receives GP-1977-25; no nonexistent earlier GP identifier is invented.
* **1975-372.7 and 1975-372.12** concern particle integrability, related to GP-1977-22 but not the same rational-KP classification problem.
* **1975-372.16** is the sine-Gordon/massive-Thirring correspondence. It is background for the 1977 coupling discussion, not an exact recurrence of the notebook's soliton-resolution or quantum-inverse-scattering questions.

## Computation, development and limitations

For the notebook equation

`3 u_yy + (4 u_t + 6 u u_x + u_xxx)_x = 0`

and `u=-2 sum (x-q_i)^(-2)`, with `p_i=q_i,y`, Laurent coefficients give

`q_i,yy = -8 sum_{j!=i} (q_i-q_j)^(-3)` and

`q_i,t = 3 p_i^2/4 - 3 sum_{j!=i} (q_i-q_j)^(-2)`.

Thus the canonical Hamiltonians in the items have coefficients `-4` and `-3`, respectively. The assembler independently derived the formulas and saved `work/code/check_kp.py` and `work/code/output/kp_checks.json`. The Lax time sign and missing scalar coefficient are also checked there. This is an annotation of a published A result, **not an independently solved C/D problem** and not an allegation that a differently normalized published theorem is false.

The no-higher-mass-corrections assertion cannot be assessed without specifying the renormalized mass parameter. The physical lightest-breather convention gives `M/m_1 = 8/g - 1/pi + g/192 + O(g^2)` from the checked exact mass ratio. This is an editorial algebraic consequence, not evidence that Faddeev used that mass convention. It is not entered as a definite untouched open problem.

The only class C items in this contribution are the classification of all finite-action Yang–Mills critical points, beyond the explicitly classified instanton minima, and the unrestricted soliton-resolution formulation. Both state exactly what the checked partial results establish and which larger quantifiers are not verified. No class D claim is made. Under-specified classical-to-quantum solvability, an ambiguous higher-loop functional, an unidentified 1939 citation, additional group calculations, and unpublished Hermitian quadruple data remain class F with their respective source limitations.

No separate breather counterexample is presented as a new development: breathers are already explicitly recognized on P000748, and the broader word “soliton” in the notebook can include them. Item 436.5 is only annotated; the exact generic weighted-data theorem uses modified radiation. `development.tex` contains explanatory comments and no unproved independent theorem. The assembler chooses the chapter's deep development separately.

Final validation checked consecutive occurrence numbers, required fields, allowed literal-correctness values, C/D worth fields, all citation keys against each item's references, all cited keys against BibTeX and reference-audit rows, area-map coverage and accidental control characters. No schema or reference-coverage errors remained. The assembler performs the final common-style LaTeX build and independent mathematical checks.
