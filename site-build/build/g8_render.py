"""G8 render: the pages of the site (design §4-§6) and its data files.

Reads WORK/ir (registry, converted companion fields, links, staleness), the companion data in companion/years, the
works registry and the interface strings; writes WORK/site/.  Works switched off in the registry (or by
GELFAND_EXCLUDE) and records listed in exclude_records are left out of every page, index and data file; links into
them become plain text.

Pages, in Russian (ru) and English (en): home; year (every academic year with records); talk (every catalogue record);
problem index and problem pages; references; speakers; developed questions per chapter; the resolver /r/ and 404.
Base path: GELFAND_BASE (default /gelfand-seminar-russian-diplomatic/).
"""
import collections
import csv
import html as H
import io
import json
import os
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import (ASSETS, DATA, IR, ISSUES_URL, MCCME_LIST, REPO_URL, YEARS_DIR, chapter_tags, fdate, fmt_ranges,
                    latex_dir, lock, log, parse_pages, pid, release_dir, rjson, rtext, sha256_file, site_dir, wjson,
                    work_map, works, wtext, year_label)

E = lambda s: H.escape(str(s if s is not None else ""), quote=True)
BASE = os.environ.get("GELFAND_BASE", "/gelfand-seminar-russian-diplomatic/")
LANGS = ("ru", "en")
UI = rjson(DATA / "ui_strings.json")
ASSET_V = sha256_file(ASSETS / "site.css")[:6] + sha256_file(ASSETS / "site.js")[:6]   # cache key of the assets
READERS = {"ru": "gelfand-russian-chapters01-34-complete-first1527.pdf",
           "en": "gelfand-english-chapters01-34-complete-first1527.pdf"}
KIND_ORDER = ["talk", "plan", "heading", "other"]
# the companion reader (kit/build_global_reader.py --pdf): GELFAND_COMPANION_PDF names the PDF, copied to /readers/;
# GELFAND_COMPANION_RELEASE the tag of the GitHub release that carries the same PDF (linked from the home page)
COMPANION_PDF = "GelfandSeminar_companion.pdf"
COMPANION_PDF_SRC = Path(os.environ["GELFAND_COMPANION_PDF"]) if os.environ.get("GELFAND_COMPANION_PDF") else None
COMPANION_RELEASE = os.environ.get("GELFAND_COMPANION_RELEASE", "")


def pdf_pages(p):
    import subprocess
    r = subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True, encoding="latin-1")
    m = re.search(r"^Pages:\s+(\d+)", r.stdout, re.M)
    return int(m.group(1)) if m else None


def u(lang, key, **kw):
    s = UI[lang].get(key, UI["en"].get(key, key))
    for k, v in kw.items():
        s = s.replace("{" + k + "}", str(v))
    return s


# ------------------------------------------------------------------ load
REG = rjson(IR / "registry.json")
LINKS = rjson(IR / "links.json")
STALE = rjson(IR / "stale_pages.json")
REFS = rjson(IR / "companion" / "references.json")["entries"]
LOCK = lock()
REL = LOCK["release"]
REL_DATE = REL["created_at"][:10]
REL_SHORT = re.sub(r"^readers-a4-\d{4}-\d{2}-\d{2}-frames\d+-\d+-", "", REL["tag"])
WREG = rjson(DATA / "works.json")
WM = work_map(all_=True)
TAGS = chapter_tags()                                   # included chapters
ALL_TAGS = chapter_tags(all_=True)
EXCL_REC = {str(n) for n in (WREG.get("exclude_records") or [])}
NOTES_ON = {l: WM.get(f"notes-{l}", {}).get("include", True) for l in LANGS}
CH = {t: REG["chapters"][t] for t in TAGS}
COMP = {t: rjson(IR / "companion" / f"{t}.json") for t in TAGS}
RAW = {}
for t in TAGS:
    d = YEARS_DIR / t
    RAW[t] = {k: json.loads((d / f"{t}_{k}.json").read_text(encoding="utf-8")) for k in ("talks", "items", "problems")}
RECS = {n: r for n, r in REG["records"].items() if n not in EXCL_REC}
ITEMS = {}          # id -> raw item with chapter
for t in TAGS:
    for x in RAW[t]["items"]:
        if str(x["record"]) in EXCL_REC:
            continue
        ITEMS[x["id"]] = dict(x, chapter=t)
ENTRIES = collections.defaultdict(list)   # record -> [(tag, talk entry)]
for t in TAGS:
    for tk in RAW[t]["talks"]:
        if str(tk["record"]) in EXCL_REC:
            continue
        ENTRIES[str(tk["record"])].append((t, tk))
REC_ITEMS = collections.defaultdict(list)
for iid, x in ITEMS.items():
    REC_ITEMS[(x["chapter"], str(x["record"]))].append(iid)
PROBLEMS = {}       # merged, included chapters only
for t in TAGS:
    for p in RAW[t]["problems"]:
        PROBLEMS.setdefault(p["id"], []).append(dict(p, chapter=t))
YEARS = [y for y in REG["years"] if any(str(n) in RECS for n in y["records"])]
YEAR_OF = {n: r["year"] for n, r in RECS.items()}
STALE_SET = {t: set(STALE["chapters"].get(t, {}).get("stale_pages", [])) for t in TAGS}
STALE_WHAT = {t: STALE["chapters"].get(t, {}).get("what_changed", {}) for t in TAGS}
PAGE_ITEMS = collections.defaultdict(list)
for iid, x in ITEMS.items():
    for p in parse_pages(x.get("pages")):
        PAGE_ITEMS[p].append(iid)
REMOVED_ITEMS = set()
for t in ALL_TAGS:
    if t in TAGS:
        continue
    for x in json.loads((YEARS_DIR / t / f"{t}_items.json").read_text(encoding="utf-8")):
        REMOVED_ITEMS.add(x["id"])
for t in TAGS:
    for x in RAW[t]["items"]:
        if str(x["record"]) in EXCL_REC:
            REMOVED_ITEMS.add(x["id"])


def slug(tag):
    ys = CH[tag]["years"] if tag in CH else REG["chapters"][tag]["years"]
    return ys[0] if len(ys) == 1 else f"{ys[0][:4]}-{ys[-1][-2:]}"


def years_text(lang, ys):
    ys = [year_label(y) for y in ys]
    return ys[0] if len(ys) == 1 else (" and " if lang == "en" else " и ").join(ys)


CHAPTER_OF_YEAR = {}
for t in TAGS:
    for y in CH[t]["years"]:
        CHAPTER_OF_YEAR[y] = t


BADGE_IN_MATH = re.compile(r'(<span class="math (?:inline|display)">(?:(?!</span>).)*?)(<span class="badge ours">[^<]*</span>)'
                           r'((?:(?!</span>).)*?</span>)', re.S)


def unbadge_math(html):
    """A "proved here" / "computed here" mark written inside a formula is moved after the formula (HTML inside the TeX
    would stop MathJax from typesetting it)."""
    prev = None
    while prev != html:
        prev = html
        html = BADGE_IN_MATH.sub(r"\1\3 \2", html)
    return html


def number_equations(html):
    """Give each labelled displayed equation of a development text a number (\\tag) and an anchor; returns the new
    HTML and {label: number}."""
    eq = {}

    def disp(m):
        inner = m.group(1)
        labels = re.findall(r"\\label\{([^}]+)\}", inner)
        if not labels:
            return m.group(0)
        if "\\tag" not in inner:
            def addtag(mm):
                lab = mm.group(1)
                eq.setdefault(lab, len(eq) + 1)
                return f"\\tag{{{eq[lab]}}}\\label{{{lab}}}"
            inner = re.sub(r"\\label\{([^}]+)\}", addtag, inner)
        return ("".join(f'<span id="{E(l)}" class="eqanchor"></span>' for l in labels)
                + f'<span class="math display">{inner}</span>')
    return re.sub(r'<span class="math display">((?:(?!</span>).)*?)</span>', disp, html, flags=re.S), eq


def number_sections(html):
    """Number the developed questions (the h2 headings) of a development text; returns the new HTML and {id: n}."""
    sec, n = {}, 0

    def h2(m):
        nonlocal n
        attrs, inner = m.group(1), m.group(2)
        if "unnumbered" in attrs:
            return m.group(0)
        n += 1
        mm = re.search(r'id="([^"]+)"', attrs)
        if mm:
            sec[H.unescape(mm.group(1))] = n
        return f'<h2{attrs}><span class="secno">{n}</span> {inner}</h2>'
    return re.sub(r"<h2([^>]*)>(.*?)</h2>", h2, html, flags=re.S), sec


EQNUM, SECNUM = {}, {}
for t in TAGS:
    _dev, EQNUM[t] = number_equations(unbadge_math(COMP[t].get("development") or ""))
    COMP[t]["development"], SECNUM[t] = number_sections(_dev)


# ------------------------------------------------------------------ urls
def url(lang, *parts, anchor=None):
    s = BASE + lang + "/" + "".join(f"{p}/" for p in parts)
    return s + (f"#{anchor}" if anchor else "")


def talk_url(lang, n, anchor=None):
    return url(lang, "talks", n, anchor=anchor)


def item_url(lang, iid):
    x = ITEMS.get(iid)
    return talk_url(lang, x["record"], anchor=iid) if x else None


def page_url(lang, p, here=()):
    """Link to notebook page p: the anchor on this page when the page is listed here, else the anchor on the talk page
    of the first record whose catalogue window holds it."""
    p = int(p)
    if p in here:
        return f"#{pid(p)}"
    recs = [r for r in REG["pages"].get(str(p), {}).get("records", []) if str(r) in RECS]
    return talk_url(lang, recs[0], anchor=pid(p)) if recs else None


