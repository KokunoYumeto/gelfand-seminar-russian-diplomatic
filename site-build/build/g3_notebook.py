"""G3 notebook adapter: the Russian and English notebook text of the locked release, page by page (design §7).

Reads the two cumulative LaTeX files of the release (WORK/cache/<tag>/x/) and
  - splits them at \\SourcePage into the 1,527 notebook pages (with the number written on each page);
  - keeps the passages (the GelfandAdjacentEvidence groups, numbered per page) as anchors P000659.2;
  - turns the marked readings (\\Unclear, \\Incomplete, \\SourceFigure, \\EvidenceBlock and the diagram comparisons)
    into notes with their scan crops (the PNG details of the release's figures/ folder);
  - takes every figure out for G4 (tikzpicture, tikzcd, \\tikz, and formulas that contain TikZ), keyed by the
    SHA-256 of its TeX, so identical figures of the two languages share one SVG;
  - converts the rest with pandoc, TeX mathematics kept for MathJax.

Output: WORK/ir/notebook/{ru,en}.json  {"P000659": {"label", "html", "passages", "readings"}},
        WORK/ir/notebook/figures.json   {hash: {"tex", "kind", "lang", "page"}},
        WORK/ir/notebook/crops.json     {"GELFAND-P000659-label": [png file names]}.
Check (parity): both languages have the same 1,527 pages, the same passage numbers on each page and the same
marked-reading labels on each page (differences in reports/g3_parity.tsv); every page and note converted; no LaTeX
left outside the mathematics (reports/g3_latex.tsv).
"""
import collections
import hashlib
import html as H
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import IR, latex_dir, log, report, rjson, wjson  # noqa: E402

LANGS = {"ru": "russian", "en": "english"}
OUT = IR / "notebook"
MATHENV = r"(?:equation|gather|align|multline|flalign|alignat|eqnarray)\*?"
READING_MACROS = {"Unclear": ("unclear", 3), "Incomplete": ("incomplete", 3), "SourceFigure": ("figure", 3),
                  "EvidenceBlock": ("evidence", 4), "GelfandDiagramComparison": ("figure", 3),
                  "GelfandWideDiagramComparison": ("figure", 3)}
CAPTION_MACROS = ("SourceCropCaption", "ReadingCaption", "IncompleteCaption", "DiagramCaption", "GelfandExcerptCaption",
                  "TypesetDiagramCaption", "PhaseWords", "GridWords")
PANDOC_PRE = "\\documentclass{article}\n\\usepackage{amsmath,amssymb,ulem,xcolor,hyperref}\n\\begin{document}\n"
CAPKEY = {}     # caption TeX -> field key (each distinct caption is converted once)
SENT = "QQFIELD{:06d}QQ"
SPLIT = re.compile(r"<p>QQFIELD(\d{6})QQ</p>\n?")


# ------------------------------------------------------------------ TeX reading helpers
def group(s, i):
    """s[i] == '{' -> (content, index after the matching '}')."""
    depth, j, n = 0, i, len(s)
    while j < n:
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
    raise ValueError(f"unbalanced braces at {i}: {s[i:i + 80]!r}")


def skip_ws(s, i):
    while i < len(s) and s[i] in " \t\n":
        i += 1
    return i


def opt_arg(s, i):
    j = skip_ws(s, i)
    if j < len(s) and s[j] == "[":
        depth, k = 0, j + 1
        while k < len(s):
            c = s[k]
            if c == "\\":
                k += 2
                continue
            if c == "{":
                depth += 1
            elif c == "}":
                depth -= 1
            elif c == "]" and depth == 0:
                return s[j + 1:k], k + 1
            k += 1
    return None, i


def args(s, i, n):
    out = []
    for _ in range(n):
        i = skip_ws(s, i)
        if i >= len(s) or s[i] != "{":
            raise ValueError(f"missing argument at {i}: {s[i:i + 60]!r}")
        a, i = group(s, i)
        out.append(a)
    return out, i


def sub_macro(s, name, nargs, fn, nopt=0):
    """Replace every \\name[opt]...{a1}...{an} by fn(opts, args); arguments are passed as written."""
    out, pos = [], 0
    for m in re.finditer(r"\\" + name + r"(?![A-Za-z@])", s):
        if m.start() < pos:
            continue
        i = m.end()
        opts = []
        try:
            for _ in range(nopt):
                o, i = opt_arg(s, i)
                opts.append(o)
            a, i = args(s, i, nargs)
        except ValueError:
            continue
        out.append(s[pos:m.start()])
        out.append(fn(opts, a))
        pos = i
    out.append(s[pos:])
    return "".join(out)


def strip_comments(s):
    return re.sub(r"(?<!\\)%[^\n]*\n[ \t]*", "", s)


# ------------------------------------------------------------------ per-language state
class Doc:
    def __init__(self, lang):
        self.lang = lang
        self.math = []          # QQMT tokens
        self.pics = []          # QQTP tokens (masked pictures)
        self.figs = []          # QQFG tokens: (hash, kind)
        self.readings = []      # QQMR tokens: dict
        self.passages = []      # QQPB tokens: (page, n)
        self.pages = []         # QQSP tokens: (page, label)
        self.captions = {}

    def tok(self, kind, i):
        return f"QQ{kind}{i:05d}QQ"


