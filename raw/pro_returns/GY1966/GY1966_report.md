# GY1966 research and verification report

**Scope:** I. M. Gelfand seminar, academic year 1966–67; MCCME records 92–129; scans P000140–P000207. **Status date:** 9 November 2026.

## 1. Outcome and editorial scope

The chapter covers **38 catalogue records, 277 mathematical occurrences, 21 indexed problems, 78 bibliographic entries, and 108 corrections or qualifications**. There are 20 new problem identifiers, assigned consecutively by first occurrence, and one reused identifier, **GP-1965-03**. Every record remains in catalogue order, including the three zero-item records 117, 118, and 128. The order is not silently sorted by calendar date.

The companion separates the notebook report, a precise mathematical statement, and the editorial reconstruction in every occurrence. A statement's historical fate is independent of its literal correctness. Newly supplied counterexamples and proofs are marked `\ours`; computations are marked `\oursComputed`. Those marks mean that the derivation or calculation was performed for this companion. They do **not** claim publication priority or mathematical novelty.

The three C items are the general algebraic topological classification of Anosov diffeomorphisms, the smooth-metric part of the exact Helgason sphere-support problem, and smooth classification under equal prime geodesic periods. None yielded a plausible bounded research advance in this run. No D item is justified. The full proof section is a **critical annotation of Minlos's published variance argument**, not a claim to solve one of those open problems. Its conclusions and scope are explicit below.

The source scans were visually examined across all 68 pages, with particular attention to formula-dependent conclusions and ambiguous headings. `code/source_page_coverage.csv` maps scan pages to occurrences. The `talk.pages` fields retain broad catalogue intervals in the early records and use refined actual-content spans in several later records; the summaries explain boundaries. The narrower `item.pages` fields follow the actual handwritten content. All original catalogue intervals remain recoverable in the included source list, including record 127's continuation beyond its catalogue endpoint.

## 2. Counts

### Items by historical class

| Class | Items |
|---|---:|
| A | 22 |
| B | 45 |
| C | 3 |
| D | 0 |
| E | 185 |
| F | 22 |
| **Total** | **277** |

A: publication soon after by the speaker or Gelfand; B: development by others; C: a delimited partly developed question; D: a supported undeveloped item; E: prior mathematics or exposition; F: the notes do not identify an exact assertion adequately. An F item may still have a recognizable subject and useful related literature.

### Items by catalogue speaker

| Catalogue speaker | Items |
|---|---:|
| I. M. Gelfand | 17 |
| D. A. Kazhdan | 8 |
| V. I. Arnold | 79 |
| G. E. Shilov | 8 |
| I. N. Bernstein | 19 |
| R. A. Minlos | 35 |
| Lee Lorch | 5 |
| Louis Nirenberg | 14 |
| M. I. Vishik | 9 |
| O. A. Oleinik | 7 |
| M. S. Agranovich | 16 |
| A. A. Kirillov | 23 |
| A. S. Dynin | 17 |
| A. N. Parshin | 6 |
| S. I. Gelfand | 14 |
| **Total** | **277** |

These are **catalogue-attribution counts**, not assertions of personal authorship. The 15 geometry-list items in record 114 carry an explicit unattributed-speaker override. Three items under record 124 belong to the handwritten **D. V. Anosov** intervention. Gelfand's other interventions also carry overrides. Empty-speaker headings have no mathematical items and do not enter this table.

### Items by primary area

| Primary area | Items |
|---|---:|
| Topology and singularity theory | 54 |
| Lie groups, representations and algebraic quotients | 41 |
| Dynamical systems | 18 |
| Functional analysis and infinite-dimensional equations | 8 |
| Hyperbolic, fluid and heat equations | 31 |
| K-theory, index theory and elliptic/PDO analysis | 60 |
| Statistical mechanics and probability | 35 |
| Sturm-Liouville theory and special functions | 5 |
| Symplectic, Maslov and semiclassical analysis | 10 |
| Differential geometry | 15 |
| **Total** | **277** |

