#!/usr/bin/env python3
"""Validate the assembled data, built TeX/PDF and recorded final build logs.

Run from any directory after compiling the top-level chapter. This structural
audit supplements, and does not replace, the independent mathematical reviews.
"""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import json
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
TAG="GY1974"
errors=[]
def require(condition,message):
    if not condition: errors.append(message)
def read_json(suffix):
    return json.loads((ROOT/f"{TAG}_{suffix}.json").read_text())

talks=read_json("talks")
items=read_json("items")
problems=read_json("problems")
counts=json.loads((ROOT/"audit_counts.json").read_text())
expected_records=[331,332,*range(334,362)]
require([t["record"] for t in talks]==expected_records,"record coverage/order")
ids=[x["id"] for x in items]
require(len(ids)==len(set(ids)),"duplicate item identifier")
for record in expected_records:
    actual=[x["id"] for x in items if x["record"]==record]
    require(actual==[f"1974-{record}.{i+1}" for i in range(len(actual))],
            f"nonconsecutive items for {record}")
classes=dict(Counter(x["class"] for x in items))
require(len(items)==counts["items"] and len(talks)==counts["records"],
        "count report disagrees with data")
require(not counts["schema_errors"],"assembler reports schema errors")
require(all(classes.get(k,0)==counts["classes"][k] for k in "ABCDEF"),
        "class counts disagree")

prior=(ROOT/"code/generation/previous_index.md").read_text()
imap={x["id"]:x for x in items}
pmap={p["id"]:p for p in problems}
require(len(pmap)==len(problems),"duplicate problem identifier")
for p in problems:
    require(p["status_date"]=="2026-11",f"{p['id']}: status date")
    for ident in p["occurrences"]:
        if ident.startswith("1974-"):
            require(ident in imap and imap[ident]["problem"]==p["id"],
                    f"{p['id']}: missing reciprocal occurrence {ident}")
        else:
            require(ident in prior,f"{p['id']}: earlier item absent from supplied index")
for x in items:
    if x["problem"]:
        require(x["problem"] in pmap and x["id"] in pmap[x["problem"]]["occurrences"],
                f"{x['id']}: problem does not list occurrence")

bib=(ROOT/f"{TAG}_references.bib").read_text()
keys=re.findall(r"(?m)^@\w+\s*\{\s*([^,\s]+)\s*,",bib)
require(len(keys)==len(set(keys))==counts["references"],"bibliography key counts")
chapter=(ROOT/f"{TAG}_chapter.tex").read_text()
require(re.findall(r"\\begin\{GSitem\}\{([^}]+)\}",chapter)==ids,
        "rendered item coverage/order")
cited={k.strip() for group in re.findall(
    r"\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]+)\}",chapter)
    for k in group.split(",")}
require(cited<=set(keys),"rendered citation missing bibliography key")
with (ROOT/f"{TAG}_corrections.csv").open(newline="") as f:
    reader=csv.DictReader(f)
    require(reader.fieldnames==["page","place","transcription_reads","should_read",
                               "evidence","applies_to","type"],"CSV header")
    corrections=list(reader)
require(len(corrections)==counts["corrections"],"correction count")
require(all(x["applies_to"] in {"ru","en","both"} for x in corrections),
        "invalid correction language")
require(all(x["type"] in {"transcription","translation","ambiguity",
                         "faithful_error","provenance",""} for x in corrections),
        "invalid correction type")

log=(ROOT/f"{TAG}_test.log").read_text(errors="replace")
biblog=(ROOT/f"{TAG}_test.blg").read_text(errors="replace")
failure_patterns={
 "fatal TeX error":r"(?m)^!|Emergency stop|Fatal error|LaTeX Error|Undefined control sequence",
 "missing math delimiter":r"Missing \$ inserted",
 "unresolved citation/reference":r"undefined citations|undefined references|undefined on input line",
 "missing glyph":r"Missing character:",
 "font warning":r"LaTeX Font Warning|Package fontspec Warning",
 "rerun warning":r"Rerun to get|Label\(s\) may have changed",
}
log_checks={k:not bool(re.search(v,log,re.I)) for k,v in failure_patterns.items()}
for name,passed in log_checks.items():require(passed,name)
overfull=[{"points":float(m.group(1)),"context":m.group(0)}
          for m in re.finditer(r"Overfull \\[hv]box \(([\d.]+)pt too (?:wide|high)\)[^\n]*",log)]
require(not overfull,"overfull boxes remain")
require(not re.search(r"Warning--|error message|I couldn't|I found no",biblog,re.I),
        "BibTeX warning/error")

pdf=ROOT/f"{TAG}_test.pdf"
pdftext=subprocess.run(["pdftotext","-layout",str(pdf),"-"],
                        check=True,capture_output=True,text=True).stdout
text_pages=pdftext.split("\f")
if not text_pages[-1].strip():text_pages.pop()
pages=len(text_pages)
page_match=re.search(r"Output written on .*?\.pdf \((\d+) pages",log)
require(bool(page_match) and int(page_match.group(1))==pages,
        "PDF text page count differs from the final TeX log")
require(all(ident in pdftext for ident in ids),"PDF text lacks an item ID")
require("Bibliography" in pdftext,"PDF has no bibliography")
require("No class C or D item" in pdftext,"verification-scope statement absent")
require("Final compilation is in progress" not in (ROOT/f"{TAG}_report.md").read_text(),
        "report validation placeholder remains")
require(not re.search(r"__[A-Z_]+__",(ROOT/f"{TAG}_report.md").read_text()),
        "report template placeholder remains")

required=[f"{TAG}_{x}" for x in ("talks.json","items.json","problems.json",
 "overview.tex","development.tex","corrections.csv","references.bib","report.md",
 "chapter.tex","test.pdf")]
for name in required:require((ROOT/name).is_file() and (ROOT/name).stat().st_size>0,
                             f"missing or empty deliverable {name}")
hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
        for name in required if (ROOT/name).is_file()}
result={
 "checked_at_utc":datetime.now(timezone.utc).isoformat(),
 "status_date":"2026-11","records":len(talks),"items":len(items),
 "exact_source_aliases":5,"items_after_removing_exact_aliases":len(items)-5,
 "prior_boundary_rows":26,"classes":counts["classes"],
 "problems":len(problems),"references":len(keys),"corrections":len(corrections),
 "rendered_citation_keys":len(cited),"pdf_pages":pages,
 "log_checks":log_checks,"overfull_boxes":overfull,
 "bibtex_warnings_or_errors":False if not re.search(r"Warning--|error message|I couldn't|I found no",biblog,re.I) else True,
 "required_artifact_sha256":hashes,
 "errors":errors,
 "scope":"Structural and build validation; mathematical and historical verification is recorded separately in the audits and research logs."
}
(ROOT/"validation.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(result,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