def fig_hash(tex):
    return hashlib.sha256(tex.encode("utf-8")).hexdigest()[:16]


def close_at_depth0(s, i, closer):
    """Index after the first `closer` at brace depth 0 from position i (escaped characters skipped), or -1."""
    depth, n, L = 0, len(s), len(closer)
    while i < n:
        c = s[i]
        if c == "\\":
            if depth == 0 and s.startswith(closer, i) and closer[0] == "\\":
                return i + L
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth < 0:
                return -1
        elif depth == 0 and c == "$" and closer.startswith("$") and s.startswith(closer, i):
            return i + L
        i += 1
    return -1


def find_math(s):
    """[(start, end)] of the formulas of s (text with the pictures masked); closers are taken at brace depth 0, so a
    formula inside a group of the formula (a TikZ node, a \\text) does not end it."""
    out = []
    pat = re.compile(r"\\begin\{(" + MATHENV + r")\}|\\ensuremath\s*\{|(?<!\\)\\\[|(?<!\\)\\\(|(?<!\\)\$\$|(?<!\\)\$")
    i = 0
    while True:
        m = pat.search(s, i)
        if not m:
            break
        if m.group(0).startswith("\\ensuremath"):
            try:
                _, end = group(s, m.end() - 1)
            except ValueError:
                i = m.end()
                continue
        elif m.group(1):
            env = m.group(1)
            e = s.find("\\end{" + env + "}", m.end())
            if e < 0:
                break
            end = e + len("\\end{" + env + "}")
        else:
            op = m.group(0)
            end = close_at_depth0(s, m.end(), {"\\[": "\\]", "\\(": "\\)", "$$": "$$", "$": "$"}[op])
            if end < 0:
                i = m.end()
                continue
        out.append((m.start(), end))
        i = end
    return out


MATH_FIXES = [
    (r"\\uuline(?![A-Za-z])", r"\\underline\\underline"),
    (r"\\(?:uline|uwave|dashuline|dotuline)(?![A-Za-z])", r"\\underline"),
    (r"\\sout(?![A-Za-z])", r"\\cancel"),
    (r"\\xout(?![A-Za-z])", r"\\cancel"),
]


MJ_DEFINED = {"relax"}      # macros the site's MathJax configuration defines (g8_render.MATHJAX_MACROS)
# macros of the notebook formulas that MathJax 3.2.2 lacks (used when the MathJax folder is not available)
MJ_FALLBACK_UNSUPPORTED = {
    "rotatebox", "multicolumn", "makebox", "textcircled", "lhook", "joinrel", "ensuremath", "shortstack",
    "textquotedbl", "GelfandCircledIndex", "parbox", "raggedright", "cline", "ooalign", "arraystretch", "linewidth",
    "textsuperscript", "begingroup", "endgroup", "setlength", "arraycolsep", "minipage"}
_MJ_KNOWN = []


def mathjax_known():
    """The words of MathJax's TeX input code (the macro and environment names it defines are among them), or None."""
    if not _MJ_KNOWN:
        import os
        root = os.environ.get("GELFAND_MATHJAX")
        words = None
        if root and (Path(root) / "tex-chtml.js").exists():
            words = set()
            for f in [Path(root) / "tex-chtml.js"] + sorted((Path(root) / "input" / "tex" / "extensions").glob("*.js")):
                words |= set(re.findall(r"[A-Za-z]+", f.read_text(encoding="utf-8", errors="replace")))
        _MJ_KNOWN.append(words)
    return _MJ_KNOWN[0]


def mj_unsupported(t):
    """Macro and environment names of formula t that MathJax cannot typeset (such a formula is typeset by LaTeX in
    G4, as a figure)."""
    names = {m.group(1) for m in re.finditer(r"\\([A-Za-z]+|.)", t) if m.group(1).isalpha()}
    names |= set(re.findall(r"\\begin\{([A-Za-z]+)\*?\}", t))
    names -= MJ_DEFINED
    known = mathjax_known()
    if known is None:
        return sorted(names & MJ_FALLBACK_UNSUPPORTED)
    return sorted(n for n in names if n not in known)


TEXT_MATH_ONLY = r"\\(underline|cancel|phantom|vphantom|hphantom)(?![A-Za-z])"


def depth_at(s, i):
    d, j = 0, 0
    while j < i:
        c = s[j]
        if c == "\\":
            j += 2
            continue
        d += c == "{"
        d -= c == "}"
        j += 1
    return d


