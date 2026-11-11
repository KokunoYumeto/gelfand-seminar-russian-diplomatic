"""Build the ChatGPT Pro package of one chapter of the Gelfand seminar companion (one academic year, or two small ones).

The package is the folder packages/TAG/ with six files: TAG_prompt.md, TAG_en.tex, TAG_ru.tex (the notes of the
year's pages, cut page by page from the newest cumulative working readers), TAG_scans.zip (the scans of those pages),
TAG_talks.md (the MCCME records of the year with their pages) and TAG_kit.zip (the chapter kit, the index of the
earlier years and the cumulative bibliography, built from the pilot and from returned chapters in returns/).

usage: python -I make_year_package.py TAG [TAG ...]      e.g. GY1965
       python -I make_year_package.py --list            the packages and their years, pages and records"""
import collections
import io
import json
import pathlib
import re
import sys
import zipfile

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).parent
WORK = pathlib.Path(r"C:\Users\user\Documents\Codex\2026-10-06\gelfand-pro-transcription-packets-20261006\work")
PKT = pathlib.Path(r"C:\Users\user\Documents\Gelfand Pro transcription packets")
PILOT = pathlib.Path(r"C:\Users\user\Documents\gelfand_year_pilot_20261108\answers\GY1964_unzipped\GY1964")
PACKAGES = {"GY1965": ["1965-66"], "GY1966": ["1966-67"], "GY1967": ["1967-68", "1968-69"],
            "GY1969": ["1969-70", "1970-71"], "GY1971": ["1971-72"], "GY1972": ["1972-73"], "GY1973": ["1973-74"],
            "GY1974": ["1974-75"], "GY1975": ["1975-76"], "GY1976": ["1976-77"], "GY1977": ["1977-78"],
            "GY1978": ["1978-79"], "GY1979": ["1979-80"], "GY1980": ["1980-81"], "GY1981": ["1981-82"],
            "GY1982": ["1982-83"], "GY1983": ["1983-84", "1984-85"], "GY1985": ["1985-86"], "GY1986": ["1986-87"],
            "GY1987": ["1987-88"], "GY1988": ["1988-89", "1990-91"]}


def newest_reader():
    best = None
    for d in WORK.glob("A4-reader-chapters01-*-first*-separated-diplomatic-r*"):
        m = re.search(r"-first(\d+)-separated-diplomatic-r(\d+)$", d.name)
        if m and (d / "sources" / "source-provenance.json").is_file() and \
                len(list((d / "sources").glob("gelfand-*-chapters01-*-first*.tex"))) >= 2:
            k = (int(m.group(1)), int(m.group(2)))
            best = max(best, (k, d)) if best else (k, d)
    return best[1]


READER = newest_reader()
SRC = READER / "sources"
PROV = json.loads((SRC / "source-provenance.json").read_text(encoding="utf-8"))
N_DONE = max(int(f["manuscript_frame"][-6:]) for f in PROV["manuscript_frames"])


def acad(date):
    y, mo = int(date[:4]), int(date[5:7])
    a = y if mo >= 8 else y - 1
    return f"{a}-{(a + 1) % 100:02d}"


REC = {r["record"]: r for r in PROV["catalogue_records"]}
REC_YEAR = {n: acad(r["date_as_catalogued"]) for n, r in REC.items() if r.get("date_as_catalogued")}
REC_PAGES = collections.defaultdict(list)
for f in PROV["manuscript_frames"]:
    for n in f["catalogue_record_numbers"]:
        REC_PAGES[n].append(int(f["manuscript_frame"][-6:]))


def mccme_years():
    """Academic year of every dated record in the full MCCME list (774 records), from its 'dd-Mon-yy' date."""
    import html as _html
    h = pathlib.Path(r"C:\Users\user\AppData\Local\Temp\claude\f2c80a22394db22f\329fb1e6-0570-47be-9060-a2a454bf3e15"
                     r"\scratchpad\mccme\all-links.html").read_bytes().decode("cp1251", errors="replace")
    mon = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}
    out = {}
    for n, d in re.findall(r'<a href="record-(\d+)\.html[^"]*">([^<]*)</a>', h):
        m = re.match(r"\s*(\d{1,2})-([A-Z][a-z]{2})-(\d{2})", _html.unescape(d))
        if m and m.group(2) in mon:
            out[int(n)] = acad(f"{1900 + int(m.group(3))}-{mon[m.group(2)]:02d}-01")
    return out


