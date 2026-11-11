# GY1982: editorial and research report

**Scope:** I. M. Gelfand seminar, academic year 1982–83. **Status cutoff:** November 2026. **Deliverable:** a critical companion, occurrence index, problem index, correction ledger, and one fully worked bounded development.

## 1. Coverage and reading decisions

All **37 supplied catalog records** are represented, with **335 mathematical items**, **19 indexed problems**, **119 bibliography entries**, and **143 correction-ledger entries**. Record 579 is the year heading and has no invented mathematical item. These are occurrence counts: a theorem repeated in another talk receives another occurrence, while the problem index joins exact recurrences.

The 90 supplied images cover P001026–P001115. The last image explicitly starts Deligne’s talk of **5 September 1983**. It is evidence for the packet boundary, not a mathematical occurrence of the 1982–83 academic year. The present chapter covers the preceding 89 source pages. The original catalog ranges are retained in the talk data even where they include neighboring material. Each item has a narrower locator based on the actual source. In particular, the April source sequence is **594, 593, 596, 595, 598**; numerical catalog order would misrepresent the sequence in the notebook. Wodzicki’s record 598 is an interruption within the last Beilinson discussion.

The Russian diplomatic transcription was treated as the textual authority, with the English used as a reading aid. Scans were checked where a sign, index, drawing, cancellation, inserted qualification, or ambiguous name affected the mathematics. An assertion first written too broadly but repaired later on the same page is assessed with that repair. For example, the invariant-form restriction and the corrected contracting form in the equivariant-cohomology discussion are part of the notebook’s own argument. The supplied transcriber’s uncertainty markers were not converted into guessed text.

The three layers remain separate in every item: **notes**, **precise statement**, and **reconstruction**. A precise statement may be a valid restricted replacement for an invalid literal formula; the separate correctness and publication-match axes make that distinction explicit. The reconstruction field identifies added assumptions, conventions, and interpretations. The companion does not silently repair the source files themselves.

## 2. Counts

The following counts are computed from the final JSON and CSV, rather than manually maintained estimates. `code/validation_statistics.json` records the same totals and additional assessment-axis counts.

### By class

| Class | Meaning | Items | Share |
| --- | --- | --- | --- |
| A | Speaker-associated near-contemporary publication | 47 | 14.0% |
| B | Established later development by others | 29 | 8.7% |
| C | Specified partial resolution | 3 | 0.9% |
| D | Documented lack of development | 0 | 0.0% |
| E | Known before the talk | 214 | 63.9% |
| F | Formulation or identification unresolved | 42 | 12.5% |
| Total |  | 335 | 100% |

Class A records a speaker-associated publication, not a certification that every formula in the notebook was already correct. Class E records prior mathematical knowledge, even when the source needs an emendation. Class B includes established negative answers and later rigorous versions with explicitly stated scope. Class F records an identification or formulation limit; it is not evidence of an untouched open problem. There is no D assignment based solely on an unsuccessful search.

### By catalog speaker

| Catalog speaker | Records | Items |
| --- | --- | --- |
| A. A. Beilinson | 2 | 12 |
| A. A. Kirillov | 4 | 27 |
| A. A. Migdal | 1 | 8 |
| A. B. Zamolodchikov | 4 | 51 |
| A. M. Polyakov | 1 | 22 |
| A. S. Schwarz | 1 | 10 |
| B. L. Feigin | 1 | 8 |
| D. B. Fuchs | 1 | 9 |
| George Wilson | 3 | 19 |
| I. M. Gelfand | 1 | 4 |
| I. M. Krichever | 1 | 6 |
| I. Yu. Kobzarev | 1 | 10 |
| J. Fröhlich | 2 | 38 |
| M. A. Semenov-Tian-Shansky | 1 | 4 |
| Mariusz Wodzicki | 3 | 22 |
| S. P. Novikov | 1 | 3 |
| V. I. Arnold | 1 | 24 |
| V. L. Ginzburg | 4 | 30 |
| Ya. G. Sinai | 1 | 8 |
| Yu. A. Neretin | 1 | 10 |
| Yu. I. Manin | 1 | 10 |
| Total mathematical records | 36 | 335 |

These totals use the speaker attached to each catalog record. An intervention by Gelfand or another participant remains within that record’s count and receives an explicit `speaker` field where identified. This convention prevents double counting and should not be read as a count of individual authors’ discoveries.

