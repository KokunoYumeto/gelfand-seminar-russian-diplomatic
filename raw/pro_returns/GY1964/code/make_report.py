"""Generate reproducible counts, the chapter overview, and the editorial report."""
from pathlib import Path
from collections import Counter, defaultdict
import csv
import json
import re
import sys

from assemble_data import bib_entries

WORK = Path(__file__).resolve().parents[1]
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else WORK / 'output'
EVIDENCE = WORK / 'evidence'

AREA = {
 2:'Algebraic geometry and sheaves', 3:'Statistical mechanics and probability',
 4:'Nonlinear evolution and quantum fields',5:'Nonlinear evolution and quantum fields',
 6:'Measure theory',7:'Functional analysis and kernels',8:'Lie groups and rigidity',
 9:'Statistical mechanics and probability',10:'Dynamics and entropy',
 11:'Representation theory',12:'Invariant differential equations',13:'Representation theory',
 14:'Arithmetic groups and equidistribution',15:'Fredholm and elliptic theory',
 16:'Statistical mechanics and probability',17:'Operator theory',
 18:'Geometric optics and quantization',19:'Mathematical statistics',20:'Several complex variables',
 21:'Geometric optics and quantization',22:'Spectral theory',
 24:'Arithmetic groups and equidistribution',25:'Symmetry and mathematical physics',
 26:'Commutative algebra and differential operators',27:'Commutative algebra and differential operators',
 28:'Fredholm and elliptic theory',29:'Fredholm and elliptic theory',30:'Topology and K-theory',
 31:'Commutative algebra and differential operators',32:'Operator theory',33:'Dynamics and entropy',
 34:'Representation theory',35:'Symmetry and mathematical physics',36:'Dynamics and entropy',
 37:'Noncommutative algebra',38:'Noncommutative algebra',39:'Random matrices and symmetric spaces',
 40:'Algebraic geometry and sheaves',41:'Random matrices and symmetric spaces',
 42:'Random matrices and symmetric spaces',43:'Dynamics and entropy',44:'Convex and integral geometry',
 45:'Convex and integral geometry',46:'Random matrices and symmetric spaces',47:'Spectral theory',
 48:'Several complex variables',49:'Algebraic geometry and sheaves',50:'Operator theory',
}
OVERRIDES = {'1964-9.1':'Representation theory','1964-9.4':'Symmetry and mathematical physics',
             '1964-17.2':'Representation theory'}

def table(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+
                     ['| '+' | '.join(map(str,row))+' |' for row in rows])

def field(entry, name):
    m = re.search(r'\b'+name+r'\s*=\s*\{([^}]*)\}',entry,re.I)
    return m.group(1) if m else ''

