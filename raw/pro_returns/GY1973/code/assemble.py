#!/usr/bin/env python3
"""Assemble the separately audited source blocks without changing their order."""
from pathlib import Path
from collections import Counter
import argparse
import csv
import json
import re
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from bib_audit import entries,field

OWNERS=["agenda","manin_fuchs","autumn_representations","spring_integrable"]
ALIASES={"mishchenko1974infinite":"mishchenko1974signatures",
         "mccmeGelfandArchive":"mccme2026gelfand"}
PREFER={"quillen1973higher":"autumn_representations",
        "weibel2013kbook":"autumn_representations",
        "mishchenko1974signatures":"autumn_representations"}
AREAS={
 "Number theory":"Arithmetic and p-adic analysis",
 "Number theory and p-adic analysis":"Arithmetic and p-adic analysis",
 "p-adic analysis":"Arithmetic and p-adic analysis",
 "Arithmetic geometry":"Arithmetic and p-adic analysis",
 "Group theory and topology":"Group theory and arithmetic groups",
 "Algebraic K-theory":"Algebraic K-theory and categorical homotopy",
 "Algebraic K-theory and categorical topology":"Algebraic K-theory and categorical homotopy",
 "Operator algebras and index theory":"Operator theory and higher signatures",
 "Topology and index theory":"Operator theory and higher signatures",
 "Symplectic geometry and representation theory":"Representation theory, buildings and lattices",
 "Lattice and representation theory":"Representation theory, buildings and lattices",
 "Buildings and p-adic groups":"Representation theory, buildings and lattices",
 "Representation theory":"Representation theory, buildings and lattices",
 "Nonlinear PDE and dynamics":"Nonlinear waves and integrable systems",
 "Integrable systems and spectral theory":"Nonlinear waves and integrable systems",
 "Microlocal analysis":"Microlocal analysis and spectral geometry",
 "Spectral geometry":"Microlocal analysis and spectral geometry",
 "Unidentified":"Unidentified",
}

def aliases(s):
    for a,b in ALIASES.items():s=s.replace(a,b)
    return s

def load(path):
    return json.loads(aliases(path.read_text()))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--fragments",type=Path,default=HERE/"fragments")
    parser.add_argument("--output",type=Path,default=HERE.parent)
    args=parser.parse_args()
    args.output.mkdir(exist_ok=True,parents=True)
    joined={name:[] for name in ["talks","items","problems"]}
    corrections=[];areas={};bibs={};audit=[]
    for owner in OWNERS:
        folder=args.fragments/owner
        for name in joined:joined[name].extend(load(folder/(name+".json")))
        with (folder/"corrections.csv").open(newline="",encoding="utf-8") as f:
            corrections.extend({k:aliases(v or "") for k,v in r.items()} for r in csv.DictReader(f))
        for k,v in load(folder/"area_map.json").items():
            areas[k]=AREAS.get(v,v)
        for oldkey,e in entries((folder/"references.bib").read_text()):
            key=ALIASES.get(oldkey,oldkey);e=aliases(e)
            bibs.setdefault(key,[]).append((owner,e))
    all_records=[t["record"] for t in joined["talks"]]
    expected=set(range(302,334))
    if set(all_records)!=expected or len(all_records)!=32:
        raise ValueError(f"Expected all 32 source records302–333; got {all_records}")
    if all_records.index(307)>all_records.index(306):
        raise ValueError("P000512 source order lost:307 precedes306")
    if all_records.index(313)>all_records.index(312):
        raise ValueError("P000525 source order lost:313 precedes312")
    if all_records.index(321)>all_records.index(320):
        raise ValueError("P000532 source order lost:321 precedes320")
    unique=[]
    for key,versions in bibs.items():
        chosen=next((e for o,e in versions if o==PREFER.get(key)),versions[0][1])
        if len(versions)>1:
            for name in ["year","doi","pages"]:
                values={field(e,name).strip() for _,e in versions if field(e,name).strip()}
                if len(values)>1:
                    audit.append(f"CHECK {key} {name}: {values}")
            notes=[]
            for owner,e in versions:
                note=field(e,"annote")
                if note:notes.append(owner+": "+note)
            # Append a separate nonprinting verification field; no verified scope is lost.
            position=chosen.rfind("}")
            chosen=chosen[:position].rstrip().rstrip(",")+",\n verificationrecord = {"+ " | ".join(notes)+"}\n"+chosen[position:]
            audit.append(f"MERGED {key}: "+", ".join(o for o,_ in versions))
        unique.append((key,chosen))
    for name,data in joined.items():
        (args.output/f"GY1973_{name}.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
    with (args.output/"GY1973_corrections.csv").open("w",newline="",encoding="utf-8") as f:
        names=["page","place","transcription_reads","should_read","evidence","applies_to","type"]
        writer=csv.DictWriter(f,fieldnames=names);writer.writeheader();writer.writerows(corrections)
    (args.output/"GY1973_references.bib").write_text(
        "% Critical companion, cutoff 9 November 2026. Individual verification scopes are in annote.\n\n"+
        "\n".join(e for _,e in sorted(unique)))
    critical=(args.fragments/"manin_fuchs/critical_verifications.tex").read_text()
    marker="\\end{proof}\n"
    critical=critical.replace(marker,marker+"\n"+(HERE/"moment_check_note.tex").read_text(),1)
    development=((HERE/"critical_prelude.tex").read_text()+"\n"+critical+"\n"+
                 (args.fragments/"autumn_representations/development.tex").read_text())
    (args.output/"GY1973_development.tex").write_text(development)
    (args.output/"GY1973_area_map.json").write_text(json.dumps(areas,ensure_ascii=False,indent=2)+"\n")
    talk_by_id={t["record"]:t for t in joined["talks"]}
    items=joined["items"]
    stats={
        "talks":len(all_records),"catalogue_records_supplied":30,"source_recovered_records":[331,332],
        "talk_kind":dict(Counter(t.get("kind","talk") for t in joined["talks"])),
        "items":len(items),"problems":len(joined["problems"]),"references":len(unique),
        "corrections":len(corrections),"class":dict(sorted(Counter(x["class"] for x in items).items())),
        "speaker_by_talk":dict(sorted(Counter(talk_by_id[x["record"]]["speaker"] for x in items).items())),
        "speaker_by_attribution":dict(sorted(Counter(x.get("speaker") or talk_by_id[x["record"]]["speaker"] for x in items).items())),
        "area":dict(sorted(Counter(areas[x["id"]] for x in items).items())),
        "literal_correctness":dict(Counter(x["literal_correctness"] for x in items)),
        "publication_match":dict(Counter(x["publication_match"] for x in items)),
        "verification":dict(Counter(x["verification"] for x in items)),
        "development":dict(Counter(x["development"] for x in items)),
        "correction_type":dict(Counter(x["type"] for x in corrections)),
        "source_order":all_records,
    }
    (args.output/"GY1973_statistics.json").write_text(json.dumps(stats,ensure_ascii=False,indent=2)+"\n")
    logs=args.output/"logs";logs.mkdir(exist_ok=True)
    (logs/"assembly.txt").write_text("\n".join(audit)+"\n"+json.dumps(stats,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:stats[k] for k in ["talks","items","problems","references","corrections","class"]},ensure_ascii=False))
    if any(line.startswith("CHECK") for line in audit):
        raise SystemExit("Resolve bibliography metadata discrepancy in logs/assembly.txt.")

if __name__=="__main__":main()
