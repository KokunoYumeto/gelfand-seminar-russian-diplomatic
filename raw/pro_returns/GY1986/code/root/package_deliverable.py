"""Create the single requested GY1986.zip and verify its complete inventory."""
from pathlib import Path
import hashlib,json,zipfile

OUT=Path(__file__).resolve().parents[2]
ROOT=OUT.parent
ARCHIVE=ROOT/"GY1986.zip"
CODE=OUT/"code"/"root"

def included(path):
    rel=path.relative_to(OUT)
    if any(p.startswith(".") or p=="__pycache__" for p in rel.parts):return False
    if path.suffix in {".pyc",".pyo"}:return False
    if len(rel.parts)==1 and path.suffix in {".aux",".bbl",".blg",".out",".toc",".log"}:return False
    return path.is_file()

def main():
    required=["GY1986_"+s for s in [
        "talks.json","items.json","problems.json","overview.tex","development.tex",
        "corrections.csv","references.bib","report.md","chapter.tex","test.pdf"
    ]]
    assert all((OUT/name).is_file() for name in required)
    validation=json.loads((CODE/"final_validation.json").read_text())
    assert validation["status"]=="complete"
    assert not any(validation["latex_log_findings"].values())
    assert validation["pdf_pages"]==191
    for filename,digest in validation["required_file_sha256"].items():
        assert hashlib.sha256((OUT/filename).read_bytes()).hexdigest()==digest,filename
    pdfs=[str(p.relative_to(OUT)) for p in OUT.rglob("*.pdf") if included(p)]
    assert pdfs==["GY1986_test.pdf"],pdfs
    (CODE/"package_deliverable.out").write_text(
        "PASS: all requested standard files and the reading PDF are present.\n"
        "PASS: final validation is complete; required-file hashes match.\n"
        "PASS: no TeX errors, missing glyphs, unresolved citations, rerun requests, or overfull boxes.\n"
        "The ZIP contains authored code and complete mathematical outputs, supporting source metadata, and the unmodified input kit.\n"
        "The distribution excludes downloaded source articles, full retrieved article bodies, and environment-specific build caches.\n"
        "Archive member names and CRC integrity are tested immediately after creation.\n"
    )
    files=sorted(p for p in OUT.rglob("*") if included(p) and p.name!="MANIFEST.sha256")
    manifest="".join(
        hashlib.sha256(p.read_bytes()).hexdigest()+"  "+str(p.relative_to(OUT))+"\n"
        for p in files
    )
    (OUT/"MANIFEST.sha256").write_text(manifest)
    files.append(OUT/"MANIFEST.sha256")
    with zipfile.ZipFile(ARCHIVE,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for path in sorted(files):
            z.write(path,str(path.relative_to(OUT)))
    with zipfile.ZipFile(ARCHIVE) as z:
        assert z.testzip() is None
        names=z.namelist()
        assert len(names)==len(set(names))
        assert all(not n.startswith("/") and ".." not in Path(n).parts for n in names)
        assert all(name in names for name in required)
        for line in manifest.splitlines():
            expected,name=line.split("  ",1)
            assert hashlib.sha256(z.read(name)).hexdigest()==expected,name
    result={
        "archive":str(ARCHIVE),"files":len(files),"bytes":ARCHIVE.stat().st_size,
        "sha256":hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
        "zip_crc_check":"passed","member_sha256_check":"passed",
        "required_files":required,
    }
    (ROOT/"root_notes"/"archive_validation.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
