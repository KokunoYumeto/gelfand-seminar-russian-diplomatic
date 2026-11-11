"""Run the required builder / XeLaTeX / BibTeX / XeLaTeX / XeLaTeX sequence.

Normal TeX installations need no configuration changes. The bounded fallback
handles this execution environment's missing ls-R databases and XeLaTeX format
entirely inside the chapter directory; it does not modify the system installation.
"""
import json,os,subprocess,sys
from pathlib import Path
D=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parent.parent
logs=D/'audit/buildlogs';logs.mkdir(parents=True,exist_ok=True)
env=os.environ.copy();commands=[]
def run(args,name,cwd=D):
    path=logs/(name+'.txt')
    with path.open('w') as f:r=subprocess.run(args,cwd=cwd,env=env,stdout=f,stderr=subprocess.STDOUT)
    commands.append({'argv':list(map(str,args)),'cwd':str(cwd),'log':str(path.relative_to(D)),'exit_code':r.returncode})
    if r.returncode:
        print(path.read_text()[-8000:]);raise SystemExit(r.returncode)
    print(name+': PASS',flush=True)

probe=subprocess.run(['kpsewhich','-engine=xetex','-progname=xelatex','xelatex.fmt'],env=env,text=True,capture_output=True)
fallback=not probe.stdout.strip()
if fallback:
    trees=[p for p in ('/usr/share/texmf','/usr/share/texlive/texmf-dist') if Path(p).is_dir()]
    if not trees:raise SystemExit('No usable TeX distribution: install XeLaTeX and BibTeX.')
    env['TEXMF']='{'+','.join(trees)+'}'
    local=D/'code/texruntime';local.mkdir(parents=True,exist_ok=True)
    if not (local/'xelatex.fmt').exists():run(['xetex','-ini','-etex','-jobname=xelatex','-progname=xelatex','xelatex.ini'],'format_build',local)
    env['TEXFORMATS']=str(local)+':'
run([sys.executable,'build_chapter.py','GY1985'],'builder')
run(['xelatex','-interaction=nonstopmode','-halt-on-error','GY1985_test.tex'],'xelatex_1')
run(['bibtex','GY1985_test'],'bibtex')
run(['xelatex','-interaction=nonstopmode','-halt-on-error','GY1985_test.tex'],'xelatex_2')
run(['xelatex','-interaction=nonstopmode','-halt-on-error','GY1985_test.tex'],'xelatex_3')
log=(D/'GY1985_test.log').read_text()
# A truly clean extraction can need another label-settling pass after the
# required sequence. Honour actual rerun warnings, with a finite limit.
for extra in range(4,6):
    warning_lines=[line for line in log.splitlines() if not line.startswith('Package: rerunfilecheck')]
    if not any('Rerun' in line or 'may have changed' in line for line in warning_lines):break
    run(['xelatex','-interaction=nonstopmode','-halt-on-error','GY1985_test.tex'],f'xelatex_{extra}')
    log=(D/'GY1985_test.log').read_text()
bad=[line for line in log.splitlines() if not line.startswith('Package: rerunfilecheck') and (line.startswith('!') or 'Overfull' in line or 'Missing character' in line or 'undefined' in line.lower() or 'Rerun' in line or 'may have changed' in line)]
result={'status':'PASS' if not bad else 'REVIEW','local_tex_format_fallback':fallback,'environment_overrides':{k:env[k] for k in ('TEXMF','TEXFORMATS') if env.get(k)!=os.environ.get(k)},'commands':commands,'remaining_layout_or_reference_messages':bad}
(D/'audit/build_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
sys.exit(bool(bad))
