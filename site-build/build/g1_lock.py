"""G1 lock: fix the transcription release and the companion files the site is built from.

usage: python g1_lock.py [--release TAG] [--keep]
  Without --release the newest release whose tag starts with 'readers-a4-' is taken (from the GitHub API).  With
  --keep the release already named in gelfand.lock.json is kept and only re-verified (and the companion hashes
  refreshed).

Downloads the release's cumulative LaTeX archive and its two reader PDFs into WORK/cache/<tag>/, checks each file's
SHA-256 against the digest GitHub publishes, extracts the archive into WORK/cache/<tag>/x/, and writes
site-build/gelfand.lock.json: tag, commit, date, assets with SHA-256, and the SHA-256 of every companion file.
Accepted when every digest matches and every chapter folder has its seven data files.
"""
import argparse
import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import (CACHE, COMPANION, DATA_FILES, LOCK, REPO_SLUG, YEARS_DIR, log, now_utc, rjson, sha256_file,
                    wjson)

LATEX_ZIP = "gelfand-chapters01-34-cumulative-and-standalone-latex.zip"
PDFS = {"ru": "gelfand-russian-chapters01-34-complete-first1527.pdf",
        "en": "gelfand-english-chapters01-34-complete-first1527.pdf"}
NEED = ["source-provenance.json", "gelfand-russian-chapters01-34-complete-first1527.tex",
        "gelfand-english-chapters01-34-complete-first1527.tex"]


def gh_json(path):
    r = subprocess.run(["gh", "api", path], capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        sys.exit(f"gh api {path}: {r.stderr.strip()}")
    return json.loads(r.stdout)


def newest_release():
    rels = gh_json(f"repos/{REPO_SLUG}/releases?per_page=40")
    rels = [r for r in rels if r["tag_name"].startswith("readers-a4-")]
    return max(rels, key=lambda r: r["created_at"])["tag_name"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--release")
    ap.add_argument("--keep", action="store_true")
    a = ap.parse_args()
    old = rjson(LOCK, {})
    tag = a.release or (old.get("release", {}).get("tag") if a.keep else None) or newest_release()
    rel = gh_json(f"repos/{REPO_SLUG}/releases/tags/{tag}")
    ref = gh_json(f"repos/{REPO_SLUG}/git/ref/tags/{tag}")
    commit = ref["object"]["sha"]
    if ref["object"]["type"] == "tag":
        commit = gh_json(f"repos/{REPO_SLUG}/git/tags/{commit}")["object"]["sha"]
    dest = CACHE / tag
    dest.mkdir(parents=True, exist_ok=True)
    assets = {}
    want = [LATEX_ZIP] + list(PDFS.values())
    for asset in rel["assets"]:
        if asset["name"] not in want:
            continue
        f = dest / asset["name"]
        digest = (asset.get("digest") or "").removeprefix("sha256:")
        if not f.exists() or sha256_file(f) != digest:
            log("downloading", asset["name"])
            subprocess.run(["gh", "release", "download", tag, "-R", REPO_SLUG, "-p", asset["name"], "-D", str(dest),
                            "--clobber"], check=True)
        h = sha256_file(f)
        assets[asset["name"]] = {"bytes": f.stat().st_size, "sha256": h, "github_digest": digest,
                                 "digest_ok": h == digest, "url": asset["browser_download_url"]}
    missing = [n for n in want if n not in assets]
    bad = [n for n, v in assets.items() if not v["digest_ok"]]
    x = dest / "x"
    stamp = x / ".extracted"
    if not stamp.exists() or stamp.read_text() != assets[LATEX_ZIP]["sha256"]:
        if x.exists():
            shutil.rmtree(x)
        with zipfile.ZipFile(dest / LATEX_ZIP) as z:
            z.extractall(x)
        stamp.write_text(assets[LATEX_ZIP]["sha256"])
    absent = [n for n in NEED if not (x / n).exists()]
    comp = {}
    for f in sorted(COMPANION.rglob("*")):
        if f.is_file():
            comp[f.relative_to(COMPANION).as_posix()] = sha256_file(f)
    years = sorted(d.name for d in YEARS_DIR.glob("GY*") if d.is_dir())
    incomplete = [y for y in years if not all((YEARS_DIR / y / f"{y}_{k}").exists() for k in DATA_FILES)]
    lock = {"_about": "The inputs of the site build: the transcription release (tag, commit, assets with SHA-256 equal to "
                      "GitHub's digests) and the SHA-256 of every companion file. Written by site-build/build/g1_lock.py.",
            "locked_utc": now_utc(),
            "release": {"repository": REPO_SLUG, "tag": tag, "commit": commit, "name": rel.get("name"),
                        "created_at": rel["created_at"], "published_at": rel.get("published_at"),
                        "assets": assets, "files_used": NEED},
            "companion": {"years": years, "files": comp}}
    wjson(LOCK, lock)
    ok = not missing and not bad and not absent and not incomplete and len(years) > 0
    print(f"G1 lock: release {tag} (commit {commit[:10]}), {len(assets)} assets, digests "
          f"{'all equal' if not bad else 'DIFFER: ' + ', '.join(bad)}; missing assets {missing or 'none'}; "
          f"archive files missing {absent or 'none'}; {len(years)} chapters, {len(comp)} companion files, "
          f"incomplete chapters {incomplete or 'none'}")
    print("G1", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
