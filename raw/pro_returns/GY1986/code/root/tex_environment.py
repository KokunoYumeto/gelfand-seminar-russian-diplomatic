"""Use installed TeX files with a writable local format cache if needed.

The execution image supplies TeX binaries and package files but may omit its
generated ls-R databases and formats. This does not alter system directories
or download packages. A normal complete TeX installation is used unchanged.
"""
from pathlib import Path
import os, shutil, subprocess

def environment(out):
    env=os.environ.copy()
    available=subprocess.run(["kpsewhich","xelatex.fmt"],env=env,text=True,capture_output=True)
    if available.returncode==0 and available.stdout.strip():
        return env,["Used the installed XeLaTeX format and configuration."]
    out=Path(out)
    cache=out/".texmf_build"
    dist=Path("/usr/share/texlive/texmf-dist")
    if not dist.is_dir():
        raise RuntimeError("A complete XeLaTeX installation is required.")
    roots=[cache,dist,Path("/usr/share/texmf"),Path("/etc/texmf")]
    # Remove database-only !! restrictions by overriding the tree list, not
    # by modifying the system texmf.cnf or filesystem permissions.
    env["TEXMF"]="{"+",".join(str(p) for p in roots if p.is_dir() or p==cache)+"}"
    env["TEXMFVAR"]=str(cache)
    env["TEXMFCONFIG"]=str(cache)
    env["TEXMFCACHE"]=str(cache)
    env["TEXFORMATS"]=str(cache/"web2c")+"//:"
    config=cache/"tex"/"generic"/"config";config.mkdir(parents=True,exist_ok=True)
    shutil.copy2(dist/"tex"/"generic"/"config"/"language.us",config/"language.dat")
    # No Russian hyphenation package is installed in this image. The supplied
    # style imports Babel's Russian locale; allocate an unhyphenated language
    # explicitly so Cyrillic quotations have correct language metadata.
    with (config/"language.dat").open("a") as f:
        f.write("\nrussian zerohyph.tex\n")
    maps=cache/"fonts"/"map"/"pdftex"/"local";maps.mkdir(parents=True,exist_ok=True)
    maptext="\n".join(p.read_text() for p in sorted((dist/"fonts"/"map"/"dvips"/"amsfonts").glob("*.map")))
    (maps/"pdftex.map").write_text(maptext)
    (maps/"psfonts.map").write_text(maptext)
    fmt=cache/"web2c"/"xetex";fmt.mkdir(parents=True,exist_ok=True)
    if not (fmt/"xelatex.fmt").exists():
        result=subprocess.run(
            ["xetex","-ini","-etex","-jobname=xelatex","-interaction=nonstopmode","-halt-on-error","xelatex.ini"],
            cwd=fmt,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (out/"code"/"root"/"tex_format_generation.out").write_text(result.stdout)
        if result.returncode:
            raise RuntimeError("Local XeLaTeX format generation failed:\n"+result.stdout[-8000:])
    return env,[
        "Used installed package trees with a local XeLaTeX format; system directories were not changed.",
        "The local configuration removes database-only lookup restrictions because generated system databases are absent.",
        "Russian locale metadata is retained; Russian quotations use no hyphenation patterns in this image.",
        "Computer Modern/AMS Type 1 map entries are copied from the installed maps for mathematical fonts.",
    ]
