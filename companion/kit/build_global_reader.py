"""Build the global reader of the Gelfand seminar companion: one book with every returned year as a chapter, a
single bibliography (the years' .bib files merged, first entry of each key kept) and one table of contents.

Each year is rebuilt from its seven data files with build_chapter.py first (so a chapter always matches its data).
Reads   returns/GY*/GY*_{talks.json,items.json,problems.json,overview.tex,development.tex,corrections.csv,
        references.bib}  (the seven data files of each returned year)
Writes  reader/YEAR/... (the years' chapter files), reader/GelfandSeminar_companion.tex, reader/companion_references.bib
        and, with --pdf, reader/GelfandSeminar_companion.pdf (xelatex, bibtex, xelatex, xelatex).
usage: python -I build_global_reader.py [--pdf]"""
import pathlib
import re
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
KIT = pathlib.Path(__file__).resolve().parent
ROOT = KIT.parent
OUT = ROOT / "reader"
OUT.mkdir(exist_ok=True)
DATA = ("talks.json", "items.json", "problems.json", "overview.tex", "development.tex", "corrections.csv",
        "references.bib")
years = sorted(d for d in (ROOT / "returns").glob("GY*") if (d / f"{d.name}_items.json").exists())
inputs, bibs = [], []
seen_problems = set()
for d in years:
    tag = d.name
    w = OUT / tag
    w.mkdir(exist_ok=True)
    for f in DATA:
        shutil.copyfile(d / f"{tag}_{f}", w / f"{tag}_{f}")
    r = subprocess.run([sys.executable, "-I", str(KIT / "build_chapter.py"), tag, str(w)], capture_output=True,
                       text=True, encoding="utf-8")
    print(r.stdout.strip() or r.stderr.strip()[-400:])
    if r.returncode:
        sys.exit(f"{tag}: build_chapter.py failed")
    # a label an earlier year already defined (a problem that recurs; a record on the boundary of two packages, such as
    # a year heading) gets a year-qualified form in the later chapter: each label is defined once, and the later
    # chapter's own links go to its own entry
    ch = w / f"{tag}_chapter.tex"
    text = ch.read_text(encoding="utf-8")
    mine = set(re.findall(r"\\label\{((?:prob|rec|item|talk):[^}]+)\}", text))
    for lab in sorted(mine & seen_problems):
        text = text.replace(f"\\label{{{lab}}}", f"\\label{{{lab}:{tag}}}")
        text = text.replace(f"\\hyperref[{lab}]", f"\\hyperref[{lab}:{tag}]")
        text = text.replace(f"\\ref{{{lab}}}", f"\\ref{{{lab}:{tag}}}").replace(f"\\pageref{{{lab}}}", f"\\pageref{{{lab}:{tag}}}")
    ch.write_text(text, encoding="utf-8")
    seen_problems |= mine
    inputs.append(f"{tag}/{tag}_chapter.tex")
    bibs.append((w / f"{tag}_references.bib").read_text(encoding="utf-8"))

# one bibliography: entries split at each '@', the first entry of every key kept (later years reuse the keys)
seen, entries = set(), []
for text in bibs:
    for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,.*?(?=^@|\Z)", text, re.S | re.M):
        if m.group(1) not in seen:
            seen.add(m.group(1))
            entries.append(m.group(0).rstrip() + "\n")
(OUT / "companion_references.bib").write_text("\n".join(entries), encoding="utf-8")

first, last = years[0].name[2:], years[-1].name[2:]
span = f"{first}--{(int(last) + 1) % 100:02d}"
main = [
    "\\documentclass[11pt,oneside]{book}",
    "\\usepackage[a4paper,margin=22mm,headheight=15pt]{geometry}",
    "\\usepackage{gelfand_companion}",
    "\\setlength{\\emergencystretch}{2em}",
    # no line runs into the margin: a paragraph that cannot be set within the usual tolerance gets looser lines
    # (long inline formulas and compounds in the later years' fields); 13 Nov 2026
    "\\setlength{\\emergencystretch}{3em}\\tolerance=9999",
    # table of contents: room for four-digit page numbers, and ragged entry lines (long titles break instead of
    # running into the page number), and room for section numbers such as 10.36 and 10.36.10; 13 Nov 2026
    "\\makeatletter\\renewcommand{\\@pnumwidth}{3em}\\renewcommand{\\@tocrmarg}{4em plus 1fil}"
    "\\patchcmd{\\l@chapter}{1.5em}{2.2em}{}{}"
    "\\renewcommand*{\\l@section}{\\@dottedtocline{1}{1.5em}{3.6em}}"
    "\\renewcommand*{\\l@subsection}{\\@dottedtocline{2}{5.1em}{4.8em}}\\makeatother",
    f"\\hypersetup{{pdftitle={{The Gelfand Seminar {span}: A Critical Companion}}}}",
    "\\begin{document}",
    "\\begin{titlepage}\\centering\\vspace*{6em}",
    "{\\Huge The Gelfand Seminar\\par}\\vspace{1em}",
    f"{{\\Large A critical companion, {span.replace('--', '–')}\\par}}\\vspace{{2em}}",
    "{\\large The seminar notes of the Moscow Mathematical Society seminar of I.~M.~Gelfand, year by year: the talks,"
    " every mathematical statement with its later fate and present status, the open problems, and corrections to"
    " the transcription.\\par}",
    "\\end{titlepage}",
    "\\tableofcontents",
]
main += [f"\\input{{{p}}}" for p in inputs]
main += ["\\bibliographystyle{plainnat}", "\\bibliography{companion_references}", "\\end{document}", ""]
(OUT / "GelfandSeminar_companion.tex").write_text("\n".join(main), encoding="utf-8")
print(f"reader: {len(years)} years ({', '.join(d.name for d in years)}), {len(entries)} references")

if "--pdf" in sys.argv:
    import os
    env = dict(os.environ, TEXINPUTS=f".{os.pathsep}{KIT}{os.pathsep}")
    for cmd in (["xelatex", "-interaction=nonstopmode", "GelfandSeminar_companion.tex"],
                ["bibtex", "GelfandSeminar_companion"],
                ["xelatex", "-interaction=nonstopmode", "GelfandSeminar_companion.tex"],
                ["xelatex", "-interaction=nonstopmode", "GelfandSeminar_companion.tex"]):
        subprocess.run(cmd, cwd=OUT, env=env, capture_output=True)
    log = (OUT / "GelfandSeminar_companion.log").read_text(encoding="latin-1")
    pages = re.search(r"Output written on .*?\((\d+) pages", log)
    print("errors:", len(re.findall(r"^! ", log, re.M)), "| pages:", pages.group(1) if pages else None,
          "| undefined references:", len(re.findall(r"Reference `[^']+' on page \d+ undefined", log)),
          "| multiply defined labels:", len(re.findall(r"multiply defined", log)))
