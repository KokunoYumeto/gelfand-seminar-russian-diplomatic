# Research and audit log: GY1975, records 386–396

Status checked on **10 November 2026**. This file documents the evidentiary scope of the authored fragments; it is not a claim to have surveyed every publication in each subject.

## Deliverables and coverage

The block contains **11 catalogue records, 85 mathematical items, 8 problem-index objects and 27 correction rows**. The item classes are A: 3, B: 9, C: 4, D: 0, E: 66, F: 3. Each item has an area, a precise page or page range, an explicit modern statement, and separate source-identification and correctness assessments. There are 35 entries in `c_references.bib`; two additional cited entries, `roiter1978roots` and `perchik1975dissertation`, belong to `root_references.bib` and are deliberately not duplicated. All 37 sources have records in `c_sources.json`.

| Record | Date | Items | Mathematical pages |
|---|---|---:|---|
| 386 | 15 March 1976 | 9 | P000644–P000647 |
| 387 | 22 March 1976 | 2 | P000648 |
| 388 | 22 March 1976 | 7 | P000648–P000649 |
| 389 | 22 March 1976 | 8 | P000649–P000650 |
| 390 | 22 March 1976 | 5 | P000650 |
| 391 | 29 March 1976 | 17 | P000651–P000653 |
| 392 | 5 April 1976 | 4 | P000654 |
| 393 | 12 April 1976 | 11 | P000655–P000656 |
| 394 | 12 April 1976 | 12 | P000656–P000657 |
| 395 | 19 April 1976 | 6 | P000657–P000658 |
| 396 | 19 April 1976 | 4 | P000658 |

The original Russian and English TeX files and the extracted slices were consulted. The Russian manuscript governs uncertain formulas and speaker attribution. Broad catalogue page ranges are retained in the talks file; those broad ranges are not used as evidence that every item occupies every listed page.

## Boundaries and recurrence

P000643 and the upper part of P000644 conclude the preceding Krichever/Drinfeld discussion. They belong to the earlier block. Polyakov starts at the explicit heading in the middle of P000644. P000647 announces continuation on 5 April; that continuation is record 392 on P000654.

The catalogue names Krichever for record 391, but Shnirelman begins explicitly on P000651. The Laplacian, flat torus, positivity, Sturm, Courant and Arnold interventions are all on **P000651**; the spectral phases and return-map amplitudes are on P000652; the elliptic-function sketch and wave-trace continuation are on P000653. The item-level speaker field preserves this change without inventing an additional catalogue record. Buchstaber similarly intervenes on P000656 within record 393, before Novikov's new heading starts record 394. The chapter boundary follows record 396 on P000658.

The static-energy discussion in 386.9 attaches to **GP-1975-10**, shared with 1975-377.9 in the preceding block; the parent should merge that occurrence into the other block's problem object. It is not a new mass-gap problem. The quiver discussion is thematically related to GP-1972-301 and GP-1972-302, but no identical classification question is repeated in 388, so no fabricated recurrence is added. The wave-trace material revisits 1973-333.18–20. Lattice gauge variables revisit 1974-345.1–8. Serre's problem reuses **GP-1973-33** and includes its earlier occurrence 1973-322.1.

New problem IDs used are GP-1975-20 through GP-1975-26. IDs 27–29 remain unused. The normalization exercise has GP-1975-22 because it is a definite identifiable question, although its mathematical answer was already known. The broad quantum-gravity intervention is not assigned a manufactured definite problem ID.

## Scan inspection and decisions

The following decisive images were inspected directly; the same filenames are in `work/scans/`.

