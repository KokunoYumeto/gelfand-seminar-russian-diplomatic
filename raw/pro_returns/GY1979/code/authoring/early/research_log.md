# GY1979 records 462–470: research and evidence log

Research date and status cutoff: **2026-11-10**. This ledger records the early-batch research, its source access limits, manuscript decisions, and saved computations. It accompanies the structured item records; it does not claim an exhaustive survey of every subsequent publication.

## Scope and manuscript protocol

The assigned catalogue contains nine records, 462–470. Both English and Russian source transcriptions were read for P000840–P000865; P000866 was inspected for the boundary with the following contribution. Mathematical assertions were separated from notebook shorthand in the `notes`, `statement`, and `reconstruction` fields. No new 1979 item was created for a passage already indexed in the preceding year. Routine expository facts are classified E, and incomplete physical programmes or underdetermined questions F; missing search results are not treated as evidence of openness.

The source page boundaries differ substantially from the catalogue envelopes. The actual spans are:

| Record | Critical source span | Boundary evidence |
|---|---|---|
| 462 | P000841–P000842 | New dated Kallosh heading on P000841; Zakharov starts P000843. |
| 463 | P000843–P000847 | Zakharov heading, with Arnold and Gelfand interventions. |
| 464 | Upper P000848 | Gelfand's spinor/Dirac introduction. |
| 465 | Lower P000848–P000853 | Kallosh's eight-part programme begins at the foot of P000848. |
| 466 | Opening P000854 | Dated 8 October programme and three lines of exercises. |
| 467 | Remaining P000854–P000858 | Gindikin's twistor lecture, ending before the 15 October heading. |
| 468 | P000859–upper P000862 | Berezin, then Gelfand/Gindikin interventions on graph algebras and BGG. |
| 469 | Lower P000862–middle P000863 | Shabat-labelled contribution, before Høegh-Krohn. |
| 470 | Lower P000863–P000865 | Energy representation and Brownian path realization. |

P000840 is prior-talk carry-in. Its vertex-model, Yang–Baxter and Ising material is already represented by **1978-460.12–20** in the earlier index; it is not a new Kallosh occurrence and does not require a twenty-eighth catalogue record. This was initially considered against record 461, but the actual prior item crosswalk identifies record 460. The root integration retains the exact supplied catalogue in its crosswalk and normalizes `talks.pages` to the critical spans, preserving the discrepancy as provenance. The early authoring file itself still retains the supplied catalogue envelopes pending that reproducible root transformation.

### Scan review

The original PNG was consulted for every mathematically decisive ambiguity. Full images or reduced views were inspected for P000841–P000858 and P000860–P000865; P000840 and P000859 were checked for boundaries and context. Reduced review images are in `scanchecks/`; the P000861 formula-(8) crop is especially useful. Image reduction was solely for inspection, not a replacement for the supplied originals.

Decisive observations:

- P000841 formula (2) has a coefficient involving `s−1/3`, whereas P000853 formula (39) has `s−2/3`. Operator conventions and normalization were not recovered from the inaccessible original index article, so neither is silently corrected to the other.
- P000842 retains an overwritten sign in the boson–fermion relation. Self-duality is explicitly present. An unclear abbreviation by the exceptional group cannot justify using the compact real form in place of the maximal-supergravity split form.
- P000843's reading list is a transcribed figure, not a missing textual paragraph. The mathematical passage first asks for a single extra collision invariant, then explicitly proposes obtaining equations with infinitely many first integrals, and only then asks whether the difference construction is general. That quantifier change is preserved.
- P000844's evolution-variable assignments disagree with its exponential formula. There is no uniquely supported sign/variable correction. The first-order statement `K=−F` must be separated from the nonlinear GLM equation.
- P000845 confirms the second denominator's plus signs in the displayed four-wave coefficient; the claimed on-resonance vanishing is false. P000846 confirms that the Poincaré obstruction omits the factor involving the candidate integral.
- P000848's three anticommuting square roots of −1 give the universal Clifford algebra, not the quaternion algebra without a further quotient relation.
- P000849's Pauli multiplication lacks the factor `i`; P000850 uses a further matrix scaling. A single silent correction cannot cover both conventions.
- P000850 acts with Hodge star on full Riemann curvature. The Ricci-flat consequence does not follow from Weyl self-duality alone.
- P000851 omits `1/2` from the chiral projections. Its spin-5/2 no-interaction sentence cannot be promoted to a universal no-go theorem.
- P000852 explicitly marks the common-eigenvalue-multiplicity conjecture incorrect. P000853 calls the remaining quantity a regularized sum; it is not generally integral. P000853's same-star curvature contraction is not the general Euler density.
- P000855–P000856 confirm the Witt-basis matrix with mixed blocks `iI` and `−iI`, the graph chart, and the positive/negative tube inequalities. The reverse mixed products are not zero. Graph coordinates require transversality.
- P000857's arbitrary `GL(2,C)` affine stabilizer includes dilations. P000858's final metric exponent is visibly `3`, a faithfully transcribed mathematical error; the determinant requires a square. Its point/ray sentence interchanges the two sides of twistor incidence.
- P000861 formula (8) has **sdet in both factors**, confirmed in the crop. No correction to `det` was made.
- P000862's heading initial resembles Russian Yu (`Ю.`), whereas the catalogue identifies G. B. Shabat. Both are retained; no silent author substitution was made. The two Berezin matrix questions occur above that heading.
- P000864's printed `Ad(phi)` and `phi^{-1}dphi` mixture is not a consistent left affine action. P000865 labels the stochastic-development input with the group instead of its Lie algebra, omits finite-energy restrictions on the infinite interval, and makes a false type-III claim for the stated multiplication-plus-unitary algebra.

