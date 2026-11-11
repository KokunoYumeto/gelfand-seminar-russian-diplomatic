# Research and scan audit: spring / integrable systems shard

**Scope and audit date:** records 586, 587, 588, 589, 590, 591, 592, 594, 593, 596, 595, 598; verified through **11 November 2026**. Read CHAPTER_FORMAT.md before authoring and the complete GY1982_prompt.md. Both English and Russian transcriptions were consulted throughout the assigned material. Russian was reread page by page for formula-heavy portions and every ambiguity below. Original scans, not transcription typography alone, determine emendations.

## Deliverable and reproducibility

The six required shard files are talks.json, items.json, problems.json, corrections.csv, references.bib, and this audit. The authoring script write_records.py saves after every record. The bibliography script preserves cumulative keys and produces source_audit.json. The audit script produces this document and area_by_record.json. independent_checks.py and checks_output.json contain exact elementary checks. Root owns the joint chapter, substantive development, final build and delivery.

source_segments.json is the website/source attribution map. Catalogue ranges are retained verbatim in talk metadata; exact item locations do not inherit those overlaps.

| Record | Actual source segment | Boundary decision |
|---|---|---|
| 586 | P001087 to upper P001089 | Ends before Wodzicki; P001086 ends Arnold, record 585. |
| 587 | Lower P001089–P001092 | Includes determinant and Clausen interventions. |
| 588 | P001093 to upper P001094 | Ends at Semenov-Tian-Shansky heading. |
| 589 | Lower P001094–P001095 | Drinfeld pointer belongs to this heading. |
| 590 | P001096–P001098 | Includes Fedosov and Gelfand interventions. |
| 591 | P001099–P001100 | Includes Krichever’s final KP intervention. |
| 592 | P001101–P001107 | Detailed Wilson lecture. |
| 594 | Written strip of P001108 | Before record 593 in notebook order. |
| 593 | P001109–P001112 | Extends beyond its catalogue end. |
| 596 | P001113 above Beilinson | Before 595; opening Levinson plan has no specified theorem. |
| 595 | Lower P001113, then P001114 around Wodzicki | Resumed “B.” paragraph belongs to Beilinson. |
| 598 | Middle interruption of P001114 | Ends before “B.”; not the full catalogue range. |

P001115 starts **5 September 1983**, with Deligne on Faltings/families/Néron-type degeneration. It is outside this academic-year shard. Overlapping catalogue ranges for 596 and 598 do not attribute September material to either speaker. This is a provenance correction.

## Scan inspection register

All source scans **P001087–P001115** were visually inspected. P001087–P001091 were inspected at original resolution in the early pass; P001092–P001115 as full-page 1150-pixel previews, with original/cropped inspection where needed. Reduced images are in scan_review; originals remain in work/scans. P001115 is inspected to verify exclusion.

