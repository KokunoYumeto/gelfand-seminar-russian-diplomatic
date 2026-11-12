"""Additional semantic checks beyond the supplied chapter builder."""
from pathlib import Path
from collections import Counter, defaultdict
import csv
import json
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemble_data import bib_entries

WORK = Path(__file__).resolve().parents[1]
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else WORK / "output"

ENUMS = {
 "kind": set("definition construction theorem claim conjecture question problem method remark".split()),
 "class": set("ABCDEF"),
 "literal_correctness": {"correct", "correct with missing hypotheses", "false as written", "not determinable"},
 "publication_match": {"exact", "partial", "thematic only", "none found"},
 "verification": {"read the result", "publisher metadata checked", "indirect", "unresolved lead"},
 "development": {"none", "annotated", "developed in this chapter"},
 "confidence": {"high", "medium", "low"},
}
FIELDS = {"id", "record", "pages", "kind", "title", "notes", "statement", "reconstruction", "class", "fate",
          "present_status", "literal_correctness", "publication_match", "verification", "development", "problem", "worth", "refs", "confidence"}

def cites(value):
    return {k.strip() for group in re.findall(r"\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}", value)
            for k in group.split(",") if k.strip()}

def main():
    errors, review = [], []
    talks = json.loads((OUT / "GY1964_talks.json").read_text())
    items = json.loads((OUT / "GY1964_items.json").read_text())
    problems = json.loads((OUT / "GY1964_problems.json").read_text())
    bibliography = bib_entries((OUT / "GY1964_references.bib").read_text())
    if [t["record"] for t in talks] != list(range(2,51)):
        errors.append("Records must be exactly 2 through 50 in supplied catalogue order.")
    for t in talks:
        if t.get("kind") not in {"talk", "plan", "heading", "other"}:
            errors.append(f"record {t['record']}: invalid kind")
        if not t.get("summary") or not t.get("pages"):
            errors.append(f"record {t['record']}: empty summary or pages")
    known_ids = {x["id"] for x in items}
    problem_by_id = {p["id"]: p for p in problems}
    for x in items:
        missing = FIELDS - x.keys()
        if missing:
            errors.append(f"{x['id']}: missing {sorted(missing)}")
        for key, allowed in ENUMS.items():
            if x.get(key) not in allowed:
                errors.append(f"{x['id']}: {key}={x.get(key)!r}")
        for key in ("notes", "statement", "fate", "present_status"):
            if not x.get(key):
                errors.append(f"{x['id']}: empty {key}")
        if "2026" not in x.get("present_status", ""):
            errors.append(f"{x['id']}: undated present status")
        if x["class"] in "CD" and not x.get("worth"):
            errors.append(f"{x['id']}: C/D needs a development-worth sentence")
        if x["class"] == "D" and not any(w in x["fate"].lower() for w in ("search", "query", "checked")):
            errors.append(f"{x['id']}: D needs a stated search scope")
        cited = cites(" ".join(v for v in x.values() if isinstance(v,str)))
        if cited - set(x["refs"]):
            errors.append(f"{x['id']}: citations omitted from refs {sorted(cited-set(x['refs']))}")
        if set(x["refs"]) - bibliography.keys():
            errors.append(f"{x['id']}: missing bibliography keys")
        if x.get("problem"):
            p = problem_by_id.get(x["problem"])
            if not p or x["id"] not in p.get("occurrences", []):
                errors.append(f"{x['id']}: problem back-link missing")
        if "P000090" in x["pages"]:
            review.append(f"{x['id']}: touches next-year page90; verify scope")
        if x["kind"] in {"question", "conjecture", "problem"} and not x.get("problem"):
            review.append(f"{x['id']}: question without problem index entry; justify exclusion")
    for p in problems:
        if p["status_date"] != "2026-11":
            errors.append(f"{p['id']}: incorrect status date")
        for occurrence in p["occurrences"]:
            if occurrence.startswith("1964-") and occurrence not in known_ids:
                errors.append(f"{p['id']}: unknown occurrence {occurrence}")
        if cites(p["statement"]+p["status"]) - set(p["refs"]):
            errors.append(f"{p['id']}: citation omitted from refs")
    doi_keys, url_keys = defaultdict(list), defaultdict(list)
    for key, entry in bibliography.items():
        if not re.search(r"\bnote\s*=\s*\{(?:verified|unverified)\}", entry, re.I):
            errors.append(f"{key}: missing literal verified/unverified bibliography note")
        if not re.search(r"\b(?:url|doi)\s*=", entry, re.I):
            errors.append(f"{key}: missing URL/DOI")
        for field, dest in (("doi",doi_keys),("url",url_keys)):
            m = re.search(rf"\b{field}\s*=\s*\{{([^}}]+)\}}", entry, re.I)
            if m:
                dest[m.group(1).lower().rstrip("/")].append(key)
    for field, mapping in (("DOI",doi_keys),("URL",url_keys)):
        for value, keys in mapping.items():
            if len(keys)>1:
                review.append(f"Duplicate {field}: {keys}: {value}")
    baseline_path = WORK / "evidence/input_audit.json"
    baseline = json.loads(baseline_path.read_text())["occurrences"] if baseline_path.exists() else []
    base = {x["id"]:x for x in baseline}
    missing_baseline = sorted(set(base) - known_ids)
    if missing_baseline:
        errors.append(f"Baseline occurrences omitted: {missing_baseline}")
    changes = [{"id":x["id"],"old_class":base[x["id"]]["class"],"new_class":x["class"]}
               for x in items if x["id"] in base and x["class"] != base[x["id"]]["class"]]
    report = {"records":len(talks),"items":len(items),"problems":len(problems),"references":len(bibliography),
              "classes":dict(sorted(Counter(x['class'] for x in items).items())),
              "verification":dict(Counter(x['verification'] for x in items)),
              "confidence":dict(Counter(x['confidence'] for x in items)),
              "baseline_class_changes":changes,
              "new_occurrences":[x['id'] for x in items if x['id'] not in base],
              "missing_baseline_occurrences":missing_baseline,
              "errors":errors,"review_flags":review}
    (WORK / "evidence/data_audit.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(report,ensure_ascii=False,indent=2))
    raise SystemExit(bool(errors))

if __name__ == "__main__":
    main()
