from pathlib import Path
import subprocess,os,json
root=Path.cwd()
d=root/'work/late_correction_preflight';cache=root/'work/texmf'
env=os.environ.copy()
env.update(TEXMF='{'+str(cache)+',/etc/texmf,/usr/share/texlive/texmf-dist,/usr/share/texmf}',
 TEXMFVAR=str(cache/'var'),TEXMFCONFIG=str(cache/'config'),VARTEXFONTS=str(cache/'fonts'),TEXFORMATS=str(cache)+'//:')
r=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','late_correction_test.tex'],cwd=d,env=env,capture_output=True,text=True)
(d/'late_correction_stdout.txt').write_text(r.stdout+r.stderr)
print(json.dumps({'returncode':r.returncode,'last_output':(r.stdout+r.stderr)[-1800:]},indent=2))
raise SystemExit(r.returncode)
