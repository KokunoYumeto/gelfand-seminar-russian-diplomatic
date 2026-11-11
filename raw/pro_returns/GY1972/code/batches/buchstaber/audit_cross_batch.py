"""Read-only cross-batch bibliography and catalogue reconciliation."""
import re,json,difflib,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).parent
def bib_entries(path):
    text=path.read_text();out=[]
    for m in re.finditer(r'@(\w+)\s*\{\s*([^,\s]+)\s*,',text):
        i=m.end();start=i;depth=1
        while i<len(text) and depth:
            if text[i]=='{' and (i==0 or text[i-1]!='\\'):depth+=1
            if text[i]=='}' and (i==0 or text[i-1]!='\\'):depth-=1
            i+=1
        body=text[start:i-1];fields={}
        # The source files use brace-delimited fields. Handle quoted values too.
        for f in re.finditer(r'\b(\w+)\s*=\s*([{"])',body):
            j=f.end();beg=j
            if f[2]=='{':
                d=1
                while j<len(body) and d:
                    if body[j]=='{' and body[j-1]!='\\':d+=1
                    if body[j]=='}' and body[j-1]!='\\':d-=1
                    j+=1
                val=body[beg:j-1]
            else:
                while j<len(body) and not(body[j]=='"' and body[j-1]!='\\'):j+=1
                val=body[beg:j]
            fields[f[1].lower()]=val.strip()
        out.append(dict(key=m[2],kind=m[1],path=str(path),fields=fields))
    return out
def normtitle(s):
    s=re.sub(r'\\(?:mathbb|mathrm|operatorname|text|emph)\b','',s)
    s=re.sub(r'\\[A-Za-z]+','',s)
    return re.sub('[^a-z0-9]','',s.lower())
def doi(e):return e['fields'].get('doi','').lower().replace('https://doi.org/','').strip()
cum=bib_entries(ROOT/'references_cumulative.bib')
new=[]
for path in sorted((ROOT/'batches').glob('*/references.bib')):new+=bib_entries(path)
groups=collections.defaultdict(list)
for e in new:groups[e['key']].append(e)
lines=['# Cross-batch reconciliation','', 'Read-only audit, 2026-11-09.','', '## Key and work matching','']
lines.append(f'Cumulative bibliography: {len(cum)} entries, {len(set(e["key"] for e in cum))} unique keys. Current batches: {len(new)} entries, {len(groups)} unique keys.')
lines.append('')
for key,es in groups.items():
    old=[e for e in cum if e['key']==key]
    if len(es)>1:lines.append(f'- Shared current key `{key}`: '+', '.join(Path(e['path']).parent.name for e in es)+'. Retain one merged entry and combine verification annotations.')
    if old:lines.append(f'- Reused cumulative key `{key}`: '+', '.join(Path(e['path']).parent.name for e in es)+'.')
lines+=['','### Candidate duplicate works under different keys','']
candidates=[]
for e in new:
    for f in cum+new:
        if e['key']==f['key']:continue
        ed,fd=doi(e),doi(f)
        et,ft=normtitle(e['fields'].get('title','')),normtitle(f['fields'].get('title',''))
        yearsame=e['fields'].get('year')==f['fields'].get('year')
        exact=et and et==ft
        score=difflib.SequenceMatcher(None,et,ft).ratio()
        if (ed and ed==fd) or (exact and yearsame) or (score>.91 and yearsame):
            pair=tuple(sorted([e['key'],f['key']]))
            if pair not in [x[0] for x in candidates]:candidates.append((pair,ed==fd if ed and fd else False,score,e['fields'].get('title',''),f['fields'].get('title','')))
if not candidates:lines.append('No same-DOI or same-year near-identical-title duplicate under a different key was found.')
for pair,match,score,t1,t2 in candidates:lines.append(f'- `{pair[0]}` / `{pair[1]}`: DOI match={match}, normalized-title similarity={score:.3f}. Titles: {t1} / {t2}.')
lines+=['','## Current talk records and actual item pages','']
alltalks=[];allitems=[]
for path in sorted((ROOT/'batches').glob('*/talks.json')):
    for t in json.loads(path.read_text()):alltalks.append((path.parent.name,t))
for path in sorted((ROOT/'batches').glob('*/items.json')):allitems+=json.loads(path.read_text())
records=[t['record'] for _,t in alltalks]
lines.append(f'{len(records)} talk records; duplicates={sorted(r for r,c in collections.Counter(records).items() if c>1)}.')
lines+=['','| Record | Batch | Talk pages currently | Range of item pages |','|---|---|---|---|']
for batch,t in sorted(alltalks,key=lambda x:x[1]['record']):
    pages=[]
    for i in allitems:
        if i['record']==t['record']:
            nums=[int(x) for x in re.findall(r'P(\d+)',i['pages'])]
            if nums:pages.extend(range(min(nums),max(nums)+1))
    lines.append(f'| {t["record"]} | {batch} | {t["pages"]} | '+(f'P{min(pages):06d}–P{max(pages):06d}' if pages else 'heading')+' |')
report=OUT/'cross_batch_audit.md'
if report.exists() and '\n## Manual bibliography reconciliation\n' in report.read_text():
    manual=report.read_text().split('\n## Manual bibliography reconciliation\n',1)[1]
    lines.append('\n## Manual bibliography reconciliation\n'+manual)
report.write_text('\n'.join(lines)+'\n')
print('Current bibliography:',len(new),'entries;',len(groups),'unique keys; candidate duplicate key pairs:',len(candidates))
for x in candidates:print(x)
print('Current catalogue records:',len(records),'unique',len(set(records)))
print('Wrote',OUT/'cross_batch_audit.md')
