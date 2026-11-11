"""Run the prescribed XeLaTeX/BibTeX build and retain readable logs.

The normal route uses the installed TeX configuration. In the supplied
container the distribution files exist but the generated filename database
and xelatex format do not. The fallback only creates a local format/cache;
it never edits the system installation or changes the chapter's mathematics.
"""
from pathlib import Path
import argparse
import json
import os
import shutil
import subprocess
import sys


def run(command,cwd,env,log):
    r=subprocess.run(command,cwd=cwd,env=env,capture_output=True,text=True)
    log.parent.mkdir(parents=True,exist_ok=True)
    log.write_text('$ '+' '.join(command)+'\n'+r.stdout+r.stderr)
    print(json.dumps({'command':command,'returncode':r.returncode,'log':str(log)}),flush=True)
    if r.returncode:
        print((r.stdout+r.stderr)[-8000:])
        raise SystemExit(r.returncode)
    return r


def main():
    p=argparse.ArgumentParser()
    p.add_argument('directory',nargs='?',default='.')
    p.add_argument('--tag',default='GY1976')
    p.add_argument('--cache',default=None)
    p.add_argument('--skip-generate',action='store_true')
    a=p.parse_args()
    d=Path(a.directory).resolve()
    logs=d/'code/output/build'
    cache=Path(a.cache).resolve() if a.cache else d/'code/runtime_texmf'
    env=os.environ.copy()
    check=subprocess.run(['kpsewhich','xelatex.fmt'],capture_output=True,text=True,env=env)
    fallback=check.returncode!=0
    if fallback:
        installed=Path('/usr/share/texlive/texmf-dist')
        if not (installed/'tex/latex/base/latex.ltx').exists():
            raise SystemExit('A functioning XeLaTeX installation is required.')
        cache.mkdir(parents=True,exist_ok=True)
        env.update(TEXMF='{'+str(cache)+',/etc/texmf,/usr/share/texlive/texmf-dist,/usr/share/texmf}',
                   TEXMFVAR=str(cache/'var'),TEXMFCONFIG=str(cache/'config'),
                   VARTEXFONTS=str(cache/'fonts'),TEXFORMATS=str(cache)+'//:')
        if not (cache/'xelatex.fmt').exists():
            run(['xetex','-ini','-etex','-interaction=nonstopmode','-halt-on-error',
                 '-jobname=xelatex','-progname=xelatex','xelatex.ini'],cache,env,logs/'00_format.txt')
    if not a.skip_generate:
        run([sys.executable,'build_chapter.py',a.tag],d,env,logs/'01_schema_and_generation.txt')
    commands=[['xelatex','-interaction=nonstopmode','-halt-on-error',a.tag+'_test.tex'],
              ['bibtex',a.tag+'_test'],
              ['xelatex','-interaction=nonstopmode','-halt-on-error',a.tag+'_test.tex'],
              ['xelatex','-interaction=nonstopmode','-halt-on-error',a.tag+'_test.tex']]
    for i,cmd in enumerate(commands,2):
        run(cmd,d,env,logs/f'{i:02d}_{cmd[0]}.txt')
    status={'tag':a.tag,'commands':[c[0] for c in commands],
            'local_format_fallback':fallback,'all_returncodes_zero':True,
            'pdf':a.tag+'_test.pdf'}
    (logs/'build_summary.json').write_text(json.dumps(status,indent=2)+'\n')
    print(json.dumps(status,indent=2))

if __name__=='__main__':main()
