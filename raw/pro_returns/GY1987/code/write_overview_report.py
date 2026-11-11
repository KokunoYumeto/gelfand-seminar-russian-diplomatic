#!/usr/bin/env python3
"""Regenerate the overview and editorial report from audited chapter data."""
from collections import Counter,defaultdict
import csv,json,re
from pathlib import Path
import sys

D=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
talks=json.loads((D/'GY1987_talks.json').read_text())
items=json.loads((D/'GY1987_items.json').read_text())
problems=json.loads((D/'GY1987_problems.json').read_text())
talkmap={x['record']:x for x in talks}
classes=Counter(x['class'] for x in items)
with (D/'GY1987_corrections.csv').open(newline='',encoding='utf-8') as f:corrections=list(csv.DictReader(f))
def speaker_name(x):
 name=x.get('speaker') or talkmap[x['record']]['speaker'] or 'Unattributed'
 if name.startswith('I. M. Gelfand;'):return 'I. M. Gelfand'
 if name.startswith('Unidentified reporter'):return 'Unidentified reporter'
 return name
speakers=Counter(speaker_name(x) for x in items)
area_file=D/'logs'/'item_areas.json'
areas=json.loads(area_file.read_text()) if area_file.exists() else {}
default_areas={
714:'Sheaves, categories and homological algebra',715:'Algebraic combinatorics and representation theory',
716:'Integrable systems',717:'Sheaves, categories and homological algebra',718:'Sheaves, categories and homological algebra',
719:'Analysis and summation',720:'Algebraic combinatorics and representation theory',
721:'Sheaves, categories and homological algebra',722:'Sheaves, categories and homological algebra',
723:'Dynamical systems',724:'Dynamical systems',725:'Matroids and commutative algebra',
726:'Algebraic combinatorics and representation theory',727:'Dynamical systems',
728:'Spectral and linear algebra',729:'Arithmetic, adeles and determinants',730:'Toric and algebraic geometry',
733:'Analysis and summation',734:'Differential geometry',735:'Spectral and linear algebra',
736:'Conformal field theory',737:'Spectral and linear algebra',738:'Integrable systems',
739:'Sheaves, categories and homological algebra',740:'Matroids and commutative algebra',
741:'Historical mathematical problems',742:'Toric and algebraic geometry',743:'Toric and algebraic geometry',
744:'Sheaves, categories and homological algebra',745:'Graph theory and algorithms',
746:'Sheaves, categories and homological algebra',747:'Topology and gauge theory',
748:'Topology and gauge theory',749:'Quantum groups and knot invariants',750:'Integrable systems',751:'Topology and gauge theory'}
# One primary area per occurrence; keep the mapping explicit and reproducible.
primary={x['id']:default_areas[x['record']] for x in items}
for identifier in ['1987-716.4']:
 if identifier in primary:primary[identifier]='Spectral and linear algebra'
for identifier in ['1987-719.3']:
 if identifier in primary:primary[identifier]='Algebraic combinatorics and representation theory'
area_counts=Counter(primary.values())
(D/'logs'/'primary_area_map.json').write_text(json.dumps(primary,ensure_ascii=False,indent=2)+'\n')

