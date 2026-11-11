# Records 649–657: research and integration notes

Checked against the Russian transcription, English transcription, and original page images; literature status dated November 2026. The complete prompt and `CHAPTER_FORMAT.md` were read before authorship. All fragment output is confined to `work/strings`.

## Core inventory

The nine talks contain **76 distinct items**: A 2, B 1, C 0, D 0, E 65, F 8. Their source order is **649, 650, 651, 653, 652, 654, 655, 656, 657**. Both talks on P001217 are dated **21 October 1985** from the manuscript `21/X/85`, while the catalogue's 21 September is retained as a provenance conflict. Record653 is physically above record652. The supplement at P001258–P001259 is separate and does not enter these counts.

| Record | True surviving pages | Items |
|---|---|---:|
|649|P001207 lower–P001209|9|
|650|P001210–P001212|11|
|651|P001213–P001216|11|
|653|P001217 upper|3|
|652|P001217 lower–P001218|7|
|654|P001219–P001221 upper|10|
|655|P001221 lower–P001222|6|
|656|P001223–P001224|6|
|657|P001225–P001228|13|

All pages P001207–P001228 were inspected visually. Reduced review copies are in `scan_review`; the original files remain under `work/scans`. The important formula decisions were also checked against original-resolution pages when necessary. The boundaries follow handwritten speaker/topic/date changes, not the overlapping catalogue ranges.

## Primary identifications

* **Ryzhikova's decidability announcement (653)** is exactly identifiable with *Decidability of the identity recognition problem in lattices of linear subspaces*, Doklady297(5) (1987),1058–1061. The full four-page Russian paper was read. Lemma1 supplies a dimension bound; duality supplies the other half of the manuscript's symmetric bound. Lemmas2–3 and the main theorem give fixed-characteristic reduction and decidability. Received16May1986; English translation1988. No earlier public preprint was verified. New problem **GP-1985-20** is solved, not open.
* **Ryzhikova's later lattice talk (656)** explicitly presents Gelfand–Ponomarev1974. It is exposition, classE. The source's sections1.1–1.4 recover the recursive cubicle indices. The distinction between equality in the free modular lattice and equality in all linear representations is retained. The paper's separate completeness conjecture is absent from the notes and is not imported. Earlier occurrence links:1973-319.1–4 and1973-319.7–9. The separate representability problem GP-1973-30 is not re-posed.
* **Müller (654)** reports Cheeger–Gromov's characteristic numbers and Cheeger's conic spectral geometry, then asks a general Fuchs-operator index question. Cheeger–Gromov's Theorem0.6, Cheeger's Theorems4.1/4.4 and section6, and Lesch's Proposition1.3.16, Corollary2.4.7, Theorem2.4.8 were actually read. The question is reconstructed with cone ellipticity and a specified domain; it is **B**, new problem **GP-1985-21**. Lesch's habilitation was submitted1993, preprint1996, book1997. This does not assign a canonical index to every expression resembling the notebook's formula.
* The final Hilbert modular example strongly matches **Müller1984**. The author's publication list was opened, but the full paper was blocked. The exact factor `1/(2π)` multiplying the L-value/covolume is therefore **not verified**. Müller's1987 book was checked only in its publisher metadata and chapter list. These items explicitly state metadata-only verification.
* **Feigin's determinant-line definition (655)** uses the dual of Quillen's own operator determinant line. Quillen's original Russian paper was read. Consequently **dividing the squared Hodge norm by the zeta determinant is correct in the notebook's convention**. Do not turn this division into a multiplication during integration.
* **Virasoro reducibility (657)** repeats **GP-1982-03**, prior occurrence1982-566.7. Feigin–Fuchs1982 was read in Russian, including printedp.58. The notebook's final polynomial coefficient is visibly `1/2`; the correct coefficient is `1/16`. The bracket with positive creators needs a central-generator sign conversion before the later standard central charge formulas can be used. The first singular grade is the minimum of all products `rs` whose factor vanishes.
* **Sugawara and coset constructions** were checked in AdrianKent's1985 primary author report, pp.132–134, equations(10),(15)–(20). The reconstruction includes normalized invariant forms, embedding index, restricted modules, completion, and both noncritical levels. Kac–Peterson1981 metadata was checked on Kac's own publication list; its full paper was not read, and the text says so.
* **Selberg and Dotsenko–Fateev integrals**: the displayed Gamma product is the ordered-chamber Selberg value with Vandermonde exponent `2ρ`; the ordinary symmetric cube has an additional `m!`. Dotsenko–Fateev1984 was read at the screening contours and four-point constructions. The real-cube reading of mixed exponent `−2` fails at collisions. Analytic continuation from discrete screening counts is not unique without extra conditions. That last claim is F, not a manufactured open problem.

## Main mathematical corrections

The CSV separates faithful notebook errors, ambiguities, and provenance. It does not label them OCR errors. Its 57 core rows include several clarifying rows that prevent an incorrect editorial repair.

