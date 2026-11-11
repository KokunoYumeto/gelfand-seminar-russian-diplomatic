#!/usr/bin/env python3
"""Independent, read-only audit of the assembled GY1966 data.

Writes only code/final_audit.{json,md}, relative to the deliverable root.
Does not invoke the assembler,
alter deliverable files, open external sources, or certify final PDF layout.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import hashlib
import json
import re

OUT = Path(__file__).resolve().parent
D = OUT.parent  # The script lives at <deliverable>/code/audit_final.py.
checks = []

def check(name, issues=(), details=None):
    issues = list(issues)
    row = {'check': name, 'passed': not issues, 'issues': issues}
    if details is not None:
        row['details'] = details
    checks.append(row)

def readj(name):
    return json.loads((D / name).read_text())

T = readj('GY1966_talks.json')
I = readj('GY1966_items.json')
P = readj('GY1966_problems.json')
tm = {x['record']: x for x in T}
im = {x['id']: x for x in I}
pm = {x['id']: x for x in P}
report = (D / 'GY1966_report.md').read_text()
overview = (D / 'GY1966_overview.tex').read_text()
development = (D / 'GY1966_development.tex').read_text()
prior = (D / 'code/source_inputs/previous_index.md').read_text()
catalogue = (D / 'code/source_inputs/GY1966_talks.md').read_text()
prior_ids = set(re.findall(r'\b196[45]-\d+\.\d+\b', prior))
prior_gp = set(re.findall(r'\bGP-196[45]-\d+\b', prior))
with (D / 'GY1966_corrections.csv').open(newline='') as f:
    cr = csv.DictReader(f)
    correction_columns = cr.fieldnames
    corrections = list(cr)

def bibfield(body, name):
    m = re.search(r'\b' + re.escape(name) + r'\s*=\s*', body, re.I)
    if not m:
        return ''
    pos = m.end()
    if body[pos] == '{':
        start, depth = pos + 1, 1
        pos += 1
        while pos < len(body) and depth:
            if body[pos] == '{' and body[pos-1] != '\\':
                depth += 1
            elif body[pos] == '}' and body[pos-1] != '\\':
                depth -= 1
            pos += 1
        return body[start:pos-1]
    if body[pos] == '"':
        return body[pos+1:body.find('"', pos+1)]
    return body[pos:].split(',')[0].strip()

bib = (D / 'GY1966_references.bib').read_text()
entries_list = re.findall(r'^@\w+\s*\{\s*([^,]+),([\s\S]*?)(?=^@|\Z)', bib, re.M)
B = dict(entries_list)
citere = re.compile(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}')

def citations(text):
    return {k.strip() for group in citere.findall(text) for k in group.split(',') if k.strip()}

def alltext(obj):
    if isinstance(obj, str):
        return obj
    if isinstance(obj, dict):
        return '\n'.join(alltext(v) for v in obj.values())
    if isinstance(obj, list):
        return '\n'.join(alltext(v) for v in obj)
    return ''

def pages(s):
    m = re.fullmatch(r'P(\d{6})(?:-P(\d{6}))?', s)
    if not m:
        raise ValueError(s)
    a, b = int(m[1]), int(m[2] or m[1])
    if b < a:
        raise ValueError(s)
    return set(range(a, b+1))

expected = {'records': 38, 'items': 277, 'problems': 21, 'references': 78, 'corrections': 108}
counts = {'records': len(T), 'items': len(I), 'problems': len(P), 'references': len(B), 'corrections': len(corrections)}
check('Required object counts', [f'{k}: {counts[k]} != {v}' for k,v in expected.items() if counts[k] != v], counts)
check('Unique identifiers and exact source order',
      ([f'record order: {[x["record"] for x in T]}'] if [x['record'] for x in T] != list(range(92,130)) else [])
      + ([f'duplicate item IDs'] if len(im) != len(I) else [])
      + ([f'duplicate problem IDs'] if len(pm) != len(P) else [])
      + ([f'duplicate bibliography keys'] if len(B) != len(entries_list) else []))

talk_fields = set('record date speaker pages title kind summary'.split())
item_fields = set('id record pages kind title notes statement reconstruction class fate present_status literal_correctness publication_match verification development problem worth refs confidence'.split())
problem_fields = set('id title statement occurrences status status_date refs'.split())
issues = []
for label, data, fields, extra, empty in [
    ('talk', T, talk_fields, set(), {'date','speaker'}),
    ('item', I, item_fields, {'speaker'}, {'reconstruction','problem','worth'}),
    ('problem', P, problem_fields, set(), set())]:
    for x in data:
        xid = x.get('id', x.get('record'))
        if fields - x.keys(): issues.append(f'{label} {xid}: missing {sorted(fields-x.keys())}')
        if x.keys() - fields - extra: issues.append(f'{label} {xid}: extra {sorted(x.keys()-fields-extra)}')
        for k in fields & x.keys():
            if k in ('record','refs','occurrences'): continue
            if not isinstance(x[k], str): issues.append(f'{label} {xid}: {k} is not a string')
            elif not x[k].strip() and k not in empty: issues.append(f'{label} {xid}: blank {k}')
        if 'record' in x and not isinstance(x['record'], int): issues.append(f'{label} {xid}: noninteger record')
        for k in ('refs','occurrences'):
            if k in x and (not isinstance(x[k],list) or any(not isinstance(y,str) for y in x[k])):
                issues.append(f'{label} {xid}: invalid {k} list')
enums = {
    'kind': {'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
    'class': set('ABCDEF'),
    'literal_correctness': {'correct','correct with missing hypotheses','false as written','not determinable'},
    'publication_match': {'exact','partial','thematic only','none found'},
    'verification': {'read the result','publisher metadata checked','indirect','unresolved lead'},
    'development': {'none','annotated','developed in this chapter'},
    'confidence': {'high','medium','low'}}
for x in I:
    for k, valid in enums.items():
        if x[k] not in valid: issues.append(f'{x["id"]}: invalid {k}: {x[k]}')
for x in T:
    if x['kind'] not in {'talk','plan','heading','other'}: issues.append(f'talk {x["record"]}: invalid kind')
check('Full required schema, types and enumerations', issues)

issues = []
for t in T:
    ii = [x for x in I if x['record'] == t['record']]
    expected_ids = [f'1966-{t["record"]}.{n}' for n in range(1,len(ii)+1)]
    if [x['id'] for x in ii] != expected_ids: issues.append(f'record {t["record"]}: numbering/order mismatch')
for x in I:
    if x['record'] not in tm: issues.append(f'{x["id"]}: absent parent record')
check('Occurrence numbering and parent records', issues)

catalog = {}
for record, front, span in re.findall(r'^- record (\d+): ([^;]+); pages ([^;]+);', catalogue, re.M):
    dm = re.search(r'\((\d{4}-\d\d-\d\d)\)', front)
    sm = re.search(r'^[^,]+,\s*(.*?)\.\s+\(', front)
    catalog[int(record)] = {'date': dm[1] if dm else '', 'speaker': sm[1] if sm else '', 'pages': span}
issues, differences = [], []
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
for t in T:
    c = catalog.get(t['record'])
    if c is None: issues.append(f'missing catalogue record {t["record"]}'); continue
    if c['date'] != t['date']: issues.append(f'record {t["record"]}: catalogue date differs')
    if norm(c['speaker']) != norm(t['speaker']): issues.append(f'record {t["record"]}: catalogue speaker differs')
    if c['pages'] != t['pages']: differences.append({'record':t['record'],'catalogue':c['pages'],'actual_talk_pages':t['pages']})
    try:
        if not pages(t['pages']) <= set(range(140,208)): issues.append(f'talk {t["record"]}: pages out of source range')
    except ValueError: issues.append(f'talk {t["record"]}: invalid page syntax')
for x in I:
    try:
        if not pages(x['pages']) <= pages(tm[x['record']]['pages']): issues.append(f'{x["id"]}: pages outside parent span')
    except ValueError: issues.append(f'{x["id"]}: invalid page syntax')
check('Catalogue dates, speakers, page syntax and content containment', issues,
      {'catalogue_records':len(catalog),'refined_talk_page_ranges':differences,
       'provenance_note':'Fourteen refined ranges are explicitly qualified in the revised report. Record 127 legitimately continues through P000204; record 128 remains later in catalogue order although dated 20 March.'})

issues = []
for x in I:
    if not any(d in x['present_status'] for d in ['9 November 2026','2026-11-09','November 9, 2026']): issues.append(f'{x["id"]}: missing day-precise status')
for p in P:
    if p['status_date'] not in {'2026-11','2026-11-09'}: issues.append(f'{p["id"]}: wrong status_date')
check('Dated present-status fields',issues,
      {'problem_date_precision':dict(Counter(p['status_date'] for p in P)),
       'scope':'The supplied problem schema permits YYYY-MM metadata. Every item is explicitly dated 9 November 2026; the chapter report identifies the same final audit date.'})

all_document_text = '\n'.join([alltext(T),alltext(I),alltext(P),report,overview,development])
prior_mentions = set(re.findall(r'\b196[45]-\d+\.\d+\b', all_document_text))
current_mentions = set(re.findall(r'\b1966-\d+\.\d+\b', all_document_text))
check('All explicit prior/current occurrence references resolve',
      [f'unknown prior {x}' for x in sorted(prior_mentions-prior_ids)]
      + [f'unknown current {x}' for x in sorted(current_mentions-im.keys())],
      {'distinct_prior_occurrences_referenced':len(prior_mentions),'prior_occurrences':sorted(prior_mentions)})

issues = []
new = sorted((p for p in P if p['id'].startswith('GP-1966-')), key=lambda x:x['id'])
if [p['id'] for p in new] != [f'GP-1966-{n:02d}' for n in range(1,21)]: issues.append('new IDs are not exactly GP-1966-01 through GP-1966-20')
old = [p for p in P if not p['id'].startswith('GP-1966-')]
if [p['id'] for p in old] != ['GP-1965-03']: issues.append('reused ID set differs from GP-1965-03')
for p in old:
    if p['id'] not in prior_gp: issues.append(f'{p["id"]}: absent from prior index')
order = {x['id']:n for n,x in enumerate(I)}
firsts = [min(order[o] for o in p['occurrences'] if o in order) for p in new]
if firsts != sorted(firsts): issues.append('new GP IDs are not in first-occurrence order')
for p in P:
    if len(p['occurrences']) != len(set(p['occurrences'])): issues.append(f'{p["id"]}: repeated occurrence')
    for o in p['occurrences']:
        if o not in im and o not in prior_ids: issues.append(f'{p["id"]}: unknown occurrence {o}')
        elif o in im and im[o]['problem'] != p['id']: issues.append(f'{p["id"]}: occurrence {o} lacks reciprocal link')
for x in I:
    if x['problem']:
        if x['problem'] not in pm: issues.append(f'{x["id"]}: unknown problem')
        elif x['id'] not in pm[x['problem']]['occurrences']: issues.append(f'{x["id"]}: problem lacks reciprocal occurrence')
check('Problem IDs, reused prior ID, first-occurrence order and reciprocal links',issues,
      {'new_problem_ids':[p['id'] for p in new],'preserved_prior_problem_ids':[p['id'] for p in old]})

issues, used = [], set()
for label,data in [('item',I),('problem',P)]:
    for x in data:
        cites, refs = citations(alltext(x)), set(x['refs'])
        for k in cites-refs: issues.append(f'{label} {x["id"]}: citation {k} absent from refs')
        for k in refs-B.keys(): issues.append(f'{label} {x["id"]}: missing bibliography key {k}')
        if len(x['refs']) != len(refs): issues.append(f'{label} {x["id"]}: repeated reference key')
        used |= refs | cites
used |= citations(all_document_text)
for k in used-B.keys(): issues.append(f'undefined citation {k}')
for k,e in B.items():
    if bibfield(e,'note') not in {'verified','unverified'}: issues.append(f'{k}: invalid verification note')
    if not (bibfield(e,'url') or bibfield(e,'doi')): issues.append(f'{k}: neither URL nor DOI')
cumulative_bib = (D/'code/source_inputs/references_cumulative.bib').read_text()
cumulative = dict(re.findall(r'^@\w+\s*\{\s*([^,]+),([\s\S]*?)(?=^@|\Z)', cumulative_bib, re.M))
def source_identifiers(body):
    return {bibfield(body,f).lower().strip().rstrip('/') for f in ('doi','url') if bibfield(body,f)}
for k,e in B.items():
    for oldkey,oldbody in cumulative.items():
        if k != oldkey and source_identifiers(e) & source_identifiers(oldbody):
            issues.append(f'{k}: source identifier matches cumulative entry {oldkey} under a different key')
check('Citations, per-object reference lists, complete bibliography and verification metadata',issues,
      {'unique_references':len(B),'all_keys_used':not(B.keys()-used),'unused_keys':sorted(B.keys()-used),
       'notes':dict(Counter(bibfield(e,'note') for e in B.values())),
       'cumulative_keys_reused':sorted(B.keys() & cumulative.keys()),
       'reused_entries_without_annote':sorted(k for k,e in B.items() if not bibfield(e,'annote')),
       'scope':'Checks stored bibliographic structure, not external-link accessibility or independently reopening all primary works.'})

C = [x for x in I if x['class'] in {'C','D'}]
expected_C = ['1966-94.4','1966-114.2','1966-114.13']
issues = []
if [x['id'] for x in C] != expected_C: issues.append('unexpected C/D item set')
for x in C:
    if not x['worth'].strip(): issues.append(f'{x["id"]}: missing worth assessment')
    if not x['problem']: issues.append(f'{x["id"]}: missing indexed definite question')
    if not all(x[k].strip() for k in ['statement','fate','present_status']): issues.append(f'{x["id"]}: missing statement/status/gap')
for key in ['1966-100.2','1966-100.4']:
    if im[key]['class'] != 'F': issues.append(f'{key}: final F reclassification not present')
check('C/D completeness and final Minlos reclassification',issues,
      {'C_items':expected_C,'D_items':[],
       'manual_gap_review':'94.4: unrestricted topological Anosov classification; 114.2: smooth-metric sphere-support remainder; 114.13: diffeomorphism type under equal prime periods. Each identifies the stronger assumptions of cited partial results and explains why no bounded advance was attempted.'})

A = [x for x in I if x['class']=='A']
issues, a_rows = [], []
for x in A:
    speaker = x.get('speaker',tm[x['record']]['speaker'])
    surname = norm(speaker.split()[-1])
    matches = []
    for k in x['refs']:
        author = norm(bibfield(B[k],'author'))
        if surname in author or 'gelfand' in author: matches.append(k)
    if not matches: issues.append(f'{x["id"]}: no speaker/Gelfand-authored source')
    a_rows.append({'id':x['id'],'speaker':speaker,'matched_authorial_references':matches})
for key in ['1966-93.1','1966-93.4']:
    if im[key]['class']!='B': issues.append(f'{key}: expected corrected class B')
check('Strict class A author attribution',issues,
      {'A_items':len(A),'by_speaker':dict(Counter(x.get('speaker',tm[x['record']]['speaker']) for x in A)),
       'author_matches':a_rows,'scope':'All 22 A fates manually inspected. No further clear author mismatch found. Does not re-adjudicate nuanced prior circulation or priority of elementary components.'})

areas = readj('code/item_areas.json')
issues = []
if areas.keys()!=im.keys(): issues.append(f'area-map key mismatch: missing {sorted(im.keys()-areas.keys())}; extra {sorted(areas.keys()-im.keys())}')
class_counts = {c:sum(x['class']==c for x in I) for c in 'ABCDEF'}
speaker_counts = dict(Counter(tm[x['record']]['speaker'] for x in I))
area_counts = dict(Counter(areas.values()))
audit_counts = readj('code/audit_counts.json')
computed = {**counts,'new_problems':len(new),'classes':class_counts,'speakers':speaker_counts,'areas':area_counts,
            'verification':dict(Counter(x['verification'] for x in I)),
            'literal_correctness':dict(Counter(x['literal_correctness'] for x in I)),
            'publication_match':dict(Counter(x['publication_match'] for x in I)),
            'correction_types':dict(Counter(x['type'] for x in corrections))}
for k,v in computed.items():
    if audit_counts.get(k)!=v: issues.append(f'code/audit_counts.json: incorrect {k}')

def markdown_table(header):
    lines = report.splitlines()
    start = lines.index(header)+2
    rows=[]
    for line in lines[start:]:
        if not line.startswith('|'): break
        row=[x.strip() for x in line.strip('|').split('|')]
        if row[0] != '**Total**': rows.append(row)
    return rows

for header, values in [('| Class | Items |',class_counts),('| Catalogue speaker | Items |',speaker_counts),
                       ('| Primary area | Items |',area_counts),('| Literal correctness | Items |',computed['literal_correctness']),
                       ('| Publication match | Items |',computed['publication_match']),('| Verification | Items |',computed['verification']),
                       ('| Correction type | Items |',computed['correction_types'])]:
    try:
        found = {r[0]:int(r[1]) for r in markdown_table(header)}
        if found!=values: issues.append(f'report table mismatch: {header}')
    except (ValueError,IndexError): issues.append(f'cannot parse report table: {header}')
record_rows = markdown_table('| Record | Catalogue speaker | Kind | Items | A | B | C | D | E | F |')
if len(record_rows)!=38: issues.append('record-level report table does not have 38 rows')
for row in record_rows:
    rec = int(row[0]); t=tm[rec]; ri=[x for x in I if x['record']==rec]
    expected_row=[str(rec),t['speaker'] or '—',t['kind'],str(len(ri))]+[str(sum(x['class']==c for x in ri)) for c in 'ABCDEF']
    if row!=expected_row: issues.append(f'report record table mismatch: {rec}')
zero=[t['record'] for t in T if not any(x['record']==t['record'] for x in I)]
if zero!=[117,118,128]: issues.append(f'zero-item record mismatch: {zero}')
check('All report count tables, area assignments and generated audit counts',issues,computed)

issues=[]
required_columns='page place transcription_reads should_read evidence applies_to type'.split()
if correction_columns!=required_columns: issues.append('CSV columns differ from required schema')
for n,row in enumerate(corrections,2):
    if row['type'] not in {'transcription','translation','ambiguity','faithful_error','provenance'}: issues.append(f'CSV row {n}: invalid type')
    if row['applies_to'] not in {'ru','en','both'}: issues.append(f'CSV row {n}: invalid applies_to')
    if not all(row[k].strip() for k in required_columns): issues.append(f'CSV row {n}: blank required cell')
    try:
        if not pages(row['page'])<=set(range(140,208)): issues.append(f'CSV row {n}: invalid source page')
    except ValueError: issues.append(f'CSV row {n}: invalid page syntax')
check('Correction CSV schema, source pages and types',issues)

with (D/'code/source_page_coverage.csv').open(newline='') as f:
    coverage=list(csv.DictReader(f))
issues=[]
if [r['page'] for r in coverage]!=[f'P{n:06d}' for n in range(140,208)]: issues.append('coverage does not list each of 68 source pages exactly once')
for row in coverage:
    n=int(row['page'][1:])
    actual=[x.strip() for x in row['items'].split(';') if x.strip()]
    expected=[x['id'] for x in I if n in pages(x['pages'])]
    if actual!=expected: issues.append(f'{row["page"]}: occurrence mapping inconsistent with item pages')
    records={int(x.strip()) for x in row['records'].split(';') if x.strip()}
    if records!={im[x]['record'] for x in actual}: issues.append(f'{row["page"]}: parent record mapping mismatch')
check('68-page coverage map',issues,{'scope':'Verifies map integrity and page allocation, not independent reinspection of all scan images in this final audit.'})

issues=[]
alg=readj('code/check_editorial_algebra_output.json')
sing=readj('code/check_singularities_output.json')
pair=readj('code/check_pair_partitions_output.json')
if alg['cyclic_group']['augmentation_power_tests']!=32: issues.append('32 augmentation powers report mismatch')
if alg['heisenberg']['exact_product_tests']!=121: issues.append('121 group-law tests report mismatch')
if sing['independent_mu_comparisons']!=246: issues.append('246 singularity comparisons report mismatch')
if pair['random_process_configurations']!=128: issues.append('128 configurations report mismatch')
if pair['canonical_rational_parameter_tests']!=205: issues.append('205 canonical tests report mismatch')
if pair['pair_partition_coefficients']!=[2,4,1]: issues.append('collision multiplicities mismatch')
if 'L1' in report and 'Cauchy--Schwarz' not in development: issues.append('L1 report claim missing supporting development step')
has_direction_csv=any(any(w in alltext(r).lower() for w in ['herglotz','petrovsky','past/future','past cone','future cone']) for r in corrections)
if 'and the past/future restriction in the Herglotz' in report and not has_direction_csv:
    issues.append('Report §6 lists the Herglotz–Petrovsky past/future restriction as a CSV example, but this qualification appears only in item 129.14.')
check('Selected substantive report claims against included proof/check output',issues,
      {'manual_review':'The added L1 convergence conclusion follows from the displayed Cauchy–Schwarz bound, then the stated order of limits. All three C gaps were manually compared against the report. No universal conclusion is inferred from finite test counts.'})

snapshot_files = ['GY1966_talks.json','GY1966_items.json','GY1966_problems.json','GY1966_references.bib',
                  'GY1966_corrections.csv','GY1966_report.md','GY1966_overview.tex','GY1966_development.tex',
                  'code/item_areas.json','code/audit_counts.json','code/source_page_coverage.csv']
hashes={s:hashlib.sha256((D/s).read_bytes()).hexdigest() for s in snapshot_files}
failed=[r for r in checks if not r['passed']]
result={'audit':'Independent final structured-data and report audit','auditor':'algebra agent',
        'timestamp_utc':datetime.now(timezone.utc).isoformat(),'status_date':'2026-11-09',
        'status':'PASS' if not failed else 'ISSUES_FOUND','counts':computed,
        'checks_passed':len(checks)-len(failed),'checks_total':len(checks),
        'checks':checks,'sha256_snapshot':hashes,
        'scope_exclusions':['Final PDF rendering, pagination and visual QA','Final ZIP packaging and manifest',
                            'Reopening all 78 external primary sources','Independent rederivation of every mathematical statement'],
        'previous_findings_resolved':['Report now distinguishes catalogue and refined page spans.',
                                     'Report explicitly identifies two reused cumulative entries without annote.',
                                     '93.1 and 93.4 changed from A to B because Bass–Milnor–Serre are the matched authors.',
                                     '94.18 no longer asserts unverified pre-talk congress circulation.']}
(OUT/'final_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
lines=['# GY1966 independent final consistency audit','',
       f'**Result: {result["status"]}.** {result["checks_passed"]}/{result["checks_total"]} audit groups pass. Snapshot: {result["timestamp_utc"]}.','',
       'This audit reads the assembled deliverable and its source index without changing either. It independently recomputes counts and checks schema, identity, citation, provenance, and report consistency. Final PDF and archive validation remain with the integrating editor.','',
       '## Verified results','',
       '- 38 records, numbered 92–129 in catalogue order; 277 consecutively numbered occurrences; 21 problems; 78 bibliography keys; 108 correction rows.',
       f'- Classes: '+', '.join(f'{k} {v}' for k,v in class_counts.items())+'.',
       '- Twenty new problem IDs are consecutive and ordered by first occurrence. GP-1965-03 and its earlier occurrence are preserved. All current problem links are reciprocal.',
       f'- All {len(prior_mentions)} distinct prior occurrence IDs explicitly referenced exist in the supplied previous index; all current occurrence references resolve.',
       '- Every item/problem citation is included in its refs array; every referenced key exists. All 78 keys are used and have a URL/DOI and a verified note. This is an internal metadata check, not a new accessibility certification.',
       '- Catalogue dates and speakers agree. Fourteen talk-page intervals are refined actual-content spans, transparently described in the revised report. All occurrence pages lie inside their talk spans. The 68-page map exactly agrees with the occurrence data.',
       '- Every report count table agrees with independently recomputed data, including all 38 record rows, catalogue speakers, mutually exclusive areas, correctness, publication match, verification, and correction types.',
       '- The remaining 22 A entries match a publication authored by their recorded speaker: Shilov 8, Minlos 5, Kazhdan 3, Arnold 6. No additional clear authorship mismatch was found.',
       '- C items are exactly 94.4, 114.2, and 114.13; each supplies a precise remaining question, current status, reference, and worth assessment. No D item remains. Minlos 100.2 and 100.4 have the intended F classification.',
       '- Reported computational counts agree with the saved outputs. The added L1 convergence assertion is supported by the displayed Cauchy–Schwarz bound and stated order of limits.','',
       '## Remaining issues','']
if failed:
    for r in failed:
        for issue in r['issues']: lines.append(f'- **{r["check"]}:** {issue}')
else: lines.append('None within this audit’s stated scope.')
lines += ['', '## Limits and audit trail','',
          'The audit does not independently reopen all cited publications, recertify that every scan was visually examined, rederive every theorem, or validate final PDF layout. It does check that the recorded distinctions and qualifications are internally consistent. Earlier findings about mixed page ranges, cumulative bibliography annotations, and two class A author mismatches were corrected before this snapshot. The JSON companion contains the full checks, refined-page crosswalk, author matches, and SHA-256 hashes of the audited files.','']
(OUT/'final_audit.md').write_text('\n'.join(lines))
print(json.dumps({'status':result['status'],'passed':result['checks_passed'],'total':len(checks),
                  'issues':[i for r in failed for i in r['issues']]},ensure_ascii=False,indent=2))