The final provenance review withdrew an unsupported preference for V. A. Ginzburg as the speaker of record 570. The supplied catalogue’s V. L. and the manuscript’s shorter V. are retained. Authorship of a mathematically relevant paper does not establish who gave an expository talk. The correction is documented in `research/root/provenance_review.md`; the final data and editorial patch supersede that inference in the archived authoring drafts.

### By primary subject area

| Primary reporting area | Records | Items |
| --- | --- | --- |
| Representation theory and homological algebra | 8 | 57 |
| Quantum field theory, strings, and conformal theory | 11 | 149 |
| Dynamical systems and perturbation theory | 2 | 32 |
| Symplectic and integral geometry, and localization | 5 | 36 |
| Integrable systems and Hamiltonian methods | 6 | 32 |
| Spectral analysis and index theory | 2 | 20 |
| Arithmetic geometry and zeta functions | 2 | 9 |
| Total | 36 | 335 |

For an additive table, each record is assigned one primary area; all its items inherit that reporting category. This is an editorial reporting convention, not a claim that mixed talks have only one subject. `code/area_by_record.json` gives the assignments, and `code/report_statistics.json` records the derived totals. A future website should support multiple subject tags while keeping an explicitly defined denominator for statistics.

### Other assessment axes

| Literal correctness | Items |
| --- | --- |
| correct | 7 |
| correct with missing hypotheses | 197 |
| false as written | 91 |
| not determinable | 40 |

| Publication match | Items |
| --- | --- |
| exact | 163 |
| none found | 11 |
| partial | 140 |
| thematic only | 21 |

| Verification | Items |
| --- | --- |
| indirect | 11 |
| publisher metadata checked | 36 |
| read the result | 269 |
| unresolved lead | 19 |

| Development | Items |
| --- | --- |
| annotated | 269 |
| developed in this chapter | 1 |
| none | 65 |

| Confidence | Items |
| --- | --- |
| high | 283 |
| low | 17 |
| medium | 35 |

The 197 entries marked “correct with missing hypotheses” chiefly measure the compression of seminar notes: a compactness assumption, domain, field, spectral cut, or normalization must be supplied before the modern statement is valid. They are different from the 91 literal errors. An error faithfully written in the notebook is also different from a transcription error. Neither count is an estimate of how many false claims the speaker intended to make.

## 3. What the literature search resolved

The strongest matches came from short original Soviet publications, primary author copies, and bibliographies that distinguished an early announcement from a later expanded treatment. A title match alone was not taken to establish a theorem match. The accompanying research audits give opened URLs, theorem or page locators, verification levels, failed leads, and search terms.

Several matches materially change the historical reading:

- **The string-charge question has a later algebraic existence answer.** The formal cyclic-charge Poisson algebra can be quantized through the quasi-Lie-bialgebra construction of Enriquez and Halbout (2010), as applied explicitly by Bahns and Meinecke (2011). This does not validate naive normal ordering of the particular notebook operators, and it does not supply a preferred positive Hilbert-space representation. The latter requirement was not inserted into the original question to manufacture a remaining class-C problem. See items 1982-562.7–10 and GP-1982-01.
- **Beilinson’s gluing discussion has documentary continuity with these notes.** The introduction of *How to glue perverse sheaves* states that the exposition follows S. I. Gelfand’s notes of 1982. The disk description by nearby and vanishing cycles therefore has a much firmer link than a merely thematic resemblance between D-modules and later perverse-sheaf theory. See record 574 and Beilinson (1987, Corollary 3.2).
- **Polyakov’s accessory-parameter relation became a theorem with normalization fixed.** The regularized classical Liouville action and the accessory parameters require a sign and numerical coefficient. The Zograf–Takhtajan announcement and detailed proof identify the exact punctured-sphere conjecture; the chapter does not treat an unregularized action identity as an exact quantum formula. See item 1982-577.9 and GP-1982-21.
- **The integrable-systems sequence has exact contemporary publications.** Krichever’s 1983 note supplies the missing hypotheses and correct gap-opening modes; Semenov-Tian-Shansky’s 1983 paper fixes the normalization of the factorization flow; Segal and Wilson (1985) give the precise Grassmannian, determinant, Baker-function, and hierarchy statements. The newer publication can contain a valid theorem even when the notebook’s abbreviated formula fails a simple limiting case.
- **Arnold’s publication records antecedents explicitly.** The supplement dated 30 March 1983 in Arnold (1983) credits Bloch, Levy–Keller, and Hochstadt for earlier versions of the gap estimates. Those bounds are classified as prior knowledge; the particular bracket and duality presentation is assessed separately. The recorded lower-bound-like asymptotic cannot replace an upper bound, and smoothness alone does not imply the exponential decay available under analyticity. See record 585.
- **The arithmetic status required a current check.** Boxer, Calegari, Gee, and Pilloni (2021, Theorems 1.1.2–1.1.3) prove the Hasse–Weil meromorphic-continuation and functional-equation consequence for every genus-two curve and abelian surface over a totally real field. Their 2025 preprint proves actual modularity for an additional specified class. Its Theorem B concerns a smooth genus-two curve X over Q with a model y² = f(x) of degree five, the mod-3 representation of its Jacobian surjective onto GSp4(F3), and good ordinary reduction of X at 2 and 3. Gee’s 2026 account confirms the distinction. Meromorphic continuation, holomorphy, potential automorphy, and actual automorphy are not interchangeable. Accordingly GP-1982-42 and GP-1982-43 remain distinct.

