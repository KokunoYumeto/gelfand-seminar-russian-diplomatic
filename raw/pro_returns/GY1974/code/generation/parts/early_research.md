# Early-record research and verification log

Date of this audit: 9 November 2026. Status horizon: November 2026. Academic-year identifier:1974. Assigned catalogue records:331,332,334,335,336,337,338,339,340,341.

## Deliverable and counting scope

The item data enumerate distinct definitions, constructions, methods, claims and questions, including false or incomplete literal statements. The year heading334 has no mathematical item. Record332 has one F item because a mathematical subject is announced but no mathematical content follows. The current identifiers of331/332 are **five compatibility aliases for existing source occurrences**1973-331.1–4 and1973-332.1. They are not new meetings or newly dated mathematical occurrences. The catalogue date1975-03-25 is deliberately preserved in the machine fields, while the scan reads25/III-74. Root independently opened the MCCME all-links catalogue and confirmed that it too says25March1975. The individual record pages were not retrievable. Therefore source chronology is inconsistent, rather than silently repaired.

P000550 continues the prior KdV discussion; P000552 starts a separately dated1/IV-74 talk by Yura Koblenz, with Gelfand and Shnirelman interventions, continued on P000553. Their26 prior-index rows are audited below and in early_boundary.json/.tex/.md. They are **not** assigned to current records331/332, and no current record333 is manufactured.

Every assigned page-sharing boundary was inspected. P000554 contains the year heading, Giusti introduction and the start of Novikov/Dubrovin algebraic material. P000556 contains the end of that material, Bessaga's topology discussion and the beginning of Giusti's mean-curvature discussion. P000558 ends Giusti and begins Dubrovin. P000564 contains dilogarithms belonging to342 above Giusti's heading; this agent indexes only the latter part, continued on565. The sibling owns342. The actual content boundaries, rather than the broad overlapping catalogue ranges, are used in the talk summaries.

## Source use and method

The Russian transcription is the authority, checked against the manuscript scans. English wording was compared where signs, quantifiers or mathematical terminology could change the claim. ScansP000550–P000565 were viewed, with special attention to the quartic coefficient and spectral quintic on555, pseudo-boundary on556, catenoid diagrams and cube-root example on557, BV formulas on558, Floquet plots on559–560, Riccati/monodromy formulas on561–563, and the coefficient tensor on565. Reduced PNGs under early_code/scan_previews are inspection copies only; the original scans were not altered.

The distinction between literal correctness, modern reconstruction, publication match and verification is retained in each item. Original papers were preferred. When only an author's later review or publisher metadata could verify a claim, that limitation is explicit. “Verified” in BibTeX means that the source URL was opened, not that every theorem in that work was read. The record-level verification field specifies what was actually established. Bibliographic entries reused cumulative keys; the current verificationrecord fields supplement earlier-year annotations.

## Chronology decisions

- Novikov's periodic-problem paper was received18February1974 and the publisher gives publicationJuly1974. Its Theorem2.1 proves stationary higher-KdV solutions are finite-gap and completely integrable; its p64 gives the genus-two Hamiltonian/spectral computation. These are E in September, including336.6,336.10 and340.23.
- Dubrovin–Novikov's Doklady note was received3June1974 and published in volume219(3),1974. Section2 expressly attributes the stationary-to-finite-gap direction to Novikov; section3 gives the converse and divisor description. The later JETP paper was submitted5July1974 and the Russian issue isDecember1974; its English printing bears1975copyright. The1974 key follows the journal's volume convention. General converse/divisor/Jacobian claims are A, with the source scope retained.
- The DMN survey was received2June1975 and published1976. It is used for precise theorem comparison and coordinates, not to imply that all its material was first discovered in1976.
- Gurevich–Pitaevskii was submitted3April1973, Russian publicationAugust1973, English translationFebruary1974. It is only a thematic comparator for the notebook's heading: the catalogue saysB.M.Gurevich, whereas the paper's author isA.V.Gurevich.
- Giusti–Miranda's analytic-coefficient singular example and variational example date from1968. Their exact original article was not retrieved. Mingione's equation3.3 reproduces the tensor with4/(n−2) in both factors; this indirect historical source and the independent analytic proof support the repair. They do not support the notebook's uniqueness sign.
- Classical partial regularity is not backdated from a modern survey. The precise strict dimension estimate is checked in DeFilippis–Mingione–Nowak's2025preprint, revised8July2026, introductioneqs1.1–1.2, which explicitly recalls the1968local theory.
- The near-flat two-torus theorem on adjacentP553 was received by the Moscow Mathematical Society7May1974 and published1975, after the1April1974meeting. Both primary pages were read. Its quantifier is everyk>1; Lazutkin's positive-density subsequence is explicitly described as an earlier weaker result.

## Search log and primary-source traversal

Earlier targeted lookups followed the names and formulas in the scans: finite-gap periodicity and hyperelliptic Jacobians; Giusti–Miranda analytic tensors and partial regularity; Giusti prescribed mean curvature/BV boundary relaxation; Bessaga/Anderson Z-sets and Frechet classification; Gelfand–Fuchs ray quotient; Kirillov/Fock and principal-bundle automorphisms. Primary records and full texts were then opened, and relevant sections read as listed below. Search-engine summaries alone were not promoted to exact theorem matches.

Explicit final verification queries (9November2026) were:

1. `Gelfand Giusti Hironaka resolution singularities elliptic equations 1974` — returned Hironaka algebraic-resolution material and elliptic regularity literature, no primary formulation of the notebook's proposed analogue. No precise problem was manufactured.
2. `Giusti Miranda 1968 x/|x| uniqueness Dirichlet problem analytic elliptic systems` — returned the known existence examples and reviews, not an exact uniqueness theorem for the repaired homogeneous system.
3. `Koblenz heat kernel fourth coefficient Laplace 1974 asymptotic` — no identified primary independent fourth-coefficient publication. Sakai1971 and Gilkey's attribution were checked separately.
4. `"Duistermaat" "Hörmander" "6.1.1" Fourier integral operators II pdf` — recovered the exact theorem statement from the indexed primary PDF after direct pinpoint fetches timed out. The full article itself had opened successfully.
5. `"Giusti" "Miranda" "Un esempio" "1968" pdf` and `"Un esempio di soluzioni discontinue" bdim` — located repeated references and later discussions but not an accessible original1968article. Some secondary bibliographies disagree on pagination; no invented original-source verification was added.

