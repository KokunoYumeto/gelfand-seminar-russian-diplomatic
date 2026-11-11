"""Derive all tables from the delivered data and write the methodological report."""
from pathlib import Path
from collections import Counter,defaultdict
import csv,json,re,hashlib
from bib_tools import entries

ROOT=Path(__file__).resolve().parents[1];D=ROOT
talks=json.loads((D/'GY1978_talks.json').read_text())
items=json.loads((D/'GY1978_items.json').read_text())
problems=json.loads((D/'GY1978_problems.json').read_text())
refs=entries((D/'GY1978_references.bib').read_text())
with (D/'GY1978_corrections.csv').open(newline='') as f:corrections=list(csv.DictReader(f))
byrec=defaultdict(list)
for x in items:byrec[x['record']].append(x)
talkmap={t['record']:t for t in talks}
classes=Counter(x['class'] for x in items)

def area(x):
 r=x['record'];n=int(x['id'].split('.')[-1])
 if r==446:return 'Surreal numbers and asymptotic analysis'
 if r==447:return 'Classical integrability and variational methods' if n<=7 else 'Gauge theory, loop geometry and area functionals'
 if r==448:return 'Functional integration, instantons and determinants'
 if r==449:return 'Perturbative quantum field theory and sharp inequalities' if x.get('speaker')=='L. N. Lipatov' else 'Classical integrability and variational methods'
 if r==450:return 'Representation theory, extensions and cohomology'
 if r==453:return 'Gauge theory and instanton parametrization' if n<=5 else 'Quantum integrability and statistical mechanics'
 if r==454:return 'Quantum integrability and statistical mechanics'
 if r in [455,456]:return 'Twistor geometry and Yang–Mills connections'
 if r==457:return 'Graded and infinite-dimensional Lie algebras'
 if r==458:return 'Supersymmetry and superfields'
 if r==459:return 'Local and differential Lie structures'
 if r==460:return 'Webs and algebraic geometry' if n<=11 else 'Quantum integrability and statistical mechanics'
 raise ValueError(r)

def speaker(x):
 s=x.get('speaker') or talkmap[x['record']]['speaker']
 if s.startswith('I. M. Gelfand'):return 'I. M. Gelfand (interventions)'
 return s

def table(headers,rows):
 return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+
                 ['| '+' | '.join(str(v).replace('|','\\|').replace('\n',' ') for v in row)+' |' for row in rows])

aliases=[]
def alias(old,*new,note='Same supplied source occurrence; not a chronological recurrence.'):
 aliases.append({'previous_id':old,'current_ids':list(new),'relation':'same_source_overlap','note':note})
for i in range(1,5):alias(f'1977-445.{i}',f'1978-446.{i}')
for old,news in {1:[4],2:[5],3:[6],4:[7,8],5:[9],6:[10],7:[11,12],8:[13],9:[15],10:[16]}.items():
 alias(f'1977-451.{old}',*[f'1978-450.{i}' for i in news])
alias('1977-451.11','1978-453.1','1978-453.2')
alias('1977-451.12','1978-453.3')
alias('1977-451.13','1978-453.4','1978-453.5')
for old,news in {1:[1],2:[2,3],3:[4]}.items():alias(f'1977-457.{old}',*[f'1978-456.{i}' for i in news])
for old,news in {4:[1],5:[2,3,4,5,6],6:[7],7:[8],17:[9,10],18:[11],19:[12]}.items():
 alias(f'1977-457.{old}',*[f'1978-457.{i}' for i in news])
for old,news in {20:[2],21:[1],22:[3,4],23:[5],24:[6],25:[7]}.items():
 alias(f'1977-457.{old}',*[f'1978-458.{i}' for i in news])
(D/'GY1978_aliases.json').write_text(json.dumps(aliases,ensure_ascii=False,indent=2)+'\n')

page_records={}
def own(start,end,records):
 for p in range(start,end+1):page_records[f'P{p:06d}']=records