Publication chronology is recorded at its evidential strength. A manuscript’s receipt date is not automatically its date of public circulation. The chapter distinguishes a documented preprint or prior announcement from receipt and publication. This matters for the 1981 announcement behind Schwarz’s charge-reversing strings, the pre-talk work behind Neretin’s constructions, the 1983 numerical period-tripling publication, and the 1982 notes underlying Beilinson’s 1987 exposition. Where first circulation could not be verified, it is not invented.

The bibliography’s `note = {verified}` means that the recorded URL or DOI, or its expressly identified primary-source route, was opened. It does not mean that every proof in the work was rechecked. The item-level verification field and the per-reference audit distinguish direct reading of a result, publisher or institutional metadata, an indirect account, and an unresolved lead. Metadata-only matches remain labeled as such even when the underlying mathematics is standard.

## 4. Mathematical and textual difficulties

The most important difficulty was preserving conventions without mistaking them for errors. Reversing a cocycle, passing between highest- and lowest-weight modules, changing the sign of a Laplacian, or normalizing an action can alter a displayed formula consistently. The companion fixes a convention in the precise statement, checks it against the surrounding brackets or equations, and records an emendation only when the literal formula is inconsistent or the handwriting disagrees with its transcription.

Some errors are decisive. The affine Cartan example has a wrong diagonal sign; a Virasoro or KP normalization cannot be repaired by silently dropping a factor; the stationary-phase denominator for a positive-dimensional fixed component requires its equivariant Euler class, not just a constant Pfaffian. In Fedosov’s discussion, the first orthogonal block projector requires the quadratic partition relation f₁² + f₂² = 1; the later idempotent pair is algebraically idempotent without that relation, and its separate issue is compact support. In the SU(3) orbit diagram, the written invariants `tr(A²), tr(A³)` are constant on the orbit, whereas the hexagon requires the diagonal torus moment map. These are recorded as mathematical emendations when faithfully present in the manuscript, rather than charged to the transcription.

The final Virasoro lecture provides an especially useful control case. Its reverse Witt convention becomes the standard convention under ℓₙ = −Lₙ and h = −Δ. At the first nontrivial test pair, the recorded reducibility polynomial is 16Δ² − 2(c − 5)Δ + c, exactly the standard level-two factor after that substitution. Independent calculations therefore retained the polynomial. The missing cubic central factor, the incompatible primary-covariance sign, and the final Laurent coefficient labels require separate repairs. A second reviewer checked that the modern notation is consistent throughout record 573; `research/spring_integrable/record573_review.md` records the calculation and the resolved editorial finding.

Arithmetic has a different type of ambiguity. The finite-field point-count series, its exponential zeta function, the global arithmetic Euler product, and an individual cohomological L-factor are different objects. An exponential and a divisor by the extension degree are missing in the local definition; a Frobenius eigenvalue, a zero in the local variable, and a real part in the complex `s` plane must not be conflated. The last BSD heading contains a continuation and functional-equation discussion, but no rank equality or leading-coefficient formula. The chapter therefore does not add a new BSD problem occurrence that the surviving notes do not state.

Several fragments could not be promoted to a definite problem: the topology of a continuous Grassmannian without a chosen topology; an integration theory attached to all abelian varieties without specified equations; group-free localization without replacement structures; and the exact pseudodifferential-operator realization intended by the Shintani remark. A nearby modern theory is recorded as context only when it does not answer the original quantifiers. These F entries retain useful information about the seminar’s questions without assigning a false solved/open status.

## 5. The development and its independent check

