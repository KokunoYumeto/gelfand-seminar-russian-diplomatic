#!/usr/bin/env python3
"""Independent schema/provenance/reference audit in addition to the supplied builder.

Run from GY1979/: python code/audit_chapter.py
Writes code/audit_output.json and fails if a required invariant is violated.
"""
from pathlib import Path
import collections
import csv
import hashlib
import json
import re
import sys

D = Path(__file__).resolve().parent.parent
TAG = 'GY1979'
errors = []
warnings = []


def require(ok, message):
    if not ok:
        errors.append(message)


def read_json(suffix):
    return json.loads((D/f'{TAG}_{suffix}.json').read_text())


def bib_entries(text):
    """Preserve complete BibTeX entries, including nested braces."""
    entries = []
    pattern = re.compile(r'@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,')
    for match in pattern.finditer(text):
        depth = 1
        p = match.end()
        while p < len(text) and depth:
            if text[p] == '{' and (p == 0 or text[p-1] != '\\'):
                depth += 1
            elif text[p] == '}' and (p == 0 or text[p-1] != '\\'):
                depth -= 1
            p += 1
        if depth:
            raise ValueError('Unbalanced BibTeX entry '+match.group(2))
        entries.append((match.group(2),text[match.start():p]))
    return entries


def page_numbers(text):
    vals = set()
    for a,b in re.findall(r'P(\d{6})\s*[-–]+\s*P?(\d{6})',text):
        vals.update(range(int(a),int(b)+1))
    vals.update(int(v) for v in re.findall(r'P(\d{6})',text))
    return vals


def main():
    talks,items,problems = (read_json(s) for s in ('talks','items','problems'))
    bib = (D/f'{TAG}_references.bib').read_text()
    entries = bib_entries(bib)
    bibkeys = [k for k,_ in entries]
    require(len(bibkeys)==len(set(bibkeys)),'Duplicate BibTeX keys')
    require(set(t['record'] for t in talks)==set(range(462,489)),
            'Must cover exactly the 27 catalog records 462 through 488')
    require(len(talks)==27,'Must have 27 talk/heading objects')
    recs = {t['record']:t for t in talks}
    require(recs[481]['kind']=='heading','Record 481 must remain a heading')
    require(recs[473]['date']=='1979-10-29','Critical date for record 473 must be 1979-10-29')
    require([t['record'] for t in talks].index(477)<[t['record'] for t in talks].index(476),
            'Manuscript source order puts record 477 before record 476')
    required = {'id','record','pages','kind','title','notes','statement','reconstruction',
                'class','fate','present_status','literal_correctness','publication_match',
                'verification','development','problem','worth','refs','confidence'}
    allowed_values = {
        'kind':{'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
        'class':set('ABCDEF'),
        'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
        'publication_match':{'exact','partial','thematic only','none found'},
        'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
        'development':{'none','annotated','developed in this chapter'},
        'confidence':{'high','medium','low'}}
    ids = [x['id'] for x in items]
    require(len(ids)==len(set(ids)),'Duplicate occurrence IDs')
    by_rec = collections.defaultdict(list)
    for x in items:
        ident=x['id']; by_rec[x['record']].append(ident)
        require(required.issubset(x),f'{ident}: missing fields {sorted(required-set(x))}')
        for k,allowed in allowed_values.items():
            require(x.get(k) in allowed,f'{ident}: illegal {k} {x.get(k)!r}')
        require(ident.startswith(f"1979-{x['record']}."),f'{ident}: wrong academic-year or record prefix')
        require(bool(page_numbers(x['pages'])),f'{ident}: no source page')
        require(page_numbers(x['pages'])<=set(range(841,917)),
                f'{ident}: item includes prior-year or next-year spillover')
        require(bool(re.search(r'2026|November',x['present_status'])),f'{ident}: undated present status')
        if x['class'] in 'CD':
            require(bool(x.get('worth')),f'{ident}: class {x["class"]} needs worth statement')
        require(set(x['refs'])<=set(bibkeys),f'{ident}: undeclared reference keys')
        citations = set()
        for text in (x.get(k,'') for k in ('notes','statement','reconstruction','fate','present_status','worth')):
            for group in re.findall(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]+)\}',text):
                citations.update(k.strip() for k in group.split(','))
        require(citations<=set(x['refs']),f'{ident}: cited keys absent from refs: {citations-set(x["refs"])}')
    for rec,seq in by_rec.items():
        require(seq==[f'1979-{rec}.{i}' for i in range(1,len(seq)+1)],f'{rec}: nonsequential IDs')
    for t in talks:
        if t['record'] not in by_rec:
            require(t['kind'] in {'heading','plan','other'},f'{t["record"]}: content talk has no items')
    pids = [p['id'] for p in problems]
    require(len(pids)==len(set(pids)),'Duplicate problem IDs')
    for p in problems:
        require(p['status_date']=='2026-11',f'{p["id"]}: wrong status date')
        require(len(p['occurrences'])==len(set(p['occurrences'])),f'{p["id"]}: duplicate occurrences')
        for occurrence in p['occurrences']:
            if occurrence.startswith('1979-'):
                require(occurrence in ids,f'{p["id"]}: missing current occurrence {occurrence}')
                if occurrence in ids:
                    x=items[ids.index(occurrence)]
                    require(x['problem']==p['id'],f'{occurrence}: problem back-reference mismatch')
        require(set(p['refs'])<=set(bibkeys),f'{p["id"]}: missing reference')
    for x in items:
        if x['problem']:
            require(x['problem'] in pids,f'{x["id"]}: unknown problem')
            if x['problem'] in pids:
                p=problems[pids.index(x['problem'])]
                require(x['id'] in p['occurrences'],f'{x["id"]}: absent from linked problem occurrences')
    ref_status={}
    for key,entry in entries:
        require(bool(re.search(r'\b(?:url|doi)\s*=\s*[{"]',entry,re.I)),f'{key}: no URL or DOI')
        m=re.search(r'\bnote\s*=\s*\{(verified|unverified)\}',entry,re.I)
        require(bool(m),f'{key}: no exact verified/unverified note')
        if m: ref_status[key]=m.group(1).lower()
    corrections=list(csv.DictReader((D/f'{TAG}_corrections.csv').open()))
    fields={'page','place','transcription_reads','should_read','evidence','applies_to','type'}
    for c in corrections:
        require(fields<=set(c),'Missing corrections column')
        require(c['applies_to'] in {'ru','en','both'},'Invalid correction applies_to')
        require(c['type'] in {'transcription','translation','ambiguity','faithful_error','provenance'},
                'Invalid correction type')
        require(bool(c['evidence'].strip()),'Correction without evidence')
    for path in D.glob(f'{TAG}_*'):
        if path.suffix in {'.json','.tex','.csv','.bib','.md'}:
            text=path.read_text()
            for token in ('TODO','TBD','PLACEHOLDER','turn0search','turn1search','【turn'):
                require(token not in text,f'{path.name}: unresolved placeholder/tool token {token}')
    report={'records':len(talks),'items':len(items),'problems':len(problems),
            'references':len(entries),'corrections':len(corrections),
            'classes':dict(sorted(collections.Counter(x['class'] for x in items).items())),
            'reference_status':dict(collections.Counter(ref_status.values())),
            'source_order':[t['record'] for t in talks],
            'record_item_counts':{str(k):len(v) for k,v in by_rec.items()},
            'errors':errors,'warnings':warnings,
            'result':'PASS' if not errors else 'FAIL'}
    (D/'code/audit_output.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    return int(bool(errors))


if __name__=='__main__':
    sys.exit(main())
