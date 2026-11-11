"""Structural validation for the late-record contribution; full TeX build is root-owned."""
import collections
import csv
import json
import re
from pathlib import Path

PART = Path(__file__).parent
talks = json.loads((PART / "late_talks.json").read_text())
items = json.loads((PART / "late_items.json").read_text())
problems = json.loads((PART / "late_problems.json").read_text())
evidence = json.loads((PART / "late_evidence.json").read_text())
bib = (PART / "late_references.bib").read_text()
keys = set(re.findall(r"@\w+\{([^,]+),", bib))
errors = []
required = set(
    "id record pages kind title notes statement reconstruction class fate "
    "present_status literal_correctness publication_match verification "
    "development problem worth refs confidence".split()
)
allowed = {
    "kind": set("definition construction theorem claim conjecture question problem method remark".split()),
    "class": set("ABCDEF"),
    "literal_correctness": {"correct", "correct with missing hypotheses", "false as written", "not determinable"},
    "publication_match": {"exact", "partial", "thematic only", "none found"},
    "verification": {"read the result", "publisher metadata checked", "indirect", "unresolved lead"},
    "development": {"none", "annotated", "developed in this chapter"},
    "confidence": {"high", "medium", "low"},
}
for item in items:
    missing = required - item.keys()
    if missing:
        errors.append((item.get("id"), "missing", sorted(missing)))
    for field, choices in allowed.items():
        if item.get(field) not in choices:
            errors.append((item["id"], field, item.get(field)))
    if item["class"] in "CD" and not item["worth"]:
        errors.append((item["id"], "worth empty"))
    if not set(item["refs"]) <= keys:
        errors.append((item["id"], "undefined refs", sorted(set(item["refs"]) - keys)))
    for field, value in item.items():
        if not isinstance(value, str):
            continue
        citations = {
            key.strip()
            for group in re.findall(r"\\cite\w*\{([^}]+)\}", value)
            for key in group.split(",")
        }
        if not citations <= set(item["refs"]):
            errors.append((item["id"], field, "uncatalogued citation", sorted(citations - set(item["refs"]))))
        stripped = re.sub(r"\\[{}]", "", value)
        depth = 0
        for character in stripped:
            if character == "{":
                depth += 1
            elif character == "}":
                depth -= 1
            if depth < 0:
                break
        if depth != 0:
            errors.append((item["id"], field, "brace balance", depth))
        if value.count(r"\(") != value.count(r"\)") or value.count(r"\[") != value.count(r"\]"):
            errors.append((item["id"], field, "math-delimiter balance"))
for talk in talks:
    numbers = [int(item["id"].split(".")[1]) for item in items if item["record"] == talk["record"]]
    if numbers != list(range(1, len(numbers) + 1)):
        errors.append((talk["record"], "nonconsecutive IDs", numbers))
if [talk["record"] for talk in talks] != [81, 82, 83, 84, 85, 86, 87, 89, 88]:
    errors.append("source-order mismatch")
if len({item["id"] for item in items}) != len(items):
    errors.append("duplicate IDs")
if {source["key"] for source in evidence["sources"]} != keys:
    errors.append("ledger/bibliography key mismatch")
for problem in problems:
    if not set(problem["occurrences"]) <= {item["id"] for item in items}:
        errors.append((problem["id"], "unknown occurrence"))
    if not set(problem["refs"]) <= keys:
        errors.append((problem["id"], "unknown reference"))
with (PART / "late_corrections.csv").open() as stream:
    corrections = list(csv.DictReader(stream))
major = {"1965-83.4", "1965-83.5", "1965-86.1", "1965-86.2", "1965-87.4"}
tagged = all(r"\ours" in item["reconstruction"] for item in items if item["id"] in major)
if not tagged:
    errors.append("major derivation missing provenance tag")
report = (PART / "late_report.md").read_text()
if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", report):
    errors.append("control character in report")
print(f"Records: {len(talks)}; items: {len(items)}; problems: {len(problems)}; corrections: {len(corrections)}; references: {len(keys)}.")
print("Class counts:", dict(collections.Counter(item["class"] for item in items)))
print("All major supplied derivations carry provenance tags:", tagged)
print("Validation errors:", errors)
assert not errors

