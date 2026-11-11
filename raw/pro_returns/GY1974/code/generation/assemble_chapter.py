"""Assemble the independently researched record groups and audit their schema.

Run from any directory. Editorial input parts are preserved alongside this
script in the deliverable's code/generation directory for reproducibility.
The supplied build_chapter.py remains the authoritative renderer.
"""
from collections import Counter, defaultdict
import csv
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parent
PARTS=ROOT/"parts"
OUT=ROOT/"GY1974"
OUT.mkdir(exist_ok=True)
GROUPS=("early","middle","extra","late")
ORDER=[331,332,*range(334,362)]
assert len(ORDER)==30

def read_json(name):
    return json.loads((PARTS/name).read_text())

talks=sum((read_json(f"{g}_talks.json") for g in GROUPS),[])
items=sum((read_json(f"{g}_items.json") for g in GROUPS),[])
problems=sum((read_json(f"{g}_problems.json") for g in GROUPS),[])
assert len(talks)==30, f"Need all 30 records, got {len(talks)}"
assert {t["record"] for t in talks}==set(ORDER)
assert len({t["record"] for t in talks})==30
talks.sort(key=lambda t:ORDER.index(t["record"]))
items.sort(key=lambda x:(ORDER.index(x["record"]),int(x["id"].split(".")[-1])))
problems.sort(key=lambda x:x["id"])

# Explicit, reviewable layout changes: line breaks and mathematical typesetting.
# No equation is inferred or altered by a generic string normalization.
layout_file=ROOT/"layout_edits.json"
if layout_file.exists():
    for edit in json.loads(layout_file.read_text()):
        if edit["collection"]=="corrections":continue
        collection={"items":items,"talks":talks,"problems":problems}[edit["collection"]]
        ident="record" if edit["collection"]=="talks" else "id"
        target=next(x for x in collection if x[ident]==edit["id"])
        old=target[edit["field"]]
        assert edit["old"] in old, f"Stale layout edit: {edit['id']} {edit['field']}"
        target[edit["field"]]=old.replace(edit["old"],edit["new"])

# Cross-group occurrence links are reconciled once all local files exist.
for p in problems:
    if p["id"]=="GP-1974-10":
        for ident in ("1974-340.7","1974-343.2"):
            if ident not in p["occurrences"]:p["occurrences"].append(ident)
        p["occurrences"].sort(key=lambda s:tuple(map(int,re.split(r"[-.]",s))))
for x in items:
    if x["id"]=="1974-340.7":x["problem"]="GP-1974-10"

# Preserve sources' verification notes while eliminating duplicate BibTeX keys.
# Entries are delimited at start-of-line @type, never by internal TeX braces.
entries={}
duplicate_keys=[]
verification_records=defaultdict(list)
bib_sources=["root_source_catalogue.bib","root_references.bib","extra_references.bib",
             "early_references.bib","middle_references.bib","late_references.bib"]
for fname in bib_sources:
    text=(PARTS/fname).read_text()
    starts=list(re.finditer(r"(?m)^@\w+\s*\{\s*([^,\s]+)\s*,",text))
    for i,m in enumerate(starts):
        entry=text[m.start():starts[i+1].start() if i+1<len(starts) else len(text)].strip()
        key=m.group(1)
        verification_records[key].append({"source":fname,"entry":entry})
        if key in entries:
            duplicate_keys.append((key,fname))
        else: entries[key]=entry
bib="\n\n".join(entries[k] for k in sorted(entries))+"\n"

header=["page","place","transcription_reads","should_read","evidence","applies_to","type"]
corrections=[]
for g in GROUPS:
    with (PARTS/f"{g}_corrections.csv").open(newline="") as f:
        corrections.extend(csv.DictReader(f))
corrections.sort(key=lambda r:int(re.search(r"\d+",r["page"]).group()))
if layout_file.exists():
    for edit in json.loads(layout_file.read_text()):
        if edit["collection"]!="corrections":continue
        matches=[x for x in corrections if x["page"]==edit["page"] and x["place"]==edit["id"]]
        assert len(matches)==1,f"Ambiguous correction layout edit: {edit['id']}"
        target=matches[0]
        assert edit["old"] in target[edit["field"]],f"Stale correction layout edit: {edit['id']}"
        target[edit["field"]]=target[edit["field"]].replace(edit["old"],edit["new"])

