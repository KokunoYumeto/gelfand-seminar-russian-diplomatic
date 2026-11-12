import json,pathlib,subprocess,sys
root=pathlib.Path(__file__).parent
stage=sys.argv[1] if len(sys.argv)>1 else "1"
cmd=["bibtex","GY1983_test"] if stage=="bib" else ["xelatex","-interaction=nonstopmode","-halt-on-error","GY1983_test.tex"]
r=subprocess.run(cmd,cwd=root,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
log=root/("build_"+stage+".log")
log.write_text(r.stdout,encoding="utf-8")
errors=[s for s in r.stdout.splitlines() if "!" in s or "Warning" in s or "Missing character" in s or "Overfull" in s or "Underfull" in s]
print(json.dumps({"stage":stage,"returncode":r.returncode,"tail":r.stdout[-2500:],"warnings":errors[-30:]}))
sys.exit(r.returncode)