def main():
    talks=json.loads((OUT/'GY1964_talks.json').read_text())
    items=json.loads((OUT/'GY1964_items.json').read_text())
    problems=json.loads((OUT/'GY1964_problems.json').read_text())
    corrections=list(csv.DictReader((OUT/'GY1964_corrections.csv').open()))
    bib=bib_entries((OUT/'GY1964_references.bib').read_text())
    audit=json.loads((EVIDENCE/'input_audit.json').read_text())
    base={x['id']:x for x in audit['occurrences']}
    classes=Counter(x['class'] for x in items)
    old=Counter(x['class'] for x in base.values())
    verification=Counter(x['verification'] for x in items)
    correctness=Counter(x['literal_correctness'] for x in items)
    match=Counter(x['publication_match'] for x in items)
    confidence=Counter(x['confidence'] for x in items)
    by_record=defaultdict(list)
    talkmap={t['record']:t for t in talks}
    by_speaker=Counter()
    by_area=Counter()
    for x in items:
        by_record[x['record']].append(x)
        by_speaker[talkmap[x['record']]['speaker'] or '(unattributed)']+=1
        by_area[OVERRIDES.get(x['id'],AREA[x['record']])]+=1
    added=[x['id'] for x in items if x['id'] not in base]
    changes=[{'id':x['id'],'old_class':base[x['id']]['class'],'new_class':x['class'],'title':x['title']}
             for x in items if x['id'] in base and base[x['id']]['class']!=x['class']]
    with (EVIDENCE/'baseline_class_changes.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['id','old_class','new_class','title']);w.writeheader();w.writerows(changes)
    with (EVIDENCE/'coverage_by_record.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['record','date','speaker','pages','items','classes'])
        for t in talks:
            c=Counter(x['class'] for x in by_record[t['record']])
            w.writerow([t['record'],t['date'],t['speaker'],t['pages'],len(by_record[t['record']]),
                        '; '.join(f'{k}:{c[k]}' for k in 'ABCDEF' if c[k])])
    with (EVIDENCE/'bibliography_verification.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['key','note','url','doi','item_occurrences','problem_ids'])
        for k,e in bib.items():
            w.writerow([k,field(e,'note'),field(e,'url'),field(e,'doi'),
                        ';'.join(x['id'] for x in items if k in x['refs']),
                        ';'.join(p['id'] for p in problems if k in p['refs'])])
    stats={'status_date':'2026-11-12','records':len(talks),'items':len(items),'problems':len(problems),
           'references':len(bib),'corrections':len(corrections),'classes':dict(classes),
           'baseline_classes':dict(old),'changed_class_count':len(changes),'new_occurrences':added,
           'by_speaker':dict(sorted(by_speaker.items())),'by_area':dict(sorted(by_area.items())),
           'verification':dict(verification),'literal_correctness':dict(correctness),
           'publication_match':dict(match),'confidence':dict(confidence),
           'correction_types':dict(Counter(x['type'] for x in corrections)),
           'bibliography_notes':dict(Counter(field(e,'note') for e in bib.values()))}
    (EVIDENCE/'counts.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
    (EVIDENCE/'area_assignments.json').write_text(json.dumps(
        {x['id']:OVERRIDES.get(x['id'],AREA[x['record']]) for x in items},ensure_ascii=False,indent=2)+'\n')

    class_rows='\n'.join(f'{c}&{classes[c]}&{old[c]}\\\\' for c in 'ABCDEF')
    overview=r'''\nocite{*}
\paragraph{Scope and how to read this chapter.}
This chapter covers all \textbf{RECORDS records} in the supplied 1964--65
catalogue, with \textbf{ITEMS mathematical occurrences}.  All 247 supplied
identifiers are retained; the additional support-of-measure observation
is numbered 1964-6.9.  Dates range from
21 September 1964 to 10 May 1965; the February planning entry is included
without inventing mathematical content.  The sequence follows the supplied
MCCME record order, which is not chronological.  Individual page citations
locate the actual, sometimes interleaved, notebook text.  P000090 starts the
following academic year's Kohn material and is excluded from the present
occurrence count.  Russian transcription is the textual authority; scans
decide consequential doubtful readings.  In each entry, \emph{The notes},
\emph{Statement}, and \emph{Reconstruction} distinguish the record, a precise
modern formulation, and the editor's additions.

\paragraph{The year's mathematical lines.}
The seminar alternates sustained exposition with short announcements and
questions.  Blowups, representation theory, Hilbert kernels, distributions,
Fredholm operators, algebraic jets, and sites supply common language.
Statistical mechanics leads from contour arguments to a walk question;
random matrices lead from circular ensembles to gap probabilities and
spectral traces.  Arnold's geometric optics connects caustics to quantization,
while Novikov's exposition places vector fields on spheres in real
\(K\)-theory.  The final Halmos session collects several decades of
invariant-subspace methods and ends with unusually concrete weighted
operators.  These connections are mathematical and textual; the chapter does
not infer influence merely from two related topics appearing together.

\paragraph{Publication and identification.}
Some announcements have close later matches; others were already published
or circulating.  Dobrushin's phase-separation work requires its correction
as well as the original theorem.  The different-rank Weyl-algebra question
(1964-38.1) has an affirmative distinction through dimension growth; it is
not the fixed-rank endomorphism conjecture.  Sz.-Nagy--Foia\c{s}'s contraction
theorem is available before the Halmos talk, and its linked erratum leaves
that theorem intact.  Domar's later weighted-shift construction resolves the
question of an invariant-subspace chain indexed by all integers, after
adjoining zero and the whole space.  Submission dates are reported as submission dates:
they are not silently identified with first public circulation.  A modern
proof of a recorded idea, such as the Slater-determinant route to Sturm's
theorem, is distinguished from a new theorem discovered in the notebook.

\begin{center}
\begin{tabular}{@{}lrr@{}}\toprule
Class&This chapter&Supplied first run\\\midrule
CLASS_ROWS
\midrule Total&ITEMS&247\\\bottomrule
\end{tabular}
\end{center}
Here A denotes a close subsequent publication by the speaker or Gelfand;
B a later development by others; C a partly settled precise line; D a
searched but undeveloped line; E prior mathematics; and F an identification
the record cannot sustain.  The separate correctness and match fields are
essential: a familiar theorem may be false in the notebook's literal
wording.  E is an expository classification, not a separately audited
priority claim for every assertion: some record-6 entries lack a verified
pre-talk theorem-level publication date, as their fates expressly state.
No absence of a search hit is used as evidence of an orphan idea.

\paragraph{Questions and bounded development.}
The PROBLEMS problem entries include both settled and unresolved questions,
with explicit hypotheses.  The major residual operator questions concern
the Hilbert invariant-subspace problem and Bishop operators.  Weight
classification is reported only to the scope of the verified criteria.
The walk question needs its sampling law specified before a
modern asymptotic question is assigned to it.  Sinai's observation on
spectral multiplicity is not converted into a conjecture absent from the
source.  Recent 2026 claims are reported with their actual verification
level, not treated as accepted resolutions.

One development is provided, for Bishop cyclicity.  It proves rational
cyclicity and a finite-orbit continuity bound, supplies exact approximation
certificates checked by two independent implementations, and derives a
terminating sufficient continued-fraction criterion.  These are bounded
certification and exposition results, not a solution for every irrational
rotation and not a claim of historical novelty; compare
\citet{chamizo2020bishop} and \citet{behani2023bishop}.

\paragraph{Continuity with the supplied index.}
Despite its filename, \texttt{previous\_index.md} contains this same year's
247 first-run items, no earlier-year occurrences, and no existing problem
identifiers.  It is therefore a comparison baseline, not evidence for
cross-year links.  All retained identifiers remain stable; CHANGES class
assignments change after renewed source checking.  Within-year links join
the two invariant-subspace announcements, repeated gap formulas, and the
successive algebraic-jet discussions.  A genuine earlier-year index can be
joined later without fabricating a history that was not supplied.
'''
    for a,b in [('RECORDS',str(len(talks))),('ITEMS',str(len(items))),('PROBLEMS',str(len(problems))),
                ('CHANGES',str(len(changes))),('CLASS_ROWS',class_rows)]: overview=overview.replace(a,b)
    (OUT/'GY1964_overview.tex').write_text(overview)

    report=f'''# GY1964: research and editorial report

**Coverage:** academic year 1964–65, MCCME records 2–50.  
**Status checked through:** 12 November 2026.  
**Deliverable:** a critical companion, occurrence index, problem index, correction ledger, and one bounded mathematical development.

## 1. What the chapter establishes

The chapter contains **{len(talks)} records, {len(items)} mathematical occurrences, {len(problems)} problem entries, {len(bib)} bibliography entries, and {len(corrections)} correction or provenance entries**. All supplied record numbers are represented, including the planning entry. The original 247 occurrence identifiers are retained to make the revision directly comparable with the supplied first run. The added occurrence {', '.join(added)} records the distinct support-of-measure claim on P000015; the baseline's count was not treated as a quota. Counts measure editorially delimited occurrences, not independent discoveries or the productivity of speakers.

The dominant result is clarification. Many entries become reliable statements after specifying a function space, field, regularity assumption, topology, probability law, or quantifier. A publication on the same subject is not automatically an exact match. Conversely, a source fragment that cannot determine a mathematical assertion is not evidence of an undeveloped research programme.

The development concerns Bishop operators. It provides complete proofs of rational cyclicity and the transfer estimate, finite certificates checked by two independent implementations, a computable sufficient continued-fraction condition, and the precise limitation of that condition. Established rational and generic cyclicity results are re-proved for a self-contained certificate method. No novelty claim or universal irrational solution is made.

## 2. Counts and accounting conventions

### Fate classes

{table(['Class','Meaning','First run','This chapter','Change'],[(c,{'A':'Close subsequent publication by speaker/Gelfand','B':'Later development by others','C':'Partly developed, residual question specified','D':'Searched but not developed','E':'Known before the talk','F':'Not identifiable with adequate precision'}[c],old[c],classes[c],f'{classes[c]-old[c]:+d}') for c in 'ABCDEF'])}

There are {len(changes)} changed class assignments. The full item-level comparison is in `evidence/baseline_class_changes.csv`; it should be read with each revised fate, not as an unexplained re-rating. The chapter does not use D merely because a short title search failed. F describes insufficient identification, while C requires an identifiable line and a stated remaining question.

The E count needs a chronology qualification. It classifies material judged to be prior or expository mathematics; it is not a claim that the exact pre-talk publication date of every assertion was independently established. Several record-6 fates explicitly report this limit. Their later expository sources explain the mathematical framework but do not, by themselves, prove historical priority. Confidence and verification fields retain this distinction, and a future chronology audit could revise the provisional E assignments without changing the identified mathematics.

### Items by catalogued speaker

Each occurrence is counted once under its record's catalogued speaker. Jointly attributed records remain joint rows; their items are not duplicated between participants. A named intervention can additionally appear in an item's optional `speaker` field. Thus this table is a catalogue-based allocation, not a claim about individual authorship of every remark.

{table(['Catalogued speaker','Items'],sorted(by_speaker.items()))}

### Items by mathematical area

Every item has exactly one primary area for this count. The assignment is editorial and intentionally permits overlaps in subject matter without double-counting. For example, spectral traces could also be placed in mathematical physics, and rigidity uses cohomology. `evidence/area_assignments.json` records every allocation; these labels do not alter the required item schema.

{table(['Primary area','Items'],sorted(by_area.items()))}

### Independent assessment dimensions

{table(['Literal correctness','Items'],sorted(correctness.items()))}

{table(['Publication match','Items'],sorted(match.items()))}

{table(['Verification level','Items'],sorted(verification.items()))}

{table(['Confidence in identification/fate','Items'],sorted(confidence.items()))}

Bibliography opening status: {', '.join(f"{v} {k}" for k,v in sorted(stats['bibliography_notes'].items()))}. In the required BibTeX field, **verified means that the linked source or DOI was opened**. It does not mean that every proof in that source was independently validated. The occurrence-level verification field and locator carry the stronger distinction. A theorem may be read in an author's primary manuscript while the journal page is accessible only as metadata. A recent preprint can have a verified bibliographic record and an unverified proof.

## 3. Provenance and coverage decisions

The supplied `previous_index.md` is not an index of earlier academic years: it contains the same 247 identifiers beginning with 1964, and no pre-existing problem IDs. The cumulative bibliography contains no usable entries. This is established by the saved input audit, which includes SHA-256 hashes of all six supplied files. No earlier-year occurrence was invented. New problem IDs are local to 1964–65 and can later be reconciled with a real multi-year index.

The chapter preserves records 2–50 in the supplied MCCME order. This order is neither a chronological sort nor a guarantee that every record occupies a disjoint page interval. Preliminary remarks, continuations, and shared pages make the broad catalogue envelopes unsuitable as exact mathematical locators. The talk entry identifies the record; the item entry supplies the actual page citation. The source boundary also matters: P000090 starts Kohn's September 1965 material. It is acknowledged in the correction ledger but excluded from the 1964–65 occurrence count.

The Russian transcription was used to settle the intended wording. Scans were inspected where letters, signs, diagrams, attribution, or layout changed the mathematics. A mathematically implausible formula was not silently corrected merely because a familiar theorem suggested a replacement. The correction table distinguishes transcription, translation, ambiguity, faithful mathematical error, and provenance. A faithful error leaves the diplomatic source intact and places the repaired statement in the critical layer.

## 4. Searches that changed the interpretation

**Phase separation.** Searching Dobrushin's Math-Net record and following its linked short announcement and correction was more effective than relying on a title match. The talk, submission dates, printed theorem, and later repair must be distinguished. The contour argument is a close publication match, but a source's erroneous sign or compressed constant is not validated by that match. The occurrence entries specify which statement is being repaired.

**Entropy.** Kushnirenko's 1965 note supplies a precise hypersurface-expansion estimate and an explicit acknowledgement of Arnold. Its actual theorem and its discussion of examples are different statements. The stronger invertible estimate is justified through a later differential-entropy argument, explicitly identified as an editorial implication; it is not attributed to a line the 1965 paper does not contain.

**Weyl algebras.** The source asks about different numbers of canonical pairs. The relevant distinction is growth dimension, not the fixed-rank Dixmier endomorphism question. This is a useful test of problem matching: changing a quantifier can convert an elementary settled distinction into a famous open problem.

**Fredholm maps and algebraic jets.** Smale's Fredholm-map paper makes a nonlinear index precise at the derivative level. A nonlinear map does not acquire a vector-space kernel and cokernel merely by analogy. The Kazhdan–Palamodov discussions require localization, characteristic assumptions and variable-coefficient differential conditions. Later Noetherian-operator theory supplies a precise framework, but its full modern formulation is marked as reconstruction.

**Spectral multiplicity.** A flow and a single measure-preserving transformation are different objects. The constant functions must be removed when discussing Lebesgue spectrum of an ergodic probability-preserving system. Sinai's source observation about the examples then known is not itself a precisely stated Banach conjecture. The chapter separates a published flow result from a September 2026 claimed transformation result whose theorem statement was inspected but whose proof was not independently verified.

**Invariant subspaces and errata.** The de Branges–Rovnyak announcement is catalogued together with its retraction; both were verified through author bibliographies, without claiming to have read the original announcement or correction. Halmos's polynomially compact theorem is separated from the general problem. The original Sz.-Nagy–Foiaș VIII and IX papers were opened, and the linked 1965 correction was checked: the correction explicitly preserves the invariant-subspace theorem used in the chapter while retracting a different proposition. The library of examples, counterexamples and sufficient hypotheses does not settle the general Hilbert-space problem.

**Bishop operators.** The arithmetic condition in Chamizo et al. concerns existence of hyperinvariant subspaces. The cyclicity results in Béhani concern approximation by a vector orbit. One cyclic vector is not equivalent to absence of proper invariant subspaces; that absence would require every nonzero vector to be cyclic. A 2026 determinant preprint was found as an indexed lead, but its primary endpoints did not open, so it is not used as a theorem. The independently computed interior zero is reported without a novelty claim.

**Unsuccessful or partial identifications.** Several short prompts omit the object or a hypothesis needed for any definite theorem: Boolean products, a quotient algebra for nonlinear equations, numerical symmetry proposals, unspecified growth-controlled division, and a sphere-bundle construction. Searches and related sources are recorded, but thematic resemblance does not justify replacing F by A or B. The logs retain failed access and unresolved leads rather than conceal them.

The research logs in `evidence/` give actual source URLs, query families, receipt/publication distinctions, and whether a theorem, abstract, or only bibliographic metadata was inspected. They are a source trail, not an exhaustive search of every historical archive.

**The integer-chain question.** A backward-reference search from Shkarin's paper led to Domar's 1981 Theorem 2. Its scanned primary pages were rendered and read. The explicit choice of weight w_n = exp(−2 n|n|) meets the logarithmic convexity, concavity, summability, and quadratic-growth hypotheses. Unitary conjugation gives the bounded bilateral shift S e_j = exp(−2|2j+1|)e_(j+1), whose invariant subspaces are exactly the coordinate tails together with zero and the whole space. A second reader independently checked the hypotheses and conjugation. This changes 1964-50.17 from an unresolved identification into a verified later resolution; an unsuccessful first search would have missed it.

## 5. Problems, open scope, and the bounded contribution

{table(['Problem ID','Title','Occurrences'],[(p['id'],p['title'],', '.join(p['occurrences'])) for p in problems])}

Each problem has a definite formulation, a dated status, and occurrence links. A solved question stays in the index because its historical recurrence matters. Independent review of the question-kind occurrences added the solved subnormal problem in 1964-50.5 and documented the reasons for excluding thirteen other prompts in `evidence/problem_index_review.md`. Vague discussion prompts are not promoted into independent open problems. The source's possible self-avoiding walk interpretation is separated from the precise modern uniform-walk model. Results about a honeycomb lattice, a diameter, or a different sampling procedure cannot silently settle a square-lattice expected endpoint question.

For Bishop operators, the development first proves that a rational rotation yields a finite fibre matrix whose endpoint determinant is nonzero. Singular interior fibres are allowed: they have measure zero, and the cyclicity proof uses truncation rather than a uniform inverse. It then derives an L² continuity estimate which accounts for the jumps of the fractional-part function. Treating that function as globally Lipschitz would invalidate the transfer argument.

Two programs verify the arithmetic independently. The first uses symbolic rational matrix operations and exact polynomial integration. The second uses integer Bareiss elimination and Python `Fraction`, with separately rebuilt orbit polynomials. They agree on all reported integrals and determinant signs, including the coprime pair (9,16). The endpoint formula and matrix-power identity also pass all 31 coprime pairs with 2 ≤ q ≤ 10. These finite checks are explicitly distinguished from the all-denominator proof.

The concrete degree-four polynomial approximates x² at rotation 1/2 with squared error 2117561/24772369344. Its coefficient sum gives an error below 1/50 throughout the stated parameter neighbourhood. One finite approximation does not prove cyclicity at a fixed irrational parameter. The subsequent theorem supplies a total computable sufficient gap function by a terminating rational search. No practical growth bound for that function, and no necessity claim, is asserted. The remaining obstruction is controlling the degree and coefficient size uniformly as denominators grow.

The notation `[proved here]` or `[computed here]` records work supplied and checked in this companion. It does not claim that the result is historically new. The next bounded research step is to obtain the 2026 preprint, compare its bounds with the exact certificate method, and prove useful coefficient estimates. The present work does not forecast a universal solution.

## 6. What the A–F classes miss

A single fate letter cannot encode all relevant distinctions. E can describe a standard theorem whose literal source formula is false. A can describe a speaker's close publication even if the manuscript was submitted before the seminar. B can mean a proof strategy realized much later, rather than a newly discovered theorem. F can coexist with a useful thematic reference without licensing a definite attribution. C can cover a broad unresolved problem and a much narrower tractable subquestion.

The independent fields are therefore part of the scholarly conclusion, not administrative decoration. Literal correctness assesses the recorded sentence; publication match assesses the relationship to a source; verification describes what was actually inspected; confidence describes identification and fate; development describes this companion's work. These should remain separately searchable and should never be collapsed into an automatic quality score.

The required schema has only one problem link per occurrence and one aggregate verification value. Future versions should allow a list of typed relations and per-reference evidence records. The present files keep the fixed schema, placing such qualifications in prose instead of silently extending it.

## 7. Recommendations for the generated website

A reader entering at a talk should first see its date, attribution, physical source pages, a concise summary, and a direct path to the relevant scan. Each item should display three adjacent or clearly labelled layers: source wording, precise modern statement, and reconstruction. The fate and current status should follow, with bibliography locators and an explicit checked-through date. Assessment badges should be expandable explanations rather than an unexplained rank.

The most useful navigation is talk → item → problem → other occurrences, with a return link to the exact source page. Within this year, links should connect the invariant-subspace announcement and Halmos's review, the repeated gap formula, the Fredholm/sheaf-index discussions, and the Kazhdan–Palamodov sequence. A source observation used only as a thematic comparison should be labelled as such. Cross-year links must wait for actual earlier or later occurrence records.

Add structured fields in a future schema for `source_anchor` (page and region), `attribution_basis`, `source_scope` versus `modern_scope`, `first_circulation_date`, `submission_date`, `publication_date`, `checked_at`, `result_locator`, `evidence_level`, and `status_history`. Typed relations such as `same_question`, `special_case`, `proof_strategy`, `counterexample`, `retraction`, and `thematic_comparison` would prevent accidental conflation. Reference versions should be explicit when theorem numbers differ between a preprint and a journal article.

Search should cover mathematical notation and transliteration variants, and allow filters by year, speaker, area, item kind, class, correctness, and verification. A user should be able to find all false literal statements without excluding their correct reconstructions, or all open precise questions without receiving unidentified fragments. Corrections need bidirectional links to the source and affected occurrences. The present task supplies data and recommendations; it does not deploy a website.

## 8. Reproduction, build, and limitations

The seven required source files are authoritative. The supplied builder generates `GY1964_chapter.tex` and the standalone driver; XeLaTeX and BibTeX produce `GY1964_test.pdf`. The archive contains the builder, style, driver, research code, exact arithmetic outputs, data audits, and build/visual-QA evidence. The README identifies commands and dependencies. Input hashes identify the attachments used for the source-extraction audit without requiring the scans to be duplicated in this archive.

Verification is bounded. No claim is made to have independently re-proved every literature theorem, to have exhausted every unpublished source, or to have established consensus on very recent preprints. The explicit verification levels preserve those limits. New proofs and finite computations supplied in the development received a second independent check; the saved review records what was checked and any resulting corrections. Build success establishes syntactic and typesetting consistency, not mathematical truth, so it is reported separately from the mathematical review.

## 9. Selected references for the report

The complete reference list and item-specific locators are in `GY1964_references.bib` and the compiled chapter. These selected references support the principal historical and mathematical decisions above; opening a publisher abstract is distinguished from reading the complete article in the corresponding occurrence and bibliography annotation.

Béhani, V. (2023). A study of Bishop operators from the point of view of linear dynamics. *Journal of Mathematical Analysis and Applications, 526*(1), Article 127204. https://doi.org/10.1016/j.jmaa.2023.127204. [Primary preprint](https://arxiv.org/pdf/2207.11419), Theorems 4.4–4.5, 4.9, 4.16 and Question 5.4.

Brown, S. W. (1978). Some invariant subspaces for subnormal operators. *Integral Equations and Operator Theory, 1*, 310–333. https://doi.org/10.1007/BF01682842. Publisher abstract and metadata inspected; full subscription article not read.

Chamizo, F., Gallardo-Gutiérrez, E. A., Monsalve-López, M., & Ubis, A. (2020). Invariant subspaces for Bishop operators and beyond. *Advances in Mathematics, 375*, Article 107365. https://doi.org/10.1016/j.aim.2020.107365. [Primary preprint](https://arxiv.org/pdf/1812.08059), Theorems 3.7 and 4.1.

Couronné, O. (2025). New upper bound for the connective constant for square-lattice self-avoiding walks. *Journal of Statistical Physics, 192*(11), Article 153. https://doi.org/10.1007/s10955-025-03542-6. First preprint: 29 November 2022; publisher abstract inspected.

Dobrushin, R. L. (1965). The existence of a phase transition in the two-dimensional and three-dimensional Ising models. *Theory of Probability and Its Applications, 10*(2), 193–213. https://doi.org/10.1137/1110026. [Russian original and bibliographic record](https://www.mathnet.ru/eng/tvp518), Theorems 1–2 and contour lemmas.

Dobrushin, R. L. (1966). Addendum: The existence of a phase transition in the two-dimensional and three-dimensional Ising models. *Theory of Probability and Its Applications, 11*(3), 486–487. https://doi.org/10.1137/1111054. [Russian correction](https://www.mathnet.ru/eng/tvp656), both corrective paragraphs.

Domar, Y. (1981). Translation invariant subspaces of weighted lᵖ and Lᵖ spaces. *Mathematica Scandinavica, 49*, 133–144. https://doi.org/10.7146/math.scand.a-11926. [Primary paper](https://journals.msp.org/mscand/article/download/1747/1746/1778), Theorem 2, pp. 134–135.

Gelfand, I. M., & Kirillov, A. A. (1966). Sur les corps liés aux algèbres enveloppantes des algèbres de Lie. *Publications Mathématiques de l’IHÉS, 31*, 5–19. https://doi.org/10.1007/BF02684800. [Primary paper](https://www.numdam.org/item/PMIHES_1966__31__5_0.pdf), §4, Lemma 5 and Theorem 2.

Smale, S. (1965). An infinite dimensional version of Sard's theorem. *American Journal of Mathematics, 87*(4), 861–866. https://doi.org/10.2307/2373250. [Primary paper](https://people.math.harvard.edu/~dafr/M392C-2018-MorseTheory/Readings/Smale.pdf).

Sz.-Nagy, B., & Foiaș, C. (1964). Sur les contractions de l'espace de Hilbert. IX. Factorisations de la fonction caractéristique. Sous-espaces invariants. *Acta Scientiarum Mathematicarum, 25*(3–4), 283–316. [Primary paper](https://acta.bibl.u-szeged.hu/14044/1/math_025_fasc_003_004_283-316.pdf), Theorem 3 and Remark (ii), p. 314; read with the [1965 correction](https://acta.bibl.u-szeged.hu/14072/1/math_026_fasc_001_002_193-196.pdf), p. 193.
'''
    (OUT/'GY1964_report.md').write_text(report)
    print(json.dumps(stats,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
