"""Generate the descriptive report and auditable count tables from final data."""
import collections
import csv
import json
import sys
from pathlib import Path
from bibtools import entries, value

ROOT=Path(__file__).resolve().parent
OUT=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'final'/'GY1981'
T=json.loads((OUT/'GY1981_talks.json').read_text())
I=json.loads((OUT/'GY1981_items.json').read_text())
P=json.loads((OUT/'GY1981_problems.json').read_text())
B=entries((OUT/'GY1981_references.bib').read_text())
C=list(csv.DictReader((OUT/'GY1981_corrections.csv').open()))
owner={t['record']:t['speaker'] for t in T}

def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join('---' for _ in headers)+' |']+
                     ['| '+' | '.join(str(x).replace('|','\\|') for x in row)+' |' for row in rows])

text=r'''# GY1981: research, editorial and verification report

**Academic year:** 1981–82. **Assessment date:** 11 November 2026. **Source:** all 30 supplied catalogue records, 530–559, and all 45 manuscript pages, P000981–P001025. The Russian diplomatic transcription is the textual authority; decisive readings and diagrams were checked against the scans. The chapter is an occurrence-based critical companion, not a reconstruction of unrecorded lectures.

## 1. Coverage and counts

There are **210 mathematical occurrences**, **17 problem-index entries**, **93 bibliographic entries**, and **134 correction, ambiguity or provenance entries**. The catalogue contains 26 talk records, two headings, one plan and one separately catalogued intervention. Headings 530 and 545 are retained without invented mathematical occurrences. The brief MacPherson programme has three distinct subjects but remains a plan. Fuchs's intervention remains its own record beside the topology discussion in which it occurs.

The counts below are derived directly from the delivered JSON and CSV by `code/make_report.py`. An occurrence is counted once even when it repeats a result from the preceding week. Consequently these are counts of the notebook's mathematical contents, not counts of independent discoveries.

### By historical class

'''
labels={'A':'Speaker or Gelfand publication soon afterwards','B':'Established subsequent development by others','C':'Partial development with a precise remainder','D':'No development identified','E':'Known before the talk','F':'Exact assertion or fate not identifiable'}
cc=collections.Counter(x['class'] for x in I)
text+=table(['Class','Meaning','Items','Share'],[(k,labels[k],cc[k],f'{100*cc[k]/len(I):.1f}%') for k in 'ABCDEF'])
text+=r'''

Rounded percentages need not total exactly 100%. A class is a historical assessment of the identifiable thread. It is deliberately independent of literal correctness and of how much of a publication was actually read.

### By record and catalogue speaker

The following attribution counts every occurrence under its record owner. Named interventions are separately counted in the next table. Catalogue names and qualifications are preserved; they are not silently converted into assertions that an announced foreign speaker was physically present.

'''
text+=table(['Record','Date','Catalogue speaker','Items','A','B','C','D','E','F'],[
 (t['record'],t['date'] or 'undated',t['speaker'] or 'year heading',
  sum(x['record']==t['record'] for x in I),
  *[sum(x['record']==t['record'] and x['class']==k for x in I) for k in 'ABCDEF']) for t in T])
text+=r'''

### By explicitly attributed speaker

The item-level `speaker` field overrides the catalogue owner where the notebook attributes an intervention. Otherwise the record owner is used. This accounting totals 210 and makes the concentration of Gelfand's interventions visible without erasing the hosts of the talks.

'''
attributed=collections.Counter(x.get('speaker') or owner[x['record']] for x in I)
text+=table(['Speaker or attribution','Items'],sorted(attributed.items(),key=lambda a:(-a[1],a[0])))
text+=r'''

### By area

Each item has exactly one editorial `area` label. These are descriptive labels, not a claim of an established subject ontology; hybrid labels are intentional. The uncollapsed labels below permit the counts to be reproduced without a hidden mapping or double-counting multidisciplinary items.

'''
areas=collections.Counter(x['area'] for x in I)
text+=table(['Area','Items'],sorted(areas.items(),key=lambda a:(-a[1],a[0])))
text+=r'''

### Assessment and correction counts

'''
for field,title in [('literal_correctness','Literal correctness'),('verification','Verification level'),('development','Development assessment')]:
    text+='\n**'+title+'**\n\n'
    text+=table(['Assessment','Items'],collections.Counter(x[field] for x in I).items())+'\n'