def fill(lang, html, tag=None, here=()):
    """Resolve the placeholders of the converted companion HTML for a page in `lang`: references, talks, problems,
    the chapter's developed questions, and the notebook pages and items named in the text (resolved here, at build
    time, to their pages).  Links to removed or missing targets become plain text.  Cross-references to the
    chapter's numbered equations and sections show those numbers."""
    if not html:
        return ""
    html = unbadge_math(html)
    if tag:
        def reftext(m):
            a, typ, lab, txt = m.group(1), m.group(2), m.group(3), m.group(4)
            if typ == "eqref" and lab in EQNUM.get(tag, {}):
                txt = f"({EQNUM[tag][lab]})"
            elif typ == "ref" and lab in SECNUM.get(tag, {}):
                txt = str(SECNUM[tag][lab])
            return f'{a}data-reference-type="{typ}" data-reference="{lab}">{txt}</a>'
        html = re.sub(r'(<a [^>]*?)data-reference-type="(\w+)" data-reference="([^"]+)">(.*?)</a>', reftext, html,
                      flags=re.S)
    html = html.replace("@@REFS@@", url(lang, "references")).replace("@@TALK@@", BASE + lang + "/talks/")
    html = html.replace("@@PROB@@", BASE + lang + "/problems/")
    if tag:
        html = html.replace("@@DEV@@", url(lang, "development", slug(tag)))

    def rlink(m):
        q = m.group(1)
        if re.fullmatch(r"P\d{6}", q):
            return page_url(lang, int(q[1:]), here) or "@@GONE@@"
        return (item_url(lang, q) if q in ITEMS else None) or "@@GONE@@"
    html = re.sub(r"@@R@@\?([A-Za-z0-9.\-]+)", rlink, html)

    def unlink(m):
        href, inner = m.group(1), m.group(2)
        if href == "@@GONE@@":
            return inner
        mm = re.search(r"/talks/(\d+)/(?:#.*)?$", href)
        if mm and mm.group(1) in EXCL_REC:
            return inner
        mm = re.search(r"/problems/([^/#]+)/$", href)
        if mm and mm.group(1) not in PROBLEMS:
            return inner
        return m.group(0)
    return re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', unlink, html, flags=re.S)


# ------------------------------------------------------------------ shell
def head(lang, title, desc="", noindex=False, works_ids=()):
    return (f'<!doctype html>\n<html lang="{lang}"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1"><title>{E(title)}</title>'
            + (f'<meta name="description" content="{E(desc)}">' if desc else "")
            + ('<meta name="robots" content="noindex">' if noindex else "")
            + (f'<meta name="works" content="{E(" ".join(works_ids))}">' if works_ids else "")
            + f'<link rel="icon" href="data:,"><link rel="stylesheet" href="{BASE}assets/site.css?v={ASSET_V}"></head>\n')


def header(lang, crumbs, other):
    cr = '<span class="sep">›</span>'.join(f'<a href="{E(h)}">{E(t)}</a>' if h else E(t) for t, h in crumbs)
    ol = "en" if lang == "ru" else "ru"
    return (f'<header class="top"><a class="site" href="{url(lang)}">{E(UI["site_name"][lang])}</a>'
            f'<nav class="crumbs" aria-label="breadcrumb">{cr}</nav>'
            f'<form class="refbox" id="refbox" role="search"><input name="q" aria-label="{E(u(lang, "refbox_placeholder"))}" '
            f'placeholder="{E(u(lang, "refbox_placeholder"))}"><button type="submit">{E(u(lang, "refbox_go"))}</button>'
            f'<span class="refmsg" aria-live="polite" data-nf="{E(u(lang, "refbox_notfound"))}"></span></form>'
            f'<div class="tools"><a href="{E(other)}" hreflang="{ol}" lang="{ol}">{E(u(lang, "other_language"))}</a>'
            f'<button type="button" id="theme-toggle" title="{E(u(lang, "theme"))}" aria-label="{E(u(lang, "theme"))}">◐</button>'
            f'</div></header>\n')


def status(text):
    return f'<div class="status">{text}</div>\n'


def footer(lang, extra=""):
    return (f'<footer class="bottom"><div class="inner">{extra}<p class="rights">{u(lang, "rights", issues=E(ISSUES_URL))}</p>'
            f'<p>{E(u(lang, "source_repo"))}: <a href="{REPO_URL}">{E(REPO_URL.replace("https://", ""))}</a> · '
            f'<a href="{BASE}data/">{E(u(lang, "data"))}</a></p></div></footer>\n')


MATHJAX_MACROS = {"relax": ""}     # g3_notebook.MJ_DEFINED: formulas using other macros MathJax lacks are figures


def scripts(math=False):
    s = f'<script src="{BASE}assets/site.js?v={ASSET_V}"></script>'
    if math:
        cfg = {"loader": {"load": ["ui/lazy", "[tex]/mathtools", "[tex]/textmacros"]},
               "tex": {"inlineMath": [["\\(", "\\)"]], "displayMath": [["\\[", "\\]"]], "processEnvironments": True,
                       "tags": "none", "packages": {"[+]": ["mathtools", "textmacros"]}, "macros": MATHJAX_MACROS},
               "options": {"lazyMargin": "600px", "menuOptions": {"settings": {"assistiveMml": False}}},
               "chtml": {"fontURL": f"{BASE}assets/mathjax/output/chtml/fonts/woff-v2"}}
        s = (f'<script>window.MathJax={json.dumps(cfg, ensure_ascii=False)};</script>'
             f'<script defer src="{BASE}assets/mathjax/tex-chtml.js"></script>') + s
    return s


def page(lang, title, crumbs, other, stat, body, math=False, desc="", works_ids=(), kind="page", noindex=False,
         footer_extra="", index=True, extra_head=""):
    pf = f' data-pagefind-body data-pagefind-filter="section:{E(u(lang, "section_" + kind))}"' if index else ""
    return (head(lang, title, desc, noindex, works_ids).replace("</head>", extra_head + "</head>")
            + f'<body data-base="{BASE}" data-lang="{lang}" data-page-kind="{kind}">'
            + header(lang, crumbs, other) + status(stat)
            + f'<div class="page"{pf}>{body}</div>'
            + footer(lang, footer_extra) + scripts(math) + "</body></html>\n")


def other_lang(lang):
    return "en" if lang == "ru" else "ru"


# ------------------------------------------------------------------ status lines and notices
def notebook_status(lang):
    key = "status_notebook_both"
    return E(u(lang, key, date=fdate(lang, REL_DATE), release=REL_SHORT))


def companion_status(lang, tag):
    c = CH[tag]
    note = (c.get("note") or {}).get(lang) or (c.get("note") or {}).get("en")   # how the chapter was received
    return E(u(lang, "status_companion", model=c["model"], written=fdate(lang, c["written"]))
             + (" " + note if note else ""))


def general_status(lang):
    ws = sorted({CH[t]["written"] for t in TAGS})
    span = fdate(lang, ws[0]) + (f" – {fdate(lang, ws[-1])}" if ws and ws[-1] != ws[0] else "") if ws else ""
    models = sorted({CH[t]["model"] for t in TAGS}) or [""]
    return E(u(lang, "status_companion_many", model=", ".join(models), written=span,
               notebook=u(lang, "status_notebook_both", date=fdate(lang, REL_DATE), release=REL_SHORT)))


def what_text(lang, cats):
    order = ["text", "notes", "marking", "figures"]
    return ", ".join(u(lang, f"stale_what_{c}") for c in order if c in cats)


def stale_notice(lang, tag, pages):
    st = sorted(set(pages) & STALE_SET.get(tag, set()))
    if not st:
        return ""
    cats = set()
    for p in st:
        cats |= set(STALE_WHAT[tag].get(str(p), []))
    return (f'<div class="notice stale" data-stale-pages="{" ".join(pid(p) for p in st)}">'
            + E(u(lang, "stale", pages=fmt_ranges(st), written=fdate(lang, CH[tag]["written"]), what=what_text(lang, cats),
                  release=REL_SHORT, date=fdate(lang, REL_DATE))) + "</div>")


def lang_notice(lang):
    return f'<p class="notice lang">{E(u(lang, "commentary_lang"))}</p>' if lang == "ru" else ""


# ------------------------------------------------------------------ pieces
def class_badge(lang, c):
    return f'<span class="b cls cls-{E(c)}" title="{E(c)}: {E(u(lang, "class_" + str(c)))}">{E(u(lang, "class"))} {E(c)}</span>'


def item_badges(lang, x, talk_speaker):
    b = [f'<span class="b">{E(x.get("kind"))}</span>', class_badge(lang, x.get("class")),
         f'<span class="b" title="{E(u(lang, "literal_correctness"))}">{E(x.get("literal_correctness"))}</span>',
         f'<span class="b" title="{E(u(lang, "verification"))}">{E(x.get("verification"))}</span>',
         f'<span class="b" title="{E(u(lang, "confidence"))}">{E(u(lang, "confidence")).lower()}: {E(x.get("confidence"))}</span>']
    if x.get("speaker") and x.get("speaker") != talk_speaker:
        b.append(f'<span class="b">{E(u(lang, "said_by"))}: {E(x["speaker"])}</span>')
    if x.get("problem") and x["problem"] in PROBLEMS:
        b.append(f'<span class="b"><a href="{url(lang, "problems", x["problem"])}">{E(x["problem"])}</a></span>')
    if x.get("development") == "developed in this chapter":
        b.append(f'<span class="b"><a href="{url(lang, "development", slug(x["chapter"]))}">{E(u(lang, "go_development"))}</a></span>')
    st = sorted(set(parse_pages(x.get("pages"))) & STALE_SET.get(x["chapter"], set()))
    if st:
        b.append(f'<span class="b warn" title="{E(u(lang, "stale_item", pages=fmt_ranges(st)))}">'
                 f'{E(u(lang, "stale_item", pages=fmt_ranges(st)))}</span>')
    return '<div class="badges">' + " ".join(b) + "</div>"


def page_links(lang, ps, here=()):
    out = []
    for p in ps:
        h = page_url(lang, p, here)
        out.append(f'<a href="{E(h)}">{pid(p)}</a>' if h else pid(p))
    return ", ".join(out)


