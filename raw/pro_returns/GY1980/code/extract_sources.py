"""Reproduce the page-by-page source workspace from the supplied attachments."""
import hashlib
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUTS = ROOT / 'inputs'
if not INPUTS.is_dir():
    INPUTS = ROOT.parent / 'upload'
PAGES = ROOT / 'source_pages'
SCANS = ROOT / 'scans'
PAGES.mkdir(exist_ok=True)
SCANS.mkdir(exist_ok=True)
manifest = {}
for language in ['en', 'ru']:
    source = INPUTS / f'GY1980_{language}.tex'
    content = source.read_text(encoding='utf-8')
    matches = list(re.finditer(r'(?m)^\\SourcePage\{GELFAND-(P\d{6})\}', content))
    identifiers = [m.group(1) for m in matches]
    assert identifiers == [f'P{n:06d}' for n in range(916, 981)]
    for i, match in enumerate(matches):
        end = matches[i+1].start() if i+1 < len(matches) else len(content)
        (PAGES / f'{match.group(1)}_{language}.tex').write_text(content[match.start():end])
    manifest[source.name] = {'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                             'pages': len(matches)}
    print(source.name, '65 source-page blocks extracted')

archive = INPUTS / 'GY1980_scans.zip'
with zipfile.ZipFile(archive) as z:
    names = [n for n in z.namelist() if re.search(r'GELFAND-P\d{6}\.png$', n)]
    assert len(names) == 65
    for name in names:
        # Write only the observed base filename; never extract arbitrary archive paths.
        (SCANS / Path(name).name).write_bytes(z.read(name))
manifest[archive.name] = {'sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
                          'scans': len(names)}
(ROOT / 'checks/source_input_hashes.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(archive.name, '65 notebook scans extracted')
print('Source extraction and page-range checks PASS')
