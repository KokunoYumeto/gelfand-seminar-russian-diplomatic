"""G6 links: item -> record, pages, problem, development; problem -> occurrences; page -> items; reference -> items.

Problems that occur in several chapters' problems.json are merged by id: occurrences are united, the entry with the
latest status_date gives the current status, and differing titles or statements are listed in
reports/g6_problem_variants.tsv (every chapter's entry stays visible on the problem page).

Output: WORK/ir/links.json.  Accepted when every item's record exists, every item's problem id exists, every
occurrence id exists or belongs to a year without a companion chapter (listed as pending and shown without a link),
and every refs key is in the bibliography.
"""
import collections
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import IR, YEARS_DIR, chapter_tags, parse_pages, report, rjson, wjson


def main():
    reg = rjson(IR / "registry.json")
    stale = rjson(IR / "stale_pages.json")
    refs = rjson(IR / "companion" / "references.json")["entries"]
    tags = chapter_tags(all_=True)
    items, problems, pages, refx, records = {}, {}, collections.defaultdict(list), collections.defaultdict(lambda: {"items": [], "problems": []}), collections.defaultdict(lambda: {"entries": [], "items": []})
    bad_record, bad_problem, bad_ref, bad_occ, pending = [], [], [], [], []
    chapter_years = {t: reg["chapters"][t]["years"] for t in tags}
    covered_prefixes = set()
    for t in tags:
        for y in chapter_years[t]:
            covered_prefixes.add(y[:4])
    raw_problems = collections.defaultdict(list)
    for t in tags:
        d = YEARS_DIR / t
        st = set(stale["chapters"].get(t, {}).get("stale_pages", []))
        talks = json.loads((d / f"{t}_talks.json").read_text(encoding="utf-8"))
        for tk in talks:
            records[str(tk["record"])]["entries"].append(t)
        for x in json.loads((d / f"{t}_items.json").read_text(encoding="utf-8")):
            ps = parse_pages(x.get("pages"))
            items[x["id"]] = {"chapter": t, "record": x["record"], "pages": ps, "problem": x.get("problem") or None,
                              "refs": list(x.get("refs") or []), "stale_pages": sorted(set(ps) & st),
                              "class": x.get("class"), "kind": x.get("kind"), "title": x.get("title"),
                              "development": x.get("development")}
            if str(x["record"]) not in reg["records"]:
                bad_record.append((t, x["id"], x["record"]))
            records[str(x["record"])]["items"].append(x["id"])
            for p in ps:
                pages[str(p)].append(x["id"])
            for k in x.get("refs") or []:
                if k not in refs:
                    bad_ref.append((t, x["id"], k))
                else:
                    refx[k]["items"].append(x["id"])
        for p in json.loads((d / f"{t}_problems.json").read_text(encoding="utf-8")):
            raw_problems[p["id"]].append(dict(p, chapter=t))
            for k in p.get("refs") or []:
                if k not in refs:
                    bad_ref.append((t, p["id"], k))
                elif p["id"] not in refx[k]["problems"]:
                    refx[k]["problems"].append(p["id"])
    variants = []
    for pid, ents in raw_problems.items():
        occ = []
        for e in ents:
            for o in e.get("occurrences") or []:
                if o not in occ:
                    occ.append(o)
        latest = max(ents, key=lambda e: (str(e.get("status_date") or ""), e["chapter"]))
        linked, pend = [], []
        for o in occ:
            if o in items:
                linked.append(o)
            elif o.split("-")[0] not in covered_prefixes:
                pend.append(o)
                pending.append((pid, o))
            else:
                bad_occ.append((pid, o))
        problems[pid] = {"chapters": [e["chapter"] for e in ents], "status_from": latest["chapter"],
                         "status_date": latest.get("status_date"), "title": latest.get("title"),
                         "occurrences": occ, "linked": linked, "pending": pend,
                         "years": sorted({o.split("-")[0] for o in occ})}
        if len({e.get("title") for e in ents}) > 1 or len({e.get("statement") for e in ents}) > 1:
            variants.append((pid, " | ".join(e["chapter"] for e in ents),
                             " || ".join(e.get("title") or "" for e in ents)))
    for iid, x in items.items():
        if x["problem"] and x["problem"] not in problems:
            bad_problem.append((x["chapter"], iid, x["problem"]))
        elif x["problem"] and iid not in problems[x["problem"]]["occurrences"]:
            problems[x["problem"]].setdefault("items_naming_it", []).append(iid)
    out = {"items": items, "problems": problems, "pages": dict(pages), "references": dict(refx),
           "records": dict(records)}
    wjson(IR / "links.json", out, indent=None)
    report("g6_bad_records", bad_record, ["chapter", "item", "record"])
    report("g6_bad_problems", bad_problem, ["chapter", "item", "problem"])
    report("g6_bad_refs", bad_ref, ["chapter", "item or problem", "key"])
    report("g6_bad_occurrences", bad_occ, ["problem", "occurrence"])
    report("g6_pending_occurrences", pending, ["problem", "occurrence (year without companion)"])
    report("g6_problem_variants", variants, ["problem", "chapters", "titles"])
    ok = not (bad_record or bad_problem or bad_ref or bad_occ)
    n_entries = sum(len(v) for v in raw_problems.values())
    print(f"G6 links: {len(items)} items, {len(problems)} problems ({n_entries} chapter entries; {len(variants)} with "
          f"differing titles or statements), {len(refx)} references cited by items or problems, "
          f"{len(pages)} notebook pages cited by items; bad records {len(bad_record)}, bad problem ids "
          f"{len(bad_problem)}, bad refs {len(bad_ref)}, bad occurrences {len(bad_occ)}, pending occurrences "
          f"{len(pending)}")
    print("G6", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
