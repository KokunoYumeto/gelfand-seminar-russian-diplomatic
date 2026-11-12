"""G10 checks of the built site (design §7).  Run after g8_render.py (and the later steps that add to the site).

  counts     per companion chapter: talk entries, items, problem entries and references in the source data
             (companion/years) = in the site's data files = rendered on the pages, in both languages
  citations  no undefined citation keys (pandoc's bold "key?" markers) and no leftover build placeholders
  latex      no LaTeX outside math: no TeX control words, \\( \\[ or $ delimiters in the text outside the math spans
  links      every inside link (href, src) reaches a file of the site and its #anchor an id on that page; reader PDF
             links name an existing page of the PDF
  coverage   every record, academic year and problem has a page in both languages
  notices    one status line and one rights statement in the page's language per page (both languages on the
             bilingual pages); the revised-text notice on every talk entry and item whose pages were revised since
             the commentary was written (G7), and on the year page; the commentary-language notice on Russian pages
             with commentary; the stub notice exactly on the years and talks without a companion chapter
  ids        no duplicate ids on a page; <html lang> is the page's language
  notebook   every notebook page has its anchor on its archive chapter's page and its shard in /data/pages/, in both
             languages; the passages and marked readings on the pages equal G3's; G3's parity report is empty
  outside    a sample of 50 outside links (MCCME record pages, DOIs and URLs of the bibliography) answers
             (GELFAND_SKIP_OUTSIDE=1 skips it, e.g. offline)
  size       the site's size by folder (reports/g10_size.tsv), under GitHub Pages' 1 GB
  public     no local paths, e-mail addresses or forbidden terms in the site or in the repository files this build
             publishes (companion/, site-build/, .github/)

Reports: WORK/reports/g10_*.tsv.  Exit status 1 when a check fails.
"""
import collections
import html as H
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import lxml.html

sys.path.insert(0, str(Path(__file__).parent))
from common import (DATA, IR, REPO, REPORTS, SB, YEARS_DIR, chapter_tags, parse_pages, pid, report, rjson,  # noqa
                    site_dir)
from sync_companion import forbidden_patterns, scan_text  # noqa: E402

BASE = os.environ.get("GELFAND_BASE", "/gelfand-seminar-russian-diplomatic/")
UI = rjson(DATA / "ui_strings.json")
OUT = site_dir()
TEXT_EXT = {".html", ".json", ".csv", ".js", ".css", ".txt", ".md", ".bib", ".tex", ".yml", ".yaml", ".py", ".sty",
            ".xml", ".svg", ".tsv"}
RESULTS = []


def result(name, ok, detail):
    RESULTS.append((name, "PASS" if ok else "FAIL", detail))
    print(f"  {'PASS' if ok else 'FAIL'}  {name}: {detail}")


def norm(s):
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", "", s or ""))).strip()


def bib_keys(p):
    keys = []
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", Path(p).read_text(encoding="utf-8")):
        if m.group(1).lower() not in ("comment", "string", "preamble"):
            keys.append(m.group(2))
    return keys


def pdf_pages(p):
    try:
        r = subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True, timeout=60)
        m = re.search(r"^Pages:\s+(\d+)", r.stdout, re.M)
        return int(m.group(1)) if m else None
    except (OSError, subprocess.SubprocessError):
        return None


