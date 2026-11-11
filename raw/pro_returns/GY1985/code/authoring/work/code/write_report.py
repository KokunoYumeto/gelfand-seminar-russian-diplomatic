"""Generate the report from the actual merged data, avoiding hand-count drift."""
import json
from pathlib import Path
W=Path(__file__).resolve().parent.parent;D=W/'deliverable'
s=json.loads((D/'audit/statistics.json').read_text())
def table(pairs,left='Category',right='Items'):
    return '| '+left+' | '+right+' |\n|---|---:|\n'+''.join('| '+str(k)+' | '+str(v)+' |\n' for k,v in pairs)

text=f'''# GY1985 — Critical companion report

**Evidence and status date: 11 November 2026.**

## 1. Deliverable and coverage

The chapter covers all **{s['records']} requested catalogue records (641–666)**, with **{s['items']} core mathematical items** and **{s['problems']} problem-index entries**. There are 25 talks and one catalogue heading; record 665 intentionally has no mathematical item. The chapter includes the seven required data/LaTeX/bibliography files, the built chapter and XeLaTeX PDF, the supplied builder and style, this report, computational code with its output, and a source/provenance audit. The final two supplied leaves are discussed in a separate adjacent-record supplement; its {s['adjacent_items']} items are excluded from all core counts below.

The 61 original scans were inspected across the three research groups and the integrating review, with the diplomatic Russian controlling doubtful English readings. The page coverage is P001199–P001259. Core attribution ends at P001257. The two later leaves begin explicit Kontsevich and Morozov headings; treating them as part of Beilinson's record 666 would misattribute their mathematics. They are preserved with ADJ identifiers, not extra entries in the requested 26-record core.

The normalized source order is:

641, 642, 643, 644, 646, 645, 647, 648, 649, 650, 651, 653, 652, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666.

This differs from numerical order where the physical manuscript does. A heading can interrupt another talk on a shared page; a flat inclusive page interval does not identify ownership adequately.

## 2. Counts

### By class

'''
text+=table(s['by_class'].items(),'Class')
text+='''
A means a direct subsequent publication by the speaker or Gelfand; B means development by others; C means partial development with a specified remaining question; D would require a defensible negative literature finding; E means prior knowledge or circulation; F means that the exact mathematical assertion or its fate cannot be identified. These are occurrence counts. They do not measure a speaker's originality, and a recurrence is not deduplicated into a single historical theorem.

### By principal speaker

'''+table(s['by_primary_speaker'].items(),'Principal speaker')
text+='''
Each occurrence is counted once under the record's principal speaker. The talk summaries and item-level `speaker` fields retain interventions by Gelfand, Beilinson, Belavin, Feigin and others. In particular, these totals must not be read as attribution of every theorem to the speaker whose meeting record contains it.

### By primary mathematical area

'''+table(s['by_area'].items(),'Primary area')
text+='''
Areas are a mutually exclusive reporting classification at the talk level. For example, Müller's mixed cusp/arithmetic material is counted with spectral geometry; the explicit record-to-area mapping is in `audit/statistics.json`. Cross-topic items remain searchable by their statements and references rather than being counted twice.

### By record

'''+table(s['by_record'].items(),'Record')
text+='''
### Assessment and correction counts

'''+table(s['literal_correctness'].items(),'Literal statement')+'\n'+table(s['verification'].items(),'Verification level')+'\n'+table(s['correction_type'].items(),'Correction type','Rows')
text+=f'''
The correction ledger has **{s['corrections']} rows**. A row can record provenance or a necessary qualification rather than a character substitution, and several rows can concern one item. Most repairs concern mathematics faithfully recorded in the notebook. They are therefore not described as OCR or translation mistakes. The unusually large “missing hypotheses” and “false as written” counts reflect literal examination of working notes, not a claim that the speakers endorsed those sentences as publication-ready theorems.

The bibliography has **{s['references']} unique entries**. Every bibliography `verified` marker refers to an actually opened URL or DOI. It does not certify that a full original proof was available. Each item records its verification level; bibliography annotations and source ledgers state the exact section, theorem, formula or metadata checked. Duplicate current entries were merged by key; cumulative keys were retained. The merge audit records the decisions.

## 3. What the research established

The principal line is the relation between string Gaussian determinants, moduli geometry, Virasoro representations and oscillator constructions. Its core was already in print or circulation before these talks. Publication year alone would misclassify Witten's ten-dimensional construction, circulated in May 1985 but published in 1986, and Connes's June 1985 Bourbaki lecture, printed in 1986. The first-circulation evidence is given separately in the items and bibliography.

Several exact identifications nevertheless explain the seminar's contemporary research content. Kapranov–Manin's 1986 paper contains the higher-dimensional Baker-function construction (section 3). Ryzhikova's 1987 Doklady note contains the dimension reduction and the decision theorem announced in record 653. Beilinson–Manin's 1986 article identifies the speaker's direct subsequent Mumford-form work. The last identification is verified at the publisher abstract/metadata level; the detailed geometric statement is checked in the accessible Belavin–Knizhnik paper and Bost's Bourbaki exposition. No inaccessible proof is represented as read.

Arnold's discussion leads to a definite uniform-zero question for first Abelian periods. Binyamini, Novikov, and Yakovenko's theorem supplies an explicit finite degree-dependent bound (2008 preprint, 2010 publication). This does not solve the full sixteenth Hilbert problem or automatically cover higher-order perturbation coefficients. Similarly, Vigneras's announced construction is an important precursor of the full local GSp(4) correspondence; Gan and Takeda's Main Theorem and section 11 explain the later complete scope and the limitations of the earlier work. The chapter matches quantifiers rather than treating a shared topic as an exact solution.

Novikov's periodic Schrödinger construction is substantially the 1976 and 1984 theory. The manuscript's derivatives and gauge conventions require correction, but they do not conceal an undeveloped hierarchy. The fixed-energy Manakov triple is rigorously separated from ordinary Lax evolution and whole-spectrum isospectrality. A fully explicit smooth two-soliton reduction refutes the unrestricted sentence that ordinary Lax pairs give only Euclidean motions. This does not refute a more narrowly stated genuinely two-dimensional obstruction, because no such hypothesis is supplied in the notes.

The determinant-line sequence is especially instructive. Record 655's division by the determinant is consistent with its cohomological determinant convention. Record 666 later multiplies by the spectral factor while using the same line convention. Quillen's original uses the dual line. The finite-dimensional determinant-of-complex isomorphism fixes the reciprocal unambiguously; it is not a matter of choosing whichever formula appears more often. The companion also distinguishes flat curvature, a global trivialization, holonomy, and the remaining normalization constant.

## 4. Stage 2 selection and its exact scope

There are two C items and no D items.

**GP-1985-04, arithmetic occurrence and multiplicity in the automorphic spectrum**, is genuinely broader than the already established spectral decomposition by Eisenstein series. Arthur's orthogonal/symplectic classifications are substantial partial solutions for specified groups. The notebook chooses no group, packet or obstruction, so it supplies no plausible bounded contribution for this chapter. The decision to defer development is explicit and does not reclassify established harmonic analysis as open.

**GP-1985-42, simplicial four-polytope realization-space universality**, is the selected development. The manuscript's hedged “more or less any” topology is not an exact stable-equivalence statement. The chapter separates an editorial homotopy formulation from Adiprasito and Padrol's stronger neighborly-four-polytope conjecture. General four-polytope universality and simplicial universality with growing dimension are distinct theorems. Adiprasito and Padrol also explain why earlier proofs of the variable-dimensional simplicial statement were incomplete; an early announcement is kept separate from the later proof.

The contribution is an explicit certificate for a restricted family: a prescribed finite history of facet stackings on a fixed labelled simplex. The insertion region is nonempty, open and convex. A continuous inward-normal/barycenter construction gives a global section with a quantitative strict-slack estimate. Linear interpolation within each fiber is a strong deformation retraction; induction contracts the normalized history space. A second derivation avoids square roots and gives rational insertion points. The chapter additionally proves that nonempty simplicial realization spaces contain rational points and explains why this obstructs stable equivalence to arbitrary non-open primary sets such as the positive root of t²−2.

These are complete proofs. They do not claim novelty for the known contractibility of stacked-polytope realization spaces. They do not assert that every realization of the final combinatorial type admits the chosen deletion history, and they do not identify the fixed affine-frame model with the literature's homogenized quotient model without qualification. The next bounded step is a specified last-vertex deletion test for one small labelled final type, not a claim that finitely many examples establish universality.

As of the stated date, no resolution of the fixed-dimensional simplicial question was found in the bounded search. The latest opened explicit open-status source is the 2024 compendium, entries CG68–CG69. A 2026 search lead about noncontractible realization spaces was inaccessible in full and is logged as unverified; it is not used to assert a theorem or to imply that the earlier search was exhaustive.

## 5. Mathematical checks and second review

Every supplied proof and substantive editorial computation received a second derivation, independent implementation or independent review. The archive contains the scripts and their actual outputs.

- The root checking script computes the Novikov–Veselov commutator by a general Leibniz coefficient algebra, then independently applies the operators to unrelated polynomials for two potentials. All positive-order coefficients cancel with the reconstructed auxiliary equations.
- The KdV reduction is checked by both coefficient algebra and direct action. The explicit positive two-soliton tau function is checked by a rational PDE identity and a separate Hirota-bilinear argument. An independent moment/cumulant implementation gives the two unequal velocity ratios −92/3 and −89524/4861 at the same time, excluding translations.
- Baker–Akhiezer asymptotics are checked independently at both punctures; the reality sign is rederived from conjugation and uniqueness. A reviewer reopened the 1976 and 1984 originals rather than trusting a retyped isolated formula.
- The hyperelliptic product defect is proved using local orders, involution parity and Riemann–Roch. The boundary genus 2 case and genera 2–9 are also checked exactly. The Quillen reciprocal is checked by an acyclic scalar map and a general singular-value proof. The Beltrami wedge is checked in real and complex coordinates. The Todd coefficient is expanded independently, and the torus area scaling is checked against the opened determinant formula.
- Four exact rational stacking histories cover dimensions 2, 3, 4, with two different four-dimensional histories and 14 insertion steps in total. At each step all supporting facets are independently enumerated from vertex subsets, rather than assumed from the stacking update rule. Strict inequalities are verified at four interpolation parameters. This checks the implementation; the general contraction theorem is proved symbolically.
- The early-record script checks Jacobian quotients, q-series coefficients through degree 32 with shorter repeated runs, all 256 eight-bit partition encodings at all 9 gaps, the four-cube section, and the 2-adic expansion. Independent methods are recorded in its output and notes.
- The oscillator/Schubert script checks the Vandermonde normalization for n=2,3,4, divided-difference relations, the Sugawara vacuum coefficient in dimensions 1, 2, 26, the vertex creation coefficient for six frequencies, 25 Laurent-mode coefficient cases, and the zero-momentum exception. Its finite scope is explicit.

The second editorial review caught a missing minus sign in the logarithmic Gaussian action variation and a missing compactness hypothesis in the canonical-curve statement; both were corrected before the final build. An initially inefficient symbolic differentiation was interrupted and replaced by exact rational cancellation after each derivative. This altered performance only; both independent mathematical identities agree.

## 6. Provenance, difficult readings, and limitations

The main source-criticism difficulty is that catalogue page ranges overlap and do not track speaker changes. P001217 records Ryzhikova above Fuchs and reads 21/X/85; the catalogue says 21 September. The chapter uses 21 October 1985 and retains the conflict in the ledger. The Kontsevich leaf reads 24 February 85, the Morozov leaf 24 February 86, and the catalogue lists both under 24 February 87. Monday-calendar agreement supports 1986 as a contextual inference, not as the literal date on both leaves. The adjacent supplement retains each reading.

The archive's all-links index was opened and its date/speaker sequence checked. The supplied `record-<number>.html` endpoints were not reliably retrievable in this environment. Their original links remain in the provided style for compatibility; the report does not pretend that clicking them verifies the scan boundaries. The attached images provide that evidence. A production website should use tested scan URLs, with page-part anchors, rather than deriving every link from the record number.

The most difficult formula issues were the mutually dependent vertex-mode conventions, the two dual determinant lines, metric/area normalizations, and derivative placements in the Schrödinger equations. In each case a literal transcription error was distinguished from a faithful mathematical error. Where the notebook did not determine a convention, the ambiguity is preserved rather than silently filled from a convenient source.

Searches used exact Russian and English titles, Math-Net issue records and full texts, author-hosted papers and bibliographies, journal publisher metadata, Numdam, arXiv, and references followed backwards from later primary papers. Google Scholar/zbMATH leads were not treated as theorem verification. Some publisher or archive endpoints returned access failures or challenges, notably the Beilinson–Manin full text, some Knizhnik material, and Müller's exact cusp L-value source. The selected verification level remains metadata-only in those cases. The source ledgers record successful and failed endpoints separately.

F does not mean that a mathematical topic is unexplored. It can mean an incomplete diagram, an unspecified energy/domain, a slogan about convergence, an unidentifiable coefficient, or a vague analogy. The 23 F occurrences do not support an orphan-idea conclusion. Conversely, the absence of D is not a theorem that every conceivable idea in the notes has been developed; it is the result of refusing to turn missing quantifiers or a weak search into a definite negative finding.

## 7. Earlier-year links and the website

The supplied earlier index ends with the 1982 academic year. The chapter links earlier Baker functions, twistor constructions, Clifford algebras, partitions, modular lattices, Jacobians and Virasoro modules only where the supplied identifiers support the connection. The exact reducibility question reuses **GP-1982-03**, including occurrence 1982-566.7. Related automorphy questions GP-1982-42/43 and lattice representability GP-1973-30 are contextual neighbors, not falsely merged recurrences.

A reader arriving at a talk should first see its true page parts and the distinction between the notebook sentence and the corrected precise statement. The most useful next link is often the exact theorem locator in the publication, followed by the problem's present status. On the string sequence, readers need to follow the determinant-line convention from 655 to 666 and the oscillator convention across 657, 659, 660 and 662. On Vershik's talk, they need an immediate distinction between general four-polytopes, simplicial polytopes in varying dimension, and simplicial four-polytopes.

The existing schema should remain stable for this delivery. A future compatible extension would add:

1. **Structured source spans:** page ID, upper/middle/lower region, and continuation/intervention ownership, allowing discontinuous spans.
2. **Date provenance:** catalogue date, literal manuscript date, normalized date, inference confidence, and evidence type.
3. **Separate chronology fields:** first manuscript/circulation date, received date, online publication and printed issue date.
4. **Result-level evidence:** source key plus theorem/section/formula locator, verified version, verification date, and access scope. A work-level Boolean is too coarse.
5. **Typed links:** exact recurrence, historical precursor, contextual relation, corrected formulation, and later partial result. Only exact recurrence should merge problem IDs.
6. **Normalization metadata:** determinant-line dual, central-generator sign, mode indexing, area convention and realization-space quotient. These affect the mathematics, not just the typography.
7. **Correction identity:** a stable correction ID linked directly to the affected item, with faithful mathematical error visibly distinct from transcription and translation.

The date selector should not reorder the source automatically. The two orderings should be explicit views. ADJ entries should carry a visible boundary flag and remain excluded from the year's core statistics until the catalogue assignment is resolved in a later chapter.

## 8. Building and audit files

The chapter was assembled from reviewed JSON, with unique consecutive item IDs, complete record coverage, checked problem occurrences, cumulative bibliography-key reuse, and citation-to-reference validation. The supplied Python builder produces `GY1985_chapter.tex` and the standalone test driver. The required sequence is:

```bash
python build_chapter.py GY1985
xelatex GY1985_test
bibtex GY1985_test
xelatex GY1985_test
xelatex GY1985_test
```

The archive also includes `code/rebuild.sh`, the completed mathematical checking outputs, source and review notes under `audit/`, the final validation output, and build logs. The rendering uses the supplied common style and author–year bibliography conventions so this chapter remains compatible with the reader. Local TeX installation repairs, if required in the execution environment, are recorded separately from the mathematical content; they do not change the seven-file schema.

The original scans and entire third-party research papers are not duplicated in this archive. The attached primary inputs remain the source witnesses, and the bibliography supplies verified publication URLs. The item data, proofs, corrections and report are self-contained for review.
'''
(D/'GY1985_report.md').write_text(text)
print(json.dumps({'report_words':len(text.split()),'core_items':s['items'],'references':s['references'],'adjacent_items':s['adjacent_items']},indent=2))
