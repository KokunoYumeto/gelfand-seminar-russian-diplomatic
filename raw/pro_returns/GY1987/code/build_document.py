#!/usr/bin/env python3
"""Build with the supplied builder, XeLaTeX, BibTeX and two XeLaTeX passes.

On the research host the binaries and distribution are installed but the
default kpathsea roots are unavailable. A private format built from the
existing read-only TeX distribution fixes this without a system mutation.
Ordinary TeX Live installations use their normal configuration.
"""
import argparse,json,os
from pathlib import Path
import subprocess,sys

parser=argparse.ArgumentParser()
parser.add_argument('directory',nargs='?',type=Path,default=Path('.'))
parser.add_argument('--checkpoint',action='store_true')
args=parser.parse_args()
d=args.directory.resolve();logs=d/'logs';logs.mkdir(exist_ok=True)
env=os.environ.copy()
probe=subprocess.run(['kpsewhich','book.cls'],capture_output=True,text=True)
configuration={'default_book_class':probe.stdout.strip()}
if not probe.stdout.strip():
    tree=Path('/usr/share/texlive/texmf-dist')
    if not (tree/'tex/latex/base/book.cls').exists():
        raise RuntimeError('No usable installed TeX distribution found')
    private=d.parent/'tex_build_runtime'
    private.mkdir(exist_ok=True)
    roots='{'+str(tree)+',/usr/share/texmf}'
    env.update(TEXMFCNF=str(tree/'web2c'),TEXMF=roots,TEXMFDBS=roots,
               TEXMFVAR=str(private),TEXMFCONFIG=str(private),
               TEXFORMATS=str(private)+'//',TEXMFOUTPUT=str(private))
    configuration['private_format_directory']=str(private)
    configuration['existing_distribution']=str(tree)
    if not (private/'xelatex.fmt').exists():
        command=['xetex','-ini','-etex','-interaction=nonstopmode','-halt-on-error',
                 '-progname=xelatex','-jobname=xelatex','xelatex.ini']
        with (logs/'format_build.log').open('w') as stream:
            result=subprocess.run(command,cwd=private,env=env,stdout=stream,stderr=subprocess.STDOUT)
        if result.returncode:raise RuntimeError('Private XeLaTeX format failed; see logs/format_build.log')

commands=[([sys.executable,'build_chapter.py','GY1987'],'build.log'),
          (['xelatex','-interaction=nonstopmode','-halt-on-error','GY1987_test.tex'],'xelatex_pass1_console.log')]
if not args.checkpoint:
    commands += [(['bibtex','GY1987_test'],'bibtex_console.log'),
                 (['xelatex','-interaction=nonstopmode','-halt-on-error','GY1987_test.tex'],'xelatex_pass2_console.log'),
                 (['xelatex','-interaction=nonstopmode','-halt-on-error','GY1987_test.tex'],'xelatex_pass3_console.log')]
results=[]
for command,logname in commands:
    with (logs/logname).open('w') as stream:
        result=subprocess.run(command,cwd=d,env=env,stdout=stream,stderr=subprocess.STDOUT)
    results.append({'command':command,'returncode':result.returncode,'output':str(Path('logs')/logname)})
    print(json.dumps(results[-1]),flush=True)
    if result.returncode and not (args.checkpoint and command[0]==sys.executable):break
if not args.checkpoint and all(r['returncode']==0 for r in results):
    # A changed bibliography can move the later cross-references one pass
    # beyond the required three XeLaTeX runs. Resolve that concrete warning.
    for pass_number in range(4,7):
        tex_log=(d/'GY1987_test.log').read_text(errors='replace')
        if 'Label(s) may have changed' not in tex_log and 'Rerun to get' not in tex_log:
            break
        command=['xelatex','-interaction=nonstopmode','-halt-on-error','GY1987_test.tex']
        logname=f'xelatex_pass{pass_number}_console.log'
        with (logs/logname).open('w') as stream:
            result=subprocess.run(command,cwd=d,env=env,stdout=stream,stderr=subprocess.STDOUT)
        results.append({'command':command,'returncode':result.returncode,'output':str(Path('logs')/logname)})
        print(json.dumps(results[-1]),flush=True)
        if result.returncode:break
configuration['commands']=results
configuration['status']='PASS' if all(r['returncode']==0 for r in results) else 'FAIL'
(logs/'build_commands.json').write_text(json.dumps(configuration,indent=2)+'\n')
sys.exit(0 if configuration['status']=='PASS' else 1)
