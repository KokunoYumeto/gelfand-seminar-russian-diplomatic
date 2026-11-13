"""Shared helpers of the Gelfand seminar site build: paths, JSON and text I/O, hashing, the works registry with its
include flags, and small formatting helpers.

Paths are relative to the repository (this file is site-build/build/common.py).  Build output goes to the folder named
by the environment variable GELFAND_WORK (default site-build/_work, which is not committed):
    WORK/cache/<release tag>/   the locked release assets and the extracted LaTeX archive
    WORK/ir/                    intermediate data (registry, converted companion fields, links, staleness)
    WORK/site/                  the built site
    WORK/reports/               check reports
    WORK/dist/                  the site tarball for deployment
"""
import datetime
import hashlib
import json
import os
import re
import sys
from pathlib import Path

BUILD = Path(__file__).resolve().parent
SB = BUILD.parent                      # site-build/
REPO = SB.parent                       # repository root
DATA = SB / "data"
ASSETS = SB / "assets"
COMPANION = REPO / "companion"
YEARS_DIR = COMPANION / "years"
LOCK = SB / "gelfand.lock.json"
WORK = Path(os.environ.get("GELFAND_WORK") or (SB / "_work")).resolve()
CACHE = WORK / "cache"
IR = WORK / "ir"
REPORTS = WORK / "reports"
DIST = WORK / "dist"
REPO_SLUG = "KokunoYumeto/gelfand-seminar-russian-diplomatic"
REPO_URL = f"https://github.com/{REPO_SLUG}"
ISSUES_URL = f"{REPO_URL}/issues"
MCCME_LIST = "https://old.mccme.ru/gelfand/notes/all-links.html"
DATA_FILES = ("talks.json", "items.json", "problems.json", "overview.tex", "development.tex", "corrections.csv",
              "references.bib")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def site_dir():
    """Output folder of the site; GELFAND_SITE_OUT overrides it (used by the removal test build)."""
    return Path(os.environ.get("GELFAND_SITE_OUT") or (WORK / "site"))


def rjson(p, default=None):
    p = Path(p)
    if not p.exists():
        if default is not None:
            return default
        raise FileNotFoundError(p)
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def wjson(p, obj, indent=1):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)
        f.write("\n")
    os.replace(tmp, p)


def wtext(p, s):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(s)


def rtext(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def lock():
    return rjson(LOCK)


def release_dir():
    """WORK/cache/<tag>/ of the locked release."""
    return CACHE / lock()["release"]["tag"]


def latex_dir():
    return release_dir() / "x"


# ------------------------------------------------------------------ works registry (DECISIONS_USER item 7)
def works():
    """data/works.json with each work's include flag resolved (registry flag, then GELFAND_EXCLUDE, a comma-separated
    list of work ids switched off for one build)."""
    reg = rjson(DATA / "works.json")
    excl = {w.strip() for w in os.environ.get("GELFAND_EXCLUDE", "").split(",") if w.strip()}
    out = []
    for w in reg["works"]:
        w = dict(w)
        w["include"] = bool(w.get("include", True)) and w["id"] not in excl
        out.append(w)
    return out


def work_map(all_=False):
    return {w["id"]: w for w in works() if all_ or w["include"]}


def chapter_tags(all_=False):
    """Companion chapters (works of kind companion-chapter) whose data folder exists, in order."""
    out = []
    for w in works():
        if w["kind"] != "companion-chapter" or not (all_ or w["include"]):
            continue
        if (YEARS_DIR / w["tag"] / f"{w['tag']}_items.json").exists():
            out.append(w["tag"])
    return sorted(out)


def transcription_included():
    m = work_map(all_=True)
    return {lang: m.get(f"notes-{lang}", {}).get("include", False) for lang in ("ru", "en")}


def report(name, rows, header=None):
    p = REPORTS / f"{name}.tsv"
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        if header:
            f.write("\t".join(header) + "\n")
        for r in rows:
            f.write("\t".join(str(x).replace("\t", " ").replace("\n", " ") for x in r) + "\n")
    return p


# ------------------------------------------------------------------ years and dates
def acad(date):
    """Academic year of an ISO date: 'YYYY-YY' (August starts the year)."""
    y, mo = int(date[:4]), int(date[5:7])
    a = y if mo >= 8 else y - 1
    return f"{a}-{(a + 1) % 100:02d}"


def pid(n):
    return f"P{int(n):06d}"


def pnum(p):
    return int(str(p)[-6:])


def parse_pages(s):
    """'P000090-P000092, P000095' -> [90, 91, 92, 95] (tolerant of 'GELFAND-' prefixes and en dashes)."""
    out = []
    s = str(s or "").replace("GELFAND-", "").replace("–", "-").replace("—", "-")
    for part in re.split(r"[,;]\s*|\s+and\s+", s):
        part = part.strip()
        if not part:
            continue
        m = re.fullmatch(r"P?(\d{1,6})\s*-\s*P?(\d{1,6})", part)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            if a <= b and b - a < 400:
                out.extend(range(a, b + 1))
            continue
        for m in re.finditer(r"P(\d{6})", part):
            out.append(int(m.group(1)))
    return sorted(set(out))


def ranges(ps):
    out, start, prev = [], None, None
    for p in sorted(set(ps)):
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


def fmt_ranges(ps, sep="–"):
    return ", ".join(pid(a) if a == b else f"{pid(a)}{sep}{pid(b)}" for a, b in ranges(ps))


MONTHS_EN = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
MONTHS_RU = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября",
             "ноября", "декабря"]
MONTHS_RU_NOM = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь",
                 "ноябрь", "декабрь"]


def fdate(lang, iso):
    """'1976-09-06' -> '6 Sep 1976' / '6 сентября 1976 г.'; partial dates are shown as given."""
    iso = str(iso or "")
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", iso[:10])
    if not m:
        m2 = re.fullmatch(r"(\d{4})-(\d{2})", iso[:7]) if len(iso) == 7 else None
        if m2 and 1 <= int(m2.group(2)) <= 12:   # not an academic year such as 1984-85
            y, mo = int(m2.group(1)), int(m2.group(2))
            return f"{MONTHS_EN[mo - 1]} {y}" if lang == "en" else f"{MONTHS_RU_NOM[mo - 1]} {y} г."
        return iso
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if not (1 <= mo <= 12):
        return iso
    rest = iso[10:]   # a remark after the date, e.g. ' (reconstructed)', is kept
    return (f"{d} {MONTHS_EN[mo - 1]} {y}" if lang == "en" else f"{d} {MONTHS_RU[mo - 1]} {y} г.") + rest


def year_label(y):
    """'1976-77' -> '1976–77'."""
    return y.replace("-", "–")


def now_utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
