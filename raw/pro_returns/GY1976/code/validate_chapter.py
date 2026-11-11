"""Additional content/schema/reference checks beyond the supplied builder.

Run from the unpacked archive: python code/validate_chapter.py .
This checks referential integrity and scope accounting, not the truth of
historical identifications or proofs; those are documented in research logs.
"""
from pathlib import Path
from collections import Counter
import argparse
import csv
import hashlib
import json
import re

EXPECTED = [397,398,399,400,401,402,403,404,405,406,407,408,409,410,
            411,412,413,414,416,415,417,418,437]
ENUMS={
 'kind':{'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
 'class':set('ABCDEF'),
 'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
 'publication_match':{'exact','partial','thematic only','none found'},
 'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
 'development':{'none','annotated','developed in this chapter'},
 'confidence':{'high','medium','low'}
}

def entries(s):
    out={}
    for m in re.finditer(r'@\w+\s*\{\s*([^,\s]+)\s*,',s):
        key=m.group(1);i=s.index('{',m.start())+1;depth=1
        while i<len(s) and depth:
            if s[i]=='{' and s[i-1]!='\\':depth+=1
            elif s[i]=='}' and s[i-1]!='\\':depth-=1
            i+=1
        if depth:raise ValueError('Unbalanced BibTeX entry: '+key)
        if key in out:raise ValueError('Duplicate BibTeX key: '+key)
        out[key]=s[m.start():i]
    return out

def cites(s):
    return {k.strip() for g in re.findall(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]+)\}',s)
            for k in g.split(',')}

