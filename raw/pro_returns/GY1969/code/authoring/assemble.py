#!/usr/bin/env python3
"""Assemble the reviewed GY1969 segment data without changing item identities.

Run from the task workspace. The companion's supplied builder remains the
authority for the fixed schema; code/check_dataset.py adds editorial audits.
"""
from pathlib import Path
import collections
import csv
import json
import re
import shutil

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "work"
OUT = ROOT / "deliverable"
OUT.mkdir(exist_ok=True)
TAG = "GY1969"
PARTS = [WORK / "parts" / p for p in ("early", "middle", "late", "root")]


def bib_entries(text):
    """Read complete brace-delimited BibTeX records, preserving their text."""
    result = {}
    for match in re.finditer(r"(?m)^\s*@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,", text):
        start = match.start()
        pos = text.index("{", match.start())
        depth = 0
        for end in range(pos, len(text)):
            char = text[end]
            if char in "{}" and (end == 0 or text[end - 1] != "\\"):
                depth += 1 if char == "{" else -1
                if depth == 0:
                    result[match.group(2)] = text[start:end + 1].strip()
                    break
        else:
            raise ValueError("Unbalanced BibTeX entry " + match.group(2))
    return result


def field(entry, name):
    match = re.search(r"\b" + re.escape(name) + r"\s*=\s*\{([^{}]*)\}", entry, re.I)
    return match.group(1).strip() if match else ""


cumulative = bib_entries((WORK / "references_cumulative.bib").read_text())
entries = dict(cumulative)
doi_keys = {}
for key, entry in cumulative.items():
    doi = field(entry, "doi").lower().removeprefix("https://doi.org/")
    if doi:
        doi_keys.setdefault(doi, key)
aliases = {}
conflicts = []
for part in PARTS:
    path = part / "references.bib"
    if not path.exists():
        continue
    for key, entry in bib_entries(path.read_text()).items():
        doi = field(entry, "doi").lower().removeprefix("https://doi.org/")
        if key in cumulative:
            canonical = key
        elif doi and doi in doi_keys:
            canonical = doi_keys[doi]
        else:
            canonical = key
        if canonical != key:
            aliases[key] = canonical
        if canonical not in entries:
            entries[canonical] = re.sub(r"^(@\w+\s*\{)\s*[^,]+", lambda m: m[1] + canonical, entry)
        elif canonical not in cumulative and entries[canonical] != entry and canonical == key:
            conflicts.append({"key": key, "part": str(part.relative_to(ROOT)),
                              "action": "retained first complete entry"})
        if doi:
            doi_keys.setdefault(doi, canonical)

# Bibliographic container fields checked against Numdam's own records on
# 2026-11-09. An expose number is a chapter, not the serial issue number.
for key, number, series, publisher, chapter in [
    ("cartier1968theta", "10", "Séminaire Bourbaki", "Société mathématique de France", "338"),
    ("meyer1987uncertainty", "145--146", "Astérisque", "Société mathématique de France", "662"),
    ("raynaud1969artin", "11", "Séminaire Bourbaki", "Springer-Verlag", "363"),
    ("serre1954borelweil", "2", "Séminaire Bourbaki", "Société mathématique de France", "100"),
]:
    if key in entries:
        entry = entries[key]
        entry = re.sub(r"(?m)^\s*(?:volume|number|series|publisher|chapter|type)\s*=.*\n", "", entry)
        extra = f"  series = {{{series}}},\n  number = {{{number}}},\n  publisher = {{{publisher}}},\n  chapter = {{{chapter}}},\n  type = {{Exposé}},\n"
        entries[key] = entry.replace("\n", "\n" + extra, 1)
if "fichera1967unilateral" in entries:
    entry = entries["fichera1967unilateral"].replace("@incollection", "@article", 1)
    entry = re.sub(r"(?m)^\s*booktitle\s*=.*\n", "  journal = {Séminaire sur les équations aux dérivées partielles, no. 3},\n", entry)
    entry = re.sub(r"(?m)^\s*number\s*=.*\n", "", entry)
    entry = entry.replace("year = {1967}", "year = {1966--1967}")
    entries["fichera1967unilateral"] = entry.replace("\n", "\n  publisher = {Collège de France},\n", 1)


def normalize(value):
    if isinstance(value, dict):
        return {k: normalize(v) for k, v in value.items()}
    if isinstance(value, list):
        return [normalize(v) for v in value]
    if not isinstance(value, str):
        return value
    value = value.replace("\\'s", "'s")
    value = value.replace("\textquotesingle", "'").replace("\textquoteright", "'")
    value = value.replace("semisisimple", "semisimple")
    if value in aliases:
        return aliases[value]
    for old, new in aliases.items():
        value = re.sub(r"(?<=[{,])" + re.escape(old) + r"(?=[,}])", new, value)
    return value


def collect(name):
    out = []
    for part in PARTS:
        p = part / (name + ".json")
        if p.exists():
            out.extend(json.loads(p.read_text()))
    return normalize(out)


