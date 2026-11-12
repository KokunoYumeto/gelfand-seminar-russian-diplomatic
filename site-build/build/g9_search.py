"""G9 search: Pagefind indexes the site into SITE/pagefind/, one index per language (chosen by each page's
<html lang>); the search pages /{l}/search/ load the index of their language.

Pages are indexed from their main block (data-pagefind-body: companion pages and the notebook text; the notebook
column of the talk pages and the headers of the notebook pages are left out), with a "section" filter (talks and
items, notebook text, problems, years, ...). The indexer is the vendored Pagefind 1.3.0 (site-build/data/
vendor.lock.json): GELFAND_PAGEFIND names its executable (pagefind or pagefind_extended from the npm package
@pagefind/windows-x64, or the binary for another system).
Check: the index lists both languages, and each language's page count equals the number of indexed pages of that
language in the site.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import DATA, log, report, rjson, site_dir  # noqa: E402


def exe():
    p = os.environ.get("GELFAND_PAGEFIND")
    if p and Path(p).exists():
        return p
    w = shutil.which("pagefind_extended") or shutil.which("pagefind")
    if w:
        return w
    sys.exit("G9: Pagefind not found (set GELFAND_PAGEFIND to the pagefind executable, version in data/vendor.lock.json)")


def main():
    out = site_dir()
    want = rjson(DATA / "vendor.lock.json")["pagefind"]["version"]
    ex = exe()
    v = subprocess.run([ex, "--version"], capture_output=True, text=True).stdout.strip()
    if want not in v:
        sys.exit(f"G9: Pagefind {v!r} is not the locked version {want}")
    dest = out / "pagefind"
    if dest.exists():
        shutil.rmtree(dest)
    r = subprocess.run([ex, "--site", str(out), "--output-subdir", "pagefind"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    log(r.stdout[-1500:])
    if r.returncode != 0:
        log(r.stderr[-1500:])
        sys.exit(f"G9: Pagefind exit {r.returncode}")
    entry = rjson(dest / "pagefind-entry.json")
    langs = {k: v.get("page_count") for k, v in entry.get("languages", {}).items()}
    # pages that carry an index body, per language
    expect = {}
    for l in ("ru", "en"):
        n = 0
        for f in (out / l).rglob("index.html"):
            if "data-pagefind-body" in f.read_text(encoding="utf-8", errors="replace")[:200000]:
                n += 1
        expect[l] = n
    size = sum(f.stat().st_size for f in dest.rglob("*") if f.is_file())
    rows = [(l, langs.get(l), expect[l]) for l in ("ru", "en")]
    report("g9_search", rows, ["language", "pages in the index", "indexed pages in the site"])
    ok = all(langs.get(l) == expect[l] and expect[l] > 0 for l in ("ru", "en"))
    print(f"G9 search: Pagefind {v}; index languages {langs}; indexed pages in the site {expect}; "
          f"{size / 1e6:.1f} MB in pagefind/")
    print("G9", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