| Scan | Observation and editorial decision |
|---|---|
| P000644 | The upper discussion is still algebro-geometric. The Polyakov heading is unambiguous. The connection components are written as belonging to SU(2), followed by “Lie algebra”; anti-Hermitian trace-zero matrices fix the intended algebra. The positive bare trace action needs a sign convention. |
| P000645 | The factor one-half on the mixed electric/multiplier term and on the later Gauss term is visible. Direct Legendre transformation gives coefficient one on the multiplier term. The bracket convention is inconsistent with the displayed Hamilton equation; constraint preservation survives the sign change. |
| P000646 | The longitudinal equation changes commutator order. The consistent reconstruction uses total charge rho minus g[a,P], and M=-partial D. The missing coupling in the first perturbative correction is a mathematical omission in the source. |
| P000647 | The canonical commutator is schematic and omits i hbar and the transverse projector. The charge-kernel vacuum average and the “5 April continuation” line are clear. No rigorous vacuum construction appears. |
| P000648 | The generalized Poisson formula, parameter range, and normalization question are legible. The Roiter length-quantifier order is faithfully transcribed but is not the intended uniform upper bound; the modern correction is distinguished from a transcription error. |
| P000649 | The root divisibility criterion, star form, and Kirillov superanalysis material are present. The root statement is read in its finite/affine context, with positive q(x) supplied. The star with at least five arms is indefinite and does not automatically satisfy that criterion. |
| P000650 | The super-Poisson deformation question precedes Sinai's heading. The Ising row matrix, trace partition function and largest-eigenvalue discussion are distinct items. “Free energy” is used for dimensionless pressure. The anticommuting-matrix formula suppresses sector and scalar factors. |
| P000651 | The Shnirelman heading is explicit. Ground-state positivity, the polynomial analogy and the Sturm/Courant/Arnold material are on this page, not P000652–653. The sphere-average formula lacks the standard 2n factor. |
| P000652 | The poorly approximable-angle hypothesis is explicitly present. It is **not** an omitted hypothesis of the elliptic delta comb. Its analytical role is the polynomial small-divisor bound. The negative-real multiplier expression cannot have the same sinh denominator for odd and even iterates. The regularizing factor and mean subtraction are misplaced inside the delta argument. |
| P000653 | There is a double reciprocal-pole sum and an integral of a function called Weierstrass, together with a pole-lattice sketch. The imaginary period/scale and regularization are incomplete or overwritten. No unique exact identity is asserted. The later meromorphic-continuation statement is too strong: the standard local wave trace has logarithmic lower terms. |
| P000654 | A squared A with two indices appears in the action, but F is defined below. “Any character” is immediately glossed as a class function. The finite lattice has 4n link-group integrations and unreduced dimension 12n; this is not the dimension of the gauge quotient. |
| P000655 | The opening abbreviation is divergence-free, but the differential is Hamiltonian. These agree only in the plane. The Gelfand–Kalinin–Fuchs attribution, degrees7 and10, and memory-failure report are clear. K-prime is introduced before its Euler star is dropped. The tensor-product statement lacks the weight-zero exception. |
| P000656 | The general product row's middle t exponent is overwritten and resembles2; homogeneity requires ell. The terminal coefficient is visibly **10t^70**, and the lower bound is **57**. Buchstaber's heading and the subsequent Novikov heading are distinct. Lorentzian volume and stress-variation index positions require explicit correction. |
| P000657 | The nuclear estimate really reads **10^-23 cm**. Either the length exponent or the unit is wrong; the intended correction cannot be uniquely recovered. The point-mass delta equation is schematic. The Serre heading has “projective” inserted in a callout. |
| P000658 | The resultant-translation lemma is explicitly attributed to Suslin. The sentence “need c=1” omits unit-ideal patching. Novikov writes M-n despite a four-entry signature. The sound inequalities and Gödel's timelike-loop remark are legible. |

The CSV distinguishes mathematical emendations (`faithful_error`), ambiguous readings, and provenance corrections. Its content fields escape LaTeX special characters; enum and page fields remain unescaped schema values.

## Principal identifications and limits

**Gauge theory.** Arnowitt and Fickler (1962) and Schwinger (1962) were identified at publisher abstract level; their complete derivations were not read. Reinhardt et al. (2018), Section 2, equations (1)–(5), supplies a directly read modern canonical formula. Wilson (1974), Sections I–III, was read in the original paper. The Jaffe–Witten problem statement separates confinement from continuum existence and the mass gap. Finite Haar integrals and formal Wick rotation do not settle either continuum issue. The conventions in 386 are reconstructed consistently rather than silently copied from incompatible manuscript signs.

**Generalized Poisson law.** Consul and Jain (1973), Section 3, equation (3.1), is an exact prior match. The generating-function normalization proof is supplied and marked as such: Lagrange inversion yields exp(x0(T(z)-1)), and the derivative of exp(alpha(t-1))-t is strictly negative on [0,1] when 0<alpha<1. The source's unspecified biological attribution is not resolved by that mathematical match.