Areas are mutually exclusive editorial bins for counting, not a taxonomy of mathematical dependence. The exact assignment of every item is saved in `code/item_areas.json`. Elliptic family indices are counted with K-theory/PDO analysis; lacunas with hyperbolic equations; the differential-geometry list contributes 15 geometry items and one PDO heading item. This prevents totals from drifting through double counting.

### Record-level audit

| Record | Catalogue speaker | Kind | Items | A | B | C | D | E | F |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|
| 92 | I. M. Gelfand | talk | 3 | 0 | 0 | 0 | 0 | 3 | 0 |
| 93 | D. A. Kazhdan | talk | 4 | 0 | 2 | 0 | 0 | 2 | 0 |
| 94 | V. I. Arnold | talk | 18 | 0 | 5 | 1 | 0 | 12 | 0 |
| 95 | G. E. Shilov | talk | 8 | 8 | 0 | 0 | 0 | 0 | 0 |
| 96 | I. M. Gelfand | talk | 7 | 0 | 1 | 0 | 0 | 5 | 1 |
| 97 | I. N. Bernstein | talk | 6 | 0 | 0 | 0 | 0 | 6 | 0 |
| 98 | I. N. Bernstein | talk | 9 | 0 | 1 | 0 | 0 | 6 | 2 |
| 99 | R. A. Minlos | talk | 11 | 0 | 0 | 0 | 0 | 11 | 0 |
| 100 | R. A. Minlos | talk | 12 | 2 | 0 | 0 | 0 | 7 | 3 |
| 101 | D. A. Kazhdan | talk | 4 | 3 | 0 | 0 | 0 | 0 | 1 |
| 102 | Lee Lorch | talk | 5 | 0 | 0 | 0 | 0 | 4 | 1 |
| 103 | I. M. Gelfand | talk | 3 | 0 | 1 | 0 | 0 | 2 | 0 |
| 104 | I. N. Bernstein | talk | 4 | 0 | 0 | 0 | 0 | 4 | 0 |
| 105 | Louis Nirenberg | talk | 11 | 0 | 6 | 0 | 0 | 5 | 0 |
| 106 | R. A. Minlos | talk | 7 | 3 | 1 | 0 | 0 | 3 | 0 |
| 107 | R. A. Minlos | talk | 5 | 0 | 0 | 0 | 0 | 4 | 1 |
| 108 | V. I. Arnold | talk | 7 | 4 | 0 | 0 | 0 | 3 | 0 |
| 109 | I. M. Gelfand | talk | 4 | 0 | 0 | 0 | 0 | 3 | 1 |
| 110 | Louis Nirenberg | talk | 3 | 0 | 1 | 0 | 0 | 1 | 1 |
| 111 | M. I. Vishik | heading | 2 | 0 | 0 | 0 | 0 | 0 | 2 |
| 112 | M. I. Vishik | talk | 7 | 0 | 0 | 0 | 0 | 7 | 0 |
| 113 | O. A. Oleinik | talk | 7 | 0 | 0 | 0 | 0 | 6 | 1 |
| 114 | M. S. Agranovich | other | 16 | 0 | 5 | 2 | 0 | 6 | 3 |
| 115 | V. I. Arnold | talk | 21 | 1 | 4 | 0 | 0 | 14 | 2 |
| 116 | V. I. Arnold | talk | 25 | 1 | 13 | 0 | 0 | 11 | 0 |
| 117 | — | heading | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 118 | — | plan | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 119 | A. A. Kirillov | talk | 10 | 0 | 0 | 0 | 0 | 9 | 1 |
| 120 | A. S. Dynin | talk | 3 | 0 | 0 | 0 | 0 | 3 | 0 |
| 121 | A. A. Kirillov | talk | 4 | 0 | 0 | 0 | 0 | 4 | 0 |
| 122 | A. A. Kirillov | talk | 7 | 0 | 0 | 0 | 0 | 7 | 0 |
| 123 | A. A. Kirillov | talk | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| 124 | V. I. Arnold | talk | 8 | 0 | 0 | 0 | 0 | 7 | 1 |
| 125 | A. N. Parshin | talk | 6 | 0 | 0 | 0 | 0 | 5 | 1 |
| 126 | A. S. Dynin | talk | 7 | 0 | 0 | 0 | 0 | 7 | 0 |
| 127 | A. S. Dynin | talk | 7 | 0 | 5 | 0 | 0 | 2 | 0 |
| 128 | A. N. Parshin | heading | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 129 | S. I. Gelfand | talk | 14 | 0 | 0 | 0 | 0 | 14 | 0 |

