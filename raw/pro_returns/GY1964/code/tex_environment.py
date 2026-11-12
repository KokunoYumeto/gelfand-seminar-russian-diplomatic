"""Use installed TeX files without modifying a broken system filename database.

Normal TeX installations need no adjustment. This restricted environment had
installed package files but dangling ls-R/format links. The fallback creates
only a local XeLaTeX format, records its output, and uses recursive searches.
"""
from pathlib import Path
import os
import subprocess


def environment(directory, logs):
    env = os.environ.copy()
    probe = subprocess.run(['kpsewhich', 'latex.ltx'], capture_output=True,
                           text=True, env=env)
    if probe.returncode == 0:
        return env
    roots = [Path('/usr/share/texlive/texmf-dist'), Path('/usr/share/texmf'),
             Path('/etc/texmf')]
    roots = [str(p) for p in roots if p.is_dir()]
    if not roots:
        raise RuntimeError('No installed TeX tree found.')
    cache = Path(directory) / '.tex-cache'
    cache.mkdir(exist_ok=True)
    env['TEXMF'] = '{' + ','.join(roots) + '}'
    env['TEXMFVAR'] = str(cache / 'var')
    env['TEXMFCONFIG'] = str(cache / 'config')
    env['TEXFORMATS'] = str(cache) + ':'
    if not (cache / 'xelatex.fmt').is_file():
        command = ['xetex', '-ini', '-etex', '-interaction=nonstopmode',
                   '-halt-on-error', '-jobname=xelatex', '-progname=xelatex',
                   'xelatex.ini']
        p = subprocess.run(command, cwd=cache, env=env, text=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (Path(logs) / 'local_format.txt').write_text(p.stdout)
        if p.returncode:
            raise RuntimeError('Local XeLaTeX format creation failed:\n' + p.stdout[-6000:])
    (Path(logs) / 'environment.txt').write_text(
        'Installed system packages; local format fallback.\n' +
        '\n'.join(f'{k}={env[k]}' for k in
                  ('TEXMF', 'TEXMFVAR', 'TEXMFCONFIG', 'TEXFORMATS')) + '\n')
    return env
