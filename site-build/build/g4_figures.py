"""G4 figures: every figure of the notebook text typeset by LuaLaTeX with the edition's own preamble, one SVG each
(design §7).

The figures are those G3 took out of the text (WORK/ir/notebook/figures.json): TikZ pictures, commutative diagrams,
inline \\tikz, and formulas that contain TikZ or use macros MathJax lacks. Per (language, archive chapter) one
document: the preamble of the language's cumulative file, the TikZ libraries and styles the text sets
(figure_setup.json), the preview package; one page per figure; lualatex once. A figure whose part of the log shows an
error gets no SVG (if the page count does not match, the document is split in halves until the failing figures are
alone); the site then shows the scan crop and the page of the reader PDF instead (reports/g4_failed.tsv).
pdftocairo converts each page to SVG.

Cache: WORK/cache/figures/<sha256(preamble + page TeX)[:24]>.svg, so a re-run compiles only new or changed figures.
Output: SITE/assets/figures/<figure hash>.svg and WORK/ir/notebook/figures_built.json {hash: [width, height, depth]}
(pt; the depth below the baseline, from preview's log, places a figure inside a line of text).
"""
import collections
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import CACHE, IR, latex_dir, log, report, rjson, sha256_bytes, site_dir, wjson  # noqa: E402

LANGS = {"ru": "russian", "en": "english"}
NB = IR / "notebook"
FIGCACHE = CACHE / "figures"
BUILD = CACHE / "figure_build"
WORKERS = int(os.environ.get("GELFAND_LATEX_JOBS") or 4)
PRE_EXTRA = "\n\\usepackage[active,tightpage]{preview}\n\\setlength\\PreviewBorder{1.5pt}\n\\pagestyle{empty}\n"
MARK = "QQFIGURE"
DISPLAY_ENVS = {"equation": None, "gather": "gathered", "align": "aligned", "flalign": "aligned",
                "multline": "gathered", "alignat": "alignedat", "eqnarray": "array"}


def preamble(lang, setup):
    src = latex_dir() / f"gelfand-{LANGS[lang]}-chapters01-34-complete-first1527.tex"
    pre = src.read_text(encoding="utf-8").split("\\begin{document}", 1)[0]
    gp = latex_dir().resolve().as_posix().rstrip("/") + "/"
    return pre + "\n\\graphicspath{{" + gp + "}}\n" + "\n".join(setup) + "\n" + PRE_EXTRA


def group_arg(s, i):
    depth, j = 0, i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced")


def tags(t):
    """\\tag{x} -> (x) after a quad, \\tag*{x} -> x; labels and \\notag dropped (a formula in a preview box is
    typeset in text style display, where \\tag is not allowed)."""
    t = re.sub(r"\\label\{[^{}]*\}|\\nonumber(?![A-Za-z])|\\notag(?![A-Za-z])", "", t)
    out, pos = [], 0
    for m in re.finditer(r"\\tag(\*?)\s*\{", t):
        if m.start() < pos:
            continue
        try:
            a, e = group_arg(t, m.end() - 1)
        except ValueError:
            continue
        out.append(t[pos:m.start()])
        out.append("\\qquad\\text{" + (a if m.group(1) else "(" + a + ")") + "}")
        pos = e
    out.append(t[pos:])
    return "".join(out)


def page_tex(kind, tex):
    t = tex.replace("\r\n", "\n").replace("\r", "\n").strip()
    if kind in ("picture", "tikzcd", "tikz-inline"):
        return "\\begin{preview}" + t + "\\end{preview}"
    t = re.sub(r"\n[ \t]*(?:\n[ \t]*)+", "\n", t)           # no paragraph break inside a formula
    inline = False
    m = re.fullmatch(r"\\begin\{([a-z]+)(\*?)\}(.*)\\end\{\1\2\}", t, re.S)
    if t.startswith("\\[") and t.endswith("\\]"):
        body = t[2:-2]
    elif t.startswith("$$") and t.endswith("$$"):
        body = t[2:-2]
    elif t.startswith("\\(") and t.endswith("\\)"):
        body, inline = t[2:-2], True
    elif t.startswith("$") and t.endswith("$"):
        body, inline = t[1:-1], True
    elif t.startswith("\\ensuremath"):
        body, inline = group_arg(t, t.index("{"))[0], True
    elif m and m.group(1) in DISPLAY_ENVS:
        env, body = DISPLAY_ENVS[m.group(1)], m.group(3)
        if env == "alignedat":
            n, e = group_arg(body, body.index("{"))
            body = "\\begin{alignedat}{" + n + "}" + body[e:] + "\\end{alignedat}"
        elif env == "array":
            body = "\\begin{array}{rcl}" + body + "\\end{array}"
        elif env:
            body = "\\begin{" + env + "}" + body + "\\end{" + env + "}"
    else:
        body = t
    body = tags(body)
    return "\\begin{preview}$" + ("" if inline else "\\displaystyle ") + body + "$\\end{preview}"


