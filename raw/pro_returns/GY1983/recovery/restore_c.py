#!/usr/bin/env python3
"""Rebuild records C files from the two recovered JSON bundles.
Usage: python rebuild_c.py core.json audit.json output_directory
This recovery script was authored during the execution outage; it was not run there.
"""
import csv
import json
import sys
from pathlib import Path

core = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
audit = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
out = Path(sys.argv[3])
out.mkdir(parents=True, exist_ok=True)
assert len(core["items"]) == 107
assert len({x["id"] for x in core["items"]}) == 107
keys = {r["key"] for r in core["references"]}
assert all(k in keys for x in core["items"] for k in x["refs"])
talks = []
for original in core["talks"]:
    t = dict(original)
    t["catalogue_pages"] = t["pages"]
    t["pages"] = t["actual_pages"]
    talks.append(t)
def write_json(name, value):
    (out / name).write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
write_json("talks.json", talks)
for key in ("items", "problems", "references"):
    write_json(key + ".json", core[key])
(out / "references.bib").write_text(core["references_bib"], encoding="utf-8")
fields = ("page", "place", "transcription_reads", "should_read",
          "evidence", "applies_to", "type")
with (out / "corrections.csv").open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(core["corrections"])
for key, filename in (
    ("coverage_md", "coverage.md"),
    ("research_log_md", "research_log.md"),
    ("proof_review_laurent_md", "proof_review_root.md"),
    ("proof_review_radon_md", "proof_review_radon.md"),
):
    (out / filename).write_text(audit[key], encoding="utf-8")
write_json("validation.json", audit["validation"])
for filename, code in audit["code"].items():
    (out / filename).write_text(code, encoding="utf-8")
print(json.dumps({
    "talks": len(talks), "items": len(core["items"]),
    "problems": len(core["problems"]), "corrections": len(core["corrections"]),
    "references": len(core["references"]), "output_directory": str(out),
    "tex_compiled": False, "pdf_created": False, "zip_created": False
}, ensure_ascii=False))