The following table records the opened sources and usable web reference IDs. IDs are research trace tokens, not citations to be printed in the companion; the final text uses the BibTeX keys and pinpoint locators. A root agent citing a child web result in chat must reopen it itself.

| Bib key | Opened primary/source URL | What was actually checked | Retrieval IDs |
|---|---|---|---|
| novikov1974periodic | https://www.mathnet.ru/eng/faa2358 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2358&what=fullt ; https://link.springer.com/article/10.1007/BF01075697 | Full original§§1–2, Thm2.1, eqs18–19; received date; publisherJuly1974 | turn117view0,turn118view0,turn120view0,turn139view0 |
| dubrovinnovikov1974periodicity | https://people.sissa.it/~dubrovin/Papers/1974/dubrovin_novikov_1974_dan.pdf | Full author-hosted English text,§§2–4; chronology, converse, Hamiltonian; transcription defects retained | turn13view0,turn41view0,turn57view0 |
| dubrovinnovikov1974periodic | https://www.jetp.ras.ru/cgi-bin/dn/e_040_06_1058.pdf | Full primary text, Bloch/divisor construction and dates | turn13view1,turn117view3 |
| dubrovinmatveevnovikov1976nonlinear | https://www.mathnet.ru/eng/rm3642 ; https://people.sissa.it/~dubrovin/Papers/1976/dubrovin_matveev_novikov_1976.pdf | Metadata; English ChII§§1–4, pp72–106; coordinate relationp105 | turn2view0,turn2view1,turn88view0 |
| gurevichpitaevskii1974shock | https://www.jetp.ras.ru/cgi-bin/dn/e_038_02_0291.pdf | §1 and author/date; thematic only for heading332 | turn50view1 |
| araki1970factorizable | https://ems.press/content/serial-article-files/41656 | §4pp370–373 exponential Hilbert space; received/revised dates | turn50view0,turn51view5 |
| vershikgelfandgraev1975diffeomorphisms | https://www.mathnet.ru/eng/rm4288 | Metadata and abstract; received15May1975; no unrecorded Kirillov theorem inferred | turn28view4 |
| wockel2007symmetry | https://arxiv.org/abs/math/0612522 | Abstract and stated automorphism extension; preprintDecember2006, publication2007 | turn28view3 |
| gelfandfuchs1967topology | https://www.mathnet.ru/eng/faa2842 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2842&what=fullt | Original introductionp34: quotient is Hausdorff, nonregular, all continuous real functions constant | turn15view3,turn28view5,turn41view1 |
| anderson1967special | https://dml.cz/manakin/bitstream/handle/10338.dmlcz/700850/Toposym_02-1966-1_9.pdf | p31infinite-dimensional Frechet classification; Thm4/Cor4pp37–38 | turn31view1,turn73view0,turn73view1 |
| andersonchapman1971extending | https://msp.org/pjm/1971/38-2/pjm-v38-n2-p01-p.pdf | Introductionp281 Z-set unknotting; Thm6.1; finalp293 and received1June1970 | turn13view2,turn73view2,turn117view1,turn119view1 |
| giusti1976boundary | https://www.numdam.org/article/ASNSP_1976_4_3_3_501_0.pdf | Introduction and§1 BV area, perimeter condition, relaxed boundary data; received/revised1976 | turn2view2,turn117view2 |
| giusti1969partial | https://www.numdam.org/article/ASNSP_1969_3_23_1_115_0.pdf | Original arbitrary-order paper opened; formula OCR insufficient for exact higher-order dimension comparison | turn15view0 |
| mingione2006regularity | https://dml.cz/bitstream/handle/10338.dmlcz/134645/AplMat_51-2006-4_4.pdf | §3.2eqs3.3–3.5 tensor and variational example; Thm4.1; indirect verification of1968original | turn31view0,turn51view2,turn51view3 |
| giusti1982basic | https://dml.cz/bitstream/handle/10338.dmlcz/702271/Equadiff_05-1982-1_26.pdf | pp111–113 growth assumptions, minimizers versus stationary points | turn50view3,turn51view0 |
| milne1986jacobian | https://www.jmilne.org/math/xnotes/JVs.pdf | §2analytic Jacobian; Thm5.1 Abel birational map and exceptional linear-system fibres | turn50view2,turn57view1 |
| milne2008abelian | https://www.jmilne.org/math/CourseNotes/AV.pdf | ChI§2 Lemma2.4, Thm2.8 Riemann forms/projectivity;§18Jacobians | turn61view0,turn118view2,turn118view3 |
| johnstara1990regularity | https://dml.cz/bitstream/handle/10338.dmlcz/702382/Equadiff_07-1990-1_5.pdf | pp28–30 energy-class scalar/two-dimensional alternatives | turn90view0 |
| frehse2007irregular | https://webdoc.sub.gwdg.de/ebook/serien/e/sfb611/343.pdf | Thm3.1complex scalar equation with measurable spatial coefficients; not exact analyticA(u) match | turn95view2 |
| defilippismingionenowak2026partial | https://arxiv.org/abs/2501.08405 ; https://arxiv.org/pdf/2501.08405 | Revised8July2026; introeqs1.1–1.2 exact classical local partial-regularity hypotheses | turn91view1,turn92view0 |
| shabat1973kdv | https://www.mathnet.ru/eng/dan37878 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=37878&what=fullt | Full4pages; cubic evolutioneqs13,18; dates; hypotheses retained | turn129view1,turn131view1 |
| shabat2014interpolation | https://www.mathnet.ru/eng/tmf8662 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=tmf&option_lang=eng&paperid=8662&what=fullt | p305explicit1974seminar link;§3Thm1 nondegeneracy/normalization; Wronskian constant | turn125view1,turn126view1,turn127view2,turn129view2 |
| mckeansinger1967curvature | https://www.mathnet.ru/eng/mat535 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=mat&option_lang=eng&paperid=535&what=fullt | Original1967metadata plus1969Russian translation;§1/§7heat coefficients, sign conventions; scan extraction imperfect | turn125view2,turn126view2,turn129view0,turn135view1 |
| gilkey1979recursion | https://www.numdam.org/article/CM_1979__38_2_201_0.pdf | Intro attribution to Sakai; local invariants, contractions, off-diagonal decay | turn124view2 |
| sakai1971eigenvalues | https://www.jstage.jst.go.jp/browse/tmj/23/4/_contents/-char/en | Publisher issue title,1971,pp589–603,doi10.2748/tmj/1178242547; full formula not read | turn125view3,turn126view3 |
| balianbloch1972oscillations | https://www.sciencedirect.com/science/article/pii/0003491672900061 | Direct fetch403; exact formula unverified. Bibliography explicitly saysunverified; historical link confirmed in Colin de Verdière's introduction | turn128view0(failure) |
| colindeverdiere1973geodesicsii | https://www.numdam.org/article/CM_1973__27_2_159_0.pdf | Introduction, nondegenerate critical-manifold conditions and main-result scope; closed manifold distinct from billiards | turn128view1 |
| duistermaathormander1972fourierii | https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6131-11511_2006_Article_BF02392165.pdf ; https://link.springer.com/article/10.1007/BF02392165 | Full primary opened; theorem6.1.1 recovered from indexed primary; pinpoint fetches timed out; metadataJuly1972 | turn128view2,turn137view0,turn138search12 |
| duistermaatguillemin1975spectrum | https://link.springer.com/article/10.1007/BF01405172 | Publisher metadata only: received20October1974,publishedFebruary1975; no exact billiard formula asserted | turn128view3 |
| shnirelman1975multiplicity | https://www.mathnet.ru/eng/rm4279 ; https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=4279&what=fullt | Both originalpages265–266, every-index theorem and three lemmas; received7May1974 | turn125view0,turn126view0,turn127view0,turn131view0 |

