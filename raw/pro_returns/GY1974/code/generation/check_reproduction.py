#!/usr/bin/env python3
"""Test portable regeneration in a disposable copy; do not compile a PDF."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
CODE = HERE.parent
CHAPTER = CODE.parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--compare-delivered", action="store_true",
                    help="Require regenerated text/data to equal the top-level delivered outputs")
args = parser.parse_args()

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run(arguments, cwd):
    result = subprocess.run([str(x) for x in arguments], cwd=cwd,
                            capture_output=True, text=True)
    if result.returncode:
        print(result.stdout, end="")
        print(result.stderr, end="", file=sys.stderr)
        raise SystemExit(result.returncode)
    return result.stdout

checks = {}
with tempfile.TemporaryDirectory(prefix="gy1974-reproduction-", dir=CHAPTER) as temporary:
    chapter = Path(temporary) / "GY1974"
    code = chapter / "code"
    shutil.copytree(CODE, code,
                    ignore=shutil.ignore_patterns("__pycache__", "GY1974", ".texruntime"))
    if (CHAPTER / "fonts").is_dir():
        shutil.copytree(CHAPTER / "fonts", chapter / "fonts")
    run([sys.executable, code / "generation/regenerate.py"], chapter)
    checks["isolated_regeneration"] = "passed"
    regenerated = code / "generation/GY1974"
    counts = json.loads((regenerated / "audit_counts.json").read_text())
    assert not counts["schema_errors"]
    checks["schema_errors"] = counts["schema_errors"]
    expected_exact = json.loads((code / "exact_checks.json").read_text())
    run([sys.executable, code / "exact_checks.py"], chapter)
    assert json.loads((code / "exact_checks.json").read_text()) == expected_exact
    checks["exact_checks_recorded_json"] = "identical"
    for script, output in (("check_dilogarithm.py", "check_dilogarithm.out"),
                           ("check_spectral_compatibility.py", "check_spectral_compatibility.txt")):
        actual = run([sys.executable, code / script], chapter)
        assert actual == (code / output).read_text(), output
        checks[output] = "identical"
    for name in ("CHAPTER_FORMAT.md", "build_chapter.py", "gelfand_companion.sty"):
        assert (code / "generation/kit" / name).read_bytes() == (code / "kit_original" / name).read_bytes()
        checks["supplied_kit_unchanged:" + name] = True
    audit_script = code / "generation/parts/middle_code/audit_csv_tex.py"
    if audit_script.is_file():
        run([sys.executable, audit_script], chapter)
        checks["early_extra_csv_and_canonical_generator_audit"] = "passed"
    if shutil.which("bash"):
        run(["bash", "-n", code / "environment/env.sh", code / "environment/build_format.sh"], chapter)
        checks["environment_shell_syntax"] = "passed"
    else:
        checks["environment_shell_syntax"] = "not checked: Bash is unavailable"
    outputs = ["GY1974_" + suffix for suffix in (
        "talks.json", "items.json", "problems.json", "references.bib", "corrections.csv",
        "overview.tex", "development.tex", "report.md", "chapter.tex", "test.tex")]
    outputs += ["audit_counts.json", "bibliography_verification.json", "gelfand_companion.sty", "build_chapter.py"]
    output_hashes = {name: sha(regenerated / name) for name in outputs}
    if args.compare_delivered:
        mismatches = [name for name in outputs
                      if not (CHAPTER / name).is_file() or sha(CHAPTER / name) != output_hashes[name]]
        if mismatches:
            raise SystemExit("Delivered outputs differ from the current snapshot: " + ", ".join(mismatches))
        checks["delivered_outputs_equal"] = "all 14 compared files identical"
    else:
        checks["delivered_outputs_equal"] = "not requested"

report = {
    "checked_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "python_version": sys.version.split()[0],
    "snapshot_manifest_sha256": sha(HERE / "snapshot_manifest.json"),
    "pending_final_inserts": json.loads((HERE / "snapshot_manifest.json").read_text())["pending_final_inserts"],
    "pdf_compilation": "not performed by this check; see the separate final validation record",
    "counts": {key: counts[key] for key in ("records", "items", "problems", "references", "corrections", "classes")},
    "checks": checks,
    "regenerated_output_sha256": output_hashes,
}
(CODE / "reproduction_check.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
