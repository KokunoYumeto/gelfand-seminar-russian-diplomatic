#!/usr/bin/env python3
"""Create and validate the single requested ZIP after all checks are complete."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "deliverable"
required = {"GY1969_talks.json", "GY1969_items.json", "GY1969_problems.json",
            "GY1969_overview.tex", "GY1969_development.tex", "GY1969_corrections.csv",
            "GY1969_references.bib", "GY1969_report.md", "GY1969_chapter.tex", "GY1969_test.pdf"}
assert all((D / name).is_file() for name in required)
assert (D / "output/visual_qa.md").is_file()
build = json.loads((D / "output/build_summary.json").read_text())
for field in ["latex_errors", "undefined_citations_or_references", "missing_characters",
              "overfull_boxes", "bibtex_warnings", "dataset_errors", "dataset_warnings"]:
    assert not build[field], (field, build[field])

def included(path):
    rel = path.relative_to(D)
    if not path.is_file() or "__pycache__" in rel.parts or "texformats" in rel.parts:
        return False
    if path.suffix in {".fmt", ".aux", ".out", ".toc", ".xdv", ".blg", ".log"} and len(rel.parts) == 1:
        return False
    if path.suffix == ".fmt" or "checkpoint" in path.name:
        return False
    return path.name != "SHA256SUMS.json"

files = sorted(p for p in D.rglob("*") if included(p))
manifest = [{"path": str(p.relative_to(D)), "bytes": p.stat().st_size,
             "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]
(D / "SHA256SUMS.json").write_text(json.dumps(manifest, indent=2) + "\n")
files.append(D / "SHA256SUMS.json")
target = ROOT / "GY1969.zip"
with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for path in files:
        archive.write(path, str(path.relative_to(D)))
with zipfile.ZipFile(target) as archive:
    assert archive.testzip() is None
    assert required <= set(archive.namelist())
    for entry in manifest:
        assert hashlib.sha256(archive.read(entry["path"])).hexdigest() == entry["sha256"]
result = {"archive": target.name, "bytes": target.stat().st_size,
          "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
          "entries": len(files), "required_files_present": True,
          "crc_check_passed": True, "all_entry_hashes_verified": True}
(ROOT / "work/zip_validation.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