**Roiter.** The initial unsuccessful identification of the divisibility criterion was resolved through the parent's lead to Roiter (1978). This agent independently opened and read the original: condition (*) and its reflection invariance on p.202, Proposition 4 on p.205, and Lemma 6 on p.206. The finite/connected affine formulation is consequently **A**, with the 22 March 1976 notebook as an earlier recorded witness and Russian publication 1978/English translation1980. The indefinite generalization is not claimed. The Gabriel–Roiter chain and length-bound interpretation uses Ringel (2006), with the extracted power bound explicitly marked as our deduction.

**Supergeometry.** Berezin and Leites (1975) and Berezin and G. I. Kac (1970) were read directly. The latter's Section 3.5 Theorem 4 is a formal Lie correspondence, not triangularization for all solvable Lie superalgebras. The 64-dimensional algebra remains F: dimension and a particle comparison do not identify a unique superalgebra or representation. Bordemann (2000) answers an explicitly restricted even symplectic super-Poisson deformation problem, not every possible odd or degenerate reading of the note.

**Commuting operators and spectral geometry.** Krichever (1978), Theorem 2.3, is the exact generic higher-rank inverse construction; receipt was15 February 1977, and the introduction corrects the earlier implementation. Rank means the gcd of orders in the entire ring, not necessarily a selected pair. The asymptotic framing and r-1 functions cannot be omitted from the inverse data. For the spectral portion, Duistermaat–Guillemin (1975) was checked at publisher metadata level, while Zelditch's original wave-trace expansion was read. Zelditch's journal date is1998 and arXiv upload2000; the upload must not be called its prepublication circulation. Bérard–Helffer's Sturm paper circulated2017, was revised2018 and appeared in the2020 issue. The extended-Courant counterexample is a precise reconstruction of one possible Arnold question; the original broad Harnack wording has no exact bound.

**Hamiltonian cohomology.** Relative cohomology to sp2, full Hamiltonian fields including translations, and the vanishing-at-origin algebra ham2-zero are kept distinct. The missing Euler star and the zero-weight exception are mathematically decisive. The Gelfand–Kalinin–Fuchs class is older than the talk; the machine-memory failure is not a vanishing statement. Mikami (2016), Theorem 1.1 recalls the GKF factorization, while Theorem 1.2 proves the Metoki factorization. Stable-rank Morita–Sakasai–Suzuki computations do not solve the fixed-rank problem. The coefficient-infinitude statement is explicit in Mohammadzadeh–Fuchs (2014), Section 2; Mikami's infinitude question is weaker. Searches through 10 November 2026 located no later exact resolution; no claim of exhaustive nonexistence is made.

Perchik's 1975 thesis date is verified in Harvard's dissertation catalogue, which establishes earlier work but not an exact public-circulation date or a theorem locator in the dissertation. Item393.7 retains class E **provisionally**, with medium confidence and an explicit statement that exact pre-seminar circulation remains unestablished. The original 1976 article could not be retrieved; the mathematical formula was read in later primary restatements. Its bibliography entry is accordingly `unverified`, with this limitation explained. Kotschick–Morita (2009), Remark 9 labels a series containing negative weights by a superscript-zero algebra inconsistent with its own Section 5 construction; the distinction is resolved by the definitions and the translation factors.

The Mohammadzadeh–Fuchs table's extracted text at m86 reads -2204, while the parent's two exact algorithms give -22044 and agree at adjacent checkpoints. Neither agent obtained a usable image of the published table. This is logged as an **extracted-text discrepancy**, not as a printed-paper erratum. The notebook's 10t^70 is independently confirmed, not corrected. The notebook's57 is exactly the sum of absolute relative Euler coefficients from m=-1 through 35, including weight zero and the negative weight; the positive-weight subtotal is54.

**Buchstaber.** The expectation notation has a concrete partial match in Buchstaber (1975), Sections 3–4: the average over the branches of a two-valued formal group gives a linear coproduct. For actual compact groups, the continuous-function coproduct uses a completed tensor product. Adams–Liulevicius's1975 article is a bibliographical lead matching the heading; its full text was not read, and no theorem is attributed to it. The directly read mathematical source is Buchstaber's PartI.