The primary Giusti–Miranda1968article, an exact uniqueness theorem, the higher-order dimension statement under the shorthand hypotheses, Koblenz's independent calculation, and the catalogue's individual record pages remain unverified. Failed direct Math-Net links sometimes succeeded when reached by the metadata-page PDF link; both outcomes are distinguished in the traversal log.

## Mathematical areas and cross-year connections

| Area | Current coverage | Prior/cumulative connection and consequence |
|---|---|---|
| Infinite-dimensional group representations |331.1–4;332heading | Five source duplicates from1973; Fock conventions are classical, current-group classification is not supplied |
| Algebraic geometry and integrable systems |336.1–15;339.1–4;340.1–24 | Novikov's earlier1973-326line; GP-1973-50band monotonicity and GP-1973-51supplementary inverse data reused; middle'sGP-1974-10finite-gap characterization linked |
| Infinite-dimensional topology |337.1–7 | Ray quotient repeats1967-132.7; newGP-1974-01is settled by Gelfand–Fuchs1967; pseudo-boundary is sigma-Z, not closedZ |
| Elliptic systems and regularity |335.1–4;341.1–11 |1968counterexamples and partial regularity explain the1974discussion; broad variational questionGP-1974-02was already answered |
| Geometric PDE and BV |335.5;338.1–13 | Mean-curvature size restrictions, catenoid obstruction, weak limits, relaxed boundary values; definitions and classical methods distinct from later refined existence theorems |
| Adjacent inverse scattering |prior1973-330.6–11 |1973scattering evolution and2014explicit retrospective interpolation theorem; no current-year reassignment |
| Adjacent spectral geometry/microlocal analysis |prior1973-333.1–20 |1967heat coefficients,1971Sakai,1973geodesic trace,1975Shnirelman every-index theorem; wave/heat conventions separated |

## Candidate triage: no eligible new C/D question

No mathematically definite unresolved C or D item survived the formulation and literature check in these assigned records. This is not a claim that the surrounding fields have no open questions.

- The question about continuous functions on the ray quotient is already answered: every continuous real-valued function is constant. The space is Hausdorff but nonregular; calling it non-Hausdorff would be another error.
- The finite-gap/stationary characterization is established; its two directions have different1974publication histories. The sibling owns its definitive problem entryGP-1974-10.
- The broad question about discontinuous variational minimizers was answered in1968. It is not sharpened without evidence to the later autonomous-integrand problem.
- “Describe all algebraic tori” lacks a choice of polarization, equivalence or moduli problem. The almost-periodic completeness question lacks a function class and spectral transform. “Maximal sigma-Z” lacks the absorption/universality notion; literal inclusion maximality is wrong. These remain F rather than being inflated into open problems.
- The n=3,N=2claim lacks coefficient and lower-order-term hypotheses; the Frehse2007example is deliberately only a partial match. The uniqueness sign and higher-order dimension bound are unverified source assertions, not automatically open mathematical questions.
- Gelfand's Hironaka analogy does not specify the class of equations, allowable modifications or object to resolve. Archival clarification would be useful; a new theorem answering an invented interpretation would not resolve the historical question.
- The adjacent twin-gap and three-torus remarks also lack quantifiers/classes. The precise two-torus theorem was found and checked, so it is not listed as open.

Consequently the deep-work contribution here is an explicit verification audit, not a purported original solution to an open problem. Any further bounded project should begin by selecting and documenting additional hypotheses; this packet does not authorize attributing them to the seminar.

## Formula audits and independent review

`early_audit.tex` contains full proofs of the Giusti residual and a uniformly elliptic reconstruction, with n=N>=3, the unit ball, the energy class, trace, weak first derivatives and the vanishing inner flux O(epsilon^(n−2)). It asserts existence only. It also factors the exact Poisson bracket and computes the spectral quintic conditionally on u=q1, canonical Hamiltonian time and the stated divisor polynomial. The coefficient5/2→5/8 is supported by the source and algebra; the spectral c²coefficient and constant-term sign remain a normalization discrepancy rather than a recovered manuscript reading.

`early_code/exact_checks.py` uses only Python's standard library. Sparse polynomial operations over Fractions check the Poisson bracket, conservation, squared-eigenfunction identity and third-order equation in independent indeterminates. A separate rational first-derivative jet implementation evaluates the unsimplified tensor flux in dimensions3–6. Output is `early_code/exact_checks.json`. These finite jet checks supplement the analytic proof; no numerical sample is offered as a theorem proof. All own proofs/computations are marked ours/oursComputed in TeX and explicitly disclaim novelty.

Root independently reviewed the entire early audit and confirmed the residual, ellipticity, weak flux and both Hamiltonian identities against a separate derivation. Root requested an explicit O(epsilon^(n−1)) boundary estimate for identifying weak first derivatives of the bounded radial map; that sentence was added.