def item_html(lang, iid, talk_speaker, here=()):
    x = ITEMS[iid]
    t = x["chapter"]
    c = COMP[t]["items"].get(iid, {})
    f = lambda k: fill(lang, c.get(k), t, here)
    ps = parse_pages(x.get("pages"))
    refs = [k for k in (x.get("refs") or []) if k in REFS]
    v_nb = (f'<p class="lbl">{E(u(lang, "pages"))}: {page_links(lang, ps, here) or E(x.get("pages"))}</p>'
            f'<p class="lbl">{E(u(lang, "notes_say"))}</p>{f("notes")}')
    v_st = f'<p class="lbl">{E(u(lang, "statement"))}</p>{f("statement")}'
    if c.get("reconstruction"):
        v_st += f'<div class="recon"><p class="lbl">{E(u(lang, "reconstruction"))}</p>{f("reconstruction")}</div>'
    v_fa = f'<p class="lbl">{E(u(lang, "fate"))}</p>{f("fate")}'
    if refs:
        v_fa += (f'<p class="lbl">{E(u(lang, "cited_works"))}</p><ul class="compact">'
                 + "".join(f'<li><a href="{url(lang, "references", anchor=k)}">{E(k)}</a>'
                           + (f' · <a href="https://doi.org/{E(REFS[k]["doi"])}">doi</a>' if REFS[k].get("doi") else
                              (f' · <a href="{E(REFS[k]["url"])}">url</a>' if REFS[k].get("url") else ""))
                           + "</li>" for k in refs) + "</ul>")
    rows = [("literal_correctness", x.get("literal_correctness")), ("publication_match", x.get("publication_match")),
            ("verification", x.get("verification")), ("confidence", x.get("confidence")),
            ("development_f", x.get("development")), ("class", f'{x.get("class")}: {u("en", "class_" + str(x.get("class")))}')]
    v_ss = (f'<p class="lbl">{E(u(lang, "present_status"))}</p>{f("present_status")}'
            f'<table class="assess">' + "".join(f'<tr><td>{E(u(lang, k))}</td><td>{E(v)}</td></tr>' for k, v in rows if v)
            + "</table>")
    if c.get("worth"):
        v_ss += f'<p class="lbl">{E(u(lang, "worth"))}</p>{f("worth")}'
    if x.get("problem"):
        p = x["problem"]
        v_ss += (f'<p class="lbl">{E(u(lang, "go_problem"))}: '
                 + (f'<a href="{url(lang, "problems", p)}">{E(p)}</a>' if p in PROBLEMS else E(p)) + "</p>")
    views = [("view_notebook", "nb", v_nb), ("view_statement", "st", v_st), ("view_fate", "fa", v_fa),
             ("view_status", "ss", v_ss)]
    det = "".join(f'<details class="view v-{k}"><summary>{E(u(lang, lab))}</summary><div class="body" lang="en">{body}</div></details>'
                  for lab, k, body in views)
    return (f'<section class="item" id="{E(iid)}" data-work="{E(CH[t]["work"])}" data-class="{E(x.get("class"))}">'
            f'<h3><a class="iid" href="#{E(iid)}">{E(iid)}</a><span class="ititle" lang="en">{E(x.get("title"))}</span></h3>'
            + item_badges(lang, x, talk_speaker) + det + "</section>")


def class_counts(iids):
    c = collections.Counter(ITEMS[i].get("class") for i in iids)
    return " ".join(f"{k}{c[k]}" for k in "ABCDEF" if c[k])


def rec_title(lang, n):
    r = RECS[str(n)]
    ents = ENTRIES.get(str(n), [])
    if ents:
        return ents[0][1].get("title") or r.get("label") or ""
    return r.get("label") or ""


def rec_date(n):
    ents = ENTRIES.get(str(n), [])
    if ents and ents[0][1].get("date"):
        return ents[0][1]["date"]
    return RECS[str(n)].get("date") or ""


def rec_speaker(n):
    ents = ENTRIES.get(str(n), [])
    if ents and ents[0][1].get("speaker"):
        return ents[0][1]["speaker"]
    return RECS[str(n)].get("speaker_as_catalogued") or ""


def rec_pages(n):
    ps = set()
    for t, tk in ENTRIES.get(str(n), []):
        ps |= set(parse_pages(tk.get("pages")))
    return sorted(ps) or RECS[str(n)]["pages"]


# ------------------------------------------------------------------ talk page
def reader_link(lang, which, p):
    pg = REG["pages"][str(p)].get("pdf", {}).get(which)
    if not pg or not NOTES_ON[which]:
        return ""
    return (f'<a href="{BASE}readers/{READERS[which]}#page={pg}">{E(u(lang, "reader_" + which))}, '
            f'{E(u(lang, "reader_p", p=pg))}</a>')


def listed_pages(n):
    """(pages the companion gives for the talk, all pages listed in the talk page's notebook column)."""
    talk_pages = set()
    for t, tk in ENTRIES.get(str(n), []):
        talk_pages |= set(parse_pages(tk.get("pages")))
    return talk_pages, sorted(set(RECS[str(n)]["pages"]) | talk_pages)


def notebook_column(lang, n):
    r = RECS[str(n)]
    talk_pages, allp = listed_pages(n)
    here = set(allp)
    out = [f'<h2>{E(u(lang, "notebook_pages"))}</h2><p class="lbl">{E(u(lang, "notebook_col_note"))}</p>'
           f'<p class="lbl">{notebook_status(lang)}</p>']
    if r.get("empty"):
        out.append(f'<p>{E(u(lang, "empty_record"))}</p>')
    corr_by_page = collections.defaultdict(list)
    for t, tk in ENTRIES.get(str(n), []):
        for row in COMP[t]["corrections"]:
            if row.get("type") == "faithful_error":
                for p in parse_pages(row.get("page")):
                    corr_by_page[p].append((t, row))
    for p in allp:
        pg = REG["pages"].get(str(p), {})
        scans = pg.get("scans") or []
        win = "" if (not talk_pages or p in talk_pages) else f' <span class="win">({E(u(lang, "pages_window"))})</span>'
        links = [f'<a href="{nb_url(lang, p)}">{E(u(lang, "nb_text_link"))}</a>'] if nb_on(lang) else []
        links += [f'<a href="{E(s)}">{E(u(lang, "scan"))} ↗</a>' for s in scans[:1]]
        links += [x for x in (reader_link(lang, "ru", p), reader_link(lang, "en", p)) if x]
        its = [i for i in PAGE_ITEMS.get(p, []) if str(ITEMS[i]["record"]) == str(n)]
        others = [i for i in PAGE_ITEMS.get(p, []) if str(ITEMS[i]["record"]) != str(n)]
        rev = []
        for t, tk in ENTRIES.get(str(n), []):
            if p in STALE_SET.get(t, set()):
                rev.append(u(lang, "revised_page", what=what_text(lang, set(STALE_WHAT[t].get(str(p), [])))))
        s = (f'<div class="nbpage" id="{pid(p)}"><h3>{pid(p)}{win}</h3><div>{" · ".join(links)}</div>'
             + ("".join(f'<div class="rev">{E(x)}</div>' for x in sorted(set(rev))))
             + (f'<div>{E(u(lang, "items_on_page"))}: ' + ", ".join(f'<a href="#{E(i)}">{E(i)}</a>' for i in its)
                + (", " if its and others else "")
                + ", ".join(f'<a href="{item_url(lang, i)}">{E(i)}</a>' for i in others[:12]) + "</div>"
                if its or others else "")
             + (f'<details class="nbload" data-src="{BASE}data/pages/{lang}/{pid(p)}.json"><summary>'
                f'{E(u(lang, "nb_show_text"))}</summary><div class="nbtext" lang="{lang}"></div></details>'
                if nb_on(lang) and pid(p) in NB[lang] else ""))
        for t, row in corr_by_page.get(p, []):
            s += (f'<details class="view"><summary>{E(u(lang, "corrections_page"))}</summary><div class="body" lang="en">'
                  f'{fill(lang, row.get("place"), t, here)}<p class="lbl">{E(u(lang, "reads"))}</p>{fill(lang, row.get("transcription_reads"), t, here)}'
                  f'<p class="lbl">{E(u(lang, "should_read"))}</p>{fill(lang, row.get("should_read"), t, here)}'
                  f'<p class="lbl">{E(u(lang, "evidence"))}</p>{fill(lang, row.get("evidence"), t, here)}</div></details>')
        out.append(s + "</div>")
    return "".join(out)


def talk_page(lang, n):
    r = RECS[str(n)]
    ents = ENTRIES.get(str(n), [])
    y = r["year"]
    yt = CHAPTER_OF_YEAR.get(y)
    date = rec_date(n)
    meta = [E(fdate(lang, date)) if date else "", E(rec_speaker(n)),
            f'{E(u(lang, "record"))} {n}',
            f'{E(u(lang, "pages"))} {E(fmt_ranges(rec_pages(n)))}' if rec_pages(n) else "",
            f'<a href="{E(r["url"])}">{E(u(lang, "scans_at"))} ↗</a>']
    title = rec_title(lang, n)
    body = [f'<p class="meta">{" · ".join(m for m in meta if m)}</p><h1 lang="{"en" if ents else "ru"}">{E(title)}</h1>']
    alerts = []
    if r.get("date_fix"):
        fx = r["date_fix"]
        alerts.append(E(u(lang, "date_fix", catalogued=fx["catalogued"], date=fdate(lang, fx["date"]), reason=fx["reason"])))
    cat = r.get("date_as_catalogued")
    if ents and cat and ents[0][1].get("date") and ents[0][1]["date"] != cat and not r.get("date_fix"):
        alerts.append(E(u(lang, "date_differs", catalogued=fdate(lang, cat), date=fdate(lang, ents[0][1]["date"]))))
    beyond = sorted(set(rec_pages(n)) - set(r["pages"])) if ents else []
    if beyond and r["pages"]:
        alerts.append(E(u(lang, "beyond_window", pages=fmt_ranges(beyond))))
    if r.get("empty"):
        alerts.append(E(u(lang, "empty_record")))
    body += [f'<div class="notice">{a}</div>' for a in alerts]
    works_ids = [f"notes-{l}" for l in LANGS if NOTES_ON[l]]
    here = set(listed_pages(n)[1])
    if ents:
        stat = companion_status(lang, ents[0][0])
        main = [lang_notice(lang)]
        for t, tk in ents:
            works_ids.append(CH[t]["work"])
            iids = REC_ITEMS.get((t, str(n)), [])
            pages_t = set(parse_pages(tk.get("pages")))
            for i in iids:
                pages_t |= set(parse_pages(ITEMS[i].get("pages")))
            head_ = (f'<h2>{E(u(lang, "in_chapter", years=years_text(lang, CH[t]["years"])))}</h2>' if len(ents) > 1 else "")
            kind = tk.get("kind") or ""
            main.append(f'<section class="entry" data-work="{E(CH[t]["work"])}">{head_}'
                        + stale_notice(lang, t, pages_t)
                        + (f'<p class="meta">{E(u(lang, "kind_" + kind) if kind else "")} · {E(tk.get("date") or "")} · '
                           f'{E(tk.get("speaker") or "")} · {E(tk.get("pages") or "")}</p>' if len(ents) > 1 else
                           (f'<p class="meta">{E(u(lang, "kind_" + kind))}</p>' if kind and kind != "talk" else ""))
                        + f'<div class="summary" lang="en">{fill(lang, COMP[t]["talks"].get(str(n), {}).get("summary"), t, here)}</div>'
                        + (f'<h2>{E(u(lang, "items"))} ({len(iids)})</h2>' if iids else "")
                        + "".join(item_html(lang, i, tk.get("speaker"), here) for i in iids) + "</section>")
    elif yt:
        stat = companion_status(lang, yt)
        main = [f'<p class="notice">{E(u(lang, "no_entry", label=r.get("label") or ""))}</p>']
    else:
        stat = notebook_status(lang)
        main = [f'<p class="notice">{u(lang, "stub_talk", year=year_label(y))}</p>']
    order = sorted((int(k) for k in RECS), key=int)
    i = order.index(int(n))
    pv = order[i - 1] if i > 0 else None
    nx = order[i + 1] if i + 1 < len(order) else None
    pager = ('<nav class="pager">'
             + (f'<a href="{talk_url(lang, pv)}">← {E(u(lang, "prev"))}: {pv}</a>' if pv else "<span></span>")
             + (f'<a href="{talk_url(lang, nx)}">{E(u(lang, "next"))}: {nx} →</a>' if nx else "<span></span>") + "</nav>")
    body.append(f'<div class="cols"><div>{"".join(main)}{pager}</div><aside data-pagefind-ignore>'
                f'{notebook_column(lang, n)}</aside></div>')
    crumbs = [(u(lang, "years"), url(lang)), (year_label(y), url(lang, "years", y)), (f'{u(lang, "record")} {n}', None)]
    return page(lang, f'{title} — {u(lang, "record")} {n} — {UI["site_name"][lang]}', crumbs, talk_url(other_lang(lang), n),
                stat, "".join(body), math=bool(ents) or nb_on(lang), works_ids=works_ids, kind="talk")


