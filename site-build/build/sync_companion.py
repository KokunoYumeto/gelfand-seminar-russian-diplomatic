"""Copy the companion's data into companion/ of this repository and register new chapters in the works registry.

usage: python sync_companion.py --returns DIR [--kit DIR] [--reader DIR]
  --returns  the folder holding one folder per returned chapter (GY1965/, GY1966/, ...); from each, the seven data
             files GY<year>_{talks.json, items.json, problems.json, overview.tex, development.tex, corrections.csv,
             references.bib} are copied to companion/years/GY<year>/ (nothing else of the return)
  --kit      the chapter kit: CHAPTER_FORMAT.md, gelfand_companion.sty, build_chapter.py, build_global_reader.py are
             copied to companion/kit/
  --reader   the global reader: GelfandSeminar_companion.tex and companion_references.bib go to companion/reader/

A chapter seen for the first time is added to site-build/data/works.json with the date of its newest data file as the
date it was returned (edit it when the receipt date is known).  Every copied file is scanned for local paths, e-mail
addresses and names that must not be published; the copy stops if one is found.
"""
import argparse
import datetime
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import COMPANION, DATA, DATA_FILES, YEARS_DIR, rjson, wjson, log  # noqa: E402

KIT_FILES = ("CHAPTER_FORMAT.md", "gelfand_companion.sty", "build_chapter.py", "build_global_reader.py")
READER_FILES = ("GelfandSeminar_companion.tex", "companion_references.bib")
MODEL = "GPT-6 Astra (ChatGPT Pro mode)"


def forbidden_patterns():
    """Patterns that must not appear in public files: local paths, e-mail addresses, and the words listed (one per
    line) in data/forbidden_public_terms.txt, which is not committed."""
    # the words are split so that this file does not match its own patterns
    pats = [r"[A-Za-z]:\\\\?Users", r"[A-Za-z]:/Users", r"(?<![\w.])/Us" r"ers/", r"App" r"Data", r"(?i:scratch" r"pad)",
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9.-]*[A-Za-z]{2,}"]
    extra = DATA / "forbidden_public_terms.txt"
    if extra.exists():
        pats += ["(?i:" + re.escape(w.strip()) + ")" for w in extra.read_text(encoding="utf-8").splitlines() if w.strip()]
    return re.compile("|".join(f"(?:{p})" for p in pats))


# e-mail-like strings that are not addresses (BibTeX keys never contain @; DOIs and URLs can)
EMAIL_OK = re.compile(r"https?://\S+|doi\.org/\S+|10\.\d{4,}/\S+")


def scan_text(text, name, pat):
    bad = []
    for m in pat.finditer(text):
        s = m.group(0)
        ctx = text[max(0, m.start() - 60):m.end() + 20]
        if "@" in s and EMAIL_OK.search(ctx[max(0, ctx.find(s) - 60):]):
            continue
        bad.append((name, s, ctx.replace("\n", " ")))
    return bad


def years_of(tag):
    """Academic years of a chapter, from its talks (the year of each dated talk)."""
    from common import acad
    talks = json.loads((YEARS_DIR / tag / f"{tag}_talks.json").read_text(encoding="utf-8"))
    ys = sorted({acad(t["date"]) for t in talks if re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(t.get("date") or ""))})
    return ys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--returns", required=True)
    ap.add_argument("--kit")
    ap.add_argument("--reader")
    a = ap.parse_args()
    pat = forbidden_patterns()
    bad = []
    plan = []
    for d in sorted(Path(a.returns).glob("GY*")):
        tag = d.name
        if not re.fullmatch(r"GY\d{4}", tag):
            continue
        files = [d / f"{tag}_{k}" for k in DATA_FILES]
        if not all(f.exists() for f in files):
            log(f"{tag}: not all seven data files present; skipped")
            continue
        for f in files:
            bad += scan_text(f.read_text(encoding="utf-8"), f.name, pat)
            plan.append((f, YEARS_DIR / tag / f.name))
    if a.kit:
        for k in KIT_FILES:
            f = Path(a.kit) / k
            bad += scan_text(f.read_text(encoding="utf-8"), f.name, pat)
            plan.append((f, COMPANION / "kit" / k))
    if a.reader:
        for k in READER_FILES:
            f = Path(a.reader) / k
            bad += scan_text(f.read_text(encoding="utf-8"), f.name, pat)
            plan.append((f, COMPANION / "reader" / k))
    if bad:
        for b in bad[:50]:
            log("FORBIDDEN", *b)
        sys.exit(f"{len(bad)} forbidden strings; nothing copied")
    changed = 0
    for src, dst in plan:
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.exists() or dst.read_bytes() != src.read_bytes():
            shutil.copyfile(src, dst)
            changed += 1
    # register new chapters
    reg = rjson(DATA / "works.json")
    have = {w.get("tag") for w in reg["works"]}
    for d in sorted(YEARS_DIR.glob("GY*")):
        tag = d.name
        if tag in have:
            continue
        newest = max(f.stat().st_mtime for f in d.iterdir() if f.is_file())
        returned = datetime.datetime.fromtimestamp(newest, datetime.timezone.utc).date().isoformat()
        ys = years_of(tag)
        reg["works"].append({
            "id": f"companion-{tag}", "kind": "companion-chapter", "tag": tag, "years": ys,
            "title": {"en": f"Critical companion, {', '.join(y.replace('-', '–') for y in ys)}",
                      "ru": f"Критический комментарий, {', '.join(y.replace('-', '–') for y in ys)}"},
            "authors": [MODEL], "model": MODEL, "written": returned,
            "source": {"repository": "KokunoYumeto/gelfand-seminar-russian-diplomatic", "path": f"companion/years/{tag}/"},
            "include": True})
        log(f"registered {tag} {ys} returned {returned}")
    reg["works"].sort(key=lambda w: (w["kind"] != "notebook", w.get("tag") or w["id"]))
    wjson(DATA / "works.json", reg)
    print(f"{len(plan)} files checked, {changed} copied or updated")


if __name__ == "__main__":
    main()