This agent independently reviewed `root_audit.tex` and `middle_audit.tex` and found no proof error. The Riccati and product/Wronskian signs, common-factor invariance, nonconstant example, Rogers-dilogarithm transformations, golden-ratio substitutions, normalized planar U(1) integration and SU(2) Bessel factor were checked. Both root and middle scripts were rerun without modifying them; outputs matched their saved files. The numerical series tail bound is correctly distinguished from decimal rounding, and the quadrature is only a check rather than an exact proof.

## Data validation

The builder saves incrementally after each item. Consecutive record-local IDs, valid enum fields, citation-key availability, reciprocal current problem links and absence of hidden control characters were checked. The five source duplicates are retained in raw counts and removed only in the distinct-source count. The root performs the shared-kit schema/build/XeLaTeX validation after merging; this agent does not modify the kit or root outputs.

Current checkpoint: 10talks/heading records; 84raw items, 79after removing the five exact source aliases; 41correction rows; 4problem entries owned here (two new settled IDs and two reused IDs). Classes: A=14, B=0, C=0, D=0, E=59, F=11. Middle-owned GP-1974-10 is linked from340.7 but not duplicated in this agent’s problem file.

## Item-by-item coverage ledger

| Occurrence | Page(s) | Class | Kind | Title |
|---|---|---|---|---|
|1974-331.1|P000551|F|remark|Representation programme for diffeomorphism and current groups|
|1974-331.2|P000551|E|construction|Automorphisms of a principal bundle and the gauge extension|
|1974-331.3|P000551|E|construction|Symmetric Fock space|
|1974-331.4|P000551|E|definition|Exponential vectors and factorial normalization|
|1974-332.1|P000551|F|remark|An unrecorded account of Whitham’s method for KdV|
|1974-335.1|P000554|E|theorem|Scalar Hölder regularity for measurable uniformly elliptic coefficients|
|1974-335.2|P000554|E|claim|Using linear theory in scalar nonlinear regularity|
|1974-335.3|P000554|E|claim|Failure of scalar regularity for elliptic systems|
|1974-335.4|P000554|E|theorem|Partial regularity and the dimension of the singular set|
|1974-335.5|P000554|E|definition|Mean curvature of a graph and a size obstruction|
|1974-336.1|P000554|E|definition|Complex tori and algebraic tori|
|1974-336.2|P000554|F|question|The unspecified problem of describing all tori|
|1974-336.3|P000554|E|construction|Hyperelliptic curves and their holomorphic differentials|
|1974-336.4|P000554|E|construction|The Jacobian and the missing Hodge quotient|
|1974-336.5|P000554|E|construction|Period matrices and the moduli diagram|
|1974-336.6|P000555|E|construction|A genus-two polynomial Hamiltonian pair and its corrected quartic coefficient|
|1974-336.7|P000555|E|claim|Commuting Hamiltonian vector fields|
|1974-336.8|P000555|A|theorem|Common levels as open parts of abelian varieties|
|1974-336.9|P000555|A|theorem|Rational parametrization of the marked universal hyperelliptic Jacobian|
|1974-336.10|P000555|E|construction|The spectral quintic and a parameter-normalization discrepancy|
|1974-336.11|P000555|E|construction|Abel’s map from a symmetric power|
|1974-336.12|P000555|E|definition|Normalized Bloch solutions and the unit multiplier condition|
|1974-336.13|P000555|F|remark|The almost-periodic completeness warning|
|1974-336.14|P000555|E|construction|The two-sheeted spectral surface and its genus|
|1974-336.15|P000556|A|theorem|The finite-gap isospectral family and its Jacobian|
|1974-337.1|P000556|E|definition|Z-sets defined by approximation of Hilbert-cube maps|
|1974-337.2|P000556|E|claim|The pseudoboundary of the Hilbert cube|
|1974-337.3|P000556|E|theorem|Z-set unknotting in the Hilbert cube|
|1974-337.4|P000556|E|definition|Countable unions of Z-sets|
|1974-337.5|P000556|F|claim|The ambiguous maximal sigma-Z-set assertion|
|1974-337.6|P000556|E|claim|Every continuous real function on the ray space is constant|
|1974-337.7|P000556|E|theorem|Homeomorphism type of infinite-dimensional separable Fréchet spaces|
|1974-338.1|P000556|E|problem|The prescribed-mean-curvature Dirichlet equation|
|1974-338.2|P000556-P000557|E|construction|A radial annulus and the maximal catenoid height|
|1974-338.3|P000557|F|remark|Soap-film diagrams as a geometric illustration|
|1974-338.4|P000557|E|construction|A continuous prescribed curvature with an infinite-slope solution|
|1974-338.5|P000557|E|claim|Raising one endpoint beyond the possible flux|
|1974-338.6|P000557|E|method|The area-plus-potential functional and its Euler equation|
|1974-338.7|P000557|E|question|Removing the gradient cutoff in variational minimization|
|1974-338.8|P000557|E|claim|A necessary flux-perimeter inequality|
|1974-338.9|P000558|E|definition|Bounded variation and the dual definition of total variation|
|1974-338.10|P000558|E|definition|Relaxed area for a BV graph|
|1974-338.11|P000558|E|theorem|Lower semicontinuity of BV area|
|1974-338.12|P000558|E|theorem|Compactness of bounded BV sets|
|1974-338.13|P000558|E|construction|Boundary mismatch in the relaxed Dirichlet functional|
|1974-339.1|P000558|A|construction|The finite-gap hyperelliptic spectral curve|
|1974-339.2|P000558|A|theorem|Meromorphic continuation of the normalized Bloch solution|
|1974-339.3|P000558|A|claim|Pole and zero divisors of degree N with possible cancellation|
|1974-339.4|P000558|A|claim|One divisor point on each real gap oval|
|1974-340.1|P000559|E|definition|Periodic Schrödinger bands and finite-gap potentials|
|1974-340.2|P000559|E|construction|Unimodular monodromy and its characteristic equation|
|1974-340.3|P000559-P000560|E|theorem|The bounded-solution and discriminant criterion for the spectrum|
|1974-340.4|P000560|E|definition|Quasimomentum and the Bloch multiplier|
|1974-340.5|P000560|E|claim|Base-point independence of the discriminant|
|1974-340.6|P000560|A|theorem|Bloch continuation to the finite-gap curve|
|1974-340.7|P000560|A|theorem|Finite-gap potentials are stationary for a higher KdV equation|
|1974-340.8|P000560|A|theorem|The Jacobian description of the isospectral manifold|
|1974-340.9|P000560|A|claim|Higher KdV flows on the isospectral Jacobian|
|1974-340.10|P000560|E|claim|Monotonicity of a chosen band phase|
|1974-340.11|P000560|F|remark|The physical trapping and exponential-decay shorthand|
|1974-340.12|P000560-P000561|E|claim|Extrema of the discriminant and the sign of the lower bound|
|1974-340.13|P000561-P000562|E|claim|Open band edges, closed gaps and monodromy Jordan form|
|1974-340.14|P000561|E|construction|The normalization-independent Riccati variable|
|1974-340.15|P000561|E|claim|Amplitude, phase and the real part of the Riccati variable|
|1974-340.16|P000561-P000563|E|method|The high-energy Riccati expansion and local differential polynomials|
|1974-340.17|P000561|E|claim|The monodromy formula and the missing subtraction|
|1974-340.18|P000562|E|claim|The Wronskian normalization at the base point|
|1974-340.19|P000562|A|construction|Cancelling the closed-gap entire factor|
|1974-340.20|P000562|A|claim|Why the reduced entire function is a polynomial|
|1974-340.21|P000562|A|construction|The polynomial representation of the Riccati variable|
|1974-340.22|P000562|E|claim|The leading power of the spectral square root|
|1974-340.23|P000562-P000563|E|construction|Conserved Riccati integrals and the stationary variational equation|
|1974-340.24|P000563|E|claim|The derivative order of the Riccati densities|
|1974-341.1|P000564-P000565|E|definition|The energy weak formulation of a quasilinear system|
|1974-341.2|P000564-P000565|E|definition|Strong ellipticity and the distinction from coefficient smoothness|
|1974-341.3|P000565|E|definition|The Sobolev energy space and zero trace|
|1974-341.4|P000565|E|theorem|Scalar or two-dimensional regularity in the energy class|
|1974-341.5|P000565|E|construction|The Giusti coefficient tensor and the singular radial solution|
|1974-341.6|P000565|F|claim|A three-variable, two-component counterexample without a specified system|
|1974-341.7|P000565|F|claim|The unverified uniqueness assertion for singular Dirichlet data|
|1974-341.8|P000565|E|theorem|A relatively closed singular set of dimension strictly below n minus two|
|1974-341.9|P000565|F|claim|The compressed higher-order partial-regularity bound|
|1974-341.10|P000565|E|question|Variational problems with nonregular minimizers|
|1974-341.11|P000565|F|question|Gelfand’s proposed analogue of resolution of singularities|