for name,data in (("talks",talks),("items",items),("problems",problems)):
    (OUT/f"GY1974_{name}.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
(OUT/"GY1974_references.bib").write_text(bib)
(OUT/"bibliography_verification.json").write_text(json.dumps(verification_records,ensure_ascii=False,indent=2)+"\n")
with (OUT/"GY1974_corrections.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=header);w.writeheader();w.writerows(corrections)

errors=[]
enum={
 "kind":{"definition","construction","theorem","claim","conjecture","question","problem","method","remark"},
 "class":set("ABCDEF"),
 "literal_correctness":{"correct","correct with missing hypotheses","false as written","not determinable"},
 "publication_match":{"exact","partial","thematic only","none found"},
 "verification":{"read the result","publisher metadata checked","indirect","unresolved lead"},
 "development":{"none","annotated","developed in this chapter"},
 "confidence":{"high","medium","low"},
}
cite_re=re.compile(r"\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}")
ids={x["id"] for x in items}
pids={p["id"] for p in problems}
for x in items:
    for k,allowed in enum.items():
        if x.get(k) not in allowed:errors.append(f'{x["id"]}: invalid {k}={x.get(k)!r}')
    for k in ("reconstruction","problem","worth"):
        if k not in x: errors.append(f'{x["id"]}: missing {k}')
    for k,s in x.items():
        if isinstance(s,str):
            bad=[ord(c) for c in s if ord(c)<32 and c!="\n"]
            if bad:errors.append(f'{x["id"]} {k}: control characters {bad}')
            cited={q.strip() for group in cite_re.findall(s) for q in group.split(",")}
            if cited-set(x["refs"]):errors.append(f'{x["id"]} {k}: cited keys absent from refs {cited-set(x["refs"])}')
    if x["problem"] and x["problem"] not in pids:errors.append(f'{x["id"]}: unresolved problem id')
    if x["class"] in "CD" and not x["worth"]:errors.append(f'{x["id"]}: no worth-development assessment')
for p in problems:
    if p["status_date"]!="2026-11":errors.append(f'{p["id"]}: status date')
    for ident in p["occurrences"]:
        if ident.startswith("1974-") and ident not in ids:errors.append(f'{p["id"]}: missing {ident}')
        if ident.startswith("1974-") and next(x for x in items if x["id"]==ident)["problem"]!=p["id"]:
            errors.append(f'{p["id"]}: occurrence {ident} lacks reciprocal problem link')
for key,entry in entries.items():
    if not re.search(r"\b(url|doi)\s*=",entry,re.I):errors.append(f'{key}: missing URL/DOI')
    if not re.search(r"\bnote\s*=\s*\{\s*(unverified|verified)\s*\}",entry,re.I):
        errors.append(f'{key}: missing verification note')

areas={
331:"Representations and current groups",332:"Integrable systems and spectral theory",
335:"Elliptic PDE and variational problems",336:"Integrable systems and spectral theory",
337:"Topology, configurations and buildings",338:"Elliptic PDE and variational problems",
339:"Integrable systems and spectral theory",340:"Integrable systems and spectral theory",
341:"Elliptic PDE and variational problems",342:"Characteristic classes and complex geometry",
343:"Integrable systems and spectral theory",344:"Topology, configurations and buildings",
345:"Gauge field theory",346:"Newton polyhedra and singularities",
347:"Newton polyhedra and singularities",348:"Topology, configurations and buildings",
349:"Newton polyhedra and singularities",350:"Gauge field theory",
351:"Representations and current groups",353:"Microlocal analysis and differential operators",
354:"Statistical mechanics and random fields",355:"Statistical mechanics and random fields",
356:"Microlocal analysis and differential operators",357:"Microlocal analysis and differential operators",
358:"Statistical mechanics and random fields",359:"Gauge field theory",
360:"Characteristic classes and complex geometry",361:"Characteristic classes and complex geometry",
}
recmap={t["record"]:t for t in talks}
owners={
331:"A. A. Kirillov",332:"B. M. Gurevich",335:"Enrico Giusti",
336:"S. P. Novikov",337:"Czesław Bessaga",338:"Enrico Giusti",
339:"B. A. Dubrovin",340:"B. A. Dubrovin",341:"Enrico Giusti",
342:"I. M. Gelfand",343:"I. M. Gelfand",344:"Graeme Segal",
345:"A. M. Polyakov",346:"A. G. Kushnirenko",347:"V. I. Arnold",
348:"Graeme Segal",349:"A. G. Kushnirenko",350:"A. M. Polyakov",
351:"M. I. Graev",353:"V. N. Tulovskii",354:"Ya. G. Sinai",
355:"Ya. G. Sinai",356:"V. N. Tulovskii",357:"V. N. Tulovskii",
358:"R. L. Dobrushin",359:"A. M. Polyakov",360:"James King",361:"James King",
}
counts={
 "records":len(talks),"items":len(items),"problems":len(problems),
 "references":len(entries),"corrections":len(corrections),
 "classes":{k:sum(x["class"]==k for x in items) for k in "ABCDEF"},
 "by_record":{str(r):sum(x["record"]==r for x in items) for r in ORDER},
 "by_record_speaker":dict(sorted(Counter(owners[x["record"]] for x in items).items())),
 "by_attributed_speaker":dict(sorted(Counter(x.get("speaker") or owners[x["record"]] for x in items).items())),
 "by_area":dict(sorted(Counter(areas[x["record"]] for x in items).items())),
 "literal_correctness":dict(Counter(x["literal_correctness"] for x in items)),
 "publication_match":dict(Counter(x["publication_match"] for x in items)),
 "verification":dict(Counter(x["verification"] for x in items)),
 "correction_types":dict(Counter(r["type"] for r in corrections)),
 "talk_kinds":dict(Counter(t["kind"] for t in talks)),
 "duplicates_removed":duplicate_keys,
 "schema_errors":errors,
}
(OUT/"audit_counts.json").write_text(json.dumps(counts,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(counts,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
