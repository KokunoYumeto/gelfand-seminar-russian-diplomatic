"""G7 staleness: which notebook pages changed after each chapter's commentary was written.

Each chapter was written against the Russian text of its pages as attached to its prompt (<TAG>_ru.tex, cut page by
page from the cumulative reader of that day).  That text is compared, page by page, with the Russian cumulative
LaTeX of the locked release.  A page whose text differs is stale for that chapter: the site shows the notice of
design §6.2 on the talk and on every item that cites the page.

Where the attached text is read from, in order: the folder named by GELFAND_PACKAGES (<dir>/<TAG>/<TAG>_ru.tex or
<dir>/_TO_DO/<TAG>/<TAG>_ru.tex), raw/prompts/<TAG>/attached/<TAG>_ru.tex in this repository, or the path that
raw/prompts/<TAG>/ATTACHMENTS.md gives inside raw/pro_returns/.  Its SHA-256 is checked against ATTACHMENTS.md when that
file is present.

Comparison: lines starting with \\expandafter\\def are dropped (the package builder dropped them), trailing spaces are
removed and runs of blank lines are collapsed.  A page that still differs is classified: 'text' (the transcription
outside the evidence notes), 'notes' (the transcriber's notes on readings: \\Unclear, \\Incomplete, \\SourceFigure,
\\EvidenceBlock), 'marking' (the same notes, re-marked, e.g. a doubtful reading now marked as a plain excerpt),
'figures' (tikzpicture drawings).  A page whose only differences are layout commands (spacing, centring, colour,
environment wrappers) is not counted as revised.
Output: WORK/ir/stale_pages.json; reports/g7_stale.tsv.  Accepted when every chapter's attached text is found (and
matches ATTACHMENTS.md where present) and every page of the chapter is found in the release.
"""
import difflib
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import IR, REPO, chapter_tags, latex_dir, lock, report, rjson, rtext, sha256_file, wjson

RU = "gelfand-russian-chapters01-34-complete-first1527.tex"


def split_pages(tex):
    marks = list(re.finditer(r"\\SourcePage\{GELFAND-P(\d{6})\}", tex))
    out = {}
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else tex.find("\\end{document}", m.start())
        out[int(m.group(1))] = tex[m.start():end if end > 0 else len(tex)]
    return out


def norm(s):
    lines = [l.rstrip() for l in s.split("\n") if not l.startswith("\\expandafter\\def")]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def args(s, i, n):
    """parse n brace groups starting at s[i] (skipping spaces); return (list, end)"""
    out = []
    for _ in range(n):
        while i < len(s) and s[i] in ' \t\n':
            i += 1
        if i >= len(s) or s[i] != '{':
            return None, i
        d = 0
        j = i
        while j < len(s):
            c = s[j]
            if c == '\\':
                j += 2
                continue
            if c == '{':
                d += 1
            elif c == '}':
                d -= 1
                if d == 0:
                    break
            j += 1
        out.append(s[i + 1:j])
        i = j + 1
    return out, i


KIND = {'ReadingCaption': 'reading', 'IncompleteCaption': 'incomplete', 'DiagramCaption': 'figure',
        'GelfandExcerptCaption': 'excerpt'}
ARITY = {'Unclear': (3, 'reading'), 'Incomplete': (3, 'incomplete'), 'SourceFigure': (3, 'figure'), 'EvidenceBlock': (4, None)}
EVRE = re.compile(r'\\(Unclear|Incomplete|SourceFigure|EvidenceBlock)(?![A-Za-z])')
LAYOUT = re.compile(r'\\(smallskip|medskip|bigskip|par|centering|noindent|hfill|begingroup|endgroup|GelfandFitDiagram|linewidth|baselineskip|relax)(?![A-Za-z])')
LAYOUT_ARG = re.compile(r'\\(color|Needspace|vspace\*?|hspace\*?)\{[^{}]*\}')
ENV = re.compile(r'\\(begin|end)\{(center|minipage|flushright|flushleft|scope|GelfandAdjacentEvidence)\}(\[[^\]]*\])?(\{[^{}]*\}){0,2}')


