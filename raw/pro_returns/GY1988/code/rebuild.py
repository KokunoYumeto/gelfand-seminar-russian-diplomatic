"""Rebuild with the original unchanged kit.

Run from the directory containing GY1988_*:
    python code/rebuild.py --kit 'GY1988_kit(1).zip'

Requires the kit's dependencies/fonts, XeLaTeX and BibTeX.
This recovery script was not executed during the outage.
"""
import argparse
import collections
import json
from pathlib import Path
import re
import subprocess
import sys
import zipfile

TAG = "GY1988"
root = Path.cwd()

parser = argparse.ArgumentParser()
parser.add_argument("--kit", type=Path, required=True)
args = parser.parse_args()

core = [
    f"{TAG}_{suffix}" for suffix in (
        "talks.json", "items.json", "problems.json",
        "corrections.csv", "references.bib",
        "overview.tex", "development.tex", "report.md"
    )
]
for name in core:
    if not (root/name).is_file():
        raise SystemExit("Missing reconstructed file: "+name)

talks = json.loads((root/f"{TAG}_talks.json").read_text(encoding="utf-8"))
items = json.loads((root/f"{TAG}_items.json").read_text(encoding="utf-8"))
problems = json.loads((root/f"{TAG}_problems.json").read_text(encoding="utf-8"))

required = {
    "id","record","pages","kind","title","notes","statement",
    "reconstruction","class","fate","present_status",
    "literal_correctness","publication_match","verification",
    "development","problem","worth","refs","confidence"
}
assert len(talks)==22 and len(items)==160 and len(problems)==7
assert len({t["record"] for t in talks})==22
by_id = {x["id"]:x for x in items}
assert len(by_id)==160
assert all(required <= x.keys() for x in items)
assert all(x["record"] in {t["record"] for t in talks} for x in items)
assert collections.Counter(x["class"] for x in items)=={
    "A":33,"B":3,"C":1,"E":107,"F":16
}

bib = (root/f"{TAG}_references.bib").read_text(encoding="utf-8")
keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,",bib)
assert len(keys)==len(set(keys)), "Duplicate bibliography key"
assert len(keys)==71
assert all(k in keys for x in items for k in x["refs"])
assert all(k in keys for p in problems for k in p["refs"])

by_problem = {p["id"]:p for p in problems}
assert len(by_problem)==7
for p in problems:
    assert p["status_date"]=="2026-11"
    assert len(p["occurrences"])==len(set(p["occurrences"]))
    for identifier in p["occurrences"]:
        assert by_id[identifier]["problem"]==p["id"]
for item in items:
    if item["problem"]:
        assert item["id"] in by_problem[item["problem"]]["occurrences"]

# Copy exact original bytes, without altering the fixed files.
with zipfile.ZipFile(args.kit) as source:
    for name in ("build_chapter.py","gelfand_companion.sty"):
        candidates = [
            p for p in source.namelist()
            if p.rstrip("/").split("/")[-1]==name
        ]
        assert len(candidates)==1, (name,candidates)
        data = source.read(candidates[0])
        target = root/name
        target.write_bytes(data)
        assert target.read_bytes()==data

subprocess.run(
    [sys.executable,"build_chapter.py",TAG],
    check=True,cwd=root
)
commands = [
    ["xelatex","-interaction=nonstopmode","-halt-on-error",TAG+"_test.tex"],
    ["bibtex",TAG+"_test"],
    ["xelatex","-interaction=nonstopmode","-halt-on-error",TAG+"_test.tex"],
    ["xelatex","-interaction=nonstopmode","-halt-on-error",TAG+"_test.tex"]
]
for command in commands:
    subprocess.run(command,check=True,cwd=root)

log = (root/(TAG+"_test.log")).read_text(
    encoding="utf-8",errors="replace"
)
for failure in (
    "Undefined control sequence",
    "Missing character:",
    "There were undefined references",
    "There were undefined citations"
):
    assert failure not in log, failure
assert (root/(TAG+"_test.pdf")).stat().st_size>0

# Visual page inspection remains a separate editorial step.
deliverables = [root/name for name in core]
deliverables += [
    root/(TAG+"_chapter.tex"), root/(TAG+"_test.tex"),
    root/(TAG+"_test.pdf"), root/"build_chapter.py",
    root/"gelfand_companion.sty"
]
for directory in ("code","evidence"):
    if (root/directory).exists():
        deliverables += [
            p for p in (root/directory).rglob("*") if p.is_file()
        ]

with zipfile.ZipFile(
    root/(TAG+".zip"),"w",zipfile.ZIP_DEFLATED
) as archive:
    for p in sorted(set(deliverables)):
        archive.write(p,p.relative_to(root))

print("Created",TAG+".zip")