# ------------------------------------------------------------------ year page
def year_page(lang, y):
    yr = next(v for v in YEARS if v["year"] == y)
    t = CHAPTER_OF_YEAR.get(y)
    recs = [n for n in yr["records"] if str(n) in RECS]
    body = [f'<h1>{E(u(lang, "year_title", year=year_label(y)))}</h1>']
    if t:
        c = CH[t]
        stat = companion_status(lang, t)
        chap_iids = [i for i, x in ITEMS.items() if x["chapter"] == t]
        stl = STALE["chapters"].get(t, {})
        body.append(f'<p class="meta">{E(u(lang, "chapter_written", years=years_text(lang, c["years"]), written=fdate(lang, c["written"])))}'
                    f' · <a href="{url(lang, "development", slug(t))}">{E(u(lang, "development"))}</a></p>')
        n_st, m_st = len(stl.get("stale_pages", [])), len(stl.get("pages", []))
        body.append(f'<div class="notice{" stale" if n_st else ""}">'
                    + E(u(lang, "stale_year" if n_st else "stale_none_year", n=n_st, m=m_st, written=fdate(lang, c["written"])))
                    + "</div>")
        body.append(lang_notice(lang))
        body.append(f'<div class="overview" lang="en">{fill(lang, COMP[t]["overview"], t)}</div>')
        cc = collections.Counter(ITEMS[i].get("class") for i in chap_iids)
        body.append(f'<h2>{E(u(lang, "items_by_class"))}</h2><table class="list" style="width:auto"><tr>'
                    + "".join(f'<th class="num" title="{E(u(lang, "class_" + k))}">{k}</th>' for k in "ABCDEF")
                    + f'<th class="num">{E(u(lang, "total"))}</th></tr><tr>'
                    + "".join(f'<td class="num">{cc[k]}</td>' for k in "ABCDEF") + f'<td class="num">{len(chap_iids)}</td></tr></table>'
                    + f'<p class="lbl">{E(u(lang, "class_legend"))}</p>')
    else:
        stat = notebook_status(lang)
        body.append(f'<p class="notice">{u(lang, "stub_year", year=year_label(y))}</p>')
    rows = []
    for n in recs:
        r = RECS[str(n)]
        iids = [i for (tt, nn), ids in REC_ITEMS.items() if nn == str(n) for i in ids]
        kind = ENTRIES[str(n)][0][1].get("kind") if ENTRIES.get(str(n)) else r.get("association_kind")
        rows.append(f'<tr><td class="nowrap">{E(fdate(lang, rec_date(n)))}</td><td>{E(rec_speaker(n))}</td>'
                    f'<td><a href="{talk_url(lang, n)}">{E(rec_title(lang, n))}</a>'
                    + (f' <span class="lbl">({E(u(lang, "kind_" + kind))})</span>' if kind and kind != "talk" else "")
                    + f'</td><td class="num"><a href="{talk_url(lang, n)}">{n}</a></td>'
                    f'<td class="hide-sm nowrap">{E(fmt_ranges(rec_pages(n)))}</td><td class="num">{len(iids) or ""}</td>'
                    f'<td class="hide-sm">{E(class_counts(iids))}</td></tr>')
    body.append(f'<h2>{E(u(lang, "all_talks", year=year_label(y)))}</h2><table class="list"><tr><th>{E(u(lang, "date"))}</th>'
                f'<th>{E(u(lang, "speaker"))}</th><th>{E(u(lang, "title"))}</th><th class="num">{E(u(lang, "record"))}</th>'
                f'<th class="hide-sm">{E(u(lang, "pages"))}</th><th class="num">{E(u(lang, "items"))}</th>'
                f'<th class="hide-sm">{E(u(lang, "classes"))}</th></tr>' + "".join(rows) + "</table>")
    if t:
        extra = [n for n in yr.get("chapter_records_from_other_years", []) if str(n) in RECS and
                 any(tt == t for tt, _ in ENTRIES.get(str(n), []))]
        if extra:
            body.append(f'<p class="lbl">{E(u(lang, "talk_records_other_years"))}: '
                        + ", ".join(f'<a href="{talk_url(lang, n)}">{n}</a> ({E(rec_title(lang, n))})' for n in extra) + "</p>")
        probs = [p for p, ents in PROBLEMS.items() if any(e["chapter"] == t for e in ents)]
        if probs:
            body.append(f'<h2>{E(u(lang, "problems_of_year"))}</h2><ul class="compact">'
                        + "".join(f'<li><a href="{url(lang, "problems", p)}">{E(p)}</a> <span lang="en">{E(problem_title(p))}</span></li>'
                                  for p in sorted(probs)) + "</ul>")
    if yr["pages"]:
        p0 = yr["pages"][0]
        body.append(f'<h2>{E(u(lang, "readers"))}</h2><p>' + " · ".join(x for x in (reader_link(lang, "ru", p0), reader_link(lang, "en", p0)) if x) + "</p>")
    ylist = [v["year"] for v in YEARS]
    i = ylist.index(y)
    body.append('<nav class="pager">' + (f'<a href="{url(lang, "years", ylist[i - 1])}">← {year_label(ylist[i - 1])}</a>' if i else "<span></span>")
                + (f'<a href="{url(lang, "years", ylist[i + 1])}">{year_label(ylist[i + 1])} →</a>' if i + 1 < len(ylist) else "<span></span>") + "</nav>")
    crumbs = [(u(lang, "years"), url(lang)), (year_label(y), None)]
    wids = [CH[t]["work"]] if t else []
    return page(lang, u(lang, "year_title", year=year_label(y)), crumbs, url(other_lang(lang), "years", y), stat,
                "".join(body), math=bool(t), works_ids=wids, kind="year")


# ------------------------------------------------------------------ problems
def problem_title(p):
    ents = PROBLEMS[p]
    latest = max(ents, key=lambda e: (str(e.get("status_date") or ""), e["chapter"]))
    return latest.get("title") or ""


def first_html(html, n=220):
    """The opening of a converted field, about n characters, as HTML: inline formulas kept whole (as math spans),
    displayed formulas left out, other markup dropped."""
    parts = re.split(r'(<span class="math (?:inline|display)">.*?</span>)', html or "", flags=re.S)
    out, length = [], 0
    for part in parts:
        if part.startswith('<span class="math display">'):
            if out and not out[-1].endswith(" … "):
                out.append(" … ")
            continue
        if part.startswith('<span class="math inline">'):
            tex = H.unescape(re.sub(r"<[^>]+>", "", part))
            if length + len(tex) > n and out:
                return "".join(out).rstrip() + " …"
            out.append(part)
            length += len(tex)
            continue
        txt = H.unescape(re.sub(r"<[^>]+>", "", part))
        for w in re.findall(r"\s+|\S+", txt):
            if length + len(w) > n:
                return "".join(out).rstrip() + " …"
            out.append(E(w))
            length += len(w)
    return "".join(out).strip()


