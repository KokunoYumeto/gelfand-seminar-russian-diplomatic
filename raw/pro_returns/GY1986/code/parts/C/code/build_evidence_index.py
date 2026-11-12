"""Make a compact query/open log and a per-item verification ledger."""
from pathlib import Path
import csv
import json
import re

root=Path(__file__).resolve().parents[1]
evidence=root/'evidence'
lines=['# Web evidence index', '',
       'Cutoff: 12 November 2026. Raw arguments and responses remain in each named JSON log.',
       'An attempted open that failed is evidence of the attempt, not of reading the source.', '']
for path in sorted(evidence.glob('web*.json')):
    obj=json.loads(path.read_text())
    args=obj['args']
    lines += ['## '+path.name,'']
    for kind in ('system1_search_query','system2_search_query'):
        for q in args.get(kind,[]):
            lines.append('- Search: '+q['q'])
    for opened in args.get('open',[]):
        lines.append('- Open: '+opened['ref_id']+
                     ('; line '+str(opened['lineno']) if 'lineno' in opened else ''))
    for clicked in args.get('click',[]):
        lines.append('- Click: '+clicked['ref_id']+'; link '+str(clicked['id']))
    for found in args.get('find',[]):
        lines.append('- Find: '+found['ref_id']+'; '+found['pattern'])
    for shot in args.get('screenshot',[]):
        lines.append('- PDF page image: '+shot['ref_id']+'; page '+str(shot['pageno']))
    texts='\n'.join(x.get('text','') for x in obj['result'].get('content',[]) if x.get('type')=='text')
    urls=sorted(set(re.findall(r'https?://[^\s<>"\)]+',texts)))
    if urls:
        lines.append('- URLs returned by the retrieval:')
        lines += ['  - '+u for u in urls if len(u)<500]
    if any(s in texts for s in ('Failed to fetch','Internal Error','not accessible')):
        lines.append('- Retrieval contains an error; consult raw result before claiming source access.')
    lines.append('')
(evidence/'search_index.md').write_text('\n'.join(lines)+'\n')
items=json.loads((root/'items.json').read_text())
with (evidence/'verification_ledger.csv').open('w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['id','title','class','publication_match','verification','refs','confidence'])
    for x in items:
        writer.writerow([x['id'],x['title'],x['class'],x['publication_match'],
                         x['verification'],';'.join(x['refs']),x['confidence']])
print('Indexed',len(list(evidence.glob('web*.json'))),'web logs and',len(items),'items')
