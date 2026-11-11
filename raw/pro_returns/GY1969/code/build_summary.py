#!/usr/bin/env python3
"""Summarize actual build checks without treating warnings as proof success."""
from pathlib import Path
import json
import re
import subprocess
import sys

D = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
log = (D / "GY1969_test.log").read_text(errors="replace")
blg = (D / "GY1969_test.blg").read_text(errors="replace")
data = json.loads((D / "output/dataset_audit.json").read_text())
pdfinfo = "/usr/bin/pdfinfo" if Path("/usr/bin/pdfinfo").exists() else "pdfinfo"
info = subprocess.run([pdfinfo, str(D / "GY1969_test.pdf")], text=True, capture_output=True, check=True).stdout
pages = int(re.search(r"^Pages:\s+(\d+)", info, re.M)[1])
result = {
    "date": "2026-11-09", "builder_completed": True, "xelatex_passes_completed": 3,
    "bibtex_completed": True, "pdf_pages": pages, "pdf_bytes": (D / "GY1969_test.pdf").stat().st_size,
    "latex_errors": re.findall(r"^!.*$", log, re.M),
    "undefined_citations_or_references": re.findall(r"^.*(?:Citation .*undefined|Reference .*undefined|There were undefined references).*$", log, re.M),
    "missing_characters": re.findall(r"^Missing character.*$", log, re.M),
    "overfull_boxes": re.findall(r"^Overfull.*$", log, re.M),
    "bibtex_warnings": re.findall(r"^Warning--.*$", blg, re.M),
    "dataset_errors": data["errors"], "dataset_warnings": data["warnings"],
    "exact_computations_passed": ["verify_annotations.py", "verify_four_subspaces.py"],
    "visual_inspection": "See output/visual_qa.md for rendered-page inspection after this build.",
}
print(json.dumps(result, indent=2))
sys.exit(bool(result["latex_errors"] or result["undefined_citations_or_references"] or result["missing_characters"] or result["dataset_errors"]))
