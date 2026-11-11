#!/usr/bin/env python3
"""Compile the development separately while the occurrence data are assembled."""
from pathlib import Path
import subprocess
import sys
from tex_environment import ensure_tex_environment

D=Path(__file__).resolve().parent.parent
env=ensure_tex_environment(D)
(D/'development_check.tex').write_text(r'''\documentclass[11pt,oneside]{book}
\usepackage[a4paper,margin=22mm,headheight=15pt]{geometry}
\usepackage{gelfand_companion}
\setlength{\emergencystretch}{2em}
\begin{document}
\chapter{Development check}
\section{Developments}
\input{GY1979_development.tex}
\bibliographystyle{plainnat}
\bibliography{GY1979_references}
\end{document}
''')
commands=[['xelatex','-interaction=nonstopmode','-halt-on-error','development_check.tex'],
          ['bibtex','development_check'],
          ['xelatex','-interaction=nonstopmode','-halt-on-error','development_check.tex'],
          ['xelatex','-interaction=nonstopmode','-halt-on-error','development_check.tex']]
with (D/'code/development_build_output.txt').open('w') as log:
    for command in commands:
        log.write('$ '+' '.join(command)+'\n')
        run=subprocess.run(command,cwd=D,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        log.write(run.stdout)
        log.flush()
        if run.returncode:
            print(run.stdout[-7000:])
            sys.exit(run.returncode)
print('Development XeLaTeX/BibTeX build completed.')