def problem_page(lang, p):
    ents = PROBLEMS[p]
    latest = max(ents, key=lambda e: (str(e.get("status_date") or ""), e["chapter"]))
    t = latest["chapter"]
    cm = COMP[t]["problems"].get(p, {})
    occ = []
    for e in ents:
        for o in e.get("occurrences") or []:
            if o not in occ:
                occ.append(o)
    occ_html = []
    for o in occ:
        if o in ITEMS:
            occ_html.append(f'<li><a href="{item_url(lang, o)}">{E(o)}</a> <span lang="en">{E(ITEMS[o].get("title"))}</span></li>')
        else:
            occ_html.append(f'<li>{E(o)} <span class="lbl">({E(u(lang, "pending"))})</span></li>')
    refs = []
    for e in ents:
        for k in e.get("refs") or []:
            if k in REFS and k not in refs:
                refs.append(k)
    body = [f'<h1><span class="lbl">{E(p)}</span><br><span lang="en">{E(latest.get("title"))}</span></h1>', lang_notice(lang),
            f'<div lang="en"><p class="lbl">{E(u(lang, "statement"))}</p>{fill(lang, cm.get("statement"), t)}'
            f'<p class="lbl">{E(u(lang, "status_as_of", date=latest.get("status_date") or ""))}</p>{fill(lang, cm.get("status"), t)}</div>',
            f'<h2>{E(u(lang, "occurrences"))}</h2><ul class="compact">{"".join(occ_html)}</ul>']
    if refs:
        body.append(f'<h2>{E(u(lang, "cited_works"))}</h2><ul class="compact">'
                    + "".join(f'<li><a href="{url(lang, "references", anchor=k)}">{E(k)}</a></li>' for k in refs) + "</ul>")
    body.append(f'<h2>{E(u(lang, "entries_by_chapter"))}</h2>')
    for e in ents:
        c2 = COMP[e["chapter"]]["problems"].get(p, {})
        body.append(f'<details class="view" data-work="{E(CH[e["chapter"]]["work"])}"><summary>{E(u(lang, "in_chapter", years=years_text(lang, CH[e["chapter"]]["years"])))}'
                    f' — {E(e.get("status_date") or "")}</summary><div class="body" lang="en"><p><strong>{E(e.get("title"))}</strong></p>'
                    f'{fill(lang, c2.get("statement"), e["chapter"])}<p class="lbl">{E(u(lang, "status_as_of", date=e.get("status_date") or ""))}</p>'
                    f'{fill(lang, c2.get("status"), e["chapter"])}<p class="lbl">{E(u(lang, "occurrences"))}: {E(", ".join(e.get("occurrences") or []))}</p></div></details>')
    crumbs = [(u(lang, "problems"), url(lang, "problems")), (p, None)]
    return page(lang, f'{p}: {latest.get("title")} — {UI["site_name"][lang]}', crumbs, url(other_lang(lang), "problems", p),
                companion_status(lang, t), "".join(body), math=True, works_ids=[CH[e["chapter"]]["work"] for e in ents],
                kind="problem")


def problems_index(lang):
    rows = []
    for p in sorted(PROBLEMS, key=lambda s: (int(s.split("-")[1]), int(s.split("-")[2]) if s.split("-")[2].isdigit() else 0)):
        ents = PROBLEMS[p]
        latest = max(ents, key=lambda e: (str(e.get("status_date") or ""), e["chapter"]))
        occ_years = sorted({o.split("-")[0] for e in ents for o in (e.get("occurrences") or [])})
        st = first_html(COMP[latest["chapter"]]["problems"].get(p, {}).get("status"))
        rows.append(f'<tr><td class="nowrap"><a href="{url(lang, "problems", p)}">{E(p)}</a></td><td lang="en">{E(latest.get("title"))}</td>'
                    f'<td class="hide-sm">{E(", ".join(occ_years))}</td><td class="nowrap hide-sm">{E(latest.get("status_date") or "")}</td>'
                    f'<td class="hide-sm" lang="en">{st}</td></tr>')
    body = (f'<h1>{E(u(lang, "problems"))}</h1><p>{E(u(lang, "problems_index_text"))}</p>{lang_notice(lang)}<table class="list"><tr>'
            f'<th>{E(u(lang, "problem"))}</th><th>{E(u(lang, "title"))}</th><th class="hide-sm">{E(u(lang, "years_col"))}</th>'
            f'<th class="hide-sm">{E(u(lang, "status_date"))}</th><th class="hide-sm">{E(u(lang, "first_status"))}</th></tr>'
            + "".join(rows) + "</table>")
    return page(lang, f'{u(lang, "problems")} — {UI["site_name"][lang]}', [(u(lang, "problems"), None)],
                url(other_lang(lang), "problems"), general_status(lang), body, math=True, kind="index")


# ------------------------------------------------------------------ references
REF_ITEMS = collections.defaultdict(list)
for iid, x in ITEMS.items():
    for k in x.get("refs") or []:
        REF_ITEMS[k].append(iid)
REF_PROBS = collections.defaultdict(list)
for p, ents in PROBLEMS.items():
    for e in ents:
        for k in e.get("refs") or []:
            if p not in REF_PROBS[k]:
                REF_PROBS[k].append(p)


def ref_shown(k):
    return any(t in TAGS for t in REFS[k].get("chapters", []))


def sort_key_ref(k):
    s = re.sub(r"<[^>]+>", "", REFS[k].get("html") or k)
    return H.unescape(s).lower()


def references_page(lang):
    keys = sorted((k for k in REFS if ref_shown(k)), key=sort_key_ref)
    out = []
    for k in keys:
        e = REFS[k]
        chs = [t for t in e.get("chapters", []) if t in TAGS]
        its = REF_ITEMS.get(k, [])
        pr = [p for p in REF_PROBS.get(k, []) if p in PROBLEMS]
        note = (e.get("note") or "").strip().lower()
        nt = u(lang, "verified") if note.startswith("verified") else (u(lang, "unverified") if note.startswith("unverified") else "")
        meta = [f'<a href="#{E(k)}">{E(k)}</a>']
        if nt:
            meta.append(E(nt))
        meta.append(E(u(lang, "chapters_col")) + ": " + ", ".join(f'<a href="{url(lang, "years", CH[t]["years"][0])}">{E(years_text("en", CH[t]["years"]))}</a>' for t in chs))
        if its or pr:
            meta.append(E(u(lang, "cited_by")) + ": " + ", ".join([f'<a href="{item_url(lang, i)}">{E(i)}</a>' for i in its]
                                                                  + [f'<a href="{url(lang, "problems", p)}">{E(p)}</a>' for p in pr]))
        out.append(f'<div class="ref" id="{E(k)}" lang="en" data-chapters="{" ".join(chs)}">{fill(lang, e.get("html"))}'
                   f'<span class="refmeta">{" · ".join(meta)}</span></div>')
    body = (f'<h1>{E(u(lang, "references"))}</h1><p>{E(u(lang, "references_text", n=len(keys)))}</p>'
            f'<div class="refs">{"".join(out)}</div>')
    return page(lang, f'{u(lang, "references")} — {UI["site_name"][lang]}', [(u(lang, "references"), None)],
                url(other_lang(lang), "references"), general_status(lang), body, math=True, kind="index"), len(keys)


# ------------------------------------------------------------------ speakers
def speaker_key(s):
    return re.sub(r"[^a-zа-яё]", "", (s or "").lower())


def speakers_page(lang):
    groups = collections.defaultdict(list)
    names = collections.defaultdict(collections.Counter)
    for n in sorted(RECS, key=int):
        r = RECS[n]
        sp = rec_speaker(n)
        if not sp:
            continue
        for part in re.split(r"\s*(?:;|,\s*(?=[A-ZА-Я]\.)|\band\b)\s*", sp):
            part = part.strip().rstrip(".")
            if len(speaker_key(part)) < 3:
                continue
            k = speaker_key(part)
            groups[k].append(n)
            names[k][part] += 1
    order = sorted(groups, key=lambda k: names[k].most_common(1)[0][0].split()[-1].lower())
    out = []
    for k in order:
        nm = names[k].most_common(1)[0][0]
        rows = "".join(f'<li>{E(fdate(lang, rec_date(n)))} · <a href="{talk_url(lang, n)}">{E(rec_title(lang, n))}</a> '
                       f'<span class="lbl">({E(u(lang, "record"))} {n})</span></li>' for n in groups[k])
        out.append(f'<h3 id="{E(k)}">{E(nm)} <span class="lbl">({len(groups[k])})</span></h3><ul class="compact">{rows}</ul>')
    body = f'<h1>{E(u(lang, "speakers"))}</h1><p>{E(u(lang, "speaker_index_text"))}</p>' + "".join(out)
    return page(lang, f'{u(lang, "speakers")} — {UI["site_name"][lang]}', [(u(lang, "speakers"), None)],
                url(other_lang(lang), "speakers"), general_status(lang), body, kind="index"), {k: k for k in groups}


# ------------------------------------------------------------------ development
def development_page(lang, t):
    c = CH[t]
    body = (f'<h1>{E(u(lang, "development_title", years=years_text(lang, c["years"])))}</h1>{lang_notice(lang)}'
            f'<p class="meta"><a href="{url(lang, "years", c["years"][0])}">{E(u(lang, "year_title", year=years_text(lang, c["years"])))}</a></p>'
            f'<div class="development" lang="en">{fill(lang, COMP[t]["development"], t)}</div>')
    crumbs = [(u(lang, "years"), url(lang)), (year_label(c["years"][0]), url(lang, "years", c["years"][0])),
              (u(lang, "development"), None)]
    return page(lang, f'{u(lang, "development_title", years=years_text(lang, c["years"]))} — {UI["site_name"][lang]}', crumbs,
                url(other_lang(lang), "development", slug(t)), companion_status(lang, t), body, math=True,
                works_ids=[c["work"]], kind="development")


# ------------------------------------------------------------------ notebook text (G3 pages, G4 figures)
NB_DIR = IR / "notebook"
NB = {l: rjson(NB_DIR / f"{l}.json") for l in LANGS if NOTES_ON[l] and (NB_DIR / f"{l}.json").exists()}
FIGS_BUILT = rjson(NB_DIR / "figures_built.json", {}) if NB else {}
FIG_RE = re.compile(r'<(div|span) class="fig fig-([a-z-]+)" data-fig="([0-9a-f]{16})"></\1>')
INLINE_FIGS = ("math-inline", "tikz-inline")
NB_CHAPTERS = sorted(REG["archive_chapters"], key=int)
CHAPTER_OF_PAGE = {int(p): v["chapter"] for p, v in REG["pages"].items()}


def nb_on(lang):
    return lang in NB


def nb_url(lang, p, anchor=True):
    """The notebook text of page p (a number or 'P000659'), or of a passage 'P000659.2'."""
    s = str(p)
    n = int(re.match(r"P?0*(\d+)", s).group(1))
    return url(lang, "notebook", str(CHAPTER_OF_PAGE[n]), anchor=(s if s.startswith("P") else pid(n)) if anchor else None)


def resolve_nb_html(lang, html, p):
    """Figures to their SVG (or a pointer to the scan and the PDF when one could not be typeset), crops to their files."""
    def fig(m):
        tag, kind, h = m.group(1), m.group(2), m.group(3)
        b = FIGS_BUILT.get(h)
        if b and b[0]:
            w, hh, dp = b
            style = f"width:{w / 11:.3f}em"
            if kind in INLINE_FIGS:
                style += f";height:{hh / 11:.3f}em" + (f";vertical-align:-{(dp + 1.5) / 11:.3f}em" if dp is not None else "")
            return (f'<{tag} class="fig fig-{kind}"><img src="{BASE}assets/figures/{h}.svg" alt="{E(u(lang, "figure_alt"))}" '
                    f'loading="lazy" style="{style}"></{tag}>')
        rl = reader_link(lang, lang, p)
        return f'<span class="fig-missing">[{E(u(lang, "figure_missing"))}{"; " + rl if rl else ""}]</span>'
    html = FIG_RE.sub(fig, html)
    return html.replace("@@CROPS@@", BASE + "assets/crops/")


