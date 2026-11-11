"""Build one year's chapter of the Gelfand seminar companion from the files of that year (see CHAPTER_FORMAT.md),
check them, and write the chapter and a small driver that compiles it alone.

usage: python build_chapter.py GY1965 [DIR]
  reads   DIR/GY1965_talks.json, _items.json, _problems.json, _overview.tex, _development.tex, _corrections.csv,
          _references.bib (DIR defaults to the current directory)
  writes  DIR/GY1965_chapter.tex (the chapter) and DIR/GY1965_test.tex (driver: xelatex, bibtex, xelatex, xelatex)
Exit status 1 if a check fails; every problem found is printed."""
# Compatibility amendments for this deliverable: render the supplied problem
# index, check missing item/problem references and sequential IDs, and use an
# A4 one-sided test driver. The untouched supplied files are in code/kit_original.
import collections
import csv
import json
import pathlib
import re
import sys

TAG = sys.argv[1]
D = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else pathlib.Path(".")
YEAR = int(TAG[2:6])
# optional column of TAG_corrections.csv (GY1965 report, proposal (i))
CORRECTION_TYPES = {"transcription", "translation", "ambiguity", "faithful_error", "provenance"}
CLASSES = set("ABCDEF")
errors, warnings = [], []


def load_json(name):
    p = D / f"{TAG}_{name}.json"
    if not p.exists():
        errors.append(f"missing {p.name}")
        return []
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except ValueError as e:
        errors.append(f"{p.name}: invalid JSON: {e}")
        return []


def text(name):
    p = D / f"{TAG}_{name}"
    if not p.exists():
        errors.append(f"missing {p.name}")
        return ""
    return p.read_text(encoding="utf-8")


def esc(s):
    """Plain text -> LaTeX."""
    s = str(s or "")
    rep = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{",
           "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(rep.get(c, c) for c in s)


talks = load_json("talks")
items = load_json("items")
problems = load_json("problems")
overview = text("overview.tex")
development = text("development.tex")
bib = text("references.bib")
bibkeys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib))

# ---- checks
TALK_KEYS = ["record", "date", "speaker", "pages", "title", "summary"]
ITEM_KEYS = ["id", "record", "pages", "kind", "title", "notes", "statement", "class", "fate", "present_status",
             "literal_correctness", "publication_match", "verification", "development", "refs", "confidence"]
recs = {}
for t in talks:
    for k in TALK_KEYS:
        if k not in t:
            errors.append(f"talk {t.get('record')}: missing key {k}")
    if t.get("record") in recs:
        errors.append(f"talk record {t.get('record')} twice")
    recs[t.get("record")] = t
ids = set()
per_rec = collections.defaultdict(list)
for x in items:
    for k in ITEM_KEYS:
        if k not in x:
            errors.append(f"item {x.get('id')}: missing key {k}")
    i = x.get("id", "")
    if i in ids:
        errors.append(f"item id {i} twice")
    ids.add(i)
    if not re.fullmatch(rf"{YEAR}-\d+\.\d+|{YEAR + 1}-\d+\.\d+", i):
        errors.append(f"item id {i}: expected {YEAR}-<record>.<n>")
    if x.get("record") not in recs:
        errors.append(f"item {i}: record {x.get('record')} has no talk entry")
    if x.get("class") not in CLASSES:
        errors.append(f"item {i}: class {x.get('class')!r} is not one of A-F")
    if x.get("class") in ("C", "D") and not x.get("worth"):
        warnings.append(f"item {i}: class {x.get('class')} without 'worth'")
    for k in x.get("refs") or []:
        if k not in bibkeys:
            errors.append(f"item {i}: bib key {k} not in {TAG}_references.bib")
    per_rec[x.get("record")].append(x)
