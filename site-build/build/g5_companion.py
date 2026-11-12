"""G5 companion fields: convert every LaTeX field of the companion to HTML.

Per chapter, all LaTeX fields (talk summaries; the notes, statement, reconstruction, fate, present status and worth of
every item; problem statements and statuses; the overview; the developed questions; the cells of the corrections
table) go into one LaTeX document, each preceded by a sentinel paragraph.  The macros of gelfand_companion.sty are
mapped (\\ru -> a Russian-language span, \\ours and \\oursComputed -> badges, \\GSpage and \\GSrecord -> links, the
theorem environments kept), and pandoc runs once with --citeproc on the merged bibliography, so that \\citet, \\citep
and their locators become author-year citations linked to the bibliography.  The HTML is split at the sentinels.
If a sentinel goes missing (a field pandoc could not read on its own), the chapter is converted again in halves, down
to single fields.

The merged bibliography keeps the first entry of each key in chapter order (the rule of the global reader); its
entries are formatted by the same pandoc/citeproc run (Chicago author-date).

Output: WORK/ir/companion/<TAG>.json, WORK/ir/companion/references.json, WORK/ir/companion/references.bib.
Accepted when every field is converted and every citation key is in the bibliography.
"""
import concurrent.futures as cf
import csv
import io
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import IR, YEARS_DIR, chapter_tags, log, report, rjson, rtext, sha256_bytes, wjson

OUT = IR / "companion"
ITEM_FIELDS = ["notes", "statement", "reconstruction", "fate", "present_status", "worth"]
CORR_FIELDS = ["place", "transcription_reads", "should_read", "evidence"]
PREAMBLE = r"""\documentclass{article}
\usepackage{amsmath,amssymb,amsthm}
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{conjecture}[theorem]{Conjecture}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{question}[theorem]{Question}
\newtheorem{example}[theorem]{Example}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\newcommand{\ours}{QQOURSQQ}
\newcommand{\oursComputed}{QQOURSCQQ}
\newcommand{\ru}[1]{\foreignlanguage{russian}{#1}}
\newcommand{\GSpage}[1]{QQPGQQ#1QQPGENDQQ}
\newcommand{\GSrecord}[1]{QQRECQQ#1QQRECENDQQ}
\begin{document}
"""
SENT = "QQFIELD{:05d}QQ"
SPLIT = re.compile(r"<p>QQFIELD(\d{5})QQ</p>\n?")
CITE = re.compile(r"\\cite(?:t|p|alp|alt|author|year|yearpar|num)?\*?(?:\[[^\]]*\]){0,2}\{([^}]*)\}")


