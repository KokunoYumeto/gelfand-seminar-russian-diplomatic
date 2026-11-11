#!/usr/bin/env python3
"""Editorial checks beyond the supplied GY1969 schema builder."""
from pathlib import Path
import collections
import csv
import json
import re
import sys

D = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
TAG = "GY1969"
talks = json.loads((D / f"{TAG}_talks.json").read_text())
items = json.loads((D / f"{TAG}_items.json").read_text())
problems = json.loads((D / f"{TAG}_problems.json").read_text())
bib = (D / f"{TAG}_references.bib").read_text()
keys = re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib)
errors = []
warnings = []


def require(condition, message):
    if not condition:
        errors.append(message)


require({t["record"] for t in talks} == set(range(174, 229)), "Records must be exactly174–228")
require(len(talks) == 55, "Exactly55 catalogue records required")
require(len(keys) == len(set(keys)), "Duplicate bibliography keys")
require(len({x["id"] for x in items}) == len(items), "Duplicate occurrence IDs")
required = {"id", "record", "pages", "kind", "title", "notes", "statement", "reconstruction",
            "class", "fate", "present_status", "literal_correctness", "publication_match",
            "verification", "development", "problem", "worth", "refs", "confidence"}
enums = {
    "kind": {"definition", "construction", "theorem", "claim", "conjecture", "question", "problem", "method", "remark"},
    "literal_correctness": {"correct", "correct with missing hypotheses", "false as written", "not determinable"},
    "publication_match": {"exact", "partial", "thematic only", "none found"},
    "verification": {"read the result", "publisher metadata checked", "indirect", "unresolved lead"},
    "development": {"none", "annotated", "developed in this chapter"},
    "confidence": {"high", "medium", "low"},
    "class": set("ABCDEF"),
}
byid = {x["id"]: x for x in items}
byproblem = {p["id"]: p for p in problems}
for x in items:
    require(required <= x.keys(), f"{x['id']}: missing fields {required - x.keys()}")
    for field, values in enums.items():
        require(x.get(field) in values, f"{x['id']}: invalid {field}={x.get(field)!r}")
    require("2026" in x["present_status"], f"{x['id']}: present status has no explicit2026 date")
    if x["class"] in "CD":
        require(bool(x["worth"].strip()), f"{x['id']}: C/D needs worth sentence")
    if x["problem"]:
        require(x["problem"] in byproblem, f"{x['id']}: missing problem object")
        if x["problem"] in byproblem:
            require(x["id"] in byproblem[x["problem"]]["occurrences"],
                    f"{x['id']}: problem does not link back")
    citations = set()
    for field in ["notes", "statement", "reconstruction", "fate", "present_status", "worth"]:
        for group in re.findall(r"\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}", x.get(field, "")):
            citations.update(k.strip() for k in group.split(","))
    require(citations <= set(x["refs"]), f"{x['id']}: cited keys absent from refs: {citations - set(x['refs'])}")
    for field in ["notes", "statement", "reconstruction", "fate", "present_status"]:
        value = x.get(field, "")
        require(not any(ord(c) < 32 and c != "\n" for c in value), f"{x['id']} {field}: control character")
        if "\\'s" in value:
            warnings.append(f"{x['id']} {field}: possible accent used as apostrophe")
        if "``" in value and "''" not in value and "\\textquotedblright" not in value:
            warnings.append(f"{x['id']} {field}: possibly unclosed TeX quote")

for p in problems:
    require(p["status_date"] == "2026-11", p["id"] + ": wrong status date")
    require(len(p["occurrences"]) == len(set(p["occurrences"])), p["id"] + ": duplicate occurrences")
    for occurrence in p["occurrences"]:
        if occurrence in byid:
            require(byid[occurrence]["problem"] == p["id"],
                    f"{p['id']}: {occurrence} has another or empty problem field")

corrections = list(csv.DictReader((D / f"{TAG}_corrections.csv").open()))
for row in corrections:
    for key in ("place", "transcription_reads", "should_read", "evidence"):
        stripped = re.sub(r"\\\(.*?\\\)|\\\[.*?\\\]|(?<!\\)\$.*?(?<!\\)\$", " ", row[key], flags=re.S)
        stripped = re.sub(r"\\(?:url|nolinkurl|path)\{[^}]*\}", " ", stripped)
        require(not re.search(r"(?<!\\)[_^]", stripped),
                f"{row['page']} correction {key}: raw caret/underscore outside mathematics")
covered = set()
for x in items:
    nums = [int(n) for n in re.findall(r"P(\d+)", x["pages"])]
    if len(nums) == 2 and "-" in x["pages"]:
        covered.update(range(nums[0], nums[1] + 1))
    else:
        covered.update(nums)
report = {
    "record_count": len(talks), "item_count": len(items), "problem_count": len(problems),
    "reference_count": len(keys), "correction_count": len(corrections),
    "class_counts": dict(sorted(collections.Counter(x["class"] for x in items).items())),
    "kind_counts": dict(sorted(collections.Counter(x["kind"] for x in items).items())),
    "verification_counts": dict(sorted(collections.Counter(x["verification"] for x in items).items())),
    "literal_correctness_counts": dict(sorted(collections.Counter(x["literal_correctness"] for x in items).items())),
    "correction_type_counts": dict(sorted(collections.Counter(x["type"] for x in corrections).items())),
    "source_pages_with_indexed_items": sorted(covered),
    "in_scope_pages_without_item_start_or_range": sorted(set(range(283, 360)) - covered),
    "errors": errors, "warnings": warnings,
}
print(json.dumps(report, ensure_ascii=False, indent=2))
sys.exit(bool(errors))
