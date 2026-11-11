"""Run the supplied chapter builder and TeX chain on this isolated fragment."""
from pathlib import Path
import json,re,shutil,subprocess

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
KIT=BASE/'source_kit'/'kit'
OUT=HERE/'validation'
OUT.mkdir(exist_ok=True)
TAG='GY1967'
for name in ('talks.json','items.json','problems.json','corrections.csv','references.bib'):
    shutil.copyfile(HERE/name,OUT/(TAG+'_'+name))
shutil.copyfile(KIT/'gelfand_companion.sty',OUT/'gelfand_companion.sty')
(OUT/(TAG+'_overview.tex')).write_text('Isolated validation of records 131--140.\n')
(OUT/(TAG+'_development.tex')).write_text('')

items=json.loads((HERE/'items.json').read_text())
keys=set(re.findall(r'@\w+\s*\{\s*([^,\s]+)',(HERE/'references.bib').read_text()))
for x in items:
    cites=set()
    for v in x.values():
        if isinstance(v,str):
            for group in re.findall(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]+)\}',v):
                cites.update(group.split(','))
    assert cites<=set(x['refs']),(x['id'],cites-set(x['refs']))
    assert set(x['refs'])<=keys,(x['id'],set(x['refs'])-keys)
log=[]
commands=[['python',str(KIT/'build_chapter.py'),TAG,str(OUT)],
          ['xelatex','-interaction=nonstopmode','-halt-on-error',TAG+'_test.tex'],
          ['bibtex',TAG+'_test'],
          ['xelatex','-interaction=nonstopmode','-halt-on-error',TAG+'_test.tex'],
          ['xelatex','-interaction=nonstopmode','-halt-on-error',TAG+'_test.tex']]
for cmd in commands:
    p=subprocess.run(cmd,cwd=OUT,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    log.append('$ '+' '.join(cmd)+'\n'+p.stdout)
    (HERE/'validation_log.txt').write_text('\n'.join(log))
    print('exit',p.returncode,':',' '.join(cmd))
    if p.returncode:
        print(p.stdout[-6000:])
        raise SystemExit(p.returncode)
print('All supplied schema and LaTeX checks passed.')