def split_text_group(c):
    """The content of \\text{...} -> MathJax's form.  MathJax's text mode lacks \\underline, \\cancel and the phantoms
    (it has them only in math mode): \\text{A \\underline{X} B} becomes \\text{A }\\underline{\\text{X}}\\text{ B}.
    \\hfill and \\strut are dropped, a \\text or \\mbox inside the text is unwrapped; formulas inside the text ($...$)
    are left alone."""
    c = re.sub(r"\\(?:hfill|strut)(?![A-Za-z])", " ", c)
    for _ in range(3):
        c2 = sub_macro(c, "(?:text|textrm|mbox|textnormal)", 1, lambda o, a: a[0])
        if c2 == c:
            break
        c = c2
    while c.strip().startswith("{"):        # {\uuline{x}}: a group around the whole text
        try:
            inner, e = group(c, c.index("{"))
        except ValueError:
            break
        if c[e:].strip():
            break
        c = inner
    def math_spans(s):
        return [(m.start(), m.end()) for m in re.finditer(r"(?<!\\)\$[^$]*\$|\\\(.*?\\\)", s, re.S)]
    maths = math_spans(c)
    c = re.sub(r"\\(?:ldots|dots|textellipsis)(?![A-Za-z])\s?",
               lambda m: m.group(0) if any(a <= m.start() < b for a, b in maths) else "…", c)
    maths = math_spans(c)
    inmath = lambda i: any(a <= i < b for a, b in maths)
    res, pos = [], 0
    for m in re.finditer(TEXT_MATH_ONLY, c):
        if m.start() < pos or inmath(m.start()) or depth_at(c, m.start()) != 0:
            continue
        j, cmds = m.end(), [m.group(1)]
        while True:
            mm = re.match(r"\s*\\(underline|cancel)(?![A-Za-z])", c[j:])
            if not mm:
                break
            cmds.append(mm.group(1))
            j += mm.end()
        j = skip_ws(c, j)
        if j >= len(c) or c[j] != "{":
            continue
        try:
            arg, e = group(c, j)
        except ValueError:
            continue
        if c[pos:m.start()]:
            res.append("\\text{" + c[pos:m.start()] + "}")
        inner = split_text_group(arg)
        for k in reversed(cmds):
            inner = "\\" + k + "{" + inner + "}"
        res.append(inner)
        pos = e
    if c[pos:] or not res:
        res.append("\\text{" + c[pos:] + "}")
    return "".join(res)


def fix_text_modes(t):
    out, pos = [], 0
    for m in re.finditer(r"\\(?:text|textrm|mbox|textnormal)\s*\{", t):
        if m.start() < pos:
            continue
        try:
            c, e = group(t, m.end() - 1)
        except ValueError:
            continue
        if not re.search(TEXT_MATH_ONLY + r"|\\(?:hfill|strut|text|textrm|mbox|textnormal|ldots|dots|textellipsis)"
                                          r"(?![A-Za-z])", c):
            continue
        out.append(t[pos:m.start()])
        out.append(split_text_group(c))
        pos = e
    out.append(t[pos:])
    t = "".join(out)
    # \tag{\text{A}}: the tag is text already
    t = re.sub(r"(\\tag\*?\{)\\text\{([^{}]*)\}\}", r"\1\2}", t)
    # \tag*{(1)\hfill}: the tag is text
    for _ in range(3):
        t2 = re.sub(r"(\\tag\*?\{[^{}]*?)\\hfill(?![A-Za-z])", r"\1 ", t)
        if t2 == t:
            break
        t = t2
    return t


def nest_unary(t):
    """\\underline\\underline{x} (LaTeX takes the second \\underline as the argument; MathJax wants braces)."""
    for _ in range(6):
        m = re.search(r"\\(underline|overline|cancel)\s*(\\(?:underline|overline|cancel))\s*\{", t)
        if not m:
            break
        try:
            arg, e = group(t, m.end() - 1)
        except ValueError:
            break
        t = t[:m.start()] + "\\" + m.group(1) + "{" + m.group(2) + "{" + arg + "}}" + t[e:]
    return t


def brace_sets(t):
    """{\\underset{a}{U}}_{t}: MathJax counts the underscript as a subscript ("double subscripts")."""
    out, pos = [], 0
    for m in re.finditer(r"\\(?:underset|overset|stackrel)(?![A-Za-z])", t):
        if m.start() < pos:
            continue
        try:
            _a, i = args(t, m.end(), 2)
        except ValueError:
            continue
        j = skip_ws(t, i)
        if j < len(t) and t[j] in "_^":
            out.append(t[pos:m.start()])
            out.append("{" + t[m.start():i] + "}")
            pos = i
    out.append(t[pos:])
    return "".join(out)


def fix_math(t):
    for a, b in MATH_FIXES:
        t = re.sub(a, b, t)
    t = re.sub(r"\\raisebox\{[^{}]*\}(?:\[[^\]]*\]){0,2}", "", t)
    t = re.sub(r"\\(?:resizebox|scalebox)\{[^{}]*\}(?:\{[^{}]*\})?", "", t)
    t = sub_macro(t, "textcolor", 2, lambda o, a: "{" + a[1] + "}")
    t = re.sub(r"\\color\{[^{}]*\}", "", t)
    t = re.sub(r"\\(?:Needspace|vspace\*?)\{[^{}]*\}", "", t)
    t = re.sub(r"\\(?:smallskip|medskip|bigskip|noindent|centering|par)(?![A-Za-z])", " ", t)
    return brace_sets(nest_unary(fix_text_modes(t)))