### Correctness, identification, and verification

| Literal correctness | Items |
|---|---:|
| false as written | 29 |
| correct with missing hypotheses | 160 |
| correct | 64 |
| not determinable | 24 |
| **Total** | **277** |

| Publication match | Items |
|---|---:|
| exact | 157 |
| partial | 98 |
| thematic only | 15 |
| none found | 7 |
| **Total** | **277** |

| Verification | Items |
|---|---:|
| read the result | 212 |
| publisher metadata checked | 45 |
| unresolved lead | 16 |
| indirect | 4 |
| **Total** | **277** |

“Read the result” means that the relevant statement or a sufficiently substantive primary-source abstract was read, with the actual scope recorded in the bibliography annotation. It does not assert that the entire proof or book was read. In particular, a scanned PDF that opened without usable text was not automatically promoted to a full-result verification. “Publisher metadata checked” also covers a curated author bibliography where that is the directly opened bibliographic authority; the corresponding annotation identifies which one was used. Unresolved leads remain visible.

## 3. Which searches located the publications

### Authorial short papers and Soviet announcements

Math-Net was particularly effective for author, subject, and year combinations. Kazhdan's lattice finiteness and isolation argument matches **Theorems 1–3 and 5–6** of [Kazhdan (1967)](https://www.mathnet.ru/eng/faa2807), received 10 October 1966 after the September lecture. The paper's ambient-group hypotheses were retained: containing an arbitrary property-T subgroup is not sufficient in general.

Shilov's Hilbert-space algebra, spherical means, and derivation match [Shilov (1967), Part I](https://www.mathnet.ru/eng/faa2820). The nonlinear continuation appears in [Part III](https://www.mathnet.ru/eng/sm4156). The concrete character-space model in the chapter is explicitly reconstructed. The notebook's weak-closedness wording and the use of an unrestricted norm-continuous algebra require qualification. The broad boundary class could not be replaced by a self-contained general domain theorem from the abbreviated notes; those matches are partial.

The complex-power material was traced to Seeley's preprint as published in Russian, **Matematika 12(1), 96–112 (1968)**. Its first page explicitly identifies a preprint. That item is not silently treated as bibliographically identical to the differently titled 1967 proceedings paper. Arnold's Maslov paper was received in September 1966 and printed in 1967; receipt is reported as receipt, not proof of public circulation.

### Singularity theory: following the survey back to original results

