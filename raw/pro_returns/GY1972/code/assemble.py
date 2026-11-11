"""Assemble the GY1972 deliverable from independently reviewed research batches.

Usage: python assemble.py OUTPUT_DIRECTORY
In the delivered archive: python code/assemble.py .
This does not fetch references or rerun the authoring scripts; the reviewed
batch JSON/CSV/BibTeX and evidence files are the checkpoint inputs.
"""
import collections
import csv
import hashlib
import json
from pathlib import Path
import re
import sys

BASE = Path(__file__).resolve().parent
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
OUT.mkdir(parents=True, exist_ok=True)
TAG = 'GY1972'
BATCHES = ('early', 'buchstaber', 'topology', 'root')
ORDER = [272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,
         287,289,290,292,291,293,294,295,296,298,297,299,300]
POSITION = {r: n for n, r in enumerate(ORDER)}
FIELDS = ['page','place','transcription_reads','should_read','evidence','applies_to','type']


def prose_spacing(value):
    """Fix run-together dates in prose, preserving formulas, citations and URLs."""
    if not isinstance(value, str):
        return value
    protected = r'(\\\(.*?\\\)|\\\[.*?\\\]|\\cite\w*\*?(?:\[[^]]*\])*\{[^}]*\}|https?://\S+)'
    parts = re.split(protected, value, flags=re.S)
    months = ('January|February|March|April|May|June|July|August|September|October|November|December')
    for n in range(0, len(parts), 2):
        s = parts[n]
        s = re.sub(r'(?<=[A-Za-z])(?=(?:18|19|20)\d{2}\b)', ' ', s)
        s = re.sub(r'(?<=\d)(?=(?:'+months+r')\b)', ' ', s)
        s = re.sub(r'\b('+months+r')(?=\d)', r'\1 ', s)
        s = re.sub(r'\b(and|in|of|the|The|received|Received|on|for|to|at|through|before|after|all)(?=\d)', r'\1 ', s)
        s = s.replace('\\textquotesingle s', '’s')
        parts[n] = s
    return ''.join(parts)


talks, items, problems, corrections, entries = [], [], [], [], {}
hashes = {}
for batch in BATCHES:
    folder = BASE / 'batches' / batch
    for name, target in [('talks',talks),('items',items),('problems',problems)]:
        file = folder / (name+'.json')
        hashes[str(file.relative_to(BASE))] = hashlib.sha256(file.read_bytes()).hexdigest()
        target.extend(json.loads(file.read_text()))
    with (folder/'corrections.csv').open(newline='') as stream:
        corrections.extend(csv.DictReader(stream))
    bib = (folder/'references.bib').read_text()
    starts = list(re.finditer(r'^@\w+\s*\{\s*([^,\s]+)\s*,', bib, re.M))
    for j, match in enumerate(starts):
        key = match.group(1)
        entry = bib[match.start(): starts[j+1].start() if j+1<len(starts) else len(bib)].strip()
        if key in entries:
            raise ValueError('Unexpected duplicate bibliography key: '+key)
        entries[key] = entry

assert len(talks) == len(ORDER) and {t['record'] for t in talks} == set(ORDER)
talks.sort(key=lambda t: POSITION[t['record']])
items.sort(key=lambda i: (POSITION[i['record']], int(i['id'].rsplit('.',1)[1])))
problems.sort(key=lambda p: p['id'])
corrections.sort(key=lambda c: (int(re.search(r'\d+',c['page']).group()), c['place']))

for group in (talks,items,problems,corrections):
    for obj in group:
        for key, value in obj.items():
            if key not in ('id','record','date','pages','page','problem','refs','occurrences','status_date'):
                obj[key] = prose_spacing(value)
for talk in talks:
    if talk.get('kind') == 'heading' and talk['speaker'] == '-':
        talk['speaker'] = ''
    if talk['record'] == 287:
        talk['summary'] += (' The page also announces a plan for topology reports by Buchstaber and Mishchenko '
                            'and for work of Deligne and Langlands; the latter heading supplies no additional '
                            'mathematical assertion on this page.')

