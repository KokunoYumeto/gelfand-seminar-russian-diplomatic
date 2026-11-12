#!/usr/bin/env python3
"""Restore the exact records-a deliverables from the saved source/audit JSON.
Usage: python restore_payload.py source.json audit.json OUTPUT_DIRECTORY
This restoration script was authored during the execution-environment outage.
It was not executed there. The mathematical JS checks were executed separately.
"""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("audit", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    source = json.loads(args.source.read_text(encoding="utf-8"))
    audit = json.loads(args.audit.read_text(encoding="utf-8"))
    output = args.output
    output.mkdir(parents=True, exist_ok=True)
    scripts = output / "scripts"
    scripts.mkdir(exist_ok=True)
    expected = {597: 9, 599: 0, 600: 18, 601: 24, 602: 7, 603: 10,
                604: 10, 605: 13, 606: 14, 607: 6, 608: 12, 609: 6, 610: 11}
    items = source["items"]
    assert len(items) == 140
    assert len({item["id"] for item in items}) == 140
    for record, count in expected.items():
        assert sum(item["record"] == record for item in items) == count
    def write_json(name: str, value: object) -> None:
        (output / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n",
                                  encoding="utf-8")
    for name in ("talks", "items", "problems"):
        write_json(name + ".json", source[name])
    (output / "references.bib").write_text(source["references_bib"], encoding="utf-8")
    (output / "coverage.md").write_text(audit["coverage_md"], encoding="utf-8")
    (output / "research_log.md").write_text(audit["research_log_md"], encoding="utf-8")
    fields = ["page", "place", "transcription_reads", "should_read",
              "evidence", "applies_to", "type"]
    with (output / "corrections.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(audit["corrections"])
    (scripts / "verify_occurrences.js").write_text(
        audit["verification_js"] + "\n\nconsole.log(JSON.stringify(verifyA(), null, 2));\n",
        encoding="utf-8")
    (scripts / "authoring_helpers.js").write_text(
        "// Historical source helpers for the functions V8 load/store environment.\n"
        "// Supplied as source provenance; restore_payload.py uses final JSON instead.\n"
        + audit["authoring_helpers_js"] + "\n", encoding="utf-8")
    (scripts / "restore_payload.py").write_text(audit["restore_py"], encoding="utf-8")
    write_json("verification_output.json", audit["verification_output"])
    write_json("schema_audit.json", audit["schema_audit"])
    print(json.dumps({"talks": len(source["talks"]), "items": len(items),
                      "problems": len(source["problems"]),
                      "corrections": len(audit["corrections"]),
                      "output": str(output)}, ensure_ascii=False))

if __name__ == "__main__":
    main()