def caption_defs(pre):
    out = {}
    for name in CAPTION_MACROS:
        m = re.search(r"\\newcommand\{\\" + name + r"\}\{", pre)
        if m:
            out[name], _ = group(pre, m.end() - 1)
    return out


TEXT_DROP = [
    r"\\Needspace\*?\{[^{}]*\}", r"\\(?:vspace|vskip)\*?\{[^{}]*\}", r"\\pdfbookmark(?:\[[^\]]*\])?\{[^{}]*\}\{[^{}]*\}",
    r"\\section\*?\{[^{}]*\}", r"\\phantomsection", r"\\label\{[^{}]*\}", r"\\linespread\{[^{}]*\}",
    r"\\(?:smallskip|medskip|bigskip|noindent|centering|raggedright|raggedleft|clearpage|newpage|pagebreak|"
    r"nopagebreak|begingroup|endgroup|selectfont|small|scriptsize|footnotesize|tiny|normalsize|large|Large|"
    r"sffamily|rmfamily|ttfamily|bfseries|mdseries|itshape|upshape|relax|hfill|vfill|strut)(?![A-Za-z])",
    r"\\color\{[^{}]*\}", r"\\pagenumbering\{[^{}]*\}", r"\\setlength\{[^{}]*\}\{[^{}]*\}",
]


def text_transform(t, d):
    """Text-mode TeX (formulas masked) -> TeX that pandoc reads, with markers for what pandoc cannot express."""
    for name, val in d.captions.items():
        t = re.sub(r"\\" + name + r"(?![A-Za-z])\s?", lambda m, v=val: v + " ", t)
    for p in TEXT_DROP:
        t = re.sub(p, " ", t)
    t = re.sub(r"\\(?:hspace\*?\{[^{}]*\}|enspace|quad|qquad|thinspace|,|;|:)(?![A-Za-z])", " ", t)
    t = re.sub(r"\\rule(?:\[[^\]]*\])?\{[^{}]*\}\{[^{}]*\}", "———", t)
    t = re.sub(r"\\(?:begin|end)\{minipage\}(?:\[[^\]]*\])*(?:\{[^{}]*\})?", "\n\n", t)
    t = re.sub(r"\\begin\{varwidth\}\{[^{}]*\}|\\end\{varwidth\}", "\n\n", t)
    for _ in range(6):      # nested wrappers are unwrapped one level per round
        before = t
        for name, nopt, nargs in (("GelfandFitDiagram", 0, 1), ("resizebox", 0, 3), ("scalebox", 0, 2),
                                  ("mbox", 0, 1), ("makebox", 2, 1), ("raisebox", 2, 2), ("fbox", 0, 1),
                                  ("framebox", 2, 1), ("parbox", 3, 2),
                                  ("shortstack", 1, 1)):
            t = sub_macro(t, name, nargs, lambda o, a: a[-1], nopt=nopt)
        t = sub_macro(t, "uwave", 1, lambda o, a: "\\underline{QQWVQQ " + a[0] + "}")
        t = sub_macro(t, "uuline", 1, lambda o, a: "\\underline{QQUUQQ " + a[0] + "}")
        t = sub_macro(t, "dashuline", 1, lambda o, a: "\\underline{QQDUQQ " + a[0] + "}")
        t = sub_macro(t, "dotuline", 1, lambda o, a: "\\underline{QQDUQQ " + a[0] + "}")
        t = sub_macro(t, "uline", 1, lambda o, a: "\\underline{" + a[0] + "}")
        t = sub_macro(t, "xout", 1, lambda o, a: "\\sout{" + a[0] + "}")
        if t == before:
            break
    t = re.sub(r"\\par(?![A-Za-z])", "\n\n", t)
    return t


