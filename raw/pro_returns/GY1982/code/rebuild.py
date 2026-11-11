#!/usr/bin/env python3
"""Rebuild and verify the GY1982 chapter from its authoritative data.

Requirements: Python 3, XeLaTeX, BibTeX, the packages loaded by the supplied
gelfand_companion.sty, and a Unicode text font (DejaVu Serif is suitable).
Use --calculations to rerun the independent Haar-integral calculation; this
additional step requires SymPy. The supplied builder and style are unmodified.

The fallback format creation handles the minimal TeX Live installation used
for this task. On an ordinary complete TeX installation it is not needed.
"""
from pathlib import Path
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--calculations', action='store_true')
    parser.add_argument('--directory', type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    root = args.directory.resolve()
    logs = root / 'code' / 'build_logs'
    logs.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    manifest = {'commands': [], 'supplied_files': {}}

    for filename in ('build_chapter.py', 'gelfand_companion.sty'):
        target = root / filename
        original = root / 'code' / 'kit_original' / filename
        same = target.read_bytes() == original.read_bytes()
        manifest['supplied_files'][filename] = {
            'sha256': hashlib.sha256(target.read_bytes()).hexdigest(),
            'identical_to_supplied': same,
        }
        if not same:
            raise SystemExit(f'{filename} differs from the supplied file; review before rebuilding.')

    def run(argv, name, cwd=None):
        started = time.monotonic()
        completed = subprocess.run(argv, cwd=cwd or root, env=env,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   text=True, errors='replace')
        (logs / name).write_text(completed.stdout, encoding='utf-8')
        manifest['commands'].append({'command': argv, 'log': name,
                                     'returncode': completed.returncode,
                                     'elapsed_seconds': round(time.monotonic()-started, 3)})
        print(f'{name}: exit {completed.returncode}')
        if completed.returncode:
            print('\n'.join(completed.stdout.splitlines()[-35:]))
            (logs / 'build_manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
            raise SystemExit(completed.returncode)
        return completed.stdout

    run([sys.executable, 'build_chapter.py', 'GY1982'], '01_builder.txt')
    run([sys.executable, 'code/chapter_checks.py', '.'], '02_semantic_checks.txt')
    if args.calculations:
        run([sys.executable, 'code/haar_check.py'], '03_haar_check.txt')

    for tool in ('xelatex', 'bibtex', 'kpsewhich'):
        if shutil.which(tool) is None:
            raise SystemExit(f'Required program not found: {tool}')
    probe = subprocess.run(['kpsewhich', '-format=fmt', 'xelatex.fmt'], env=env,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if not probe.stdout.strip():
        texmf = Path('/usr/share/texlive/texmf-dist')
        if not texmf.is_dir() or shutil.which('xetex') is None:
            raise SystemExit('xelatex.fmt is absent. Install the XeLaTeX format for your TeX distribution.')
        env['TEXMF'] = '{/usr/share/texlive/texmf-dist,/usr/share/texmf}'
        cache = root / 'code' / 'tex_cache'
        cache.mkdir(exist_ok=True)
        if not (cache / 'xelatex.fmt').exists():
            run(['xetex', '-ini', '-etex', '-jobname=xelatex', '-progname=xelatex',
                 '-interaction=nonstopmode', '-halt-on-error', 'xelatex.ini'],
                '04_local_format.txt', cache)
        env['TEXFORMATS'] = str(cache) + os.pathsep
        manifest['format_workaround'] = 'Created or reused a local XeLaTeX format; no system files changed.'
    manifest['tex_programs'] = {
        tool: subprocess.run([tool, '--version'], env=env, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, text=True).stdout.splitlines()[0]
        for tool in ('xelatex', 'bibtex')
    }
    tex = ['xelatex', '-interaction=nonstopmode', '-halt-on-error', 'GY1982_test.tex']
    run(tex, '05_xelatex_first.txt')
    run(['bibtex', 'GY1982_test'], '06_bibtex.txt')
    run(tex, '07_xelatex_second.txt')
    run(tex, '08_xelatex_final.txt')
    final_log = (root / 'GY1982_test.log').read_text(errors='replace')
    problematic = [line for line in final_log.splitlines()
                   if ('undefined' in line.lower() or 'multiply defined' in line.lower()
                       or line.startswith('!') or 'Missing character:' in line)]
    manifest['unresolved_diagnostics'] = problematic
    manifest['overfull_boxes'] = [line for line in final_log.splitlines() if 'Overfull' in line]
    (logs / 'build_manifest.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
    if problematic:
        print('\n'.join(problematic))
        raise SystemExit('The final TeX pass has unresolved diagnostics.')
    print('PASS: supplied builder, semantic checks, bibliography, and final XeLaTeX pass.')
    print('Output: GY1982_test.pdf')


if __name__ == '__main__':
    main()