own(786,790,[446]);own(791,798,[447]);own(799,803,[448]);own(804,807,[449]);own(808,811,[450])
own(812,812,[452,453]);own(813,815,[453]);own(816,820,[454]);own(821,822,[455]);own(823,823,[456])
own(824,825,[457]);own(829,829,[457]);own(830,833,[458]);own(834,836,[459]);own(837,840,[460]);own(841,842,[])
assert len(page_records)==54

def cited_pages(value):
 found=set()
 for a,b in re.findall(r'P(\d{6})\s*[-–]\s*P(\d{6})',value):found.update(range(int(a),int(b)+1))
 found.update(map(int,re.findall(r'P(\d{6})',value)))
 return {f'P{p:06d}' for p in found}
page_items=defaultdict(list)
for x in items:
 for p in cited_pages(x['pages']):page_items[p].append(x['id'])
coverage=[]
for page,records in sorted(page_records.items()):
 note='Supplied scan and both transcriptions audited; the ownership follows manuscript headings.'
 if page=='P000812':note='Reading plan followed by Belavin; catalogue divider 451 has no independent mathematical occurrence.'
 if page in ['P000824','P000825','P000829']:note='Fuchs source-established addition 457; intervening P826–828 were not supplied and are not reconstructed.'
 if page in ['P000839','P000840']:note='Shabat record 460 includes the separately named Sasha Zamolodchikov intervention, with per-item speaker overrides.'
 if page in ['P000841','P000842']:note='Out-of-year boundary: Renata Kallosh, 24 September 1979; no 1978 occurrence ID assigned.'
 coverage.append({'page':page,'records':records,'items':page_items[page],'scope':'main' if records else 'following_year_boundary','note':note})
