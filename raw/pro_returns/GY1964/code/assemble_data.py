"""Assemble disjoint, independently researched record blocks.

The authoritative final data are the GY1964 JSON/CSV/BibTeX files. This script
records how the initial reviewed blocks were merged; final editorial changes
are separately recorded in editorial_changes.json when applied.
"""
from pathlib import Path
from collections import Counter
import csv
import json
import re
import sys

WORK = Path(__file__).resolve().parents[1]
OUT = Path(sys.argv[1]).resolve() if len(sys.argv)>1 else WORK / "output"
OUT.mkdir(exist_ok=True)

def bib_entries(text):
    entries = {}
    for m in re.finditer(r"(?m)^@\w+\s*\{\s*([^,\s]+)\s*,", text):
        depth, end, escaped = 1, m.end(), False
        while end < len(text) and depth:
            c = text[end]
            if c == "{" and not escaped:
                depth += 1
            elif c == "}" and not escaped:
                depth -= 1
            escaped = c == "\\" and not escaped
            if c != "\\":
                escaped = False
            end += 1
        if depth:
            raise ValueError(f"Unbalanced bibliography entry {m.group(1)}")
        key = m.group(1)
        if key in entries:
            raise ValueError(f"Duplicate key within one bibliography: {key}")
        entries[key] = text[m.start():end]
    return entries

def main():
    datasets = {"talks": [], "items": [], "problems": []}
    corrections, bibliography, conflicts = [], {}, []
    for part in ("autumn", "winter", "spring"):
        directory = WORK / "parts" / part
        for kind in datasets:
            datasets[kind].extend(json.loads((directory / f"{kind}.json").read_text()))
        with (directory / "corrections.csv").open(newline="") as handle:
            corrections.extend(csv.DictReader(handle))
        for key, entry in bib_entries((directory / "references.bib").read_text()).items():
            if key in bibliography and re.sub(r"\s+", "", bibliography[key]) != re.sub(r"\s+", "", entry):
                conflicts.append({"key": key, "part": part, "existing": bibliography[key], "incoming": entry})
            else:
                bibliography[key] = entry
    for key, entry in bib_entries((WORK / "parts/root_references.bib").read_text()).items():
        if key not in bibliography:
            bibliography[key] = entry
        elif re.sub(r"\s+", "", bibliography[key]) != re.sub(r"\s+", "", entry):
            conflicts.append({"key": key, "part": "root", "existing": bibliography[key], "incoming": entry})
    datasets["talks"].sort(key=lambda x: x["record"])
    datasets["items"].sort(key=lambda x: (x["record"], int(x["id"].split(".")[1])))
    # Recurrent problems can be researched in more than one block.
    problems = {}
    for problem in datasets["problems"]:
        key = problem["id"]
        if key not in problems:
            problems[key] = problem
        else:
            for field in ("occurrences", "refs"):
                problems[key][field] = list(dict.fromkeys(problems[key][field] + problem[field]))
            if problem["statement"] != problems[key]["statement"] or problem["status"] != problems[key]["status"]:
                conflicts.append({"problem": key, "existing": problems[key], "incoming": problem})
    datasets["problems"] = list(problems.values())
    for kind, data in datasets.items():
        (OUT / f"GY1964_{kind}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    columns = ["page", "place", "transcription_reads", "should_read", "evidence", "applies_to", "type"]
    with (OUT / "GY1964_corrections.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(corrections)
    (OUT / "GY1964_references.bib").write_text("\n\n".join(bibliography[k] for k in sorted(bibliography)) + "\n")
    (WORK / "evidence/merge_conflicts.json").write_text(json.dumps(conflicts, ensure_ascii=False, indent=2) + "\n")
    print(f"Merged {len(datasets['talks'])} records and {len(datasets['items'])} items.")
    print("Class counts:", dict(sorted(Counter(x["class"] for x in datasets["items"]).items())))
    print(f"Problems: {len(problems)}; bibliography entries: {len(bibliography)}; corrections: {len(corrections)}")
    print(f"Conflicts requiring explicit review: {len(conflicts)}")

if __name__ == "__main__":
    main()