talks = collect("talks")
items = collect("items")
problems = collect("problems")
for item in items:
    if item["id"] == "1970-195.6":
        item["statement"] = item["statement"].replace(
            "The nearest-neighbor energy resembles the classical one-step Markov/Gibbs construction.",
            "The nearest-neighbor energy resembles a one-step Markov model with Gibbs weights.")
    if item["id"] == "1970-196.1":
        item["statement"] = r"For every commutative ring \(A\) and every \(A\)-module \(M\), \[H^q(\operatorname{Spec}A,\widetilde M)=0\qquad(q>0).\] Neither Noetherianity nor finite generation of \(M\) is required."
    if item["id"] == "1970-199.1":
        item["statement"] = r"For a finite distinguished-open cover, choose \(N\) and lifts \(u_i^{(k)}\in M_{f_i}\) of \(f_k^N m_{ik}\). Increase the common exponent, multiplying the lifts by the same extra powers of \(f_k\), so that all finitely many localization-equality errors vanish and \(u_i^{(k)}-u_j^{(k)}=f_k^N m_{ij}\) in \(M_{f_if_j}\). Choose \(g_k\in A\) with \(\sum_k g_kf_k^N=1\). Then \(n_i=\sum_k g_ku_i^{(k)}\) satisfies \(m_{ij}=n_i-n_j\), proving degree-one affine acyclicity. The lifts are chosen; localization maps need not be injective."
    if item["id"] == "1970-201.6":
        item["statement"] = item["statement"].replace(
            r"with the grading shifted by \(-n\)",
            r"where \(\operatorname{Hom}_k(R_d,k)\) is placed in degree \(-d-n\)")
# Source leaves precede numerical catalogue order in the first section.
# Within a shared page the source's heading order is retained explicitly.
source_tie_order = {186: 0, 184: 1, 185: 2, 181: 0, 182: 1}
talks.sort(key=lambda t: (int(re.search(r"P(\d+)", t["pages"])[1]),
                          source_tie_order.get(t["record"], t["record"])))
rank = {t["record"]: n for n, t in enumerate(talks)}
items.sort(key=lambda x: (rank[x["record"]], int(x["id"].rsplit(".", 1)[1])))
problems.sort(key=lambda p: p["id"])
for name, data in [("talks", talks), ("items", items), ("problems", problems)]:
    (OUT / f"{TAG}_{name}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

corrections = []
for part in PARTS:
    p = part / "corrections.csv"
    if p.exists():
        with p.open(newline="") as stream:
            corrections.extend(csv.DictReader(stream))
corrections = normalize(corrections)
for row in corrections:
    for key in ("place", "transcription_reads", "should_read", "evidence"):
        row[key] = row[key].replace("16_Nov-70", r"\texttt{16\_Nov-70}")
corrections.sort(key=lambda r: (r["page"], r["place"]))
with (OUT / f"{TAG}_corrections.csv").open("w", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=["page", "place", "transcription_reads", "should_read",
                                               "evidence", "applies_to", "type"])
    writer.writeheader()
    writer.writerows(corrections)

development = normalize((WORK / "parts/root/development.tex").read_text())
(OUT / f"{TAG}_development.tex").write_text(development)
text_to_check = json.dumps([talks, items, problems, corrections], ensure_ascii=False).replace("\\\\", "\\") + development
used = {k for obj in items + problems for k in obj.get("refs", [])}
for group in re.findall(r"\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}", text_to_check):
    used.update(k.strip() for k in group.split(",") if k.strip())
# The overview/report uses the archive itself for its boundary attribution.
used.add("mccme2026gelfand")
missing = sorted(used - entries.keys())
if missing:
    raise ValueError("Missing bibliography keys: " + ", ".join(missing))
(OUT / f"{TAG}_references.bib").write_text(
    "% Verified source records; see research/source_checks.json for verification scope.\n\n"
    + "\n\n".join(entries[k] for k in sorted(used)) + "\n")

for name in ["build_chapter.py", "gelfand_companion.sty", "CHAPTER_FORMAT.md"]:
    shutil.copy2(WORK / "kit" / name, OUT / name)
(OUT / "research").mkdir(exist_ok=True)
sources = []
for part in PARTS:
    path = part / "sources.json"
    if path.exists():
        value = json.loads(path.read_text())
        if isinstance(value, list):
            sources.extend({"segment": part.name, **normalize(v)} if isinstance(v, dict)
                           else {"segment": part.name, "entry": normalize(v)} for v in value)
        else:
            sources.append({"segment": part.name, "ledger": normalize(value)})
(OUT / "research/source_checks.json").write_text(json.dumps(sources, ensure_ascii=False, indent=2) + "\n")
audit = {"record_count": len(talks), "item_count": len(items),
         "problem_count": len(problems), "reference_count": len(used),
         "correction_count": len(corrections), "class_counts": dict(collections.Counter(x["class"] for x in items)),
         "source_record_order": [t["record"] for t in talks], "reference_key_aliases": aliases,
         "final_editorial_normalizations": ["1970-195.6 prose line breaking", "1970-196.1 displayed vanishing formula", "1970-199.1 explicit localization lifts", "1970-201.6 explicit dual grading", "record201 date literal typeset as text"],
         "bibliography_conflicts": conflicts}
(OUT / "research/assembly_audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(audit, indent=2))
