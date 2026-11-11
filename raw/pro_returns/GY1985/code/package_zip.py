"""Create GY1985.zip with an internal SHA-256 manifest and verify its CRCs.

Run: python code/package_zip.py [chapter_directory] [output_zip]
"""
import hashlib,json,sys,zipfile
from pathlib import Path
D=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parent.parent
Z=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else D.parent/'GY1985.zip'
required=[f'GY1985_{x}' for x in ['talks.json','items.json','problems.json','overview.tex','development.tex','corrections.csv','references.bib','report.md','chapter.tex','test.pdf']]
for name in required:assert (D/name).is_file(),name
for name in ['audit/build_output.json','audit/validation_output.json','audit/checks/checks_output.json','audit/pdf_qa/pdf_qa_output.json']:
    assert json.loads((D/name).read_text())['status']=='PASS',name
def include(p):
    rel=p.relative_to(D)
    if not p.is_file() or '__pycache__' in rel.parts or 'texruntime' in rel.parts:return False
    if p.suffix in {'.pyc','.aux','.out','.fmt'}:return False
    if len(rel.parts)==1 and (p.suffix in {'.log','.blg','.bbl'} or p.name.endswith('.stdout.txt')):return False
    return p.resolve()!=Z
def files():return sorted(p for p in D.rglob('*') if include(p))
def write_archive():
    selected=[p for p in files() if p.name!='MANIFEST.sha256']
    manifest=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(D).as_posix()+'\n' for p in selected)
    (D/'MANIFEST.sha256').write_text(manifest)
    with zipfile.ZipFile(Z,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in files():z.write(p,p.relative_to(D).as_posix())
    with zipfile.ZipFile(Z) as z:
        assert z.testzip() is None
        names=z.namelist();assert len(names)==len(set(names))
        for name in required:assert name in names
        for line in z.read('MANIFEST.sha256').decode().splitlines():
            sha,name=line.split('  ',1);assert hashlib.sha256(z.read(name)).hexdigest()==sha,name
    return names
report={'status':'PASS','required_deliverables':required,'excluded':['binary TeX runtime formats','Python caches','root auxiliary files','obsolete root compiler stdout files'],'zip_crc_test':'pending','internal_sha256_manifest':'pending'}
path=D/'audit/package_output.json';path.write_text(json.dumps(report,indent=2)+'\n')
write_archive()
report.update(zip_crc_test='PASS',internal_sha256_manifest='PASS')
path.write_text(json.dumps(report,indent=2)+'\n')
names=write_archive()
print(json.dumps({'status':'PASS','archive':str(Z),'members':len(names),'bytes':Z.stat().st_size,'sha256':hashlib.sha256(Z.read_bytes()).hexdigest(),'zip_crc_test':'PASS','internal_sha256_manifest':'PASS'},indent=2))
