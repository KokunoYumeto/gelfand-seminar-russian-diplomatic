#!/usr/bin/env python3
"""Build the supplied chapter with XeLaTeX/BibTeX, preserving complete logs.

On this execution image the installed TeX tree exists but its ls-R database
and prebuilt XeLaTeX format do not.  The fallback below only changes process
search paths and writes a private format under the chapter directory.  It
does not modify the supplied style, system files, or any mathematical data.
"""
from pathlib import Path
import argparse
import os
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('tag', nargs='?', default='GY1975')
parser.add_argument('--directory', type=Path, default=Path(__file__).resolve().parent.parent)
args = parser.parse_args()
root = args.directory.resolve()
logs = root / 'build_logs'
logs.mkdir(exist_ok=True)
for old_pass in logs.glob('pass_*.log'):
    old_pass.unlink()
env = dict(os.environ)


def execute(command, log_name, cwd=root):
    result = subprocess.run(command, cwd=cwd, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (logs / log_name).write_text(result.stdout)
    print(' '.join(command), '->', result.returncode, flush=True)
    if result.returncode:
        print(result.stdout[-6000:])
        raise SystemExit(result.returncode)
    return result


source_lookup = subprocess.run(['kpsewhich', 'latex.ltx'], env=env,
                               text=True, capture_output=True)
format_lookup = subprocess.run(['kpsewhich', '-engine=xetex', 'xelatex.fmt'], env=env,
                               text=True, capture_output=True)
if source_lookup.returncode or format_lookup.returncode:
    tex_cache = root / 'texcache'
    tex_cache.mkdir(exist_ok=True)
    candidates = [Path('/usr/share/texlive/texmf-dist'), Path('/usr/share/texmf')]
    trees = [str(p) for p in candidates if p.exists()]
    if trees:
        env['TEXMF'] = '{' + ','.join([str(tex_cache), *trees]) + '}'
    env['TEXMFVAR'] = str(tex_cache)
    env['TEXMFCONFIG'] = str(tex_cache)
    env['TEXFORMATS'] = str(tex_cache) + ':'
    env['TEXMFOUTPUT'] = str(tex_cache)
    if not (tex_cache / 'xelatex.fmt').exists():
        execute(['xetex', '-ini', '-etex', '-jobname=xelatex', '-progname=xelatex',
                 '-interaction=nonstopmode', '-halt-on-error', 'xelatex.ini'],
                'format.log', cwd=tex_cache)

execute(['python', 'build_chapter.py', args.tag], 'validation.log')
for number, command in enumerate([
    ['xelatex', '-interaction=nonstopmode', '-halt-on-error', args.tag + '_test.tex'],
    ['bibtex', args.tag + '_test'],
    ['xelatex', '-interaction=nonstopmode', '-halt-on-error', args.tag + '_test.tex'],
    ['xelatex', '-interaction=nonstopmode', '-halt-on-error', args.tag + '_test.tex'],
], 1):
    execute(command, f'pass_{number}.log')
# A bibliography can shift more than one page of cross-references.  Continue
# only when TeX explicitly requests another pass, with a strict finite limit.
for number in range(5, 8):
    previous = (logs / f'pass_{number-1}.log').read_text()
    if not any(token in previous for token in [
        'Rerun to get cross-references right',
        'Rerun to get outlines right',
        'Please rerun LaTeX',
    ]):
        break
    execute(['xelatex', '-interaction=nonstopmode', '-halt-on-error',
             args.tag + '_test.tex'], f'pass_{number}.log')
else:
    final = (logs / 'pass_7.log').read_text()
    if 'Rerun to get cross-references right' in final:
        raise SystemExit('Cross-references did not stabilize after seven passes.')
print('Built', root / (args.tag + '_test.pdf'))