# ------------------------------------------------------------------ preparation of one language
def prepare(lang):
    src = latex_dir() / f"gelfand-{LANGS[lang]}-chapters01-34-complete-first1527.tex"
    s = src.read_text(encoding="utf-8")
    pre, body = s.split("\\begin{document}", 1)
    body = body.split("\\end{document}")[0]
    d = Doc(lang)
    d.captions = caption_defs(pre)
    # scan crops of the marked readings: \expandafter\def\csname evidence-KEY\endcsname{...}
    crops = {}
    full = pre + body
    for m in re.finditer(r"\\expandafter\\def\\csname evidence-([^\\]+)\\endcsname\{", full):
        try:
            val, _ = group(full, m.end() - 1)
        except ValueError:
            continue
        crops[m.group(1)] = re.findall(r"figures/([^{}\s]+?\.png)", val)
    del full
    body = strip_comments(body)
    body = re.sub(r"\\expandafter\\def\\csname [^\\]+\\endcsname\{(?:[^{}]|\{[^{}]*\})*\}", "", body)
    # TikZ libraries loaded and styles set in the text: G4 adds them to the figures' preamble
    d.fig_setup = []

    def keep_setup(m):
        if m.group(0) not in d.fig_setup:
            d.fig_setup.append(m.group(0))
        return ""
    body = re.sub(r"\\usetikzlibrary\{[^{}]*\}", keep_setup, body)
    for m in re.finditer(r"\\tikzset\{", body):
        try:
            val, _ = group(body, m.end() - 1)
        except ValueError:
            continue
        if "\\tikzset{" + val + "}" not in d.fig_setup:
            d.fig_setup.append("\\tikzset{" + val + "}")
    # the first passage of a page opens before the page's \SourcePage: put the page marker first
    body = re.sub(r"(\\begin\{GelfandAdjacentEvidence\}\{(GELFAND-P\d{6})\}\{[^{}]+\}(?:\s|\\Needspace\*?\{[^{}]*\})*)"
                  r"(\\SourcePage\{\2\}\{[^{}]*\})", r"\3\n\1", body)
    # 1. mask pictures
    def mask_env(t, env):
        out, pos = [], 0
        tokpat = re.compile(r"\\(begin|end)\{" + env + r"\}")
        for m in re.finditer(r"\\begin\{" + env + r"\}", t):
            if m.start() < pos:
                continue
            depth, e = 0, -1
            for mm in tokpat.finditer(t, m.start()):       # nested pictures (a picture in a node) end together
                depth += 1 if mm.group(1) == "begin" else -1
                if depth == 0:
                    e = mm.end()
                    break
            if e < 0:
                continue
            out.append(t[pos:m.start()])
            d.pics.append((env, t[m.start():e]))
            out.append(d.tok("TP", len(d.pics) - 1))
            pos = e
        out.append(t[pos:])
        return "".join(out)
    body = mask_env(body, "tikzpicture")
    body = mask_env(body, "tikzcd")
    unmask = lambda t: re.sub(r"QQTP(\d{5})QQ", lambda m: d.pics[int(m.group(1))][1], t)
    # 2. formulas: with TikZ inside, or with macros MathJax lacks -> figure (typeset by LaTeX in G4); else -> math token
    out, pos = [], 0
    d.mj_figs = collections.Counter()
    for a, b in find_math(body):
        out.append(body[pos:a])
        tex = body[a:b]
        mt = None
        if "\\tikz" not in tex and "QQTP" not in tex:
            t2 = "\\(" + group(tex, tex.index("{"))[0] + "\\)" if tex.startswith("\\ensuremath") else tex
            mt = fix_math(t2)
            bad = mj_unsupported(mt)
            if bad:
                d.mj_figs.update(bad)
                mt = None
        if mt is None:
            full = unmask(tex)
            h = fig_hash(full)
            disp = not (tex.startswith("$") and not tex.startswith("$$")) and not tex.startswith("\\(") \
                and not tex.startswith("\\ensuremath")
            d.figs.append((h, "math-display" if disp else "math-inline", full))
            out.append((" " if not disp else "\n\n") + d.tok("FG", len(d.figs) - 1) + (" " if not disp else "\n\n"))
        else:
            d.math.append(mt)
            out.append(d.tok("MT", len(d.math) - 1))
        pos = b
    out.append(body[pos:])
    body = "".join(out)

    # 3. remaining pictures and inline \tikz -> figures
    def pic(m):
        env, tex = d.pics[int(m.group(1))]
        h = fig_hash(tex)
        d.figs.append((h, "tikzcd" if env == "tikzcd" else "picture", tex))
        return "\n\n" + d.tok("FG", len(d.figs) - 1) + "\n\n"
    body = re.sub(r"QQTP(\d{5})QQ", pic, body)
    out, pos = [], 0
    for m in re.finditer(r"\\tikz(?![A-Za-z])", body):
        if m.start() < pos:
            continue
        i = m.end()
        o, i = opt_arg(body, i)
        j = skip_ws(body, i)
        try:
            if j < len(body) and body[j] == "{":
                _, e = group(body, j)
            else:
                depth, e = 0, j
                while e < len(body):
                    c = body[e]
                    if c == "\\":
                        e += 2
                        continue
                    if c == "{":
                        depth += 1
                    elif c == "}":
                        depth -= 1
                    elif c == ";" and depth == 0:
                        e += 1
                        break
                    e += 1
        except ValueError:
            continue
        tex = unmask(body[m.start():e])
        tex = re.sub(r"QQMT(\d{5})QQ", lambda mm: d.math[int(mm.group(1))], tex)
        out.append(body[pos:m.start()])
        d.figs.append((fig_hash(tex), "tikz-inline", tex))
        out.append(" " + d.tok("FG", len(d.figs) - 1) + " ")
        pos = e
    out.append(body[pos:])
    body = "".join(out)
    # \includegraphics in the text (scan details placed by hand)
    body = sub_macro(body, "includegraphics", 1,
                     lambda o, a: " QQIMG" + re.sub(r"[^A-Za-z0-9._-]", "", Path(a[0]).name) + "QQIMG ", nopt=1)

    # 4. marked readings (also those written inside the note of another one)
    def readings_pass(t):
        for name, (kind, n) in READING_MACROS.items():
            def rd(o, a, kind=kind, n=n):
                page, label = a[0].strip(), a[1].strip()
                cap = a[3] if n == 4 else {"unclear": "\\ReadingCaption", "incomplete": "\\IncompleteCaption",
                                           "figure": "\\DiagramCaption", "evidence": ""}[kind]
                d.readings.append({"kind": kind, "page": page, "label": label, "note": a[2], "caption": cap,
                                   "crops": crops.get(f"{page}-{label}", [])})
                return "\n\n" + d.tok("MR", len(d.readings) - 1) + "\n\n"
            t = sub_macro(t, name, n, rd)
        return t
    body = readings_pass(body)
    k = 0
    while k < len(d.readings):
        d.readings[k]["note"] = readings_pass(d.readings[k]["note"])
        k += 1
    # 5. passages and pages
    def pb(m):
        d.passages.append((m.group(1), m.group(2).strip()))
        return "\n\n" + d.tok("PB", len(d.passages) - 1) + "\n\n"
    body = re.sub(r"\\begin\{GelfandAdjacentEvidence\}\{(GELFAND-P\d{6})\}\{([^{}]+)\}", pb, body)
    body = body.replace("\\end{GelfandAdjacentEvidence}", "\n\nQQPEQQ\n\n")

    def sp(m):
        d.pages.append((m.group(1), m.group(2)))
        return "\n\n" + d.tok("SP", len(d.pages) - 1) + "\n\n"
    body = re.sub(r"\\SourcePage\{(GELFAND-P\d{6})\}\{([^{}]*)\}", sp, body)
    body = text_transform(body, d)
    for r in d.readings:
        r["note"] = text_transform(r["note"], d)
        r["caption"] = text_transform(r["caption"], d).strip()
    return d, body, crops