for p in problems:
    for k in ("id", "title", "statement", "occurrences", "status", "status_date", "refs"):
        if k not in p:
            errors.append(f"problem {p.get('id')}: missing key {k}")
    for o in p.get("occurrences") or []:
        if o.startswith(f"{YEAR}-") and o not in ids:
            errors.append(f"problem {p.get('id')}: occurrence {o} is not an item of this year")
    for k in p.get("refs") or []:
        if k not in bibkeys:
            errors.append(f"problem {p.get('id')}: bib key {k} not in {TAG}_references.bib")
problem_ids = [p.get('id') for p in problems]
if len(problem_ids) != len(set(problem_ids)):
    errors.append('duplicate problem IDs')
for record, record_items in per_rec.items():
    expected = [f'{YEAR}-{record}.{n}' for n in range(1, len(record_items) + 1)]
    if [x['id'] for x in record_items] != expected:
        errors.append(f'record {record}: item numbers are not consecutive')
for x in items:
    if x.get('problem') and x['problem'] not in problem_ids:
        errors.append(f"item {x['id']}: missing problem {x['problem']}")
cited = set(re.findall(r"\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}", overview + development +
                       json.dumps(items, ensure_ascii=False).replace("\\\\", "\\") +
                       json.dumps(talks, ensure_ascii=False).replace("\\\\", "\\")))
for group in cited:
    for k in group.split(","):
        if k.strip() and k.strip() not in bibkeys:
            errors.append(f"\\cite key {k.strip()} not in {TAG}_references.bib")
corrections = []
cp = D / f"{TAG}_corrections.csv"
if cp.exists():
    rows = list(csv.DictReader(cp.open(encoding="utf-8")))
    for r in rows:
        for k in ("page", "place", "transcription_reads", "should_read", "evidence", "applies_to"):
            if k not in r:
                errors.append(f"corrections.csv: missing column {k}")
                break
    for r in rows:
        t = (r.get("type") or "").strip()
        if t and t not in CORRECTION_TYPES:
            errors.append(f"corrections.csv: type {t!r} not one of {sorted(CORRECTION_TYPES)}")
    corrections = rows
else:
    errors.append(f"missing {cp.name}")

# ---- chapter
acad = sorted({(int(t["date"][:4]) if int(t["date"][5:7]) >= 8 else int(t["date"][:4]) - 1)
               for t in talks if re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(t.get("date", "")))}) or [YEAR]
names = [f"{a}--{(a + 1) % 100:02d}" for a in acad]
title = (f"The academic year {names[0]}" if len(names) == 1 else
         "The academic years " + ", ".join(names[:-1]) + " and " + names[-1])
L = [f"% Generated by build_chapter.py from the {TAG} files. Do not edit by hand; edit the files and rebuild.",
     f"\\chapter{{{title}}}\\label{{ch:{YEAR}}}", overview.strip(), ""]
for t in talks:
    L.append(f"\\GStalk{{{t.get('record')}}}{{{esc(t.get('date'))}}}{{{esc(t.get('speaker'))}}}"
             f"{{{esc(t.get('pages'))}}}{{{esc(t.get('title'))}}}")
    L.append(str(t.get("summary", "")).strip())
    L.append("")
    for x in per_rec.get(t.get("record"), []):
        L.append(f"\\begin{{GSitem}}{{{esc(x.get('id'))}}}{{{esc(x.get('class'))}}}{{{esc(x.get('title'))}}}")
        spk = f"; {esc(x['speaker'])}" if x.get("speaker") else ""
        L.append(f"\\GSfield{{Kind; source}}{{{esc(x.get('kind'))}; \\GSpage{{{esc(x.get('pages'))}}}{spk}}}")
        L.append(f"\\GSfield{{The notes}}{{{x.get('notes', '')}}}")
        L.append(f"\\GSfield{{Statement}}{{{x.get('statement', '')}}}")
        if x.get("reconstruction"):
            L.append(f"\\GSfield{{Reconstruction}}{{{x['reconstruction']}}}")
        L.append(f"\\GSfield{{Fate}}{{{x.get('fate', '')}}}")
        L.append(f"\\GSfield{{Present status}}{{{x.get('present_status', '')}}}")
        L.append(f"\\GSfield{{Assessment}}{{literal statement: {esc(x.get('literal_correctness'))}; publication match: "
                 f"{esc(x.get('publication_match'))}; verification: {esc(x.get('verification'))}; development: "
                 f"{esc(x.get('development'))}; confidence: {esc(x.get('confidence'))}"
                 + (f"; problem \\hyperref[prob:{x['problem']}]{{{esc(x['problem'])}}}" if x.get("problem") else "")
                 + "}")
        if x.get("worth"):
            L.append(f"\\GSfield{{Worth developing}}{{{x['worth']}}}")
        L.append("\\end{GSitem}")
    L.append("")
