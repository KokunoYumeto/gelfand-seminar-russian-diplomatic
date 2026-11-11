"""Run the prescribed chapter builder, XeLaTeX and BibTeX, saving all logs."""
from pathlib import Path
import json,subprocess,sys
D=Path(sys.argv[1]).resolve();OUT=D/'code/output';OUT.mkdir(parents=True,exist_ok=True)
ROOT=Path(__file__).resolve().parents[2]
launcher=ROOT/'work/tex_runtime/run_tex.py'
commands=[('typesetting',[sys.executable,str(Path(__file__).parent/'repair_typesetting.py'),str(D)]),
          ('builder',[sys.executable,'build_chapter.py','GY1977']),
          ('xelatex_1',['xelatex','-interaction=nonstopmode','-halt-on-error','GY1977_test.tex']),
          ('bibtex',['bibtex','GY1977_test']),
          ('xelatex_2',['xelatex','-interaction=nonstopmode','-halt-on-error','GY1977_test.tex']),
          ('xelatex_3',['xelatex','-interaction=nonstopmode','-halt-on-error','GY1977_test.tex'])]
rows=[]
for name,cmd in commands:
    if name not in ['builder','typesetting'] and launcher.exists():cmd=[sys.executable,str(launcher)]+cmd
    proc=subprocess.run(cmd,cwd=D,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (OUT/(name+'.txt')).write_text(proc.stdout)
    rows.append({'stage':name,'command':cmd,'returncode':proc.returncode})
    print(name,proc.returncode,flush=True)
    if proc.returncode:
        print('\n'.join(proc.stdout.splitlines()[-55:]),flush=True)
        (OUT/'compile_commands.json').write_text(json.dumps(rows,indent=2)+'\n')
        sys.exit(proc.returncode)
(OUT/'compile_commands.json').write_text(json.dumps(rows,indent=2)+'\n')
print('All prescribed compilation commands succeeded.',flush=True)
