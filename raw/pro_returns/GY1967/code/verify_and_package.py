"""Check the final deliverable and create the single requested ZIP archive.

Run after the final build and visual review. Uses only the Python standard
library and the installed Poppler pdfinfo/pdftotext executables.
"""
from pathlib import Path
import collections
import csv
import difflib
import hashlib
import json
import re
import shutil
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT/'audit'
REQUIRED = ['GY1967_talks.json', 'GY1967_items.json', 'GY1967_problems.json',
            'GY1967_overview.tex', 'GY1967_development.tex', 'GY1967_corrections.csv',
            'GY1967_references.bib', 'GY1967_report.md', 'GY1967_chapter.tex',
            'GY1967_test.pdf']
assert all((ROOT/name).is_file() and (ROOT/name).stat().st_size for name in REQUIRED)
dataset = json.loads((AUDIT/'dataset_validation.json').read_text())
assert dataset['status']=='PASS' and not dataset['errors']
items = json.loads((ROOT/'GY1967_items.json').read_text())
talks = json.loads((ROOT/'GY1967_talks.json').read_text())
problems = json.loads((ROOT/'GY1967_problems.json').read_text())
with (ROOT/'GY1967_corrections.csv').open(newline='') as file:
    corrections = list(csv.DictReader(file))
bib = (ROOT/'GY1967_references.bib').read_text()
keys = re.findall(r'(?m)^@\w+\s*\{\s*([^,\s]+)', bib)
assert len(keys)==len(set(keys))==95
assert len(talks)==43 and len(items)==320 and len(problems)==11 and len(corrections)==101
assert collections.Counter(item['class'] for item in items)==dict(A=42,B=8,C=3,E=239,F=28)

def command(name):
    path = Path('/usr/bin')/name
    return str(path) if path.exists() else shutil.which(name)

pdf = ROOT/'GY1967_test.pdf'
info = subprocess.check_output([command('pdfinfo'),str(pdf)],text=True)
text = subprocess.check_output([command('pdftotext'),'-layout',str(pdf),'-'],text=True)
pages = int(re.search(r'^Pages:\s+(\d+)',info,re.M)[1])
missing_ids = [item['id'] for item in items if item['id'] not in text]
assert not missing_ids, missing_ids
missing_records = [talk['record'] for talk in talks
                   if not re.search(r'\brecord\s+'+str(talk['record'])+r'\b',text)]
assert not missing_records, missing_records

log = (ROOT/'GY1967_test.log').read_text(errors='replace')
patterns = {'latex_errors':r'^!', 'overfull_boxes':r'Overfull \\[hv]box',
            'missing_characters':r'Missing character:',
            'undefined_citations':r'Citation .* undefined',
            'undefined_references':r'(?:Reference .* undefined|There were undefined references)',
            'latex_or_package_warnings':r'(?:LaTeX|Package [^\n]+) Warning:'}
issues = {name:len(re.findall(pattern,log,re.M)) for name,pattern in patterns.items()}
assert not any(issues.values()), issues
assert 'Output written on GY1967_test.pdf ('+str(pages)+' pages)' in log
blg = (ROOT/'GY1967_test.blg').read_text(errors='replace')
bibtex_warnings = len(re.findall(r'Warning--|error message',blg,re.I))
assert bibtex_warnings==0
assert 'Built GY1967_chapter.tex and GY1967_test.pdf successfully.' in (AUDIT/'build_chain_stdout.txt').read_text()
weyl = json.loads((AUDIT/'verify_weyl_output.json').read_text())
assert weyl['total_assertions']==522 and weyl['status']=='all exact checks passed'
assert json.loads((AUDIT/'regeneration.json').read_text())['packaged_fragment_regeneration_identical']
assert (AUDIT/'visual_review.md').is_file()
render = json.loads((AUDIT/'render_output.json').read_text())
assert render['rendered_pages']==pages

patch=[]
for name in ['build_chapter.py','gelfand_companion.sty']:
    before=(ROOT/'code/kit_original'/name).read_text().splitlines(keepends=True)
    after=(ROOT/name).read_text().splitlines(keepends=True)
    patch.extend(difflib.unified_diff(before,after,fromfile='kit_original/'+name,tofile=name))
(ROOT/'code/kit_changes.patch').write_text(''.join(patch))

verification = {
    'status':'PASS', 'status_date':'2026-11-09',
    'records':43, 'items':320, 'problems':11, 'corrections':101, 'references':95,
    'class_counts':{key:collections.Counter(item['class'] for item in items)[key] for key in 'ABCDEF'},
    'required_deliverables':REQUIRED, 'pdf_pages':pages,
    'pdf_bytes':pdf.stat().st_size, 'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'all_occurrence_ids_in_pdf':True, 'all_catalogue_records_in_pdf':True,
    'final_latex_log':issues, 'bibtex_warnings':bibtex_warnings,
    'build_sequence':['python build_chapter.py GY1967','XeLaTeX','BibTeX','XeLaTeX','XeLaTeX'],
    'build_script_success':True, 'packaged_data_regeneration_identical':True,
    'weyl_exact_assertions':weyl['total_assertions'], 'editorial_arithmetic_checks':105,
    'additional_elementary_check_families':6,
    'visual_review':'audit/visual_review.md',
    'scope':'Structural/build/computation checks supplement the source audits and complete proofs; they do not independently establish every historical theorem.'
}
(AUDIT/'final_verification.json').write_text(json.dumps(verification,indent=2)+'\n')
(AUDIT/'final_pdfinfo.txt').write_text(info)

def included(path):
    relative=path.relative_to(ROOT)
    return (path.is_file() and '.build-cache' not in relative.parts
            and '__pycache__' not in relative.parts and path.suffix!='.pyc'
            and path.name!='MANIFEST.sha256')

files=sorted(path for path in ROOT.rglob('*') if included(path))
manifest=''.join(hashlib.sha256(path.read_bytes()).hexdigest()+'  '+path.relative_to(ROOT).as_posix()+'\n'
                 for path in files)
(ROOT/'MANIFEST.sha256').write_text(manifest)
files.append(ROOT/'MANIFEST.sha256')
archive=ROOT.parent/'GY1967.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as package:
    for path in sorted(files):
        package.write(path,Path('GY1967')/path.relative_to(ROOT))
with zipfile.ZipFile(archive) as package:
    assert package.testzip() is None
    assert all('GY1967/'+name in package.namelist() for name in REQUIRED)
    assert len(package.namelist())==len(files)
    for line in manifest.splitlines():
        digest,name=line.split('  ',1)
        assert hashlib.sha256(package.read('GY1967/'+name)).hexdigest()==digest
print(json.dumps({'status':'PASS','archive':str(archive),'members':len(files),
                  'bytes':archive.stat().st_size,
                  'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
                  'crc_checked':True,'all_manifest_hashes_checked':True,
                  'pdf_pages':pages},indent=2))