MCCME_YEAR = mccme_years()


def ready(years):
    want = [n for n, y in MCCME_YEAR.items() if y in years]
    return bool(want) and all(REC_PAGES.get(n) for n in want), len(want)


def records_of(years):
    rs = sorted(n for n, y in REC_YEAR.items() if y in years)
    # undated records (headings, plans) lying between the year's first and last record belong to it too
    if rs:
        rs = sorted(set(rs) | {n for n in REC if rs[0] <= n <= rs[-1] and n not in REC_YEAR})
    return rs


def pages_of(recs):
    return sorted({p for n in recs for p in REC_PAGES.get(n, [])})


def split_pages(tex):
    marks = list(re.finditer(r"\\SourcePage\{GELFAND-P(\d{6})\}", tex))
    out = {}
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else tex.find("\\end{document}", m.start())
        out[int(m.group(1))] = tex[m.start():end if end > 0 else len(tex)]
    return out


def ranges(ps):
    out, start, prev = [], None, None
    for p in ps:
        if start is None:
            start = prev = p
        elif p == prev + 1:
            prev = p
        else:
            out.append((start, prev))
            start = prev = p
    if start is not None:
        out.append((start, prev))
    return out


def fmt_ranges(ps):
    return ", ".join(f"P{a:06d}" if a == b else f"P{a:06d}-P{b:06d}" for a, b in ranges(ps))


def previous_index(tag):
    """Index of the earlier years: the 1964-65 pilot (from its inventory) and every returned chapter before TAG."""
    lines = ["# Items and problems of the earlier years", "",
             "For linking only: when a question of this year recurs from an earlier year, reuse the earlier item ids",
             "in the problem's occurrences and the earlier problem id if there is one.", ""]
    inv = (PILOT / "GY1964_inventory.md").read_text(encoding="utf-8")
    lines += ["## 1964-65 (first run; items are `1964-<record>.<n>`)", ""]
    for m in re.finditer(r"^### (1964-\d+\.\d+)(?: —|\.) (.+)$", inv, re.M):
        c = re.search(r"Class(?:es)? ([A-F])", inv[m.end():m.end() + 400])
        lines.append(f"- {m.group(1)} [{c.group(1) if c else '?'}] {m.group(2)}")
    for d in sorted((HERE / "returns").glob("GY*")):
        if d.name >= tag:
            continue
        for kind in ("items", "problems"):
            p = d / f"{d.name}_{kind}.json"
            if p.exists():
                data = json.loads(p.read_text(encoding="utf-8"))
                lines += ["", f"## {d.name}: {kind}", ""]
                for x in data:
                    lines.append(f"- {x.get('id')} [{x.get('class', x.get('status_date', ''))}] {x.get('title')}")
    return "\n".join(lines) + "\n"


def cumulative_bib(tag):
    parts = ["% References verified in earlier chapters of the companion. Reuse these keys.\n"]
    for d in sorted((HERE / "returns").glob("GY*")):
        p = d / f"{d.name}_references.bib"
        if d.name < tag and p.exists():
            parts.append(f"% ---- from {d.name}\n" + p.read_text(encoding="utf-8"))
    return "\n".join(parts)


def scans(pages):
    found = {}
    want = set(pages)
    for d in sorted(PKT.glob("GELFAND-0*")):
        z = d / f"{d.name}-input.zip"
        if not z.exists():
            continue
        with zipfile.ZipFile(z) as zi:
            for n in zi.namelist():
                m = re.match(r"images/GELFAND-P(\d{6})\.png$", n)
                if m and int(m.group(1)) in want and int(m.group(1)) not in found:
                    found[int(m.group(1))] = zi.read(n)
        if len(found) == len(want):
            break
    return found