## Boundary audit: P000550 and P000552–P000553

These are 26 prior-index audit rows, not new current-year record assignments. All three scans were inspected in full, including overwritten formulas and the returning-loop diagram. P000552 explicitly dates the Koblenz talk 1 April 1974. The catalogue ranges overlap; P000551 alone holds the five331/332 source items. Status: November2026.

### 1973-330.6 — Polynomial-exponential solutions and Bargmann potentials

Page: P000550. Classification: E. Verification: read the result.

The notes assert that arbitrary interpolation parameters produce a fundamental pair \(P(x,\zeta)e^{i\zeta x}\), \(Q(x,\zeta)e^{-i\zeta x}\) for a Sturm--Liouville equation with a Bargmann potential. A valid reflectionless construction requires admissible scattering data and a nonsingular interpolation system; an arbitrary complex choice need not give a real nonsingular potential, nor a fundamental pair at the Wronskian zeros.

The construction belongs to established reflectionless inverse scattering. \citet[\S3, Theorem~1]{shabat2014interpolation} gives a precise interpolation theorem and explicitly recalls the 1974 Gelfand discussion on p.~305. Its general equation may have spectral-parameter-dependent potential; the real Bargmann specialization needs further conditions. This is a partial match, not validation of “arbitrary”.

Bib keys: shabat2014interpolation, shabat1973kdv.

### 1973-330.7 — The interpolation problem and its missing normalization

Page: P000550. Classification: F. Verification: read the result.

The recorded conditions are \(P/Q=c_j e^{2i\zeta_jx}\) at finitely many nodes and \(P/Q\to1\) at infinity. The node count is overwritten as \(2n\,?\,1\); the degrees, admissibility, and rank condition are absent. Therefore the literal system does not determine a general existence or uniqueness theorem.

\citet[\S3, equations (44)--(49), Theorem~1]{shabat2014interpolation} specifies degrees \(m,n\), \(m+n+1\) nodes, normalization of the product of leading coefficients, and nondegeneracy. Its conventions do not identify the overwritten count or repair the notebook automatically. No open problem is extracted from this incomplete formulation.

Bib keys: shabat2014interpolation.

### 1973-330.8 — The polynomial Wronskian and the absent leading factor

Page: P000550. Classification: E. Verification: read the result.

The notes write \(P_xQ-Q_xP-2i\zeta PQ=\prod_j(\zeta-\zeta_j)\). Differentiating the interpolation equations does give zeros of the left side at the nodes. But if \(P,Q\) have degrees \(m,n\) and leading product \(pq\), its leading coefficient is \(-2ipq\), not automatically one. Its negative exponential sign is consistent with \(Pe^{-i\zeta x},Qe^{i\zeta x}\), opposite to the earlier displayed pair.

\citet[Theorem~1, equation (50)]{shabat2014interpolation} proves the corresponding Wronskian factorization with an explicit leading constant \(-2\) in its real spectral convention. The degree, normalization and exponential signs must be chosen consistently. This is a mathematical normalization audit, not a confident reconstruction of the overwritten spectral letters.

Bib keys: shabat2014interpolation.

### 1973-330.9 — Cubic time evolution of the interpolation data

Page: P000550. Classification: E. Verification: read the result.

The source evolves \(c_j(t)=c_j(0)e^{2i\zeta_j^3t}\). The structural assertion is that the scattering or interpolation coefficients evolve exponentially with a cubic spectral exponent under a KdV flow. The numerical factor and sign depend on the scaling of time, the Schrödinger operator and the chosen scattering functions.

