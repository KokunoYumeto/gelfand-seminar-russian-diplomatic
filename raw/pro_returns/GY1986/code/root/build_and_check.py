"""Build the chapter with the supplied pipeline and record objective checks."""
from pathlib import Path
from collections import Counter
import csv, hashlib, importlib, json, platform, re, subprocess, sys
from tex_environment import environment

OUT=Path(__file__).resolve().parents[2]
CODE=OUT/"code"/"root"
TAG="GY1986"
TEX_ENV=None

def run(name,args):
    result=subprocess.run(args,cwd=OUT,env=TEX_ENV,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (CODE/name).write_text(result.stdout)
    print(name,"exit",result.returncode)
    if result.returncode:
        print(result.stdout[-9000:])
        raise SystemExit(result.returncode)
    return result.stdout

def main():
    global TEX_ENV
    TEX_ENV,environment_notes=environment(OUT)
    run("build_chapter.out",[sys.executable,"build_chapter.py",TAG])
    run("xelatex_pass1.out",["xelatex","-interaction=nonstopmode","-halt-on-error",TAG+"_test.tex"])
    run("bibtex.out",["bibtex",TAG+"_test"])
    run("xelatex_pass2.out",["xelatex","-interaction=nonstopmode","-halt-on-error",TAG+"_test.tex"])
    run("xelatex_pass3.out",["xelatex","-interaction=nonstopmode","-halt-on-error",TAG+"_test.tex"])
    log=(OUT/(TAG+"_test.log")).read_text()
    for passno in range(4,7):
        if not re.search(r"Rerun to get|Label\(s\) may have changed",log):
            break
        run(f"xelatex_pass{passno}.out",["xelatex","-interaction=nonstopmode","-halt-on-error",TAG+"_test.tex"])
        log=(OUT/(TAG+"_test.log")).read_text()
    issues={}
    patterns={
        "latex_errors":r"(?m)^!.*$",
        "missing_characters":r"(?m)^Missing character:.*$",
        "undefined_references":r"(?m)^.*(?:Citation|Reference).*undefined.*$",
        "rerun_requests":r"(?m)^.*(?:Rerun to get|Label\(s\) may have changed|There were undefined).*?$",
        "overfull_boxes":r"(?m)^Overfull.*$",
    }
    for k,p in patterns.items():issues[k]=re.findall(p,log)
    for name in ["latex_errors","missing_characters","undefined_references","rerun_requests"]:
        if issues[name]:print(name,issues[name])
    info=run("pdfinfo.out",["pdfinfo",TAG+"_test.pdf"])
    run("pdftotext.out",["pdftotext","-layout",TAG+"_test.pdf",str(CODE/"pdf_text.txt")])
    pages=int(re.search(r"(?m)^Pages:\s+(\d+)",info)[1])
    talks=json.loads((OUT/(TAG+"_talks.json")).read_text())
    items=json.loads((OUT/(TAG+"_items.json")).read_text())
    problems=json.loads((OUT/(TAG+"_problems.json")).read_text())
    counts=json.loads((CODE/"assembly_counts.json").read_text())
    required=[TAG+"_"+x for x in [
        "talks.json","items.json","problems.json","overview.tex","development.tex",
        "corrections.csv","references.bib","report.md","chapter.tex","test.tex","test.pdf"
    ]]
    assert sorted(t["record"] for t in talks)==list(range(667,713))
    assert len({x["id"] for x in items})==len(items)
    assert dict(Counter(x["class"] for x in items))==counts["classes"]
    assert all((OUT/n).is_file() and (OUT/n).stat().st_size>0 for n in required)
    pmap={p["id"]:set(p["occurrences"]) for p in problems}
    for x in items:
        if x.get("problem"):
            assert x["id"] in pmap[x["problem"]], x["id"]
    for id_ in ["1986-688.5","1986-695.11","1986-698.1"]:
        assert id_ in pmap["GP-1986-60"], id_
    hashes={n:hashlib.sha256((OUT/n).read_bytes()).hexdigest() for n in required}
    versions={"python":platform.python_version()}
    for module in ["sympy","mpmath"]:
        versions[module]=importlib.import_module(module).__version__
    text=(CODE/"pdf_text.txt").read_text()
    text_pages=text.split("\f")
    firsttalk=[i+1 for i,p in enumerate(text_pages) if "record 667;" in p]
    computed={}
    for name in ["quantum_kdv","unitary_integral","stationary_formula","complex_structures","cube_regions","slab"]:
        path=CODE/("check_"+name+".out")
        assert path.exists() and path.stat().st_size>0
        computed[name]={"program":"code/root/check_"+name+".py",
                        "output":str(path.relative_to(OUT)),
                        "sha256":hashlib.sha256(path.read_bytes()).hexdigest()}
    valid={
        "checked_on":"2026-11-12",
        "status":"compiled; automated checks complete; visual inspection recorded separately",
        "records":len(talks),"items":len(items),"problems":len(problems),
        "classes":counts["classes"],"pdf_pages":pages,
        "first_talk_pdf_pages":firsttalk,
        "overview_constraint":"Overview is the material before record 667; inspect its two-page limit in the rendered PDF.",
        "latex_log_findings":issues,
        "runtime_versions":versions,
        "tex_environment_notes":environment_notes,
        "required_file_sha256":hashes,
        "mathematical_outputs":computed,
        "notes":[
            "All mathematical computation outputs were independently checked as recorded in proof_review.md.",
            "The build uses the provided chapter builder, XeLaTeX, BibTeX, and two further XeLaTeX passes.",
            "Archive integrity is checked after packaging; it is recorded outside the ZIP to avoid self-reference.",
        ],
    }
    (CODE/"final_validation.json").write_text(json.dumps(valid,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:valid[k] for k in ["records","items","problems","pdf_pages","first_talk_pdf_pages","latex_log_findings"]},ensure_ascii=False,indent=2))
    if any(issues[k] for k in ["latex_errors","missing_characters","undefined_references","rerun_requests"]):
        raise SystemExit("Resolve the reported LaTeX issues before delivery.")

if __name__=="__main__":
    main()