Only one C item had both an unambiguous recorded formula and a useful bounded calculation: **1982-565.6 / GP-1982-02**, the four-unitary matrix integral. Its exact notebook convention has a negative exponent and a sum over all ordered pairs, including diagonal terms. Haar measure is explicitly reconstructed as probability Haar measure. Removing the diagonal or reversing the sign would change the answer.

For fixed `d` and matrix size `N`, write

\[
F_{d,N}(\beta)=N^{-2}\log\mathbb E\exp\{-\beta N\sum_{\mu,\nu=1}^{d}\operatorname{Tr}(U_\mu U_\nu U_\mu^*U_\nu^*)\}.
\]

The development gives complete proofs of finite-size real analyticity, convexity, uniform Lipschitz bounds, subsequential compactness, and the exact first two derivatives for `N ≥ 2`:

\[
F'_{d,N}(0)=-d-\frac{d(d-1)}{N^2},\qquad
F''_{d,N}(0)=d(d-1)\left[\frac{N^2+4}{N^2-1}+\frac{4d-10}{N^2}\right].
\]

The scalar case is handled separately: `F_{d,1}(β) = −d²β`. The limiting expansion

\[
F_4(\beta)=-4\beta+6\beta^2+O(\beta^3)
\]

is justified by the small-potential large-unitary-integral theorem of Collins, Guionnet, and Maurel-Segala (2009, Theorem 0.1; preprint 2006), rather than inferred from finite-size numerical evidence. This is a statement near zero about the analytic limiting function. It is not a uniform finite-size remainder bound and not an evaluation at arbitrary coupling. The chapter makes no priority claim for the elementary coefficient formulas.

The independent check uses a different derivation. The proof conditions on a shared Haar matrix and uses character orthogonality. `code/haar_check.py` instead expands trace words into indices, applies the degree-one and degree-two Weingarten formulas, and counts free index loops. It checks six basic mixed moments as exact rational functions, then sums **584 ordered plaquette pairs** for `d = 2, 3, 4, 5`. Additional evaluations use `N = 2, 3, 4, 7, 11`. All checks agree; for `d = 4`, the second derivatives at `N = 2, 3, 4` are `50, 55/2, 41/2`. The singular low-rank boundary is explicitly excluded from the rational formula and verified separately. Code, stdout, and machine-readable results are included. A separate reviewer also derived the same moments from \(\mathbb E\chi_\rho([U,V])=1/\dim\rho\), using the symmetric-square, exterior-square, and adjoint character decompositions, and independently recounted adjacent plaquettes. The reviewer reopened Theorem 0.1 and Corollary 7.1 of the primary large-matrix paper and checked the hypotheses and the exchange of derivatives and limits. The isolated rerun and character computation both pass. The review records the hashes of the version reviewed; a subsequent explanatory paragraph added that same character argument without changing the result. See `research/spring_integrable/development_review.md` and its computation outputs.

The checked literature did not provide an all-coupling evaluation of this exact, unmodified four-unitary integral. This is the stated limit of a bounded search, not a proof of absence. Quenched or twisted reductions and recent calculations for different matrix models are not substituted for the displayed integral. A further bounded run could compute higher connected Haar cumulants and quantify a local interval. It could not responsibly promise a global solution or the continuum QCD equivalence. The arithmetic C items are much broader and do not have a similarly bounded new theorem justified by this run.

## 6. Earlier occurrences and editorial method

| Reused ID | Question | Earlier occurrences | This year |
| --- | --- | --- | --- |
| GP-1981-41 | Geometric realization of compact-group weight multiplicities | 1981-556.1, 1981-556.6 | 1982-584.5 |
| GP-1981-44 | Spectral zeta constructions without self-adjointness | 1981-559.8, 1981-559.13, 1981-559.14 | 1982-590.2 |
| GP-1981-43 | Eta regularity without a bounding manifold | 1981-559.9 | 1982-590.9 |

Other cross-year links are contextual: the 1973–77 finite-gap and KP sequence, the 1978 twistor construction, the 1981 superspace formulation, older Schubert geometry, and earlier moment-map discussion. These links are not enough to reuse a problem ID. An exact recurrence requires the same mathematical object, scope, and question. Previous unresolved fragments are not silently given a new meaning through later terminology.

The A–F classification usefully tracks historical fate but misses several dimensions that matter this year. It cannot by itself distinguish an exact contemporary match from a corrected reconstruction; a numerical discovery from a theorem; an abstract existence result from an explicit operator realization; or a current partial theorem from the original unrestricted proposal. The required assessment axes supply much of that information. For future chapters, the following additions would improve the common format without replacing those axes:

