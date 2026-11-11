#!/usr/bin/env python3
"""Regenerate the chapter sources from the preserved edited snapshots.

No source retrieval, prose drafting, or TeX compilation is performed here.
The output directory is code/generation/GY1974; published files are untouched.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "GY1974"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--allow-edited-inputs", action="store_true",
                    help="Permit deliberate changes to the preserved snapshot files")
args = parser.parse_args()
manifest = json.loads((ROOT / "snapshot_manifest.json").read_text(encoding="utf-8"))
if not args.allow_edited_inputs:
    mismatches = []
    for entry in manifest["files"]:
        path = ROOT / entry["destination"]
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != entry["packaged_sha256"]:
            mismatches.append(entry["destination"])
    if mismatches:
        raise SystemExit("Snapshot changed or incomplete: " + ", ".join(mismatches)
                         + ". Use --allow-edited-inputs only for intentional changes.")
if manifest["pending_final_inserts"]:
    print("Snapshot warning: final report inserts were pending: "
          + ", ".join(manifest["pending_final_inserts"]), flush=True)

def run(*arguments):
    print("RUN " + " ".join(str(x) for x in arguments), flush=True)
    subprocess.run([str(x) for x in arguments], cwd=ROOT, check=True)

run(sys.executable, ROOT / "assemble_chapter.py")
run(sys.executable, ROOT / "render_development.py")
run(sys.executable, ROOT / "render_frontmatter.py")
shutil.copy2(ROOT / "kit" / "gelfand_companion.sty", OUT / "gelfand_companion.sty")
shutil.copy2(ROOT / "kit" / "build_chapter.py", OUT / "build_chapter.py")

# The supplied fonts belong to the complete chapter package, two levels up.
# The style has a system-font fallback if only this code directory was copied.
font_source = ROOT.parents[1] / "fonts"
if font_source.is_dir():
    shutil.copytree(font_source, OUT / "fonts", dirs_exist_ok=True)
(OUT / "code").mkdir(exist_ok=True)
for path in ROOT.parent.iterdir():
    if path.is_file() and path.suffix in {".py", ".json", ".out", ".txt"}:
        shutil.copy2(path, OUT / "code" / path.name)
run(sys.executable, ROOT / "check_bib_keys.py")
run(sys.executable, ROOT / "kit" / "build_chapter.py", "GY1974", OUT)
print("Regenerated chapter sources: " + str(OUT), flush=True)
print("PDF compilation is a separate step documented in code/README.md.", flush=True)