text+='\n**Correction types**\n\n'+table(['Type','Entries'],collections.Counter(x['type'] for x in C).items())+'\n'
text+=r'''

The correction log includes 56 mathematical errors faithfully reproduced from the manuscript, 64 ambiguities, 13 provenance clarifications and one translation correction. These are not 134 demonstrated transcription failures. The distinction matters particularly where the scan confirms a wrong formula, an overwritten sign is inconclusive, or a catalogue page window overlaps several actual headings.

## 2. Main findings and warranted developments

### Goldsheid: a negative answer to the sharp question

The original page P001018 specifies the norm of the difference of **orthogonal projectors**. For a Lagrangian n-plane L in the fixed Euclidean symplectic space R^(2n), it asks whether a plane obtained by choosing one line in each prescribed coordinate symplectic two-plane can have gap at most 1/sqrt(2). A separate sentence accepts any dimension-independent constant c<1. Those are different questions, indexed together as GP-1981-40 but assessed separately.

The development proves the exact reduction to approximation of a symmetric unitary S by diagonal unitaries D, with gap ||S−D||/2. An explicit block construction from the three-by-three Fourier matrix gives a real Lagrangian six-plane in R^12 for which **every** such gap is greater than 1/sqrt(2). Every hypothesis is checked. The proof uses positivity with zero diagonal to force incompatible phase equations; it does not depend on numerical optimization.

For every odd m≥3, an m-by-m Fourier block gives the lower bound

\[
\inf_K\|P_{L_m}-P_K\|\geq\frac12\sqrt{2+\sqrt{2-2/\sqrt m}}.
\]

Thus any universal constant must be at least **cos(pi/8) ≈ 0.9238795325**. This estimate excludes every smaller constant, but does not exclude the endpoint. A separate eigenvalue-arc argument proves a fixed-dimension upper bound cos(pi/(2n)); it is sharp at n=2 and tends to one. No uniform upper bound less than one is established. The global literature search found no exact resolution of the weaker question; that retrieval limit is stated explicitly instead of promoting it to a proof of universal nondevelopment.

Mehrmann and Poloni (2012, Theorem 3.4) are a precisely checked neighbouring result: their graph entries have diagonal bound one and off-diagonal bound sqrt(2). Entrywise bounds are not the same as the requested operator-gap estimate. A misleading search extraction of the latter constant was corrected from the full paper. The development does not claim historical priority for its elementary matrix arguments.

### Haefliger: complete continuous solvability, with smooth regularity left open

GP-1981-23 records the exact equation f=u−u∘T+v−v∘S on RP¹, where T(x)=x+1 and S(x)=−1/x. The notebook asks for smooth solutions and separately asserts density in the smooth topology. The chapter proves **exact solvability for continuous functions**, with a uniform-norm existence estimate, and gives an exact averaging reduction of the smooth question.

The proof first rules out a common invariant probability measure: translation invariance forces all mass to infinity, while S sends infinity to zero. Weak-* compactness gives a uniform total-variation defect of invariance. Passing from a signed measure to its total variation transfers that estimate to the full Banach dual. Hahn–Banach separation and a convergent residual series then give surjectivity. An independent closed-range argument checks the same conclusion.

The proof supplies neither derivative estimates nor a smooth right inverse. The smooth dual contains distributions, so the measure argument alone does not verify the source's smooth-density claim. Both smooth assertions remain separate C occurrences. The thematic literature on invariant functionals does not automatically answer this noncompact discrete-group action. No account of why the original problem was allegedly abandoned is invented.

### The other C items

The Regge question GP-1981-21 separates convergence of discrete curvature measures from convergence of solutions of the discrete variational equations. Cheeger, Müller, and Schrader's (1984) theorem, its earlier symposium announcement, and later Einstein-tensor consistency results do not by themselves settle the notebook's solution-convergence question. A missing gauge, topology, boundary problem and stability theorem would need to be fixed before a bounded numerical or analytic research contribution could be certified. The item is retained with that precise limitation rather than developed through an unjustified inference.

GP-1981-22 is the finite-coefficient Friedlander–Milnor comparison. The adjacent Milnor statements are separated into their proved components and their conjectural extension. The renewed 2021 preprint proof claim is recorded without certification; the more general abelian-topological-group results appearing in 2025 are not presented as a solution for all Lie groups. The exact sources and current-status search are documented in the topology log. No general resolution was verified as of the assessment date.

### Important corrections to established mathematics

The root-multiplicity discussion does not justify manufacturing an open demand for a positive formula. A finite recursive lowering algorithm is proved for the maximal-ideal definition of the contragredient algebra; the established symmetrizable multiplicity formula predates the seminar. Independent Serre-ideal calculations check five rank-two cases through height eight. The elementary Gelfand–Tsetlin count is a representation's dimension, not a count of isomorphism classes with one fixed highest weight.

The Jantzen question has a genuine quantifier trap. Dominant directions and arbitrary regular directions are not interchangeable. Williamson's published type-A3 example changes the layer dimensions from (7,3,2,1) to (7,2,4,0). The supplied computation reconstructs the contravariant forms from gl4 commutators and confirms the result through two independent exact linear-algebra procedures. This reproduces an established counterexample; it is not labelled a new C development.

The spring notes omit a product of all edge lengths in converting the Gram-matrix density to an edge-length density. Macdonald's partition identity needs both partition conjugation and inversion of the variable in the recorded specialization. The geometric multiplicity formula omits the quotient of the moment-map level by the torus. The fractional derivative omits its gamma normalization. The div–grad–curl matrix has the wrong sign under conventional operators. The zeta-shift formula omits t^mu in each residue summand. These are mathematically substantive corrections supported by the scans, exact algebra and identified sources.

One additional audit rejected an attractive but false extension: spectral-cut independence at zero does not imply cut independence at every negative integer, even for differential operators. Ponge's (2006) exact cut-difference identity and Loya and Moroianu's (2012) negative eta/absolute-zeta pole discussion separate these issues. The final chapter also gives a fully explicit counterexample: a rank-four massive Dirac operator on the flat three-torus has absolute-zeta residue −2πμ⁴ at −1 and opposite cut-zeta values ∓iπ²μ⁴. Its square, multiplicities, heat coefficient, Mellin residue and branch signs are proved and independently checked. The valid zero-value theorem and precise residue criterion are retained, with the false blanket extension marked as such. The detailed log records the rejected reasoning so that a future editor does not restore it inadvertently.

## 3. Search methods, successes and limitations

The four research logs provide source URLs, exact locators, chronology and failed access routes. Primary full papers were preferred to search snippets. Math-Net was especially effective for short Soviet announcements and received dates. NUMDAM supplied Bourbaki and Astérisque sources with inspectable title pages. Author-hosted originals and bibliographies resolved chronology or theorem details when publisher routes failed. Later primary papers were useful when they stated precisely which earlier result they used; that is recorded as indirect verification of an inaccessible original, not full-text reading.

The highest-value matches include Macdonald's June 1981 Bourbaki exposé; the full Abeasis–Del Fra–Kraft quiver paper; Elashvili's announcement received 30 November 1981, one week after his talk; Cartier's November 1981 exposé published in 1982; Krichever's elliptic-matrix algebra and sigma kernel; Cheeger–Müller–Schrader's curvature convergence; Kashiwara–Schapira's exact contact/microsupport results; McMullen's complete congress article; McDuff's parity statements; Milnor's discrete-group paper; Givental's 1983 announcement; and the APS/Gilkey/Ponge sequence for spectral asymmetry.

Negative searches were strongest when the missing quantifier was made explicit. For Goldsheid they included transliteration variants and the symmetric-unitary formulation. For Haefliger they included modular-group, projective-circle, smooth-coinvariant and invariant-distribution variants in English and French. Lorentz/neutrino, Elashvili's unnamed gamma function, the erased Kac–Moody statement, unspecified characteristic classes and the spectral p-adic analogy remain identification gaps. They are F, not D. A later article sharing a broad subject does not establish an exact fate.

There are **85 entries marked verified** and **eight marked unverified**. “Verified” means the cited URL or DOI route was actually opened; it does not imply that every proof was read. The `annote` field gives the actual inspection scope, while item-level verification distinguishes result reading, metadata, indirect evidence and an unresolved lead. The inaccessible original entries are:

'''
text+=table(['Key','Original-source limitation'],[(e['key'],value(e,'annote')) for e in B if value(e,'note')=='unverified'])
text+=r'''

No citation is silently upgraded because a source was cited in an earlier chapter. Existing bibliography keys are reused; 1,160 cumulative entries representing 941 unique keys were parsed in a brace-aware audit. Exact DOI/title matching found no newly introduced alias requiring replacement. Repeated inherited annotation fields were consolidated without deleting the current-run verification record. Separate original and translation editions remain separate when their dates or pagination differ.

## 4. What the A–F classes miss this year

**Chronology has more than one event.** A receipt date, an oral announcement, a circulated preprint, an online posting and a printed issue are not interchangeable. The Wodzicki 1982 paper was published in February, before the April talks, whereas his fuller 1984 treatment followed them. Atiyah's 1981 receipt and the earlier seminar record precede the 1982 journal paper. The geometric multiplicity preprint is recorded in March before its October 1982 publication. The current data distinguish those events in prose; one A/E letter cannot encode all of them.

**Truth and historical fate are independent.** Many E items are old theorems stated with false signs, missing restrictions or ambiguous conventions. Conversely, an A item may be a partial match to a later paper whose correct theorem does not endorse the literal notebook formula. This is why the explicit correctness and match fields are indispensable. F also has several causes: missing formulation, uncertain attribution, an erased statement, and a real bibliographic pointer that does not specify a theorem. It should not be treated as a low-value bin or as evidence of unsolved mathematics.

**One question can have several topologies or constants.** Haefliger's C0 and C∞ versions, smooth density versus surjectivity, and Goldsheid's sharp versus weak constants must remain linked but distinct. Similarly, Jantzen's dominant-direction theorem and a regular-direction counterexample answer different quantifiers. A website that collapses them into one “solved” badge would materially mislead readers.

**A successful proof here is not a priority claim.** The two bounded developments are marked as proved in this companion and have independent checks. The literature search is expressly limited. Editorial proofs of older results and repairs of faithful errors are labelled verification annotations, even though they use the same `\ours` marker. No C/D quota was imposed: D is empty because no sufficiently specified undeveloped target survived the audit.

## 5. Earlier links and presentation on the website

The problem index reuses **GP-1979-41** for the Kazhdan–Lusztig multiplicity/cohomological thread and retains its earlier occurrences. The primitive-envelope question links to 1964-37.1–2; no previous GP identifier for that exact question was supplied, so a new identifier is used with the old occurrences. Torus convexity points to 1980-508.15. Eta regularity points to 1972-296.2–3 and 1972-296.5. Earlier identifiers are retained as textual cross-chapter targets in the stand-alone PDF, while current-year occurrences are active internal links. The cross-year website can resolve them to their companion pages.

A reader arriving at a talk should first see the short summary, the actual manuscript section and its catalogue attribution. Each item should then show the recorded statement beside the precise hypothesis-complete reconstruction. The correctness, match and verification assessments should remain visible when the fate is expanded; a class letter alone is insufficient. A source-page control should open the scan at the decisive reading, and a separate bibliography control should expose the result locator and inspection scope.

The most useful relation links are: the quiver orbit description to the later p-adic GL(n) multiplicity theorem; Verma modules to the Jantzen direction question and the older KL problem; discrete curvature convergence to the separate Regge-equation problem; Milnor's conjecture to the distinct proved comparison statements; Haefliger's original smooth question to the new continuous theorem and the density caveat; Kirillov's level set to its reduced space; and the two Wodzicki talks to their repeated formulas and corrected spectral conventions. Source order must remain available independently of record number and calendar date.

Recommended optional schema extensions are `source_order`, `actual_page_span`, `catalogue_attribution`, structured `chronology` events, and per-reference `verification_locator`, `verification_date`, and `access_scope`. A typed `relations` list could distinguish repeats, generalizations, corrections, counterexamples and prior occurrences. A `formulation_variant` field would keep sharp/weak, continuous/smooth, and density/exact questions linked without conflating their statuses. The present delivery stays compatible with the supplied schema; prose, optional `speaker`/`area` fields, bibliography annotations and research logs preserve the evidence now.

## 6. Reproducibility and independent checks

Every claimed development was checked a second time by a separate derivation or a genuinely independent computational route. The Goldsheid audit independently reconstructs the symmetric-unitary identity, every phase constraint, the Fourier norm bound, the n=2 endpoint, and the distinction between vectorwise and spanwise approximation. The Haefliger proof was checked both through Hahn–Banach residual approximation and through the Banach closed-range theorem; the transfer from signed to positive measures was explicitly audited. These are mathematical checks, not finite experiments standing in for universal proofs.

The saved exact and numerical checks include:

- primitive necklaces versus the Witt formula in 65 bidegrees, Catalan recurrence through n=12, 210 Gelfand–Tsetlin top rows, 120 quiver interval supports, five rank-two Serre/lowering comparisons through height eight, Euler products through degree 14, and the Schwarz density scaling;
- a 13-dimensional A3 Shapovalov space in three directions, with t-adic elementary divisors checked independently by exact truncated-matrix ranks; Cauchy signs at sizes 1–5; the Rayleigh transformation; a binary-cubic Kirillov pairing; and all 511 sign sequences of length at most eight by two constructions;
- bounded Macdonald-identity enumeration with negative controls and exact Gram/edge Jacobian checks, including a one-dimensional check;
- projector identities with two seeds, dimensions 1, 2, 3, 6 and 9, Fourier sizes 3, 5, 7 and 11, two explicitly uncertified numerical phase searches, exact vector-calculus symbol multiplication, 42 Pochhammer derivative/residue coefficient checks, and the explicit three-torus negative-cut example with all 16 Clifford anticommutators and exact phase limits.

Scripts, outputs and the stated parameter ranges are included under `code/` and `research/`. The initial random Goldsheid exploration is also retained: its apparently favourable samples did not predict the structured counterexample and were never used to prove a universal bound. No numerical optimizer is reported as a certified optimum. No downloaded research PDFs or scan cache is needed to rebuild the chapter; the user-supplied transcriptions and catalogue are the external source inputs for the authoring history.

The delivered build script checks the seven prescribed data files and generates the chapter and stand-alone driver. XeLaTeX, BibTeX, XeLaTeX, XeLaTeX produce the PDF; the build log and final diagnostics are saved. A targeted schema/citation audit additionally checks all enums, consecutive identifiers, bidirectional problem occurrence links, dated statuses, C/D worth statements, bibliography verification markers and LaTeX-special-character hazards. The supplied style is retained with only a spacing repair after the two proof/computation markers. The driver additionally prints all bibliography entries referenced by the data, including indirectly identified originals, through `\nocite{*}`; their verification qualifications remain explicit. A workspace-local TeX environment setup is included for the restricted runtime used here; ordinary complete TeX Live installations can run the standard commands directly.

Final page count, resolved citation/link diagnostics and visual inspection results are recorded in `code/verification/final_quality.json`. The overview occupies two pages of the compiled chapter. The ZIP contains the complete data, report, bibliography, generated chapter, driver, compiled PDF and reproducibility material, with no additional download required.
'''
(OUT/'GY1981_report.md').write_text(text)
print(f'Report written: {len(text.split())} whitespace-delimited words, {len(T)} records, {len(I)} items.')
