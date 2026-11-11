#!/usr/bin/env python3
"""Run the supplied builder and the required XeLaTeX/BibTeX sequence.

Some container distributions install TeX input files but omit their generated
filename database and XeLaTeX format. In that case this script generates a
private format in .build-cache, without altering the system TeX installation.
On an ordinary complete TeX Live installation no repair is needed.
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'audit'


def query(name, env):
    p = subprocess.run(['kpsewhich', name], env=env, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.stdout.strip() if p.returncode == 0 else ''


def run(command, log, env):
    print('Running:', ' '.join(str(x) for x in command), flush=True)
    with (AUDIT / log).open('w') as f:
        p = subprocess.run(command, cwd=ROOT, env=env,
                           stdout=f, stderr=subprocess.STDOUT)
    if p.returncode:
        tail = (AUDIT / log).read_text(errors='replace').splitlines()[-35:]
        print('\n'.join(tail), file=sys.stderr)
        raise SystemExit(p.returncode)


def main():
    AUDIT.mkdir(exist_ok=True)
    env = os.environ.copy()
    configuration = {'private_format_generated': False}
    if not query('latex.ltx', env):
        directories = ['/usr/share/texmf', '/usr/share/texlive/texmf-dist']
        directories = [d for d in directories if pathlib.Path(d).is_dir()]
        if not directories:
            raise RuntimeError('No usable TeX input tree found.')
        env['TEXMF'] = '{' + ','.join(directories) + '}'
        configuration['TEXMF'] = env['TEXMF']
    if not query('xelatex.fmt', env):
        cache = ROOT / '.build-cache'
        cache.mkdir(exist_ok=True)
        env['TEXFORMATS'] = str(cache) + ':'
        env['TEXMFVAR'] = str(cache / 'texmf-var')
        env['TEXMFCONFIG'] = str(cache / 'texmf-config')
        if not (cache / 'xelatex.fmt').exists():
            run(['xetex', '-ini', '-etex', '-jobname=xelatex', '-progname=xelatex',
                 '-interaction=nonstopmode', '-halt-on-error',
                 '-output-directory=' + str(cache), 'xelatex.ini'],
                'format_generation.log', env)
            configuration['private_format_generated'] = True
        configuration['TEXFORMATS'] = '.build-cache:'
    configuration['xelatex'] = shutil.which('xelatex')
    configuration['bibtex'] = shutil.which('bibtex')
    (AUDIT / 'build_environment.json').write_text(json.dumps(configuration, indent=2) + '\n')
    run([sys.executable, 'build_chapter.py', 'GY1971'], 'builder.log', env)
    xelatex = ['xelatex', '-interaction=nonstopmode', '-halt-on-error', 'GY1971_test.tex']
    run(xelatex, 'xelatex_pass1.log', env)
    run(['bibtex', 'GY1971_test'], 'bibtex_console.log', env)
    run(xelatex, 'xelatex_pass2.log', env)
    run(xelatex, 'xelatex_pass3.log', env)
    print('Completed the required four-stage typesetting sequence.', flush=True)


if __name__ == '__main__':
    main()
