"""Validate only this agent's part and prepare an isolated kit-format build.

Does not edit shared chapter files. Run from the workspace root.
"""
from pathlib import Path
import collections, csv, json, re, shutil, subprocess

P=Path(__file__).resolve().parent
ROOT=P.parent.parent
talks=json.loads((P/'talks.json').read_text())
items=json.loads((P/'items.json').read_text())
problems=json.loads((P/'problems.json').read_text())
bib=(P/'references.bib').read_text()
keys=re.findall(r'@\w+\s*\{\s*([^,\s]+)',bib)
assert len(keys)==len(set(keys)), 'Duplicate local bibliography key'
assert [t['record'] for t in talks]==list(range(481,489))
assert not [x for x in items if x['record']==481]
assert not [x for x in items if re.search(r'P00091[78]',x['pages'])]
for r in range(482,489):
    current=[x for x in items if x['record']==r]
    assert [x['id'] for x in current]==[f'1979-{r}.{n+1}' for n in range(len(current))]
for x in items:
    assert all(k in keys for k in x['refs']), x['id']
    if x['class'] in ('C','D'):assert x['worth'],x['id']
    cites=set()
    for s in x.values():
        if isinstance(s,str):
            for group in re.findall(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}',s):
                cites.update(y.strip() for y in group.split(','))
    assert cites<=set(x['refs']),(x['id'],cites-set(x['refs']))
for block in re.split(r'(?=^@)',bib,flags=re.M):
    if block.startswith('@'):
        assert re.search(r'\b(?:url|doi)\s*=',block),block[:70]
        assert re.search(r'note\s*=\s*\{verified\}',block),block[:70]
q=P/'qa';q.mkdir(exist_ok=True)
for stem in ('talks.json','items.json','problems.json','corrections.csv','references.bib'):
    shutil.copyfile(P/stem,q/('GY1979_'+stem))
for stem in ('overview.tex','development.tex'):
    (q/('GY1979_'+stem)).write_text('% Isolated late-record verification only.\n')
shutil.copyfile(ROOT/'kit'/'gelfand_companion.sty',q/'gelfand_companion.sty')
run=subprocess.run(['python',str(ROOT/'kit'/'build_chapter.py'),'GY1979',str(q)],capture_output=True,text=True)
(q/'build_log.txt').write_text(run.stdout+run.stderr)
assert run.returncode==0,run.stdout+run.stderr
report={
    'status_date':'2026-11-10','records':len(talks),'items':len(items),
    'per_record':dict(collections.Counter(x['record'] for x in items)),
    'by_class':dict(collections.Counter(x['class'] for x in items)),
    'problem_ids':[p['id'] for p in problems],
    'corrections':len(list(csv.DictReader((P/'corrections.csv').open()))),
    'bibliography_entries':len(keys),'checks':'PASS',
    'boundary_pages_are_occurrences':False,
    'kit_build_exit_code':run.returncode,
}
(P/'validation_output.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