def main():
    tags = chapter_tags()
    works = {w["id"]: w for w in rjson(DATA / "works.json")["works"]}
    work_tag = {wid: w.get("tag") for wid, w in works.items()}
    pages = sorted(p for p in OUT.rglob("*.html"))
    docs, ids, langs = {}, {}, {}
    dup_ids, lang_bad = [], []
    for p in pages:
        rel = p.relative_to(OUT).as_posix()
        s = p.read_text(encoding="utf-8")
        doc = lxml.html.fromstring(s)
        docs[rel] = (s, doc)
        seen = collections.Counter(el.get("id") for el in doc.iter() if isinstance(el.tag, str) and el.get("id"))
        ids[rel] = set(seen)
        dup_ids += [(rel, k, n) for k, n in seen.items() if n > 1]
        seg = rel.split("/")[0]
        langs[rel] = seg if seg in ("ru", "en") else None
        hl = doc.get("lang") if doc.tag == "html" else doc.getroottree().getroot().get("lang")
        if langs[rel] and hl != langs[rel]:
            lang_bad.append((rel, hl))
    print(f"G10: {len(pages)} HTML pages under {OUT}")
    report("g10_duplicate_ids", dup_ids, ["page", "id", "count"])
    result("ids", not dup_ids and not lang_bad, f"{len(dup_ids)} duplicate ids, {len(lang_bad)} pages with a wrong lang")

    # ---------------------------------------------------------------- counts
    data = {k: rjson(OUT / "data" / f"{k}.json") for k in ("talks", "items", "problems", "references", "records", "years")}
    src = {}
    for t in tags:
        d = YEARS_DIR / t
        keys = bib_keys(d / f"{t}_references.bib")
        src[t] = {"talks": len(json.loads((d / f"{t}_talks.json").read_text(encoding="utf-8"))),
                  "items": len(json.loads((d / f"{t}_items.json").read_text(encoding="utf-8"))),
                  "problems": len(json.loads((d / f"{t}_problems.json").read_text(encoding="utf-8"))),
                  "references": len(set(keys)), "bib_entries": len(keys)}
    dat = collections.defaultdict(collections.Counter)
    for k in ("talks", "items", "problems"):
        for r in data[k]:
            dat[r["chapter"]][k] += 1
    for r in data["references"]:
        for t in r["chapters"]:
            dat[t]["references"] += 1
    rend = {l: collections.defaultdict(collections.Counter) for l in ("ru", "en")}
    ref_unique = {}
    for rel, (s, doc) in docs.items():
        l = langs[rel]
        if not l:
            continue
        kind = rel.split("/")[1] if "/" in rel else ""
        if kind == "talks":
            for el in doc.find_class("entry"):
                rend[l][work_tag.get(el.get("data-work"))]["talks"] += 1
            for el in doc.find_class("item"):
                if el.tag == "section":
                    rend[l][work_tag.get(el.get("data-work"))]["items"] += 1
        elif kind == "problems" and rel.count("/") == 3:
            for el in doc.xpath("//details[@data-work]"):
                rend[l][work_tag.get(el.get("data-work"))]["problems"] += 1
        elif kind == "references":
            refs = doc.xpath("//div[@class='ref']")
            ref_unique[l] = len(refs)
            for el in refs:
                for t in (el.get("data-chapters") or "").split():
                    rend[l][t]["references"] += 1
    rows, bad = [], []
    tot = collections.Counter()
    for t in tags:
        for k in ("talks", "items", "problems", "references"):
            vals = (src[t][k], dat[t][k], rend["en"][t][k], rend["ru"][t][k])
            tot[(k, "src")] += vals[0]
            tot[(k, "data")] += vals[1]
            tot[(k, "en")] += vals[2]
            tot[(k, "ru")] += vals[3]
            rows.append((t, k) + vals + (src[t]["bib_entries"] if k == "references" else "",))
            if len(set(vals)) != 1:
                bad.append((t, k) + vals)
    report("g10_counts", rows, ["chapter", "what", "source", "data files", "pages en", "pages ru", "bib entries"])
    n_keys = len(data["references"])
    summary = "; ".join(f"{k} {tot[(k, 'src')]}/{tot[(k, 'data')]}/{tot[(k, 'en')]}/{tot[(k, 'ru')]}"
                        for k in ("talks", "items", "problems", "references"))
    result("counts", not bad and ref_unique.get("en") == n_keys == ref_unique.get("ru"),
           f"source/data/en/ru per chapter, summed: {summary}; distinct references {n_keys} (pages en "
           f"{ref_unique.get('en')}, ru {ref_unique.get('ru')}); {len(bad)} chapter rows differ")

    # ---------------------------------------------------------------- citations, placeholders, LaTeX outside math
    undefined, leftovers, latex = [], [], []
    tex = re.compile(r"\\[A-Za-z]+|\\[()\[\]]|(?<![\w\\])\$[^$\s][^$]{0,80}\$")
    for rel, (s, doc) in docs.items():
        for m in re.finditer(r'<span class="citation"[^>]*>(?:(?!</span>).)*?<strong>([^<]*\?)</strong>', s, re.S):
            undefined.append((rel, m.group(1)))
        for m in re.finditer(r"@@[A-Z]+@@|QQ[A-Z]+\d*QQ|QQFIELD", s):
            leftovers.append((rel, m.group(0)))
        body = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", s, flags=re.S)
        body = re.sub(r'<span class="math (?:inline|display)">.*?</span>', " ", body, flags=re.S)
        text = H.unescape(re.sub(r"<[^>]+>", " ", body))
        for m in tex.finditer(text):
            latex.append((rel, m.group(0), text[max(0, m.start() - 50):m.end() + 30].replace("\n", " ")))
    report("g10_undefined_citations", undefined, ["page", "marker"])
    report("g10_leftover_placeholders", leftovers, ["page", "text"])
    report("g10_latex_outside_math", latex, ["page", "match", "context"])
    result("citations", not undefined and not leftovers,
           f"{len(undefined)} undefined citation markers, {len(leftovers)} leftover placeholders")
    lc = collections.Counter(m for _, m, _ in latex)
    result("latex", not latex, f"{len(latex)} TeX fragments outside math"
           + (f" (most common: {', '.join(f'{k} x{v}' for k, v in lc.most_common(8))})" if latex else ""))

    # ---------------------------------------------------------------- links
    pdfmax = {}
    for f in (OUT / "readers").glob("*.pdf"):
        pdfmax[f.name] = pdf_pages(f)
    broken = []
    n_links = 0
    for rel, (s, doc) in docs.items():
        for el, attr, link, _pos in doc.iterlinks():
            if attr not in ("href", "src", "action") or not link:
                continue
            if re.match(r"^(?:https?:|mailto:|data:|javascript:)", link):
                continue
            n_links += 1
            if link.startswith("#"):
                if link[1:] and H.unescape(link[1:]) not in ids[rel]:
                    broken.append((rel, link, "anchor missing on this page"))
                continue
            if not link.startswith(BASE):
                broken.append((rel, link, "not under the base path"))
                continue
            path, _, frag = link[len(BASE):].partition("#")
            path = path.split("?")[0]
            if path == "" or path.endswith("/"):
                path += "index.html"
            target = OUT / path
            if not target.exists():
                broken.append((rel, link, "no such file"))
                continue
            if frag:
                if path.endswith(".pdf"):
                    m = re.fullmatch(r"page=(\d+)", frag)
                    mx = pdfmax.get(Path(path).name)
                    if not m or (mx and not 1 <= int(m.group(1)) <= mx):
                        broken.append((rel, link, f"PDF page outside 1..{mx}"))
                elif path in ids and frag not in ids[path]:
                    broken.append((rel, link, "anchor missing on the target page"))
    report("g10_broken_links", broken, ["page", "link", "problem"])
    bk = collections.Counter(p for _, _, p in broken)
    result("links", not broken, f"{n_links} inside links checked, {len(broken)} broken"
           + (f" ({dict(bk)})" if broken else "") + f"; reader PDFs: {pdfmax}")

    # ---------------------------------------------------------------- coverage
    missing = []
    for l in ("ru", "en"):
        for r in data["records"]:
            if f"{l}/talks/{r['record']}/index.html" not in docs:
                missing.append((l, "record", r["record"]))
        for y in data["years"]:
            if f"{l}/years/{y['year']}/index.html" not in docs:
                missing.append((l, "year", y["year"]))
        for pr in {r["id"] for r in data["problems"]}:
            if f"{l}/problems/{pr}/index.html" not in docs:
                missing.append((l, "problem", pr))
    report("g10_missing_pages", missing, ["lang", "kind", "id"])
    result("coverage", not missing, f"{len(data['records'])} records, {len(data['years'])} years, "
           f"{len({r['id'] for r in data['problems']})} problems in both languages; {len(missing)} pages missing")

    # ---------------------------------------------------------------- notices
    issues_url = "https://github.com/KokunoYumeto/gelfand-seminar-russian-diplomatic/issues"
    rights = {l: norm(UI[l]["rights"].replace("{issues}", issues_url)) for l in ("ru", "en")}
    notice_bad = []
    for rel, (s, doc) in docs.items():
        if rel.startswith("data/") or rel.startswith("assets/"):
            continue
        st = doc.xpath("//div[@class='status']")
        if len(st) != 1:
            notice_bad.append((rel, f"{len(st)} status lines"))
        rg = [norm(lxml.html.tostring(e, encoding="unicode")) for e in doc.xpath("//p[@class='rights']")]
        want = [langs[rel]] if langs[rel] else ["en", "ru"]
        for l in want:
            if rg.count(rights[l]) != 1:
                notice_bad.append((rel, f"rights statement in {l}: {rg.count(rights[l])}"))
        if len(rg) != len(want):
            notice_bad.append((rel, f"{len(rg)} rights statements"))
    stale = rjson(OUT / "data" / "stale_pages.json")["chapters"]
    stale_set = {t: set(v.get("stale_pages", [])) for t, v in stale.items()}
    item_pages = collections.defaultdict(set)
    for x in data["items"]:
        item_pages[(x["chapter"], str(x["record"]))] |= set(parse_pages(x["pages"]))
    n_stale_items = n_stale_entries = 0
    for x in data["items"]:
        if not x["stale_pages"]:
            continue
        n_stale_items += 1
        for l in ("ru", "en"):
            s, doc = docs[f"{l}/talks/{x['record']}/index.html"]
            sec = doc.xpath(f"//section[@id='{x['id']}']")
            if not sec or not sec[0].xpath(".//span[contains(@class,'warn')]"):
                notice_bad.append((f"{l}/talks/{x['record']}/", f"item {x['id']} without its revised-text badge"))
    for tk in data["talks"]:
        t, n = tk["chapter"], str(tk["record"])
        ps = (set(parse_pages(tk["pages"])) | item_pages[(t, n)]) & stale_set.get(t, set())
        if not ps:
            continue
        n_stale_entries += 1
        for l in ("ru", "en"):
            s, doc = docs[f"{l}/talks/{n}/index.html"]
            sec = doc.xpath(f"//section[@class='entry'][@data-work='{tk['work']}']")
            if not sec or not sec[0].xpath(".//div[contains(@class,'stale')]"):
                notice_bad.append((f"{l}/talks/{n}/", f"entry of {t} without the revised-text notice"))
    chapter_of_year = {y["year"]: y["chapter"] for y in data["years"]}
    stub_words = {"en": "<strong>Stub.</strong>", "ru": "<strong>Заготовка.</strong>"}
    for l in ("ru", "en"):
        for y, t in chapter_of_year.items():
            s, doc = docs[f"{l}/years/{y}/index.html"]
            if t and stale_set.get(t) and not doc.xpath("//div[contains(@class,'notice') and contains(@class,'stale')]"):
                notice_bad.append((f"{l}/years/{y}/", "year without the revised-text summary"))
            if bool(t) == (stub_words[l] in s):
                notice_bad.append((f"{l}/years/{y}/", "stub notice " + ("on a year with a companion" if t else "missing")))
        for r in data["records"]:
            s, doc = docs[f"{l}/talks/{r['record']}/index.html"]
            has_ch = bool(chapter_of_year.get(r["academic_year"])) or bool(r["chapters"])
            if has_ch == (stub_words[l] in s):
                notice_bad.append((f"{l}/talks/{r['record']}/", "stub notice " + ("with a companion" if has_ch else "missing")))
            if l == "ru" and r["chapters"] and "notice lang" not in s:
                notice_bad.append((f"ru/talks/{r['record']}/", "no commentary-language notice"))
    report("g10_notices", notice_bad, ["page", "problem"])
    result("notices", not notice_bad, f"status line and rights statement on {len(docs)} pages; revised-text notices on "
           f"{n_stale_entries} talk entries and {n_stale_items} items (both languages); stubs and language notices; "
           f"{len(notice_bad)} problems")

    # ---------------------------------------------------------------- notebook text (G3, G4)
    nb_ir = IR / "notebook"
    if (nb_ir / "ru.json").exists():
        reg = rjson(IR / "registry.json")
        nb_bad, cnt = [], collections.Counter()
        for l in ("ru", "en"):
            ir = rjson(nb_ir / f"{l}.json")
            for ch, plist in reg["archive_chapters"].items():
                rel = f"{l}/notebook/{ch}/index.html"
                if rel not in docs:
                    nb_bad.append((l, f"chapter {ch}", "no notebook page"))
                    continue
                s, doc = docs[rel]
                for p in plist:
                    key = f"P{int(p):06d}"
                    if key not in ids[rel]:
                        nb_bad.append((l, key, f"no anchor on {rel}"))
                    if not (OUT / "data" / "pages" / l / f"{key}.json").exists():
                        nb_bad.append((l, key, "no page shard"))
                cnt[(l, "pages")] += len(plist)
                cnt[(l, "passages")] += len(doc.xpath("//div[contains(concat(' ',@class,' '),' passage ') and @id]"))
                cnt[(l, "readings")] += len(doc.xpath("//*[contains(concat(' ',@class,' '),' mr ')]"))
                cnt[(l, "figures")] += len(doc.xpath("//*[contains(concat(' ',@class,' '),' fig ')]/img"))
                cnt[(l, "figures missing")] += len(doc.find_class("fig-missing"))
            want_p = sum(len(v["passages"]) for v in ir.values())
            want_r = sum(len(v["readings"]) for v in ir.values())
            if cnt[(l, "passages")] != want_p:
                nb_bad.append((l, "passages", f"{cnt[(l, 'passages')]} on the pages, {want_p} in G3"))
            if cnt[(l, "readings")] != want_r:
                nb_bad.append((l, "marked readings", f"{cnt[(l, 'readings')]} on the pages, {want_r} in G3"))
        parity = REPORTS / "g3_parity.tsv"
        n_par = max(0, len(parity.read_text(encoding="utf-8").splitlines()) - 1) if parity.exists() else -1
        if n_par != 0:
            nb_bad.append(("ru/en", "parity", f"{n_par} differences in reports/g3_parity.tsv"))
        failed = REPORTS / "g4_failed.tsv"
        n_fail = max(0, len(failed.read_text(encoding="utf-8").splitlines()) - 1) if failed.exists() else -1
        report("g10_notebook", nb_bad, ["lang", "what", "problem"])
        result("notebook", not nb_bad,
               "; ".join(f"{l}: {cnt[(l, 'pages')]} pages, {cnt[(l, 'passages')]} passages, {cnt[(l, 'readings')]} "
                         f"marked readings, {cnt[(l, 'figures')]} figures ({cnt[(l, 'figures missing')]} not typeset)"
                         for l in ("ru", "en"))
               + f"; parity differences {n_par}; figures without SVG {n_fail} (reports/g4_failed.tsv); "
                 f"{len(nb_bad)} problems")

    # ---------------------------------------------------------------- outside links (a sample)
    if os.environ.get("GELFAND_SKIP_OUTSIDE") != "1":
        urls = [r["mccme_url"] for r in data["records"]][::max(1, len(data["records"]) // 25)][:25]
        refs = [(r.get("doi") and "https://doi.org/" + r["doi"]) or r.get("url") for r in data["references"]]
        refs = [x for x in refs if x and x.startswith("http")]
        urls += refs[::max(1, len(refs) // 25)][:25]
        out_rows = []

        def probe(u):
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (compatible; site-link-check/1.0)"})
            try:
                with urllib.request.urlopen(req, timeout=25) as r:
                    return (u, r.status, r.geturl()[:120])
            except urllib.error.HTTPError as e:
                return (u, e.code, "")
            except Exception as e:  # noqa: BLE001
                return (u, "error", str(e)[:120])
        with ThreadPoolExecutor(max_workers=8) as ex:
            out_rows = list(ex.map(probe, urls))
        report("g10_outside_links", out_rows, ["url", "status", "final url or error"])
        gone = [r for r in out_rows if r[1] in (404, 410)]
        errs = [r for r in out_rows if r[1] == "error"]
        refused = [r for r in out_rows if isinstance(r[1], int) and r[1] in (401, 403, 429)]
        okn = [r for r in out_rows if isinstance(r[1], int) and r[1] < 400]
        result("outside", not gone and len(errs) <= 5,
               f"{len(urls)} sampled (MCCME record pages and bibliography DOIs/URLs): {len(okn)} answer, "
               f"{len(refused)} refuse automated clients, {len(gone)} gone, {len(errs)} errors or timeouts")

    # ---------------------------------------------------------------- size
    by_top = collections.Counter()
    n_all = 0
    big = []
    for f in OUT.rglob("*"):
        if f.is_file():
            sz = f.stat().st_size
            top = f.relative_to(OUT).parts[0] if len(f.relative_to(OUT).parts) > 1 else "(root)"
            if top in ("ru", "en") and len(f.relative_to(OUT).parts) > 2:
                top = f"{top}/{f.relative_to(OUT).parts[1]}"
            if top == "assets" and len(f.relative_to(OUT).parts) > 2:
                top = f"assets/{f.relative_to(OUT).parts[1]}"
            by_top[top] += sz
            n_all += 1
            big.append((sz, f.relative_to(OUT).as_posix()))
    total = sum(by_top.values())
    report("g10_size", sorted(((k, v) for k, v in by_top.items()), key=lambda kv: -kv[1])
           + [("TOTAL", total), ("files", n_all)] + [("largest: " + p, s) for s, p in sorted(big, reverse=True)[:15]],
           ["folder", "bytes"])
    result("size", total < 1_000_000_000, f"{total / 1e6:.0f} MB in {n_all} files (GitHub Pages limit 1 GB); largest "
           f"folders: " + ", ".join(f"{k} {v / 1e6:.0f} MB" for k, v in by_top.most_common(5)))

    # ---------------------------------------------------------------- public files
    pat = forbidden_patterns()
    hits = []
    n_files = 0
    vendor_credits = 0
    for f in OUT.rglob("*"):
        if f.is_file() and f.suffix.lower() in TEXT_EXT:
            n_files += 1
            rel_f = "site/" + f.relative_to(OUT).as_posix()
            h = scan_text(f.read_text(encoding="utf-8", errors="replace"), rel_f, pat)
            if rel_f.startswith("site/pagefind/"):
                # Pagefind's generated UI credits its translators by name and e-mail address: third-party text
                keep = [x for x in h if not re.fullmatch(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", x[1])]
                vendor_credits += len(h) - len(keep)
                h = keep
            hits += h
    pub = [REPO / "companion", SB, REPO / ".github"]
    for root in pub:
        if not root.exists():
            continue
        for f in root.rglob("*"):
            relp = f.relative_to(REPO).as_posix()
            if not f.is_file() or "/_work/" in f"/{relp}" or "__pycache__" in relp or f.name == "forbidden_public_terms.txt":
                continue
            if f.suffix.lower() in TEXT_EXT or f.suffix == "":
                n_files += 1
                hits += scan_text(f.read_text(encoding="utf-8", errors="replace"), relp, pat)
    report("g10_public_scan", hits, ["file", "match", "context"])
    result("public", not hits, f"{n_files} files scanned (site and the repository folders this build publishes); "
           f"{len(hits)} hits" + (f" (not counted: {vendor_credits} translator e-mail addresses in Pagefind's own "
                                  f"generated UI script)" if vendor_credits else ""))

    report("g10_summary", RESULTS, ["check", "result", "detail"])
    ok = all(r[1] == "PASS" for r in RESULTS)
    print("G10", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