def restore_math(t, d):
    return re.sub(r"QQMT(\d{5})QQ", lambda m: d.math[int(m.group(1))], t)


# ------------------------------------------------------------------ pandoc
def pandoc(tex):
    r = subprocess.run(["pandoc", "-f", "latex", "-t", "html", "--mathjax", "--wrap=none"],
                       input=tex.encode("utf-8"), capture_output=True, timeout=3600)
    return r.stdout.decode("utf-8"), r.stderr.decode("utf-8", "replace"), r.returncode


def convert(fields, depth=0):
    """fields: [(key, tex)] -> ({key: html or None}, [messages])"""
    doc = PANDOC_PRE + "".join(f"\n\n\\par {SENT.format(i)}\\par\n\n{tex}\n" for i, (k, tex) in enumerate(fields))
    doc += "\n\n\\par " + SENT.format(len(fields)) + "\\par\n\n\\end{document}\n"
    html, err, rc = pandoc(doc)
    parts = SPLIT.split(html)
    got = {int(parts[j]): parts[j + 1] for j in range(1, len(parts) - 1, 2)}
    if rc == 0 and len(got) == len(fields) + 1 and all(i in got for i in range(len(fields) + 1)):
        return {fields[i][0]: got[i].strip() for i in range(len(fields))}, []
    if len(fields) == 1:
        return {fields[0][0]: None}, [f"{fields[0][0]}: {err.strip()[:300]}"]
    mid = len(fields) // 2
    a, wa = convert(fields[:mid], depth + 1)
    b, wb = convert(fields[mid:], depth + 1)
    a.update(b)
    return a, wa + wb


def convert_all(fields, batch=60, workers=4):
    chunks = [fields[i:i + batch] for i in range(0, len(fields), batch)]
    res, msgs = {}, []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for got, w in ex.map(convert, chunks):
            res.update(got)
            msgs += w
    return res, msgs


# ------------------------------------------------------------------ HTML after pandoc
def post(html, d, notes_html):
    html = re.sub(r"<p>\s*QQPB(\d{5})QQ\s*</p>", lambda m: passage_open(d, int(m.group(1))), html)
    html = re.sub(r"<p>\s*QQPC(\d{5})QQ\s*</p>", lambda m: passage_open(d, int(m.group(1)), cont=True), html)
    html = re.sub(r"<p>\s*QQPEQQ\s*</p>", "</div>", html)
    html = re.sub(r"<p>\s*QQMR(\d{5})QQ\s*</p>", lambda m: reading_html(d, int(m.group(1)), notes_html, "div"), html)
    html = re.sub(r"QQMR(\d{5})QQ", lambda m: reading_html(d, int(m.group(1)), notes_html, "span"), html)
    return finish(html, d)


def finish(html, d):
    html = re.sub(r"<p>\s*QQFG(\d{5})QQ\s*</p>", lambda m: fig_html(d, int(m.group(1)), "div"), html)
    html = re.sub(r"QQFG(\d{5})QQ", lambda m: fig_html(d, int(m.group(1)), "span"), html)
    html = re.sub(r"QQIMG([A-Za-z0-9._-]+)QQIMG", lambda m: f'<img class="crop" src="@@CROPS@@{m.group(1)}" alt="">', html)
    html = html.replace("<u>QQWVQQ ", '<u class="wave">').replace("<u>QQUUQQ ", '<u class="double">')
    html = html.replace("<u>QQDUQQ ", '<u class="dash">')
    html = re.sub(r'<span style="color: ?orange[^"]*">', '<span class="ed">', html)
    html = re.sub(r'<span style="color: ?[^"]*">', '<span class="ink">', html)
    return html