def main():
    p=argparse.ArgumentParser();p.add_argument('directory',nargs='?',default='.')
    a=p.parse_args();d=Path(a.directory).resolve();errors=[];warnings=[]
    tag='GY1976'
    talks=json.loads((d/f'{tag}_talks.json').read_text())
    items=json.loads((d/f'{tag}_items.json').read_text())
    probs=json.loads((d/f'{tag}_problems.json').read_text())
    bib=entries((d/f'{tag}_references.bib').read_text())
    if [t['record'] for t in talks]!=EXPECTED:errors.append('Record coverage/source order differs from the reviewed 23-record manifest.')
    by_record={t['record']:t for t in talks};by_item={x['id']:x for x in items};by_prob={x['id']:x for x in probs}
    if len(by_item)!=len(items):errors.append('Duplicate occurrence IDs.')
    if len(by_prob)!=len(probs):errors.append('Duplicate problem IDs.')
    for t in talks:
        allowed_talk={'record','date','speaker','pages','title','kind','summary'}
        if set(t)!=allowed_talk:errors.append(f"record {t['record']}: core talk field set differs: {sorted(set(t)^allowed_talk)}")
        if t.get('kind') not in {'talk','plan','heading','other'}:errors.append(f"record {t['record']}: invalid kind")
        for f in ['record','date','speaker','pages','title','summary']:
            if f not in t:errors.append(f"record {t['record']}: missing {f}")
    for x in items:
        ident=x.get('id','?')
        required_item={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
        if not required_item<=set(x) or set(x)-required_item-{'speaker'}:
            errors.append(f'{ident}: incorrect core item field set')
        for f,allowed in ENUMS.items():
            if x.get(f) not in allowed:errors.append(f'{ident}: invalid {f}: {x.get(f)}')
        for f in ['notes','statement','fate','present_status','reconstruction','problem','worth','refs','pages']:
            if f not in x:errors.append(f'{ident}: missing {f}')
        if not x.get('statement'):errors.append(f'{ident}: empty modern statement')
        if x.get('class') in {'C','D'} and not x.get('worth'):errors.append(f'{ident}: C/D lacks worth')
        if x.get('record') not in by_record:errors.append(f'{ident}: unknown record')
        if not re.fullmatch(r'197[67]-\d+\.\d+',ident):errors.append(f'{ident}: academic-year ID format')
        expected_year=1977 if x.get('record')==437 else 1976
        if not ident.startswith(str(expected_year)+'-'):errors.append(f'{ident}: incorrect academic-year prefix')
        if '2026' not in x.get('present_status',''):errors.append(f'{ident}: status lacks date')
        cited=cites(' '.join(v for v in x.values() if isinstance(v,str)))
        missing=cited-set(x.get('refs',[]))
        if missing:errors.append(f'{ident}: citations absent from refs: {sorted(missing)}')
        for key in x.get('refs',[]):
            if key not in bib:errors.append(f'{ident}: missing bibliography key {key}')
        pr=x.get('problem')
        if pr and pr not in by_prob:errors.append(f'{ident}: missing problem {pr}')
        if pr in by_prob and ident not in by_prob[pr]['occurrences']:errors.append(f'{ident}: absent from linked problem occurrences')
        for k,v in x.items():
            if isinstance(v,str) and any(ord(ch)<32 and ch not in '\n\t\r' for ch in v):
                errors.append(f'{ident}/{k}: unexpected control character')
    for record in by_record:
        got=[x['id'] for x in items if x['record']==record]
        prefix=1977 if record==437 else 1976
        expected=[f'{prefix}-{record}.{i+1}' for i in range(len(got))]
        if got!=expected:errors.append(f'record {record}: nonconsecutive item IDs')
    prev=d/'code/inputs/previous_index.md'
    previous=prev.read_text() if prev.exists() else ''
    for p in probs:
        if set(p)!={'id','title','statement','occurrences','status','status_date','refs'}:
            errors.append(p['id']+': incorrect core problem field set')
        if p['status_date']!='2026-11':errors.append(p['id']+': wrong status month')
        for key in cites(p['statement']+' '+p['status'])-set(p['refs']):
            errors.append(p['id']+': cited key missing from refs '+key)
        for key in p['refs']:
            if key not in bib:errors.append(p['id']+': missing bibliography '+key)
        for occurrence in p['occurrences']:
            if occurrence.startswith(('1976-','1977-')) and occurrence not in by_item:
                errors.append(p['id']+': missing occurrence '+occurrence)
            elif not occurrence.startswith(('1976-','1977-')) and previous and occurrence not in previous:
                errors.append(p['id']+': older occurrence absent from supplied index: '+occurrence)
    for key,e in bib.items():
        if not re.search(r'\b(?:url|doi)\s*=',e,re.I):errors.append(key+': lacks URL/DOI')
        if not re.search(r'\bnote\s*=\s*\{(?:verified|unverified)\}',e,re.I):errors.append(key+': invalid/missing verified note')
    correction_rows=list(csv.DictReader((d/f'{tag}_corrections.csv').open()))
    for i,r in enumerate(correction_rows,1):
        if r['applies_to'] not in {'ru','en','both'}:errors.append(f'correction {i}: applies_to')
        if r.get('type','') not in {'transcription','translation','ambiguity','faithful_error','provenance',''}:
            errors.append(f'correction {i}: type')
    all_text='\n'.join((d/f'{tag}_{s}').read_text() for s in ['talks.json','items.json','problems.json','overview.tex','development.tex','corrections.csv'])
    all_text=all_text.replace('\\\\','\\')
    for k in cites(all_text)-set(bib):errors.append('Global unresolved citation '+k)
    counts={'records':len(talks),'items':len(items),'classes':dict(sorted(Counter(x['class'] for x in items).items())),
            'problems':len(probs),'references':len(bib),'corrections':len(correction_rows),
            'verification':dict(sorted(Counter(x['verification'] for x in items).items())),
            'literal_correctness':dict(sorted(Counter(x['literal_correctness'] for x in items).items()))}
    result={'counts':counts,'errors':errors,'warnings':warnings,'status':'PASS' if not errors else 'FAIL'}
    out=d/'code/output/validation.json';out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    raise SystemExit(bool(errors))

if __name__=='__main__':main()
