"""Input integrity, page inventory, and first-run occurrence baseline."""
from pathlib import Path
import hashlib
import re
import json
import sys
from collections import Counter

WORK = Path(__file__).resolve().parents[1]
INPUTS = Path(sys.argv[1]) if len(sys.argv)>1 else WORK.parent / "upload"
files = sorted(INPUTS.iterdir())
manifest = [{"file": p.name, "bytes": p.stat().st_size,
             "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in files if p.is_file()]
index = (WORK / "previous_index.md").read_text()
occurrences = [{"id": i, "class": c, "title": t} for i, c, t in
               re.findall(r"(?m)^- (1964-\d+\.\d+) \[([A-F])\] (.+)$", index)]
records = sorted(set(int(x["id"].split("-")[1].split(".")[0]) for x in occurrences))
report = {"inputs": manifest, "baseline_items": len(occurrences),
          "baseline_classes": dict(sorted(Counter(x["class"] for x in occurrences).items())),
          "baseline_records_with_items": records,
          "baseline_has_earlier_years": bool(re.search(r"(?m)^- (?!1964)\d{4}-", index)),
          "baseline_has_problem_ids": bool(re.search(r"GP-\d{4}-", index)),
          "occurrences": occurrences}
(WORK / "evidence/input_audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
print(f"Attached input files: {len(manifest)}")
print(f"First-run items: {len(occurrences)}")
print("First-run classes:", report["baseline_classes"])
print("Records with baseline items:", len(records))
print("Earlier academic years represented:", report["baseline_has_earlier_years"])
print("Existing problem IDs supplied:", report["baseline_has_problem_ids"])
for lo, hi in [(2,14),(15,35),(36,50)]:
    count = sum(lo <= int(x["id"].split("-")[1].split(".")[0]) <= hi for x in occurrences)
    print(f"Baseline records {lo}-{hi}: {count} items")
