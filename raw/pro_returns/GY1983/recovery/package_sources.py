import pathlib,json,hashlib,zipfile,sys
p=pathlib.Path("work/GY1983")
files=sorted(f for f in p.rglob("*") if f.is_file() and f.suffix!=".pyc")
manifest={str(f.relative_to(p)):{"bytes":f.stat().st_size,"sha256":hashlib.sha256(f.read_bytes()).hexdigest()} for f in files}
(p/"GY1983_manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
z=pathlib.Path("work/GY1983.zip")
with zipfile.ZipFile(z,"w",zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
 for f in sorted(p.rglob("*")):
  if f.is_file() and f.suffix!=".pyc":archive.write(f,f.relative_to(p).as_posix())
with zipfile.ZipFile(z) as archive:
 bad=archive.testzip()
 names=archive.namelist()
 required=["GY1983_talks.json","GY1983_items.json","GY1983_problems.json","GY1983_corrections.csv","GY1983_references.bib","GY1983_overview.tex","GY1983_development.tex","GY1983_report.md","GY1983_chapter.tex","GY1983_test.tex"]
 missing=[n for n in required if n not in names]
 report={"zip_bytes":z.stat().st_size,"sha256":hashlib.sha256(z.read_bytes()).hexdigest(),"files":len(names),"crc_failure":bad,"missing_text_deliverables":missing,"compiled_pdf_present":"GY1983_test.pdf" in names}
 print(json.dumps(report))
 if bad or missing:sys.exit(1)
