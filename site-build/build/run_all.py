"""Build the whole site and check it, step by step (design §7); stops at the first step that fails.

usage: python -I run_all.py [--returns DIR [--kit DIR] [--reader DIR]] [--release TAG | --keep-lock] [--from STEP]
                            [--tarball]
  --returns    first copy the companion's returned chapters from DIR (sync_companion.py); a chapter returned since the
               last build is registered in data/works.json and enters every page, index and data file
  --release    lock this readers release instead of the newest one; --keep-lock keeps the release in gelfand.lock.json
  --from       start at this step (g1, g2, g7, g5, g6, g3, g4, g8, g9, g10)
  --tarball    after the checks pass, pack the site for the Pages workflow (deploy/make_site_tarball.py)

Steps: G1 lock the transcription release and the companion files; G2 registry of records, pages and academic years;
G7 pages revised since each chapter was written; G5 companion fields to HTML; G6 links; G3 notebook pages (when
present); G4 figures (when present); G8 render; G9 search index (when present); G10 checks.

Environment: GELFAND_WORK (build folder), GELFAND_PACKAGES (the chapters as sent, for G7), GELFAND_MATHJAX (the
MathJax 3.2.2 es5 folder copied into the site), GELFAND_PAGEFIND (the pagefind binary, for G9), GELFAND_EXCLUDE
(works switched off for one build), GELFAND_BASE (base path of the site).
"""
import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
STEPS = [("g1", "g1_lock.py"), ("g2", "g2_registry.py"), ("g7", "g7_stale.py"), ("g5", "g5_companion.py"),
         ("g6", "g6_links.py"), ("g3", "g3_notebook.py"), ("g4", "g4_figures.py"), ("g8", "g8_render.py"),
         ("g9", "g9_search.py"), ("g10", "g10_check.py")]


def run(args):
    print("+", " ".join(str(a) for a in args), flush=True)
    r = subprocess.run([sys.executable, "-I"] + [str(a) for a in args], cwd=HERE)
    if r.returncode:
        sys.exit(f"step failed: {args[0]} (exit status {r.returncode})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--returns")
    ap.add_argument("--kit")
    ap.add_argument("--reader")
    ap.add_argument("--release")
    ap.add_argument("--keep-lock", action="store_true")
    ap.add_argument("--from", dest="start", default="g1")
    ap.add_argument("--tarball", action="store_true")
    a = ap.parse_args()
    names = [s for s, _ in STEPS]
    if a.start not in names:
        sys.exit(f"--from must be one of {', '.join(names)}")
    if a.returns:
        run(["sync_companion.py", "--returns", a.returns] + (["--kit", a.kit] if a.kit else [])
            + (["--reader", a.reader] if a.reader else []))
    for name, script in STEPS[names.index(a.start):]:
        if not (HERE / script).exists():
            print(f"- {name}: {script} not present, skipped", flush=True)
            continue
        extra = []
        if name == "g1":
            extra = ["--keep"] if a.keep_lock else (["--release", a.release] if a.release else [])
        run([script] + extra)
    if a.tarball:
        run([HERE.parent / "deploy" / "make_site_tarball.py"])


if __name__ == "__main__":
    main()