**Relativity.** The source's +--- signature is retained, with one explicit stress-variation convention. The electromagnetic stress formula was independently checked in this convention. The Einstein–Hilbert variation uses compactly supported variations to control the boundary divergence. Fluid conservation is explicitly projected along and perpendicular to the unit velocity. Fourès-Bruhat (1958), Section 2, gives the constraint-propagation argument; Sections 9–12 give the perfect-fluid equations and acoustic cone. The1952 article's Introduction was read, but a later full-paper retrieval timed out. Kruskal's publisher abstract was read; the local radius saddle is independently derived from UV=(1-r/rs)exp(r/rs). It occurs at the bifurcation sphere, not at every horizon point. Gödel (1949), Sections 2–3, includes a cosmological constant and dust; omitting that term would misstate the example.

**Serre/Suslin.** Items395.1/.2/.3/.5/.6 are B, as near-contemporary work of others. Receipt and Academy presentation before 19 April 1976 do not prove public circulation before the meeting. The notebook itself records the oral transmission. Suslin's polynomial-ring conclusion is in Section III, Theorems 2–3; Theorem 1 is the more general almost-isomorphic-module result. Quillen's original proof was not read, but its metadata was checked. Monceur–Yengui (2017), Theorem 3.1 and Lemma 4.1, provide directly read exact resultant statements. The general-ring lemma is separated from the infinite-field hypothesis used by their streamlined algorithm. The reduction patches several resultants generating the unit ideal; it does not assume the first resultant equals one.

## Independent mathematical audits

The parent's `root_development.tex` and `root_spectral_development.tex` were independently reviewed. No mathematical error was found. One terminology change was suggested: Hamiltonians of **weight** ell have polynomial degree ell+2.

For Perchik's product, the maximum negative weight is two, so cutoff N+2 is sufficient. The Weyl projector extracts a0-a2 from a symmetric Laurent character. The parity rule, support bound |k|<=3n, logarithmic-derivative recurrence and descending-factor update are correct. Finite cochain dimensions justify Euler–Poincaré and the absolute-value Euler lower bound. The finite results do not imply eventual nonvanishing, infinitely many signs or explicit cocycle representatives.

For spectral phases, the Fourier normalization is correct. The circle has frequencies |k|/R and gives the atomic comb with coefficient2R. The inequality |exp(s+i theta)-1|>=exp(s)-1 provides a uniform Fourier bound; coefficient convergence therefore gives distributional convergence. On the sphere, the phase is -1+O(1/ell); after multiplicity weighting and Abel prefactor the accumulated error is O(1), giving the stated -1/(pi epsilon) divergence. The sphere is explicitly outside the generic hypotheses. The necessity direction of the Fourier criterion uses the stated boundedness of the family away from zero together with uniform boundedness on smooth test functions.

Our additional bounded reconstructions were checked directly: the Gabriel–Roiter filtration exponent, star-form square completion, determinant formulas for elliptic/positive/negative hyperbolic blocks, the geometric-series delta-comb coefficients, generalized-Poisson normalization, stress-index variation, fluid projections and the Kruskal radius expansion. These are marked `ours` or `oursComputed` where supplied in the occurrence index; no novelty claim is made.

## Final integration notes

The parent owns compilation, the complete chapter and the two development files. Do not create a duplicate GP-1975-10 object from this block; add occurrence 1975-386.9 to the shared confinement entry. The two root-owned bibliography entries must remain unique. The source ledger records exact URLs, DOI metadata, tool result identifiers and queries for both resolved and unresolved identification searches. Full proof access is never inferred merely from an abstract or publisher page.

The final structural audit passed required fields, enum values, consecutive occurrence IDs, item-level citation-key membership, bibliography-key uniqueness, problem-occurrence resolution and balanced mathematical delimiters. The spectral-phase statement and its problem entry explicitly define the nonnegative square-root Laplace eigenvalues with multiplicity on a closed compact Riemannian manifold. Repeated thin-space escapes from successive record saves were removed by making the authoring transformation idempotent. The parent reported successful full PDF compilation before these final local wording and spacing refinements.
