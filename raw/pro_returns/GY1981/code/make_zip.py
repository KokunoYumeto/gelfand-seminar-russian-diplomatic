"""Create the requested single archive and verify its manifest and CRCs."""
import hashlib
import json
from pathlib import Path
import zipfile

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'final'/'GY1981'
TARGET=ROOT.parent/'GY1981.zip'
required={f'GY1981_{s}' for s in [
 'talks.json','items.json','problems.json','overview.tex','development.tex',
 'corrections.csv','references.bib','report.md','chapter.tex','test.pdf']}
assert required<=set(p.name for p in SOURCE.iterdir())
files=sorted(p for p in SOURCE.rglob('*') if p.is_file() and p.name!='MANIFEST.sha256')
manifest=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(SOURCE).as_posix()+'\n' for p in files)
(SOURCE/'MANIFEST.sha256').write_text(manifest)
files.append(SOURCE/'MANIFEST.sha256')
with zipfile.ZipFile(TARGET,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(files):z.write(p,p.relative_to(SOURCE).as_posix())
with zipfile.ZipFile(TARGET) as z:
    assert z.testzip() is None
    assert required<=set(z.namelist())
    for line in manifest.splitlines():
        expected,name=line.split('  ',1)
        assert hashlib.sha256(z.read(name)).hexdigest()==expected,name
    assert all(not n.startswith('/') and '..' not in Path(n).parts for n in z.namelist())
report={'archive':str(TARGET),'file_count':len(files),'bytes':TARGET.stat().st_size,
        'uncompressed_bytes':sum(p.stat().st_size for p in files),
        'sha256':hashlib.sha256(TARGET.read_bytes()).hexdigest(),
        'crc_check':'PASS','manifest_hash_check':'PASS','required_files':'PASS'}
(ROOT/'zip_validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
