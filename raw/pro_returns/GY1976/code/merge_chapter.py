"""Merge independently authored, reviewed segments without changing the core schema.

Reproduce from the archive root:
  python code/merge_chapter.py --segments code/segments --output .
The source-scope and area data are kept in sidecars, because CHAPTER_FORMAT.md
does not prescribe those fields in its seven core files.
"""
from pathlib import Path
from collections import Counter, defaultdict
import argparse
import csv
import json
import re

ORDER=[397,398,399,400,401,402,403,404,405,406,407,408,409,410,
       411,412,413,414,416,415,417,418,437]
TALK_FIELDS=['record','date','speaker','pages','title','kind','summary']
ITEM_FIELDS=['id','record','pages','kind','title','notes','statement','reconstruction',
 'class','fate','present_status','literal_correctness','publication_match','verification',
 'development','problem','worth','refs','confidence','speaker']
PROBLEM_FIELDS=['id','title','statement','occurrences','status','status_date','refs']
CORRECTION_FIELDS=['page','place','transcription_reads','should_read','evidence','applies_to','type']

def bib_entries(s):
    out={}
    for m in re.finditer(r'@\w+\s*\{\s*([^,\s]+)\s*,',s):
        key=m.group(1);i=s.index('{',m.start())+1;depth=1
        while i<len(s) and depth:
            if s[i]=='{' and s[i-1]!='\\':depth+=1
            elif s[i]=='}' and s[i-1]!='\\':depth-=1
            i+=1
        if depth:raise ValueError('Unbalanced bibliography: '+key)
        if key in out:raise ValueError('Duplicate in segment bibliography: '+key)
        out[key]=s[m.start():i]
    return out