def bib_entries(text):
    return [(m.group(1), m.group(0).rstrip() + "\n")
            for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,.*?(?=^@|\Z)", text, re.S | re.M)]


def pandoc(latex, bib, extra=()):
    r = subprocess.run(["pandoc", "-f", "latex", "-t", "html", "--mathjax", "--wrap=none", "--citeproc",
                        "--bibliography", str(bib), "-M", "link-citations=true", *extra],
                       input=latex.encode("utf-8"), capture_output=True, timeout=1800)
    return r.stdout.decode("utf-8"), r.stderr.decode("utf-8", "replace"), r.returncode


def convert(fields, bib, depth=0):
    """fields: list of (key, latex) -> ({key: html}, [warnings])"""
    doc = PREAMBLE + "".join(f"\n\n\\par {SENT.format(i)}\\par\n\n{tex}\n" for i, (k, tex) in enumerate(fields))
    doc += "\n\n\\par " + SENT.format(len(fields)) + "\\par\n\n\\end{document}\n"
    html, err, rc = pandoc(doc, bib)  # the bibliography pandoc appends after the last sentinel is dropped
    parts = SPLIT.split(html)
    # parts: [before, '00000', html0, '00001', html1, ...]
    got = {}
    for j in range(1, len(parts) - 1, 2):
        got[int(parts[j])] = parts[j + 1]
    ok = rc == 0 and all(i in got for i in range(len(fields) + 1)) and len(got) == len(fields) + 1
    if ok:
        return {fields[i][0]: got[i].strip() for i in range(len(fields))}, [w for w in err.splitlines() if w.strip()]
    if len(fields) == 1:
        log(f"  field {fields[0][0]}: pandoc could not convert it on its own (rc {rc}); kept as text")
        return {fields[0][0]: None}, [f"[UNCONVERTED] {fields[0][0]}: {err.strip()[:300]}"]
    mid = len(fields) // 2
    a, wa = convert(fields[:mid], bib, depth + 1)
    b, wb = convert(fields[mid:], bib, depth + 1)
    a.update(b)
    return a, wa + wb


def post(html, dev_labels):
    """Map the sentinels of the macros and the links pandoc made to site placeholders (resolved by the renderer):
    @@REFS@@ the bibliography page, @@R@@ the permalink resolver, @@TALK@@ talk pages, @@PROB@@ problem pages,
    @@DEV@@ the chapter's development page."""
    if html is None:
        return None
    html = html.replace("QQOURSCQQ", '<span class="badge ours">computed here</span>')
    html = html.replace("QQOURSQQ", '<span class="badge ours">proved here</span>')

    def pg(m):
        inner = re.sub(r"P(\d{6})", lambda x: f'<a href="@@R@@?P{x.group(1)}">P{x.group(1)}</a>', m.group(1))
        return f'<span class="pid">{inner}</span>'
    html = re.sub(r"QQPGQQ(.*?)QQPGENDQQ", pg, html, flags=re.S)
    html = re.sub(r"QQRECQQ\s*(\d+)\s*QQRECENDQQ", lambda m: f'<a href="@@TALK@@{m.group(1)}/">record {m.group(1)}</a>', html)
    html = re.sub(r'href="#ref-([^"]+)"', lambda m: f'href="@@REFS@@#{m.group(1)}" class="cite"', html)

    def href(m):
        lab = m.group(1)
        if lab.startswith("prob:"):
            return f'href="@@PROB@@{lab[5:]}/"'
        if lab.startswith("item:"):
            return f'href="@@R@@?{lab[5:]}"'
        if lab.startswith(("rec:", "talk:")):
            return f'href="@@TALK@@{lab.split(":", 1)[1]}/"'
        if lab in dev_labels:
            return f'href="@@DEV@@#{lab}"'
        return m.group(0)
    html = re.sub(r'href="#([^"]+)"', href, html)
    return html


def chapter_fields(tag):
    d = YEARS_DIR / tag
    talks = json.loads((d / f"{tag}_talks.json").read_text(encoding="utf-8"))
    items = json.loads((d / f"{tag}_items.json").read_text(encoding="utf-8"))
    probs = json.loads((d / f"{tag}_problems.json").read_text(encoding="utf-8"))
    corr = list(csv.DictReader(io.StringIO((d / f"{tag}_corrections.csv").read_text(encoding="utf-8-sig"))))
    fields = []
    for t in talks:
        fields.append((f"talk|{t['record']}|summary", str(t.get("summary") or "")))
    for x in items:
        for k in ITEM_FIELDS:
            v = x.get(k)
            if v:
                fields.append((f"item|{x['id']}|{k}", str(v)))
    for p in probs:
        for k in ("statement", "status"):
            if p.get(k):
                fields.append((f"problem|{p['id']}|{k}", str(p[k])))
    for i, r in enumerate(corr):
        for k in CORR_FIELDS:
            if (r.get(k) or "").strip():
                fields.append((f"corr|{i}|{k}", r[k]))
    fields.append(("overview", rtext(d / f"{tag}_overview.tex")))
    fields.append(("development", rtext(d / f"{tag}_development.tex")))
    return talks, items, probs, corr, fields


def do_chapter(tag, bib, keys):
    talks, items, probs, corr, fields = chapter_fields(tag)
    src_hash = sha256_bytes(json.dumps(fields, ensure_ascii=False).encode("utf-8") + Path(bib).read_bytes())
    out = OUT / f"{tag}.json"
    old = rjson(out, {})
    if old.get("source_hash") == src_hash:
        return tag, old, True
    dev = rtext(YEARS_DIR / tag / f"{tag}_development.tex")
    dev_labels = set(re.findall(r"\\label\{([^}]+)\}", dev))
    conv, warns = convert(fields, bib)
    res = {"source_hash": src_hash, "talks": {}, "items": {}, "problems": {}, "corrections": [],
           "overview": None, "development": None, "warnings": warns}
    for k, tex in fields:
        h = post(conv.get(k), dev_labels)
        parts = k.split("|")
        if parts[0] == "talk":
            res["talks"].setdefault(parts[1], {})[parts[2]] = h
        elif parts[0] == "item":
            res["items"].setdefault(parts[1], {})[parts[2]] = h
        elif parts[0] == "problem":
            res["problems"].setdefault(parts[1], {})[parts[2]] = h
        elif parts[0] == "corr":
            pass
        else:
            res[parts[0]] = h
    cmap = {}
    for k, tex in fields:
        if k.startswith("corr|"):
            _, i, f = k.split("|")
            cmap.setdefault(int(i), {})[f] = post(conv.get(k), dev_labels)
    for i, r in enumerate(corr):
        row = {"page": r.get("page"), "applies_to": r.get("applies_to"), "type": (r.get("type") or "").strip()}
        for f in CORR_FIELDS:
            row[f] = cmap.get(i, {}).get(f, "")
            row[f + "_tex"] = r.get(f) or ""
        res["corrections"].append(row)
    used = set()
    for k, tex in fields:
        for m in CITE.finditer(tex):
            used |= {x.strip() for x in m.group(1).split(",") if x.strip()}
    for x in items:
        used |= set(x.get("refs") or [])
    for p in probs:
        used |= set(p.get("refs") or [])
    res["cite_keys"] = sorted(used)
    res["undefined"] = sorted(used - keys)
    res["unconverted"] = [k for k, tex in fields if conv.get(k) is None]
    res["n_fields"] = len(fields)
    wjson(out, res, indent=None)
    return tag, res, False


def references(bib_path, order):
    """Format every entry of the merged bibliography (nocite all) and keep its HTML by key."""
    doc = PREAMBLE + "\\nocite{*}\n\\end{document}\n"
    html, err, rc = pandoc(doc, bib_path)
    entries = {}
    for m in re.finditer(r'<div id="ref-([^"]+)" class="csl-entry"[^>]*>(.*?)</div>', html, re.S):
        entries[m.group(1)] = m.group(2).strip()
    return entries, [w for w in err.splitlines() if w.strip()]


def main():
    tags = chapter_tags(all_=True)
    OUT.mkdir(parents=True, exist_ok=True)
    seen, merged, per_chapter = set(), [], {}
    for tag in tags:
        ents = bib_entries(rtext(YEARS_DIR / tag / f"{tag}_references.bib"))
        per_chapter[tag] = [k for k, e in ents]
        for k, e in ents:
            if k not in seen:
                seen.add(k)
                merged.append((k, e))
    bib = OUT / "references.bib"
    bib.write_text("\n".join(e for k, e in merged), encoding="utf-8", newline="\n")
    keys = {k for k, e in merged}
    refs_old = rjson(OUT / "references.json", {})
    bib_hash = sha256_bytes(bib.read_bytes())
    if refs_old.get("bib_hash") != bib_hash:
        entries, rwarn = references(bib, [k for k, e in merged])
        refs = {"bib_hash": bib_hash, "warnings": rwarn, "entries": {}}
        for k, e in merged:
            doi = re.search(r"\bdoi\s*=\s*[{\"]([^}\"]+)", e, re.I)
            url = re.search(r"\burl\s*=\s*[{\"]([^}\"]+)", e, re.I)
            note = re.search(r"\bnote\s*=\s*[{\"]([^}\"]*)", e, re.I)
            refs["entries"][k] = {"html": entries.get(k), "doi": doi.group(1).strip() if doi else None,
                                  "url": url.group(1).strip() if url else None,
                                  "note": note.group(1).strip() if note else None,
                                  "chapters": [t for t in tags if k in per_chapter[t]], "bibtex": e}
        wjson(OUT / "references.json", refs, indent=None)
    else:
        refs = refs_old
        for k, e in merged:
            refs["entries"][k]["chapters"] = [t for t in tags if k in per_chapter[t]]
        wjson(OUT / "references.json", refs, indent=None)
    results = {}
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(do_chapter, t, bib, keys): t for t in tags}
        for f in cf.as_completed(futs):
            tag, res, cached = f.result()
            results[tag] = res
            log(f"  {tag}: {res['n_fields']} fields{' (cached)' if cached else ''}; undefined keys "
                f"{len(res['undefined'])}; unconverted {len(res['unconverted'])}; pandoc warnings {len(res['warnings'])}")
    rows = []
    for tag in tags:
        r = results[tag]
        rows.append((tag, r["n_fields"], len(r["unconverted"]), len(r["undefined"]), " ".join(r["undefined"][:20]),
                     len(r["warnings"])))
    report("g5_fields", rows, ["chapter", "fields", "unconverted", "undefined citation keys", "keys", "pandoc warnings"])
    report("g5_warnings", [(t, w) for t in tags for w in results[t]["warnings"]], ["chapter", "pandoc message"])
    noent = [k for k, v in refs["entries"].items() if not v.get("html")]
    report("g5_references_unformatted", [(k,) for k in noent], ["key"])
    n_f = sum(r["n_fields"] for r in results.values())
    n_u = sum(len(r["unconverted"]) for r in results.values())
    n_k = sum(len(r["undefined"]) for r in results.values())
    print(f"G5 companion fields: {len(tags)} chapters, {n_f} fields, unconverted {n_u}, undefined citation keys {n_k}; "
          f"bibliography {len(merged)} keys ({sum(len(v) for v in per_chapter.values())} chapter entries), "
          f"{len(merged) - len(noent)} formatted")
    ok = n_u == 0 and n_k == 0 and not noent
    print("G5", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
