#!/usr/bin/env python3
"""Collect reproducibility files and source-check provenance for the archive."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "deliverable"
W = ROOT / "work"

for directory in [D / "code/authoring", D / "code/kit_original", D / "research/segments", D / "output/visuals"]:
    directory.mkdir(parents=True, exist_ok=True)
for name in ["assemble.py", "write_report.py", "prepare_package.py", "make_zip.py"]:
    shutil.copy2(W / name, D / "code/authoring" / name)
shutil.copy2(W / "render_qa.py", D / "code/render_qa.py")
for path in (W / "kit").iterdir():
    if path.is_file():
        shutil.copy2(path, D / "code/kit_original" / path.name)
for segment in ["early", "middle", "late"]:
    source = W / "parts" / segment
    target = D / "research/segments" / segment
    code_target = D / "code/authoring" / segment
    target.mkdir(parents=True, exist_ok=True)
    code_target.mkdir(parents=True, exist_ok=True)
    for path in source.iterdir():
        if not path.is_file():
            continue
        if path.suffix == ".py":
            shutil.copy2(path, code_target / path.name)
        elif path.suffix in {".json", ".csv", ".bib", ".md", ".log"}:
            shutil.copy2(path, target / path.name)
for name in ["proof_audit.md", "research_notes.md"]:
    shutil.copy2(W / "parts/root" / name, D / "research" / name)
shutil.copy2(W / "parts/root/output/verify_annotations_rerun.json", D / "output/verify_annotations_rerun.json")
shutil.copy2(D / "GY1969_test.log", D / "output/final_latex.log")
shutil.copy2(D / "GY1969_test.blg", D / "output/final_bibtex.log")
shutil.copy2(W / "assembly_final.log", D / "output/assembly.log")
shutil.copy2(W / "report_generation.log", D / "output/report_generation.log")
for path in (W / "pdf_qa").glob("contact_*.png"):
    shutil.copy2(path, D / "output/visuals" / path.name)
if (W / "pdf_qa/render_manifest.json").exists():
    shutil.copy2(W / "pdf_qa/render_manifest.json", D / "output/render_manifest.json")
inputs = []
for path in sorted((ROOT / "upload").iterdir()):
    if path.is_file():
        inputs.append({"file": path.name, "bytes": path.stat().st_size,
                       "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
(D / "research/input_sha256.json").write_text(json.dumps(inputs, indent=2) + "\n")
summary = json.loads((D / "output/build_summary.json").read_text())
counts = json.loads((D / "research/counts.json").read_text())
readme = f"""# GY1969 — Critical companion to the Gelfand seminar

Open **GY1969_test.pdf** for the complete {summary['pdf_pages']}-page chapter.
The editorial report, **GY1969_report.md**, explains the findings, source
limitations, counts, development decisions, and website recommendations.

## Coverage

- 55 catalogue records:174–228, academic years1969–70 and1970–71.
- {counts['items']} mathematical occurrences and {counts['problems']} problem entries.
- {counts['corrections']} correction records and91 bibliography entries.
- Historical classes:A19, B8, C4, D0, E231, F28.

The indexed content lies on P000283–P000359. The supplied adjacent leaves
P000282 and P000360 are documented as previous/next-year boundary evidence.
The opening carryover is not counted again, and no new229 record is invented
inside this chapter. Dates, source order and ambiguous attribution are explicit.

## Authoritative files

The seven `GY1969_` data files are `talks.json`, `items.json`, `problems.json`,
`overview.tex`, `development.tex`, `corrections.csv`, and `references.bib`.
The generated `GY1969_chapter.tex` and `GY1969_test.tex` build the PDF with the
provided companion style. Edit the data and regenerate; do not edit the
generated chapter by hand.

## Rebuild

From this directory, run:

```bash
bash code/build.sh
```

This runs the supplied builder, the additional data audit, XeLaTeX, BibTeX,
two resolving XeLaTeX passes, and the exact mathematical checks. It includes
a local-format fallback for an uninitialized TeX Live installation. The four
bundled DejaVu Serif fonts and their licence provide reproducible text shapes.
The final build had zero errors, undefined references/citations, missing
characters, overfull boxes, or BibTeX warnings. See `output/build_summary.json`.

The computations can be run separately with standard-library Python:

```bash
python code/verify_annotations.py
python code/verify_four_subspaces.py
```

Code and exact JSON outputs are included. The full proofs, their scope and
independent checks are in the chapter's Developments section and in
`research/proof_audit.md`. No mathematical novelty is claimed.

## Evidence and audit files

`research/source_checks.json` records opened sources and verification scope.
`research/item_areas.csv` makes the report's speaker/area counts reproducible.
The segment snapshots and their validators, logs and peer reviews are retained
in `research/segments/`; drafting scripts are in `code/authoring/`. Those
drafting scripts preserve the original task-workspace paths and may depend on
the supplied source attachments. The final seven-file build and mathematical
checks do not require those drafting paths. Input file hashes are recorded
without duplicating the large scan archive.

The fixed-format chapter is the reviewed final synthesis; raw segment snapshots
precede a few explicitly logged typesetting and precision normalizations.
`code/kit_original/` preserves the supplied kit unchanged. Rendered contact
sheets and the visual inspection record are in `output/`.

The bibliography deliberately distinguishes an opened link (`verified`) from
result-level verification. One2026 lead is explicitly unverified. Its
inaccessibility is not used to claim that the arbitrary coherent-sequence
problem remains globally open. The report and item assessments state all
material limitations.
"""
readme = readme.replace("records:174", "records: 174").replace("years1969", "years 1969").replace("and1970", "and 1970").replace("and91", "and 91").replace("classes:A19, B8, C4, D0, E231, F28", "classes: A 19, B 8, C 4, D 0, E 231, F 28").replace("new229", "new 229").replace("One2026", "One 2026")
(D / "README.md").write_text(readme)
print(json.dumps({"pdf_pages": summary["pdf_pages"], "input_files_hashed": len(inputs),
                  "references": 91, "artifact_directory": str(D)}, indent=2))
