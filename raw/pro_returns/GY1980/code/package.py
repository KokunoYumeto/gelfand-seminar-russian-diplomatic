"""Package the complete chapter, reproducibility files, and supplied sources.

The archive contains no transient TeX format, cached runtime, or duplicate
rendered page images. Its internal SHA-256 manifest covers every payload file
except the manifest itself and the packaging log.
"""
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT.parent / 'GY1980.zip'
CHECKS = ROOT / 'checks'
INPUTS = ROOT / 'inputs'
if not INPUTS.is_dir():
    INPUTS = ROOT.parent / 'upload'

required = [
    'GY1980_talks.json', 'GY1980_items.json', 'GY1980_problems.json',
    'GY1980_overview.tex', 'GY1980_development.tex', 'GY1980_corrections.csv',
    'GY1980_references.bib', 'GY1980_report.md', 'GY1980_chapter.tex',
    'GY1980_test.pdf', 'GY1980_test.tex', 'GY1980_test.bbl', 'GY1980_test.log',
    'README.md', 'requirements.txt', 'build_chapter.py', 'gelfand_companion.sty',
    'previous_index.md', 'references_cumulative.bib',
]
files = {name: ROOT / name for name in required}
for directory, suffixes in {
    'code': {'.py'},
    'checks': {'.txt', '.md', '.json', '.csv'},
    'parts': {'.py', '.md', '.json', '.csv', '.bib'},
    'kit': {'.md', '.py', '.sty'},
}.items():
    for path in sorted((ROOT / directory).iterdir()):
        if path.is_file() and path.suffix in suffixes:
            files[str(path.relative_to(ROOT))] = path
for name in ['GY1980_en.tex', 'GY1980_ru.tex', 'GY1980_talks.md',
             'GY1980_prompt.md', 'GY1980_scans.zip']:
    files['inputs/' + name] = INPUTS / name
for name in ['checks/manifest_sha256.txt', 'checks/package_output.txt']:
    files.pop(name, None)
for name, path in files.items():
    if not path.is_file():
        raise SystemExit('Required file missing: ' + name)

audit = json.loads((CHECKS / 'pdf_audit.json').read_text())
assert audit['structural_result'] == 'PASS' and not any(audit['errors'].values())
assert (CHECKS / 'visual_review.md').is_file(), 'Visual review must be complete before packaging.'
assert 'STRICT VALIDATION PASS' in (CHECKS / 'validation_output.txt').read_text()
for name, phrase in [('weyl_output.txt', 'ALL EXACT WEYL CHECKS PASSED'),
                     ('formal_output.txt', 'ALL FORMAL TRUNCATION CHECKS PASSED'),
                     ('curve_models_output.txt', 'ALL AFFINE MODEL CHECKS PASSED')]:
    assert phrase in (CHECKS / name).read_text(), name

manifest = '\n'.join(hashlib.sha256(path.read_bytes()).hexdigest() + '  ' + name
                     for name, path in sorted(files.items())) + '\n'
manifest_path = CHECKS / 'manifest_sha256.txt'
manifest_path.write_text(manifest)
files['checks/manifest_sha256.txt'] = manifest_path

with zipfile.ZipFile(OUTPUT, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for name, path in sorted(files.items()):
        archive.write(path, name, compress_type=zipfile.ZIP_STORED if path.suffix == '.zip' else zipfile.ZIP_DEFLATED)
with zipfile.ZipFile(OUTPUT) as archive:
    assert archive.testzip() is None
    for name in required:
        assert name in archive.namelist()
    for line in manifest.splitlines():
        digest, name = line.split('  ', 1)
        assert hashlib.sha256(archive.read(name)).hexdigest() == digest, name

log = ('Archive: GY1980.zip\n'
       f'Payload files: {len(files) + 1}\n'
       f'PDF pages: {audit["pages"]}\n'
       'Required files: PASS\n'
       'Internal SHA-256 payload comparison: PASS\n'
       'Archive CRC check: PASS\n'
       'Schema, mathematical checks, PDF build and visual review: COMPLETE\n'
       'The archive includes this log; the manifest excludes itself and this log.\n')
log_path = CHECKS / 'package_output.txt'
log_path.write_text(log)
with zipfile.ZipFile(OUTPUT, 'a', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    archive.write(log_path, 'checks/package_output.txt')
with zipfile.ZipFile(OUTPUT) as archive:
    assert archive.testzip() is None
print(log, end='')
print('Final archive size:', OUTPUT.stat().st_size, 'bytes')
print('Final archive SHA-256:', hashlib.sha256(OUTPUT.read_bytes()).hexdigest())
