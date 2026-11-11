#!/usr/bin/env python3
"""Stage the research audit and create a checked, hash-manifested deliverable.

The ordinary packaging command uses only the unpacked deliverable.
The optional --stage-from argument identifies the original task workspace.
"""
from pathlib import Path
from collections import Counter
import argparse
import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
import zipfile

from bib_audit import entries, field

BASE = Path(__file__).resolve().parents[1]
OWNERS = ["agenda", "manin_fuchs", "autumn_representations", "spring_integrable"]
REQUIRED = [
    "GY1973_talks.json", "GY1973_items.json", "GY1973_problems.json",
    "GY1973_overview.tex", "GY1973_development.tex", "GY1973_corrections.csv",
    "GY1973_references.bib", "GY1973_report.md", "GY1973_chapter.tex",
    "GY1973_test.pdf",
]
ROOT_FILES = REQUIRED + [
    "GY1973_test.tex", "GY1973_test.bbl", "GY1973_statistics.json",
    "GY1973_area_map.json", "build_chapter.py", "gelfand_companion.sty",
    "CHAPTER_FORMAT.md", "README.md",
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def copy(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def stage(workspace):
    work = workspace / "work"
    for owner in OWNERS:
        source = work / "fragments" / owner
        target = BASE / "code" / "fragments" / owner
        for name in [
            "talks.json", "items.json", "problems.json", "area_map.json",
            "corrections.csv", "references.bib", "critical_verifications.tex",
            "development.tex", "validation_output.json", "build_output.txt",
            "check_conic_output.txt", "download_output.txt",
        ]:
            if (source / name).exists():
                copy(source / name, target / name)
        for p in source.glob("*.py"):
            copy(p, target / p.name)
        for name in ["audit.md", "search_log.md"]:
            if (source / name).exists():
                copy(source / name, BASE / "audit" / owner / name)
        for p in source.glob("*review.md"):
            copy(p, BASE / "audit" / owner / p.name)
        for folder in ["code", "output"]:
            if (source / folder).is_dir():
                for p in (source / folder).iterdir():
                    if p.is_file() and p.suffix in {".py", ".md", ".txt", ".json"}:
                        copy(p, target / folder / p.name)
    copy(BASE / "GY1973_test.log", BASE / "logs" / "xelatex_final.log")
    copy(BASE / "layout_probe.tex", BASE / "code" / "layout_probe.tex")
    inputs = []
    for p in sorted((workspace / "upload").iterdir()):
        if p.is_file():
            inputs.append({"filename": p.name, "bytes": p.stat().st_size, "sha256": digest(p)})
    write_csv(BASE / "audit" / "source_input_sha256.csv", ["filename", "bytes", "sha256"], inputs)
    kit = []
    for name in ["build_chapter.py", "gelfand_companion.sty", "CHAPTER_FORMAT.md"]:
        before = work / "kit" / name
        after = BASE / name
        same = before.read_bytes() == after.read_bytes()
        assert same, f"Supplied kit file changed: {name}"
        kit.append({"filename": name, "sha256": digest(after), "identical_to_supplied": same})
    (BASE / "audit" / "supplied_kit_check.json").write_text(
        json.dumps(kit, indent=2) + "\n", encoding="utf-8"
    )
    oldkeys = {k for k, _ in entries((work / "references_cumulative.bib").read_text())}
    bibliography = []
    for key, entry in entries((BASE / "GY1973_references.bib").read_text()):
        bibliography.append({
            "key": key, "author": field(entry, "author"), "year": field(entry, "year"),
            "title": field(entry, "title"), "verification_flag": field(entry, "note"),
            "cumulative_key_reused": key in oldkeys, "doi": field(entry, "doi"),
            "url": field(entry, "url"), "verification_scope": field(entry, "annote"),
        })
    write_csv(
        BASE / "audit" / "bibliography_inventory.csv",
        list(bibliography[0]), bibliography,
    )
    items = json.loads((BASE / "GY1973_items.json").read_text())
    page_rows = []
    for page in range(501, 554):
        own = []
        for item in items:
            nums = [int(x) for x in re.findall(r"P(\d{6})", item["pages"])]
            if nums and min(nums) <= page <= max(nums):
                own.append(item)
        page_rows.append({
            "page": f"GELFAND-P{page:06d}", "item_count": len(own),
            "record_ids": ";".join(str(r) for r in sorted({x["record"] for x in own})),
            "item_ids": ";".join(x["id"] for x in own),
        })
    write_csv(BASE / "audit" / "source_page_coverage.csv", list(page_rows[0]), page_rows)
    (BASE / "audit" / "final_independent_review.md").write_text("""# Final independent review

The final read-only review checked the integrated files, separately from assembly.

- Counts: 32 records, 301 items, 17 problem entries, 91 bibliography entries, 93 corrections.
- Coverage: all records 302–333, unique identifiers, resolving bibliography and problem links.
- PDF: 148 pages; no errors, overfull boxes, undefined-reference warnings or missing characters in the final engine log.
- The corrected Bernoulli moments, unit Euler factor, residue-ball/clopen distinction, tag counterexample, Q-construction homotopies and conic certificates remain in the final appendix.
- The real-form qualification in the KP reduction and the flow convention for the positive half-wave propagator remain in the final items.
- A stale pending-build line in the report was identified and replaced by the verified report generator before packaging.
- The data bibliography contains 91 entries; the printed bibliography contains 90 because the general archive record is uncited in the typeset chapter.

The final log includes nine underfull-box notices. They are typographic diagnostics, not missing content or unresolved mathematics. Page samples from the overview, occurrence entries, appendix, corrections and bibliography were inspected visually.
""", encoding="utf-8")
    (BASE / "README.md").write_text("""# GY1973: critical companion to the Gelfand seminar, 1973–74

## Start here

Open GY1973_test.pdf for the complete 148-page chapter. GY1973_report.md explains the editorial decisions, counts, searches, remaining uncertainties, and website recommendations.

The edition contains 32 source records, 301 mathematical occurrences, 17 indexed problems, and 93 corrections or recorded ambiguities. It covers all 53 supplied scan pages. The 30 supplied catalogue entries are retained; two additional records on the scans, 331 and 332, are included under their written date of 25 March 1974, with the catalogue's 1975 discrepancy documented.

The historical counts are A = 25, B = 7, C = 4, D = 0, E = 229, F = 36. The research cutoff is 9 November 2026. No bounded new research contribution to a C or D question was warranted. GY1973_development.tex contains a labelled critical verification appendix, including complete proofs and independently checked computations required to assess the notes.

## Files

| Location | Contents |
| --- | --- |
| GY1973_talks.json, GY1973_items.json, GY1973_problems.json | Authoritative structured edition and problem links |
| GY1973_overview.tex, GY1973_development.tex | Overview and critical verification appendix |
| GY1973_corrections.csv | Source readings, proposed corrections, and evidence |
| GY1973_references.bib | 91 bibliography entries, with verification scope and links |
| GY1973_chapter.tex, GY1973_test.tex, GY1973_test.bbl | Generated chapter, standalone wrapper, and resolved bibliography |
| GY1973_test.pdf | Compiled chapter |
| GY1973_report.md | Editorial report, count tables, coverage and limitations |
| GY1973_statistics.json, GY1973_area_map.json | Reproducible report counts and area labels |
| code | Assembly, validation, mathematical verification, and packaging programs |
| code/fragments | Audited source blocks, historical generators, and computational outputs |
| audit | Search logs, source reviews, input hashes, bibliography inventory, and coverage table |
| logs | Assembly, mathematical verification, data validation, and TeX/BibTeX outputs |
| fonts | Four DejaVu Serif faces and their license |
| MANIFEST.sha256.json | Byte sizes and SHA-256 hashes of every other delivered file |

Of the 91 bibliography entries, 88 are marked verified and three unverified. The latter are explicitly identified in the report and item assessments. A verified link is not a claim that every proof in that source was read. The printed bibliography has 90 entries because the general archive record is not invoked by a typesetting citation.

The supplied builder, style and format specification are byte-identical to the kit. Original source attachments and downloaded publisher papers are not duplicated into this archive. The input hash audit identifies the attachments used; the bibliography and research logs identify the checked publications.

## Build and validate

Use Python 3 and a XeLaTeX installation including the packages required by the supplied style, together with BibTeX. From this directory, run the prescribed sequence:

    python build_chapter.py GY1973
    xelatex GY1973_test
    bibtex GY1973_test
    xelatex GY1973_test
    xelatex GY1973_test

The helper runs the same builder and engines, uses the bundled font faces, and builds in a fresh temporary directory. Compilation errors stop the build; the packaging audit additionally checks the final logs for unresolved diagnostics:

    python code/build_pdf.py
    python code/validate_data.py

On the original runtime, a generated TeX format and filename database were absent despite the packages being installed. The helper contains a documented fallback for that environment. It does not change the supplied builder or style. An additional XeLaTeX pass is used when required to settle labels.

To repeat the independent mathematical checks:

    python code/independent_checks.py
    python code/fragments/autumn_representations/check_conic.py
    python code/fragments/spring_integrable/code/verify_emendations.py

The first two use the Python standard library. The third requires SymPy 1.14.0; its requirement file and original output are in the spring fragment. Symbolic identities and finite exact checks have the scope stated in their accompanying proofs. Numerical checks are not offered as proofs of unbounded assertions.

To reassemble from the delivered audited fragments:

    python code/final_polish.py
    python code/assemble.py
    python code/write_editorial.py
    python code/build_pdf.py
    python code/write_editorial.py --verified

The root JSON, CSV and bibliography files are the authoritative final edition. Older per-fragment generator programs are preserved as research history; some assume the original task directory and source attachments and can regenerate earlier intermediate text. They are not needed for a normal rebuild. To check older problem identifiers against the previous index, pass its path explicitly:

    python code/validate_data.py --previous /path/to/previous_index.md

To regenerate the package and verify all manifest hashes:

    python code/package_deliverable.py --zip /path/to/GY1973.zip

The manifest excludes itself. The packaging program checks the ZIP's CRCs and every payload's SHA-256 digest after writing it.
""", encoding="utf-8")


def package(destination):
    for name in ROOT_FILES:
        path = BASE / name
        assert path.is_file() and path.stat().st_size, f"Missing or empty: {name}"
    data = {n: json.loads((BASE / f"GY1973_{n}.json").read_text()) for n in ["talks", "items", "problems"]}
    with (BASE / "GY1973_corrections.csv").open(newline="", encoding="utf-8") as f:
        corrections = list(csv.DictReader(f))
    refs = entries((BASE / "GY1973_references.bib").read_text())
    counts = {
        "records": len(data["talks"]), "items": len(data["items"]),
        "problems": len(data["problems"]), "references": len(refs),
        "corrections": len(corrections),
    }
    assert counts == {"records": 32, "items": 301, "problems": 17, "references": 91, "corrections": 93}
    expected_classes = {"A": 25, "B": 7, "C": 4, "E": 229, "F": 36}
    assert dict(Counter(x["class"] for x in data["items"])) == expected_classes
    report = (BASE / "GY1973_report.md").read_text()
    assert "**Final build:**" in report and "pending the final integrated run" not in report
    pdfinfo = shutil.which("pdfinfo")
    if Path("/usr/bin/pdfinfo").exists():
        pdfinfo = "/usr/bin/pdfinfo"
    assert pdfinfo, "pdfinfo is required for the archive audit"
    pdfmeta = subprocess.run([pdfinfo, str(BASE / "GY1973_test.pdf")], check=True, capture_output=True, text=True).stdout
    pages = int(re.search(r"(?m)^Pages:\s*(\d+)", pdfmeta).group(1))
    assert pages == 148
    final_log = (BASE / "logs" / "xelatex_pass4.txt").read_text()
    bib_log = (BASE / "logs" / "bibtex.txt").read_text()
    forbidden = r"(?im)(^!|LaTeX Warning:|Package \w+ Warning:|Missing character:|Overfull \\[hv]box|undefined references|undefined citations)"
    assert not re.search(forbidden, final_log), "Final XeLaTeX diagnostics need review"
    assert not re.search(r"(?i)warning|error message", bib_log), "BibTeX diagnostics need review"
    validation = subprocess.run(
        [sys.executable, str(BASE / "code" / "validate_data.py")],
        check=True, capture_output=True, text=True,
    ).stdout
    (BASE / "logs" / "archive_semantic_validation.txt").write_text(validation)
    audit = {
        "counts": counts, "classes": {k: expected_classes.get(k, 0) for k in "ABCDEF"},
        "bibliography_flags": dict(Counter(field(e, "note") for _, e in refs)),
        "pdf_pages": pages, "final_tex_errors_or_warnings": 0,
        "final_bibtex_warnings": 0, "required_files_present": True,
        "semantic_validation": "passed", "manifest_excludes_itself": True,
        "archive_verification": "CRC and payload SHA-256 checks enforced after archive creation",
    }
    (BASE / "logs" / "final_archive_audit.json").write_text(json.dumps(audit, indent=2) + "\n")
    paths = [BASE / n for n in ROOT_FILES]
    for folder in ["code", "audit", "logs", "fonts"]:
        paths.extend(
            p for p in (BASE / folder).rglob("*")
            if p.is_file() and not any(part.startswith(".") or part == "__pycache__"
                                       for part in p.relative_to(BASE).parts)
        )
    paths = sorted(set(paths), key=lambda p: p.relative_to(BASE).as_posix())
    manifest = {
        "format": "sha256", "file_count": len(paths),
        "files": [
            {"path": p.relative_to(BASE).as_posix(), "bytes": p.stat().st_size, "sha256": digest(p)}
            for p in paths
        ],
    }
    manifest_path = BASE / "MANIFEST.sha256.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    paths.append(manifest_path)
    destination = destination.resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    assert destination not in paths
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in paths:
            z.write(p, p.relative_to(BASE).as_posix())
    with zipfile.ZipFile(destination) as z:
        assert z.testzip() is None
        for row in manifest["files"]:
            payload = z.read(row["path"])
            assert len(payload) == row["bytes"]
            assert hashlib.sha256(payload).hexdigest() == row["sha256"]
        assert len(z.namelist()) == len(paths)
        assert not any("/primary/" in n or "/__pycache__/" in n or ".tex_runtime" in n for n in z.namelist())
    print(json.dumps({
        **audit, "archive": str(destination), "archive_files": len(paths),
        "archive_bytes": destination.stat().st_size, "sha256": digest(destination),
        "crc_and_manifest_validation": "passed",
    }, indent=2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage-from", type=Path)
    parser.add_argument("--stage-only", action="store_true")
    parser.add_argument("--zip", type=Path, default=BASE.parent / "GY1973.zip")
    args = parser.parse_args()
    if args.stage_from:
        stage(args.stage_from.resolve())
    if args.stage_only:
        assert args.stage_from, "--stage-only requires --stage-from"
        print("Staged audit, code, provenance, and README.")
    else:
        package(args.zip)


if __name__ == "__main__":
    main()
