#!/usr/bin/env python3
"""Build and verify the one-file GY1979 delivery, without raw source downloads.

The seven prescribed data files, report, built TeX/PDF, original build support,
research/verification code and outputs are archived at their documented paths.
The payload manifest hashes every ordinary member. The two control reports
are excluded from their own hash list to avoid circular self-hashes.
"""
from pathlib import Path
import hashlib, json, shutil, zipfile
import fitz

D=Path(__file__).resolve().parent.parent
OUT=D.parent/'GY1979.zip'
REQUIRED=[
    'GY1979_talks.json','GY1979_items.json','GY1979_problems.json',
    'GY1979_overview.tex','GY1979_development.tex','GY1979_corrections.csv',
    'GY1979_references.bib','GY1979_report.md','GY1979_chapter.tex','GY1979_test.pdf']
ROOT_SUPPORT=['README.md','CHAPTER_FORMAT.md','build_chapter.py',
              'gelfand_companion.sty','GY1979_test.tex','root_references.bib']
CONTROL=['code/package_manifest.json','code/archive_validation.json']
BUILD_ARTIFACTS=['GY1979_test.log','GY1979_test.blg','GY1979_test.bbl','GY1979_test.aux']
for name in REQUIRED+ROOT_SUPPORT:
    assert (D/name).is_file(),name
assert json.loads((D/'code/audit_output.json').read_text())['result']=='PASS'
status=json.loads((D/'code/build_status.json').read_text())
assert all(x['exit_code']==0 for x in status['commands'])
assert all('Underfull' in x for x in status['log_flags']),status['log_flags']
assert (D/'code/visual_qa.md').is_file()
qa=json.loads((D/'code/pdf_qa_output.json').read_text())
assert qa['sha256']==hashlib.sha256((D/'GY1979_test.pdf').read_bytes()).hexdigest()
assert qa['all_pages_rendered'] and not qa['text_spans_outside_page']
assert json.loads((D/'code/verify_energy_identity_output.json').read_text())['all_checks_passed']

build_dir=D/'code/tex_build_artifacts';build_dir.mkdir(exist_ok=True)
for name in BUILD_ARTIFACTS:
    assert (D/name).exists()
    shutil.copy2(D/name,build_dir/name)
payload={name:D/name for name in REQUIRED+ROOT_SUPPORT}
for path in sorted((D/'code').rglob('*')):
    if not path.is_file() or '__pycache__' in path.parts:continue
    relative=path.relative_to(D).as_posix()
    if relative in CONTROL or path.suffix=='.pyc':continue
    payload[relative]=path
manifest={
    'assessment_date':'2026-11-10',
    'archive':'GY1979.zip',
    'root_required_files':REQUIRED,
    'control_files_excluded_from_self_hashes':CONTROL,
    'payload':[
        {'path':name,'bytes':path.stat().st_size,
         'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
        for name,path in sorted(payload.items())],
    'excluded_intermediates':'Raw scans/transcriptions, source-paper downloads, temporary full-page renders, temporary TeX runtime and development-only PDFs.'}
(D/CONTROL[0]).write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')

def write_archive(include_validation=False):
    members=dict(payload)
    members[CONTROL[0]]=D/CONTROL[0]
    if include_validation:members[CONTROL[1]]=D/CONTROL[1]
    with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
        for name,path in sorted(members.items()):
            info=zipfile.ZipInfo(name,date_time=(2026,11,10,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=(0o100644<<16)
            archive.writestr(info,path.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)

def check_archive(expect_validation):
    with zipfile.ZipFile(OUT) as archive:
        names=archive.namelist()
        assert len(names)==len(set(names))
        assert set(REQUIRED)<=set(names)
        assert all(not name.startswith('/') and '..' not in Path(name).parts for name in names)
        assert archive.testzip() is None
        for row in manifest['payload']:
            data=archive.read(row['path'])
            assert len(data)==row['bytes']
            assert hashlib.sha256(data).hexdigest()==row['sha256']
        pdfs=[x for x in names if x.lower().endswith('.pdf')]
        assert pdfs==['GY1979_test.pdf'],pdfs
        for name in ['GY1979_talks.json','GY1979_items.json','GY1979_problems.json']:
            json.loads(archive.read(name))
        if expect_validation:
            assert CONTROL[1] in names
            assert len(names)==len(payload)+2
        return names

write_archive()
check_archive(False)
validation={
    'result':'PASS',
    'archive':'GY1979.zip',
    'members':len(payload)+2,
    'payload_files':len(payload),
    'required_root_files_present':True,
    'duplicate_member_names':[],
    'unsafe_member_paths':[],
    'zip_crc_test':'PASS',
    'payload_sha256_test':'PASS',
    'pdf_count':1,
    'pdf_pages':len(fitz.open(D/'GY1979_test.pdf')),
    'pdf_sha256':qa['sha256'],
    'schema_audit':'PASS',
    'tex_build':'PASS',
    'visual_qa':'See code/visual_qa.md; all pages rendered and contact sheets inspected.',
    'note':'The archive is tested again after this report is included. This control file and the manifest omit self-hashes.'}
(D/CONTROL[1]).write_text(json.dumps(validation,indent=2)+'\n')
write_archive(True)
check_archive(True)
print(json.dumps({**validation,'zip_bytes':OUT.stat().st_size,
                  'zip_sha256':hashlib.sha256(OUT.read_bytes()).hexdigest()},indent=2))