| Scan | Details checked visually |
|---|---|
| P001087 | Krichever heading/date; perturbed KdV; incompatible \(I_3\) density and variational derivative. |
| P001088 | Old edges/double points; Hessian; gap numerator/denominator; higher-variation request. |
| P001089 | Speaker boundary; logarithmic theta expression; repeated pairing index; Hill zeta; rational-shift question; malformed binomial series. orthogonality.png confirms repeated \(s\) versus \(s'\). |
| P001090 | Quasimomentum graph; universal polynomials; factorial/denominator ambiguity. No unsupported factorial restoration. |
| P001091 | Explicit \(T=2\pi\); Bernoulli factor; opposite \(g_3\) signs; period diagram. Sign pair is compatible with \(E=-\wp(a)\). |
| P001092 | Determinant query; even-zeta normalization; \(B_2\) in cube sum; D-module diagram; Clausen definitions and \(\zeta(-5)\). |
| P001093 | Novikov’s closed-form action and monopole; tentative Witten/chiral-field aside. |
| P001094 | Target-chart covering; physical phase; Semenov heading; Drinfeld issue “5”; unhalved bracket and factorization. |
| P001095 | Modified equation; \(R\pm1\); double and hierarchy; no skew restriction in Gelfand’s \(sl_2\) query. |
| P001096 | Wodzicki/Fedosov boundary; APS projection; unsquared cutoff partition versus squared matrix entries. |
| P001097 | Incomplete/full projectors; \(a=f_1\sigma\); Todd conventions; overwritten zero. cutoff1097b.png is useful; first crop cutoff1097.png was inadequate. |
| P001098 | Local index; formal cohomology; boundary signature operator; APS I–III; coefficient K-groups. |
| P001099 | Continuous loops; Fredholm/compact projections; “unsolved” criterion; dense Krichever locus. |
| P001100 | Miura flag; central extension; Krichever zero-curvature operators and tau sign. |
| P001101 | Full Grassmannian/index-zero annotation; components and admissible frames. Reinspected in final pass. |
| P001102 | Block determinant; transversality; tau normalization/nonvanishing; charge-zero sets. |
| P001103 | Schur/Plücker; GL(n) query; curve/sheaf/disc; index \(\chi(\mathcal L)-1\). |
| P001104 | Čech diagram; theta factorization; broad abelian-variety programme; Baker uniqueness/meromorphic qualification. |
| P001105 | Miwa shifts; vertex operator; positive-part notation; finite poles; missing factor 2. |
| P001106 | Frame bundle \(\mathcal P\), changes \(\mathcal T\), pairs \(\mathcal E\) are distinct. |
| P001107 | Miura factor order; analytic cell/meromorphic flags; Galois analogy. |
| P001108 | April 11/Wilson; short conclusion; \(2q_1\); upper region blank. |
| P001109 | Ginzburg; cited authors; volume/Pfaffian shorthand; polynomial versus piecewise polynomial. |
| P001110 | Borel double fibration; localization; circle coefficient ring and degree. |
| P001111 | Extra \(u\) in \(d_1^2\); correction to invariant forms; parity grading; group-free query. |
| P001112 | Successful repair \(\beta=\alpha(1+d\alpha)^{-1}\); correct contracting identity. |
| P001113 | April 18; Levinson plan; Ginzburg/Beilinson boundary; Hamiltonian insertion; convexity credit; good reduction at every prime. |
| P001114 | Local exponential and \(1/n\) absent; zero variable; global questions; Wodzicki interruption; Beilinson completion. |
| P001115 | September 5, 1983, Deligne: excluded. |

## Research decisions and scope controls

### Finite gap theory and spectral zeta

Krichever’s 1983 paper exactly matches the Hessian and first-order gap basis. Submission preceded the talk, but submission is not public circulation: matching new results remain A. Stationary hierarchy and quasimomentum are E. Higher variations are F because the requested spectral coordinates or target identity are unspecified; ordinary derivatives do not justify inventing an open conjecture. The printed mode is a theta quotient with doubled Abel shifts, not the notebook’s single-theta logarithm; the genus-zero limit confirms a real difference.

Wodzicki’s 1984 paper explicitly records a Manin seminar presentation in November 1982. The universal-polynomial theorem matches, but ambiguous notebook factorial conventions are not certified. The determinant-derivative identity gives an exact computational formulation. Lamé’s reflected spectral coordinate explains the opposite cubic signs. The full Clausen expression was not found there; only the free specialization and definition are verified. The arithmetic query and D-module extension diagram lack sufficient data for definite later problems.

The multiplicative-anomaly formula is restricted to **commuting, positive, invertible, classical elliptic self-adjoint operators**, positive real orders, same bundle, closed manifold. The primary 2015 paper states these assumptions; Kontsevich–Vishik covers admissibility and cuts. Logarithms of positive-order operators have logarithmic symbol terms; \(b\log A-a\log B\) cancels the leading log term and is classical of order zero. No arbitrary product is assumed cut-admissible.

### Classical r-matrices

Semenov-Tian-Shansky’s paper was received 15 April 1983 and revised 16 May, after the March lecture. The unhalved bracket requires \(2t\). Local factorization and common-quotient compatibility do not imply global decomposition. The quadratic theorem needs associative multiplication, invariant nondegenerate trace pairing and skew \(R\) satisfying the modified equation.

The \(sl_2\) question concerns all operators, without skewness. Gubarev–Kozlov Proposition 2.5 supplies weight-one Rota–Baxter normal forms via \(R=2B+I\). Conjugacy, the involution \(B\mapsto-I-B\), and trivial cases are retained. The code verifies solutions and conventions, not completeness. Drinfeld’s separate pointer is Doklady 268(2), 285–287, received June 4, 1982; issue 5 is wrong. His compatible dual bracket/cobracket is distinct from a bare double Lie algebra.

### Index theory, loops and KP

APS retains the kernel term and product collar. Eta regularity reuses GP-1981-43: APS III gives odd dimension; Gilkey 1981 gives all dimensions. Global regularity does not imply pointwise zero local residue. GP-1981-44 is E: Seeley’s 1968 translated preprint already gives non-self-adjoint calculus under a principal-symbol ray condition. Excluding discrete global spectrum near the imaginary axis does not specify a complete boundary problem.

Fedosov’s orthogonal block needs \(f_1^2+f_2^2=1\) and unitary normalization. His later pair is algebraically idempotent even for arbitrary auxiliary maps. The literal \(a=f_1\sigma\) issue concerns support of the difference, **not idempotence**. The ambiguous subscript is not declared an OCR error.

The loop reconstruction is only for essentially bounded **unitary** matrix loops. For a unitary block multiplier \(U=(a,b;c,d)\), compact \(c\) gives \(a^*a=1\) in the Calkin algebra; Fredholm \(a\) is invertible there, so \(aa^*=1\), hence \(bb^*=0\) and \(b\) compact. Conversely compact \(b,c\) make \(a\) essentially unitary. Hartman then yields entries in \(QC=(H^\infty+C)\cap\overline{H^\infty+C}\). This marked own deduction is not a novelty claim or a solution for all unspecified GL-valued loops.

Segal–Wilson results were checked individually. Continuous based unitary loops are dense, not all of the completed loop Grassmannian. Frames and determinants use index zero. Proposition 6.1 gives \(\chi(\mathcal L)-1\) in the printed polarization. Theta comparison is **Theorem 9.11**. Finite-pole Fuchs bounds do not address infinity. Miura flags are local; periodic global factors need monodromy conditions. The all-abelian-variety programme and differential-Galois diagram remain F.

### Localization and arithmetic status, November 2026

Duistermaat–Heckman is 1982 background. Atiyah–Bott appeared in 1984, but was received December 1982 and cites 1982 Berline–Vergne and DH-addendum preprints. Nonisolated fixed components need the full equivariant Euler class. Reduced **cohomology classes** vary affinely; densities are polynomial **on chambers**. Convexity needs a compact connected Hamiltonian torus manifold. Credit is Atiyah and Guillemin–Sternberg; the notebook conflates this with Atiyah–Bott localization. The April report is related to Ginzburg’s autumn representation/microlocal line, but not the same questions as 568 or 570.

P001112 repairs its own failed angular-form requirement. Independently, \(D\alpha=1+d\alpha\), \(D(d\alpha)=0\), so \(D\beta=1\); the parity Leibniz rule gives the contracting identity. This check is marked in the item. No new localization theorem is claimed.

Beilinson’s heading records no BSD rank equality, leading coefficient, regulator determinant or specified special value. Continuation (GP-1982-42) and actual automorphy (GP-1982-43) are distinct. The local factor needs the exponential and \(1/n\); a smooth model exists outside finitely many primes. Finite-field purity does not prove the global assertion. The elliptic completion needs \(L(H^1(E),s)\), conductor \(N^{s/2}\) and root number.

The current result was checked in **BCGP 2021 itself**. Theorem 1.1.2 gives meromorphic continuation/functional equation for every genus-two curve or abelian surface over a totally real field; 1.1.3 gives potential automorphy. Page 157 explicitly denies control of poles over the original field. Preprint end of 2018; IHES publication 2021. The 2025 Theorem B proves actual modularity for a **smooth genus-two curve \(y^2=f(x)\) over Q, degree 5, surjective mod-3 GSp4 image, good ordinary reduction of the curve at 2 and 3**. It is not universal modularity of abelian surfaces. Gee’s 2026 ICM article is the primary current account; **Remark 2.7**, not section 2.7, gives chronology.

Shintani’s totally real cone method is verified through Cassou-Noguès’s primary 1981 report, published 1982. It does not verify an ordinary elliptic torus-operator realization. The original 1976 paper was not obtained; NII returned a robot page and is not counted as original-paper verification. An AIF 1981 metadata record names “Philippe” while its scan says “Pierrette”; that entry was not imported. The cited 1982 primary PDF clearly identifies Pierrette.

## Search audit and unresolved identifications

Adaptive searches used MathNet, Numdam, author PDFs, publisher sites and arXiv. The following are actual query families, not claims of exhaustive searches.

| Item | Query family / result sought | Outcome |
|---|---|---|
| 586 | Krichever Hessians, finite-gap perturbation, third/higher variations | Exact 1983 paper; no exact higher-variation spectral-coordinate theorem identified. |
| 587 | Wodzicki Hill finite-zone positive zeta, Lamé, Clausen negative derivatives | Exact 1984 theorem; no full branch-sensitive Clausen match. |
| 587 determinant | Multiplicative anomaly, Wodzicki formula, KV cuts | Exact commuting formula and admissibility verified. |
| 588 | Novikov many-valued Morse, Dirac map-space actions | Exact 1982 survey; chiral-field aside remains tentative. |
| 589 | Semenov classical r-matrix, sl2 modified equation, weight-one Rota–Baxter | Exact exposition and unrestricted operator classification; skew-tensor-only results rejected as substitutes. |
| 590 | APS no-filling eta, Gilkey residue, cuts, Seeley powers | Exact pre-talk sources; metadata limits explicit. Formal combined cohomology remains underspecified. |
| 591–592 | Segal Wilson KdV, compact Hankel QC, Miura flags, abelian theta, Shiota | Exact construction; precise unitary-loop reconstruction; Shiota metadata only and thematic. |
| 593–596 | DH localization, Atiyah Bott Cartan, Vergne primitive, convexity | Full contemporary localization paper and original convexity theorem. DH author metadata; theorem checked in AB. |
| 595 | Hasse–Weil curves current 2026, genus-two potential modularity, 2025 abelian surfaces, Gee ICM | Original 2021/2025 theorem statements plus 2026 account; no blanket holomorphy. |
| 598 | Shintani Dedekind torus constant coefficients pseudodifferential, negative integers | Exact cone arithmetic scope; no exact ordinary elliptic operator theorem. |

No D label is assigned merely because a search failed. F means the proposition or intended version is not identifiable. Both C items specify what remains open.

## Earlier-year matching

Exact GP reuse: **GP-1981-43**, global eta without a filling; **GP-1981-44**, removal of self-adjointness. Earlier 1981-559 occurrences are retained. Repeated APS/local-index background links to 1981-558.1–4, 558.7–8, 558.11–12 and 559.2, 559.10–11. Convexity links to 1981-556.12 and 1980-508.15. Theta background links to 1977-431.3; brackets to 1977-426.5/426.10 without reusing the different first-bracket Jacobi problem. Beilinson 1979-476.11 is thematic only. The supplied index contains no exact prior GP for the four new questions 40–43.

## Independent checks and limits

independent_checks.py passed exact SymPy identities and 60-digit mpmath comparisons: Euler–Lagrange derivatives; Hermitian 2x2 discriminant; orthogonal projector normalization; both noncommutative idempotents and bad-cutoff limit; sl2 representatives/involutions; free-circle zeta derivative at periods 1, 2π, 7/3; second-order Miura factor order. It does not prove classification completeness, the full spectral expansion or any arithmetic conjecture. The Calkin and Vergne checks above are separate short proofs. Own computations and deductions are marked in item text.

validate_shard.py and validation_report.json additionally check fields, enums, source order, consecutive IDs, citation/refs consistency, raw LaTeX math delimiters and an explicit correction-row map for every item marked false as written. All pass. A separate second-reader review of the root four-unitary development is in development_review.md, with an independent character calculation and isolated rerun of the root checker. Its coefficients and local-theorem application pass; no shared parent output was edited.

## Per-reference opened-source audit

Every key below has a real URL opened in this run. Metadata checking is not promoted to reading a result. Where an original was unread, the mathematical source is identified separately. source_audit.json is the structured equivalent.

### apery1979irrationalite

- Opened: https://numdam.org/item/AST_1979__61__11_0.pdf
- Verification: **result read**.
- Locator and scope: Full original read; irrationality theorem and proof pp. 11--13; publication 1979 after 1978 report.

### atiyah1982convexity

- Opened: https://www.math.stonybrook.edu/~azinger/mat562/Atiyah82.pdf
- Verification: **result read**.
- Locator and scope: Theorem 1 and hypotheses read; compact connected Hamiltonian action. Received 27 March 1981; publication 1982.

### atiyahbott1984moment

- Opened: https://www.math.stonybrook.edu/~mmovshev/MAT570Spring2008/BOOKS/atiyahbott_moment.pdf
- Verification: **result read**.
- Locator and scope: Full primary PDF, sections 2--8 read, especially integration formula (3.8), invariant Cartan complex, parity specialization and fixed-point denominator. Received 20 December 1982. Bibliography gives Berline--Vergne Rennes 1982 and DH Utrecht 1982 preprints, so 1984 is not a first-circulation date.

### atiyahbottpatodi1973heat

- Opened: https://link.springer.com/article/10.1007/BF01425417
- Verification: **publisher metadata checked; mathematics in other cited primary source**.
- Locator and scope: Publisher page opened for metadata. Local-density mathematics verified against Gilkey first-edition text and APS I.

### atiyahpatodisinger1975spectral1

- Opened: https://webhomes.maths.ed.ac.uk/~v1ranick/papers/aps001.pdf
- Verification: **result read**.
- Locator and scope: Theorem 3.10 and section 4 signature discussion read; product collar, kernel correction, eta convention. Received 25 March 1974.

### atiyahpatodisinger1976spectral3

- Opened: https://webhomes.maths.ed.ac.uk/~v1ranick/papers/aps003.pdf
- Verification: **result read**.
- Locator and scope: Theorem 4.5 and opening discussion read; odd-dimensional eta regularity. Received 24 January 1975.

### boxercalegarigeepilloni2021surfaces

- Opened: https://numdam.org/item/10.1007/s10240-021-00128-2.pdf
- Verification: **result read**.
- Locator and scope: Theorems 1.1.2 and 1.1.3 and discussion pp. 155--157 read. Continuation/functional equation in 1.1.2; potential automorphy in 1.1.3; the latter does not control poles over the original field. Publisher page opened: received 25 December 2018, accepted 27 October 2021, online first 29 November 2021, online issue 28 December 2021. Gee 2026 Remark 2.7 confirms preprint online at end of 2018.

### boxercalegarigeepilloni2025modularity

- Opened: https://arxiv.org/pdf/2502.20645
- Verification: **result read**.
- Locator and scope: Version 1 posted 28 February 2025. Theorems A and B and section 9.5 read. Theorem B: smooth genus-two curve y^2=f(x), degree 5, mod 3 image GSp4(F3), good ordinary reduction of the curve at 2 and 3. These conditions cannot be omitted. General genus-two meromorphic continuation and actual modularity are not conflated.

### breuilconraddiamondtaylor2001modularity

- Opened: https://virtualmath1.stanford.edu/~conrad/papers/tswfinal.pdf
- Verification: **result read**.
- Locator and scope: Theorem A and Introduction read: every elliptic curve over Q modular. Not the entire modularity-lifting proof.

### cassounogues1982series

- Opened: https://www.numdam.org/item/AST_1982__94__1_0.pdf
- Verification: **result read**.
- Locator and scope: Full primary research report read, opening pages and section I, Lemma 1 and Shintani-cone series discussion. Proceedings of 1981 Metz arithmetic days, published 1982. It reports Shintani 1976 for totally real fields and provides polynomial-series extensions; it does not state an ordinary elliptic torus-operator realization. Original Shintani 1976 text not obtained. The distinct 1981 AIF paper was not cited because publisher metadata names Philippe while its scanned title page says Pierrette.

### castillogarate2015anomaly

- Opened: https://intlpress.com/api/bgcloud-front/resource/pdf/volume/1806603322847031297-1806603322847031297-e1c0090d83aec9716fd5626a68b4a5ae.pdf
- Verification: **result read**.
- Locator and scope: Full journal PDF opened successfully earlier in this run; equation (1) and preceding hypotheses read. Later repeated fetch returned 403; this does not erase the successful full-text reading. The formula is for commuting positive invertible elliptic self-adjoint pseudodifferential operators, positive orders, same bundle on a closed manifold. Not a theorem for arbitrary noncommuting or cut-incompatible products.

### deligne1974weil

- Opened: https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf
- Verification: **result read**.
- Locator and scope: Section 1 local zeta and Theorem 1.6 purity read. July 1973 lectures; received 20 September 1973; publication 1974.

### drinfeld1983hamiltonian

- Opened: https://www.mathnet.ru/eng/dan45858
- Verification: **result read**.
- Locator and scope: Full Russian three-page paper opened and read, section 4 definition and Theorem 2, Theorem 3 on integration, section 7 on skew solutions. Presented 24 May 1982, received 4 June 1982, published 1983. Actual issue 268(2), not notebook issue 5. This source confirms the Lie-bialgebra terminology, not the unrestricted nonskew operator classification.

### drinfeldsokolov1981equations

- Opened: https://www.mathnet.ru/eng/dan44415
- Verification: **publisher metadata checked**.
- Locator and scope: Publisher metadata checked: received 27 November 1980, published 1981. Earlier announcement is explicitly cited as such by the 1984/1985 full survey. No equation-level claim is based on an unread original.

### drinfeldsokolov1985lie

- Opened: https://math.berkeley.edu/~frenkel/Drinfeld-Sokolov.pdf
- Verification: **result read**.
- Locator and scope: Full English translation read in section 3.7 (Miura transformation, Proposition 3.26) and section 6. Russian original 1984, Itogi 24,81--180; English publication 1985. Introduction identifies the 1981 announcement; MathNet intd72 verifies DOI and both publication dates.

### duistermaatheckman1982variation

- Opened: https://www.math.ru.nl/~heckman/
- Verification: **primary-author metadata checked; result checked in contemporary primary treatment**.
- Locator and scope: Author bibliography opened for exact journal/date/pages, including the distinct 1983 addendum. Original full article was not retrieved. Exact mathematical statements read in Atiyah--Bott 1984 sections 6--7, which explicitly identify the 1982 theorem and its assumptions.

### gee2026modularity

- Opened: https://epubs.siam.org/doi/full/10.1137/25M1806697
- Verification: **result read**.
- Locator and scope: Author research account read: section 1, Theorems 1.4--1.5, Remark 2.7, and discussion of future lifting/classicality work. Gives precise current scope and end-2018 preprint chronology. Section 2.7 is not a section; the correct locator is Remark 2.7.

### gilkey1981residue

- Opened: https://pages.uoregon.edu/gilkey/dirPDF/gilkeyAdvances.pdf
- Verification: **result read**.
- Locator and scope: Theorem 0.1 and Introduction read: all-dimensional global eta regularity for classical elliptic self-adjoint positive-order operators; local residue need not vanish.

### gilkey1984invariance

- Opened: https://darkwing.uoregon.edu/~gilkey/dirPDF/InvarianceTheory1Ed.pdf
- Verification: **result read**.
- Locator and scope: Full first-edition electronic reprint opened; sections 1.7,1.10,2.4--2.6, Chapter3, and sections 4.3--4.4 consulted. Original 1984, electronic reprint 1996.

### gubarevkozlov2023rota

- Opened: https://ieja.net/files/papers/volume-33/15-IEJA-3522.pdf
- Verification: **result read**.
- Locator and scope: Section 2.1, Proposition 2.5 and proof read for ordinary sl2 weight-one Rota--Baxter operators. Their current-Lie-conformal classification is a different main theorem. The involution B to -Id-B is retained when using the finite-dimensional normal forms. Received 13 September 2022; accepted 8 November 2022.

### kontsevichvishik1994geometry

- Opened: https://arxiv.org/pdf/hep-th/9406140
- Verification: **result read**.
- Locator and scope: Full primary preprint read, sections 1--2 on admissibility, cuts and anomaly. Posted 21 June 1994, explicitly an abridgement of hep-th/9404046 (April 1994). Logarithmic symbols and classical order-zero log differences are distinguished.

### krichever1983hessians

- Opened: https://www.mathnet.ru/eng/dan46140
- Verification: **result read**.
- Locator and scope: Full Russian PDF read: Theorems 1--3, Lemmas 1--3, equations (6), (13)--(19). Presented 19 October 1982; received 23 November 1982. Submission is not evidence of public circulation.

### nist2026dlmf

- Opened: https://dlmf.nist.gov/25.11
- Verification: **formulas read**.
- Locator and scope: Official sections 25.11,25.6,25.4 opened for Hurwitz zeta, even/negative values and functional equation. Access 2026 is not discovery date.

### novikov1982hamiltonian

- Opened: https://homepage.mi-ras.ru/~snovikov/74.pdf
- Verification: **result read**.
- Locator and scope: Author-hosted full text, sections 4--5 read for Dirac periods and many-valued map-space actions. Publisher metadata at https://www.mathnet.ru/eng/rm3819 opened; received 22 April 1982.

### page1975compact

- Opened: https://msp.org/pjm/1975/56-1/pjm-v56-n1-p20-p.pdf
- Verification: **result read**.
- Locator and scope: Full paper read, pages 221--223: a proof of Hartman (1958) compact-Hankel theorem. Received 25 September 1973; published November 1975. The unitary-loop QC equivalence is our marked elementary Calkin-algebra deduction, not a theorem quoted verbatim from Page.

### seeley1968powers

- Opened: https://www.mathnet.ru/eng/mat458
- Verification: **result read**.
- Locator and scope: Publisher metadata and full Russian PDF opened. Introduction pp. 96--98 read: non-self-adjoint principal-symbol ray condition, complex powers and the shifted-zeta index cancellation. Page 96 calls the source a preprint. The distinct 1967 proceedings article is not silently substituted.

### segalwilson1985loop

- Opened: https://www.numdam.org/item/PMIHES_1985__61__5_0.pdf
- Verification: **result read**.
- Locator and scope: Full primary paper consulted: sections 2--3, 5--6, 8--10; Proposition 2.7 (dense continuous-loop image), Proposition 6.1 (index), Propositions 5.1, 5.5, 5.9, Corollaries 5.12 and 5.18, Proposition 5.17, equation (5.19), Propositions 8.2--8.3 and 8.6, Theorem 9.11. These seminar notes themselves document March--April 1983 circulation.

### semenov1983classical

- Opened: https://www.mathnet.ru/eng/faa1574
- Verification: **result read**.
- Locator and scope: Full Russian PDF read: section 1 Theorem 1; section 4 Proposition 9 and Theorem 11 (including factor 2); section 5 Theorem 13, equations (22)--(23). Received 15 April 1983, revised 16 May 1983. The quadratic theorem assumes a skew R on an associative algebra with invariant trace pairing.

### shiota1986characterization

- Opened: https://link.springer.com/article/10.1007/BF01388967
- Verification: **publisher metadata checked**.
- Locator and scope: Publisher metadata and displayed references only. Bibliography records 1983 Kyoto seminar notes separately from the June 1986 article. Full theorem was not read, and this is not claimed to solve the all-abelian-varieties programme.

### wodzicki1982spectral

- Opened: https://link.springer.com/article/10.1007/BF01404760
- Verification: **publisher metadata checked**.
- Locator and scope: Publisher metadata opened: February 1982, Invent. 66,115--135. Full original unread. Exact operator-domain/cut statements checked in Kontsevich--Vishik 1994 and Gilkey book.

### wodzicki1984values

- Opened: https://www.mathnet.ru/eng/faa1431
- Verification: **result read**.
- Locator and scope: Full Russian PDF, Theorems 1--2 and section 4 read. Russian pages 67--69; English pages 55--57. Received 25 July 1983. Final paragraph explicitly records a Manin-seminar report in November 1982.

## Structured counts

{
  "talks": 12,
  "items": 71,
  "problems": 6,
  "classes": {
    "E": 33,
    "A": 21,
    "F": 12,
    "B": 3,
    "C": 2
  },
  "references": 31
}