def run_latex(wd, pre, pages, halt=False):
    """-> (pdf pages or 0, log text)."""
    if wd.exists():
        shutil.rmtree(wd, ignore_errors=True)
    wd.mkdir(parents=True, exist_ok=True)
    doc = pre + "\\begin{document}\n" + "".join(
        f"\\typeout{{{MARK}:{i}}}\n{p}\n" for i, p in enumerate(pages)) + f"\\typeout{{{MARK}:END}}\n\\end{{document}}\n"
    (wd / "d.tex").write_text(doc, encoding="utf-8")
    cmd = ["lualatex", "-interaction=nonstopmode"] + (["-halt-on-error"] if halt else []) + ["d.tex"]
    try:
        subprocess.run(cmd, cwd=wd, capture_output=True, timeout=3600)
    except subprocess.TimeoutExpired:
        return 0, "timeout"
    logtxt = (wd / "d.log").read_text(encoding="utf-8", errors="replace") if (wd / "d.log").exists() else ""
    n = 0
    if (wd / "d.pdf").exists():
        r = subprocess.run(["pdfinfo", "d.pdf"], cwd=wd, capture_output=True, text=True)
        m = re.search(r"^Pages:\s+(\d+)", r.stdout, re.M)
        n = int(m.group(1)) if m else 0
    return n, logtxt


def errors_by_figure(logtxt, count):
    """{index: first error line} from the log, by the markers written before each figure."""
    out = {}
    parts = re.split(MARK + r":(\d+|END)", logtxt)
    for j in range(1, len(parts) - 1, 2):
        if parts[j] == "END":
            continue
        errs = re.findall(r"^! .*$", parts[j + 1], re.M)
        if errs:
            out[int(parts[j])] = errs[0][:200]
    return out


def snippets(logtxt):
    """{snippet number: (height, depth, width) in pt} from preview's log lines (tightpage)."""
    flat = logtxt.replace("\r", "").replace("\n", "")
    return {int(m.group(1)): (int(m.group(2)) / 65536, int(m.group(3)) / 65536, int(m.group(4)) / 65536)
            for m in re.finditer(r"Preview: Snippet (\d+) ended\.\((-?\d+)\+(-?\d+)x(-?\d+)\)", flat)}


MUTOOL = os.environ.get("GELFAND_MUTOOL") or shutil.which("mutool")


def to_svg(wd, page, dest):
    """pdftocairo; if it fails or hangs (a crashed converter can sit waiting for Windows' error dialog), mutool."""
    out = wd / f"p{page}.svg"
    try:
        r = subprocess.run(["pdftocairo", "-svg", "-f", str(page), "-l", str(page), "d.pdf", out.name], cwd=wd,
                           capture_output=True, timeout=90)
        ok = r.returncode == 0 and out.exists() and out.stat().st_size > 200
    except subprocess.TimeoutExpired:
        ok = False
    if not ok and MUTOOL:
        out.unlink(missing_ok=True)
        try:
            r = subprocess.run([MUTOOL, "draw", "-q", "-F", "svg", "-o", out.name, "d.pdf", str(page)], cwd=wd,
                               capture_output=True, timeout=90)
            ok = r.returncode == 0 and out.exists() and out.stat().st_size > 200
        except subprocess.TimeoutExpired:
            ok = False
    if ok:
        shutil.move(str(out), str(dest))
    return ok


