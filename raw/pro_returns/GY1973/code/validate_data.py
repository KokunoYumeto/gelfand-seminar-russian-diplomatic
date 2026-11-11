#!/usr/bin/env python3
"""Additional semantic/schema checks beyond the unchanged supplied builder."""
from pathlib import Path
from collections import Counter
import argparse
import csv
import json
import re
import sys
from bib_audit import entries,field

CITE=re.compile(r"\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}")
REQUIRED={
 "id","record","pages","kind","title","notes","statement","reconstruction",
 "class","fate","present_status","literal_correctness","publication_match",
 "verification","development","problem","worth","refs","confidence"}
ENUMS={
 "kind":{"definition","construction","theorem","claim","conjecture","question","problem","method","remark"},
 "class":set("ABCDEF"),
 "literal_correctness":{"correct","correct with missing hypotheses","false as written","not determinable"},
 "publication_match":{"exact","partial","thematic only","none found"},
 "verification":{"read the result","publisher metadata checked","indirect","unresolved lead"},
 "development":{"none","annotated","developed in this chapter"},
 "confidence":{"high","medium","low"}}

def citations(obj):
    if isinstance(obj,dict):s=" ".join(v for v in obj.values() if isinstance(v,str))
    else:s=str(obj)
    return {k.strip() for group in CITE.findall(s) for k in group.split(",") if k.strip()}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--directory",type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument("--fragments",type=Path)
    parser.add_argument("--previous",type=Path)
    args=parser.parse_args()
    issues=[];notes=[]
    if args.fragments:
        folders=[args.fragments/x for x in ["agenda","manin_fuchs","autumn_representations","spring_integrable"]]
        talks=[];items=[];problems=[];bib=""
        for d in folders:
            talks+=json.loads((d/"talks.json").read_text())
            items+=json.loads((d/"items.json").read_text())
            problems+=json.loads((d/"problems.json").read_text())
            bib+=(d/"references.bib").read_text()+"\n"
    else:
        def load(n):return json.loads((args.directory/f"GY1973_{n}.json").read_text())
        talks,items,problems=load("talks"),load("items"),load("problems")
        bib=(args.directory/"GY1973_references.bib").read_text()
    keys={k for k,_ in entries(bib)}
    recs={t["record"]:t for t in talks}
    ids={x["id"] for x in items}
    probs={p["id"]:p for p in problems}
    if len(ids)!=len(items):issues.append("Duplicate item identifiers")
    if len(recs)!=len(talks):issues.append("Duplicate record identifiers")
    if len(probs)!=len(problems):issues.append("Duplicate problem identifiers")
    for x in items:
        label=x.get("id","?")
        for name in REQUIRED-set(x):issues.append(f"{label}: missing {name}")
        for name,values in ENUMS.items():
            if x.get(name) not in values:issues.append(f"{label}: bad {name}={x.get(name)}")
        if not re.fullmatch(r"1973-\d+\.\d+",label):issues.append(f"{label}: wrong academic-year prefix")
        if int(label.split("-")[1].split(".")[0])!=x["record"]:issues.append(f"{label}: wrong record")
        if x["record"] not in recs:issues.append(f"{label}: missing talk")
        if not re.search(r"2026",x.get("present_status","")):issues.append(f"{label}: status not dated")
        if x["class"] in "CD" and not x.get("worth"):issues.append(f"{label}: no development assessment")
        used=citations(x)
        if used-set(x["refs"]):issues.append(f"{label}: cited keys absent from refs {used-set(x['refs'])}")
        if set(x["refs"])-keys:issues.append(f"{label}: missing bibliography {set(x['refs'])-keys}")
        if x.get("problem"):
            if x["problem"] not in probs:issues.append(f"{label}: missing problem")
            elif label not in probs[x["problem"]]["occurrences"]:issues.append(f"{label}: problem lacks reciprocal occurrence")
        for p in re.findall(r"P(\d{6})",x["pages"]):
            if not 501<=int(p)<=553:issues.append(f"{label}: source page outside supplied corpus")
        for name in ["notes","statement","reconstruction","fate","present_status","worth"]:
            s=x.get(name,"")
            if s.count(r"\(")!=s.count(r"\)"):issues.append(f"{label}/{name}: inline math mismatch")
            if s.count(r"\[")!=s.count(r"\]"):issues.append(f"{label}/{name}: display math mismatch")
    for r in recs:
        own=[x["id"] for x in items if x["record"]==r]
        expected=[f"1973-{r}.{i}" for i in range(1,len(own)+1)]
        if own!=expected:issues.append(f"Record{r}: numbering/order mismatch")
        if not own and recs[r].get("kind") not in {"heading","plan","other"}:
            issues.append(f"Record{r}: talk has no items")
    previous=args.previous.read_text() if args.previous else ""
    for p in problems:
        if p["status_date"]!="2026-11":issues.append(f"{p['id']}: wrong cutoff")
        if citations(p)-set(p["refs"]):issues.append(f"{p['id']}: cited keys absent from refs")
        if set(p["refs"])-keys:issues.append(f"{p['id']}: missing bibliography")
        for o in p["occurrences"]:
            if o.startswith("1973-"):
                if o not in ids:issues.append(f"{p['id']}: missing current occurrence{o}")
            elif previous and o not in previous:issues.append(f"{p['id']}: earlier occurrence{o} absent from supplied index")
        if previous and not p["id"].startswith("GP-1973-") and p["id"] not in previous:
            issues.append(f"{p['id']}: reused identifier not in earlier index")
    for k,e in entries(bib):
        if not field(e,"url") and not field(e,"doi"):issues.append(f"Bibliography{k}: no URL/DOI")
        if field(e,"note").strip() not in {"verified","unverified"}:issues.append(f"Bibliography{k}: bad verification flag")
    present=set()
    for x in items:
        nums=list(map(int,re.findall(r"P(\d{6})",x["pages"])))
        if nums:present.update(range(min(nums),max(nums)+1))
    missingpages=sorted(set(range(501,554))-present)
    notes.append(f"Source pages with no mathematical item: {missingpages}; check headings/boundaries.")
    notes.append(f"Records present: {sorted(recs)}")
    notes.append(f"Counts: {len(talks)} records; {len(items)} items; {len(problems)} problems; {len(keys)} bibliography keys")
    notes.append("Classes: "+str(dict(Counter(x["class"] for x in items))))
    print("\n".join(notes))
    for issue in issues:print("ERROR:",issue)
    print("Semantic audit:",len(issues),"errors")
    raise SystemExit(bool(issues))

if __name__=="__main__":main()