overview=r'''\setlength{\emergencystretch}{3em}
\hyphenation{Par-tha-sa-ra-thy}
\noindent\textbf{Scope and editorial date: 11 November 2026.}
This chapter covers all 38 catalogue records, 714--751, in notebook
order, from October 1987 through April 1988. The archive windows overlap;
the Russian text and scans determine the narrower page attributions.
Record 719 precedes 718, and Gelfand's February exercises (733) precede
Beilinson's programme (732). The year heading and programme remain
records without invented mathematics. P001460 is a reading list.
P001478 explicitly begins 12 September 1988; P001479 continues that
next academic year and is excluded, with the boundary documented in
the corrections. The source catalogue is \citet{mccme2026gelfand}.

\paragraph{The mathematical year.}
Beilinson's course moves from sheaf cohomology, resolutions and derived
categories to microlocal and perverse sheaves, then to Morse and gauge
theory. Gelfand's interventions connect symmetric functions, Schubert
polynomials, matroids and Hecke algebras with explicit calculations.
Other sustained strands are dynamical zeta functions, joint stochastic
spectra, toric vector bundles, conformal field theory, principal angles,
quantum integrable systems, exceptional bundles, graph colouring and
quantum-group link invariants. Their coexistence is a feature of the
seminar; it does not imply that every juxtaposition is a precise theorem.

\begin{center}
\begin{tabular}{@{}lrrrrrrr@{}}
\toprule
Class & A & B & C & D & E & F & Total\\
\midrule
Items & @A@ & @B@ & @C@ & @D@ & @E@ & @F@ & @TOTAL@\\
\bottomrule
\end{tabular}
\end{center}
The occurrence index has @TOTAL@ items; the problem index has @PROBLEMS@
definite questions or conjectures. A--F describe historical fate,
not mathematical correctness or originality. The separate assessment
fields preserve that distinction. An established theorem can have a
false literal notebook formula, and an unresolved wording can concern
a well-developed subject. No unsuccessful search is promoted into an
orphan-idea claim.

\paragraph{What became of the talks.}
Exact theorem matching is more informative than subject matching.
Klyachko's filtration construction led to the 1989 Russian paper
(English translation 1990), submitted in February 1988, including
cohomology and characteristic classes
\citep[Sections~2--4]{klyachko1989equivariant}.
Conversely, some material that looks like a subsequent discovery was
already circulating: the Schubert-character construction had a 1986
preprint and 1987 announcement (item 1987-720.21). Reshetikhin's reports
carry 1987 preprint identifiers, while the scanned editions have 1988
imprints; these are distinguished rather than treated as one date.
Publication chronology is therefore checked
against first circulation wherever it could change a class.

\paragraph{Open questions and the selected development.}
The joint stochastic-spectrum question, GP-1987-21, concerns a whole
multiset, not the Karpelevich region for one eigenvalue. The development
gives complete proofs in dimensions two and three, structural necessary
conditions, and a five-dimensional counterexample to sufficiency of
all power-sum inequalities. Recent work still addresses the general
realization problem \citep{johnsonpaparella2025perron}.
The microlocal reconstruction question, GP-1987-46, retains the
codimension-two essential-image conditions explicitly singled out in
\citet[Problem~9.3]{kashiwaravilonen2014codimension}; a fully faithful
embedding alone is insufficient. The named Riemann hypothesis offers
no bounded seminar-specific route. These latter questions receive
precise status entries without manufactured partial solutions.
Three additional annotations repair a bracket that fails Jacobi,
settle the finite-dimensional tensor-angle range, and disprove the
notebook's equivalence between integral
homology-sphere topology and vanishing twisted first cohomology.
All supplied proofs are marked, independently rechecked, and make no
novelty claim; computational output is included.

\paragraph{Continuity and limits.}
The Schubert material continues 1985-661.1--8, matroid representability
continues 1985-658.12--16, the Virasoro discussion returns to
GP-1982-03 and 1985-657, and determinant lines connect with
1985-655 and 1985-666. Earlier occurrence identifiers are retained
without pretending that a thematic resemblance is the same problem.
Primary papers, author manuscripts, Math-Net records and scans carry
the argument; metadata-only checks and unresolved leads remain
explicit. The @CORRECTIONS@ corrections distinguish mistranscription,
translation, ambiguity, faithful mathematical error and provenance.
Searches establish the bounded conclusions recorded here, not the
absence of all unpublished work.
'''
for token,value in {**classes,'TOTAL':len(items),'PROBLEMS':len(problems),'CORRECTIONS':len(corrections)}.items():
 overview=overview.replace('@'+str(token)+'@',str(value))
for c in 'ABCDEF':overview=overview.replace('@'+c+'@',str(classes[c]))
(D/'GY1987_overview.tex').write_text(overview,encoding='utf-8')

def table(headers,rows):
 return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join('---' for _ in headers)+' |']+
                  ['| '+' | '.join(str(x).replace('|','/') for x in row)+' |' for row in rows])

