"""Repair generated TeX state locally, only if the host installation needs it.

Ordinary configured TeX Live installations can use the commands in BUILD.md
without running this script. This file makes no system changes or downloads.
"""
from pathlib import Path
import os, subprocess
code=Path(__file__).resolve().parent
root=code/'texenv'
for n in ['formats','maps','config','var','texmf']:(root/n).mkdir(parents=True,exist_ok=True)
(root/'config'/'language.dat').write_text('english hyphen.tex\n')
paths=list(Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts').glob('*.map'))
lm=Path('/usr/share/texmf/fonts/map/dvips/lm/lm.map')
if lm.exists():paths.append(lm)
maps='\n'.join(p.read_text() for p in sorted(paths))
for n in ['pdftex.map','psfonts.map']:(root/'maps'/n).write_text(maps)
env=os.environ.copy()
env.update({
 'TEXMF':'{'+str(root/'texmf')+',/usr/share/texmf,/usr/share/texlive/texmf-dist}',
 'TEXMFVAR':str(root/'var'),'TEXMFCONFIG':str(root/'config'),'TEXMFHOME':str(root/'texmf'),
 'TEXFORMATS':str(root/'formats')+':',
 'TEXINPUTS':'.:'+str(root/'config')+'//:/usr/share/texlive/texmf-dist/tex/latex/base//:/usr/share/texlive/texmf-dist/tex//:/usr/share/texmf/tex//:',
 'TEXFONTMAPS':str(root/'maps')+'//:/usr/share/texlive/texmf-dist/fonts/map//:/usr/share/texmf/fonts/map//:',
 'TFMFONTS':'/usr/share/texlive/texmf-dist/fonts/tfm//:/usr/share/texmf/fonts/tfm//:',
 'VFFONTS':'/usr/share/texlive/texmf-dist/fonts/vf//:/usr/share/texmf/fonts/vf//:',
 'T1FONTS':'/usr/share/texlive/texmf-dist/fonts/type1//:/usr/share/texmf/fonts/type1//:/usr/share/fonts/type1//:',
 'TTFONTS':'/usr/share/fonts/truetype//:',
 'OPENTYPEFONTS':'/usr/share/texmf/fonts/opentype//:/usr/share/fonts/opentype//:',
 'ENCFONTS':'/usr/share/texlive/texmf-dist/fonts/enc//:/usr/share/texmf/fonts/enc//:',
 'BIBINPUTS':'.:/usr/share/texlive/texmf-dist/bibtex/bib//:',
 'BSTINPUTS':'.:/usr/share/texlive/texmf-dist/bibtex/bst//:'})
shell=['# Source from the archive root: source code/texenv.sh',
       'export GY_TEXROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)/texenv"']
for k,v in env.items():
    if k.startswith(('TEX','TFMF','VFF','T1F','TTFO','OPEN','ENCFO','BIBIN','BSTIN')) and k in {'TEXMF','TEXMFVAR','TEXMFCONFIG','TEXMFHOME','TEXFORMATS','TEXINPUTS','TEXFONTMAPS','TFMFONTS','VFFONTS','T1FONTS','TTFONTS','OPENTYPEFONTS','ENCFONTS','BIBINPUTS','BSTINPUTS'}:
        shell.append('export '+k+'="'+v.replace(str(root),'$GY_TEXROOT')+'"')
(code/'texenv.sh').write_text('\n'.join(shell)+'\n')
command=['xetex','-ini','-etex','-jobname=xelatex','-progname=xelatex',
         '-interaction=nonstopmode','-halt-on-error','-output-directory='+str(root/'formats'),
         '/usr/share/texlive/texmf-dist/tex/latex/tex-ini-files/xelatex.ini']
result=subprocess.run(command,env=env,cwd=code.parent,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
(code/'build'/'local_tex_setup.txt').write_text(result.stdout)
if result.returncode:raise SystemExit(result.returncode)
print('Local XeLaTeX format and font maps prepared. Source code/texenv.sh before compiling.')