if development.strip():
    L += [f"\\section{{Developments}}\\label{{dev:{YEAR}}}", development.strip(), ""]
if problems:
    L += [f"\\section{{Problem index}}\\label{{problems:{YEAR}}}",
          "Earlier-year occurrence identifiers are retained as text; current-year identifiers link to their entries.", ""]
    for p in problems:
        L.append(f"\\subsection{{{esc(p['id'])}: {esc(p['title'])}}}\\label{{prob:{p['id']}}}")
        L.append(p['statement'])
        occurrences = []
        for occurrence in p['occurrences']:
            if occurrence in ids:
                occurrences.append(f"\\hyperref[item:{occurrence}]{{{esc(occurrence)}}}")
            else:
                occurrences.append(esc(occurrence))
        L.append("\\par\\noindent\\textit{Occurrences:} " + ", ".join(occurrences) + ".")
        L.append("\\par\\noindent\\textit{Status (" + esc(p['status_date']) + "):} " + p['status'])
        L.append("")
if corrections:
    L += [f"\\section{{Corrections to the transcription and translation}}\\label{{corr:{YEAR}}}",
          "The evidence distinguishes a transcription correction from a mathematical emendation of wording faithfully preserved in the notebook."]
    for r in corrections:
        kind_ = f"; {esc(r['type'].replace('_', ' '))}" if (r.get("type") or "").strip() else ""
        L.append(f"\\subsection*{{{esc(r.get('page'))} ({esc(r.get('applies_to'))}{kind_}): {r.get('place', '')}}}")
        for field,label in [('transcription_reads','Transcription reads'),
                            ('should_read','Critical reading'),('evidence','Evidence')]:
            L.append(f"\\noindent\\textit{{{label}.}} {r.get(field,'')}\\par")
(D / f"{TAG}_chapter.tex").write_text("\n".join(L) + "\n", encoding="utf-8")
(D / f"{TAG}_test.tex").write_text(
    "\\documentclass[11pt,oneside]{book}\n"
    "\\usepackage[a4paper,margin=22mm,headheight=15pt]{geometry}\n"
    "\\usepackage{gelfand_companion}\n"
    "\\setlength{\\emergencystretch}{2em}\n"
    f"\\hypersetup{{pdftitle={{Gelfand Seminar {YEAR}--{(YEAR + 1) % 100:02d}: A Critical Companion}}}}\n"
    "\\begin{document}\n"
    f"\\input{{{TAG}_chapter.tex}}\n\\bibliographystyle{{plainnat}}\n\\bibliography{{{TAG}_references}}\n"
    "\\end{document}\n", encoding="utf-8")

cls = collections.Counter(x.get("class") for x in items)
print(f"{TAG}: {len(talks)} talks, {len(items)} items ({', '.join(f'{k} {cls[k]}' for k in sorted(cls))}), "
      f"{len(problems)} problems, {len(bibkeys)} references, {len(corrections)} corrections")
for w in warnings:
    print("warning:", w)
for e in errors:
    print("ERROR:", e)
sys.exit(1 if errors else 0)