[Arnold (1968)](https://www.mathnet.ru/eng/rm5591) gives an especially close account of the 1966 lectures. The audit nevertheless separates older Morse and Whitney material, Boardman's universal strata, and Mather's later classification. [Boardman (1967), Theorems 6.1–6.3 and Definitions 6.4–6.5](https://www.numdam.org/item/PMIHES_1967__33__21_0.pdf), fixes both the dimension-difference sign and the positive-sequence convention in the codimension count. The length-one rank-stratum test checks those corrections independently.

[Mather's Part IV](https://www.numdam.org/item/PMIHES_1969__37__223_0.pdf) and the real corank-two classification in Part VI supply exact comparison points. The Part IV volume is dated 1969 while its printing colophon says 1970; the chapter retains that distinction. Mather's temporary use of “stable” for “infinitesimally stable” is not mistaken for a proof of their equivalence. In the elliptic local-algebra family, the notebook's mixed monomial is redundant for odd exponents. The corrected monomial changes the first failing example from length six to length five. Independent Groebner-basis and sparse linear-algebra calculations confirm this correction. Separately, 246 exact comparisons of two symbol-counting algorithms check the Boardman combinatorics.

### Boundary problems: an exact match after an initially plausible open-problem reading

The March factorization and completion problem matches Vishik–Eskin's 1967 paper **“Normally solvable problems for elliptic systems of equations in convolutions”**, received 27 April 1967. Section 3, Theorems 1.3 and 2.3, contains the augmented normal family, varying partial indices, and signed trivial-bundle index criterion needed for the source question. Consequently this is B, not C or D. The overwritten connective on P000204 remains a palaeographic uncertainty despite the successful mathematical identification. A strong publication match does not establish what a damaged glyph says.

### Source-specific geometric and dynamical questions

The Anosov question is matched to the **topological conjugacy** formulation in [Spatzier (2016), Conjecture 2.3](https://sites.lsa.umich.edu/spatzier/wp-content/uploads/sites/1081/2023/03/brinprize.pdf). The weaker question about the underlying manifold is distinguished from it. Farrell–Gogolev's exotic smooth examples rule out a naive smooth-category strengthening, not the topological conjecture. Smale's four assertions on P000143 are not all unreported open questions: the manuscript explicitly says that assertions 2–4 were refuted.

For Helgason's problem, the decisive match is [Quinto (2008), Problem 4.1](https://bpb-us-e1.wpmucdn.com/sites.tufts.edu/dist/e/6333/files/2021/01/sphere-helg.pdf). This is a transform over **geodesic spheres**, not a geodesic-ray transform. The smooth remainder is not declared solved by the analytic-metric results in the same paper. The search also distinguished the equal-prime-period topology question from the Blaschke metric-rigidity conjecture. [Li and Song (2026)](https://sites.math.rutgers.edu/~cl1412/papers/Zoll.pdf) impose simple closed prime geodesics and an entire Grauert tube; their theorem is recorded with those additional hypotheses. No general smooth-type classification is inferred.

The ambiguous geodesic item on P000172 does not legibly say “closed”. It was not replaced by the familiar infinitely-many-closed-geodesics conjecture. Conversely, the adjacent problem explicitly says closed, so it receives its own precise treatment. Yau's infinite-volume result, the dimension-dependent Bernstein theorem, and orientability in contact dimension three are separately matched to the exact questions rather than grouped under a generic “geometry solved” label.

### Bibliographic chronology

Author bibliographies and Numdam were valuable for distinguishing lectures, received dates, preprints, and print dates. Atiyah's lacuna exposé is a February 1967 Bourbaki lecture printed in 1968; its June addendum is treated separately. Earle–Eells's February journal communication date does not establish public circulation before the March seminar. Several 1969/1970 dates reflect translation or printing history, not a new mathematical result. Contemporary preprint dates are supplied where the primary source establishes them; otherwise no date is invented.

All bibliography entries have an opened URL or DOI and `note = {verified}`. The new entries have an `annote` field recording the source actually inspected and any access limit. The two reused cumulative entries for Kohn–Nirenberg and Hörmander retain their supplied form; their publisher metadata was opened, and no full-proof reading is claimed. Exact publisher metadata, author-hosted texts, Math-Net translations, and Numdam originals are preferred over secondary summaries. Some unsuccessful or inaccessible leads are described in the allocation findings. Absence of a search hit was never used as sufficient evidence for D.

## 4. The completed probability annotation

For a simple finite point process with factorial densities through order four, a real even pair kernel, and volume-uniform bounds

\[
r_2\le C_2,\quad r_3\le C_3,\quad
|r_4-r_2r_2|\le C_4\sum_{a=1,2;\,b=3,4}g(x_a-x_b)+C_0/V,
\quad g\in L^1,
\]

the chapter proves

\[
\operatorname{Var}F\le V\left[2C_2\|f\|_2^2+
(4C_3+4C_4\|g\|_1+C_0)\|f\|_1^2\right]
\]

for real even \(f\in L^1\cap L^2\). The three collision multiplicities are exactly **2, 4, 1**. Each cross-correlation term is integrated along a three-edge tree, and the canonical correction contributes exactly at volume order. Truncation gives centered convergence in probability and in **L1** for every integrable real even kernel, even when its variance is infinite. A separate averaged-correlation hypothesis identifies the limiting mean. The distinction between concentration about a moving expectation and convergence to a fixed limit is maintained throughout.

Two counterexamples have complete hypothesis checks. An ideal canonical gas with an integrable diagonal singularity has finite first moment and infinite second moment. A two-particle hard-sphere gas has the same failure for a kernel singular on an allowed separation shell, so a positive hard core does not repair arbitrary L1 data. The exact ideal canonical correction is

\[
r_4-r_2^2=-N(N-1)(4N-6)/V^4.
\]

The order-dependent effective specific volume in the notebook passes an independent ideal-gas check. The stronger statement with one common adjustment for every order would fail, but that stronger quantifier is **not** imposed on the notebook.

Historical qualifications matter. [Minlos (1968), p. 164](https://www.mathnet.ru/eng/rm5594), explicitly restores an integrable mixing majorant and the van Hove boundary-strip condition. The remaining L1/L2 problem is separate. **Problem 3** requests precise inequalities for the preceding mean/concentration arguments; the exponential estimate appears in the **following Remark 1**. The manuscript's adjusted wall-error rate is also distinct from spatial covariance decay. The final audit therefore assigns the broader programme and its undeclared rate regime to F rather than manufacturing a precise open C problem.

[Pulvirenti and Tsagkarogiannis (2015), Theorem 2.5 and Corollary 2.6](https://arxiv.org/abs/1409.2718), give a two-point dilute canonical estimate with a finite-size term. [Kuna and Tsagkarogiannis (2018), Theorems 2.1 and 2.7](https://arxiv.org/abs/1611.01716), give convergent density expansions and associated estimates in their small-density domain. Neither result is silently promoted to the needed four-point covariance bound at arbitrary density. A feasible further run would derive that bound for one specified stable finite-range potential in a certified expansion regime, then control its averaged bulk mean. This run proves the conditional implication completely and leaves the interacting-model step explicit.

## 5. Other independent mathematical checks

The finite C6 representation-ring counterexample was checked by exact polynomial arithmetic through 32 augmentation powers, in addition to the general algebraic proof. The nilmanifold reconstruction was checked over the quadratic integer ring with 121 exact group-law tests; the second derivation caught and corrected an initial central-coordinate/weight mismatch before assembly.

The Sturm-converse counterexample was differentiated symbolically and also checked by independent automatic differentiation. The exact residual is zero; the floating residual is reported with precision and is not treated as a proof. The reciprocal-endpoint limit was derived by a squeeze argument and separately checked on a sine integral and an independent cubic example. The Fredholm stabilization proof was reviewed independently, including the common finite-dimensional complement, the kernel bundle, independence of the auxiliary space, and homotopy invariance.

The singularity checks use independent Groebner-basis and sparse linear-algebra methods. Pair-observable checks use standard-library exact fractions, enumerate all 128 configurations of a nonuniform seven-site process, and compare moments computed directly with those computed from factorial marginals. They also test the canonical identity at 205 rational parameter pairs, including small particle numbers. Their complete scripts and outputs are included. No finite experiment is presented as proof of a universal theorem.

The proof reviews and the checks found no remaining discrepancy in the final variance, truncation, canonical, Sturm, endpoint, or stabilization arguments. They did produce concrete corrections: the nilmanifold coordinate convention, the Problem 3/Remark 1 attribution, the distinction between wall and pair-clustering estimates, the need for a positive lower endpoint-slope bound in the squeeze proof, and the complex-Hilbert-space convention for complex K-theory.

## 6. Corrections and source ownership

| Correction type | Items |
|---|---:|
| faithful_error | 56 |
| ambiguity | 37 |
| provenance | 10 |
| transcription | 3 |
| translation | 2 |
| **Total** | **108** |

The CSV has the exact required columns and an explicit type for each row. `faithful_error` means a mathematical defect that the transcription faithfully preserves; it is an annotation or emendation, not a new reading of the handwriting. `ambiguity` does not claim resolution. `provenance` covers attribution, date, or record-boundary problems. Translation corrections are distinguished from both.

Material examples include the Brieskorn exponent; structural stability as topological rather than smooth equivalence; weak versus norm closedness of an infinite-dimensional sphere; entropy sign and temperature factor; the heat-kernel factor four; Boardman codimension conventions; the elliptic local-algebra mixed monomial; and the extra square in the minimal-graph equation. Each CSV row points to the scan and explains the evidence. Item 1966-129.14 separately makes the future-half-space restriction in the Herglotz–Petrovsky formula explicit; this is an item-level domain qualification.

Catalogue ranges overlap heavily. The additional “Minlos, Lecture 5, phase transitions” heading on P000167 and a professor's Sturm–Liouville heading on P000168 contain no recoverable subsequent theorem; the chapter notes them without fabricating new MCCME records. The P000171 geometry problems are not attributed personally to Agranovich. P000199 explicitly names Anosov within record 124. The P000202 Parshin heading is distinct from the later March 27 factorization material. A full heading or plan can legitimately contribute no mathematical occurrence.

## 7. What the classes miss and proposed refinements

1. **Chronology and correctness are orthogonal.** A publication match can preserve an incorrect shorthand or an incomplete proof. Keep literal correctness, match strength, and verification level independent of A–F.
2. **A/B priority is imperfect for third-party reports.** A talk may describe another mathematician's already circulating but unpublished theorem. The fate field must state whose result it is and distinguish circulation from print. A new optional `result_author` field would reduce ambiguity without changing occurrence ownership.
3. **F has two different causes.** Illegible ink differs from a recognizable programme whose quantifiers are incomplete. Add an optional `identification_obstruction` field, with values such as reading, missing conclusion, missing regime, or incompatible formulations. The present prose already makes these distinctions.
4. **Publication verification needs finer granularity.** The required four labels are retained, but substantive-abstract reading, full theorem reading, proof checking, and bare metadata should be distinct optional source-level fields. A binary `verified` bibliography note means an endpoint was opened, not that every cited theorem was independently proved.
5. **Separate the source problem from its repaired version.** A corrected sufficient theorem may be useful without certifying the intended stronger assertion. A `scope_relation` field could distinguish exact, weaker sufficient version, counterexample, and related theorem. This year particularly needs that distinction for wall convergence, tensor reconstruction, boundary domains, and geometry transforms.
6. **Keep source ownership separate from catalogue ownership.** Optional actual-content page ranges and speaker overrides are useful. The present dataset follows the existing format and records the distinctions in summaries and item-level fields.
7. **Do not infer open problems from undefined exceptions.** A partly realized research programme is not automatically a precise C item. The Minlos reclassification is an example of applying the stricter standard. Completed elementary audits belong in the critical companion without creating a novelty quota.

## 8. Reproduction and final validation

The required seven source files are at the archive root, together with the report, generated chapter, test driver, and compiled PDF. The supplied builder and style are included. Reviewed allocation inputs and their generation scripts are preserved in `code/authoring/`; `code/assemble.py` merges them, renumbers only the new problem IDs, verifies occurrence links, and regenerates the count tables. Its deterministic outputs include `code/audit_counts.json`, `code/item_areas.json`, and `code/source_page_coverage.csv`.

The build command is `python build_chapter.py GY1966`, followed by XeLaTeX, BibTeX, XeLaTeX, and XeLaTeX. `code/BUILD.md` records the exact commands, the local TeX-environment repair needed in this session, the font license, and the check dependencies. All source-content build errors were fixed. Final builder output, bibliography output, LaTeX logs, and PDF information are included in `code/build/`; the visual-QA record is `code/visual_qa.md`.

The original transcriptions, catalogue list, previous occurrence/problem index, and cumulative bibliography are included as reproducibility inputs. The scan images and third-party article PDFs are not duplicated in the archive; their original filenames, page references, and bibliography links identify the evidence. The chapter and data contain brief quotations and original critical paraphrases rather than reproductions of those publications.

The final manifest records file paths and SHA-256 hashes. Rebuilding mathematical data and re-running all four mathematical check scripts require only Python's standard library, with no network access. The delivered PDF is the output of the final successful build, after inspection of its rendered pages.
