"""Build an auditable evidence ledger from the final early-batch bibliography."""
from pathlib import Path
import json, re, collections
P=Path(__file__).parent
items=json.loads((P/'items.json').read_text())
problems=json.loads((P/'problems.json').read_text())
text=r'''# GY1979 records 462–470: research and evidence log

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

'''
for m in re.finditer(r'(?ms)^@\w+\{([^,]+),\n(.*?)^\}',(P/'references.bib').read_text()):
 key,body=m.groups()
 fields=dict(re.findall(r'^\s*(\w+)\s*=\s*\{(.*)\},?\s*$',body,re.M))
 uses=[d['id'] for d in items if key in d['refs']]
 text+='### '+key+'\n\n'
 text+='- URL opened or attempted: '+fields.get('url','[DOI below]')+'\n'
 if fields.get('doi'): text+='- DOI: '+fields['doi']+'\n'
 text+='- Bibliographic verification label: '+fields.get('note','unspecified')+'.\n'
 text+='- Result, locators, support and limitations: '+fields.get('annote','[See item assessment.]')+'\n'
 text+='- Item occurrences supported: '+(', '.join(uses) or 'Research context only')+'.\n\n'
text+=r'''## Additional primary leads, failed access, and rejected substitutions

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
'''
(P/'research_log.md').write_text(text)
print('Wrote',len(text.split()),'words of evidence log.')
