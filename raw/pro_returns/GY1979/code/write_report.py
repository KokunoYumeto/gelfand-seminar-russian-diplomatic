#!/usr/bin/env python3
"""Generate the overview and report from final audited occurrence data."""
from pathlib import Path
from collections import Counter,defaultdict
import csv
import json
from audit_chapter import bib_entries

D=Path(__file__).resolve().parent.parent
talks=json.loads((D/'GY1979_talks.json').read_text())
items=json.loads((D/'GY1979_items.json').read_text())
problems=json.loads((D/'GY1979_problems.json').read_text())
corrections=list(csv.DictReader((D/'GY1979_corrections.csv').open()))
refs=bib_entries((D/'GY1979_references.bib').read_text())
classes=Counter(x['class'] for x in items)
rec={t['record']:t for t in talks}
speaker_items=Counter(rec[x['record']]['speaker'] for x in items)
speaker_records=Counter('(catalog heading)' if t['kind']=='heading' else t['speaker'] for t in talks)
attributed=Counter(x.get('speaker') or rec[x['record']]['speaker'] for x in items)
base_area={462:'Quantum gravity and supergravity',463:'Integrable systems and wave dynamics',
464:'Spinors, quaternions and projective transformations',465:'Spin geometry and index theory',
466:'Fourier analysis and oscillatory integrals',467:'Twistor and complex geometry',
468:'Superalgebra and matrix problems',469:'Complex geometry and Abelian functions',
470:'Representations of infinite-dimensional groups',471:'Hamiltonian constraints and quantization',
472:'Hamiltonian constraints and quantization',473:'Hamiltonian constraints and quantization',
474:'Quantum theory and quantization',475:'Hamiltonian constraints and quantization',
476:'Algebraic K-theory and regulators',477:'Special functions and algebraic K-theory',
478:'Hamiltonian constraints and quantization',479:'Gauge fields and particle physics',
480:'Gauge fields and particle physics',481:'Catalog heading',482:'Gauge fields and large-rank limits',
483:'Representation theory and Kazhdan–Lusztig theory',484:'Topology of singular spaces',
485:'Representations of infinite-dimensional groups',486:'Characteristic classes and combinatorial topology',
487:'Characteristic classes and combinatorial topology',488:'Hydrodynamics and integrable systems'}
area_rows=[]
for x in items:
    area=base_area[x['record']]
    reason='Primary subject of this source record'
    if x['record']==468 and int(x['id'].split('.')[-1])>=13:
        area='Algebraic geometry and exterior-module constructions'
        reason='The BGG/projective-bundle/Grassmannian intervention, separated from supermatrix algebra'
    if x['id']=='1979-464.1':
        area='Quantum electrodynamics'
        reason='The electron--positron annihilation item is distinct from the subsequent algebraic discussion'
    if x['id']=='1979-466.4':
        area='Symplectic linear algebra'
        reason='The alternating-form self-adjoint normal-form exercise is distinct from the Fourier exercises'
    area_rows.append({'id':x['id'],'area':area,'assignment_rule':reason})