def nb_page_section(lang, p):
    """One notebook page on its chapter page: header (number, written number, scan, PDF pages, records, items that cite
    it, revision state) and the text."""
    key = pid(p)
    v = NB[lang].get(key) or {"label": "", "html": ""}
    pg = REG["pages"][str(p)]
    head_ = [f'<h2 class="pid" id="{key}">{key}</h2>']
    meta = []
    if v["label"] and v["label"] != "unlabelled":
        meta.append(E(u(lang, "written_number", label=v["label"])))
    meta += [f'<a href="{E(s)}">{E(u(lang, "scan"))} ↗</a>' for s in (pg.get("scans") or [])[:1]]
    meta += [x for x in (reader_link(lang, l, p) for l in LANGS) if x]
    recs = [r for r in pg["records"] if str(r) in RECS]
    rows = [" · ".join(meta)]
    if recs:
        rows.append(f'{E(u(lang, "records_on_page"))}: ' + ", ".join(
            f'<a href="{talk_url(lang, r)}" title="{E(rec_title(lang, r))}">{r}</a>' for r in recs))
    its = [i for i in PAGE_ITEMS.get(p, []) if item_url(lang, i)]
    if its:
        rows.append(f'{E(u(lang, "items_on_page"))}: ' + ", ".join(f'<a href="{item_url(lang, i)}">{E(i)}</a>' for i in its))
    rev = set()
    for t in TAGS:
        if p in STALE_SET.get(t, set()):
            rev |= set(STALE_WHAT[t].get(str(p), []))
    if rev:
        rows.append(f'<span class="rev">{E(u(lang, "nb_revised", what=what_text(lang, rev)))}</span>')
    nbh = "".join(f"<div>{r}</div>" for r in rows if r)
    return (f'<section class="nbp" data-p="{key}">{"".join(head_)}<div class="nbhead" data-pagefind-ignore>{nbh}</div>'
            f'<div class="nbtext" lang="{lang}">{resolve_nb_html(lang, v["html"], p)}</div></section>')


def nb_years(pages):
    ys = sorted({RECS[str(r)]["year"] for p in pages for r in REG["pages"][str(p)]["records"] if str(r) in RECS})
    return ys


def notebook_page(lang, ch):
    pages = REG["archive_chapters"][ch]
    ol = other_lang(lang)
    i = NB_CHAPTERS.index(ch)
    pv = NB_CHAPTERS[i - 1] if i > 0 else None
    nx = NB_CHAPTERS[i + 1] if i + 1 < len(NB_CHAPTERS) else None
    pager = ('<nav class="pager">'
             + (f'<a href="{url(lang, "notebook", pv)}">← {E(u(lang, "nb_chapter", n=pv))}</a>' if pv else "<span></span>")
             + (f'<a href="{url(lang, "notebook", nx)}">{E(u(lang, "nb_chapter", n=nx))} →</a>' if nx else "<span></span>")
             + "</nav>")
    ys = nb_years(pages)
    modes = ""
    if nb_on(ol):
        modes = (f'<div class="nbmodes" role="group" aria-label="{E(u(lang, "nb_mode_label"))}" data-other="{ol}" '
                 f'data-loading="{E(u(lang, "nb_loading"))}" data-pagefind-ignore>'
                 f'<button type="button" data-mode="this" aria-pressed="true">{E(UI["lang_names"][lang])}</button>'
                 f'<button type="button" data-mode="other" aria-pressed="false" lang="{ol}">{E(UI["lang_names"][ol])}</button>'
                 f'<button type="button" data-mode="both" aria-pressed="false">{E(u(lang, "nb_mode_both"))}</button></div>')
    body = (f'<h1>{E(u(lang, "nb_chapter_title", n=ch))}</h1>'
            f'<p class="meta">{E(u(lang, "nb_pages", first=pid(pages[0]), last=pid(pages[-1])))} · '
            + E(u(lang, "nb_years", years=", ".join(year_label(y) for y in ys))) + f'</p>{modes}'
            + "".join(nb_page_section(lang, p) for p in pages) + pager)
    crumbs = [(u(lang, "notebook"), url(lang, "notebook")), (u(lang, "nb_chapter", n=ch), None)]
    return page(lang, f'{u(lang, "nb_chapter_title", n=ch)} — {UI["site_name"][lang]}', crumbs,
                url(ol, "notebook", ch) if nb_on(ol) else url(ol), E(u(lang, "status_notebook", date=fdate(lang, REL_DATE),
                                                                      release=REL_SHORT)),
                body, math=True, works_ids=[f"notes-{lang}"], kind="notebook")


def notebook_index(lang):
    rows = []
    for ch in NB_CHAPTERS:
        pages = REG["archive_chapters"][ch]
        rows.append(f'<tr><td><a href="{url(lang, "notebook", ch)}">{E(u(lang, "nb_chapter", n=ch))}</a></td>'
                    f'<td>{pid(pages[0])}–{pid(pages[-1])} <span class="lbl">({len(pages)})</span></td>'
                    f'<td>{", ".join(year_label(y) for y in nb_years(pages))}</td></tr>')
    body = (f'<h1>{E(u(lang, "notebook"))}</h1><p>{E(u(lang, "notebook_index_text"))}</p>'
            f'<table class="list"><tr><th>{E(u(lang, "nb_chapters_col"))}</th><th>{E(u(lang, "nb_pages_col"))}</th>'
            f'<th>{E(u(lang, "nb_years_col"))}</th></tr>' + "".join(rows) + "</table>")
    return page(lang, f'{u(lang, "notebook")} — {UI["site_name"][lang]}', [(u(lang, "notebook"), None)],
                url(other_lang(lang), "notebook"), E(u(lang, "status_notebook", date=fdate(lang, REL_DATE), release=REL_SHORT)),
                body, kind="notebook-index")


def nb_shards(out):
    """/data/pages/{l}/P000659.json: the text of one page, for the talk pages' notebook column and the other-language
    view of the notebook pages."""
    n = 0
    for lang in NB:
        d = out / "data" / "pages" / lang
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True, exist_ok=True)
        for key, v in NB[lang].items():
            p = int(key[1:])
            wjson(d / f"{key}.json", {"page": key, "label": v["label"], "chapter": CHAPTER_OF_PAGE[p],
                                     "html": resolve_nb_html(lang, v["html"], p)}, indent=None)
            n += 1
    return n


def copy_crops(out):
    """The scan crops the marked readings show (the PNG details of the release's figures/ folder)."""
    dest = out / "assets" / "crops"
    want = set()
    for lang in NB:
        for v in NB[lang].values():
            want |= set(re.findall(r"@@CROPS@@([^\"'\s>]+)", v["html"]))
    src = latex_dir() / "figures"
    dest.mkdir(parents=True, exist_ok=True)
    have = {f.name for f in dest.glob("*")}
    missing = []
    for name in sorted(want):
        f = src / name
        if not f.exists():
            missing.append(name)
            continue
        if name not in have or (dest / name).stat().st_size != f.stat().st_size:
            shutil.copy(f, dest / name)
    for name in have - want:
        (dest / name).unlink()
    if missing:
        log(f"WARNING: {len(missing)} scan crops named in the text are not in the release: {missing[:5]}")
    return len(want) - len(missing), missing


def search_page(lang):
    """Pagefind (G9 builds the index into /pagefind/; one index per language, chosen by the page's lang)."""
    js = (f'<script src="{BASE}pagefind/pagefind-ui.js"></script><script>(function(){{'
          f'var el=document.getElementById("search");'
          f'if(!window.PagefindUI){{el.textContent=el.dataset.na;return;}}'
          f'var ui=new PagefindUI({{element:"#search",showSubResults:true,showImages:false,bundlePath:"{BASE}pagefind/"}});'
          f'var q=new URLSearchParams(location.search).get("q");if(q)ui.triggerSearch(q);}})();</script>')
    body = (f'<h1>{E(u(lang, "search"))}</h1><p>{E(u(lang, "search_text"))}</p>'
            f'<div id="search" data-na="{E(u(lang, "search_unavailable"))}"></div>')
    return page(lang, f'{u(lang, "search")} — {UI["site_name"][lang]}', [(u(lang, "search"), None)], url(other_lang(lang), "search"),
                general_status(lang), body + js, kind="search", index=False,
                extra_head=f'<link rel="stylesheet" href="{BASE}pagefind/pagefind-ui.css">')


# ------------------------------------------------------------------ home, root, resolver, 404
DATA_FILES_LIST = ["items", "talks", "problems", "references", "pages", "records", "corrections"]


def companion_pdf_block(lang):
    if not COMPANION_PDF_SRC:
        return ""
    links = f'<a href="{BASE}readers/{COMPANION_PDF}">{E(u(lang, "companion_pdf_link"))}</a>'
    if COMPANION_RELEASE:
        links += f' · <a href="{REPO_URL}/releases/tag/{E(COMPANION_RELEASE)}">{E(u(lang, "companion_pdf_release"))}</a>'
    n = pdf_pages(COMPANION_PDF_SRC)
    return (f'<h2>{E(u(lang, "companion_pdf"))}</h2><p>{E(u(lang, "companion_pdf_text", pages=(f"{n:,}" if lang == "en" else str(n)) if n else "?"))}</p>'
            f'<p>{links}</p>')


