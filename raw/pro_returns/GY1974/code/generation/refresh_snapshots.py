#!/usr/bin/env python3
"""Refresh this package from an explicitly named editorial work directory.

This is a maintainer operation. It writes only below the present code directory;
the source work directory and its authoritative data are never modified.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import zipfile

HERE = Path(__file__).resolve().parent
CODE = HERE.parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--source-work", required=True, type=Path,
                    help="Editorial work directory containing parts/, kit/, and assembly scripts")
parser.add_argument("--require-final-inserts", action="store_true",
                    help="Fail unless report_references.md and validation_report.md both exist")
args = parser.parse_args()
source = args.source_work.expanduser().resolve()
if source == HERE or HERE in source.parents:
    parser.error("Use the original editorial work directory, not the packaged copy.")
required = ["assemble_chapter.py", "render_development.py", "render_frontmatter.py",
            "check_bib_keys.py", "overview_template.tex", "report_template.md",
            "previous_index.md", "references_cumulative.bib", "layout_edits.json"]
for name in required:
    if not (source / name).is_file():
        parser.error(f"Missing required editorial input: {source / name}")
optional = ["report_references.md", "validation_report.md"]
pending = [name for name in optional if not (source / name).is_file()]
if args.require_final_inserts and pending:
    parser.error("Final inserts are not ready: " + ", ".join(pending))
records = []

def digest(data):
    return hashlib.sha256(data).hexdigest()

def rewrite_paths(relative, data):
    """Change locations only; preserve all editorial and mathematical logic."""
    changes = []
    text = data.decode("utf-8")
    if (relative.startswith("parts/early_code/") and relative.endswith(".py")) or relative == "parts/middle_code/audit_csv_tex.py":
        pairs = [
            ("Path(__file__).resolve().parents[3]", "Path(__file__).resolve().parents[2]"),
            ("ROOT/'work'/'parts'", "ROOT/'parts'"),
            ("ROOT / 'work' / 'parts'", "ROOT / 'parts'"),
            ("root/'work/parts", "root/'parts"),
            ("root/'work/references_cumulative.bib'", "root/'references_cumulative.bib'"),
        ]
    elif relative == "parts/late_code/copy_fonts.py":
        pairs = [
            ("workspace=Path('/workspace/scratch/6e3047ad1856')",
             "workspace=Path(__file__).resolve().parents[2]"),
            ("source=Path('/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf')",
             "source=workspace.parents[1]/'fonts'"),
            ("workspace/'work/GY1974/fonts'", "workspace/'GY1974/fonts'"),
            ("workspace/'work/parts/", "workspace/'parts/"),
        ]
    elif relative == "../environment/env.sh":
        pairs = [
            ("GY_TEX_RUNTIME=/workspace/scratch/6e3047ad1856/work/texruntime",
             'GY_TEX_RUNTIME="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)/.texruntime"'),
        ]
    elif relative == "../environment/build_format.sh":
        pairs = [
            ("source /workspace/scratch/6e3047ad1856/work/texruntime/env.sh",
             'source "$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)/env.sh"'),
            ("/usr/bin/xetex", "xetex"),
        ]
    elif relative == "../environment/README.md":
        pairs = [
            ("/workspace/scratch/6e3047ad1856/work/texruntime/env.sh", "code/environment/env.sh"),
            ("/workspace/scratch/6e3047ad1856/work/texruntime/build_format.sh", "code/environment/build_format.sh"),
            ("/workspace/scratch/6e3047ad1856/work/texruntime/", ".texruntime/"),
            ("/workspace/scratch/6e3047ad1856/work/kit//:", '"$(pwd)/code/generation/kit//:"'),
            ("only in work/kit rather than", "only in code/generation/kit rather than"),
        ]
    else:
        pairs = []
    for old, new in pairs:
        if old in text:
            count = text.count(old)
            text = text.replace(old, new)
            changes.append({"from": old, "to": new, "occurrences": count})
    return text.encode("utf-8"), changes

def copy_one(src, destination, label=None, adapt=False):
    original = src.read_bytes()
    data, changes = rewrite_paths(destination, original) if adapt else (original, [])
    dest = HERE / destination
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    records.append({"source": label or str(src.relative_to(source)),
                    "destination": destination, "bytes": len(data),
                    "source_sha256": digest(original), "packaged_sha256": digest(data),
                    "path_rewrites": changes})

# Copy a text-only, explicitly selected snapshot, not source scans or caches.
allowed_suffixes = {".json", ".bib", ".csv", ".md", ".tex", ".py"}
recorded_text_outputs = {"middle_code/check_dilogarithm.out",
                         "root_code/check_spectral_compatibility.txt"}
selected = []
for path in sorted((source / "parts").rglob("*")):
    if not path.is_file() or "__pycache__" in path.parts or "scan_previews" in path.parts:
        continue
    relative = path.relative_to(source / "parts").as_posix()
    if path.suffix in allowed_suffixes or relative in recorded_text_outputs:
        selected.append((path, "parts/" + relative))
for path, relative in selected:
    copy_one(path, relative, adapt=path.suffix == ".py")

# Remove only obsolete files from the previous packaged snapshot. Never delete
# an untracked user file, original editorial data, or a generated chapter.
old_manifest = HERE / "snapshot_manifest.json"
if old_manifest.is_file():
    old = json.loads(old_manifest.read_text(encoding="utf-8"))
    current_parts = {relative for _, relative in selected}
    for record in old.get("files", []):
        relative = record["destination"]
        if relative.startswith("parts/") and relative not in current_parts:
            path = (HERE / relative).resolve()
            if (HERE / "parts").resolve() in path.parents and path.is_file():
                path.unlink()

for name in required:
    copy_one(source / name, name)
for name in optional:
    if (source / name).is_file():
        copy_one(source / name, name)
    elif (HERE / name).is_file():
        (HERE / name).unlink()
for name in ("CHAPTER_FORMAT.md", "build_chapter.py", "gelfand_companion.sty"):
    copy_one(source / "kit" / name, "kit/" + name)
for name in ("env.sh", "build_format.sh", "README.md"):
    path = source / "texruntime" / name
    if path.is_file():
        copy_one(path, "../environment/" + name, adapt=True)

# Preserve the small, untouched supplied kit separately from the amended one.
original_kit = source.parent / "upload" / "GY1974_kit(1).zip"
if original_kit.is_file():
    with zipfile.ZipFile(original_kit) as archive:
        for name in ("CHAPTER_FORMAT.md", "build_chapter.py", "gelfand_companion.sty"):
            member = "kit/" + name
            data = archive.read(member)
            dest = CODE / "kit_original" / name
            dest.parent.mkdir(exist_ok=True)
            dest.write_bytes(data)
            records.append({"source": "upload/GY1974_kit(1).zip::" + member,
                            "destination": "../kit_original/" + name,
                            "bytes": len(data), "source_sha256": digest(data),
                            "packaged_sha256": digest(data), "path_rewrites": []})

for original, target in (("GY1974_prompt(1).md", "GY1974_prompt.md"),
                         ("GY1974_talks(1).md", "GY1974_talks.md")):
    path = source.parent / "upload" / original
    if path.is_file():
        copy_one(path, "inputs/" + target, "upload/" + original)

math_files = {
    "early_code/exact_checks.py": "exact_checks.py",
    "early_code/exact_checks.json": "exact_checks.json",
    "middle_code/check_dilogarithm.py": "check_dilogarithm.py",
    "middle_code/check_dilogarithm.out": "check_dilogarithm.out",
    "root_code/check_spectral_compatibility.py": "check_spectral_compatibility.py",
    "root_code/check_spectral_compatibility.txt": "check_spectral_compatibility.txt",
}
for relative, target in math_files.items():
    copy_one(source / "parts" / relative, "../" + target)

manifest = {
    "snapshot_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "source_contract": "Edited part snapshots are authoritative; drafting generators are optional historical inputs.",
    "pending_final_inserts": pending,
    "excluded": ["source scans and source/reference PDFs", "page previews and PNGs",
                 "TeX caches, downloaded runtimes, failed compilation output", "Python bytecode"],
    "files": sorted(records, key=lambda row: row["destination"]),
}
(HERE / "snapshot_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Refreshed {len(records)} files under {CODE}.")
print("Pending final inserts: " + (", ".join(pending) if pending else "none"))
