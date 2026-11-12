"""G2 registry: academic years -> catalogue records -> notebook pages, with the companion chapters that discuss them.

Inputs: source-provenance.json of the locked release (catalogue records and the 1,527 manuscript frames with their
records and archive chapters), data/catalogue_fixes.json (misprinted dates; records without pages), the talks.json of
every companion chapter, and the two reader PDFs (to find the PDF page on which each notebook page starts).

The academic year of a record (August starts the year): its catalogued date (or the corrected date); for an undated
record, the date or year written in its catalogue label ('8-Feb-65.', '1965-66.', 'YEAR 1966' = the year containing
January 1966, '1972.' = the year starting in autumn 1972), else the year of the next dated record.

Output: WORK/ir/registry.json.  Accepted when every record of every talks.json is a catalogue record, and every page
P000001-P001527 belongs to an archive chapter.  Records whose pages in talks.json differ from the catalogue's frames
are listed in reports/g2_page_differences.tsv (the site shows the catalogue's pages and the companion's).
"""
import collections
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import (DATA, IR, YEARS_DIR, acad, chapter_tags, latex_dir, lock, log, parse_pages, pid, release_dir,
                    report, rjson, work_map, wjson, works)

MON = {m: i for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}


def label_year(label):
    s = (label or "").strip()
    m = re.match(r"^(\d{4})-(\d{2})\.?$", s)
    if m:
        return f"{m.group(1)}-{m.group(2)}"
    m = re.match(r"^(\d{1,2})[-_ ]([A-Za-z]{3,})[-_ ](\d{2})", s)
    if m and m.group(2)[:3].lower() in MON:
        return acad(f"{1900 + int(m.group(3))}-{MON[m.group(2)[:3].lower()]:02d}-{int(m.group(1)):02d}")
    m = re.match(r"^YEAR (\d{4})", s)
    if m:
        y = int(m.group(1)) - 1
        return f"{y}-{(y + 1) % 100:02d}"
    m = re.match(r"^(\d{4})\.$", s)
    if m:
        y = int(m.group(1))
        return f"{y}-{(y + 1) % 100:02d}"
    return None


def label_date(label):
    m = re.match(r"^\s*(\d{1,2})[-_ ]([A-Za-z]{3,})[-_ ](\d{2})", label or "")
    if m and m.group(2)[:3].lower() in MON:
        return f"{1900 + int(m.group(3))}-{MON[m.group(2)[:3].lower()]:02d}-{int(m.group(1)):02d}"
    return None


def pdf_page_map(pdf):
    """notebook page number -> PDF page on which a line first starts with its heading 'GELFAND-Pnnnnnn'."""
    txt = pdf.with_suffix(".txt")
    if not txt.exists() or txt.stat().st_mtime < pdf.stat().st_mtime:
        subprocess.run(["pdftotext", "-enc", "UTF-8", "-layout", str(pdf), str(txt)], check=True)
    pages = txt.read_text(encoding="utf-8").split("\f")
    out = {}
    for i, pg in enumerate(pages, 1):
        for m in re.finditer(r"^\s*GELFAND-P(\d{6})(?=\s|$)", pg, re.M):
            out.setdefault(int(m.group(1)), i)
    return out, len(pages) - (1 if pages and not pages[-1].strip() else 0)