| Proposed field or relation | Why this year needs it |
|---|---|
| Structured source spans, separate from catalog page ranges | Several records share pages, two April orders are reversed, and one packet page belongs to the next year. |
| Separate catalog name, manuscript heading, and identified person, with evidence | Initials and related publications are insufficient to merge speakers; record 570 exposed this risk. |
| Separate `received`, `first_circulated`, and `published` dates, each with evidence | Receipt is not circulation, and later expositions sometimes explicitly reproduce earlier seminar notes. |
| A correction-to-item relation and a distinct notebook-error flag | Readers need to tell a transcription correction from a mathematical emendation. |
| Theorem locator and source-access level per claim | One item may cite a full result and a metadata-only historical lead. |
| Hypothesis/convention tags | Field, compactness, regularity, spectral cut, normalization, and parameter range repeatedly determine validity. |
| Multiple typed cross-links | “Same problem,” “special case,” “background,” “corrects,” and “later implementation” should not all mean “related.” |

These are proposals for the shared data model. The delivered seven principal files follow the supplied format; supplementary audits are kept separately.

## 7. Presentation on the companion website

A reader arriving at one talk should first see its short summary and source boundaries, followed by the item list. Opening an item should immediately expose the recorded statement, the precise statement, the correction or reconstruction if needed, and the dated fate with a direct theorem-level source link. The assessment fields should remain visible together. Displaying class A or E alone would hide the substantial number of literal formula errors found this year.

The most useful routes are the Virasoro/string/Liouville chain; the finite-gap-to-Grassmannian chain; orbital integrals-to-localization; and the spectral-zeta-to-arithmetic transition with its differences made explicit. Exact problem recurrences should navigate across years through stable GP identifiers. Contextual links to earlier items should carry their weaker relation type. The matrix question should link directly to its proved local expansion, the unchanged original normalization, and the reproducible computation. Arithmetic entries need a clear distinction between continuation, potential automorphy, and actual modularity.

An F badge should read “formulation or identification unresolved,” with the precise missing data shown. A failed search must not be presented as a research opportunity merely because no publication link is attached. Filters by speaker, primary and secondary area, verification level, and literal correctness would be more informative than a single solved/open toggle. The website should also expose source-order navigation independently of calendar or catalog-number sorting.

## 8. Build, validation, and archive contents

The supplied `build_chapter.py` and `gelfand_companion.sty` are unchanged and included, together with copies under `code/kit_original`. The requested builder was run, followed by XeLaTeX, BibTeX, and two further XeLaTeX passes. The environment lacked a prebuilt XeLaTeX format; a local format was generated from the installed TeX Live sources without changing system files. `code/rebuild.py` documents and reproduces that fallback when needed. On an ordinary TeX installation, the standard commands in `CHAPTER_FORMAT.md` suffice.

**Final result:** the 179-page PDF builds successfully with no undefined citations or cross-references, no missing-glyph warnings, no LaTeX errors, and no overfull boxes. Automated inspection of every PDF page found no text outside the page, no replacement characters, and no empty pages. Rendered pages were reviewed for the overview, item layout, mathematical displays, Cyrillic quotations, development, problem index, correction entries, and bibliography; the details are recorded in `code/visual_review.json`. The source audit covers all 119 bibliography entries, and all 91 items marked false as written have a checked correction-ledger link. Source coverage and final statistics are recorded in `code/source_coverage.json` and the validation outputs.

Additional checks cover all 37 records; consecutive academic-year item IDs; actual source order; required fields and allowed assessment values; reference existence and citation keys; problem backlinks; dates; control characters; bibliography verification notes; and exclusion of next-year page P001115 from mathematical items. The original attachment sizes and SHA-256 values are recorded in `code/input_manifest.json`. The bibliography reconciliation audit records reuse of cumulative keys and any duplicate metadata handled during assembly.

The archive contains the seven requested data/LaTeX/bibliography files, this report, the generated chapter, the standalone driver and compiled PDF, the supplied build assets, the computation and its output, validation logs, and research/source audits. The final data files are authoritative. The assembly scripts document how independently researched groups were combined; the rebuild script uses the final edited data directly. Full copies of later published papers are not redistributed.

## Selected references for this report