## Problem decisions and revisions

**GP-1979-01 / 1979-468.11.** The normal-form request is classified B, not open. Root verified Sergeichuk's canonical algorithm and its faithful regular-representation application to the finite-dimensional even supermatrix algebra. Wildness of embedded pair similarity does not prevent an algorithmic canonical form. First verified circulation is the **1999 Bielefeld preprint 99-070**; journal publication is 2000; the 2007 repository deposit is not first circulation. Root supplies the explicit reduction and bounded illustrative normal forms.

**GP-1979-02 / 1979-468.12.** The literal question asks for even matrices commuting with a given all-odd-entry matrix. It is a finite linear-kernel problem after expansion in Grassmann monomials, hence E. A stronger uniform structural normal form was not demanded explicitly and is not manufactured into an open problem. Root's complete `2×2, Λ4` parametrization includes cubic entries and is labelled a bounded explanatory development with no priority claim.

**GP-1977-11 / 1979-468.13.** The BGG bundle correspondence reuses the prior problem ID and definite earlier occurrences 1977-437.2, 437.11, 437.12 and 438.2–5. It concerns proper exterior modules modulo the specified stable equivalence. Instantons require additional twistor-line and reality conditions; the bundle theorem is not an unrestricted instanton classification.

**GP-1979-03 / 1979-468.14.** The demand for actual maps is matched to Eisenbud–Fløystad–Schreyer's explicit BGG/Tate/Beilinson constructions, particularly Theorems 4.1 and 6.1 and Section 5. Joint preprint first circulated in April 2001; journal publication followed in 2003.

**GP-1979-04 / 1979-468.15.** The Grassmannian counterpart is matched to Kapranov's characteristic-zero derived-category construction, with 1984 Russian/1985 English publication and the detailed 1988 account. This is not a finite enumeration of all vector bundles, and the differential itself is not claimed canonical merely because its homotopy class is canonical.

**GP-1979-05 / 1979-463.3.** A provisional C classification was revised after a final primary-source search. The original 1988 discussion alone does not establish present openness. Balk–Ferapontov's 1994 abstract expressly announces a classification of three-wave interactions with infinitely many invariants. P000843 supplies that infinitely-many framing. The record is now **B, partial publication match, indirect verification**: the exact 1994 hypotheses were not retrieved. The broader single-extra-invariant reading is different. Balk–Nazarenko–Zakharov (1991), Sections 4–6, exhibit additional invariants and announce finite-dimensionality, explicitly deferring the uniqueness proof. Balk (2014), Section 2.1, confirms Rossby uniqueness and cites the 1998 web-geometry chapter. Therefore neither the none-or-infinitely-many dichotomy nor a claim of current openness is retained. Local-component and global-all-resonance statements remain distinct; no unverified equivalence is asserted.

**GP-1979-06 / 1979-470.7.** The ordinary energy representation in base dimension two remains the only C item in this batch. Wallach (1987), Theorem 6.2, gives a precise root/covariance sufficient inequality; it does not cover every positive invariant covariance. Shimada's claimed general proof is not accepted: Hasebe and Ando explicitly identify its defective step. The verified 2010/2011 sources document the residual issue, and targeted current searches did not locate an unrestricted repair. This is a bounded literature-status statement as of the research date, not a claim that all 2026 literature was exhausted. Recent projective positive-energy representations of semidirect gauge/diffeomorphism groups are different objects. Root's `dev:energy-diagnostic` is an explicit failure of the differential identity used in the claimed proof; it is not a counterexample to irreducibility.

## Saved computations and independent scope checks

`verify_annotations.py` is executable source; `annotation_checks.json` is its saved output. The program uses `mpmath` and exact `Fraction` arithmetic.

1. For the highly oscillatory quartic integral, the two runs use 70 and 105 decimal digits and different horizontal contours, heights `0.5 r` and `0.49 r`, where `r=(1000/4)^(1/3)`. The common exponential factor is removed **before** quadrature. The rescaled answers agree to roughly 62 displayed digits; the output reports the rescaled difference. The integral is approximately `1.702010938384324421422141438650730536e−1027`. Numerical agreement is not an interval certificate or a rigorous absolute/relative error bound. The leading steepest-descent expression is separately reported and differs at its expected asymptotic order.
2. The narrow quartic exercise is checked by direct quadrature and the convergent gamma-function Taylor series, giving approximately `0.3206479707071545821`.
3. The Davey–Stewartson quartet uses `(1,0),(0,1),(0,0),(1,1)`. Momentum and energy residuals vanish exactly, while the printed interaction coefficient is `6/5`. Changing only the second denominator's plus signs produces `2`, so that simple repair does not restore the claimed identity.
4. The scalar unit-four-sphere heat coefficient is `29/90`, and subtraction of the constant zero mode gives zeta at zero `−61/90`, exactly. This disproves integrality of an individual regularized nonzero-mode count; it does not contradict integrality of an index combination.

