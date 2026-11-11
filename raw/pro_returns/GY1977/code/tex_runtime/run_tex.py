#!/usr/bin/env python3
"""Run the installed TeX Live binaries with a workspace-local generated tree.

No system files are changed.  The installed package trees are read directly,
because this image lacks the ls-R databases to which their symlinks point.
Usage: python3 run_tex.py --bootstrap
       python3 /path/to/run_tex.py xelatex [xelatex arguments]
       python3 /path/to/run_tex.py bibtex [bibtex arguments]
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
DIST = Path('/usr/share/texlive/texmf-dist')
DEBIAN = Path('/usr/share/texmf')
TREE = ROOT / 'texmf'
FORMATS = TREE / 'web2c' / 'xetex'


def environment() -> dict[str, str]:
    env = os.environ.copy()
    writable = {
        'TEXMFHOME': ROOT / 'texmf-home',
        'TEXMFCONFIG': ROOT / 'texmf-config',
        'TEXMFVAR': ROOT / 'texmf-var',
        'TEXMFSYSVAR': ROOT / 'texmf-var',
        'TEXMFSYSCONFIG': ROOT / 'texmf-config',
        'TEXMFLOCAL': TREE,
        'TEXMFCACHE': ROOT / 'cache',
        'VARTEXFONTS': ROOT / 'fonts-cache',
    }
    for key, path in writable.items():
        path.mkdir(parents=True, exist_ok=True)
        env[key] = str(path)
    # Deliberately no !!: the system ls-R files are dangling symlinks.
    env['TEXMF'] = '{' + ','.join(map(str, [TREE, ROOT / 'texmf-config',
        ROOT / 'texmf-var', ROOT / 'texmf-home', Path('/etc/texmf'), DEBIAN, DIST])) + '}'
    env['TEXMFDBS'] = str(TREE)
    env['TEXFORMATS'] = str(FORMATS) + '//:'
    # Do not invoke absent system fmtutil configurations or generate fonts elsewhere.
    env['MKTEXFMT'] = '0'
    env['MKTEXPK'] = '0'
    env['MKTEXTFM'] = '0'
    env['MKTEXMF'] = '0'
    return env


def bootstrap(force: bool = False) -> None:
    env = environment()
    if (FORMATS / 'xelatex.fmt').is_file() and not force:
        return
    if not (DIST / 'tex/latex/base/latex.ltx').is_file():
        raise SystemExit('The installed TeX Live package tree is required: ' + str(DIST))
    config = TREE / 'tex/generic/config'
    config.mkdir(parents=True, exist_ok=True)
    # Supplied TeX Live base language configuration.  Russian Unicode text is
    # supported by the delivered style's Babel locale fallback; no Russian
    # hyphenation package is installed in this image.
    shutil.copyfile(DIST / 'tex/generic/config/language.us', config / 'language.dat')
    fontmap = TREE / 'fonts/map/pdftex/local'
    fontmap.mkdir(parents=True, exist_ok=True)
    maps = sorted((DIST / 'fonts/map/dvips/amsfonts').glob('*.map'))
    maps += [DEBIAN / 'fonts/map/dvips/lm/lm.map']
    with (fontmap / 'pdftex.map').open('w', encoding='utf-8') as output:
        for source in maps:
            if source.is_file():
                output.write('% Source: ' + str(source) + '\n')
                output.write(source.read_text(encoding='utf-8'))
                output.write('\n')
    dvipdf = TREE / 'dvipdfmx'
    dvipdf.mkdir(parents=True, exist_ok=True)
    # Retain the distribution driver configuration, removing only references
    # to absent generated CJK maps (the chapter contains no CJK text).
    lines = (DIST / 'dvipdfmx/dvipdfmx.cfg').read_text(encoding='utf-8').splitlines()
    (dvipdf / 'dvipdfmx.cfg').write_text('\n'.join(
        line for line in lines if line.split() not in [['f', 'kanjix.map'], ['f', 'ckx.map']]
    ) + '\n', encoding='utf-8')
    FORMATS.mkdir(parents=True, exist_ok=True)
    command = ['/usr/bin/xetex', '-ini', '-etex', '-no-shell-escape',
        '-interaction=nonstopmode', '-halt-on-error', '-jobname=xelatex',
        '-progname=xelatex', 'xelatex.ini']
    result = subprocess.run(command, cwd=FORMATS, env=env,
        text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (ROOT / 'bootstrap.log').write_text(result.stdout, encoding='utf-8')
    if result.returncode or not (FORMATS / 'xelatex.fmt').is_file():
        print(result.stdout, file=sys.stderr)
        raise SystemExit(result.returncode or 1)
    version = subprocess.check_output(['/usr/bin/xetex', '--version'], text=True).splitlines()[0]
    (ROOT / 'runtime_manifest.json').write_text(json.dumps({
        'engine': version,
        'read_only_package_trees': [str(DIST), str(DEBIAN)],
        'generated_format': str(FORMATS / 'xelatex.fmt'),
        'bootstrap_command': command,
        'network_downloads': [],
        'font_map_sources': [str(p) for p in maps if p.is_file()],
        'language_configuration_source': str(DIST / 'tex/generic/config/language.us'),
        'scope': 'XeLaTeX and BibTeX for gelfand_companion; installed packages, English hyphenation, Unicode Russian locale',
    }, indent=2) + '\n', encoding='utf-8')
    print('Generated local xelatex format: ' + str(FORMATS / 'xelatex.fmt'))


def main() -> None:
    args = sys.argv[1:]
    if not args or args == ['--help']:
        print(__doc__)
        return
    if args == ['--bootstrap']:
        bootstrap(force=True)
        return
    if args[0] not in {'xelatex', 'bibtex', 'kpsewhich', 'xdvipdfmx'}:
        raise SystemExit('Supported commands: xelatex, bibtex, kpsewhich, xdvipdfmx')
    bootstrap()
    executable = shutil.which(args[0])
    if not executable:
        raise SystemExit('Installed binary not found: ' + args[0])
    os.execve(executable, [executable, *args[1:]], environment())


if __name__ == '__main__':
    main()