def home_page(lang):
    rows = []
    for v in YEARS:
        y = v["year"]
        t = CHAPTER_OF_YEAR.get(y)
        recs = [n for n in v["records"] if str(n) in RECS]
        n_items = sum(1 for n in recs for (tt, nn), ids in REC_ITEMS.items() if nn == str(n) for i in ids)
        comp = (f'<a href="{url(lang, "years", y)}">{E(u(lang, "companion_chapter", label=years_text(lang, CH[t]["years"])))}</a>'
                if t else E(u(lang, "no_companion")))
        nst = len(set(v["pages"]) & STALE_SET.get(t, set())) if t else 0
        rows.append(f'<tr><td><a href="{url(lang, "years", y)}">{year_label(y)}</a></td><td class="num">{len(recs)}</td>'
                    f'<td class="num hide-sm">{len(v["pages"])}</td><td>{comp}</td><td class="num">{n_items or ""}</td>'
                    f'<td class="num hide-sm">{nst if t else ""}</td></tr>')
    readers = " · ".join(f'<a href="{BASE}readers/{READERS[l]}">{E(u(lang, "reader_" + l))}</a>' for l in LANGS if NOTES_ON[l])
    data = ", ".join(f'{k} (<a href="{BASE}data/{k}.csv">CSV</a>, <a href="{BASE}data/{k}.json">JSON</a>)' for k in DATA_FILES_LIST)
    body = (f'<h1>{E(UI["site_name"][lang])}</h1><p>{E(u(lang, "tagline"))}</p>'
            f'<p class="kv">' + (f'<a href="{url(lang, "notebook")}">{E(u(lang, "notebook"))}</a> · ' if nb_on(lang) else "")
            + f'<a href="{url(lang, "problems")}">{E(u(lang, "problems"))}</a> · <a href="{url(lang, "speakers")}">{E(u(lang, "speakers"))}</a>'
            f' · <a href="{url(lang, "references")}">{E(u(lang, "references"))}</a>'
            f' · <a href="{url(lang, "search")}">{E(u(lang, "search"))}</a></p>'
            f'<h2>{E(u(lang, "years"))}</h2><table class="list yeargrid"><tr><th>{E(u(lang, "years_table_year"))}</th>'
            f'<th class="num">{E(u(lang, "years_table_records"))}</th><th class="num hide-sm">{E(u(lang, "years_table_pages"))}</th>'
            f'<th>{E(u(lang, "years_table_companion"))}</th><th class="num">{E(u(lang, "years_table_items"))}</th>'
            f'<th class="num hide-sm">{E(u(lang, "years_table_revised"))}</th></tr>' + "".join(rows) + "</table>"
            f'<p class="lbl">{E(u(lang, "class_legend"))}</p>'
            f'<h2>{E(u(lang, "readers"))}</h2><p>{E(u(lang, "readers_text", release=REL_SHORT))}</p><p>{readers}</p>'
            + companion_pdf_block(lang) +
            f'<h2>{E(u(lang, "data"))}</h2><p>{E(u(lang, "data_text"))} {data}; <a href="{BASE}data/works.json">works.json</a>, '
            f'<a href="{BASE}data/years.json">years.json</a>, <a href="{BASE}data/stale_pages.json">stale_pages.json</a>.</p>'
            f'<h2>{E(u(lang, "about"))}</h2><p>{u(lang, "about_text", mccme=f"<a href={chr(34)}{MCCME_LIST}{chr(34)}>{E(MCCME_LIST)}</a>", repo=f"<a href={chr(34)}{REPO_URL}{chr(34)}>{E(REPO_URL)}</a>")}</p>'
            f'<p>{E(u(lang, "companion_rights"))}</p>'
            f'<h2 id="credits">{E(u(lang, "credits"))}</h2><ul>'
            + "".join(f"<li>{E(c)}</li>" for c in UI[lang].get("credits_items", UI["en"].get("credits_items", [])))
            + "</ul>")
    return page(lang, UI["site_name"][lang], [(u(lang, "home"), None)], url(other_lang(lang)), general_status(lang), body,
                desc=u(lang, "tagline"), kind="home")


def ru_rights():
    """The Russian rights statement, added to the footer of the bilingual pages (root, resolver, 404)."""
    return f'<p class="rights" lang="ru">{u("ru", "rights", issues=E(ISSUES_URL))}</p>'


def root_page():
    body = (f'<h1>{E(UI["site_name"]["ru"])} · {E(UI["site_name"]["en"])}</h1>'
            f'<div class="chooser"><a href="{url("ru")}" lang="ru">Русский</a><a href="{url("en")}" lang="en">English</a></div>'
            f'<p lang="ru">{E(u("ru", "tagline"))}</p><p lang="en">{E(u("en", "tagline"))}</p>')
    return (head("en", f'{UI["site_name"]["ru"]} · {UI["site_name"]["en"]}', u("en", "tagline"))
            + f'<body data-base="{BASE}" data-lang="en" data-page-kind="root">'
            + status(general_status("en")) + f'<div class="page narrow">{body}</div>'
            + footer("en", ru_rights()) + scripts() + "</body></html>\n")


RESOLVER_JS = r"""<script>
(function(){
  var q=decodeURIComponent((location.search||'').slice(1).replace(/\+/g,' ')).trim();
  var h=(location.hash||'').slice(1);
  var L=null; try{L=localStorage.getItem('lang');}catch(e){}
  if(L!=='ru'&&L!=='en'){ L=(navigator.language||'').toLowerCase().indexOf('ru')===0?'ru':'en'; }
  var m=q.match(/^(ru|en)[:\/](.*)$/); if(m){L=m[1]; q=m[2];}
  if(!q){ location.replace(document.body.dataset.base+L+'/'); return; }
  window.GelfandResolve(q,L).then(function(u){ if(u){ location.replace(u+(h&&u.indexOf('#')<0?'#'+h:'')); } else { document.getElementById('msg').hidden=false; document.getElementById('pending').hidden=true; } },
    function(){ document.getElementById('msg').hidden=false; });
})();
</script>"""


def resolver_page():
    return (head("en", "Permalink", noindex=True) + f'<body data-base="{BASE}" data-lang="en" data-page-kind="resolver">'
            + status(general_status("en")) + f'<div class="page narrow"><p id="pending">{E(u("ru", "resolving"))} · {E(u("en", "resolving"))}</p>'
            + f'<div id="msg" hidden class="notice">{E(u("ru", "refbox_notfound"))} · {E(u("en", "refbox_notfound"))} · '
            + f'<a href="{url("ru")}">{E(u("ru", "home"))}</a> · <a href="{url("en")}">{E(u("en", "home"))}</a></div></div>'
            + footer("en", ru_rights()) + scripts() + RESOLVER_JS + "</body></html>\n")


NOTFOUND_JS = r"""<script>
(function(){
  var B=document.body.dataset.base, p=decodeURIComponent(location.pathname);
  if(p.indexOf(B)===0) p=p.slice(B.length);
  p=p.replace(/index\.html$/,'').replace(/^\/+|\/+$/g,'');
  var L='en', s=p.split('/'); if(s[0]==='ru'||s[0]==='en'){L=s.shift();}
  var q=s.join('/'); if(/^(talks|years|problems)\/?$/.test(q)) q='';
  q=q.replace(/^(talks|years|problems)\//,'');
  if(!q){ document.getElementById('nf').hidden=false; return; }
  window.GelfandResolve(q,L).then(function(u){ if(u) location.replace(u); else document.getElementById('nf').hidden=false; },
    function(){ document.getElementById('nf').hidden=false; });
})();
</script>"""


def notfound_page():
    return (head("en", "404", noindex=True) + f'<body data-base="{BASE}" data-lang="en" data-page-kind="404">'
            + status(general_status("en"))
            + f'<div class="page narrow" id="nf" hidden><h1>{E(u("en", "not_found_title"))} · <span lang="ru">{E(u("ru", "not_found_title"))}</span></h1>'
            + f'<p>{E(u("en", "not_found_text"))}</p><p lang="ru">{E(u("ru", "not_found_text"))}</p>'
            + f'<p><a href="{url("en")}">{E(u("en", "home"))}</a> · <a href="{url("ru")}">{E(u("ru", "home"))}</a></p></div>'
            + footer("en", ru_rights()) + scripts() + NOTFOUND_JS + "</body></html>\n")


# ------------------------------------------------------------------ data files
def write_csv(p, rows, header):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    for r in rows:
        w.writerow(["" if v is None else (" ".join(map(str, v)) if isinstance(v, (list, tuple)) else v) for v in r])
    wtext(p, buf.getvalue())