# Render-only equation layout adjustments found by the XeLaTeX overfull-box
# audit. These preserve the assertions and are applied before serialization,
# so rebuilding from the delivered seven files gives the same chapter.
by_id = {item['id']:item for item in items}
layout = [
 ('1972-278.7','notes',r'\((1,0,0),(0,1,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1)\)',
  r'\[(1,0,0),\ (0,1,0),\ (0,0,1),\ (1,1,0),\ (0,1,1),\ (1,1,1).\]'),
 ('1972-279.4','fate',r'Chs.VIII,X',r'Chs.~VIII, X'),
 ('1972-282.5','statement','The recoverable content is a method announcement:',
  'The notes announce a method:'),
 ('1972-283.5','statement',r'\(\sum_{n\ge1}c_n e^{\gamma nx}\sin nx\)',
  r'\[\sum_{n\ge1}c_n e^{\gamma nx}\sin nx\]'),
 ('1972-283.6','notes',r'\(\sum_{\lambda_k>0}c_ke^{\lambda_k t}v_k(x)\), whose limit',
  r'\[\sum_{\lambda_k>0}c_ke^{\lambda_k t}v_k(x).\] The limit'),
 ('1972-283.12','statement',r'\(\{e^{\gamma\lambda_nx}\sin(\lambda_nx)\}_{n\ge1}\).',
  r'\[\{e^{\gamma\lambda_nx}\sin(\lambda_nx)\}_{n\ge1}.\]'),
 ('1972-284.6','statement',r'\(Q_f=\mathcal O_{\mathbb C^n,0}/(\partial_1f,\ldots,\partial_nf)\)',
  r'\[Q_f=\mathcal O_{\mathbb C^n,0}/(\partial_1f,\ldots,\partial_nf)\]'),
 ('1972-291.18','statement',r'\([K(z,\bar v)K(v,\bar z)/(K(z,\bar z)K(v,\bar v))]^{1/h}\),',
  r'\[\left(\frac{K(z,\bar v)K(v,\bar z)}{K(z,\bar z)K(v,\bar v)}\right)^{1/h},\]'),
 ('1972-294.8','statement',r'the Milnor number is \(\dim_{\mathbb C}\mathcal O/(\partial f)\),',
  r'the Milnor number is \[\mu=\dim_{\mathbb C}\mathcal O/(\partial f),\]'),
]
for item_id, field, old, new in layout:
    assert old in by_id[item_id][field], (item_id,field,old)
    by_id[item_id][field] = by_id[item_id][field].replace(old,new)
by_id['1972-278.7']['notes'] = by_id['1972-278.7']['notes'].replace(r'.\].',r'.\]')