def canon(page):
    s = '\n'.join(l for l in page.split('\n') if not l.startswith('\\expandafter\\def'))
    evs = []
    out = []
    pos = 0
    while True:
        m = EVRE.search(s, pos)
        if not m:
            out.append(s[pos:])
            break
        out.append(s[pos:m.start()])
        n, kind = ARITY[m.group(1)]
        a, end = args(s, m.end(), n)
        if a is None:
            out.append(m.group(0))
            pos = m.end()
            continue
        if kind is None:
            cap = a[3].strip().lstrip('\\')
            kind = KIND.get(cap, cap)
        evs.append((a[1].strip(), ' '.join(a[2].split()), kind))
        out.append(' ')
        pos = end
    s = ''.join(out)
    figs = re.findall(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', s, re.S)
    s = re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', ' ', s, flags=re.S)
    s = LAYOUT_ARG.sub(' ', s)
    s = LAYOUT.sub(' ', s)
    s = ENV.sub(' ', s)
    s = re.sub(r'\\SourcePage\{[^{}]*\}\{[^{}]*\}', ' ', s)
    s = ' '.join(s.split())
    figs = [' '.join(f.split()) for f in figs]
    return s, evs, figs



def attached(tag):
    """(path, how it was found, sha256 expected from ATTACHMENTS.md or None)"""
    att = REPO / "raw" / "prompts" / tag / "ATTACHMENTS.md"
    want, inner = None, None
    if att.exists():
        t = att.read_text(encoding="utf-8")
        m = re.search(rf"`{tag}_ru\.tex`: [\d,]+ bytes, SHA-256 `([0-9a-f]{{64}})`", t)
        want = m.group(1) if m else None
        m = re.search(rf"\]\((?:\.\./\.\./)?(pro_returns/{tag}/[^)]*_ru\.tex)\)", t)
        inner = REPO / "raw" / m.group(1) if m else None
    cands = []
    pk = os.environ.get("GELFAND_PACKAGES")
    if pk:
        cands += [(Path(pk) / tag / f"{tag}_ru.tex", "package folder"),
                  (Path(pk) / "_TO_DO" / tag / f"{tag}_ru.tex", "package folder")]
    cands.append((REPO / "raw" / "prompts" / tag / "attached" / f"{tag}_ru.tex", "raw/prompts attached"))
    if inner:
        cands.append((inner, "raw/pro_returns copy"))
    for p, how in cands:
        if p.exists():
            return p, how, want
    return None, None, want


def main():
    rel = lock()["release"]
    cur = split_pages(rtext(latex_dir() / RU))
    out = {"release": rel["tag"], "release_date": rel["created_at"][:10], "chapters": {}}
    rows, problems = [], []
    for tag in chapter_tags(all_=True):
        p, how, want = attached(tag)
        if not p:
            problems.append(f"{tag}: attached Russian text not found")
            continue
        h = sha256_file(p)
        verified = (h == want) if want else None
        if want and h != want:
            problems.append(f"{tag}: attached text SHA-256 differs from ATTACHMENTS.md")
        text = rtext(p)
        head = re.search(r"cumulative working reader (\S+)\.", text[:2000])
        old = split_pages(text)
        stale, missing, sizes, kinds, layout_only = [], [], {}, {}, []
        for n, s in sorted(old.items()):
            if n not in cur:
                missing.append(n)
                continue
            a, b = norm(s), norm(cur[n])
            if a == b:
                continue
            ta, ea, fa = canon(s)
            tb, eb, fb = canon(cur[n])
            cats = []
            if ta != tb:
                cats.append("text")
            if [(l, t) for l, t, k in ea] != [(l, t) for l, t, k in eb]:
                cats.append("notes")
            elif ea != eb:
                cats.append("marking")
            if fa != fb:
                cats.append("figures")
            if not cats:
                layout_only.append(n)
                continue
            stale.append(n)
            kinds[str(n)] = cats
            d = [l for l in difflib.unified_diff(a.split("\n"), b.split("\n"), lineterm="", n=0)
                 if l[:1] in "+-" and not l.startswith(("+++", "---"))]
            sizes[str(n)] = len(d)
        if missing:
            problems.append(f"{tag}: pages not in the release: {missing[:10]}")
        out["chapters"][tag] = {"attached_sha256": h, "attachments_md_verified": verified, "found_in": how,
                                "written_against": head.group(1) if head else None, "pages": sorted(old),
                                "stale_pages": stale, "what_changed": kinds, "changed_lines": sizes,
                                "layout_only_pages": layout_only}
        cnt = {k: sum(1 for v in kinds.values() if k in v) for k in ("text", "notes", "marking", "figures")}
        rows.append((tag, len(old), len(stale), cnt["text"], cnt["notes"], cnt["marking"], cnt["figures"],
                     len(layout_only), how, verified, head.group(1) if head else ""))
    wjson(IR / "stale_pages.json", out)
    report("g7_stale", rows, ["chapter", "pages", "revised pages", "of which text", "notes on readings",
                              "reading marks only", "figures", "layout-only changes (not counted)",
                              "attached text from", "SHA-256 = ATTACHMENTS.md", "written against"])
    for r in rows:
        print(f"  {r[0]}: {r[2]} of {r[1]} pages revised since the commentary was written (text {r[3]}, notes "
              f"{r[4]}, marks {r[5]}, figures {r[6]}; layout only {r[7]})")
    ok = not problems
    for pr in problems:
        print("  PROBLEM:", pr)
    print(f"G7 staleness against {rel['tag']}: {sum(r[2] for r in rows)} stale pages in "
          f"{sum(1 for r in rows if r[2])} of {len(rows)} chapters")
    print("G7", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
