"""Use the installed TeX tree without mutating global configuration.

Some sandbox images include TeX sources but omit ls-R and prebuilt formats.
If ordinary xelatex lookup works, this changes nothing. Otherwise it selects
the readable trees and creates xelatex.fmt in this project's temporary folder.
"""
from pathlib import Path
import os
import shutil
import subprocess


def ensure_tex_environment(project):
    env=os.environ.copy()
    check=subprocess.run(['kpsewhich','--engine=xetex','--format=fmt','xelatex.fmt'],
                         env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    if check.returncode==0 and check.stdout.strip():
        return env
    root=Path(project).resolve()/'.texruntime'
    root.mkdir(exist_ok=True)
    for sub in ['var','config','fonts']:
        (root/sub).mkdir(exist_ok=True)
    # No '!!' database-only prefixes: this image has source trees but no ls-R.
    trees=[str(root),'/usr/share/texmf','/usr/share/texlive/texmf-dist']
    env.update({'TEXMF':'{'+','.join(trees)+'}',
                'TEXFORMATS':str(root)+'//:',
                'TEXMFVAR':str(root/'var'),
                'TEXMFCONFIG':str(root/'config'),
                'VARTEXFONTS':str(root/'fonts')})
    fmt=root/'xelatex.fmt'
    if not fmt.exists():
        command=['xetex','-ini','-etex','-jobname=xelatex','-progname=xelatex','xelatex.ini']
        run=subprocess.run(command,cwd=root,env=env,stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,text=True)
        (root/'format_build_output.txt').write_text(run.stdout)
        (Path(project)/'code/format_build_output.txt').write_text(run.stdout)
        if run.returncode or not fmt.exists():
            raise RuntimeError('Local XeLaTeX format build failed:\n'+run.stdout[-7000:])
    return env