1. Harmonicity for a fixed metric does not imply conformality. The metric Euler–Lagrange equation is required. The affine map `(u,v)↦(2u,v)` is a checked counterexample.
2. The area Hessian is not the fixed-metric Dirichlet Hessian. A compactly supported tangential reparametrization of a planar disk preserves area while the displayed Dirichlet quadratic form is positive. The correct normal Jacobi form is stated.
3. The conformal change of the Dolbeault adjoint on `T^j` has factors `exp(−(j+1)φ)` and `exp(jφ)`. The notebook writes the formula for the Serre-dual bundle `T^(−j−1)`. Symmetry of the determinant anomaly does not identify the operators.
4. Dimension26 and exponent13 are secure; the exact real/complex determinant powers in several manuscript formulas are not mutually consistent. Critical dimension cancels the Weyl anomaly, not all moduli dependence or boundary divergences.
5. The scalar heat coefficient uses `R/6=K_G/3`. The manuscript initially calls the latter curvature scalar, later changes terminology, and drops an overall factor. The source's finite coefficient discussion was read but imperfect OCR makes the item-level verification conservative.
6. The fixed hyperbolic conformal slice misses Teichmüller directions. The full Lie derivative must be projected to its trace-free part before its Dolbeault interpretation. Its squared adjoint is not the ordinary Hodge Laplacian.
7. The exact cone metric is `du²+u²g_Y`, while the manuscript visibly has `u^(−2)`. The boundary condition in the notes cannot be uniquely repaired without its angular mode and chosen closed extension.
8. Invariant operators need ellipticity and cusp hypotheses before finiteness of their kernels; the invariant zero operator disproves the unrestricted sentence. A Hilbert modular quotient has one cusp only with the relevant class-number/subgroup qualification.
9. The first cubicle is a relative Boolean lattice; its bottom need not be ambient zero. Its size is `2^r`, not the unexplained `2^n`.
10. The screening formula has literal endpoint/differential errors, and the same page changes “two-point” to “four-point.” The latter agrees with its cross-ratio.

## No deep-development candidate

No core item has a supported C or D classification. The recoverable questions are already solved; the F items omit essential mathematical data or are vague historical pointers. The elementary checks above are labelled **annotated**, not “developed in this chapter.” No substantive development quota should be met by inventing an unresolved Liouville, modular-lattice, or determinant problem.

In particular, a rigorous subcritical sphere Liouville construction is mentioned only with `0<γ<2`, positive cosmological constant, and the precise Seiberg bounds. It does not settle the unspecified all-genus string path integral. Dotsenko–Fateev continuation and a “surface Wiener measure” are not promoted to precise universal open questions.

## Verification and integration

`sources.json` records opened URLs, browser references, result locators, and the exact scope of verification, including failed full-text attempts. A bibliography `note={verified}` means its linked source was actually opened; each `annote` distinguishes full-result reading from metadata. The source ledger has separate failed entries where opening led to a challenge or error. The cumulative BibTeX keys are reused.

The authorship scripts are reproducible checkpoints, not part of the required final chapter bundle. Running `author_data.py` writes only core talks/items. Running `author_support.py` writes core bibliography, problems, sources and corrections, and should precede any later supplement-merging script. Parent integration should preserve the source order and exclude ADJ-prefixed items from core indexes/counts.

## Completed adjacent-page supplement

`adjacent_items.json` contains 12 separate occurrences: ADJ-667.1–6 (Kontsevich) and ADJ-668.1–6 (Morozov). `adjacent.tex` renders them with the unresolved manuscript/catalogue dates stated first. `adjacent_corrections.csv` contains 9 separate rows; root retains its fuller date provenance when merging. The supplement adds one new bibliography key, `kontsevich1987virasoro`, so the complete shard bibliography contains 19 keys and the source ledger contains 33 entries.

Kontsevich's exact two-page 1987 paper was read in Russian. Section1 supplies the formal-parameter moduli, infinitesimal Laurent-vector-field action, and the quotient by global meromorphic vector fields. The further quotients for unpointed and pointed moduli are explicitly reconstructed by formal gluing. Sections2–3 supply the determinant extension and the coefficient `6k²−6k+1`; no absolute central charge is assigned without fixing the central-generator convention. These two theorem items are A; the other supplementary items are E. The paper's final open-ended remark about representations in spaces of sections is **not present on the notebook page and is not imported**.

Morozov's Gaussian material was additionally checked in Belavin–Knizhnik1986section6, equations(6.21)–(6.26). The reconstruction distinguishes the determinant of 26 nonzero scalar modes from the constant-mode momentum delta; fixes one action/covariance convention for the sign and factor1/2; states an explicit finite-cutoff Wick subtraction; and separates a target delta derivative from a world-sheet derivative vertex. No full integrated-amplitude convergence theorem is inferred.

Explicit `\ours` or `\oursComputed` markers identify 19 core editorial checks and 7 supplementary checks in reconstruction fields. The source-based theorems remain separately attributed. These are annotations, not C/D deep developments. The format builder passes the core fragment. Parent reports that the integrated XeLaTeX build passed the full core section through page94; the local default-format failure was environmental, and no further duplicate compile was necessary.