Arnol’d, V. I. (1983). Remarks on the perturbation theory for problems of Mathieu type. *Russian Mathematical Surveys, 38*(4), 215–233. [Primary source and publication metadata](https://www.mathnet.ru/eng/rm2950).

Bahns, D. (2004). The invariant charges of the Nambu–Goto string and canonical quantization. *Journal of Mathematical Physics, 45*(12), 4640–4660. [Primary author preprint](https://arxiv.org/pdf/hep-th/0403108).

Bahns, D., & Meinecke, J. D. A. (2011). *String quantization and the shuffle Hopf algebra* [Preprint]. arXiv. [Full text](https://arxiv.org/pdf/1103.0974).

Beilinson, A. A. (1987). How to glue perverse sheaves. In *K-theory, arithmetic and geometry* (Lecture Notes in Mathematics, Vol. 1289, pp. 42–51). Springer. [Primary text](https://people.mpim-bonn.mpg.de/gaitsgde/grad_2009/Beilinson%20--%20How%20to%20glue%20perverse%20sheaves.pdf).

Boxer, G., Calegari, F., Gee, T., & Pilloni, V. (2021). Abelian surfaces over totally real fields are potentially modular. *Publications Mathématiques de l’IHÉS, 134*, 153–501. [Full text and DOI](https://www.numdam.org/articles/10.1007/s10240-021-00128-2/).

Boxer, G., Calegari, F., Gee, T., & Pilloni, V. (2025). *Modularity theorems for abelian surfaces* [Preprint]. arXiv. [Metadata and full text](https://arxiv.org/abs/2502.20645).

Collins, B., Guionnet, A., & Maurel-Segala, E. (2009). Asymptotics of unitary and orthogonal matrix integrals. *Advances in Mathematics, 222*(1), 172–215. [Primary author preprint](https://arxiv.org/pdf/math/0608193).

Collins, B., & Śniady, P. (2006). Integration with respect to the Haar measure on unitary, orthogonal and symplectic group. *Communications in Mathematical Physics, 264*(3), 773–795. [Primary author preprint](https://arxiv.org/pdf/math-ph/0402073).

Enriquez, B., & Halbout, G. (2010). Quantization of quasi-Lie bialgebras. *Journal of the American Mathematical Society, 23*(3), 611–653. [Primary author preprint](https://arxiv.org/pdf/0804.0496).

Gee, T. (2026). Modularity theorems for abelian surfaces. In S. Friedlander & Y. Tschinkel (Eds.), *Proceedings of the International Congress of Mathematicians 2026, Volume 3: Invited lectures (Sections 1–4)* (pp. 377–395). Society for Industrial and Applied Mathematics. [Full text and DOI](https://epubs.siam.org/doi/full/10.1137/25M1806697).

Krichever, I. M. (1983). “Hessians” of integrals of the Korteweg–de Vries equation and perturbations of finite-zone solutions. *Doklady Akademii Nauk SSSR, 270*(6), 1312–1317. [Primary text and metadata](https://www.mathnet.ru/eng/dan46140).

Neuberger, H. (2020). Quenched Eguchi–Kawai model revisited. *Physical Review D, 102*(9), Article 094503. [Primary text and metadata](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.102.094503).

Segal, G., & Wilson, G. (1985). Loop groups and equations of KdV type. *Publications Mathématiques de l’IHÉS, 61*, 5–65. [Full text](https://www.numdam.org/item/PMIHES_1985__61__5_0.pdf).

Semenov-Tian-Shansky, M. A. (1983). What is a classical r-matrix? *Functional Analysis and Its Applications, 17*(4), 259–272. [Primary text and metadata](https://www.mathnet.ru/eng/faa1574).

Zograf, P. G., & Takhtadzhyan, L. A. (1985). Action of the Liouville equation is a generating function for the accessory parameters and the potential of the Weil–Petersson metric on the Teichmüller space. *Functional Analysis and Its Applications, 19*(3), 219–220. [Primary announcement and metadata](https://www.mathnet.ru/eng/faa1385).

Zograf, P. G., & Takhtadzhyan, L. A. (1988). On Liouville’s equation, accessory parameters, and the geometry of Teichmüller space for Riemann surfaces of genus 0. *Mathematics of the USSR-Sbornik, 60*(1), 143–161. (Russian original published 1987.) [Primary text and metadata](https://www.mathnet.ru/eng/sm1767).

The full annotated bibliography and exact item-level locators are in `GY1982_references.bib` and the chapter. The selected references above support the report’s central methodological decisions; they do not replace the per-item source audit.