\citet[equations (13), (18)]{shabat1973kdv} obtains linear cubic evolution of the scattering kernel; the paper was received 13 December 1972, presented 18 December 1972, and published in 1973. The cubic law is known before the source discussion; the notebook coefficient is not claimed to match another convention without conversion.

Bib keys: shabat1973kdv.

### 1973-330.10 — The incomplete third-order auxiliary equation

Page: P000550. Classification: F. Verification: read the result.

The line reads \((4\partial_t+\partial_x^3-3q\partial_x)P=(\ )Q=0\). The second parenthesis is empty, and acting on polynomial factors after removing exponentials shifts every \(\partial_x\) to \(\partial_x\pm i\zeta\). A full Lax auxiliary equation also depends on its zeroth-order term and the normalization of the eigenfunctions.

The cubic auxiliary-operator mechanism is established in \citet{shabat1973kdv} and in \citet[\S2, equation (33)]{shabat2014interpolation}. Neither supplies an exact missing notebook operator under the unresolved conventions. This remains an incomplete formula, not an open mathematical problem.

Bib keys: shabat1973kdv, shabat2014interpolation.

### 1973-330.11 — Logarithmic derivatives, the spectral shift and the Miura sign

Page: P000550. Classification: E. Verification: read the result.

For \(-y_{xx}+Vy=\zeta^2y\), the logarithmic derivative \(f=y_x/y\) satisfies \(f_x+f^2=V-\zeta^2\), away from zeros. The notebook omits this shift and pairs \(4f_t+f_{xxx}+3(f^2+\zeta^2)f_x=0\) with a plus-sign KdV equation for \(f_x+f^2\). These coefficients do not form the standard Miura identity. One consistent convention is \[4V_t+V_{xxx}-6VV_x=(\partial_x+2f)\bigl(4f_t+f_{xxx}-6(f^2+\zeta^2)f_x\bigr),\quad V=f_x+f^2+\zeta^2.\]

The Riccati and factorization mechanism is classical; compare \citet[equations (2), (18)]{shabat2014interpolation}. The displayed identity is an editorial direct algebraic check \oursComputed, offered as a consistent convention rather than a palaeographic emendation of every sign on the page.

Bib keys: shabat2014interpolation.

### 1973-333.1 — The sign of the Laplace--Beltrami operator

Page: P000552. Classification: E. Verification: read the result.

On a closed smooth Riemannian manifold, the coordinate expression \(|g|^{-1/2}\partial_i(|g|^{1/2}g^{ij}\partial_j)\) is nonpositive on functions. To retain the written nonnegative eigenvalues \(\lambda_j\) and heat trace \(\sum e^{-t\lambda_j}\), define \(L=-\operatorname{div}\nabla\ge0\). The scan has heavy cancellation before the coordinate expression; an intended minus cannot be read confidently.

The sign convention and spectral expansion are standard. \citet[\S1]{mckeansinger1967curvature} uses a nonpositive Laplacian and correspondingly opposite heat-exponential sign; the mathematical correction is convention consistency, not an invented visible glyph.

Bib keys: mckeansinger1967curvature.

### 1973-333.2 — Heat-kernel expansion and trace

Page: P000552. Classification: E. Verification: read the result.

For a real orthonormal eigenbasis of \(L\ge0\), \(K(t,x,y)=\sum_j e^{-t\lambda_j}\varphi_j(x)\varphi_j(y)\) and \(\operatorname{Tr}(e^{-tL})=\int_MK(t,x,x)dV\), for \(t>0\). A complex orthonormal basis requires conjugation in the second factor.

This is established spectral theory for a smooth compact manifold; \citet[\S1 and heat-kernel construction]{mckeansinger1967curvature} and \citet[introduction]{gilkey1979recursion} state the same framework. No novelty or extra assertion about termwise convergence at \(t=0\) is intended.

Bib keys: mckeansinger1967curvature, gilkey1979recursion.

### 1973-333.3 — The small-time heat-trace expansion

Page: P000552. Classification: E. Verification: read the result.

For a closed smooth \(n\)-manifold, \(\operatorname{Tr}(e^{-tL})\sim(4\pi t)^{-n/2}\sum_{j\ge0}a_jt^j\) as \(t\downarrow0\), with \(a_0=\operatorname{vol}M\). This is an asymptotic expansion to each finite order, not an asserted convergent series. Complex-time versions require sectors inside \(\operatorname{Re}t>0\).

The notes attribute the expansion to Minakshisundaram (1949). The established result and its local-invariant interpretation are checked through \citet[introduction]{gilkey1979recursion}; \citet{mckeansinger1967curvature} predates the talk. These later explanatory sources are not used to change the historical priority.

Bib keys: mckeansinger1967curvature, gilkey1979recursion.

### 1973-333.4 — Curvature contractions

Page: P000552. Classification: E. Verification: read the result.

With a fixed curvature-sign convention, \(\operatorname{Ric}\) is a metric contraction of \(\operatorname{Rm}\), and \(\operatorname{Scal}=g^{ij}\operatorname{Ric}_{ij}\). Norms mean full metric contractions; \(|\operatorname{Rm}|^2=\sum R_{ijkl}^2\) holds in an orthonormal frame at the point. Several indices in the scan are overwritten and cannot be recovered uniquely.

These are standard tensor definitions. \citet[\S7]{mckeansinger1967curvature} and \citet[\S1]{gilkey1979recursion} provide the invariant contraction framework. The coordinate-free reconstruction avoids inventing unreadable indices.

Bib keys: mckeansinger1967curvature, gilkey1979recursion.

### 1973-333.5 — The integrated scalar-curvature coefficient

Page: P000552. Classification: E. Verification: read the result.

For the scalar nonnegative Laplacian on a smooth closed manifold, with the usual geometric scalar-curvature convention, \(a_1=\frac16\int_M\operatorname{Scal}\,dV\). It is an integrated coefficient, not the pointwise heat coefficient itself.

The formula is established before the talk; \citet[\S1, equation (5a), and \S4]{mckeansinger1967curvature} computes the scalar-curvature term. Sign conventions must be translated consistently with the Laplacian and curvature tensor.

Bib keys: mckeansinger1967curvature.

### 1973-333.6 — The quadratic integrated heat coefficient

Page: P000552. Classification: E. Verification: read the result.