def build_group(key, pre, todo, depth=0):
    """todo: [(cache key, page TeX)] -> ({cache key: error}, [missing-character lines])."""
    wd = BUILD / (key + ("" if depth == 0 else f"-{depth}-{todo[0][0][:8]}"))
    n, logtxt = run_latex(wd, pre, [p for _, p in todo], halt=depth > 0)
    errs = errors_by_figure(logtxt, len(todo)) if n else {}
    missing = re.findall(r"Missing character: [^\n]*", logtxt)
    failed = {}
    if n == len(todo):
        sn = snippets(logtxt)
        for i, (ck, _) in enumerate(todo):
            if i in errs:
                failed[ck] = errs[i]
            elif not to_svg(wd, i + 1, FIGCACHE / f"{ck}.svg"):
                failed[ck] = "pdftocairo failed"
            elif i + 1 in sn:       # the depth below the baseline, for figures inside a line of text
                (FIGCACHE / f"{ck}.depth").write_text(f"{sn[i + 1][1]:.3f}", encoding="utf-8")
        shutil.rmtree(wd, ignore_errors=True)
        return failed, missing
    shutil.rmtree(wd, ignore_errors=True)
    if len(todo) == 1:
        err = re.findall(r"^! .*$", logtxt, re.M)
        return {todo[0][0]: (err[0] if err else f"{n} pages for 1 figure")[:200]}, missing
    mid = len(todo) // 2
    f1, m1 = build_group(key, pre, todo[:mid], depth + 1)
    f2, m2 = build_group(key + "b", pre, todo[mid:], depth + 1)
    f1.update(f2)
    return f1, m1 + m2


def svg_size(p):
    head = p.read_text(encoding="utf-8", errors="replace")[:600]
    m = re.search(r'<svg[^>]*\bwidth="([\d.]+)(?:pt)?"[^>]*\bheight="([\d.]+)(?:pt)?"', head)
    return (round(float(m.group(1)), 2), round(float(m.group(2)), 2)) if m else None


def main():
    figs = rjson(NB / "figures.json")
    setup = rjson(NB / "figure_setup.json")
    reg = rjson(IR / "registry.json")
    FIGCACHE.mkdir(parents=True, exist_ok=True)
    pres = {lang: preamble(lang, setup.get(lang, [])) for lang in LANGS}
    groups = collections.defaultdict(list)
    ck_of = {}
    for h, f in figs.items():
        lang = f["lang"]
        pt = page_tex(f["kind"], f["tex"])
        ck = sha256_bytes((pres[lang] + pt).encode("utf-8"))[:24]
        ck_of[h] = ck
        if not (FIGCACHE / f"{ck}.svg").exists():
            chap = reg["pages"][str(int(f["page"][1:]))]["chapter"] if f.get("page") else 0
            groups[(lang, chap)].append((ck, pt))
    todo = sorted(groups.items())
    log(f"G4: {len(figs)} figures, {sum(len(v) for v in groups.values())} to typeset in {len(todo)} documents "
        f"({WORKERS} at a time)")
    failed, missing = {}, []

    def one(item):
        (lang, chap), lst = item
        seen, uniq = set(), []
        for ck, pt in lst:
            if ck not in seen:
                seen.add(ck)
                uniq.append((ck, pt))
        f, m = build_group(f"{lang}-{chap:02d}", pres[lang], uniq)
        log(f"G4 {lang} chapter {chap}: {len(uniq)} figures, {len(f)} failed")
        return f, m
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        for f, m in ex.map(one, todo):
            failed.update(f)
            missing += m
    out_dir = site_dir() / "assets" / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    built, rows = {}, []
    for h, f in figs.items():
        src = FIGCACHE / f"{ck_of[h]}.svg"
        if src.exists() and src.stat().st_size > 200:
            shutil.copy(src, out_dir / f"{h}.svg")
            dp = src.with_suffix(".depth")
            built[h] = list(svg_size(src) or (None, None)) + [float(dp.read_text()) if dp.exists() else None]
        else:
            rows.append((h, f["kind"], f.get("page", ""), ",".join(f.get("langs", [])),
                         failed.get(ck_of[h], "no SVG"), f["tex"][:300].replace("\n", " ").replace("\t", " ")))
    for p in out_dir.glob("*.svg"):
        if p.stem not in built:
            p.unlink()
    wjson(NB / "figures_built.json", built, indent=None)
    report("g4_failed", rows, ["figure", "kind", "page", "languages", "error", "tex"])
    mc = collections.Counter(re.sub(r"\s+", " ", m)[:120] for m in missing)
    report("g4_missing_characters", sorted(mc.items(), key=lambda kv: -kv[1]), ["log line", "count"])
    size = sum(p.stat().st_size for p in out_dir.glob("*.svg"))
    print(f"G4 figures: {len(built)} of {len(figs)} typeset ({size / 1e6:.1f} MB SVG); failed {len(rows)} "
          f"(reports/g4_failed.tsv); missing-character lines {sum(mc.values())}")
    print("G4", "PASS" if len(built) + len(rows) == len(figs) and len(rows) <= len(figs) // 50 else "FAIL")
    sys.exit(0 if len(rows) <= len(figs) // 50 else 1)


if __name__ == "__main__":
    main()
