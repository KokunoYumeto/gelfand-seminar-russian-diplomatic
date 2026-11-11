"""Rerun the delivered exact computational checks and structural validation.

Run from any directory: python /path/to/chapter/code/run_checks.py
Requires Python 3.10+ and SymPy; TeX is needed only by rebuild.sh.
"""
import json,subprocess,sys
from pathlib import Path
D=Path(__file__).resolve().parent.parent
A=D/'code/authoring'
out=D/'audit/checks';out.mkdir(parents=True,exist_ok=True)
jobs=[
 ('mathematical_checks',[sys.executable,str(D/'code/check_mathematics.py'),'--output',str(D/'code/check_mathematics_output.json')],D),
 ('early_checks',[sys.executable,'work/early/verify_early.py'],A),
 ('independent_soliton_check',[sys.executable,'work/early/verify_late_review.py'],A),
 ('oscillator_and_schubert_checks',[sys.executable,'work/virasoro/check_formulas.py'],A),
 ('chapter_validation',[sys.executable,str(D/'code/validate_chapter.py'),str(D)],D),
 ('previous_index_links',[sys.executable,str(D/'code/check_previous_links.py'),str(D)],D),
]
results=[]
for name,args,cwd in jobs:
    path=out/(name+'.txt')
    with path.open('w') as f:r=subprocess.run(args,cwd=cwd,stdout=f,stderr=subprocess.STDOUT)
    results.append({'check':name,'exit_code':r.returncode,'output':str(path.relative_to(D))})
    print(name+(': PASS' if r.returncode==0 else ': FAIL'),flush=True)
    if r.returncode:print(path.read_text()[-6000:]);break
report={'status':'PASS' if len(results)==len(jobs) and all(x['exit_code']==0 for x in results) else 'FAIL','checks':results,'scope':'Exact computational checks of the stated examples and algebraic identities, plus schema integrity; no numerical experiment is treated as proof of universality or a literature search.'}
(out/'checks_output.json').write_text(json.dumps(report,indent=2)+'\n')
sys.exit(report['status']!='PASS')