Other independent algebraic checks are written in the item reconstructions: Clifford dimension, Pauli factors, graph-chart transversality, determinant scaling, Maurer–Cartan cocycle order, and the factor-type obstruction. None is assigned a historical novelty claim.

## Evidence ledger

All access dates below are **2026-11-10**. `verified` in the bibliography means the stated URL or a primary metadata page was opened, not that every proof was read. The annotations distinguish full-text reading from metadata, abstract-only and indirect support. Root separately checks DOI-registration metadata for initially inaccessible publisher pages and logs those upgrades; those checks do not upgrade the mathematical proof-reading level.

### albeverioetal1983factorial

- URL opened or attempted: https://www.sciencedirect.com/science/article/pii/0022123683900307
- DOI: 10.1016/0022-1236(83)90030-7
- Bibliographic verification label: unverified.
- Result, locators, support and limitations: Original URL attempted on2026-11-10, returned403. Authors and metadata verified indirectly in opened Albeverioetal2015 references1--2; a separate Note appears in JFA52(1)(1983),148. Full paper and correction not read. TypeIII path-group result is only thematic for the notebook's different algebra (L-infinity union W) double commutant.
- Item occurrences supported: 1979-470.11.

### albeverioetal2015brownian

- URL opened or attempted: https://arxiv.org/pdf/1511.07378
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full primary preprint v1 dated23November2015 opened on2026-11-10. Sections2 and5, Theorems4.6 and5.8 inspected for finite-energy path hypotheses, stochastic logarithms, commuting left/right actions and explicit unitary equivalence. References1--2 distinguish1983factorial paper and its separate correction.
- Item occurrences supported: 1979-470.2, 1979-470.4, 1979-470.6, 1979-470.8, 1979-470.9, 1979-470.10.

### albeveriohoeghkrohn1978energy

- URL opened or attempted: https://www.numdam.org/article/CM_1978__36_1_37_0.pdf
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full original opened on 2026-11-10. Sections2--4 inspected for Sobolev/path-group construction, Gaussian realization and Brownian relationship. The qualified preexisting construction is kept distinct from the later irreducibility theorem.
- Item occurrences supported: 1979-470.1, 1979-470.4, 1979-470.8, 1979-470.9, 1979-470.10.

### albeveriohoeghkrohntestard1981irreducibility

- URL opened or attempted: https://www.sciencedirect.com/science/article/pii/0022123681900823
- DOI: 10.1016/0022-1236(81)90082-3
- Bibliographic verification label: unverified.
- Result, locators, support and limitations: Publisher endpoint attempted on 2026-11-10, inaccessible; primary search abstract read. Full result and restrictions independently corroborated in opened Wallach1987 Introduction and Theorem6.2. Conference footnote points to November1979 and September1980; the October1979 notebook precedes those. Original full proof not read.
- Item occurrences supported: 1979-470.5, 1979-470.6.

### ando2010local

- URL opened or attempted: https://arxiv.org/pdf/0904.2222
- DOI: 10.1142/S0219025710004036
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full primary preprint opened on2026-11-10; submitted14April2009. Introduction and type-S commutant result inspected. Does not promote scalar intersection with the type-S operators to a scalar full commutant. Publisher URL was blocked; journal metadata is corroborative, theorem reading is from the author preprint.
- Item occurrences supported: 1979-470.7.

### aragonedeser1979hypergravity

- URL opened or attempted: https://www.sciencedirect.com/science/article/pii/0370269379908086
- DOI: 10.1016/0370-2693(79)90808-6
- Bibliographic verification label: unverified.
- Result, locators, support and limitations: Original publisher URL attempted on 2026-11-10, returned 403. Primary search abstract and metadata read: published 24 September 1979, with an identified May 1979 Brandeis preprint lead. Abstract states the Weyl-curvature obstruction and self-dual exception. Full proof not read; no universal no-interaction theorem asserted.
- Item occurrences supported: 1979-465.17.

### arnold1989mechanics

- URL opened or attempted: https://link.springer.com/book/10.1007/978-1-4757-2063-1
- DOI: 10.1007/978-1-4757-2063-1
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Publisher metadata and contents opened on 2026-11-10, identifying Russian original 1974 and second edition 1989. An academic-hosted complete scan was found but exceeded reader size limit. Appendix 7 context is cited at metadata level; the formal homological elimination and first-order necessary condition are independently derived.
- Item occurrences supported: 1979-463.11, 1979-463.14.

### baez2002octonions

- URL opened or attempted: https://math.ucr.edu/home/baez/octonions/octonions.pdf
- DOI: 10.1090/S0273-0979-01-00934-X
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full author PDF opened on 2026-11-10. Sections 2.2--2.3 and Section 4.2, Theorem 5, inspected. The compact F4 automorphism theorem is explicitly historical; no 2002 novelty is inferred. Real division versus split octonions must be distinguished.
- Item occurrences supported: 1979-462.12, 1979-464.2.

