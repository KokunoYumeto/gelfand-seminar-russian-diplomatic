"""Render the overview and report using final audited counts."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
OUT=ROOT/"GY1974"
C=json.loads((OUT/"audit_counts.json").read_text())
def table(mapping,h1,h2="Items"):
    return f"| {h1} | {h2} |\n|---|---:|\n"+"\n".join(f"| {k} | {v} |" for k,v in mapping.items())
vals={"N":C["items"],"P":C["problems"],"R":C["references"],
      "K":C["corrections"],"U":C["items"]-5,**C["classes"]}
vals.update(CLASS_TABLE=table(C["classes"],"Class"),
 SPEAKER_TABLE=table(C["by_record_speaker"],"Record speaker"),
 AREA_TABLE=table(C["by_area"],"Primary area"),
 CORRECTNESS_TABLE=table(C["literal_correctness"],"Literal correctness"),
 MATCH_TABLE=table(C["publication_match"],"Publication match"),
 VERIFICATION_TABLE=table(C["verification"],"Verification level"),
 CORRECTION_TABLE=table(C["correction_types"],"Correction type","Rows"))
boundary=json.loads((ROOT/"parts"/"early_boundary.json").read_text())
vals["BOUNDARY_TABLE"]="| Earlier item | Source page | Audited content | Class |\n|---|---|---|:---:|\n"+"\n".join(
    f'| {x["prior_id"]} | {x["page"]} | {x["title"]} | {x["classification"]} |' for x in boundary)
refs=ROOT/"report_references.md"
vals["REPORT_REFERENCES"]=refs.read_text() if refs.exists() else ""
validation=ROOT/"validation_report.md"
vals["FINAL_VALIDATION"]=validation.read_text() if validation.exists() else "Final compilation is in progress; this paragraph is replaced by the verified build record before delivery."
for src,dest in (("overview_template.tex","GY1974_overview.tex"),("report_template.md","GY1974_report.md")):
    s=(ROOT/src).read_text()
    for k,v in vals.items():s=s.replace(f"__{k}__",str(v))
    (OUT/dest).write_text(s)
print("Overview and report rendered from audit_counts.json.")