def passage_open(d, i, cont=False):
    page, n = d.passages[i]
    p = page.replace("GELFAND-", "")
    if cont:
        return f'<div class="passage cont" data-n="{n}" data-of="{p}.{n}">'
    return f'<div class="passage" id="{p}.{n}" data-n="{n}">'


def fig_html(d, i, tag):
    h, kind, _ = d.figs[i]
    return f'<{tag} class="fig fig-{kind}" data-fig="{h}"></{tag}>'


def reading_html(d, i, notes_html, tag, depth=0):
    r = d.readings[i]
    p = r["page"].replace("GELFAND-", "")
    note = notes_html.get(f"n{i}") or H.escape(r["note"])
    if depth < 3:   # a marked reading inside the note of another one
        note = re.sub(r"<p>\s*QQMR(\d{5})QQ\s*</p>|QQMR(\d{5})QQ",
                      lambda m: reading_html(d, int(m.group(1) or m.group(2)), notes_html, "span", depth + 1), note)
    cap = notes_html.get(CAPKEY.get(r["caption"], "")) or H.escape(r["caption"])
    cap = re.sub(r"^<p>(.*)</p>$", r"\1", cap.strip(), flags=re.S)
    crops = "".join(f'<img class="crop" loading="lazy" src="@@CROPS@@{H.escape(c)}" alt="">' for c in r["crops"])
    capt = f'<strong class="mrcap">{cap}</strong> '
    note = note.strip()
    if tag == "span":
        inner = (f'<span class="crops">{crops}</span>' if crops else "") + \
                f'<span class="mrnote">{capt}{re.sub(r"</?p>", " ", note)}</span>'
    else:
        note = (note.replace("<p>", "<p>" + capt, 1) if note.startswith("<p>") else f"<p>{capt}</p>{note}")
        inner = (f'<div class="crops">{crops}</div>' if crops else "") + f'<div class="mrnote">{note}</div>'
    return (f'<{tag} class="mr mr-{r["kind"]}" id="r-{p}-{H.escape(r["label"])}" data-label="{H.escape(r["label"])}">'
            f'{inner}</{tag}>')