def data_files(out, speakers_map):
    d = out / "data"
    site_url = "https://kokunoyumeto.github.io" + BASE
    # items
    rows = []
    hdr = ["id", "work", "chapter", "academic_year", "record", "pages", "kind", "title", "class", "literal_correctness",
           "publication_match", "verification", "development", "confidence", "problem", "speaker", "refs",
           "stale_pages", "url", "notes", "statement", "reconstruction", "fate", "present_status", "worth"]
    js = []
    for iid, x in ITEMS.items():
        t = x["chapter"]
        st = sorted(set(parse_pages(x.get("pages"))) & STALE_SET.get(t, set()))
        rec = dict((k, x.get(k)) for k in hdr if k in x)
        rec.update({"work": CH[t]["work"], "chapter": t, "academic_year": YEAR_OF.get(str(x["record"])),
                    "stale_pages": [pid(p) for p in st], "url": site_url + f"en/talks/{x['record']}/#{iid}"})
        js.append(rec)
        rows.append([rec.get(k) for k in hdr])
    wjson(d / "items.json", js, indent=None)
    write_csv(d / "items.csv", rows, hdr)
    # talks
    hdr = ["record", "work", "chapter", "academic_year", "date", "speaker", "pages", "title", "kind", "summary", "url"]
    js, rows = [], []
    for n in sorted(ENTRIES, key=int):
        for t, tk in ENTRIES[n]:
            rec = {"record": int(n), "work": CH[t]["work"], "chapter": t, "academic_year": YEAR_OF.get(n),
                   "date": tk.get("date"), "speaker": tk.get("speaker"), "pages": tk.get("pages"), "title": tk.get("title"),
                   "kind": tk.get("kind"), "summary": tk.get("summary"), "url": site_url + f"en/talks/{n}/"}
            js.append(rec)
            rows.append([rec[k] for k in hdr])
    wjson(d / "talks.json", js, indent=None)
    write_csv(d / "talks.csv", rows, hdr)
    # problems
    hdr = ["id", "work", "chapter", "title", "statement", "occurrences", "status", "status_date", "refs", "url"]
    js, rows = [], []
    for p, ents in sorted(PROBLEMS.items()):
        for e in ents:
            rec = {"id": p, "work": CH[e["chapter"]]["work"], "chapter": e["chapter"], "title": e.get("title"),
                   "statement": e.get("statement"), "occurrences": e.get("occurrences") or [], "status": e.get("status"),
                   "status_date": e.get("status_date"), "refs": e.get("refs") or [], "url": site_url + f"en/problems/{p}/"}
            js.append(rec)
            rows.append([rec[k] for k in hdr])
    wjson(d / "problems.json", js, indent=None)
    write_csv(d / "problems.csv", rows, hdr)
    # references
    hdr = ["key", "chapters", "doi", "url", "note", "cited_by_items", "cited_by_problems", "bibtex"]
    js, rows = [], []
    for k in sorted(REFS):
        if not ref_shown(k):
            continue
        e = REFS[k]
        rec = {"key": k, "chapters": [t for t in e.get("chapters", []) if t in TAGS], "doi": e.get("doi"),
               "url": e.get("url"), "note": e.get("note"), "cited_by_items": REF_ITEMS.get(k, []),
               "cited_by_problems": [p for p in REF_PROBS.get(k, []) if p in PROBLEMS], "bibtex": e.get("bibtex")}
        js.append(rec)
        rows.append([rec[k2] for k2 in hdr])
    wjson(d / "references.json", js, indent=None)
    write_csv(d / "references.csv", rows, hdr)
    # pages
    hdr = ["page", "archive_chapter", "archive_part", "records", "scan", "reader_ru_pdf_page", "reader_en_pdf_page",
           "items", "revised_since_commentary"]
    js, rows = [], []
    rec_ok = set(RECS)
    for n, pg in sorted(REG["pages"].items(), key=lambda kv: int(kv[0])):
        recs = [r for r in pg["records"] if str(r) in rec_ok]
        if not recs:
            continue
        rev = {t: STALE_WHAT[t].get(n) for t in TAGS if int(n) in STALE_SET[t]}
        rec = {"page": pid(n), "archive_chapter": pg["chapter"], "archive_part": pg.get("part"), "records": recs,
               "scan": (pg.get("scans") or [None])[0], "reader_ru_pdf_page": pg.get("pdf", {}).get("ru") if NOTES_ON["ru"] else None,
               "reader_en_pdf_page": pg.get("pdf", {}).get("en") if NOTES_ON["en"] else None,
               "items": PAGE_ITEMS.get(int(n), []), "revised_since_commentary": rev}
        js.append(rec)
        rows.append([rec[k] for k in hdr[:-1]] + [json.dumps(rev, ensure_ascii=False) if rev else ""])
    wjson(d / "pages.json", js, indent=None)
    write_csv(d / "pages.csv", rows, hdr)
    # records
    hdr = ["record", "academic_year", "year_rule", "date", "date_as_catalogued", "date_corrected", "label",
           "speaker_as_catalogued", "association_kind", "pages", "archive_chapters", "chapters", "empty", "mccme_url"]
    js, rows = [], []
    for n in sorted(RECS, key=int):
        r = RECS[n]
        rec = {"record": int(n), "academic_year": r["year"], "year_rule": r["year_rule"], "date": r.get("date"),
               "date_as_catalogued": r.get("date_as_catalogued"), "date_corrected": bool(r.get("date_fix")),
               "label": r.get("label"), "speaker_as_catalogued": r.get("speaker_as_catalogued"),
               "association_kind": r.get("association_kind"), "pages": [pid(p) for p in r["pages"]],
               "archive_chapters": r["archive_chapters"], "chapters": [t for t in r["chapters"] if t in TAGS],
               "empty": r.get("empty"), "mccme_url": r["url"]}
        js.append(rec)
        rows.append([rec[k] for k in hdr])
    wjson(d / "records.json", js, indent=None)
    write_csv(d / "records.csv", rows, hdr)
    # corrections
    hdr = ["chapter", "work", "page", "place", "transcription_reads", "should_read", "evidence", "applies_to", "type"]
    js, rows = [], []
    for t in TAGS:
        for row in COMP[t]["corrections"]:
            rec = {"chapter": t, "work": CH[t]["work"], "page": row.get("page"), "place": row.get("place_tex"),
                   "transcription_reads": row.get("transcription_reads_tex"), "should_read": row.get("should_read_tex"),
                   "evidence": row.get("evidence_tex"), "applies_to": row.get("applies_to"), "type": row.get("type")}
            js.append(rec)
            rows.append([rec[k] for k in hdr])
    wjson(d / "corrections.json", js, indent=None)
    write_csv(d / "corrections.csv", rows, hdr)
    # years, works, staleness, resolver
    wjson(d / "years.json", [{"year": v["year"], "records": [n for n in v["records"] if str(n) in RECS],
                              "pages": [pid(p) for p in v["pages"]], "chapter": CHAPTER_OF_YEAR.get(v["year"])}
                             for v in YEARS])
    wjson(d / "works.json", {"works": [dict(w) for w in works()], "exclude_records": sorted(int(x) for x in EXCL_REC),
                             "release": {k: REL[k] for k in ("repository", "tag", "commit", "created_at")}})
    wjson(d / "stale_pages.json", {"release": STALE["release"], "release_date": STALE["release_date"],
                                   "chapters": {t: {k: v for k, v in STALE["chapters"][t].items() if k != "found_in"}
                                                for t in TAGS if t in STALE["chapters"]}})
    pages_min = {}
    for n, pg in REG["pages"].items():
        recs = [r for r in pg["records"] if str(r) in RECS]
        if recs:
            pages_min[n] = [recs[0], pg["chapter"]]
    dates = collections.defaultdict(list)
    for n in sorted(RECS, key=int):
        dd = rec_date(n)
        if dd:
            dates[dd].append(int(n))
    wjson(d / "resolve.json", {"records": sorted(int(n) for n in RECS), "items": {i: x["record"] for i, x in ITEMS.items()},
                               "problems": sorted(PROBLEMS), "pages": pages_min, "years": [v["year"] for v in YEARS],
                               "dates": dates, "speakers": speakers_map, "notebook": bool(NB)}, indent=None)
    idx = ["<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><title>Data</title>",
           f'<link rel="stylesheet" href="{BASE}assets/site.css"></head><body><div class="page narrow"><h1>Data</h1><ul>']
    for f in sorted(d.iterdir()):
        if f.is_file() and f.name != "index.html":
            idx.append(f'<li><a href="{BASE}data/{E(f.name)}">{E(f.name)}</a> ({f.stat().st_size // 1024} KB)</li>')
    idx.append(f'</ul><p class="rights">{u("en", "rights", issues=E(ISSUES_URL))}</p></div></body></html>\n')
    wtext(d / "index.html", "".join(idx))


# ------------------------------------------------------------------ assets
def copy_assets(out):
    a = out / "assets"
    a.mkdir(parents=True, exist_ok=True)
    for f in ASSETS.glob("*"):
        if f.is_file():
            shutil.copy(f, a / f.name)
    mj = os.environ.get("GELFAND_MATHJAX")
    vend = rjson(DATA / "vendor.lock.json")
    if mj and Path(mj).exists():
        src = Path(mj)
        dest = a / "mathjax"
        if dest.exists():
            shutil.rmtree(dest)
        for k in vend["mathjax"]["keep"]:
            s = src / k
            if s.is_dir():
                shutil.copytree(s, dest / k)
            elif s.exists():
                (dest / k).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(s, dest / k)
        lic = src.parent / "LICENSE"
        if lic.exists():
            shutil.copy(lic, dest / "LICENSE")
    elif not (a / "mathjax" / "tex-chtml.js").exists():
        log("WARNING: GELFAND_MATHJAX not set and no MathJax in the site: formulas will not be typeset")
    r = out / "readers"
    r.mkdir(parents=True, exist_ok=True)
    if COMPANION_PDF_SRC:
        shutil.copy(COMPANION_PDF_SRC, r / COMPANION_PDF)
    for l in LANGS:
        f = release_dir() / READERS[l]
        if NOTES_ON[l]:
            if not (r / READERS[l]).exists() or (r / READERS[l]).stat().st_size != f.stat().st_size:
                shutil.copy(f, r / READERS[l])
        elif (r / READERS[l]).exists():
            (r / READERS[l]).unlink()


# ------------------------------------------------------------------ main
def main():
    out = site_dir()
    for l in LANGS:
        if (out / l).exists():
            shutil.rmtree(out / l)
    copy_assets(out)
    counts = collections.Counter()
    speakers_map = {}
    for lang in LANGS:
        wtext(out / lang / "index.html", home_page(lang))
        for v in YEARS:
            wtext(out / lang / "years" / v["year"] / "index.html", year_page(lang, v["year"]))
            counts["year"] += 1
        for n in sorted(RECS, key=int):
            wtext(out / lang / "talks" / n / "index.html", talk_page(lang, n))
            counts["talk"] += 1
        for p in PROBLEMS:
            wtext(out / lang / "problems" / p / "index.html", problem_page(lang, p))
            counts["problem"] += 1
        wtext(out / lang / "problems" / "index.html", problems_index(lang))
        html_, nref = references_page(lang)
        wtext(out / lang / "references" / "index.html", html_)
        counts["references"] = nref
        sp_html, speakers_map = speakers_page(lang)
        wtext(out / lang / "speakers" / "index.html", sp_html)
        for t in TAGS:
            wtext(out / lang / "development" / slug(t) / "index.html", development_page(lang, t))
            counts["development"] += 1
        if nb_on(lang):
            wtext(out / lang / "notebook" / "index.html", notebook_index(lang))
            for ch in NB_CHAPTERS:
                wtext(out / lang / "notebook" / ch / "index.html", notebook_page(lang, ch))
                counts["notebook"] += 1
        wtext(out / lang / "search" / "index.html", search_page(lang))
    if NB:
        counts["page shards"] = nb_shards(out)
        counts["scan crops"], _missing = copy_crops(out)
        fig_dir = out / "assets" / "figures"
        counts["figures"] = len(list(fig_dir.glob("*.svg"))) if fig_dir.exists() else 0
    wtext(out / "index.html", root_page())
    wtext(out / "r" / "index.html", resolver_page())
    wtext(out / "404.html", notfound_page())
    wtext(out / ".nojekyll", "")
    data_files(out, speakers_map)
    print(f"G8 render: {dict(counts)} (both languages); chapters {len(TAGS)}, items {len(ITEMS)}, problems {len(PROBLEMS)}, "
          f"records {len(RECS)}, years {len(YEARS)}; base {BASE}; output {out}")


if __name__ == "__main__":
    main()