areas=Counter(x['area'] for x in area_rows)
with (D/'code/area_assignments.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['id','area','assignment_rule']);w.writeheader();w.writerows(area_rows)

overview=r'''\noindent\textbf{Scope and editorial basis.}
This chapter covers all 27 MCCME records 462--488 in manuscript source order, with
dated assessments as of 10 November 2026. The Russian transcription is the textual
authority; the scans arbitrate doubtful formulas and attribution. The supplied
79-page envelope includes three boundary pages: P000840 is already represented by
1978-460.12--1978-460.20, and P000917--P000918 belong to the session dated
22 September 1980. Neither is counted again as a 1979--80 occurrence. The present
year's content occupies P000841--P000916. Record 481 is retained as a catalog
heading. The critical date of record 473 is 29 October 1979, against the catalog's
29 September; on 19 November, Gelfand's record 477 precedes Beilinson's record 476
in the manuscript.

The occurrence index contains COUNTITEMS distinct mathematical items, COUNTPROBLEMS
problem threads, and COUNTREFS bibliography entries. Item boundaries distinguish
definitions, constructions, mathematical claims, explicit questions, and identifiable
interventions. A class records historical fate; literal correctness and strength of
publication match are separate assessments.
\begin{center}
\begin{tabular}{lrrrrrr}
\toprule
Class & A & B & C & D & E & F\\
\midrule
Items & COUNTA & COUNTB & COUNTC & COUNTD & COUNTE & COUNTF\\
\bottomrule
\end{tabular}
\end{center}

\noindent\textbf{The main lines.}
Much of the autumn is an extended mathematical encounter with quantum field theory:
Kallosh's reports on gravity and supergravity; Batalin's careful progression through
constraints, gauge slices, ghosts and BRST identities; and Kobzarev's account of
gauge fields, confinement and particle masses. Formal functional integrals are kept
separate from convergent finite-dimensional formulas. The early BRST material is
not retrospectively identified wholesale with the later BV formalism.

The surrounding mathematics is unusually broad. Zakharov treats resonance and
integrability in September and long-wave hydrodynamics in February. Gindikin's
twistor geometry and Berezin's supermathematics lead into projective bundles and
exterior algebras. Shabat's double-translation surfaces require the missing
nondegeneracy hypotheses in the classical Jacobian theorem. H\o egh-Krohn's energy
representations retain a delicate two-dimensional question. In November, Gelfand's
dilogarithm list is followed by Beilinson's specific regulator construction; the
latter has a close 1980 publication match. January brings Migdal's loop equations,
Zelevinsky's Kazhdan--Lusztig material and MacPherson's topology. Olshanskii's
representations and MacPherson's combinatorial characteristic classes distinguish
pre-talk results from genuinely subsequent developments. Their precise source
locators and chronology are given in the corresponding entries.

\noindent\textbf{What remains and what is developed here.}
The chapter does not turn a broad research programme into a definite new conjecture.
Continuum confinement is linked to the older static-potential problem; a closed
large-rank equation is not itself an area-law proof. The general two-dimensional
energy-representation question is distinguished from restricted cases and from a
published proof claim with a documented gap. Negative literature searches are reported as retrieval
limits, not proof that an idea was abandoned.

Berezin's two explicit matrix questions support a bounded mathematical treatment.
The normal-form question has an algorithmic answer through a finite-dimensional
matrix-algebra action; an explicit matrix-pair reduction explains the limits of a
simple Jordan analogy. For the even commutant of an arbitrary odd two-by-two matrix
over four Grassmann generators, the development gives a complete coefficient
parametrization, all dimension strata, and full proofs. Its exact computations were
implemented in two independent ways and agree in all 36 cases. These are proofs
and checks supplied here, with no priority claim. The literal finite commutant task
is elementary linear algebra, classified E; no open problem is manufactured to
justify its explanatory development. A separate compactly supported SU(2) example
checks the documented flaw in the energy-representation argument, without claiming
to resolve irreducibility.

\noindent\textbf{Continuity and corrections.}
The earlier occurrence index supplies links to exterior-module descriptions of
projective bundles, combinatorial Pontryagin classes, continuum confinement, and
the preceding year's integrable-system discussions. A common topic is not enough
to merge two problems with different quantifiers. The COUNTCO corrections distinguish
notebook errors faithfully transcribed, unresolved readings, and provenance
discrepancies. In particular the adjacent-year
spillover, the October date, regulator signs, normalized Wilson traces, and the
Pontryagin construction's low-dimensional cases must remain visible to a reader.
The report gives the counting rules, evidence limits, search record and website
presentation recommendations.
'''
replace={'COUNTITEMS':len(items),'COUNTPROBLEMS':len(problems),'COUNTREFS':len(refs),
         'COUNTCO':len(corrections),**{'COUNT'+c:classes[c] for c in 'ABCDEF'}}
for key,value in replace.items(): overview=overview.replace(key,str(value))
(D/'GY1979_overview.tex').write_text(overview)

class_def={'A':'Published soon after by the speaker or Gelfand',
'B':'Developed by others into established results',
'C':'Partly developed; exact remaining scope and evidence limits stated',
'D':'Not developed after a documented search',
'E':'Known before the talk; exposition or established method',
'F':'The mathematical claim or intended reference cannot be identified sufficiently'}

lines=[
'# GY1979 report: the academic year 1979–80',
'',
'**Assessment date:** 10 November 2026. **Deliverable:** the seven prescribed chapter data files, the generated chapter, a compiled stand-alone PDF, this report, and reproducible code with output.',
'',
'## 1. Coverage and counting decisions',
'',
f'All **27 records (462–488)** are present. The chapter contains **{len(items)} mathematical occurrences**, **{len(problems)} problem threads**, **{len(refs)} distinct bibliography entries**, and **{len(corrections)} corrections or provenance annotations.** Records remain identifiable by the original catalog numbers, including the non-talk heading 481. Source order, rather than numeric record order, places 477 before 476.',
'',
'The supplied 79 scans are a page envelope, not 79 pages belonging wholly to this academic year. P000840 continues material already indexed as 1978-460.12 through 1978-460.20. P000917 explicitly starts 22 September 1980; P000918 continues that later session. These boundary pages are inventoried but are not relabeled as Kallosh or Zakharov talks. Newly counted 1979–80 items are supported by P000841–P000916. The supplied transcript also ends with a wrapper for a following page; it contains no additional current-year mathematical occurrence.',
'',
'The critical date for Batalin record 473 is 1979-10-29: the scan reads 29/X-79. The supplied catalog date 1979-09-29 is retained in the provenance correction. This is a correction of identification, not a chronological reordering of the source. The catalog and manuscript disagreement over Shabat’s initial is likewise visible rather than silently harmonized.',
'',
'An item is a distinct definition, construction, proposition, method, question, or mathematically meaningful intervention. A computation illustrating the immediately preceding construction is separated when it checks a substantive sign or hypothesis. The same theorem restated at another meeting is a new occurrence, but a repeated boundary page is not. Bare reading-list names remain in summaries. Conference reports containing an identifiable mathematical assertion or an underdetermined claim are preserved as items; 462.2--4 are deliberately class F when a precise result cannot be recovered.',
'',
'### Items by class',
'',
'| Class | Count | Meaning |',
'|---|---:|---|']
for c in 'ABCDEF': lines.append(f'| {c} | {classes[c]} | {class_def[c]} |')
lines += ['',
'These counts are generated from the delivered JSON, not estimated from prose. The underlying assessment fields are deliberately independent: a class E occurrence can contain a false literal statement, while a corrected modern statement is an established theorem. A partial publication match is not promoted to an exact match merely because the subject and author coincide.',
'',
'### Items and records by catalogued speaker',
'',
'This table uses the enclosing record’s catalogued speaker so that every item is counted once. Explicit interventions can instead be recovered from the optional item-level `speaker` field; those counts follow separately. The heading contributes a record and zero mathematical items.',
'',
'| Speaker | Records | Items |','|---|---:|---:|']
for s in sorted(speaker_records):
    count=speaker_items.get(s,0) if s!='(catalog heading)' else 0
    lines.append(f'| {s} | {speaker_records[s]} | {count} |')
lines += ['', '### Counts using explicit intervention attribution', '',
          '| Speaker or unresolved source attribution | Items |','|---|---:|']
for s,n in sorted(attributed.items()): lines.append(f'| {s} | {n} |')
lines += ['', '### Items by primary area', '',
'Each occurrence receives one primary area solely for this table. Mixed topics are not counted twice. The transparent mapping is preserved in `code/area_assignments.csv`; the mathematical statements, rather than this reporting convenience, remain authoritative.', '',
'| Primary area | Items |','|---|---:|']
for s,n in sorted(areas.items()):lines.append(f'| {s} | {n} |')
lines += ['', '### Evidence and correction profiles', '',
'| Verification level | Items |','|---|---:|']
for s,n in sorted(Counter(x['verification'] for x in items).items()):lines.append(f'| {s} | {n} |')
lines += ['', '| Correction type | Entries |','|---|---:|']
for s,n in sorted(Counter(x['type'] for x in corrections).items()):lines.append(f'| {s} | {n} |')

lines += ['',
'## 2. Principal findings',
'',
'### A mathematical field-theory course within the seminar',
'',
'The long Kallosh–Batalin sequence contains substantial exposition: action principles, constraints, Poisson brackets, local gauge slices, Faddeev–Popov determinants, ghost integrals and BRST identities. Its historical interest lies partly in how carefully these ideas were translated into the seminar’s mathematical language. An on-shell invariance assertion is not an off-shell theorem, a local slice is not a global gauge section, and a finite-dimensional stationary-phase formula is not a definition of a continuum functional integral. These distinctions control both the literal-correctness and publication-match fields. The later BV antifield formalism is used only where an exact identifiable refinement warrants the link.',
'',
'### Exact chronology changes several classifications',
'',
'The source checks distinguish MacPherson’s already circulated/published combinatorial characteristic-class material from later Gelfand–MacPherson dilogarithmic developments. Beilinson’s regulator is matched to a specific 1980 note, including its local formula and lemma, rather than to the much broader later conjectural regulator programme. Olshanskii’s earlier completion/topology results are separated from the 1980 exhaustion and construction theorems. Zakharov’s hydrodynamic reinterpretation is compared with the submitted/published 1979–81 papers rather than assigned to the older Benney chain in its entirety. The corresponding item entries give the primary citations and locators.',
'',
'A final archival check recovered the original Zakharov–Schulman 1980 paper. Its page 193 contains the exact difference-curve parametrization and credits the general example to Manakov through private communication. The 1980 kinetic obstruction is distinguished from the stronger Hamiltonian theorem proved in 1988, whose authors identify a brief 1985 announcement. Accordingly, the combined occurrence 463.6 retains A for its contemporary kinetic content but has a partial publication match for the stronger modern reconstruction. The final evidence note supersedes the early batch’s metadata-only access record.',
'',
'### Open or incompletely identified questions are not interchangeable',
'',
'The confinement thread links a precise pure-gauge static-potential problem to earlier occurrences; strong-coupling lattice results, two-dimensional models, large-rank closure, a four-dimensional continuum construction, and a static area law are different assertions. The two-dimensional energy representation is another case where a published proof claim cannot simply be counted as a solution: later primary papers by Hasebe and Ando identify a specific noncommutative differential identity used incorrectly. No Shimada erratum or successful repair is asserted. The chapter reports what the checked literature establishes and does not turn a failure to find a newer paper into proof of global openness.',
'',
'### The bounded development',
'',
'Berezin’s normal-form problem is treated retrospectively through a faithful regular representation of the finite-dimensional even supermatrix algebra. Sergeichuk’s canonical matrix-algebra theorem then applies. The constructive reduction is proved in the chapter. A separate three-generator example contains arbitrary matrix pairs under simultaneous similarity, explaining why a short Jordan-like list is a stronger demand. The dual-number case with semisimple body is solved explicitly. These arguments do not equate wildness with absence of canonical forms (Sergeichuk, 2000, Theorems 1.1 and 1.3; Belitskii & Sergeichuk, 2003, §1).',
'',
'For Berezin’s second problem, expanding exterior coefficients gives a complete finite linear system for every fixed matrix size and generator number. The chapter goes further for every odd 2×2 matrix over four Grassmann generators, including arbitrary cubic coefficients. After removing scalar coefficients, the rank of the span of the linear traceless coefficients controls the cases. The possible even-commutant dimensions are **17, 20, 23, 24, 29, 30, and 32**. All cases have complete parametrizations and proofs. This is a development proved here; no worldwide priority claim is made. In particular, lack of an exact historical publication match is not represented as proof that elementary finite solvability was unknown.',
'',
'The two independent exact implementations agree on 36 examples, including generator changes and nilpotent as well as semisimple degeneracies. Every kernel vector was substituted into the original equation. Closure was checked for all 1,706 ordered products of basis vectors in three representative cases. The computation tests the proof’s signs and exceptional cases; it does not replace a proof for all matrices. A further independent mathematical review is recorded in the accompanying review file.',
'',
'The final development subsection supplies an explicit compactly supported SU(2) counterexample to the differential identity used in the flawed energy-representation proof. Direct differentiation and an independently integrated conjugation formula agree at two points. This confirms an already documented obstruction to that argument; it is not a counterexample to irreducibility or a claimed new result. The source question remains classified C with its exact evidence limits.',
'',
'The annotated Fourier exercises and the sphere heat-coefficient counterexample also have saved independent checks. A saddle-centered finite-interval calculation reproduces the highly oscillatory quartic integral, while an analytic tail bound controls the discarded contour tails; the quadrature itself remains uncertified. The sphere value is checked by a separate spectral/Hurwitz-zeta derivation. The detailed reviews distinguish these computations from literature verification. For the two quartic exercises without an assigned publication, `publication_match` is `none found` and `verification` is `indirect`; the actual verification is the disclosed derivation and independent computation, a distinction the current enum does not express directly.',
'',
'## 3. What was difficult, and which searches worked',
'',
'The first difficulty was provenance. Several catalog page ranges overlap neighboring talks; the academic-year envelope crosses both ends of the year; numeric record order differs from the handwritten order; and a Roman numeral month was catalogued incorrectly. Mathematical reconstruction before resolving these boundaries would attach the wrong theorem or speaker to a record. The page inventory, talk summaries, and provenance corrections therefore precede any inference about novelty.',
'',
'The second difficulty was precise matching. A title search for “supergravity,” “dilogarithm,” “Grassmannian,” or “loop equations” produces adjacent literature much more readily than it produces the exact assertion. Effective searches used an equation, a named construction, a journal/year hint in the notes, or a backward reference in a later primary paper. Math-Net metadata and short original Soviet papers were especially useful for Beilinson, Olshanskii and Zakharov. Numdam’s full Bourbaki text resolved the earlier circulation of MacPherson’s combinatorial construction. Author-hosted and arXiv copies made theorem and equation checks possible where publisher pages supplied only abstracts.',
'',
'The third difficulty was controlling formal physics. Statements about functional integration, perturbative unitarity, field-dependent BRST transformations, normalized traces, or confinement become different claims when hypotheses are supplied. The chapter identifies added assumptions as reconstruction. It preserves faithful mathematical errors in the notes as evidence, then gives the corrected statement separately. It does not rewrite a phenomenological picture as a rigorous existence theorem.',
'',
'The research logs retain actual queries, opened URLs, the portion read, and the inference allowed. Some attempted links were inaccessible; those attempts are not counted as result verification. A bibliography entry marked `verified` means its cited URL/DOI or primary record was actually opened, not that the entire work was proved correct or read. The per-item `verification` field and the evidence log are the stronger guide. Older cumulative keys were reused wherever the work was already present. Repository deposit dates are distinguished from preprint circulation and journal publication when the checked source permits this.',
'',
'## 4. What the A–F classes miss this year',
'',
'A single historical-fate letter cannot express five independent questions: whether the notebook’s literal words are correct; whether the object can be identified; whether an exact later theorem applies; whether there is evidence of historical influence; and whether a remaining question is mathematically well posed. This is especially visible in the commutant problem. Its finite coefficient-kernel interpretation is elementary and is classified E; its small-rank structure is developed here; and the intended stronger structural form of an answer is not specified by the notebook. An unsuccessful search for historical attribution does not convert this into class C. The explanatory development illustrates the exact finite task without claiming that its particular formulas were already published before the seminar.',
'',
'Class E also includes both established mathematics and conventional formal perturbative methods. The latter’s hypotheses and mode of interpretation must remain visible. Class B can record an exact application of a general later theorem without evidence that the author was answering this seminar question. Class F is a limit of identification, not a negative judgment on the speaker. No D classification is justified merely by missing a search hit.',
'',
'Class A can also conceal different dates within an expanded modern statement: the 1980 kinetic resonance criterion and the 1988 general Hamiltonian result must be dated separately. The schema has no dedicated class for a substantially later theorem by the same speaker. This chapter preserves the prescribed letters and explains that mismatch explicitly, rather than moving the later theorem into an earlier publication by implication.',
'',
'Recommended extensions, without changing this delivery’s required schema, are `resolution_origin` (literature / reconstruction / proved_here), `status_scope` (exact / restricted / formal / unverified_current), and a separate `historical_link` field (documented / inferred / unknown). For sources, machine-readable `opened_at`, `verified_scope`, and `result_locator` would make the difference between metadata and a read theorem searchable. For dating, separate `catalog_date` and `critical_date`, with a reason and source region. None of these should replace the existing assessment fields.',
'',
'## 5. Problem links across years',
'',
'The delivered problem index retains older identifiers when the earlier index supports identity of the question, rather than inventing a new problem number for its return. Exterior-module descriptions of projective bundles, continuum confinement, and combinatorial characteristic classes provide important continuity. The earlier index supplies titles and occurrence IDs, not the complete earlier chapters; links based on it are therefore not represented as a new independent rereading of those earlier scans. A common mathematical area alone does not justify merging problems. Restricted variants and proposed methods are identified as such in the statements and status paragraphs.',
'',
'For a future schema, an occurrence-to-problem relation should explicitly distinguish `same_statement`, `restricted_case`, `method_for`, and `related_only`. This would prevent a large-rank loop-equation method from silently replacing a finite-rank confinement question, or a classification of bundles in a derived category from being mistaken for a finite list of isomorphism classes.',
'',
'## 6. Presentation on the companion website',
'',
'A reader entering a talk should first see its critical identification, a short mathematical summary, and the item list. The identification must show any catalog/manuscript discrepancy and the actual source segments. The first useful click from an item is its source page together with the short notebook statement; the second is the precise modern formulation and what was reconstructed. Fate and dated status should remain adjacent, with exact source locators and an immediately visible verification level. The class letter is a filter and orientation aid, not the principal answer.',
'',
'For this year, the essential paths are the Batalin/Kallosh gauge-quantization sequence; Berezin → the two matrix developments and the exterior-module/bundle thread; Gelfand’s dilogarithm list → Beilinson’s regulator and MacPherson’s later dilogarithm construction; Migdal/Kobzarev → the earlier confinement problem; and the two-dimensional energy representation → the published claim and its documented flaw. Boundary pages should lead to the adjacent year and display “not counted in this year” rather than appearing as unexplained omissions. A source-order view and a calendar-order view should be separate choices.',
'',
'The existing data provide talk/item/problem IDs, citations, statements and assessments. Useful added fields would be `source_segments` (page plus region or line range), `catalog_identity`, `critical_identity`, `related_items` with relation type, and structured reference verification records. Search should index normalized mathematical names and transliterations alongside the original Russian quotations and LaTeX source. The interface should let readers filter “literal error,” “missing hypotheses,” “exact publication match,” and “result read,” independently of A–F. The current JSON is kept compatible with the supplied builder; these are schema proposals rather than undeclared required fields.',
'',
'## 7. Rebuilding and verification',
'',
'The supplied `build_chapter.py` and `gelfand_companion.sty` are included. From the archive directory run:',
'',
'```bash',
'python build_chapter.py GY1979',
'xelatex GY1979_test',
'bibtex GY1979_test',
'xelatex GY1979_test',
'xelatex GY1979_test',
'```',
'',
'`python code/build_all.py` performs the same build with the independent data audit. On a host that has TeX sources but no format/database files, it creates a local XeLaTeX format without modifying the system installation. The numerical-algebra checks can be rerun with:',
'',
'```bash',
'python code/verify_berezin.py > code/verify_berezin_output.json',
'```',
'',
'The final audit checks record completeness, source-order exceptions, sequential IDs, mandatory fields and allowed values, bibliography membership, current-year/older-year distinction, problem back-links, source boundaries, dated status fields, corrections, and unresolved placeholders. Build logs, the audit output, proof-review notes, and the visual-QA report are included. The complete final validation results are recorded in those files. The original input attachments are not required to rebuild the chapter from the seven delivered data files; they are needed only to repeat the independent scan/transcription audit.',
'']
(D/'GY1979_report.md').write_text('\n'.join(lines))
print(json.dumps({'items':len(items),'class_counts':dict(classes),'areas':dict(areas),
                  'report_words':len(' '.join(lines).split()),
                  'overview_words':len(overview.split())},indent=2))
