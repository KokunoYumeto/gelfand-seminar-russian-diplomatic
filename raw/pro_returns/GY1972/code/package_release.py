"""Create or verify a GY1972 release manifest and ZIP (standard library only)."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('directory',type=Path)
action=parser.add_mutually_exclusive_group(required=True)
action.add_argument('--verify',action='store_true')
action.add_argument('--zip',type=Path)
args=parser.parse_args()
root=args.directory.resolve()
manifest=root/'manifest.json'

def sha(data):
    return hashlib.sha256(data).hexdigest()

if args.verify:
    recorded=json.loads(manifest.read_text())
    for entry in recorded['files']:
        data=(root/entry['path']).read_bytes()
        assert len(data)==entry['bytes'],entry['path']
        assert sha(data)==entry['sha256'],entry['path']
    print(json.dumps({'status':'passed','files_verified':len(recorded['files'])},indent=2))
else:
    archive=args.zip.resolve()
    assert root not in archive.parents, 'The ZIP must be outside its payload directory.'
    files=sorted(p for p in root.rglob('*') if p.is_file()
                 and p!=manifest and '__pycache__' not in p.parts)
    entries=[]
    for p in files:
        data=p.read_bytes()
        entries.append({'path':p.relative_to(root).as_posix(),
                        'bytes':len(data),'sha256':sha(data)})
    report={'format':'GY1972 release manifest v1','status_cutoff':'2026-11-09',
            'files':entries,'manifest_excludes_itself':True}
    manifest.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in files+[manifest]:
            z.write(p,p.relative_to(root).as_posix())
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert len(z.namelist())==len(entries)+1
        assert all(not n.startswith('/') and '..' not in Path(n).parts for n in z.namelist())
        for entry in entries:
            data=z.read(entry['path'])
            assert len(data)==entry['bytes'] and sha(data)==entry['sha256'],entry['path']
    print(json.dumps({'status':'passed','archive':str(archive),
        'files':len(entries)+1,'bytes':archive.stat().st_size,
        'sha256':sha(archive.read_bytes()),'zip_crc_check':'passed',
        'all_archived_payload_hashes':'passed'},indent=2))