Under the same closed-manifold hypotheses, \[a_2=\frac1{360}\int_M\bigl(2|\operatorname{Rm}|^2-2|\operatorname{Ric}|^2+5\operatorname{Scal}^2\bigr)dV.\] A local formula also contains a divergence term whose integral vanishes on a closed manifold; boundary problems require additional coefficients.

The three curvature terms match the established result of \citet[\S7]{mckeansinger1967curvature}; \citet[introduction and \S4]{gilkey1979recursion} supplies an independent recurrence derivation. The source integral needs its volume element, but no change to the written numerical coefficients.

Bib keys: mckeansinger1967curvature, gilkey1979recursion.

### 1973-333.7 — The missing off-diagonal Gaussian

Page: P000552. Classification: E. Verification: read the result.

Near the diagonal, in a normal neighborhood and as \(t\downarrow0\), the heat parametrix has the form \[K(t,x,y)\sim(4\pi t)^{-n/2}e^{-d_g(x,y)^2/(4t)}\sum_{j\ge0}u_j(x,y)t^j.\] The notebook displays the power series without the Gaussian. That abbreviated formula is valid on the diagonal, but is false as a literal off-diagonal expansion.

The local parametrix is classical; see the heat-kernel construction in \citet{mckeansinger1967curvature}. \citet[introduction, p.~202]{gilkey1979recursion} explicitly states off-diagonal rapid decay. The omitted exponential is an emendation of mathematical content.

Bib keys: mckeansinger1967curvature, gilkey1979recursion.

### 1973-333.8 — Sakai and the fourth heat coefficient

Page: P000552. Classification: E. Verification: indirect.

The source calls \(a_3\) the fourth coefficient, counting \(a_0\) first, and attributes a computation to Sakai. No formula for \(a_3\) is recorded, so the item is an attribution, not an occurrence of every term in the general cubic-curvature expression.

\citet{sakai1971eigenvalues}, Tohoku Math. J.23(4),589--603, appeared in1971. Publisher issue metadata were opened; the attribution is explicitly confirmed by \citet[introduction]{gilkey1979recursion}. The full Sakai formula was not independently read in this audit.

Bib keys: sakai1971eigenvalues, gilkey1979recursion.

### 1973-333.9 — Koblenz’s claimed independent fourth-coefficient computation

Page: P000552. Classification: F. Verification: unresolved lead.

The speaker, named Yura Koblenz from Leningrad, is said to have computed \(a_3\) independently of Sakai. There is no formula, manuscript title, date of independent discovery or method in the notebook.

Targeted searches for Koblenz, heat coefficients and Laplace asymptotics did not identify an exact primary publication. Sakai’s known computation does not prove or disprove the claim of independence. The attribution remains unverified, rather than classified as a new open mathematical question.

Bib keys: .

### 1973-333.10 — The lattice-point and Riemann-zero analogy

Page: P000552. Classification: F. Verification: read the result.

Gelfand writes a circle lattice-point main term \(\pi r^2\) plus a schematic oscillatory sum and identifies the frequencies with zeros of the Riemann zeta function, “modulo the Riemann hypothesis”. The summation variables, coefficients and scaling are overwritten or undefined. The literal expression is not a verified lattice-point formula.

No precise claim is recovered from this analogy. \citet[introduction]{colindeverdiere1973geodesicsii} distinguishes exact Poisson formulas on flat tori from general geodesic trace asymptotics, but this does not identify the notebook’s asserted zeta-zero formula. It remains F, with no transfer of an unrelated modern theorem.

Bib keys: colindeverdiere1973geodesicsii.

### 1973-333.11 — Closed billiard paths and oscillatory spectral density

Page: P000552-P000553. Classification: E. Verification: indirect.

Shnirelman identifies oscillation lengths with closed billiard trajectories in a ball; the continuation displays \(f(\lambda)=f_0(\lambda)+\sum c_k\lambda^{\alpha_k}\sin(\ell_k\lambda+\omega_k)\). The variable must be a frequency for \(\ell_k\lambda\) to be the usual phase. Amplitudes, smoothing, boundary conditions, repeated trajectories and degeneracies are not specified.

The named Balian--Bloch1972 paper is a strong historical match, but its publisher page returned403 and the exact formula was not read. \citet[introduction]{colindeverdiere1973geodesicsii} explicitly cites their bounded-domain Green-function method and gives a related closed-manifold theorem under nondegeneracy conditions. The match to the literal billiard formula remains partial.

Bib keys: balianbloch1972oscillations, colindeverdiere1973geodesicsii.

### 1973-333.12 — Cauchy smoothing and convergence

Page: P000552. Classification: E. Verification: read the result.

The notes convolve the spectral measure with \(\varepsilon/(\lambda^2+\varepsilon^2)\). A normalized Cauchy kernel has an extra factor \(1/\pi\). One must also specify a finite spectral cutoff or a convergent regularization: for frequencies of \(\sqrt L\) in dimension \(n\ge2\), the positive tail \(\sum_j\varepsilon/\lambda_j^2\) diverges by Weyl growth. If \(\lambda_j\) denotes eigenvalues of \(L\), the bare sum instead converges in dimensions below4. A rapidly decreasing test function always defines a suitable smoothed spectral measure.

Smoothing is an established spectral method, not a theorem guaranteeing convergence of this unspecific formula. The Weyl-law framework is in \citet[\S1]{mckeansinger1967curvature}; the oscillatory context is in \citet{colindeverdiere1973geodesicsii}. The convergence distinction is an editorial check of the displayed kernel.

Bib keys: mckeansinger1967curvature, colindeverdiere1973geodesicsii.

### 1973-333.13 — The heat trace is not the displayed oscillatory trace

Page: P000553. Classification: E. Verification: read the result.

The scan literally equates \(\sum e^{i\lambda_jz}\) with \(\operatorname{Tr}(e^{-z\Delta})\). For eigenvalues \(\mu_j\) of \(L\ge0\), the heat trace is \(\sum e^{-z\mu_j}\), holomorphic for \(\operatorname{Re}z>0\). If \(\lambda_j=\sqrt{\mu_j}\), the half-wave sum is \(\operatorname{Tr}(e^{iz\sqrt L})\), holomorphic for \(\operatorname{Im}z>0\) and distributionally defined on the real axis. These are different operators and domains.