(D/'GY1978_coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
(D/'GY1978_item_areas.json').write_text(json.dumps({x['id']:area(x) for x in items},ensure_ascii=False,indent=2)+'\n')

overview=(ROOT/'code/overview_template.tex').read_text()
for key,value in {'RECORDS':len(talks),'ITEMS':len(items),'PROBLEMS':len(problems),**{c:classes[c] for c in 'ABCDEF'}}.items():overview=overview.replace('@'+key+'@',str(value))
(D/'GY1978_overview.tex').write_text(overview)

lines=['# GY1978: critical companion report','',
'**Scope and status cutoff:** academic year 1978–79; research and status statements checked as of 10 November 2026. The manuscript is the authority for what was recorded. Modern formulations, publication matches and editorial reconstructions are separate fields.','',
'## 1. Outcome and coverage','',
f'The deliverable contains **{len(talks)} records, {len(items)} mathematical occurrences, {len(problems)} problem-index entries, {len(refs)} bibliography entries and {len(corrections)} correction records**. It includes all fourteen commissioned catalogue entries and one justified addition, record 457. Records 451 and 452 are respectively a catalogue year divider and a reading plan; they contain no separate mathematical occurrences. All 54 supplied scans are accounted for in `GY1978_coverage.json`.','',
'Fuchs’s heading on P000824 is dated 5/III-79. The catalogue puts record 457 between February and March 1979 but dates it 5-Mar-78. The supplied P000824–P000825 and P000829 therefore belong to this academic year and are indexed here. Missing P000826–P000828 are not reconstructed from titles in the earlier index. P000841–P000842 are the beginning and continuation of Kallosh’s 24 September 1979 lecture. They are documented as following-year boundary evidence; they do not become Shabat items. The supplied package’s page groupings are not accepted as speaker boundaries.','',
table(['Record','Date','Speaker or entry','Items','Actual source scope'],[(t['record'],t['date'],t['speaker'] or t['kind'],len(byrec[t['record']]),t['pages']) for t in talks]),'',
'### Counts by historical class','',
table(['Class','Count','Operational reading'],[(c,classes[c],{'A':'Publication soon after the talk by the speaker or Gelfand; receipt is not public circulation.','B':'Subsequent development by other authors; partial matches are explicitly identified.','C':'A precise question partly developed, with a stated residual obstruction.','D':'A precise question not developed after a documented search.','E':'Pre-talk established material or exposition.','F':'The intended result, missing formulation, or intended correction cannot be identified.'}[c]) for c in 'ABCDEF']),'',
'No C or D assignment survived the identification audit. This does not establish that all related research problems are solved. It establishes that this source set and the literature actually checked support no precise C/D item with the required bounded development opportunity. F is never converted into D merely because a search failed.','',
'### Counts by speaker','',
'These counts use the item-level speaker when an intervention is named; otherwise they use the record speaker. The contextual identification of Kruskal is retained as an inference, alongside the discrepant catalogue initials. The Kallosh boundary contributes no occurrences to these totals.','',
table(['Speaker','Items'],sorted(Counter(speaker(x) for x in items).items())),'',
'### Counts by primary area','',
'Each item is assigned exactly one primary area for this table, so the counts sum to the occurrence total. Cross-links remain many-to-many; the area assignment is supplied separately in `GY1978_item_areas.json`.','',
table(['Primary area','Items'],sorted(Counter(area(x) for x in items).items())),'',
'### Independent assessment axes','']
for field in ['literal_correctness','publication_match','verification','development']:
 lines += ['**'+field.replace('_',' ').capitalize()+'**','',table(['Value','Items'],sorted(Counter(x[field] for x in items).items())),'']
lines += ['**Correction types**','',table(['Type','Rows'],sorted(Counter(x['type'] for x in corrections).items())),'',
'A class E entry can contain a false literal formula, and a class B entry can have only a partial publication match. Neither historical class nor a verified URL asserts that every sentence in a source was read or is mathematically correct. The bibliography `annote` fields and research logs specify the limits.','',
'## 2. What was difficult and what changed the conclusions','',
'### Source boundaries and historical aliases','',
'The manuscript headings required reassignment of several overlapping catalogue page ranges. P000812 begins with a syllabus before Belavin’s lecture; P000823 is Beilinson’s intervention, while P000824 begins Fuchs. P000830 begins Ogievetsky and P000834 begins Lebedev. On P000839 Shabat’s web discussion gives way to a separately named Zamolodchikov discussion, continued on P000840. P000842 continues the equations of Kallosh’s P000841 despite its misleading catalogue association. These are provenance corrections, not conjectural mathematical reconstructions.','',
'The earlier occurrence index is not a clean chronological authority. Several blocks index these same pages under 1977 identifiers. The following migration map records overlapping content at the finer granularity of this chapter. A one-to-many row is a split of an earlier compound item, not several independent recurrences. The old identifiers remain aliases for compatibility.','',
table(['Earlier identifier','Current occurrence(s)'],[(a['previous_id'],', '.join(a['current_ids'])) for a in aliases]),'',
'Earlier identifiers 1977-457.8–16 concern the missing intervening Fuchs pages and receive no invented replacements here. They may remain in their earlier database location pending a separate source migration. The supplied previous index also assigns GP-1977-01 to both projective-bundle algebra and nonarithmetic complex-hyperbolic lattices, and GP-1977-02 to both twisting by \\(\\mathcal O(1)\\) and the first Gelfand–Dickey Jacobi problem. Those are identifier collisions, not evidence that the problems coincide. They should be resolved by a corpus-level migration; this chapter does not silently choose one meaning.','',
'The connection from the quantum transfer-matrix material to 1977-436.16 and GP-1977-10 is thematic. It does not make the finite XYZ spectral question or the literal spin-one deformation question the same problem as constructing a general quantum inverse-scattering formalism. Similarly, the request for a “beautiful” ADHM parametrization does not supply the rationality, global-coordinate or connectedness quantifiers of a different question.','',
'### Publication is different from first circulation','',
'The fate assignments separate public preprint dates, journal dates and receipt dates. A receipt stamp establishes that a manuscript existed; it does not establish public circulation. The Zakharov–Mikhailov variational paper was received 3 October 1978 and published in 1980: the action and its rational-family development are matched to that later publication, while elementary compatibility and earlier inverse-scattering background remain exposition. The Delorme–Blanc smooth-vector theorem is attributed in the notes, but the available receipt/revision evidence alone does not establish a pre-talk public date for Blanc’s full result. Its later published development is recorded accordingly.','',
'Conversely, the 1979 Fateev–Frolov–Schwarz paper identifies an instanton-measure formula already announced by Frolov and Schwarz in 1978. Guichardet’s relevant semidirect-product work has an identifiable June 1978 preprint before its 1979 journal version. These cases show why a journal-year comparison alone would misclassify exposition as a new seminar result. Relevant citations and exact locators are given in the occurrence entries and their bibliography audit annotations.','',
'The most consequential late repair is web algebraization. Chern and Griffiths’s 1978 argument was explicitly corrected in 1981: the correction acknowledges incorrect divisibility lemmas and a separate gap, retaining a theorem with an extra normality assumption. Trépreau’s Theorem 1.1 proves the unrestricted regular holomorphic maximal-rank statement for \\(n\\ge 3\\) and \\(d\\ge 2n\\); its preprint was posted 4 August 2005 and its book chapter version appeared in 2006. The primary correction and the exact statements and hypotheses of Trépreau’s theorems were read; the complete algebraization proof was not independently audited. Beauville’s February 1979 exposition is evidence of what was then asserted, not evidence that the later gap was already repaired (Chern & Griffiths, 1981, pp. 78–79; Trépreau, 2006, Theorem 1.1).','',
'### Literal formulas, conventions and incomplete questions','',
'Several errors survive comparison with the scans and must be called mathematical emendations, not transcription corrections. They include the Gaussian-tail series, an unfinished exponential recursion, determinant and heat-trace signs, zero-curvature derivative/commutator conventions, the literal spin-one coupling ratio, the contact bracket, and rank/dimension qualifications in the geometric statements. When a glyph remains doubtful the correction is marked ambiguous; a mathematically plausible repair is not substituted as a claimed manuscript reading.','',
'The spin-one audit fixes the real skew-generator convention before testing the density. Its cubic obstruction excludes analytic regular difference-form \\(R\\)-matrices for the printed coefficient, including nonzero rescaling and added identity. It does not exclude every possible meaning of integrability. The familiar anisotropic spin-one model is a partial match to a corrected density, not a solution of the literal printed problem.','',
'The area audit separates a Hamilton–Jacobi identity from a minimum-area assertion. A curve with the same oriented coordinate areas as the planar unit circle has every spanning area at least \\(\\pi\\sqrt{1+\\varepsilon^2}>\\pi\\). A vague qualification such as “not too twisted” supplies no checkable hypothesis that would restore the equality. The calculation does not refute the separate Hamilton–Jacobi identity; an initially tempting three-coordinate differentiation would miss a transverse self-dual derivative.','',
'In the ambitwistor correspondence, holomorphic triviality on every incidence quadric is retained explicitly. The checked Mason–Skinner review uses overbroad Chern-class shorthand; \\(\\mathcal O(1,0)\\oplus\\mathcal O(-1,0)\\) on \\(\\mathbb P^1\\times\\mathbb P^1\\) has \\(c_1=c_2=0\\) but is not holomorphically trivial. The original Beilinson page supplies the required fibrewise triviality. Reading a modern source critically is as necessary as reading the notebook critically.','',
'The period-three bracket in Fuchs’s fragment has an explicit realization in the loop algebra of \\(\\mathfrak{sl}_2\\). Its graded simplicity must be separated from ordinary simplicity, which fails because evaluation has a proper kernel. The grading also fails a local-generation hypothesis used in the nearby classification theorem. These distinctions prevent an unjustified exact match to an exhaustion claim.','',
'## 3. Problem selection and completed critical work','',
table(['Problem identifier','Question'],[(p['id'],p['title']) for p in problems]),'',
'The problem index includes precise historical questions even when solved. Its status fields preserve the difference between the literal question and a corrected nearby one. It contains no open-problem entry for an unspecified multiplication law, an aesthetic parametrization, an incomplete Bessel-function claim, or an undefined universality assertion. None has enough quantifiers to support a bounded research problem.','',
'The `GY1978_development.tex` file contains critical audits rather than a manufactured Stage 2 research development. The following table records both the proof or computation and an independent check. Classical facts are not claimed as new discoveries.','',
table(['Audit','Complete argument or exact calculation','Independent check and limit'],[
('Gaussian tail','Integration by parts gives the finite expansion, signed remainder and strict next-term bound for every real \\(x>0\\) and integer \\(N\\ge 1\\).','An independently derived differential equation gives the coefficients; exact residuals and 80-digit checks corroborate the proof. Finite tests are not a proof of universal convergence.'),
('Omnific fractions','A set-sized normal-form support is shifted by a sufficiently large positive exponent; numerator and denominator then lie in \\(\\mathbf{Oz}\\).','The stated normal-form characterization is an assumption, not reproved. Cancellation shifts every exponent back; a separate mathematical review checks the set-size and denominator conditions.'),
('Projected areas','A 1-Lipschitz cylinder projection and a closed 2-form of bounded comass yield the strict quantitative area bound.','Boundary flux is recomputed symbolically; a separate derivation checks the comass and projection estimate. No Plateau-existence assertion is needed.'),
('Spin-one density','The full cubic coefficient argument gives the necessary \\(R\\)-matrix condition; an explicit six-word tensor calculation gives \\(t(t-1)(t+1)\\).','Skew generators, epsilon-index contraction and an independently built permutation/contraction tensor agree. Passing controls are not called sufficient.'),
('Contact bracket','The generic three-variable Jacobiator is computed, and the corrected convention is proved in every odd dimension by contact vector fields.','Independent coordinate/polynomial checks agree; contraction with the contact form and all signs were re-derived separately.'),
('Rational R and Ising encoding','Permutation identities prove the rational Yang–Baxter family; elementary reconstruction proves exactly two parity-even spin lifts.','Exact \\(8\\times 8\\) symbolic matrices and exhaustive 16-state enumeration corroborate the proofs. Boundary and torus-sector conditions remain explicit.'),
('Period-three bracket','The nine residue-class relations identify the loop-\\(\\mathfrak{sl}_2\\) basis and its grading.','An independent \\(2\\times 2\\) matrix calculation checks 625 ordered pairs and exponent addition; the proof for all indices is the residue-class reduction.')]),'',
'The remaining work suggested by an F item is normally source identification: obtain another record of the talk, resolve a coefficient, recover the omitted operation, or state a limiting regime. The chapter does not describe those missing specifications as mathematical obstructions already shown to be open. A further research run would first have to establish a precise new statement.','',
'## 4. Search and verification method','',
'Research proceeded from the Russian transcription and manuscript formula to an exact modern formulation, then to a publication with matching hypotheses. Searches combined speaker names, formula terminology, exact titles, equation numbers, and retrospective references. Math-Net and original Soviet journal scans were especially effective for short announcements and receipt lines. Author-deposited arXiv versions supplied full results and version dates; publisher records supplied journal metadata. Original published corrections were checked when later proofs reported a gap. Cumulative bibliography keys were reused whenever the same work was already present.','',
'The cumulative bibliography contains 896 entries but 749 unique keys; it was therefore parsed as an inventory rather than concatenated into this chapter. The delivered bibliography has unique keys. Duplicate references found by independent researchers were merged, preferring the more explicit audit annotation. A URL marked verified means it was opened; the separate item verification field records whether the mathematical result was actually read, only metadata checked, an attribution indirect, or a lead unresolved. Unverified entries remain labelled unverified and are not promoted to full-text verification.','',
table(['Bibliography link status','Entries'],sorted(Counter(e['fields'].get('note','') for e in refs).items())),'',
'Not every suggested search service was accessible, and no claim of exhaustive zbMATH or Google Scholar coverage is made. Failed publisher retrievals, image-only PDFs and indirect historical citations are recorded in the research logs and `annote` fields. The absence of a hit never establishes nondevelopment. Exact-result locators and scope take precedence over a broad thematic similarity.','',
'Per-area search logs and source-read limits are included in `code/research_logs/`. The mathematical checking programs and their outputs are in `code/`; downloaded articles, scan thumbnails and unrelated temporary files are excluded from the deliverable.','',
'## 5. What the classification misses; proposed format changes','',
'The A–F classes compress different questions. A statement can be old, false in its notebook notation, correctly reconstructed, and only partly matched to a later paper. This chapter uses the separate assessment fields for that distinction. F sometimes records an identifiable false formula whose intended published correction is unknown; the falsehood itself is not unidentified.','',
'Useful additions to the common schema are: a structured chronology object with separate manuscript-received, first-public-circulation and publication dates and evidence for each; a source-boundary object with page subregions and catalogue disagreements; an alias relation distinguishing same-source overlap from genuine recurrence; a per-reference verification record with exact version, locator and access result; and explicit links between a literal item, a corrected statement and the audit proving the difference. An item may also need more than one fate edge when different components of a compound notebook sentence have different histories.','',
'The current free-text pages field can state a catalogue range and an actual range, but a website should not have to parse that prose. Add `source_pages`, `catalogue_pages`, `source_segments`, `attribution_basis` and `scope` as structured fields. Preserve the current required fields so existing yearly builders remain compatible. The supplied auxiliary coverage and alias JSON files demonstrate these relations without altering the requested occurrence schema.','',
'## 6. Website presentation for this year','',
'A reader arriving at a talk should first see its actual source span, a short subject summary, any catalogue discrepancy, and a concise account of what the lecture contributes. Offer direct access to the Russian wording and scan segment alongside the English statement. Where a page contains two speakers, label the intervention before displaying the item; the late Zamolodchikov contribution must not appear as a web theorem of Shabat.','',
'For each item show the notebook statement, the modern formulation and the reconstruction as distinct panels. Put historical class beside the literal-correctness and verification badges; avoid a single green “verified” label. A partial publication match should open a comparison of the two statements, including the changed coefficient, category, field, boundary condition or quantifier. The equation audit should be one click away from the corresponding false-as-written badge.','',
'The key cross-links are Kruskal arithmetic → exponential → asymptotic integration; Polyakov Toda → Zakharov flatness/variational principle; Belavin exchange algebra → transfer matrices → the spin-one audit → Zamolodchikov vertex contractions; ADHM → twistor/ambitwistor geometry; and Shabat maximal rank → the 1981 correction → Trépreau’s proof. Link to earlier inverse-scattering and instanton programmes as thematic connections. Route old source aliases directly to the current item with an explanation, without rendering a false sequence of repeated seminar appearances.','',
'The problem page should show the exact question first, then dated status, occurrences, and later works. For GP-1978-10 it should display both the excluded literal density and the corrected anisotropic model; for web algebraization it should show the extra normality assumption in 1981 and its removal in the later theorem. Search should index mathematical synonyms and transliterations, but never merge similarly named problems without comparing their hypotheses.','',
'## 7. Reproduction and validation','',
'The source data are the seven files prescribed by CHAPTER_FORMAT.md, with the separate report. `build_chapter.py`, `gelfand_companion.sty` and the format guide are included. The chapter and driver are generated from the data. Run `python code/build_validate.py` from an unpacked directory to execute the supplied builder and the sequence XeLaTeX, BibTeX, XeLaTeX, XeLaTeX. The helper can create a workspace-only XeLaTeX format when installed TeX packages lack their format cache; it does not modify the system installation.','',
'Exact symbolic checks require Python with SymPy; the Gaussian numerical corroboration additionally uses mpmath. Their version numbers and complete outputs are recorded with the checking programs. `code/build_logs/` records the schema and compiler runs. `code/validation_output.txt` records independent enum, bibliography and bidirectional problem-link checks. PDF text and layout were inspected after compilation, with attention to displayed formulas, Russian quotations, long headings, bibliography and correction entries.','',
'The absence of missing-page reconstruction, the explicitly unverified bibliography leads and the limited meanings of finite computations are deliberate scope statements, not unresolved build failures.','']

(D/'GY1978_report.md').write_text('\n'.join(lines))
print('Wrote report, overview, 54-page coverage, aliases and primary-area mapping.')