### balk2014rossby

- URL opened or attempted: https://npg.copernicus.org/articles/21/49/2014/npg-21-49-2014.pdf
- DOI: 10.5194/npg-21-49-2014
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full primary PDF opened on 2026-11-10. Received 28 February 2013, revised 22 September, accepted 9 November, published 10 January 2014. Sections 1.2 and 2.1 inspected: exact collision-invariant relation versus an approximate invariant of the nonlinear PDE; Rossby invariant uniqueness is attributed to Balk--Ferapontov1998. Not a claim to classify every degenerate law or prove nonlinear integrability.
- Item occurrences supported: 1979-463.3.

### balkferapontov1994invariants

- URL opened or attempted: https://www.itp.ac.ru/en/persons/balk-alexander-markovich/
- DOI: 10.1016/0167-2789(94)90059-0
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Author-institution publication list opened on 2026-11-10 and exact metadata checked. Primary publisher abstract read in search: classification of all three-wave interactions with infinitely many independent invariants via web geometry. Publisher article URL returned 403; full theorem, equivalences and regularity hypotheses not read. Publication 1 January 1994; 1993 companion article already lists it as forthcoming. Verification is metadata and abstract, not proof.
- Item occurrences supported: 1979-463.3.

### balkferapontov1998web

- URL opened or attempted: https://www.itp.ac.ru/en/persons/balk-alexander-markovich/
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Author-institution publication list opened on 2026-11-10: title, authors, collection, volume and pages checked. Linked original chapter https://www.ams.org/books/trans2/182/01 returned 403. Rossby uniqueness content is corroborated in the opened primary Balk2014 article, Section 2.1, but the 1998 proof was not retrieved.
- Item occurrences supported: 1979-463.3.

### balknazarenkozakharov1991drift

- URL opened or attempted: https://zakharov.itp.ac.ru/pub/data/1991/1991-02-1-s2.0-037596019190105H-main.pdf
- DOI: 10.1016/0375-9601(91)90105-H
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full original opened on 2026-11-10. Received 11 October 1990, accepted 14 November 1990, published 21 January 1991. Sections 4--5 verify explicit additional collision invariants for limiting drift/Rossby laws. Section 6 announces uniqueness but expressly defers its proof. This is not a proof of full nonlinear integrability.
- Item occurrences supported: 1979-463.3.

### berezin1987superanalysis

- URL opened or attempted: https://link.springer.com/book/10.1007/978-94-017-1963-6
- DOI: 10.1007/978-94-017-1963-6
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Publisher metadata and contents opened on 2026-11-10. Grassmann algebra pp.29--73 and graded linear algebra pp.90--130 identified. Full chapter not retrieved; elementary identities and the simple-spectrum lifting argument are checked directly in the companion.
- Item occurrences supported: 1979-462.10, 1979-468.1, 1979-468.3, 1979-468.5, 1979-468.6, 1979-468.9, 1979-468.10.

### berezinleites1975supermanifolds

- URL opened or attempted: https://www.mathnet.ru/eng/dan39282
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Primary Math-Net metadata opened on 2026-11-10; volume, pages and received date 24 March 1975 checked. This batch did not reread the full original paper; the Berezinian comparison is indirect and independently checked algebraically.
- Item occurrences supported: 1979-465.16, 1979-468.7, 1979-468.8.

### bernsteingelfandgelfand1978bundles

- URL opened or attempted: https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BGG-3.pdf
- DOI: 10.1007/BF01681435
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Author-hosted English original opened on 2026-11-10. Sections 2--7, Theorems 1--4, proper modules and stable equivalence inspected. Received 10 January 1978; Russian volume 1978; English translation imprint 1979. The notes' unrestricted instanton identification is stronger than the bundle theorem.
- Item occurrences supported: 1979-468.2, 1979-468.13.

### christensenduff1979indices

- URL opened or attempted: https://www.sciencedirect.com/science/article/pii/0550321379905169
- DOI: 10.1016/0550-3213(79)90516-9
- Bibliographic verification label: unverified.
- Result, locators, support and limitations: Original URL was attempted repeatedly on 2026-11-10 and returned 403. Primary publisher abstract was available in search and read; metadata and scope are also corroborated by Duff's opened 1982 lectures. July 23 1979 publication. Exact numerical spin-index coefficients and operator normalizations were not verified from full text.
- Item occurrences supported: 1979-462.6, 1979-462.7, 1979-462.9, 1979-465.8, 1979-465.19, 1979-465.23.

### duff1982ultraviolet

- URL opened or attempted: https://arxiv.org/pdf/1201.0386
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full primary text opened on 2026-11-10. Header dates CERN preprint 22 January 1982; lectures delivered at ICTP in April 1981; repository deposit January 2012 is not first circulation. Sections 2.3, 4.1 and 4.4 and historical bibliography inspected for self-dual restrictions, anomalies, boundary/gauge caveats and Kallosh's distinct 1979 letters.
- Item occurrences supported: 1979-462.6, 1979-462.7, 1979-462.8, 1979-462.9, 1979-462.11, 1979-465.1, 1979-465.8, 1979-465.13, 1979-465.14.