The later half-wave equation on the page supports a frequency interpretation, but does not repair the earlier equality literally. Compare the complex-time heat analysis of \citet{colindeverdiere1973geodesicsii} and the later spectral-trace paper \citet{duistermaatguillemin1975spectrum}; the latter was received20October1974 and publishedFebruary1975.

Bib keys: colindeverdiere1973geodesicsii, duistermaatguillemin1975spectrum.

### 1973-333.14 — The unspecified general spectral-gap question

Page: P000553. Classification: F. Verification: read the result.

The “twin problem” asks for \(\lambda_{k+1}-\lambda_k>c\lambda_k^{-\nu}\) for “general operators”. No operator class, multiplicity convention, generic topology, constants or frequency convention is fixed. Read universally with multiplicities, it is false even for the circle.

The adjacent circle and torus examples show why a qualified formulation is essential. Neither the wave-trace theorem nor the near-flat torus theorem proves a lower bound for an unspecified generic class. The item remains F; no modern universal gap conjecture is silently substituted.

Bib keys: shnirelman1975multiplicity.

### 1973-333.15 — Exact spectral doublets on the circle

Page: P000553. Classification: E. Verification: read the result.

On a circle of length \(\ell\), the scalar Laplacian has eigenvalues \((2\pi m/\ell)^2\), each of multiplicity2 for \(m\ge1\). The half-wave eigenvalues are \(2\pi m/\ell\) with the same multiplicity. Every smooth metric on a circle is isometric to one specified by its total length, so metric perturbation preserves this doublet structure.

This elementary Fourier computation proves the particular counterexample to the unqualified lower-gap assertion. The notebook’s wider phrase about stable asymptotic double multiplicity should not be extended to an arbitrary operator perturbation without specifying its class. The nearby torus analogy is treated independently by \citet{shnirelman1975multiplicity}.

Bib keys: shnirelman1975multiplicity.

### 1973-333.16 — Shnirelman’s all-index close-neighbor theorem

Page: P000553. Classification: B. Verification: read the result.

Let a smooth Riemannian metric on \(T^2\) be sufficiently close to a flat metric, and let \(\lambda_k\) be the ordered eigenvalues of \(\sqrt{-\Delta_g}\), with multiplicities. Then, for every \(N\), there is \(C_N>0\) such that for every \(k>1\), \[\min(\lambda_{k+1}-\lambda_k,\lambda_k-\lambda_{k-1})<C_N k^{-N}.\] The closeness is enough for the invariant-torus construction used in the proof; no explicit norm threshold is supplied in the two-page announcement.

\citet[Theorem and Lemmas1--3, pp.~265--266]{shnirelman1975multiplicity} states exactly this all-index result, explicitly strengthening Lazutkin’s positive-density subsequence theorem. It was received by the Moscow Mathematical Society7May1974 and published1975, after the1April1974 notebook meeting. Both primary pages were read. This is B relative to Koblenz’s main talk, with Shnirelman’s intervention explicitly preserved.

Bib keys: shnirelman1975multiplicity.

### 1973-333.17 — The tentative three-torus comparison

Page: P000553. Classification: F. Verification: read the result.

The source says that in \(T^3\) “apparently” the preceding behavior no longer holds. It specifies neither a metric nor the quantifier of the alleged negation. Flat tori still have symmetry-related multiplicities, so the phrase cannot be read as an assertion about every three-torus metric.

\citet{shnirelman1975multiplicity} proves a two-dimensional theorem and does not supply the proposed three-dimensional negation. No exact primary theorem matching this tentative sentence was verified. It remains F rather than an eligible open problem.

Bib keys: shnirelman1975multiplicity.

### 1973-333.18 — Half-wave propagation and its trace

Page: P000553. Classification: E. Verification: read the result.

With \(L=-\Delta_g\ge0\), the Cauchy problem \(u_t=i\sqrt L\,u\), \(u(0)=\delta_x\), has distribution kernel \(U(t,y,x)\) of \(e^{it\sqrt L}\). Its distributional trace is \(\int_M U(t,x,x)dV=\sum_k e^{it\sqrt{\mu_k}}\). The sum is not generally pointwise convergent for real \(t\).

The spectral construction is classical before the meeting. Its microlocal analysis uses the real-principal propagation framework of \citet[\S6.1]{duistermaathormander1972fourierii}; the later \citet{duistermaatguillemin1975spectrum} formalizes the trace relation. The source uses the same letter for energy eigenvalues and their square roots, requiring this distinction.

Bib keys: duistermaathormander1972fourierii, duistermaatguillemin1975spectrum.

### 1973-333.19 — Unit-speed singularity propagation and caustics

Page: P000553. Classification: E. Verification: read the result.

The page places kernel singularities at \(|x-y|=t\), draws a returning loop, and mentions bifurcations. On a Riemannian manifold the precise statement is propagation along the geodesic Hamilton flow of \(|\xi|_g\), at unit speed in the base. The equality \(d_g(x,y)=|t|\) describes the short-time normal-neighborhood front, not all returning geodesics or caustics globally.

\citet[Theorem6.1.1]{duistermaathormander1972fourierii} establishes propagation of wave-front singularities along real-principal bicharacteristics before the talk. The sketch does not define an additional classification of bifurcations. Its loop is accounted for as a propagation/return diagram, not a separate unknown theorem.

Bib keys: duistermaathormander1972fourierii.

### 1973-333.20 — Closed-geodesic contributions to a wave trace

Page: P000553. Classification: E. Verification: read the result.

Restricting the propagator to the diagonal and integrating selects fixed points of geodesic flow, hence closed geodesics. The singular support of the half-wave trace is contained in zero together with signed lengths of closed geodesics. Identifying a nonzero singular coefficient or a full expansion requires clean/nondegenerate fixed-point hypotheses and control of cancellations.

\citet[introduction and main theorem]{colindeverdiere1973geodesicsii} gives a pre-talk closed-manifold oscillatory spectral/geodesic relation under explicit nondegeneracy hypotheses. \citet{duistermaatguillemin1975spectrum}, receivedOctober1974 and publishedFebruary1975, is a later general trace-theoretic continuation; only its publisher metadata were checked here. These are related to, but not an exact theorem for, the notebook’s unspecified billiard amplitudes.

Bib keys: colindeverdiere1973geodesicsii, duistermaatguillemin1975spectrum.
