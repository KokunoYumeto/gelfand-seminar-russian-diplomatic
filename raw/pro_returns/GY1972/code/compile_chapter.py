"""Run the required XeLaTeX/BibTeX build, keeping logs and local TeX caches.

Usage: python compile_chapter.py CHAPTER_DIRECTORY
On a normal TeX installation no bootstrap is needed. The supplied execution
environment has a complete TeX tree but no system filename database or formats;
the optional local fallback below uses the installed tree without global writes.
"""
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys

out = Path(sys.argv[1]).resolve()
logs = out / 'logs'
logs.mkdir(exist_ok=True)
cache = out / 'tex_cache'
cache.mkdir(exist_ok=True)
env = os.environ.copy()
bootstrap = []

def lookup(name):
    return subprocess.run(['kpsewhich',name],env=env,capture_output=True,text=True).stdout.strip()

if not lookup('latex.ltx'):
    installed = Path('/usr/share/texlive/texmf-dist')
    if not installed.is_dir():
        raise RuntimeError('An installed LaTeX package tree is required.')
    env['TEXMFCNF'] = str(installed/'web2c')
    env['TEXMF'] = '{'+str(installed)+',/usr/share/texmf}'
    bootstrap.append('Used installed TeX trees directly because system filename databases are absent.')
env['TEXMFVAR'] = str(cache/'var')
env['TEXMFCONFIG'] = str(cache/'config')
env['TEXFORMATS'] = str(cache)+':'+env.get('TEXFORMATS','')
env['VARTEXFONTS'] = str(cache/'fonts')

def run(args, name, cwd=out):
    with (logs/name).open('w') as stream:
        result = subprocess.run(args,cwd=cwd,env=env,stdout=stream,stderr=subprocess.STDOUT)
    if result.returncode:
        print((logs/name).read_text()[-6500:])
        raise SystemExit(f'{name}: command failed ({result.returncode})')
    if args[0] == 'xelatex':
        auxiliary = out/'GY1972_test.aux'
        data = auxiliary.read_bytes()
        if b'\\gdef \\@abspage@last{' not in data:
            raise RuntimeError(f'{name}: auxiliary file is incomplete despite engine success.')
        (logs/(name.removesuffix('.txt')+'.aux')).write_bytes(data)

if not lookup('xelatex.fmt'):
    run(['xetex','-ini','-etex','-interaction=nonstopmode','-halt-on-error',
         '-jobname=xelatex','-progname=xelatex','xelatex.ini'], 'format_bootstrap.txt', cache)
    bootstrap.append('Created xelatex.fmt locally from the installed xelatex.ini.')

run([sys.executable,'build_chapter.py','GY1972'],'build_chapter.txt')
# Rebuild these generated streams from scratch. A clean first pass also makes
# this script independent of stale auxiliaries from an interrupted earlier run.
for suffix in ('.aux','.out','.toc'):
    (out/('GY1972_test'+suffix)).unlink(missing_ok=True)
run(['xelatex','-interaction=nonstopmode','-halt-on-error','GY1972_test.tex'],'xelatex_pass1.txt')
run(['bibtex','GY1972_test'],'bibtex.txt')
run(['xelatex','-interaction=nonstopmode','-halt-on-error','GY1972_test.tex'],'xelatex_pass2.txt')
run(['xelatex','-interaction=nonstopmode','-halt-on-error','GY1972_test.tex'],'xelatex_pass3.txt')
extra_passes = 0
while 'Label(s) may have changed' in (out/'GY1972_test.log').read_text():
    if extra_passes >= 3:
        raise RuntimeError('Cross-references did not stabilize after three additional passes.')
    extra_passes += 1
    run(['xelatex','-interaction=nonstopmode','-halt-on-error','GY1972_test.tex'],
        f'xelatex_pass{3+extra_passes}.txt')
summary = dict(status='required four-command compilation completed',bootstrap=bootstrap,
               additional_reference_stability_passes=extra_passes,
               engine=subprocess.run(['xelatex','--version'],capture_output=True,text=True).stdout.splitlines()[0],
               pdf_bytes=(out/'GY1972_test.pdf').stat().st_size)
(logs/'compile_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