### eisenbudfloystadschreyer2003exterior

- URL opened or attempted: [DOI below]
- DOI: 10.1090/S0002-9947-03-03291-4}, url = {https://arxiv.org/abs/math/0104203
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full author preprint https://arxiv.org/pdf/math/0104203 opened on 2026-11-10; checked v2 dated 8 June 2001. First joint version 20 April 2001; journal 2003. Theorems 4.1 and 6.1 and Section 5 provide Tate resolution and actual monad maps.
- Item occurrences supported: 1979-468.14.

### gelfandponomarev1979model

- URL opened or attempted: https://www.mathnet.ru/eng/faa1912
- DOI: 10.1007/BF01077482
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Math-Net metadata and full Russian PDF opened on 2026-11-10; received 23 March 1979; original pp.1--12. Exact volume/issue match to Gelfand's citation. No theorem identifying the notebook's incomplete all-Dynkin Grassmann prescription was verified; match remains thematic.
- Item occurrences supported: 1979-468.4.

### gilkey1979recursion

- URL opened or attempted: https://www.numdam.org/item/CM_1979__38_2_201_0/}, note={verified
- Bibliographic verification label: unspecified.
- Result, locators, support and limitations: Primary Numdam metadata opened on 2026-11-10; exact title, 38(2), pages 201--240 and 1979 date checked. This batch used the author's 1984 monograph for explicit heat-coefficient formulas and did not claim a new full reading of this paper.
- Item occurrences supported: 1979-465.22.

### gilkey1984invariance

- URL opened or attempted: https://darkwing.uoregon.edu/~gilkey/dirPDF/InvarianceTheory1Ed.pdf
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full author PDF opened on 2026-11-10; electronic reprint 1996 of the 1984 first edition. Sections 1.5--1.7, 1.10, 2.2, 2.4, 3.1--3.4 and 4.8 consulted for elliptic/Hodge setting, heat/zeta identity, spin and characteristic-number formulas. The S4 rational example is independently computed.
- Item occurrences supported: 1979-462.5, 1979-462.8, 1979-465.2, 1979-465.4, 1979-465.6, 1979-465.9, 1979-465.10, 1979-465.11, 1979-465.12, 1979-465.15, 1979-465.18, 1979-465.20, 1979-465.21, 1979-465.22, 1979-465.23, 1979-465.24, 1979-466.1.

### hasebe2010white

- URL opened or attempted: https://arxiv.org/pdf/0805.1329
- DOI: 10.1142/S0219025710004243
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full primary v3 PDF opened on2026-11-10; first preprint9May2008, journal2010, checked revision15January2011. Page1 explicitly discusses unresolved general2D irreducibility and the flaw in Shimada's proof. Abstract metadata still repeats the earlier claim and is not used to infer a solution. Author homepage independently confirms journal metadata.
- Item occurrences supported: 1979-470.7.

### hawking1978foam

- URL opened or attempted: https://www.hawking.org.uk/in-print
- DOI: 10.1016/0550-3213(78)90375-9
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Author-estate bibliography opened on 2026-11-10; exact publication identified. Metadata only. Its January 1979 report listing is not taken as first circulation of the 1978 journal article. No rigorous measure or topology-sum convergence theorem is claimed as read.
- Item occurrences supported: 1979-462.1.

### hawkingpope1978symmetry

- URL opened or attempted: https://www.hawking.org.uk/in-print
- DOI: 10.1016/0550-3213(78)90073-1
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Author bibliography opened; publisher search-result abstract read on 2026-11-10. Publication 25 December 1978. Abstract restricts nonzero-mode pairing and one-loop cancellation to self-dual instanton backgrounds and discusses boundary-sensitive zero modes. Full original article not retrieved.
- Item occurrences supported: 1979-465.1, 1979-465.7, 1979-465.19.

### kallosh1980selfduality

- URL opened or attempted: https://www.sciencedirect.com/science/article/pii/0550321380903090
- DOI: 10.1016/0550-3213(80)90309-0
- Bibliographic verification label: unverified.
- Result, locators, support and limitations: Publisher URL attempted on 2026-11-10, inaccessible; primary search abstract read. Its self-dual superspace scope and bibliography are corroborated by Duff1982. Exact all-loop hypotheses and proof were not read. It does not justify unrestricted supergravity finiteness.
- Item occurrences supported: 1979-462.9.

### kapranov1984grassmann

- URL opened or attempted: https://www.mathnet.ru/eng/im1423
- DOI: 10.1070/IM1985v024n01ABEH001221
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Primary Math-Net page opened on 2026-11-10. Russian original 1984; English translation Math. USSR-Izvestiya 24(1) (1985), 183--192. Received 12 January 1983. DOI is for English translation. Metadata checked; theorem content read in Kapranov1988.
- Item occurrences supported: 1979-468.15.

### kapranov1988homogeneous

- URL opened or attempted: https://www.math.ucdavis.edu/~egorskiy/InformalAG/f20/Kapranov.pdf
- DOI: 10.1007/BF01393744
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full original paper opened on 2026-11-10. Section 3, Theorem 3.4 and preceding description of canonical homotopy class but noncanonical differential inspected. Complex Grassmannian derived-category model is exact for the reconstructed request, not a finite list classifying every vector bundle.
- Item occurrences supported: 1979-468.15.

### little1983translation

- URL opened or attempted: https://www.numdam.org/article/CM_1983__49_2_147_0.pdf
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full original opened on 2026-11-10. Definitions2.1--2.2, Corollary3.5, Proposition3.7 condition(*), Theorem3.9, hyperelliptic discussion after Example4.1 and Theorem5.1 inspected. Gives precise genericity and generalized-Jacobian version; no universal smoothability theorem inferred.
- Item occurrences supported: 1979-463.12, 1979-469.1, 1979-469.2, 1979-469.3, 1979-469.4, 1979-469.5.

### penrose1976nonlinear

- URL opened or attempted: https://link.springer.com/article/10.1007/BF00762011
- DOI: 10.1007/BF00762011
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Publisher page opened on 2026-11-10; January 1976 date, title, author, volume and pages verified. Full original theorem not read; used only to qualify the blanket historical claim that no curved twistor theory existed.
- Item occurrences supported: 1979-467.12.

### sanabria2017symplectic

- URL opened or attempted: https://arxiv.org/pdf/1710.00697
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full author preprint v1 dated 29 September 2017 opened on 2026-11-10. Theorem 1 and Corollary 11 inspected, including split-eigenvalue and perfect-field hypotheses. Introduction explicitly cites previous canonical-form results; the paper is a later exact proof, not evidence that the 1979 exercise was then open.
- Item occurrences supported: 1979-466.4.

### sergeichuk2000canonical

- URL opened or attempted: https://arxiv.org/pdf/0709.2485
- DOI: 10.1016/S0024-3795(00)00150-6
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full author version opened on 2026-11-10. Theorems 1.1 and 1.3 and matrix-algebra similarity framework checked independently by root; this batch also opened the original and read its setup. Reference32 records Bielefeld SFB343 preprint99-070 in1999; journal2000; arXiv deposit16September2007. Application to the finite even Grassmann matrix algebra is the companion's explicit reduction.
- Item occurrences supported: 1979-468.11.

### shimada2005irreducibility

- URL opened or attempted: https://arxiv.org/pdf/math-ph/0404042
- DOI: 10.1142/S0219025705001913
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full primary preprint opened on 2026-11-10, v2 dated1February2005; first version18April2004. The all-dimensional claim is not accepted as proved: Hasebe2010, checked2011v3 p1, identifies a false nonabelian differential identity used in Lemma4.6/equation4.28. Bibliographic verification does not certify the claimed theorem.
- Item occurrences supported: 1979-470.7.

### wallach1987gauge

- URL opened or attempted: https://www.numdam.org/article/CM_1987__64_1_3_0.pdf
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full original opened on 2026-11-10; Introduction and Theorem6.2 with proof inspected. Theorem page22 checked visually to verify root bound sqrt(8 pi |rho(x)|). Received19December1986, accepted2March1987; introductory lecture provenance Fall1986. General dimension>=3 result and parameter-restricted dimension2 result are distinguished.
- Item occurrences supported: 1979-470.1, 1979-470.2, 1979-470.3, 1979-470.5, 1979-470.7.

### woit2021euclidean

- URL opened or attempted: https://www.math.columbia.edu/~woit/twistorunification/euclidean-twistors.pdf
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full author-institution PDF dated 11 April 2021 opened on 2026-11-10. Only classical geometry in Sections 3.1 and 3.3.2 is used: real forms, graph coordinates, determinant metric, incidence and U(2) compactification. The speculative unification proposal is not used as established physics.
- Item occurrences supported: 1979-464.3, 1979-465.2, 1979-465.3, 1979-465.5, 1979-467.1, 1979-467.2, 1979-467.3, 1979-467.4, 1979-467.5, 1979-467.6, 1979-467.7, 1979-467.8, 1979-467.9, 1979-467.10, 1979-467.11.

### zakharovschulman1980degenerative

- URL opened or attempted: https://zakharov.itp.ac.ru/pub/
- DOI: 10.1016/0167-2789(80)90011-1
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Author publication list opened on 2026-11-10; 1980 metadata checked. Full original not read. The detailed theorem and limitations were read in the authors' 1988 paper. The October/September 1979 notebook is earlier oral circulation of the programme.
- Item occurrences supported: 1979-463.1, 1979-463.6.

### zakharovschulman1988invariants

- URL opened or attempted: https://zakharov.itp.ac.ru/pub/data/1988/1988-13-1988_PD_ZS.pdf
- DOI: 10.1016/0167-2789(88)90033-4
- Bibliographic verification label: verified.
- Result, locators, support and limitations: Full author-hosted original opened on 2026-11-10. Received 14 April 1986, revised 20 January 1987, published 1988. Sections 1--3, Theorem 3.1, equations 3.8--3.11, classification caveat near p.295, and Section 6 inspected. Distinguishes partial/complete degeneracy and quadratic-leading analytic invariants; does not prove the universal difference-curve classification.
- Item occurrences supported: 1979-463.1, 1979-463.2, 1979-463.3, 1979-463.6, 1979-463.7, 1979-463.8, 1979-463.9, 1979-463.10, 1979-463.11, 1979-463.12, 1979-463.13.

### zakharovshabat1974scheme

- URL opened or attempted: [DOI below]
- DOI: 10.1007/BF01075696}, url={https://www.mathnet.ru/eng/faa2357}, note={verified
- Bibliographic verification label: unspecified.
- Result, locators, support and limitations: Primary Math-Net metadata opened on 2026-11-10. Received 14 March 1974; original Russian pages 43--53, translation 226--235. The broad dressing identification is metadata-level in this batch; notebook linearizations are independently checked, not represented as a full rereading of the original proof.
- Item occurrences supported: 1979-463.4, 1979-463.5, 1979-463.7, 1979-463.8.

## Additional primary leads, failed access, and rejected substitutions

These are deliberately not promoted to exact results when only a topic or citation matches.

| Lead / URL | Observed result on 2026-11-10 | Consequence |
|---|---|---|
| Christensen–Deser–Duff–Grisaru, “Chirality, self-duality, and supergravity counterterms,” DOI `10.1016/0370-2693(79)91228-0` | Identified through Duff's opened primary historical bibliography. | Helps resolve the notebook's abbreviated bibliography; full original not read. |
| Kallosh's two 1979 JETP Letters citations | Duff's bibliography distinguishes “Super-self-duality” and “Structure of divergences in supergravitation.” | Russian pages 192 and 493 correspond to separate papers; they are not an erratum pair. |
| Cremmer–Julia, 1978, DOI `10.1016/0370-2693(78)90303-9` | Publisher abstract located; full article not retrieved; Duff supplies primary later account. | Supports only the properly qualified split-real-form symmetry context. |
| Arnold complete scan, https://www.ceremade.dauphine.fr/~fejoz/Enseignement/ds2021/Arnold_1989_MMCM.pdf | Reader rejected the 19.8 MB PDF as too large. Publisher book metadata/contents opened separately. | The formal homological calculation is independently derived; no unread textbook proof is claimed read. |
| Penrose–MacCallum, “Twistor theory: An approach to the quantisation of fields and space-time,” https://www.phys.lsu.edu/staff/karen/paper/TwistorTheory-Penrose%3AMacCallum.pdf | Reader size limit prevented opening the 11.3 MB scan. | Classical graph/incidence claims are checked from Woit's opened primary exposition and algebra. |
| Wells, 1979, “Complex manifolds and mathematical physics,” DOI `10.1090/S0273-0979-1979-14596-8` | Publisher access unsuccessful. | Reading-list identification only; not a proof source for a new statement. |
| Drinfeld–Manin, 1979, Yadernaya Fizika 29(6), 1646–1653; English 845–849 | Identified as “Yang–Mills fields, instantons, and tensor products of instantons.” | This is not automatically the distinct “Instantons and sheaves” result. Exact notebook theorem not identified. |
| Márki–Meyer–Szigeti–van Wyk, arXiv:1307.0292 | Grassmann matrix embeddings/identities appeared as an adjacent search lead; full work not used. | Not an identified all-odd-matrix commutant classification. |
| Driver–Hall, “The energy representation has no non-zero fixed vectors,” https://mathweb.ucsd.edu/~bdriver/DRIVER/Papers/energy15.pdf | Title and 1999 preprint/2000 publication lead located; full theorem not opened in this batch. | Absence of fixed vectors does not establish irreducibility. |
| Janssens–Neeb, 2024, “Positive energy representations of gauge groups I: Localization” | Independently checked by root. | Projective positive-energy semidirect representations have different hypotheses; no ordinary-energy solution is inferred. |
| Janssens–Niestijl, 2025, DOI `10.1007/s00220-024-05226-w` | Primary publisher result surfaced in the current search. | Diffeomorphism-group positive-energy work, not the ordinary two-dimensional energy representation. |
| AMS original web-geometry chapter, https://www.ams.org/books/trans2/182/01 | Returned 403. An attempted PDF endpoint was also inaccessible. | Chapter metadata comes from the opened author-institution list; uniqueness content is corroborated in Balk's opened 2014 primary article, not read from the original proof. |
| Balk–Ferapontov original 1994 article, https://www.sciencedirect.com/science/article/pii/0167278994900590 | Returned 403; primary abstract accessible in search, author-institution metadata opened. | Infinite-invariant classification is identified, but exact local/branch hypotheses remain unverified. |
| Balk's author page, https://www.math.utah.edu/~balk/ | Opened; contact page only, no full-text links. | No additional proof obtained. |
| Ferapontov institution list, https://publications.lboro.ac.uk/publications/all/collated/maevf.html | Search provided publication entries; direct open timed out. | Not used to claim full-text access. |
| Balk's SIAM Review article, https://epubs.siam.org/doi/10.1137/S0036144595291973 | Publisher metadata, abstract and references opened; 1997 volume 39(1), 68–94; online platform date 2006. | Confirms web-geometry development and bibliography, but its full proof is paywalled. The 2006 platform date is not first circulation. |
| Cambridge Page/Atiyah fragments | Queries returned Page's Green-function and compact-instanton papers, “Polygons and gravitons,” and boundary-index articles. | None determines the unclear notebook abbreviation; the oral fragment stays F. |

The super-index programme, all-Dynkin Grassmann-algebra suggestion, higher-dimensional twistor contest, unspecified four-manifold classification report and universal integrability speculation remain underdetermined. Broadly related literature does not supply the missing quantifiers, objects, or equivalence relation.

## Search strings and source-navigation record

The following exact query strings were used or rerun in this batch. Search engines were alternated according to coverage; primary pages and author originals, rather than secondary snippets, were used to support theorem claims. Searches with no exact hit were retained as limited negative evidence only.

### Gravity, indices, mechanics and twistors

- `Arnold Mathematical Methods Classical Mechanics Birkhoff normal form Poincare theorem nonexistence integrals pdf`
- `Penrose nonlinear gravitons curved twistor theory 1976 General Relativity Gravitation doi`
- `Christensen Duff new gravitational index theorems supertheorems 1979 pdf`
- `Aragone Deser Consistency problems hypergravity 1979 86 161 163`
- `Hawking Pope symmetry broken instantons Nuclear Physics B146 381 392 1978`
- `Kallosh Cambridge 1979 Page Atiyah Coleman Jackiw gravitational instantons meeting`

### Supermatrices, BGG and double translations

- `Berezin odd Grassmann matrices even commutant canonical form`
- `"odd" "Grassmann" "centralizer" matrices`
- `Eisenbud Floystad Schreyer BGG Beilinson monad explicit maps Grassmannian Kapranov`
- `"On the derived categories of coherent sheaves on some homogeneous spaces" DOI`
- `Little 1983 translation manifolds Lie Wirtinger theorem`

The broad centralizer query produced Grassmann embeddings, centrally essential rings, queer trace identities and automorphism-stable subspace papers, not the exact all-A structural classification. This does not make the finite kernel problem open. Direct source navigation to Sergeichuk, EFS, Kapranov, BGG and Little supplied the principal evidence instead.

### Energy representation

- `"On the local structure" "Ando" "2010" "representation"`
- `"White noise analysis on manifolds" Hasebe 2010 619 627`
- `"On irreducibility of the energy representation" Shimada 2005 153 177`
- `"energy representation" "irreducibility" "two" "gauge" 2025 2026` (current coverage, recency 730 days)

The searches were followed by opening Wallach's original paper, the Shimada preprint, Hasebe's version-3 primary text, Ando's preprint, the Albeverio et al. Brownian/path paper and the Hasebe author bibliography. An erroneous secondary coauthor attribution for Hasebe was discarded in favour of the primary author page and original PDF. The exact two-dimensional residual was not replaced by recent positive-energy semidirect-group results.

### Resonance classification: final corrective search

- `"On additional motion invariants of classical Hamiltonian wave systems" DOI`
- `"New invariant for drift turbulence" "10.1016"`
- `"Translation manifolds and the converse of Abel" "147"`
- `"degenerate dispersion laws" "classification" Zakharov Schulman`
- `Balk Ferapontov 1998 classification degenerative dispersion laws web geometry`
- `Zakharov Schulman difference curve dispersion laws universal formula classification web Ferapontov`
- `"Balk" "Ferapontov" "Wave systems" pdf`
- `"Invariants of wave systems and web geometry" pdf`
- `"difference" "dispersion" "Ferapontov"`
- `"Balk" "Ferapontov" "Wave systems with" filetype:pdf`
- `"Invariants of wave systems and web geometry" "pdf"`
- `Ferapontov publications 1994 100 114 pdf web invariants`
- `"Invariants of Wave Systems" "ams.org"`
- `"Balk" "Ferapontov" "coordinate" "dispersion"`
- `"Balk" "Ferapontov" "1998" "theorem" invariants`
- `"Wave systems with an infinite number of invariants" "pdf" "Balk"`
- `"Invariants of wave systems and web geometry" classification`

This sequence materially changed the classification. The 2014 PDF led through its Section 1.2 and Section 2.1 references to the 1994 classification, the 1998 chapter, and the 1991 finite-invariant examples. The 1991 original was opened in full; its Section 6 says that the uniqueness proof will appear separately, preventing an overstatement of what that particular paper proves. The broader hydrodynamic-system classifications returned for Ferapontov were not substituted for the exact wave-resonance question.

## Reproduction and handoff

Run `python parts/early/build_early.py` and `python parts/early/build_bibliography.py` to reproduce the structured batch. Run `python parts/early/verify_annotations.py` for the saved numerical/exact checks. Run `python parts/early/write_research_log.py` after any bibliography change to rebuild the evidence ledger. `finalize_resonance.py` records the late corrective edit; the resulting main authoring scripts already incorporate it.

The final early batch contains 9 talks, 101 items, 7 problem-index entries, 47 correction/provenance rows and 37 bibliography entries. The class counts are E=72, F=18, A=6, B=4, C=1, D=0. There is no C/D claim based solely on failure to locate a publication. The root controls final integrated page normalization, DOI-metadata upgrades, full chapter rendering, and the developed mathematical sections.