def write_json(path,obj):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--segments',default='work')
    ap.add_argument('--output',default='deliverable/GY1976')
    a=ap.parse_args();src=Path(a.segments);out=Path(a.output)
    out.mkdir(parents=True,exist_ok=True)
    talks=[];items=[];problems=[];corrections=[];bibs={};metas={};areas={};extras={}
    duplicate_bibs=[]
    for pre in ['early','middle','late','root']:
        t=json.loads((src/f'{pre}_talks.json').read_text())
        it=json.loads((src/f'{pre}_items.json').read_text())
        pr=json.loads((src/f'{pre}_problems.json').read_text())
        meta=json.loads((src/f'{pre}_meta.json').read_text())
        metas[pre]=meta
        areas.update(meta.get('areas',{}))
        for x in it:
            if x.get('area'):areas[x['id']]=x['area']
            extra={k:v for k,v in x.items() if k not in ITEM_FIELDS}
            if extra:extras[x['id']]=extra
        talks.extend({k:x[k] for k in TALK_FIELDS if k in x} for x in t)
        items.extend({k:x[k] for k in ITEM_FIELDS if k in x} for x in it)
        problems.extend({k:x[k] for k in PROBLEM_FIELDS if k in x} for x in pr)
        with (src/f'{pre}_corrections.csv').open(newline='') as f:
            corrections.extend(csv.DictReader(f))
        for key,e in bib_entries((src/f'{pre}_references.bib').read_text()).items():
            if key in bibs:
                duplicate_bibs.append({'key':key,'later_segment':pre,'identical':bibs[key]==e})
                # The same verified work may have different audit annotations.
                # Preserve the first bibliographic record; all segment originals
                # and both research logs are retained for the editorial audit.
            else:bibs[key]=e
    rank={r:i for i,r in enumerate(ORDER)}
    talks.sort(key=lambda x:rank[x['record']])
    items.sort(key=lambda x:(rank[x['record']],int(x['id'].split('.')[-1])))
    if [t['record'] for t in talks]!=ORDER:raise ValueError('Incomplete or duplicate record coverage')
    if any(x['id'] not in areas for x in items):
        raise ValueError('Missing area sidecar for '+str([x['id'] for x in items if x['id'] not in areas]))
    # Merge an earlier problem reused by more than one segment, preserving every
    # occurrence. A conflicting statement/status requires human editorial review.
    merged={}
    for p in problems:
        if p['id'] not in merged:merged[p['id']]=p
        else:
            q=merged[p['id']]
            for field in ['title','statement','status','status_date']:
                if q[field]!=p[field]:raise ValueError('Conflicting shared problem '+p['id']+'/'+field)
            q['occurrences']=list(dict.fromkeys(q['occurrences']+p['occurrences']))
            q['refs']=list(dict.fromkeys(q['refs']+p['refs']))
    problems=list(merged.values())
    for kind,data in [('talks',talks),('items',items),('problems',problems)]:
        write_json(out/f'GY1976_{kind}.json',data)
    with (out/'GY1976_corrections.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=CORRECTION_FIELDS);w.writeheader()
        for x in corrections:w.writerow({k:x.get(k,'') for k in CORRECTION_FIELDS})
    (out/'GY1976_references.bib').write_text('% Verified bibliography; see code/research for the depth and locator of each check.\n\n'+
        '\n\n'.join(bibs[k] for k in sorted(bibs))+'\n')
    allcounts=Counter(x['class'] for x in items)
    strict=[x for x in items if x['record']!=437]
    strictcounts=Counter(x['class'] for x in strict)
    speakers={t['record']:t['speaker'] for t in talks}
    by_speaker=Counter(x.get('speaker') or speakers[x['record']] for x in items)
    by_area=Counter(areas[x['id']] for x in items)
    per_record=[]
    for t in talks:
        own=[x for x in items if x['record']==t['record']]
        per_record.append({'record':t['record'],'speaker':t['speaker'],'date':t['date'],
            'kind':t['kind'],'items':len(own),'classes':dict(sorted(Counter(x['class'] for x in own).items()))})
    counts={'records':len(talks),'mathematical_records':sum(bool(x['items']) for x in per_record),
        'items':len(items),'strict_1976_items':len(strict),'appendix_1977_items':len(items)-len(strict),
        'classes':{c:allcounts[c] for c in 'ABCDEF'},
        'strict_1976_classes':{c:strictcounts[c] for c in 'ABCDEF'},
        'talk_kinds':dict(Counter(t['kind'] for t in talks)),
        'problems':len(problems),'references':len(bibs),'corrections':len(corrections),
        'by_speaker':dict(sorted(by_speaker.items())), 'by_area':dict(sorted(by_area.items())),
        'verification':dict(sorted(Counter(x['verification'] for x in items).items())),
        'literal_correctness':dict(sorted(Counter(x['literal_correctness'] for x in items).items())),
        'publication_match':dict(sorted(Counter(x['publication_match'] for x in items).items())),
        'development':dict(sorted(Counter(x['development'] for x in items).items())),
        'correction_types':dict(sorted(Counter(x['type'] for x in corrections).items())),
        'per_record':per_record}
    write_json(out/'code/output/counts.json',counts)
    write_json(out/'code/output/merge_audit.json',{'bibliography_duplicates':duplicate_bibs,'core_schema_extensions_removed':extras})
    write_json(out/'code/source_scope.json',{'status_date':'2026-11-10',
        'record437':{'catalogue_date':'1977-02-13','manuscript_date':'1978-02-13',
                     'academic_year':'1977-78','item_prefix':'1977-437','retained_because':'explicitly requested record'},
        'supplied_scan_count':55,'strict_1976_scan_pages':46,
        'miscatalogued_record437_scan_pages':4,'adjacent_context_scan_pages':5,
        'areas':areas,'segments':metas})
    ledger=[]
    for n in list(range(659,707))+list(range(752,759)):
        page=f'P{n:06d}'
        if n<=704:scope='1976-77 core';treatment='Mathematical items and record/heading boundaries indexed.'
        elif n in (705,706):scope='Adjacent 1977-78 context';treatment='Following Drinfeld lecture; not counted as 1976-77 occurrences.'
        elif n==752:scope='Adjacent earlier 1977-78 lecture';treatment='Sine-Gordon/quantum-soliton tail; not assigned to record437.'
        elif 753<=n<=756:scope='Record437, corrected 1977-78';treatment='All mathematical content indexed with1977-437 occurrence IDs.'
        else:scope='Adjacent 27 February1978 lecture';treatment='Continuation/comparison material; no new1976-77 occurrences assigned.'
        ledger.append({'page':page,'scope':scope,'treatment':treatment})
    with (out/'code/source_page_ledger.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['page','scope','treatment']);w.writeheader();w.writerows(ledger)
    print(json.dumps({k:v for k,v in counts.items() if k not in ['by_speaker','by_area','per_record']},indent=2))

if __name__=='__main__':main()
