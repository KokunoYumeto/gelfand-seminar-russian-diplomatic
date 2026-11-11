"""Create GY1966.zip and verify every archived byte against its manifest.

Uses only Python's standard library. Default output: the parent of the archive
root, named GY1966.zip. Pass an optional explicit destination as the first arg.
"""
from pathlib import Path
import hashlib
import json
import sys
import zipfile

ROOT = Path(__file__).resolve().parent.parent
DEST = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT.parent / 'GY1966.zip'
assert not DEST.is_relative_to(ROOT), 'Archive destination must be outside its source tree.'
manifest = ROOT / 'MANIFEST.sha256'
paths = sorted(p for p in ROOT.rglob('*') if p.is_file() and p != manifest)
manifest.write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' +
                            p.relative_to(ROOT).as_posix() + '\n' for p in paths))
paths.append(manifest)
with zipfile.ZipFile(DEST, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for path in sorted(paths):
        z.write(path, path.relative_to(ROOT).as_posix())
with zipfile.ZipFile(DEST) as z:
    assert z.testzip() is None
    assert len(z.namelist()) == len(paths)
    assert len(z.namelist()) == len(set(z.namelist()))
    for line in z.read('MANIFEST.sha256').decode().splitlines():
        digest, name = line.split('  ', 1)
        assert not name.startswith('/') and '..' not in Path(name).parts
        assert hashlib.sha256(z.read(name)).hexdigest() == digest, name
print(json.dumps({'status': 'PASS', 'archive': DEST.name,
                  'files_including_manifest': len(paths),
                  'size_bytes': DEST.stat().st_size,
                  'sha256': hashlib.sha256(DEST.read_bytes()).hexdigest(),
                  'zip_crc_test': 'PASS', 'all_manifest_hashes': 'PASS'}, indent=2))
