#!/usr/bin/env python3
"""Rebuild using the supplied builder and the requested XeLaTeX/BibTeX sequence.

Run from any directory: python code/build_all.py
Uses the local TeX-source fallback only when the host has no prebuilt format.
"""
from pathlib import Path
import json
import re
import subprocess
import sys
from tex_environment import ensure_tex_environment

D=Path(__file__).resolve().parent.parent
env=ensure_tex_environment(D)
commands=[['python','build_chapter.py','GY1979'],
          ['python','code/audit_chapter.py'],
          ['xelatex','-interaction=nonstopmode','-halt-on-error','GY1979_test.tex'],
          ['bibtex','GY1979_test'],
          ['xelatex','-interaction=nonstopmode','-halt-on-error','GY1979_test.tex'],
          ['xelatex','-interaction=nonstopmode','-halt-on-error','GY1979_test.tex']]
statuses=[]
with (D/'code/build_output.txt').open('w') as log:
    for command in commands:
        print('Running '+' '.join(command),flush=True)
        log.write('$ '+' '.join(command)+'\n');log.flush()
        result=subprocess.run(command,cwd=D,env=env,stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,text=True)
        log.write(result.stdout);log.flush()
        statuses.append({'command':command,'exit_code':result.returncode})
        if result.returncode:
            print(result.stdout[-10000:])
            (D/'code/build_status.json').write_text(json.dumps(statuses,indent=2)+'\n')
            sys.exit(result.returncode)
log=(D/'GY1979_test.log').read_text(errors='replace')
warnings=[line for line in log.splitlines() if any(k in line for k in
          ('Overfull','Underfull','undefined','Missing character','LaTeX Error','Warning:'))]
(D/'code/build_status.json').write_text(json.dumps({'commands':statuses,'log_flags':warnings},indent=2)+'\n')
print('Build completed. Final log flags:')
print('\n'.join(warnings) if warnings else '(none)')