class_names={'A':'Published soon after by the speaker/Gelfand','B':'Developed by others','C':'Partly developed; a specified question remains','D':'Not developed after a documented search','E':'Known before the talk','F':'Insufficiently identifiable from the notes'}
report=f'''# GY1987: editorial and research report

**Chapter:** The I. M. Gelfand seminar, academic year 1987–88.  
**Status date:** 11 November 2026.  
**Scope:** all 38 catalogue records, 714–751; {len(items)} mathematical occurrences, {len(problems)} problem records and {len(corrections)} correction entries.

## 1. Counts and the unit being counted

An item is a separately stated definition, construction, theorem, claim, question, method or mathematical remark. A catalogue record is not necessarily a complete lecture: several share one page, two are organizational material, and an intervention can have a different speaker from its parent record. Counts measure this edition's explicit splitting decisions, not the amount of original research in the seminar.

### Historical class

{table(['Class','Meaning','Items'],[(c,class_names[c],classes[c]) for c in 'ABCDEF'])}

### Speaker of the item

The optional item-level speaker overrides the record speaker, so Gelfand's interventions are counted with Gelfand. The note-taker qualification on his problem sheet does not create a separate speaker category. Unattributed reports remain unattributed. These counts sum to {len(items)}.

{table(['Speaker attribution','Items'],sorted(speakers.items(),key=lambda z:(-z[1],z[0])))}

### Primary mathematical area

One primary area is assigned to each occurrence for a reproducible, nonoverlapping count. Several items could reasonably receive secondary tags; the complete assignment is in `logs/primary_area_map.json`.

{table(['Primary area','Items'],sorted(area_counts.items(),key=lambda z:(-z[1],z[0])))}

### Record-level coverage

The following table follows the actual order of the source. The narrow page intervals are attributions within the attached notebook, not reproductions of the overlapping catalogue windows.

{table(['Record','Date','Items','Source pages','Title'],[(t['record'],t['date'] or 'undated',sum(x['record']==t['record'] for x in items),t['pages'],t['title']) for t in talks])}

## 2. What required the most care

### Page attribution and the academic-year boundary

The catalogue intervals are overlapping retrieval windows. Using them literally would duplicate mathematics and place portions under the wrong speaker. The Russian headings and scans establish record719 before718, record733 before732, Kapranov739 beginning only at P001444, and Beilinson751 ending at P001477. P001460 is a Bourbaki reading list, described in the record747 summary rather than converted into asserted theorems. P001478 says 12 September 1988; P001479 continues that session. Both are retained in the provenance account, outside this chapter's mathematical occurrence index. All 95 supplied source pages are thereby accounted for: 93 belong to the academic-year text/context and two are next-year carryover.

### Mathematical hypotheses hidden by shorthand

The main editorial risks were unrestricted claims that become true only with specific hypotheses: semisimple/generic Hecke parameters; real versus complex matroid realizations; smooth versus singular toric fans; holomorphic/nuclear transfer-operator determinants; connected versus disconnected gauge stabilizers; ordinary versus twisted cohomology; finite-dimensional versus Hilbert-space principal angles; and regularity assumptions behind a local functional's expression as a jet integral. Each repair is stated as reconstruction. False formulas copied faithfully from the notebook are mathematical emendations, not accusations of mistranscription.

### Chronology and exact publication matching

The Schubert-character question is a useful stress test. The full Kraśkiewicz–Pragacz paper appeared in 2004, but its introduction documents a 1986 preprint and 1987 announcement. Dating only the full paper would misclassify knowledge available before November 1987. Reshetikhin's two LOMI reports have 1987 series identifiers, but the scanned editions bear 1988 imprints; the second explicitly records a recommendation for publication on 6 June 1987. A report number alone is not evidence of the exact date of public circulation. Klyachko's paper was received 3 February 1988, appeared in Russian in 1989 and English in 1990. These dates answer different questions and are retained separately. Happel's 1987 Theorem 5.12 (p. 358), announced at Ottawa in 1984, already supplies the Dynkin/iterated-tilted endpoint. His §1.7 corollary anchors the pre-talk derived tilting equivalence in items739.2 and739.4, classified E. Item739.3 is B specifically for Parthasarathy's explicit heart-realization criterion, published in December1988; its receipt on15February1988 does not establish public circulation before the seminar. This refinement is not described as the first Dynkin classification. The Ushveridze review's stability conditions differ by a half-unit shift; the review therefore corrects, rather than validates, the notebook's blanket classical/quantum equivalence.

## 3. Which searches found the publications

The research was divided by source blocks, then reconciled by an independent integration audit. The retained search notes in `research/` give opened URLs, publication locators and failure modes. The bibliography's `annote` fields distinguish full-result reading, metadata confirmation and inherited background. A `verified` note means that the cited link or DOI was opened; it does not claim that every proof in the work was checked.

* **Short Soviet publications:** author–subject searches on Math-Net located the Klyachko toric-bundle paper, Rudakov's exceptional-bundle papers, Radul's work and contemporary announcements. Original/translated editions were kept separate in the chronology.
* **Author manuscripts and backwards references:** the Kraśkiewicz–Pragacz introduction recovered the early Schubert-functor chronology; the Reshetikhin LOMI manuscripts distinguished report numbering, recommendation date and imprint. Ushveridze's Russian review supplied theorem and equation matches after OCR was checked against page images.
* **Exact theorem searches:** Parthasarathy's reflection equivalences and heart conditions, Gelfand–MacPherson–Vilonen's Theorem6.4, and Kashiwara–Vilonen's Theorem1.1 and Problem9.3 prevented broad thematic matches from becoming purported solutions.
* **Current status checks:** the official Clay page supports the Riemann-hypothesis status. The2024–2025 nonnegative-inverse-eigenvalue papers distinguish a joint spectral list from a one-eigenvalue region. Recent work on explicit perverse-sheaf descriptions was checked without treating a special-family result as a uniform solution.
* **Classical exercises:** primary publications, author-hosted texts and precise modern formulations identified Good's Dyson proof, Hall/Rado transversals, classical determinant formulas, finite-dimensional principal angles and the older sheaf/derived formalism.

Coverage is a bounded, documented literature investigation. It does not certify exhaustive access to every Soviet preprint, unpublished lecture, MathSciNet/zbMATH record or later article. Failed publisher requests were followed by legitimate author or institutional copies where available. No inaccessible proof is presented as read, and no failed title search establishes classD.

## 4. Problems and what was developed

Only definite questions receive problem identifiers. Solved exercises may be included when they recur or have a clear later mathematical identity. A broad exhortation such as 'classify', 'discretize', or 'replace the circle by a manifold' is not made into an open conjecture without a specified object, quantifiers and equivalence relation. The attached earlier index was searched for exact recurrences; old problem identifiers are reused when available, and earlier occurrence identifiers are retained even when no old problem ID exists.

{table(['Problem','Title','Current-year occurrences'],[(p['id'],p['title'],', '.join(o for o in p['occurrences'] if o.startswith('1987-'))) for p in problems])}

### Selected class-C development: simultaneous stochastic spectra

GP-1987-21 asks for the complete eigenvalue multiset of a real nonnegative row-stochastic matrix. The development proves compactness and semialgebraicity for fixed order, two forms of star-shapedness, the power-sum/JLL inequalities, and complete two- and three-state characterizations with explicit realizing matrices. It gives a three-state counterexample to marginal or moment-only reasoning and the classical five-state list `1,1,−2/3,−2/3,−2/3`, with a full proof that every JLL inequality holds although no nonnegative realizing matrix exists. Fixed-order membership for algebraic input is decidable by real quantifier elimination; the unresolved question is an explicit useful structural characterization in general order, not bare decidability. No theorem in this development is claimed to be historically new.

The exact remaining obstruction is joint realization by one matrix, including reducibility, multiplicities and compatible invariant blocks. A bounded subsequent project would specify a four-state zero pattern, derive its exact feasible region and compare it with existing order-four results. The present work stops before claiming a new classification or an unverified novelty result.

### Three complete annotations

The printed second bracket for the Neumann system fails Jacobi: its cyclic expression on `(M_1,p_1,p_2)` is `(a_3−a_2)M_2`. A repaired mixed coefficient and sign give a compatible Poisson pencil and the same Hamiltonian vector field. The coordinate identities were checked symbolically; an independent proof realizes the repaired table as the Lie bracket `XDY−YDX` on skew four-by-four matrices. The correction is explicitly an algebraic emendation, not an assertion that a unique intended formula has been recovered.

For the tensor-angle exercise, normalized nonzero tensors in a real or complex d-dimensional space with d≥2 attain precisely the nonnegative principal-cosine lists with sum≤1; d=1 has only cosine1. The proof handles rankzero, deficient rank and full rank separately. This is an E annotation, not an invented open problem.

For twisted first cohomology, finite-group averaging shows that `H^1(RP^3;E)=0` for every finite-dimensional real or complex local system E although `H_1(RP^3;Z)=Z/2`. In the other direction, the connected sum M of two Poincaré homology spheres admits an irreducible SU(2) representation rho for which `H^1(M;ad rho)` has real dimension3. The bundle is trivial over the three-dimensional base, so the counterexample meets the notebook's bundle setting. A cocycle/free-product calculation and twisted Mayer–Vietoris independently give the same dimension. This corrects the literal equivalence without undermining the appropriately perturbed Floer construction.

The Riemann hypothesis and arbitrary-singular-support microlocal reconstruction have precise C entries but no supplied geometry or mechanism supporting a new bounded contribution in this run. In the latter, the codimension-three extension theorem does not remove the codimension-two essential-image conditions. The problem is stated for complex coefficients; a general positive-characteristic extension is not imported silently.

## 5. Verification and the second check

The mathematical proofs were independently reviewed across source blocks. The stochastic converse was re-derived through explicit characteristic polynomials and Fourier eigenvectors; the triangular bound was independently obtained from trace(P²) and Cauchy–Schwarz. The five-dimensional contradiction uses Perron blocks and their traces, independent of finite moment tests. The cohomology result was recomputed with a topological exact sequence. The tensor cross-Gram calculation was checked entry by entry and then formed directly in the ambient tensor product.

The included `code/verify_development.py` and `logs/development_checks.json` report:

* Four symbolic characteristic-polynomial identities, with zero residuals and identically unit row sums.
* 5,741 feasible rational real-pair cases and820 trace-rejected cases on the denominator40 grid;280 feasible boundary cases.
* 1,225 exact rational circulant-simplex cases at denominator48, including144 boundary cases.
* Two independent seeded runs, each containing2,000 stochastic matrices in orders2,3,5,7. All required inequalities passed; the largest eigenvalue-modulus excess was3.11×10⁻¹⁵, at floating-point roundoff scale.
* 2,048 exact power sums and2,048 exact JLL exponent pairs for the five-state example; all four partitions of the three negative roots between two Perron blocks fail a block-trace condition. Universal validity is proved in the text, not inferred from this finite range.
* The integral presentation determinant−1, zero common adjoint fixed space, a six-dimensional cocycle space and a three-dimensional quotient after principal cocycles.
* 600 direct real/complex tensor-embedding checks and150 realization constructions across dimensions1–6. The largest cross-Gram entry discrepancy was5.55×10⁻¹⁷ and the largest realization/norm discrepancy was4.04×10⁻¹⁴.

The early-source diagnostic script supplies a further nine check groups. It checks all 20 coordinate Jacobi triples for the repaired Neumann bracket and its pencil; exact Hecke weight identities and their q→1 limits; the worked Schubert polynomial by both divided differences and Jacobi–Trudi; all 36 pairings in S3 and576 in S4 and the adjoint divided-difference identities; determinant exchange in dimensions2 and3 plus a full symbolic two-dimensional check; the double-composition counterexample (1 versus0); different bimatroids with identical row/column matroids; rank-one sign nonuniqueness; and the two-letter Hecke Frobenius normalization. The output deliberately preserves counterexamples to the **printed** formulas. The assertions that pass are the corrected formulations, never the false source claims.

The independent review caught the invalid printed Neumann bracket, a misleading description of the triangular complex-pair region's intersection with the real axis, and a needed clarification of the abelianization relation-matrix convention. A further cross-subsection review caught reused matrix-unit notation that had different skew/ordinary meanings; the tensor construction now specifies its nonzero entries directly. These were corrected. No failed case remains concealed in the finite output. Source-formula checks, including those for the Neumann Hamiltonian, Hecke weights, trigonometric/elliptic addition laws and twisted cohomology, are recorded as corrections with their respective evidence.

The supplied builder and style are included unchanged. `logs/data_audit.json` checks source order, exact record coverage, consecutive academic-year identifiers, reference presence, problem backlinks, enumerated assessment values and accidental control characters. `logs/build.log` and the XeLaTeX/BibTeX logs document the successful required build. The final PDF has 153 pages and typesets all 99 bibliography entries. The automated page audit found no off-page text, overflowing boxes, missing glyphs, undefined citations/references or pending cross-reference rerun warning. All pages were visually reviewed in contact sheets, with full-resolution inspection of the overview, revised entries, selected development pages and bibliography. `logs/pdf_audit.json` and `logs/visual_review.json` record the checks and the exact reviewed PDF hash. The bibliography has 97 opened entries marked verified and two explicitly unverified original sources; later checked sources support their indirect uses.

## 6. What A–F misses this year

Historical fate, literal correctness and proof verification are separate axes. An E entry may contain a false handwritten sign, an A entry may be only a partial match to the published theorem, and an F entry may be a vague intervention in an established theory. The separate fields are essential. In particular, 'F' says the notes do not identify an exact claim sufficiently; it does not say no mathematics exists. 'C' says which identified part remains, not merely that the broader field is active.

The other limitation is granularity. One occurrence can state a definition, derive a formula and pose an example. Splitting these makes retrieval precise but inflates counts relative to a lecture-based metric. This report supplies the record counts and a reproducible primary-area map so comparisons with earlier chapters can use the same unit. The count of published items should not be read as a quantitative originality score.

## 7. Recommended method and data refinements

Preserve the fixed seven-file schema for compatibility. Add optional fields in a future version rather than overloading existing values:

| Proposed field | Purpose |
| --- | --- |
| `source_segments` | Record within-page start/end anchors, shared pages, and excluded carryover explicitly. |
| `date_basis` | Distinguish manuscript date, catalogue date and editorial inference. |
| `first_circulation`, `publication_date`, `translation_date` | Prevent a late full publication from changing historical classification. |
| `result_locator`, `verification_url`, `checked_at`, `verification_scope` | Make a read theorem distinguishable from opened metadata at reference level. |
| `related_items`, `relation_type` | Separate exact recurrence, prerequisite, analogy, correction and specialization. |
| `areas` | Permit multiple subject tags while retaining one optional primary area for counts. |
| `source_reading_confidence`, `fate_confidence` | Separate uncertain handwriting from uncertain publication matching. |
| `development_kind`, `novelty_claim` | Separate a bounded C/D development from an elementary proof or error annotation. |

The current edition puts this information in reconstruction, fate, bibliography annotations and the research logs when the fixed schema has no dedicated place. Automatically infer neither publication matches nor problem identity from keyword similarity.

## 8. Presentation on the companion website

A reader arriving at a talk should first see the date/speaker provenance, precise source span, a short topic summary and the item list. Each item should open into the three distinct layers: source wording, modern statement with reconstruction, and historical fate/current status. Show the literal-correctness and verification badges beside the fate class; opening an E item should not conceal a faithful mathematical error. Put the scan-page link beside each correction and each formula-dependent reconstruction.

The most useful paths this year are: the derived-category course into quiver hearts and exceptional mutations; 1985 Schubert and matroid items into the1987 combinatorics; GP-1982-03 into the1988 Virasoro discussion; stochastic-matrix questions into the complete low-dimensional development; principal angles into the tensor-range proof; and vanishing-cycle reconstruction into the codimension-two question. The gauge-theory entries need an immediate link to the twisted-cohomology counterexamples, so a reader does not retain the source's false equivalence.

The problem page should show all occurrences in chronological/source context, exact quantifiers, dated status and the strongest checked result. Permit filters for class, speaker, area, correctness, verification and development. Search should match both transliteration variants and names such as Good/Vuda, Dipper/Tipper and Ushveridze/Usheridze without overwriting the diplomatic reading. A source-order toggle is necessary because record-number order and date order do not always agree. The boundary notice for P001478–79 should lead to the next academic year when that chapter exists.

## 9. Files and reproducibility

The seven schema files are authoritative; `GY1987_chapter.tex` and `GY1987_test.pdf` are built outputs. `GY1987_test.tex`, the supplied `build_chapter.py`, `gelfand_companion.sty` and format specification support rebuilding. Reproduce the document with:

```sh
python build_chapter.py GY1987
xelatex -interaction=nonstopmode -halt-on-error GY1987_test
bibtex GY1987_test
xelatex -interaction=nonstopmode -halt-on-error GY1987_test
xelatex -interaction=nonstopmode -halt-on-error GY1987_test
```

Run the mathematical diagnostics from the package root with `python code/verify_development.py > logs/development_checks.json`. They require Python3, SymPy and NumPy; the exact versions used appear in the output. The audit and reporting scripts use Python's standard library; PDF layout inspection uses PyMuPDF. Research sources remain external links. The source transcriptions and full copyrighted research papers are not repackaged; the relevant findings and short quotations are in the edition itself.
'''
report=re.sub(r'\b(record|Record|item|items|Theorem|Problem|Proposition|in|a|the|with|including|and|of|on|was|is|only|cosine|dimension|dimensions|orders|denominator|at|across|January|February|March|April|May|June|July|August|September|October|November|December)(?=\d)',r'\1 ',report)
report=report.replace('Python3','Python 3').replace('classD','class D').replace('rankzero','rank zero')
(D/'GY1987_report.md').write_text(report,encoding='utf-8')
print(json.dumps({'overview_words':len(overview.split()),'report_words':len(report.split()),
                  'items':len(items),'area_total':sum(area_counts.values()),'speaker_total':sum(speakers.values())}))
