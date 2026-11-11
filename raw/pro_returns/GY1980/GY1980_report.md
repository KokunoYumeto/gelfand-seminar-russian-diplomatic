# GY1980 critical companion: research and verification report

**Status date: November 2026.** This report documents the research, editorial decisions and verification behind the seven schema files and the generated chapter. The PDF page count below reflects the current compilation state. The apparatus distinguishes evidence from the notebook, the diplomatic Russian transcription, the English translation, published literature and deductions made in this chapter.

## 1. Scope and completed inventory

The supplied manifest contains 36 records. The live MCCME master catalog and the attached P000960 date heading identify three additional records belonging to the same academic year: **510, 511 and 512**, cataloged under the erroneous date **23-Feb-91**. The autograph reads **23/II/81**. These records have been restored with the date **1981-02-23**, retaining their original record numbers. The chapter therefore contains **39 records: 38 mathematical talks or interventions and one nonmathematical catalog year divider**. The data and corrections document the discrepancy. Source: [MCCME seminar catalog](https://old.mccme.ru/gelfand/notes/all-links.html).

The records follow their first appearance in the manuscript. Gelfand's introductions precede Beilinson on 3, 10 and 17 November. On 24 November, the Fuchs and Lomonosov interventions precede the Beilinson continuation. On 23 February, Gelfand precedes Cherednik, reversing their catalog-number order. Interleaved continuations remain grouped with the identified talk and are described in its summary. The page fields specify the portions observed in the manuscript, resolving the manifest's overlapping ranges.

**P000916** is an undated continuation from the previous year, already represented by **1979-488.1–.7** in the supplied earlier index. It is accounted for as boundary material with links across years; it does not create a new September 1980 occurrence. **Record 507** is a catalog divider rather than an independently verified manuscript lecture. Every mathematical source page from P000917 through P000980 is represented in the current year's coverage ledger.

| Deliverable measure | Count |
|---|---:|
| Records | 39 |
| Mathematical occurrences | 246 |
| Problem identities | 16 |
| Bibliography entries | 94 |
| Correction rows | 90 |
| Compiled PDF pages | 139 |

The JSON files are the occurrence and problem indices. `GY1980_chapter.tex` is generated from them, the overview, development and corrections. The PDF includes the full chapter, problem index, correction apparatus and bibliography. The `checks` directory records validation, source-page coverage, mathematical computations and build results. Batch research ledgers in `parts` preserve the source-identification and verification history.

## 2. Counts and their interpretation

### By fate class

| Class | Items |
|---|---:|
| A | 42 |
| B | 13 |
| C | 1 |
| D | 0 |
| E | 165 |
| F | 25 |

A means a relevant result subsequently published by the speaker or Gelfand; B a subsequent development by others; C a precise question partly developed; D a defensibly identified but undeveloped question; E prior knowledge; F content whose intended statement cannot be sufficiently recovered. **No D item is asserted.** Failure to retrieve an exact source is not enough to call mathematics undeveloped. Repeated exposition is counted as repeated occurrence, not as a new theorem. These totals therefore measure the notebook's structure and the editorial decomposition, not research productivity.

The single class-C occurrence is **1980-519.3**, the question of embedding the function field of every complex algebraic curve in the first Weyl division ring. Its status is limited to what the checked literature establishes. The genus-two occurrence **1980-519.2** was changed from a provisional C classification to B after a further primary-source search located Oganesyan's theorem for arbitrary genus-two quintics. The final assessment thus distinguishes a complete genus-two result from earlier generic examples.

### By attributed speaker

An explicit item-level intervention overrides the primary talk speaker. Otherwise the item is counted under its record's primary speaker. A joint attribution retained in one row is counted once, so the table totals the number of occurrences. Attribution is not a claim of authorship of every theorem discussed.

| Attributed speaker | Items |
|---|---:|
| A. A. Beilinson | 47 |
| A. A. Belavin | 4 |
| A. A. Kirillov | 5 |
| A. B. Goncharov | 2 |
| A. G. Khovanskii | 19 |
| A. V. Bobylev | 10 |
| B. V. Lidskii | 4 |
| B. Ya. Kazarnovskii | 5 |
| Bernard Gaveau | 9 |
| C. Kassel | 2 |
| C. Soulé | 1 |
| D. B. Fuchs | 8 |
| D. B. Fuchs and A. A. Beilinson | 1 |
| E. Viehweg | 5 |
| G. I. Olshanskii | 12 |
| I. M. Gelfand | 37 |
| I. V. Cherednik | 14 |
| J.-L. Brylinski | 2 |
| M. I. Graev | 5 |
| P. G. Grinevich | 3 |
| Robert D. MacPherson | 16 |
| S. G. Gindikin | 1 |
| S. G. Krein | 8 |
| S. I. Gelfand | 2 |
| S. P. Novikov | 17 |
| V. E. Zakharov | 1 |
| V. I. Arnold | 5 |
| V. I. Lomonosov | 1 |

### By mathematical area

Each occurrence is assigned one primary area for counting. The more detailed labels are preserved in `checks/item_area_classification.csv`. An occurrence spanning several subjects is counted once.

| Primary mathematical area | Items |
|---|---:|
| Algebraic geometry and K-theory | 13 |
| Analysis, probability and stochastic methods | 10 |
| D-modules, sheaves and homological algebra | 46 |
| Differential, complex, projective and symplectic geometry | 26 |
| Integrable systems, spectral and operator theory | 54 |
| Integral geometry and special functions | 10 |
| Kinetic theory, fluid mechanics and PDE | 23 |
| Lie theory, representation theory and algebra | 32 |
| Newton polyhedra, convex and exponential geometry | 22 |
| Topology and intersection homology | 10 |

### Assessment dimensions

The fate class is independent of literal correctness and strength of verification. A pre-existing theorem can be miscopied or stated without indispensable hypotheses; a perfectly legible notebook sentence can be false.

| Literal correctness | Items |
|---|---:|
| correct | 37 |
| correct with missing hypotheses | 131 |
| false as written | 51 |
| not determinable | 27 |

| Verification level | Items |
|---|---:|
| indirect | 14 |
| publisher metadata checked | 26 |
| read the result | 194 |
| unresolved lead | 12 |

| Publication match | Items |
|---|---:|
| exact | 152 |
| none found | 9 |
| partial | 66 |
| thematic only | 19 |

Correction types are likewise distinct:

| Correction type | Rows |
|---|---:|
| ambiguity | 17 |
| faithful error | 64 |
| provenance | 8 |
| transcription | 1 |

## 3. Main mathematical findings

### D-modules, intersection homology and categorical affinity

The autumn and November talks form a sustained sequence on D-modules and their geometric applications. The apparatus distinguishes ordinary and derived inverse image, left and right modules, transfer bimodules, cohomological shifts and simple regular holonomic objects. A torsion-free D-module is not thereby a connection; reducible support requires qualifications beyond an irreducible minimal-extension theorem; arbitrary coherent D-modules need not have finite length. The notebook's middle-perversity formulas also require corrections. Because the errors are legible in the manuscript, they are classified as faithful notebook errors. The statements and precise source locators accompany occurrences 1980-490.1–.5 and 1980-493.3–.13, and the items in records 496, 498, 500 and 503.

Kashiwara's April 1980 Riemann–Hilbert announcement predates the October discussion; the apparatus separately dates the later full treatments. The categorical converse left uncertain on 3 November is answered in the continuation on 10 November, with the compact projective generator and opposite-ring qualifications made explicit. The two occurrences share one problem identity.

### Magnetic translations and Bloch bundles

Novikov's lecture on 1 December draws on Dubrovin and Novikov's already published 1980 zero-mode results. The paper received **2 December 1980** supplies the closely matching topological continuation. The physical line bundle has degree \(N\), while the reciprocal-torus zero-mode bundle has **rank \(N\) and Chern number of absolute value one**. The conflation of these quantities on P000946 is a substantive faithful notebook error. The genericity argument is formulated in the bundle of Hermitian endomorphisms, so it does not assume an unavailable global trivialization. Landau multiplicity \(N\) refers to one scalar spin sector. The uncancelled one-dimensional aside is retained as a separate F item. See Dubrovin and Novikov (1980, Section III), [full text](https://people.sissa.it/~dubrovin/Papers/1980/dubrovin_novikov_1980_dan.pdf), and Novikov (1981, Section II, Lemma 1; Section III, Lemma 2 and Theorem 2), [full text](https://homepage.mi-ras.ru/~snovikov/71.pdf).

### Grassmannians, Newton polyhedra and exponential sums

MacPherson's constructions require genericity and a distinction among a complex torus orbit, its positive real part and a compact Hamiltonian torus orbit. The last is mapped to a point by its commuting Hamiltonians and therefore cannot itself have the nontrivial polytope image drawn in the notebook. Statements about harmonic forms need degree and parity qualifications. Khovanskii's genus and root-count formulas require the appropriate toric compactification and nondegeneracy conditions. Kazarnovskii's zero asymptotic for a fixed system is checked against the regularity definition in the 1981 paper; a later result about averaged currents addresses a different statement. Precise theorem locators appear in records 508, 509, 512 and 513.

### Commuting operators: a resolved genus-two problem and a wider conjecture

A decisive source identification was Oganesyan's theorem: **every monic genus-two quintic** occurs as the spectral curve of rational-coefficient commuting operators of orders 4 and 10, using the union of two families. The result first circulated on **18 August 2016** and was published in **2018**. It resolves the genus-two question when interpreted as realization of an abstract curve or its standard quintic model. The stronger assertion about every affine coordinate ring is treated separately. See Oganesyan (2018), [published article](https://doi.org/10.1007/s10688-018-0229-0), and Theorem 3(2) of the [2016 author preprint](https://arxiv.org/abs/1608.05146).

Gelfand's separately recorded assertion asks whether the function field of **every complex algebraic curve** embeds in the **first Weyl division ring**. This is distinct from the Dixmier endomorphism conjecture, isomorphism questions for Weyl fields of unequal ranks and the Gelfand–Kirillov conjecture. All cases of genus at most two are positive. The checked constructions in higher genus establish selected families. The C classification records this limit of the evidence; it does not claim that the search exhausts the literature on the universal assertion.

### Kinetic and spectral problems

The pure Vlasov functional bracket already appears in Morrison's 1980 paper, equation (12), before Arnold's March 1981 talk. The later coadjoint-orbit and gauge formulations have their own chronology. The original Maxwell coupling and its subsequent correction for the Jacobi identity are distinguished from the correct pure Vlasov bracket, with mass normalization stated explicitly. Bobylev's Fourier and isotropic hierarchy results are qualified by the collision model and analytic class. The broad hydrodynamic-limit program remains F because the notes do not specify a theorem-level target.

Lidskii's recursive inequalities match a 1982 announcement. The apparatus distinguishes that announcement, the absence of a supporting published proof reported in the checked historical account, and the later resolution of the Horn problem. The trace equality, recursive index conditions and tensor-product saturation statement appear in 1980-526.1–.3. Record 528 separately treats Olshanskii's global and local semigroups, proper cones, orientation choices and factorization for the **minimal cone**. Each qualification affects the scope of the corresponding assertion.

## 4. Bounded development and verification

The development addresses the remaining universal question about function-field embeddings. Its genus-two subsection verifies a known positive case and clarifies the difference between realizing a function field and realizing a prescribed affine coordinate ring.

1. **Affine-unit obstruction.** For a smooth irreducible affine complex curve of positive genus with a nonconstant unit, there is no injective unital complex-algebra map from its coordinate ring into \(\mathbb C(x)[D]\). Units of this operator ring have order zero. Injectivity would force the image of the nonconstant unit to be a nonconstant rational multiplication operator, whose centralizer is \(\mathbb C(x)\). The resulting curve-field embedding into \(\mathbb C(x)\) would induce a finite nonconstant map from \(\mathbb P^1\) to a compact curve of positive genus, contradicting Riemann–Hurwitz. The proof states all hypotheses explicitly.
2. **A concrete genus-two example.** The smooth affine curve \(zw^2-z^4-1=0\) has invertible coordinate \(z\). Its function field is that of \(Y^2=z^5+z\), a squarefree genus-two quintic. The obstruction applies to its affine coordinate ring, while Oganesyan's theorem provides an embedding of its function field. The proof explains why realizing the original coordinate \(w\) requires passage to a quotient operator.
3. **The notebook's false operator formulas.** The literal sixth-order expression has a nonzero commutator with \(D^5\) coefficient \(48x-12\). The corrected Dixmier pair passes the exact check. For the notebook's two-term formal expression \(A\), the differential part of \(A^3\) is \(L^3+3xL+6D\); the corrected commuting pair instead has the term \(3D\). The next term in the formal square root supplies the correction.
4. **A known genus-two certificate.** With \(L=D^2+x^3+a\), the included operators \(P=L^2+6x\) and \(M\) satisfy \([P,M]=0\) and \(M^2=P^5+27aP^2+81\). Both the symbolic discriminant and direct elimination of common roots give the smoothness condition \(2916a^5+3125\ne0\). The construction is an existing Mironov family; the chapter supplies a reproducible certificate for it.
5. **The injectivity step.** Since \(P\) and \(M\) have differential orders 4 and 10, nonzero terms \(f(P)\) and \(g(P)M\) have orders congruent to 0 and 2 modulo 4, respectively. They cannot cancel, proving that the spectral coordinate-ring map is injective. The proof then extends the map to the curve's function field, with values in the Ore division ring.

Results proved or computed in the chapter are marked `\ours` or `\oursComputed`. The operator computation uses exact polynomial arithmetic over \(\mathbb Q[a,x]\). A second implementation checks direct action on every monomial through degree 20 at four parameter values. A triangular coefficient argument makes each finite check complete at its parameter value; the theorem for all parameters rests on the symbolic coefficient identities. A separate proof audit checked the unit obstruction and the hypotheses concerning algebraic curves. The formal pseudodifferential computation uses a justified cutoff. The code and its actual outputs are included.

Comparison with the 2012 version of Mironov's preprint identified a scalar normalization: the displayed tenth-order operator equals the centered operator plus \(9I\), while the displayed hyperelliptic equation uses the centered operator. Both operators commute with \(P\), and shifting the spectral coordinate reconciles the formulas. The chapter identifies the preprint version checked; the final journal typesetting was not checked for this issue. The initial assertion of literal equality failed the computation, and the corrected normalization passed the final run.

## 5. What was difficult and which searches worked

**Provenance before bibliography.** Broad catalog page ranges overlap several speakers. Explicit manuscript dates and speaker headings, together with the live catalog, determine attribution. Recovering records 510–512 established the February setting of material that might otherwise have been assigned to the March talks. P000916 required a decision about the boundary between academic years before its mathematical content could be classified.

**Exact-title searches and authors' bibliographies.** Submission dates on Math-Net and translations of Soviet papers hosted by their authors were especially useful for Novikov, Khovanskii, Grinevich, Kazarnovskii and Olshanskii. Contemporary seminar expositions and publisher metadata distinguished first announcements from final articles. Following references in primary sources identified the regularized diffusion setting of Gaveau's work. A targeted search for rational-coefficient commuting operators found Oganesyan's theorem and changed a provisional classification. The batch research ledgers preserve URLs, precise result locators, unsuccessful leads and access limitations.

**False statements and incomplete statements.** The correction apparatus distinguishes errors faithfully transcribed from the notebook from missing hypotheses. It also distinguishes mathematical emendations from the manuscript's actual wording. Some insufficiently specified programs remain in class F: an unspecified regularization, a comparison of operator restrictions with unclear spectral subspaces, a regularized Burgers step for an arbitrary polynomial without a stated solution class, and a request to extend semigroup ideas beyond the stated Lie-group setting.

**Verification limits.** `note={verified}` means that a bibliography link or DOI was opened; it does not mean that every original proof was read. Item-level verification and the research ledgers state the evidence actually checked. Some exact matches rest on publisher metadata together with a separate primary exposition. **Hilbert's 1901 article is the sole unverified entry among the 94 references**: the direct source remained inaccessible, and the associated item is classified as indirectly verified. Ivlev's 2026 paper was checked only through its metadata and abstract because the full text was embargoed. The search was broad and targeted, but it was not a systematic review of every publication through November 2026.

## 6. What the A–F scheme misses and proposed method changes

The single fate letter compresses several independent questions. An old formula can receive a new proof or geometric realization; an announcement can precede a complete proof by years; a refuted broad conjecture can retain open subcases; a precise theorem can coexist with a false handwritten formula in the same occurrence. This year therefore relies heavily on the separate literal-correctness, publication-match, verification and development fields. No extra state was silently introduced into the required schema.

For future chapters, useful optional additions would include separate catalog and manuscript dates; an anchor identifying the relevant region of a source page; a chronology distinguishing submission, circulation, online publication and journal issue dates; precise source locators and verification scopes for each reference; and typed links distinguishing recurrence, proof, special case, correction and thematic connection. Explicit `abstract_curve`, `affine_model` and `coefficient_ring` scope fields would prevent the genus-two ambiguity encountered here. A `primary_area` field would make area totals reproducible across chapters. These are proposals for future revisions; the delivered chapter uses the required schema.

Problem identities should follow exact statements. The existing identity GP-1967-21 is reused. Resolved exercises can have problem entries when the notes pose a definite question, with their resolved status stated explicitly. The field-embedding conjecture retains its own identity, separate from earlier questions about Weyl algebras. A search that finds no exact match does not by itself establish an undeveloped idea.

## 7. Presentation on the companion website

A reader arriving at a talk should first see its actual date, source-page footprint and provenance warning when those differ from the catalog. The next step should be the short summary and item list, with each item opening four clearly labeled panes: notebook wording, precise statement/reconstruction, fate and present status. A correction should be reachable directly from the sentence or formula it qualifies. The original scan and both transcriptions should be one click away where their hosting permits it.

Priority links should connect the November D-affinity question to its continuation; the repeated Cherednik talks to one another; records 511 and 518 to the corrected operator formulas and record 519; and the distinct genus-two and all-curves problem identities. The MacPherson, Khovanskii and Kazarnovskii talks merit links between their related polytope constructions. The collective-field material on P000916 should link to 1980-523.1 and 1980-524.2–.4. The recurrence of GP-1967-21 must resolve across years. Earlier questions about automorphisms or Weyl fields of different ranks should carry explicit thematic links while retaining their own identities.

Search should support mathematical expressions as well as titles and names. Filters should expose fate, literal correctness and verification separately; a green “verified” badge based only on an opened DOI would mislead. Useful navigational metadata include source anchors, primary areas, typed links and publication chronology. A stable item URL should retain the academic-year/record/item identifier even when a catalog date is corrected. Readers of the development should be able to inspect its proof, code and actual check output together.

## 8. Build, reproducibility and acceptance checks

The required builder is included and has been run on the seven integrated schema files. A supplementary validator checks all required enumerated values and fields, consecutive occurrence numbers, all 39 record identities, reciprocal problem links, earlier occurrence identifiers against the supplied index, citation-key inclusion and bibliography verification tags. The supplied cumulative bibliography contains repeated keys; integration selects one entry per used key and reuses existing identities. Key-reuse decisions and source coverage are recorded in `checks`.

The reproducible build uses XeLaTeX and BibTeX through the included build script, which records each pass and can generate missing TeX formats locally. **Final acceptance passed on 11 November 2026.** The 139-page PDF contains all 39 record labels and all 246 occurrence identifiers. Cross-references are stable, and the final logs contain no LaTeX errors, unresolved citations or references, missing glyphs, overfull boxes, duplicate labels or BibTeX warnings. The overview occupies parts of pages 1–2. The combined visual inspection covers every page on contact sheets and selected enlarged pages, including all development pages and the final corrected passages. No clipping, overlap or missing-glyph boxes were observed. Eleven underfull-line diagnostics remain; the inspected spacing is readable. `checks/pdf_audit.json` and `checks/visual_review.md` record the scope and final PDF checksum. The mathematical scripts and their outputs are included separately from the scholarly prose. See `README.md` for the exact build and computation commands. The seven schema files are the authoritative chapter inputs, and the generated chapter and PDF present their integrated contents.
