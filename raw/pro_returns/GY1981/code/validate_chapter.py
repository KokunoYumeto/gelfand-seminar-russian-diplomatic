"""Additional schema, citation, occurrence, bibliography and LaTeX audit."""
import collections
import csv
import json
from pathlib import Path
import re
import sys
from bibtools import entries, value

root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent/'final'/'GY1981'
tag='GY1981'
data={k:json.loads((root/f'{tag}_{k}.json').read_text()) for k in ['talks','items','problems']}
errors=[]; warnings=[]
def need(ok,msg):
    if not ok:errors.append(msg)
def cites(s):
    return {k.strip() for m in re.finditer(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]+)\}',s) for k in m.group(1).split(',')}
recs={x['record']:x for x in data['talks']}
ids={x['id']:x for x in data['items']}
probs={x['id']:x for x in data['problems']}
bib=entries((root/f'{tag}_references.bib').read_text())
keys={e['key'] for e in bib}
need(set(recs)==set(range(530,560)),'Record coverage differs from 530--559.')
need(len(recs)==len(data['talks']),'Duplicate record.')
need(len(ids)==len(data['items']),'Duplicate item ID.')
need(len(probs)==len(data['problems']),'Duplicate problem ID.')
need(len(keys)==len(bib),'Duplicate bibliography key.')
enums={
 'kind':{'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
 'class':set('ABCDEF'),
 'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
 'publication_match':{'exact','partial','thematic only','none found'},
 'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
 'development':{'none','annotated','developed in this chapter'},
 'confidence':{'high','medium','low'},
}
for x in data['items']:
    i=x['id']; need(x['record'] in recs,f'{i}: missing record')
    for k,allowed in enums.items():need(x.get(k) in allowed,f'{i}: invalid {k}={x.get(k)!r}')
    for k in ['reconstruction','problem','worth','refs','area']:need(k in x,f'{i}: missing {k}')
    if x['class'] in 'CD':need(bool(x.get('worth')),f'{i}: no worth sentence')
    need('2026' in x['present_status'],f'{i}: undated status')
    need(set(x['refs'])<=keys,f'{i}: unknown refs {set(x["refs"])-keys}')
    cs=cites(' '.join(v for v in x.values() if isinstance(v,str)))
    need(cs<=set(x['refs']),f'{i}: cited keys omitted from refs {cs-set(x["refs"])}')
    if x.get('problem'):
        need(x['problem'] in probs,f'{i}: missing problem')
        if x['problem'] in probs:need(i in probs[x['problem']]['occurrences'],f'{i}: absent from problem occurrences')
for t in data['talks']:
    need(t['kind'] in {'talk','plan','heading','other'},f'{t["record"]}: invalid talk kind')
    seq=[x['id'] for x in data['items'] if x['record']==t['record']]
    need(seq==[f'1981-{t["record"]}.{n}' for n in range(1,len(seq)+1)],f'{t["record"]}: nonconsecutive items')
for p in data['problems']:
    need(p['status_date']=='2026-11',f'{p["id"]}: status date')
    need(set(p['refs'])<=keys,f'{p["id"]}: unknown refs')
    need(cites(p['statement']+' '+p['status'])<=set(p['refs']),f'{p["id"]}: missing cited refs')
    for i in p['occurrences']:
        if i.startswith('1981-'):need(i in ids,f'{p["id"]}: missing occurrence {i}')
for e in bib:
    need(not e['duplicates'],f'{e["key"]}: duplicate fields')
    need(bool(value(e,'url') or value(e,'doi')),f'{e["key"]}: no URL/DOI')
    need(value(e,'note') in {'verified','unverified'},f'{e["key"]}: verification marker')
    need(bool(value(e,'annote')),f'{e["key"]}: no verification scope annotation')
all_tex=[]
for kind in data:
    for x in data[kind]:
        fields=['summary'] if kind=='talks' else ['statement','status'] if kind=='problems' else ['notes','statement','reconstruction','fate','present_status','worth']
        for k in fields:
            s=x.get(k,''); label=f'{x.get("id",x.get("record"))}/{k}'
            all_tex.append((label,s))
for f in ['overview.tex','development.tex']:
    all_tex.append((f,(root/f'{tag}_{f}').read_text()))
rows=list(csv.DictReader((root/f'{tag}_corrections.csv').open()))
for n,r in enumerate(rows,1):
    need(r['applies_to'] in {'ru','en','both'},f'correction {n}: applies_to')
    need(r['type'] in {'transcription','translation','ambiguity','faithful_error','provenance',''},f'correction {n}: type')
    for k in ['place','transcription_reads','should_read','evidence']:all_tex.append((f'correction {n}/{k}',r[k]))
for label,s in all_tex:
    need(cites(s)<=keys,f'{label}: unknown citation {cites(s)-keys}')
    need(not any(ord(c)<32 and c not in '\n\t\r' for c in s),f'{label}: control character')
    # A targeted linter: remove math and common escaped text; find accidental
    # plain-language subscripts such as delta_(i-1), which break XeLaTeX.
    plain=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]|(?<!\\)\$.*?(?<!\\)\$','',s,flags=re.S)
    if re.search(r'(?<!\\)[_^]',plain):
        warnings.append(f'{label}: inspect plain-text underscore/caret: '+plain[:180])
result={
 'records':len(recs),'items':len(ids),'problems':len(probs),'references':len(bib),'corrections':len(rows),
 'errors':errors,'latex_review_warnings':warnings,
 'class_counts':dict(sorted(collections.Counter(x['class'] for x in data['items']).items()))}
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(bool(errors))
