"""Build the supplied chapter with XeLaTeX/BibTeX; keep complete build logs.

Usage: python code/build_validate.py
Requires Python 3, XeLaTeX, BibTeX and the standard packages used by the supplied
gelfand_companion.sty. A workspace-only fallback handles TeX Live installations
whose installed packages have no generated filename database or format cache.
It never installs packages or edits the system TeX configuration.
"""
from pathlib import Path
import os, subprocess, sys, shutil

ROOT=Path(__file__).resolve().parents[1]
LOGS=ROOT/'code'/'build_logs'
LOGS.mkdir(exist_ok=True)
env=os.environ.copy()

def run(args,name):
    p=subprocess.run(args,cwd=ROOT,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (LOGS/name).write_text(p.stdout)
    print(name, 'exit',p.returncode)
    if p.returncode:
        print(p.stdout[-8000:])
        raise SystemExit(p.returncode)
    return p.stdout

def kpse(name):
    return subprocess.run(['kpsewhich',name],cwd=ROOT,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True).stdout.strip()

for command in ['xelatex','bibtex','kpsewhich']:
    if not shutil.which(command):raise SystemExit('Required executable not found: '+command)

run([sys.executable,'build_chapter.py','GY1978'],'01_schema.txt')
if not kpse('plainnat.bst'):
    trees=[str(p) for p in [Path('/usr/share/texmf'),Path('/usr/share/texlive/texmf-dist')] if p.exists()]
    if not trees:raise SystemExit('TeX packages unavailable; install a standard TeX Live distribution.')
    env['TEXMF']='{.,'+','.join(trees)+'}'
    print('Using installed TeX trees directly because their filename database is absent.')
if not kpse('xelatex.fmt'):
    cache=ROOT/'.tex_build'
    cache.mkdir(exist_ok=True)
    args=['xelatex','-etex','-ini','-interaction=nonstopmode','-halt-on-error','-jobname=xelatex','-progname=xelatex','xelatex.ini']
    p=subprocess.run(args,cwd=cache,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (LOGS/'02_format.txt').write_text(p.stdout)
    if p.returncode:
        print(p.stdout[-8000:]);raise SystemExit(p.returncode)
    env['TEXFORMATS']=str(cache)+'//:'

tex=['xelatex','-interaction=nonstopmode','-halt-on-error','GY1978_test.tex']
run(tex,'03_xelatex_initial.txt')
run(['bibtex','GY1978_test'],'04_bibtex.txt')
run(tex,'05_xelatex_second.txt')
run(tex,'06_xelatex_final.txt')
log=(ROOT/'GY1978_test.log').read_text(errors='replace')
failures=[line for line in log.splitlines() if
          line.startswith('!') or 'undefined citations' in line or
          'undefined references' in line or 'Missing character:' in line or
          ('Citation' in line and 'undefined' in line)]
if failures:
    print('\n'.join(failures));raise SystemExit('Unresolved compilation diagnostics.')
print('Schema, XeLaTeX, BibTeX and final citation/font checks passed.')