# ------------------------------------------------------------------ main
def build(lang):
    CAPKEY.clear()
    d, body, crops = prepare(lang)
    chunks = re.split(r"QQSP(\d{5})QQ", body)
    # chunks: [front matter, idx0, text0, idx1, text1, ...]
    # A passage that runs over a page break is closed at the end of the page and continues on the next one
    # (QQPC: a continuation, without the passage's id); a passage that opens just before the next page's marker,
    # with nothing of it on this page, opens on the next page.
    pages = {}
    carry = None
    for j in range(1, len(chunks), 2):
        page, label = d.pages[int(chunks[j])]
        t = chunks[j + 1]
        if carry is not None:
            t = f"\n\nQQP{carry[1]}{carry[0]:05d}QQ\n\n" + t
            carry = None
        state = None
        for m in re.finditer(r"QQP([BC])(\d{5})QQ|QQPEQQ", t):
            state = (int(m.group(2)), m.group(1), m.start(), m.end()) if m.group(1) else None
        if state is not None:
            idx, kind, st, en = state
            if not re.sub(r"QQ(?:WV|UU|DU)QQ", "", t[en:]).strip():
                t = t[:st]
                carry = (idx, kind)
            else:
                t += "\n\nQQPEQQ\n\n"
                carry = (idx, "C")
        pages[page.replace("GELFAND-", "")] = {"label": label, "tex": restore_math(t, d)}
    if carry is not None:
        log(f"G3 {lang}: a passage is still open at the end of the text")
    fields = [(p, v["tex"]) for p, v in pages.items()]
    notes = []
    for i, r in enumerate(d.readings):
        notes.append((f"n{i}", restore_math(r["note"], d)))
        if r["caption"] and r["caption"] not in CAPKEY:
            CAPKEY[r["caption"]] = f"c{len(CAPKEY)}"
            notes.append((CAPKEY[r["caption"]], restore_math(r["caption"], d)))
    log(f"G3 {lang}: {len(pages)} pages, {len(d.passages)} passages, {len(d.readings)} marked readings, "
        f"{len(d.figs)} figures, {len(d.math)} formulas; converting {len(fields)} pages and {len(notes)} notes")
    notes_html, m1 = convert_all(notes, batch=400)
    notes_html = {k: (finish(v, d) if v else v) for k, v in notes_html.items()}
    pages_html, m2 = convert_all(fields, batch=40)
    out = {}
    pas_by_page, rd_by_page = collections.defaultdict(list), collections.defaultdict(list)
    for pg, n in d.passages:
        pas_by_page[pg.replace("GELFAND-", "")].append(n)
    for r in d.readings:
        rd_by_page[r["page"].replace("GELFAND-", "")].append([r["kind"], r["label"]])
    for p, v in pages.items():
        h = pages_html.get(p)
        if h is None:
            h = "<pre class=\"unconverted\">" + H.escape(v["tex"]) + "</pre>"
        h = post(h, d, notes_html)
        out[p] = {"label": v["label"], "html": h, "passages": pas_by_page.get(p, []), "readings": rd_by_page.get(p, []),
                  "figures": sorted({f for f in re.findall(r'data-fig="([0-9a-f]{16})"', h)})}
    figs = {h: {"tex": tex, "kind": kind, "lang": lang} for h, kind, tex in d.figs}
    for p, v in out.items():
        for h in v["figures"]:
            if h in figs:
                figs[h].setdefault("page", p)
    unconverted = [p for p in pages if pages_html.get(p) is None] + [k for k, v in notes_html.items() if v is None]
    log(f"G3 {lang}: formulas typeset as figures because MathJax lacks {sum(d.mj_figs.values())} uses of "
        f"{dict(d.mj_figs.most_common())}")
    return out, figs, crops, m1 + m2, unconverted, d.fig_setup


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    res = {}
    for lang in LANGS:
        res[lang] = build(lang)
    allfigs, allcrops = {}, {}
    wjson(OUT / "figure_setup.json", {lang: res[lang][5] for lang in LANGS})
    for lang in LANGS:
        out, figs, crops, msgs, unconv, _setup = res[lang]
        wjson(OUT / f"{lang}.json", out, indent=None)
        for h, f in figs.items():
            if h in allfigs:
                allfigs[h]["langs"] = sorted(set(allfigs[h].get("langs", [allfigs[h]["lang"]])) | {lang})
            else:
                allfigs[h] = dict(f, langs=[lang])
        allcrops.update(crops)
        report(f"g3_pandoc_{lang}", [(m,) for m in msgs], ["message"])
        report(f"g3_unconverted_{lang}", [(u,) for u in unconv], ["page or note"])
    wjson(OUT / "figures.json", allfigs, indent=None)
    wjson(OUT / "crops.json", allcrops, indent=None)
    # parity
    ru, en = res["ru"][0], res["en"][0]
    diffs = []
    for p in sorted(set(ru) | set(en)):
        a, b = ru.get(p), en.get(p)
        if not a or not b:
            diffs.append((p, "page", "missing in " + ("en" if a else "ru"), ""))
            continue
        if a["passages"] != b["passages"]:
            diffs.append((p, "passages", a["passages"], b["passages"]))
        ra, rb = collections.Counter(map(tuple, a["readings"])), collections.Counter(map(tuple, b["readings"]))
        if ra != rb:
            diffs.append((p, "readings", sorted((ra - rb).elements()), sorted((rb - ra).elements())))
    report("g3_parity", diffs, ["page", "what", "ru", "en"])
    # LaTeX outside math
    latex = []
    for lang, (out, *_r) in res.items():
        for p, v in out.items():
            t = re.sub(r'<span class="math (?:inline|display)">.*?</span>', " ", v["html"], flags=re.S)
            t = H.unescape(re.sub(r"<[^>]+>", " ", t))
            for m in re.finditer(r"\\[A-Za-z]+|QQ[A-Z]+\d*QQ", t):
                latex.append((lang, p, m.group(0), t[max(0, m.start() - 40):m.end() + 30].replace("\n", " ")))
    report("g3_latex", latex, ["lang", "page", "match", "context"])
    # well-formed pages: balanced blocks, element ids unique on the page
    struct = []
    for lang, (out, *_r) in res.items():
        for p, v in out.items():
            h = v["html"]
            if h.count("<div") != h.count("</div>"):
                struct.append((lang, p, f"div {h.count('<div')} open, {h.count('</div>')} closed"))
            ids = collections.Counter(re.findall(r'\sid="([^"]+)"', h))
            for k, n in ids.items():
                if n > 1:
                    struct.append((lang, p, f"id {k} x{n}"))
    report("g3_structure", struct, ["lang", "page", "problem"])
    n_unconv = {l: len(res[l][4]) for l in LANGS}
    npages = {l: len(res[l][0]) for l in LANGS}
    lc = collections.Counter(m for _, _, m, _ in latex)
    print(f"G3 notebook: pages ru {npages['ru']}, en {npages['en']}; passages ru "
          f"{sum(len(v['passages']) for v in ru.values())}, en {sum(len(v['passages']) for v in en.values())}; "
          f"marked readings ru {sum(len(v['readings']) for v in ru.values())}, en "
          f"{sum(len(v['readings']) for v in en.values())}; figures {len(allfigs)} distinct; crops {len(allcrops)}; "
          f"parity differences {len(diffs)}; unconverted {n_unconv}; TeX outside math {len(latex)} "
          f"{lc.most_common(10)}; structure problems {len(struct)} {struct[:5]}")
    ok = npages["ru"] == npages["en"] == 1527 and not diffs and not any(n_unconv.values()) and not latex \
        and not struct
    print("G3", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
