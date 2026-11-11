"""Assemble audited record batches without sorting away manuscript order."""
import collections
import csv
import json
from pathlib import Path
import shutil
import sys
from bibtools import entries, serialize, value, doi, canonical_text

ROOT=Path(__file__).resolve().parent
OUT=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'final'/'GY1981'
OUT.mkdir(parents=True,exist_ok=True)
parts=[ROOT/'parts'/p for p in 'abcd']
all_data={}
for kind in ['talks','items','problems']:
    all_data[kind]=[x for p in parts for x in json.loads((p/(kind+'.json')).read_text())]
    (OUT/f'GY1981_{kind}.json').write_text(json.dumps(all_data[kind],ensure_ascii=False,indent=2)+'\n')
corrections=[]
for p in parts:
    q=p/'corrections.csv'
    if q.exists():corrections.extend(csv.DictReader(q.open()))
    else:print('PENDING',q)
with (OUT/'GY1981_corrections.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type'])
    w.writeheader();w.writerows(corrections)
bib={}
diagnostics=[]
for p in parts:
    for e in entries((p/'references.bib').read_text()):
        if e['duplicates']:
            diagnostics.append(f"Resolved repeated fields in {e['key']}: {e['duplicates']}; current annotation retained.")
        if e['key'] in bib:
            prev=bib[e['key']]
            for k,v in e['fields'].items():
                if k=='annote' and v!=prev['fields'].get(k):
                    v='{'+value(prev,k)+' Additional current-run verification: '+value(e,k)+'}'
                    prev['fields'][k]=v
                elif k not in prev['fields'] or k=='note' and value(e,k)=='verified':
                    prev['fields'][k]=v
            diagnostics.append('Merged shared key '+e['key'])
        else:bib[e['key']]=e
seen={}
for e in bib.values():
    for typ,k in [('doi',doi(e)),('title',canonical_text(value(e,'title')))]:
        if not k:continue
        if (typ,k) in seen and seen[(typ,k)]!=e['key']:
            diagnostics.append(f"REVIEW same {typ}: {seen[(typ,k)]} / {e['key']}")
        seen[(typ,k)]=e['key']
(OUT/'GY1981_references.bib').write_text('\n'.join(serialize(bib[k]) for k in sorted(bib)))
developments=[]
for p in parts:
    q=p/'development.tex'
    if q.exists():developments.append(q.read_text().strip())
(OUT/'GY1981_development.tex').write_text('\n\n'.join(developments)+'\n')
for name in ['build_chapter.py','gelfand_companion.sty','CHAPTER_FORMAT.md']:
    shutil.copy2(ROOT/'kit'/name,OUT/name)
style=OUT/'gelfand_companion.sty'
style.write_text(style.read_text().replace(
    r'\newcommand{\ours}{\textup{[proved here]}}',
    r'\newcommand{\ours}{\textup{[proved here]}\space}').replace(
    r'\newcommand{\oursComputed}{\textup{[computed here]}}',
    r'\newcommand{\oursComputed}{\textup{[computed here]}\space}'))
builder=OUT/'build_chapter.py'
builder.write_text(builder.read_text().replace(
    '\ncls = collections.Counter',
    '\n# Print also references recorded in data refs lists but cited only in prose.\n'
    'driver_path = D / f"{TAG}_test.tex"\n'
    'driver_path.write_text(driver_path.read_text().replace(r"\\bibliographystyle", '
    'r"\\nocite{*}" + "\\n" + r"\\bibliographystyle"))\n'
    '\ncls = collections.Counter'))
counts={
 'records':len(all_data['talks']),
 'items':len(all_data['items']),
 'problems':len(all_data['problems']),
 'references':len(bib),
 'corrections':len(corrections),
 'classes':dict(sorted(collections.Counter(x['class'] for x in all_data['items']).items())),
 'record_order':[t['record'] for t in all_data['talks']],
 'record_kinds':dict(collections.Counter(t['kind'] for t in all_data['talks'])),
 'correctness':dict(collections.Counter(x['literal_correctness'] for x in all_data['items'])),
 'verification':dict(collections.Counter(x['verification'] for x in all_data['items'])),
 'development':dict(collections.Counter(x['development'] for x in all_data['items'])),
 'reference_notes':dict(collections.Counter(value(e,'note') for e in bib.values())),
 'correction_types':dict(collections.Counter(r['type'] for r in corrections)),
}
(ROOT/'assembly_counts.json').write_text(json.dumps(counts,indent=2)+'\n')
(ROOT/'assembly_output.txt').write_text(json.dumps(counts,indent=2)+'\n'+'\n'.join(diagnostics)+'\n')
print(json.dumps(counts,indent=2));print('\n'.join(diagnostics))