def build(tag):
    years = PACKAGES[tag]
    recs = records_of(years)
    pages = pages_of(recs)
    ok, n_all = ready(years)
    if not ok:
        print(tag, "not ready:", len(recs), "of", n_all, "records transcribed; reader has", N_DONE, "pages")
        return
    out = HERE / "packages" / tag
    out.mkdir(parents=True, exist_ok=True)
    for lang, short in (("english", "en"), ("russian", "ru")):
        f = next(SRC.glob(f"gelfand-{lang}-chapters01-*-first*.tex"))
        pg = split_pages(f.read_text(encoding="utf-8"))
        miss = [p for p in pages if p not in pg]
        assert not miss, (lang, miss[:5])
        body = "".join(pg[p] for p in pages)
        body = "\n".join(l for l in body.split("\n") if not l.startswith("\\expandafter\\def"))
        head = (f"% Gelfand seminar notes, {' and '.join(years)}: source pages {fmt_ranges(pages)}.\n"
                f"% {'English translation' if short == 'en' else 'Russian diplomatic transcription'} (AI-made, "
                f"checked against the scans), cut page by page from the cumulative working reader {READER.name}.\n"
                "% \\SourcePage{GELFAND-Pnnnnnn}{label} starts a scanned page; the second argument is the number written\n"
                "% on the page, if any. Editorial notes give the page, a label and the transcriber's remark; \\Unclear\n"
                "% marks a doubtful reading.\n")
        (out / f"{tag}_{short}.tex").write_text(head + body, encoding="utf-8")
    talks = [f"# The I. M. Gelfand seminar, {' and '.join(years)}: the records", "",
             "From the MCCME list of the notes, https://old.mccme.ru/gelfand/notes/all-links.html (record number, date",
             "and speaker as catalogued there; each record's page links to its scans), with the source pages of the",
             "attached transcription on which the record's notes lie. Records without a date are headings or plans.", ""]
    for n in recs:
        r = REC[n]
        talks.append(f"- record {n}: {r.get('label') or ''} ({r.get('date_as_catalogued') or 'no date'}); pages "
                     f"{fmt_ranges(sorted(set(REC_PAGES.get(n, [])))) or 'none listed'}; "
                     f"https://old.mccme.ru/gelfand/notes/record-{n}.html")
    (out / f"{tag}_talks.md").write_text("\n".join(talks) + "\n", encoding="utf-8")
    imgs = scans(pages)
    miss = [p for p in pages if p not in imgs]
    with zipfile.ZipFile(out / f"{tag}_scans.zip", "w", zipfile.ZIP_STORED) as zo:
        for p in pages:
            if p in imgs:
                zo.writestr(f"GELFAND-P{p:06d}.png", imgs[p])
    with zipfile.ZipFile(out / f"{tag}_kit.zip", "w", zipfile.ZIP_DEFLATED) as zo:
        for f in ("CHAPTER_FORMAT.md", "gelfand_companion.sty", "build_chapter.py"):
            zo.write(HERE / "kit" / f, f"kit/{f}")
        zo.writestr("previous_index.md", previous_index(tag))
        zo.writestr("references_cumulative.bib", cumulative_bib(tag))
    long = (f"the academic year {years[0].replace('-', '–')}" if len(years) == 1 else
            "the academic years " + " and ".join(y.replace("-", "–") for y in years))
    rr = ranges(pages)
    note = "" if len(rr) == 1 else (f"; not contiguous: {fmt_ranges(pages)}, because the archive interleaves the "
                                    "years")
    prompt = (HERE / "PROMPT_TEMPLATE.md").read_text(encoding="utf-8")
    for k, v in {"{TAG}": tag, "{YEARS_LONG}": long, "{YEARS_SHORT}": " and ".join(years),
                 "{PAGE_RANGE}": f"GELFAND-P{pages[0]:06d} to P{pages[-1]:06d}", "{N_PAGES}": str(len(pages)),
                 "{PAGE_NOTE}": note, "{N_RECORDS}": str(len(recs))}.items():
        prompt = prompt.replace(k, v)
    (out / f"{tag}_prompt.md").write_text(prompt, encoding="utf-8")
    sizes = {p.name: p.stat().st_size for p in sorted(out.iterdir())}
    print(tag, years, len(recs), "records,", len(pages), "pages", fmt_ranges(pages), "| missing scans:", miss or "none")
    print("   ", sizes)


if __name__ == "__main__":
    if sys.argv[1] == "--list":
        print("reader:", READER.name, "pages done:", N_DONE)
        for tag, years in PACKAGES.items():
            recs = records_of(years)
            ps = pages_of(recs)
            ok, n_all = ready(years)
            print(tag, years, len(recs), "records", len(ps), "pages", fmt_ranges(ps) if ps else "-",
                  "READY" if ok else f"not ready ({n_all} records in the MCCME list)")
    else:
        for t in sys.argv[1:]:
            build(t)
