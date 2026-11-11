from pathlib import Path
import json,csv,collections
root=Path(__file__).resolve().parents[2];p=root/'parts'
items=json.loads((p/'early_items.json').read_text());talks=json.loads((p/'early_talks.json').read_text());probs=json.loads((p/'early_problems.json').read_text());cr=list(csv.DictReader((p/'early_corrections.csv').open()))
s=r'''# Early-record research and verification log

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
'''
counts=collections.Counter(v['class'] for v in items)
s+='\nCurrent checkpoint: '+str(len(talks))+'talks/heading records; '+str(len(items))+'raw items, '+str(len(items)-5)+'after removing the five exact source aliases; '+str(len(cr))+'correction rows; '+str(len(probs))+'problem entries owned here (two new settled IDs and two reused IDs). Classes: '+', '.join(k+'='+str(counts.get(k,0)) for k in 'ABCDEF')+'. Middle-owned GP-1974-10 is linked from340.7 but not duplicated in this agent’s problem file.\n'
s+='\n## Item-by-item coverage ledger\n\n| Occurrence | Page(s) | Class | Kind | Title |\n|---|---|---|---|---|\n'
for v in items:s+='|'+v['id']+'|'+v['pages']+'|'+v['class']+'|'+v['kind']+'|'+v['title'].replace('|','/')+'|\n'
s+='\n'+(p/'early_boundary.md').read_text()
(p/'early_research.md').write_text(s)
print('research log bytes',len(s.encode()))
