"""Compile an isolated middle-section proof; cross-part occurrences stay in source data."""
import json,shutil,subprocess
from pathlib import Path
PARTS=Path(__file__).resolve().parents[1]
WORK=PARTS.parent
BUILD=WORK/'build_middle'
BUILD.mkdir(exist_ok=True)
TAG='GY1974'
for suffix in ['talks.json','items.json','problems.json','corrections.csv','references.bib']:
 shutil.copy2(PARTS/f'middle_{suffix}',BUILD/f'{TAG}_{suffix}')
shutil.copy2(PARTS/'middle_audit.tex',BUILD/f'{TAG}_development.tex')
(BUILD/f'{TAG}_overview.tex').write_text('Isolated compilation of the nine middle-section records.\n')
shutil.copy2(WORK/'kit/gelfand_companion.sty',BUILD/'gelfand_companion.sty')
# The complete chapter has340.7. This isolated compile omits that external occurrence
# only from its private copy, so the kit's same-year occurrence check remains meaningful.
path=BUILD/f'{TAG}_problems.json'
rows=json.loads(path.read_text())
own={d['id'] for d in json.loads((BUILD/f'{TAG}_items.json').read_text())}
for d in rows:d['occurrences']=[x for x in d['occurrences'] if not x.startswith('1974-') or x in own]
path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
commands=[['python',str(WORK/'kit/build_chapter.py'),TAG,str(BUILD)],
 ['xelatex','-interaction=nonstopmode','-halt-on-error',f'{TAG}_test.tex'],
 ['bibtex',f'{TAG}_test'],
 ['xelatex','-interaction=nonstopmode','-halt-on-error',f'{TAG}_test.tex'],
 ['xelatex','-interaction=nonstopmode','-halt-on-error',f'{TAG}_test.tex']]
with (BUILD/'compile.out').open('w') as log:
 for cmd in commands:
  log.write('RUN '+repr(cmd)+'\n');log.flush()
  result=subprocess.run(cmd,cwd=BUILD,stdout=log,stderr=subprocess.STDOUT)
  if result.returncode:
   print('FAILED',cmd,'; see',BUILD/'compile.out')
   raise SystemExit(result.returncode)
print('Compiled',BUILD/f'{TAG}_test.pdf')