for name, data in [('talks',talks),('items',items),('problems',problems)]:
    (OUT/f'{TAG}_{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
with (OUT/f'{TAG}_corrections.csv').open('w',newline='') as stream:
    writer = csv.DictWriter(stream,fieldnames=FIELDS)
    writer.writeheader(); writer.writerows(corrections)
(OUT/f'{TAG}_references.bib').write_text(
    '% GY1972 bibliography; verification cutoff 9 November 2026.\n'
    '% The annote fields distinguish full-result reading from metadata verification.\n\n'
    +'\n\n'.join(entries[k] for k in sorted(entries))+'\n')
development = (BASE/'batches/early/development.tex').read_text()
development = development.replace('\\ours\n','\\ours\\ \n')
development = development.replace('\\paragraph{Independent verification.}\\oursComputed\n',
                                  '\\paragraph{Independent verification.}\\oursComputed\\par\n')
(OUT/f'{TAG}_development.tex').write_text(
    '% Corrective development of an A item; no bounded C/D research target qualified.\n'+development)

by_class = collections.Counter(i['class'] for i in items)
by_record = collections.Counter(i['record'] for i in items)
talk_by_record = {t['record']:t for t in talks}
by_speaker = collections.defaultdict(collections.Counter)
for item in items:
    speaker = item.get('speaker') or talk_by_record[item['record']]['speaker']
    by_speaker[speaker][item['class']] += 1
talks_by_speaker = collections.Counter(t['speaker'] for t in talks if t['kind']=='talk')
AREAS = {
 'Hodge structures and complex geometry':[272,275],
 'Arithmetic, local fields and p-adic interpolation':[273,274,298,299,300],
 'Formal groups and their homological algebra':[276,279,282,285],
 'Quiver representations':[277,278],
 'Algebraic K-theory and derived categories':[280,281],
 'Operator theory, completeness and complex analysis':[283,290,292],
 'Singularity theory':[284,294,297],
 'Surgery, normal invariants and stable homotopy':[287,289,293,295],
 'Quantization and operator symbols':[291],
 'Spectral geometry and eta invariants':[296],
}
area_of = {record:area for area,records in AREAS.items() for record in records}
by_area = collections.defaultdict(collections.Counter)
for item in items:
    by_area[area_of[item['record']]][item['class']] += 1
metrics = dict(records=len(talks), talks=sum(t['kind']=='talk' for t in talks),
               headings=sum(t['kind']=='heading' for t in talks), items=len(items),
               classes={c:by_class[c] for c in 'ABCDEF'}, problems=len(problems),
               references=len(entries), corrections=len(corrections),
               correction_types=dict(collections.Counter(c['type'] for c in corrections)),
               literal_correctness=dict(collections.Counter(i['literal_correctness'] for i in items)),
               publication_match=dict(collections.Counter(i['publication_match'] for i in items)),
               verification=dict(collections.Counter(i['verification'] for i in items)),
               development=dict(collections.Counter(i['development'] for i in items)),
               confidence=dict(collections.Counter(i['confidence'] for i in items)),
               source_order=ORDER, by_speaker=dict(by_speaker), by_area=dict(by_area),
               by_record=dict(by_record), input_sha256=hashes)
(OUT/'assembly_metrics.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n')

overview = r'''This chapter covers the 28 requested catalogue records: 27 talks and the 1973 year heading. Its 272 occurrences are ordered by the manuscript, with status assessed on 9 November 2026. The dominant feature is sustained exposition across several meetings: Hodge structures and local fields; formal groups and their homological algebra; higher algebraic K-theory; quivers and singularities; surgery and stable homotopy. Berezin's quantization, Lomonosov's invariant-subspace argument, Henkin's analytic announcements, and the reports on spectral asymmetry and p-adic L-functions connect these longer sequences to current research.

\begin{center}\small
\begin{tabular}{@{}clrr@{}}\toprule
Class & Meaning & Items & Percent\\\midrule
@@CLASS_ROWS@@
\midrule & Total & 272 & 100.0\\\bottomrule
\end{tabular}
\end{center}

The classes describe historical fate, not truth. Several A items contain literal errors, while an E theorem may be substantially harder than a new announcement. Lomonosov's note was received before his seminar talk; Berezin's symbol paper was already published, whereas the quantization programme was announced in 1973 and expanded in 1974--75. Henkin's bounded extension theorem was old by March 1973, but the convex embedding announcement has a later precise publication. The APS chronology is especially instructive: a 1973 unrestricted regularity announcement and later geometric proofs must be distinguished from Gilkey's 1981 completion of the general eta theorem \citep{lomonosov1973invariant,berezin1972symbols,henkin1972continuation,atiyahpatodisinger1976spectral3,gilkey1981residue}.

Eleven problem entries track definite questions. Most were already resolved or led promptly to established results. The sole C occurrence, 1972-287.11, is explicitly a reconstructed all-degree programme for the numerical homotopy groups of \(G/O\), with the stable-stem and extension data still required by its exact sequence. No particular finite-degree group is asserted to be unknown. The notebook supplies no bounded target for a new contribution, so no C/D item is selected for research development. Berezin's nonhomogeneous analytic-unit phrase and the proposed complex-character spectral series remain F because their missing categories prevent a uniquely formulated problem; nearby modern results do not fill those omissions.

The development appendix instead gives a complete, independently checked correction to Vasserstein's exact published flag assertion. Three elementary matrices are pairwise adjacent but do not lie in one common triangular coset, over every nonzero unital ring and after stabilization. A common acyclic-support criterion replaces the false test. This remains A, with literal correctness recorded separately; the appendix makes no novelty or priority claim \citep[\S11, Remark~(c)]{vaserstein1976foundations}. Shorter marked checks elsewhere repair the cubic cocycle's two-torsion, the reverse Adams formula, the modular-period parity and the raw p-adic zeta continuity claim. Exact computations and separate derivations accompany these corrections.

The cross-year links are specific. Gabrielov continues the Hodge material of 1969-182.2 and 1971-248/251; Buchstaber continues 1971-268/270 on formal laws and 1968-171/173 on normal maps. Vasserstein connects to 1971-253--257 and the earlier K-theory comparison problem, without turning its exposition into a repetition of every earlier conjecture. Quivers continue the four-subspace thread of 1970-198. Lomonosov revisits the compact-operator theme of 1964-50, while eta invariants connect to GP-1971-04 on spectral flow. Berezin's symbol calculus links back to quantization in 1969-178 and 1971-229.

Two ownership issues require explicit treatment. P000449 is a preceding-year tail, already represented by 1971-270.10. P000480 is the Dobrushin discussion already indexed as 1972-288.1--5 in the supplied previous index; record 288 is absent from the requested list, so those occurrences are linked, not duplicated. Within this chapter, 5 March runs 290,292,291 and 26 March runs 296,298,297. Broad catalogue scan windows are not treated as exact talk boundaries. The correction file preserves uncertain readings separately from mathematical emendations, and the bibliography's verification annotations distinguish reading a result from opening metadata.
'''
labels={'A':'Speaker/Gelfand publication soon afterward','B':'Developed by other authors',
        'C':'Partly developed, exact residual stated','D':'No development identified',
        'E':'Known before the talk','F':'Not identifiable from the notes'}
rows=[]
for c in 'ABCDEF':
    rows.append(f'{c} & {labels[c]} & {by_class[c]} & {100*by_class[c]/len(items):.1f}\\\\')
overview=overview.replace('@@CLASS_ROWS@@','\n'.join(rows))
(OUT/f'{TAG}_overview.tex').write_text(overview)


def table(header, rows):
    return ('| '+' | '.join(header)+' |\n| '+' | '.join('---' for _ in header)+' |\n'
            +'\n'.join('| '+' | '.join(str(x) for x in row)+' |' for row in rows)+'\n')


report = f'''# GY1972: research, coverage and production report

**Status cutoff:** 9 November 2026. **Scope:** all 28 requested catalogue records,
including 27 talks and the year heading. The chapter contains **{len(items)} mathematical
occurrences, {len(problems)} problem entries, {len(entries)} references and
{len(corrections)} correction/provenance entries**. Each occurrence distinguishes
the notebook, a precise statement, editorial reconstruction, historical fate,
dated status and the required assessment fields.

## 1. Counts

### Historical classes

'''
report += table(['Class','Meaning','Items','Percent'],
                [(c,labels[c],by_class[c],f'{100*by_class[c]/len(items):.2f}%') for c in 'ABCDEF'])
report += '''
These are occurrence counts, not counts of independent discoveries. A repeated
construction receives another occurrence when it is discussed again. The year
heading has no mathematical item. The eleven indexed problems include resolved
historical questions; the number of problem entries is not an open-problem count.

### By speaker

Talk counts use the catalogue attribution. Item counts use the optional speaker
override where an intervention is identified, and otherwise the talk's speaker.
The heading is excluded from this table.

'''
speakers=sorted(set(talks_by_speaker)|set(by_speaker))
report+=table(['Speaker','Talks','A','B','C','D','E','F','Items'],
              [(s,talks_by_speaker[s],*[by_speaker[s][c] for c in 'ABCDEF'],sum(by_speaker[s].values())) for s in speakers])
report+='''
### By primary area

The following mutually exclusive tags are assigned at the record level for
reproducible totals. They describe the main line of a talk; they do not deny its
other subjects. A future website should support multiple item-level tags.

'''
report+=table(['Primary area','A','B','C','D','E','F','Items'],
              [(a,*[by_area[a][c] for c in 'ABCDEF'],sum(by_area[a].values())) for a in AREAS])
report+='''
### Assessment dimensions

'''
for field in ['literal_correctness','publication_match','verification','development','confidence','correction_types']:
    report += '**'+field.replace('_',' ').capitalize()+'.** '+ '; '.join(f'{k}: {v}' for k,v in sorted(metrics[field].items()))+'.\n\n'
report+='''
The label `verified` on a bibliography entry means that its URL or DOI was
opened and checked to the extent stated in `annote`. It does not mean that a
whole monograph was read. Item-level `verification` describes the evidentiary
strength of the actual match. Metadata-only and indirect cases remain visible.

## 2. Coverage and boundaries

'''
report+=table(['Record','Date','Speaker','Actual source span','Items'],
              [(t['record'],t['date'] or 'heading',t['speaker'] or '—',t['pages'],by_record[t['record']]) for t in talks])
report+='''
The source-order sequence is:

`272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 289, 290, 292, 291, 293, 294, 295, 296, 298, 297, 299, 300`.

The two inversions are required by the handwritten headings. Henkin appears on
lower P000483 before Berezin on P000484. The arithmetic continuation occupies
upper P000497 before Gabrielov. Catalogue ranges are overlapping scan windows,
not a reliable segmentation rule. Record286 is a catalogue year heading, whose
window is retained as such; the plan on P000478 is acknowledged in record287.

Every page is accounted for. New item spans cover P000450–P000479 and
P000481–P000500. P000449 belongs to the previously indexed tail1971-270.10.
The Dobrushin material on P000480 is already in the supplied previous index as
1972-288.1–5, even though that index places it under the previous chapter.
Record288 is not among the requested28. Duplicating it would corrupt the
cross-year occurrence index; silently assigning its page to Buchstaber or
Lomonosov would corrupt speaker attribution. The chapter discloses this
ownership discrepancy and preserves the existing identifiers.

## 3. What the searches established

### Announcements, subsequent papers and exact matches

Math-Net searches by author, title fragments and year were especially effective.
They located Lomonosov's two-page1973 note, Berezin's1973 Doklady announcement
and1974–75 full papers, Henkin's1972 extension theorem and the1975 Henkin–Chirka
account, Buchstaber's1973 two-valued formal-group announcement, Nazarova's quiver
paper, Arnold's normal-form work, and Manin's1973 modular-period paper. Receipt
dates and original-language volume years were recorded separately from later
English copyright years. The dates matter: an exposition in1973 can concern
a1972 paper, a result in preprint, or a theorem not yet completely proved.

Full-result locators prevent thematic resemblance from doing the work of an
exact match. For example, Vaserstein's1976 §11 Remark(c) is the precise flag
assertion, not merely a paper about K-theory. Henkin–Chirka Proposition14 on
Russian p.111 is the convex embedding statement. Manin's Proposition9.2,
Lemma9.4, equation39 and Theorem10.2 identify the period and measure construction,
while showing that the notebook's normalization cannot simply be copied.

The APS sequence required reading backward from later proofs. PartIII explicitly
records the even-dimensional gap left after the unrestricted1973 announcement;
Gilkey's1981 Theorem0.1 supplies the general completion. Treating the1973
announcement as a fully proved general theorem would erase the most informative
historical distinction in this short record (Atiyah et al.,1976; Gilkey,1981).

For Kostyuchenko's system, later primary papers by Lyubarskii–Tkachenko,
Bilalov and Kritskov identify the one-sided real-parameter family and distinguish
completeness, minimality and the basis property. They do not certify every
Schwarz–Christoffel coefficient formula compressed into the notebook. Thus
the recognizable system can have an established fate while a proposed exact
formula remains F. Likewise, Berezin's zero-free-kernel claim is answered
negatively by pre-seminar annulus counterexamples, but their1969 chronology was
verified indirectly through Boas's author survey and is labelled accordingly.

The source logs under `code/batches/*/evidence.md` give the URLs and locators,
including unsuccessful or inconclusive leads. These logs do not claim exhaustive
coverage of MathOverflow, Scholar, every collected work or every language.
No failure of an initial query was used as grounds for D.

### Cross-year linkage

The supplied index was searched before assigning new problem IDs. Hodge
structures connect to1969-182.2 and1971-248/251; formal groups connect
to1971-268/270; normal maps and surgery connect to1968-171/173. The K-theory
exposition connects to1971-253–257 and GP-1971-20/21, but it does not pose
those exact earlier research questions again. Consequently those problem IDs
are contextual links, not falsely added current occurrences. Quivers connect
to1970-198, compact operators to1964-50, and eta geometry to GP-1971-04.
The concrete new questions retain their new IDs. Bibliography reconciliation
found16 reused cumulative keys and no same-work duplicate under another key.
The cumulative input itself has repeated entries; it is preserved unchanged
as input, while the chapter bibliography has one entry per used key.

## 4. Corrections that change the mathematics

The correction file distinguishes a reading error from an error visibly present
in the source. Most of this year's consequential changes are faithful-error
emendations or explicit qualifications, not conjectural improvements to the
transcription.

- Hodge orthogonality uses the complementary filtration index, and polarization
  symmetry changes with the correct parity. Connected components also matter
  for the period-domain transitivity statement.
- The ramification groups use a shifted historical convention. The weak
  ramification wording on this page corresponds to modern tame ramification.
- In the formal-group cubic calculation, the coefficient relation is
  `2(C1−C2)=0`, not3-torsion. Ordinary polynomial-module Ext must be separated
  from the coalgebra/comodule computation. The truncated-polynomial Ext algebra
  has a characteristic-two exception to the displayed exterior factor.
- A normal invariant includes a chosen spherical trivialization. A bare
  J-trivial stable bundle forgets data needed by the surgery sequence.
  Sullivan's Hauptvermutung condition concerns the third integral homology
  group, equivalently the relevant torsion in fourth integral cohomology,
  rather than the notebook's third-cohomology claim.
- The reverse Adams formula with a separate equality for every k is false.
  The real-K-theory S4 argument uses a multiple with J-image zero and a prime
  divisibility obstruction; it is not a counterexample to the Adams conjecture.
- Lomonosov's separation-of-zero argument requires a different ball-center
  scale. The finite-dimensional eigenspace appears under a temporary
  transitivity assumption; it is not promised by the final theorem.
- Berezin's formulas require the correct conjugation, h in the annihilation
  operator, frame-norm measure, negative weight and normalized kernel ratio.
  Compact models require line-bundle gluing and an integral normalization.
- The p-adic zeta claim needs the Euler factor, a weight branch and pole
  qualification. An explicit p=5 sequence gives different raw limits for
  sequences approaching the same weight. The modular-form page also has wrong
  automorphy and Hecke factors, a missing1+ in a character subgroup, and a real
  period of odd parity paired with an even character.
- The Bernoulli determinant uses coefficients B_r/r!. Its rigorous finite
  polynomial form is distinguished from an undefined infinite determinant.
  The endpoint B1(1), rather than B1(0), handles k=0 correctly.

Where a stroke remains uncertain, the CSV says so. Mathematical necessity does
not turn a doubtful0/a residue on P000499 or a tangent/normal symbol on P000490
into a certain palaeographic reading.

## 5. Development decision and independent verification

The sole C item is1972-287.11, a **reconstructed all-degree computation programme**
for the homotopy groups of G/O. Its object is identifiable from the PL/smooth
comparison and the later specified-trivialization data. The exact-sequence
reduction and finite ranges are known; stable-stem and extension information
still determines the all-degree numerical problem. No complete all-degree table
was located, and no particular finite-degree group is asserted to be unknown.
The recent stable-stem reference illustrates finite progress, not a solution of
all normal-invariant groups (Ranicki,2002; Burklund et al.,2026).

The notes select no degree range or particular extension. Consequently there
is **no warranted bounded C/D research development** in this chapter. The
nonhomogeneous Berezin unit phrase was independently reviewed and changed from
a provisional C to F: its analytic category is not recoverable, so the formal
unital theorem cannot be advertised as a partial answer to one exact analytic
problem. This change also removed its provisional problem-index entry.

The appendix is instead a corrective development of an A item. Vaserstein's
published flag assertion is refuted by three elementary matrices over every
nonzero unital ring. The proof gives the exact acyclic-support criterion,
handles both left and right cosets, proves persistence under stabilization,
and establishes minimal coordinate rank. Publication provenance is preserved
by keeping class A, while `literal_correctness` records falsity. No claim is
made that the counterexample is historically new. No unresolved problem is
manufactured after the literal question has been settled negatively.

The computational and proof checks are independent in substantive ways:

| Check | Primary verification | Independent verification | Conclusion |
| --- | --- | --- | --- |
| Tolerance counterexample | Exact matrix products and30 cases over five rings, dimensions3–5, both coset conventions | Separate code over four finite fields in24 cases; separate general-ring and rank-two derivations | All agree; proof, not extrapolation, gives arbitrary rings and stabilization |
| Formal cocycles and Ext | Independent polynomial implementations; finite-ring checks; normalized bar argument | Direct cubic differential and square-zero tensor-algebra derivation | Two-torsion and p=2 repairs confirmed |
| Normal-difference invariant | Pullback computation | Separate homotopy-inverse argument | Bare KO class invariant; chosen spherical data not thereby identified |
| Reverse Adams assertion | Real KO on S4 and divisibility | Independent real proof plus complex S2 check | Universal fixed-k reverse equality refuted; Adams conjecture unaffected |
| Modular measure | General coefficient calculation | Separate derivation of finite additivity, primitive cancellation, parity and Gauss prefactor | Corrected two-term measure and stated normalization consistent |
| Floor distribution |5814 exact refinements over p=2,3,5,7 | Residue-permutation proof | All finite checks pass; general identity proved separately |
| Bernoulli summation |143 power sums and independent triangular inversion |65 power sums and65 mixed-polynomial systems, including n=0 | All pass; factorial and endpoint conventions confirmed |
| Raw zeta limit | Exact Bernoulli values at three levels plus branch-limit proof | Fourth level and independently written rational recurrence | Raw limit1/3 differs from the constant sequence−1/12 |

All code and numerical output are included. `ours` and `oursComputed` mean that
the companion supplies the indicated proof or calculation; they do not assert
novelty. Source-reading and taxonomy reviews are also recorded separately.

## 6. What the classes miss, and proposed format changes

The A–F field compresses several independent dimensions. This year demonstrates
why it must never replace literal correctness, publication match, confidence
or verification level. An A claim can be false; an E item can need a long
reconstruction; a B match can settle only a corrected form; an F occurrence can
belong to a well-known programme without determining one exact theorem.

Retain the present fields, and consider these additive fields for later chapters:

1. **Circulation and publication events:** structured dates with source and
   precision, rather than one inferred year. Record contradictory receipt
   metadata without forcing a resolution.
2. **Source segments:** exact page plus region/heading, with catalogue scan
   window stored separately. A page can belong to two talks; a record can be a
   virtual heading. Add an ownership/carryover relation for the P480 situation.
3. **Claim relations:** typed links such as repeats, corrects, specializes,
   supplies-proof, and thematic-context. A corrected formula is not equivalent
   to a literal publication match.
4. **Problem formulation basis:** explicit-notebook versus reconstructed, plus
   quantified residual scope and development decision. This would make the
   programme-level C and the underspecified F distinction easier to inspect.
5. **Evidence level per citation:** result locator, access date and the actual
   portion read. One entry's verified URL should never visually imply full
   proof verification for all claims citing it.
6. **Editorial result and test links:** an ID connecting a marked argument to
   its independent review, code, parameters and output. The current plain text
   can contain this information, but a website should expose it directly.

These are recommendations, not unannounced changes to the required seven-file
schema. The delivered data remain compatible with the supplied builder.

## 7. Website presentation

A reader arriving at one talk should first see its actual page segment, a
two-sentence orientation, and the list of items with separate badges for
historical class and literal correctness. Each item should open the notebook
wording, precise reconstruction and fate side by side or in clearly labelled
panels. The first citation link should land at the exact theorem or page when
available; a metadata-only link needs that visible label.

Priority navigation for this year is:

- Formal-law entries276/279/282/285 should expose the later counterexample to
  the earlier commutativity shorthand and the module/comodule distinction.
- K-theory record280 should link its tolerance question directly to the
  corrective proof, while preserving links to the earlier comparison programme.
- Surgery records287/289/293 should keep the chosen-trivialization warning and
  the dimensional hypotheses attached to every structure-set link.
- Singularities284/294/297 should distinguish the long expositions from the
  two-item Gabrielov opening fragment; no missing lecture should be fabricated.
- The5March group should show manuscript order290→292→291 and give direct
  routes to the Lomonosov scale repair, Henkin's extension/embedding split and
  Berezin's normalization corrections.
- The26March group should show296→298→297. The eta entry needs an announcement
  versus proof timeline; arithmetic298/299/300 needs the Euler-factor, parity
  and Bernoulli-convention links.
- The boundary pages449 and480 should open their existing occurrence owners,
  with a brief explanation of the source-window overlap, avoiding duplicate
  search results under incompatible year headings.

Search should index Russian phrases, transliterations, formulas' text aliases,
record and page IDs, publication keys and problem IDs. Filters for false literal
claims, partial matches, medium/low confidence and proof availability will be
more useful than an undifferentiated “open problem” filter. The problem index
should show all historical occurrences and a dated status, including resolved
questions; only the exact residual of C should appear as unfinished.

## 8. Build and archive contents

The seven required files are at the archive root, followed by this report, the
generated chapter, standalone driver and compiled PDF. The supplied builder
and style are included, as are original input files, checked research batches,
code, numerical outputs, assembly metrics, independent reviews and build logs.
The reproduction commands are in README.txt. No external mathematical source
PDF is redistributed; the bibliography and evidence logs provide its links.

The build executes the supplied Python checker, XeLaTeX, BibTeX, and XeLaTeX
twice more. A separate audit verifies the exact record set/order, schema enums,
consecutive item IDs, reciprocal problem links, bibliography keys, assessment
counts, dated statuses and page ownership. PDF inspection checks rendered
formula-heavy and Russian-text pages as well as the overview, development,
corrections and bibliography. Build and visual-QA outcomes are recorded in
validation_summary.json and build logs; any format adjustments are documented
there rather than silently applied to the analytical data.
'''
report=prose_spacing(report)
# Markdown prose also contains tightly set record/locator labels inherited
# from research notes. Expand only these explicit labels, preserving IDs,
# formulas, bibliography keys and the numerical data themselves.
for old,new in {
    'record286':'record 286', 'record287':'record 287', 'Record288':'Record 288',
    'requested28':'requested 28', 'Remark(c)':'Remark (c)',
    'Proposition14':'Proposition 14', 'p.111':'p. 111',
    'Proposition9.2':'Proposition 9.2', 'Lemma9.4':'Lemma 9.4',
    'equation39':'equation 39', 'Theorem10.2':'Theorem 10.2',
    'PartIII':'Part III', 'Theorem0.1':'Theorem 0.1',
    'al.,1976':'al., 1976', 'Gilkey,1981':'Gilkey, 1981',
    'found16':'found 16', 'not3-torsion':'not 3-torsion',
    'missing1+':'missing 1+', 'doubtful0/a':'doubtful 0/a',
    'Ranicki,2002':'Ranicki, 2002', 'al.,2026':'al., 2026',
    'dimensions3–5':'dimensions 3–5', '|5814':'| 5814',
    '|143':'| 143', '|65':'| 65', 'limit1/3':'limit 1/3',
    'sequence−1/12':'sequence −1/12', 'entries276':'entries 276',
    'record280':'record 280', 'records287':'records 287',
    'Singularities284':'Singularities 284', 'order290':'order 290',
    'show296':'show 296', 'arithmetic298':'arithmetic 298',
    'pages449':'pages 449',
}.items():
    report=report.replace(old,new)
(OUT/f'{TAG}_report.md').write_text(report)

print(json.dumps({k:metrics[k] for k in ['records','talks','headings','items','classes','problems','references','corrections']},indent=2))
