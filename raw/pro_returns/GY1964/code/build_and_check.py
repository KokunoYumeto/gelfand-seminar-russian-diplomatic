"""Run the required chapter build, preserving every tool's complete output.

Usage: python code/build_and_check.py [directory]
The directory must contain the authoritative seven files and supplied kit.
"""
from pathlib import Path
import subprocess
import sys
import json
import re
import shutil
from tex_environment import environment

def main():
    directory=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
    logs=directory/'evidence'/'build'
    logs.mkdir(parents=True,exist_ok=True)
    env=environment(directory,logs)
    commands=[('builder',[sys.executable,'build_chapter.py','GY1964']),
              ('xelatex_1',['xelatex','-interaction=nonstopmode','-halt-on-error','GY1964_test.tex']),
              ('bibtex',['bibtex','GY1964_test']),
              ('xelatex_2',['xelatex','-interaction=nonstopmode','-halt-on-error','GY1964_test.tex']),
              ('xelatex_3',['xelatex','-interaction=nonstopmode','-halt-on-error','GY1964_test.tex'])]
    results=[]
    for name,command in commands:
        p=subprocess.run(command,cwd=directory,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (logs/(name+'.txt')).write_text(p.stdout)
        result={'step':name,'command':command,'returncode':p.returncode}
        results.append(result)
        print(name,'exit',p.returncode,flush=True)
        if p.returncode:
            print(p.stdout[-8000:])
            (logs/'build_results.json').write_text(json.dumps(results,indent=2)+'\n')
            raise SystemExit(p.returncode)
    text=(directory/'GY1964_test.log').read_text(errors='replace')
    checks={
      'latex_errors':re.findall(r'^!.*$',text,re.M),
      'overfull_boxes':re.findall(r'^Overfull[^\n]*',text,re.M),
      'missing_glyphs':re.findall(r'^Missing character:[^\n]*',text,re.M),
      'undefined_references':re.findall(r'[^\n]*(?:undefined|multiply defined)[^\n]*',text),
      'font_warnings':re.findall(r'^LaTeX Font Warning:[^\n]*',text,re.M),
      'bibliography_warnings':re.findall(r'^Warning--[^\n]*',(logs/'bibtex.txt').read_text(),re.M),
      'pdf_created':(directory/'GY1964_test.pdf').is_file(),
    }
    (logs/'build_results.json').write_text(json.dumps({'commands':results,'checks':checks},indent=2)+'\n')
    print(json.dumps(checks,indent=2),flush=True)
    if checks['latex_errors'] or checks['missing_glyphs'] or checks['undefined_references']:
        raise SystemExit(1)

if __name__=='__main__':main()
