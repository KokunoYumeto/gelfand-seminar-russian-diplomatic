#!/usr/bin/env python3
"""Package the validated companion and verify every ZIP member.

The output archive is outside the input tree. Draft TeX pass outputs, TeX
auxiliary files, caches and any regenerated nested output directory are omitted.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import zipfile

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output",type=Path,default=ROOT.parent/"GY1974.zip")
args=parser.parse_args()
target=args.output.resolve()
if target.is_relative_to(ROOT):raise SystemExit("Archive must be outside the input tree")
validation=json.loads((ROOT/"validation.json").read_text())
reproduction=json.loads((ROOT/"code/reproduction_check.json").read_text())
if validation["errors"]:raise SystemExit("Final validation has errors")
if reproduction["checks"].get("delivered_outputs_equal")!="all 14 compared files identical":
    raise SystemExit("Packaged snapshots do not reproduce delivered outputs")
manifest=json.loads((ROOT/"code/generation/snapshot_manifest.json").read_text())
if manifest["pending_final_inserts"]:raise SystemExit("Snapshot has pending report inserts")
for name,expected in validation["required_artifact_sha256"].items():
    actual=hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
    if actual!=expected:raise SystemExit(f"Validated file changed: {name}")

logs=ROOT/"build_logs";logs.mkdir(exist_ok=True)
for src,dst in (("builder.out","builder.out"),("bibtex.out","bibtex.out"),
                ("xelatex_layout2.out","xelatex_final.out"),("validation.out","validation.out")):
    if (ROOT/src).exists():
        shutil.copy2(ROOT/src,logs/dst)
    elif not (logs/dst).exists():
        raise SystemExit(f"Missing recorded build output: {dst}")
(logs/"build_commands.txt").write_text(
    "Final build record\n"
    "python3 build_chapter.py GY1974\n"
    "xelatex -interaction=nonstopmode -halt-on-error -file-line-error GY1974_test.tex\n"
    "bibtex GY1974_test\n"
    "xelatex -interaction=nonstopmode -halt-on-error -file-line-error GY1974_test.tex\n"
    "xelatex -interaction=nonstopmode -halt-on-error -file-line-error GY1974_test.tex\n"
    "Two further XeLaTeX passes followed explicit data-layout repairs.\n"
    "The final pass is xelatex_final.out; the full engine and bibliography logs\n"
    "are GY1974_test.log and GY1974_test.blg at archive root.\n"
    "python3 code/validate_delivery.py\n"
    "python3 code/generation/check_reproduction.py --compare-delivered\n")

files=[]
for path in sorted(ROOT.rglob("*")):
    if not path.is_file():continue
    rel=path.relative_to(ROOT)
    if "__pycache__" in rel.parts or path.suffix in {".pyc",".pyo"}:continue
    if rel.parts[:3]==("code","generation","GY1974"):continue
    if path.parent==ROOT and (path.suffix in {".aux",".out"} or path.name=="archive_manifest.json"):
        continue
    if path.suffix==".pdf" and rel.as_posix()!="GY1974_test.pdf":
        raise SystemExit(f"Unexpected PDF in package: {rel}")
    if path.suffix in {".png",".jpg",".jpeg"}:
        raise SystemExit(f"Unexpected image in package: {rel}")
    files.append((path,rel.as_posix()))

rows=[{"path":rel,"bytes":path.stat().st_size,
       "sha256":hashlib.sha256(path.read_bytes()).hexdigest()} for path,rel in files]
manifest_path=ROOT/"archive_manifest.json"
manifest_path.write_text(json.dumps({
    "created_at_utc":datetime.now(timezone.utc).isoformat(),
    "manifest_scope":"Every archive member except this manifest itself.",
    "files":rows
},ensure_ascii=False,indent=2)+"\n")
files.append((manifest_path,manifest_path.name))
with zipfile.ZipFile(target,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for path,rel in files:z.write(path,rel)
with zipfile.ZipFile(target) as z:
    bad=z.testzip()
    if bad:raise SystemExit(f"ZIP CRC error: {bad}")
    if len(z.namelist())!=len(set(z.namelist())):raise SystemExit("Duplicate ZIP member")
    for row in rows:
        if hashlib.sha256(z.read(row["path"])).hexdigest()!=row["sha256"]:
            raise SystemExit("Archive payload differs: "+row["path"])
    required=set(validation["required_artifact_sha256"])
    if not required<=set(z.namelist()):raise SystemExit("Missing required archive member")
print(json.dumps({
    "archive":str(target),"bytes":target.stat().st_size,
    "members":len(files),"required_files_present":True,
    "all_payload_hashes_match":True,"zip_crc_check":"passed",
    "sha256":hashlib.sha256(target.read_bytes()).hexdigest()
},indent=2))
