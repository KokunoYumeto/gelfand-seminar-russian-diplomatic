"""Build the supplied test driver with XeLaTeX, BibTeX, and two reruns.

On a normal TeX installation, this uses the standard search configuration.
The execution image used for this chapter omitted generated TeX databases
and formats. If that condition is detected, a format is generated locally
from the installed sources; no system files or home directories are changed.
"""
import json
import os
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKS = ROOT / 'checks'
RUNTIME = ROOT / 'runtime'
CHECKS.mkdir(exist_ok=True)
ENV = os.environ.copy()
ENV['max_print_line'] = '1000'

def lookup(filename):
    result = subprocess.run(['kpsewhich', filename], cwd=ROOT, env=ENV,
                            text=True, capture_output=True)
    return result.stdout.strip() if result.returncode == 0 else ''

def run(command, logname):
    print('Running:', ' '.join(str(x) for x in command), flush=True)
    with (CHECKS / logname).open('w') as out:
        result = subprocess.run(command, cwd=ROOT, env=ENV,
                                stdout=out, stderr=subprocess.STDOUT)
    print(logname, 'exit status', result.returncode, flush=True)
    if result.returncode:
        print((CHECKS / logname).read_text(errors='replace')[-6000:])
        raise SystemExit(result.returncode)

for executable in ['xelatex', 'xetex', 'bibtex', 'kpsewhich']:
    if not shutil.which(executable):
        raise SystemExit('Required TeX executable not found: ' + executable)

local_tree = RUNTIME / 'texmf'
fallback = not lookup('latex.ltx')
if fallback:
    roots = [local_tree, Path('/etc/texmf'), Path('/usr/share/texmf'),
             Path('/usr/share/texlive/texmf-dist')]
    if not roots[-1].is_dir():
        raise SystemExit('LaTeX sources not found; install a complete TeX distribution.')
    local_tree.mkdir(parents=True, exist_ok=True)
    ENV['TEXMF'] = '{' + ','.join(str(p) for p in roots if p.is_dir()) + '}'
    for variable, directory in [('TEXMFVAR', 'texmf-var'), ('TEXMFCONFIG', 'texmf-config')]:
        target = RUNTIME / directory
        target.mkdir(parents=True, exist_ok=True)
        ENV[variable] = str(target)

format_args = []
if not lookup('xelatex.fmt'):
    destination = local_tree / 'web2c'
    destination.mkdir(parents=True, exist_ok=True)
    run(['xetex', '-ini', '-etex', '-interaction=nonstopmode', '-halt-on-error',
         '-jobname=xelatex', '-output-directory=' + str(destination), 'xelatex.ini'],
        'tex_format_build.txt')
    format_args = ['-fmt=' + str(destination / 'xelatex.fmt')]

engine = ['xelatex', '-interaction=nonstopmode', '-halt-on-error',
          '-file-line-error', *format_args, 'GY1980_test.tex']
run(engine, 'xelatex_pass1.txt')
run(['bibtex', 'GY1980_test'], 'bibtex_output.txt')
run(engine, 'xelatex_pass2.txt')
run(engine, 'xelatex_pass3.txt')

# Long chapters may require one more pass after citation widths alter pagination.
for pass_number in range(4, 7):
    log = (ROOT / 'GY1980_test.log').read_text(errors='replace')
    if not any(message in log for message in ['Label(s) may have changed',
                                               'Rerun to get cross-references right',
                                               'Rerun to get outlines right']):
        break
    run(engine, f'xelatex_pass{pass_number}.txt')
else:
    raise SystemExit('Cross-references failed to stabilize after six XeLaTeX passes.')

environment = {'local_TeX_bootstrap': fallback,
               'TEXMF_override': ENV.get('TEXMF') if fallback else None,
               'commands': {'xelatex': engine, 'bibtex': ['bibtex', 'GY1980_test']}}
for command in ['xelatex', 'bibtex']:
    version = subprocess.run([command, '--version'], env=ENV,
                             text=True, capture_output=True)
    environment[command + '_version'] = version.stdout.splitlines()[0]
(CHECKS / 'tex_environment.json').write_text(json.dumps(environment, indent=2) + '\n')
print('XeLaTeX / BibTeX build completed.')