def main():
    lk = lock()
    prov = rjson(latex_dir() / "source-provenance.json")
    fixes = rjson(DATA / "catalogue_fixes.json")
    reg_works = rjson(DATA / "works.json")
    excl_records = set(reg_works.get("exclude_records") or [])
    recs = {}
    for r in prov["catalogue_records"]:
        recs[r["record"]] = dict(r, empty=False)
    for r in fixes["empty_records"]:
        if r["record"] not in recs:
            recs[r["record"]] = dict(r, empty=True)
    pages = {}
    rec_pages = collections.defaultdict(list)
    for f in prov["manuscript_frames"]:
        n = int(f["manuscript_frame"][-6:])
        pages[n] = {"chapter": f["archive_chapter"], "part": f.get("archive_part"),
                    "records": list(f["catalogue_record_numbers"]), "scans": f.get("upstream_image_URLs") or []}
        for r in f["catalogue_record_numbers"]:
            rec_pages[r].append(n)
    # reader PDFs
    pdfmaps = {}
    for lang, name in (("ru", "gelfand-russian-chapters01-34-complete-first1527.pdf"),
                       ("en", "gelfand-english-chapters01-34-complete-first1527.pdf")):
        m, npages = pdf_page_map(release_dir() / name)
        pdfmaps[lang] = {"file": name, "pages": npages, "found": len(m)}
        for n, pg in m.items():
            if n in pages:
                pages[n].setdefault("pdf", {})[lang] = pg
    # dates and years
    dated = {}
    for n, r in recs.items():
        fx = fixes["date_fixes"].get(str(n))
        d = fx["date"] if fx else r.get("date_as_catalogued")
        if d:
            dated[n] = d
    order = sorted(recs)
    for n in order:
        r = recs[n]
        fx = fixes["date_fixes"].get(str(n))
        r["date"] = dated.get(n) or label_date(r.get("label"))
        r["date_fix"] = fx
        if n in dated:
            r["year"] = acad(dated[n])
            r["year_rule"] = "date"
        elif label_year(r.get("label")):
            r["year"] = label_year(r.get("label"))
            r["year_rule"] = "label"
        else:
            nxt = [m for m in order if m > n and m in dated]
            prv = [m for m in order if m < n and m in dated]
            r["year"] = acad(dated[nxt[0]]) if nxt else acad(dated[prv[-1]])
            r["year_rule"] = "next dated record"
        r["pages"] = sorted(set(rec_pages.get(n, [])))
        r["archive_chapters"] = sorted({pages[p]["chapter"] for p in r["pages"]})
        r["url"] = r.get("catalogue_record_url") or f"https://old.mccme.ru/gelfand/notes/record-{n}.html"
        r["chapters"] = []
        r["excluded"] = n in excl_records
    # companion chapters
    wm = {w.get("tag"): w for w in works() if w["kind"] == "companion-chapter"}
    chapters = {}
    unknown, diffs = [], []
    for tag in chapter_tags(all_=True):
        w = wm[tag]
        talks = json.loads((YEARS_DIR / tag / f"{tag}_talks.json").read_text(encoding="utf-8"))
        chapters[tag] = {"tag": tag, "work": w["id"], "years": w["years"], "written": w["written"],
                         "model": w["model"], "include": w["include"], "records": [t["record"] for t in talks]}
        for t in talks:
            n = t["record"]
            if n not in recs:
                unknown.append((tag, n))
                continue
            recs[n]["chapters"].append(tag)
            tp = parse_pages(t.get("pages"))
            if tp != recs[n]["pages"]:
                diffs.append((tag, n, t.get("pages"), ", ".join(pid(p) for p in recs[n]["pages"])))
    # years
    years = collections.defaultdict(list)
    for n in order:
        years[recs[n]["year"]].append(n)
    ylist = []
    for y in sorted(years):
        rs = years[y]
        cov = [t for t, c in chapters.items() if y in c["years"]]
        extra = sorted({n for t in cov for n in chapters[t]["records"] if recs[n]["year"] != y})
        ylist.append({"year": y, "records": rs, "pages": sorted({p for n in rs for p in recs[n]["pages"]}),
                      "chapters": cov, "chapter_records_from_other_years": extra})
    # chapters' records not in their talks.json
    no_entry = []
    for t, c in chapters.items():
        mine = set(c["records"])
        for y in c["years"]:
            for n in years.get(y, []):
                if n not in mine:
                    no_entry.append((t, y, n, recs[n].get("label")))
    arch = collections.defaultdict(list)
    for n, p in sorted(pages.items()):
        arch[p["chapter"]].append(n)
    orphan_pages = [n for n in range(1, 1528) if n not in pages or not pages[n].get("chapter")]
    out = {"release": {"tag": lk["release"]["tag"], "commit": lk["release"]["commit"],
                       "created_at": lk["release"]["created_at"]},
           "pdf": pdfmaps,
           "chapters": chapters,
           "years": ylist,
           "records": {str(n): recs[n] for n in order},
           "pages": {str(n): pages[n] for n in sorted(pages)},
           "archive_chapters": {str(k): v for k, v in sorted(arch.items())}}
    wjson(IR / "registry.json", out)
    report("g2_page_differences", diffs, ["chapter", "record", "pages in talks.json", "pages in the catalogue frames"])
    report("g2_records_without_entry", no_entry, ["chapter", "academic year", "record", "catalogue label"])
    report("g2_year_rules", [(n, recs[n].get("label"), recs[n]["year"], recs[n]["year_rule"]) for n in order
                             if recs[n]["year_rule"] != "date"], ["record", "label", "year", "rule"])
    ok = not unknown and not orphan_pages and len(pages) == 1527
    print(f"G2 registry: {len(recs)} records ({sum(1 for r in recs.values() if r['empty'])} without pages), "
          f"{len(pages)} pages in {len(arch)} archive chapters, {len(ylist)} academic years "
          f"({ylist[0]['year']} to {ylist[-1]['year']}), {len(chapters)} chapters; talks.json records not in the "
          f"catalogue: {unknown or 'none'}; pages without archive chapter: {orphan_pages or 'none'}; records whose "
          f"companion pages differ from the catalogue frames: {len(diffs)}; records of a chapter's years without an "
          f"entry in it: {len(no_entry)}; PDF page map: ru {pdfmaps['ru']['found']}, en {pdfmaps['en']['found']} of 1527")
    print("G2", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
