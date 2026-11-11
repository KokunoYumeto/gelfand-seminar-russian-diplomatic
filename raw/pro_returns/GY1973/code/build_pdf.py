#!/usr/bin/env python3
"""Rebuild the supplied chapter with XeLaTeX/BibTeX; prepare a local format if needed.

No installed package or supplied style is modified. A runtime missing TeX's
generated filename database can use the installed distribution by direct search.
Run from the extracted deliverable directory: python code/build_pdf.py
"""
from pathlib import Path
import argparse
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile

def run(args, cwd, env, log):
    with log.open("w", encoding="utf-8") as f:
        result = subprocess.run(args, cwd=cwd, env=env, stdout=f,
                                stderr=subprocess.STDOUT, text=True)
    print(" ".join(map(str,args)), "->", result.returncode, flush=True)
    aux=cwd/"GY1973_test.aux"
    if aux.exists() and args[0] in {"xelatex","bibtex"}:
        data=aux.read_bytes()
        print("Auxiliary bytes:",len(data),"SHA256:",hashlib.sha256(data).hexdigest(),flush=True)
    if result.returncode:
        print(log.read_text(errors="replace")[-6000:])
        raise SystemExit(result.returncode)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--prepare",action="store_true")
    args=parser.parse_args()
    base=Path(__file__).resolve().parents[1]
    logs=base/"logs";logs.mkdir(exist_ok=True)
    runtime=base/".tex_runtime";runtime.mkdir(exist_ok=True)
    env=os.environ.copy()
    test=subprocess.run(["kpsewhich","fontspec.sty"],capture_output=True,text=True)
    fmtargs=[]
    if not test.stdout.strip():
        roots=[Path("/usr/share/texlive/texmf-dist"),Path("/usr/share/texmf"),
               Path("/etc/texmf")]
        if not (roots[0]/"tex/latex/fontspec/fontspec.sty").exists():
            raise SystemExit("Install XeLaTeX with fontspec, AMS, natbib and the supplied style's packages.")
        env["TEXMF"]="{"+",".join(str(p) for p in [runtime,*roots])+"}"
        env["TEXMFVAR"]=str(runtime)
        env["TEXMFCONFIG"]=str(runtime)
        fmt=runtime/"xelatex.fmt"
        if not fmt.exists():
            run(["xetex","-ini","-etex","-no-shell-escape",
                 "-interaction=nonstopmode","-halt-on-error","-jobname=xelatex",
                 str(roots[0]/"tex/latex/tex-ini-files/xelatex.ini")],
                 runtime,env,logs/"format_build.txt")
        fmtargs=["-fmt="+str(fmt)]
    if args.prepare:
        print("TeX runtime prepared.")
        return
    run([sys.executable,"build_chapter.py","GY1973"],base,env,logs/"builder.txt")
    # Keep in-progress TeX auxiliaries out of the final artifact directory.
    # Only a completed build replaces the published workspace outputs.
    with tempfile.TemporaryDirectory(prefix=".tex-build-",dir=base) as temp:
        job=Path(temp)
        for name in ["GY1973_chapter.tex","GY1973_test.tex",
                     "GY1973_references.bib","gelfand_companion.sty"]:
            shutil.copy2(base/name,job/name)
        if (base/"fonts").is_dir():
            shutil.copytree(base/"fonts",job/"fonts")
        command=["xelatex","-no-shell-escape","-interaction=nonstopmode",
                 "-halt-on-error","-file-line-error",*fmtargs,"GY1973_test.tex"]
        run(command,job,env,logs/"xelatex_pass1.txt")
        run(["bibtex","GY1973_test"],job,env,logs/"bibtex.txt")
        run(command,job,env,logs/"xelatex_pass2.txt")
        run(command,job,env,logs/"xelatex_pass3.txt")
        if "Label(s) may have changed" in (job/"GY1973_test.log").read_text():
            run(command,job,env,logs/"xelatex_pass4.txt")
        for suffix in ["pdf","aux","bbl","blg","log","out"]:
            path=job/f"GY1973_test.{suffix}"
            if path.exists():
                shutil.copy2(path,base/path.name)
    print("Built",base/"GY1973_test.pdf")

if __name__=="__main__":
    main()
