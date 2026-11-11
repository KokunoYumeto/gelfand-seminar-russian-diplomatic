"""Collect reviewed code, authoring checkpoints and audit files for delivery.

This collection script runs in the original task workspace, before archiving.
The portable rebuild/check entry points are separate and need no source inputs.
"""
import difflib,hashlib,importlib.metadata,json,platform,shutil,subprocess,sys,zipfile
from pathlib import Path
W=Path(__file__).resolve().parent.parent
root=W.parent;D=W/'deliverable';C=D/'code';A=C/'authoring';AW=A/'work'
for path in (C,AW,D/'audit/sources',D/'audit/reviews',C/'kit_original',AW/'code',AW/'kit',A/'upload'):
    path.mkdir(parents=True,exist_ok=True)
def cp(src,dst):
    dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
portable=['build_all.py','check_mathematics.py','check_mathematics_output.json','validate_chapter.py','check_previous_links.py','rebuild.sh','run_checks.py','pdf_qa.py','package_zip.py','check_archive.py']
for name in portable:
    if (W/'code'/name).exists():cp(W/'code'/name,C/name)
(C/'rebuild.sh').chmod(0o755)
authoring=['assemble.py','write_report.py','format_corrections.py','format_layout.py','cumulative_keys.json','validate_chapter.py','format_corrections_mapping.json','format_corrections_qa.json','collect_package.py','README_package.md']
for name in authoring:cp(W/'code'/name,AW/'code'/name)
parts=['early','strings','virasoro','late']
for part in parts:
    for src in (W/part).iterdir():
        if src.is_file() and src.suffix in {'.py','.json','.csv','.bib','.tex','.md','.txt'}:
            cp(src,AW/part/src.name)
    cp(W/part/'sources.json',D/'audit/sources'/f'{part}_sources.json')
    cp(W/part/'research_notes.md',D/'audit/sources'/f'{part}_research_notes.md')
    for src in (W/part).glob('*review*.md'):cp(src,D/'audit/reviews'/f'{part}_{src.name}')
for name in ['reassembly_probe_output.json']:
    cp(W/'early'/name,D/'audit/reviews'/name)
for name in ['format_corrections_mapping.json','format_corrections_qa.json']:
    cp(W/'code'/name,D/'audit'/name)
for name in ['build_chapter.py','gelfand_companion.sty','CHAPTER_FORMAT.md']:
    cp(W/'kit'/name,AW/'kit'/name);cp(W/'kit'/name,C/'kit_original'/name)
for name in ['previous_index.md','references_cumulative.bib']:cp(W/name,AW/name)
for name in ['GY1985_en.tex','GY1985_ru.tex','GY1985_talks.md','GY1985_prompt.md']:
    cp(root/'upload'/name,A/'upload'/name)
for name in ['GY1985_test.log','GY1985_test.blg','GY1985_test.bbl']:
    cp(D/name,D/'audit/buildlogs'/name)
cp(W/'code/README_package.md',D/'README.md')
(D/'requirements-checks.txt').write_text('sympy==1.14.0\n')
(D/'requirements-render.txt').write_text('PyMuPDF==1.26.6\nPillow==13.0.0\n')
versions={'python':platform.python_version(),'packages':{n:importlib.metadata.version(n) for n in ['sympy','mpmath','PyMuPDF','Pillow']}}
for cmd in ['xelatex','bibtex']:
    p=subprocess.run([cmd,'--version'],text=True,capture_output=True)
    versions[cmd]=p.stdout.splitlines()[0]
(D/'audit/environment.json').write_text(json.dumps(versions,indent=2)+'\n')
inputs=[]
for src in sorted((root/'upload').iterdir()):
    if src.is_file():inputs.append({'file':str(src.relative_to(root)),'bytes':src.stat().st_size,'sha256':hashlib.sha256(src.read_bytes()).hexdigest()})
for src in sorted((W/'scans').glob('*.png')):
    inputs.append({'file':'scans/'+src.name,'bytes':src.stat().st_size,'sha256':hashlib.sha256(src.read_bytes()).hexdigest()})
(D/'audit/input_manifest.json').write_text(json.dumps({'scope':'Supplied attachments plus every decompressed scan; hashes identify source witnesses without duplicating scan payloads.','files':inputs},indent=2)+'\n')
with zipfile.ZipFile(root/'upload/GY1985_kit.zip') as z:
    kit=[]
    for name in ['build_chapter.py','gelfand_companion.sty','CHAPTER_FORMAT.md']:
        raw=z.read('kit/'+name);pub=(D/name).read_bytes()
        kit.append({'file':name,'supplied_sha256':hashlib.sha256(raw).hexdigest(),'published_sha256':hashlib.sha256(pub).hexdigest(),'identical':raw==pub})
assert all(x['identical'] for x in kit)
(D/'audit/kit_provenance.json').write_text(json.dumps({'status':'PASS','scope':'Byte-for-byte comparison with the kit attached to this task. The compatibility-amendment header already exists in that supplied builder.','files':kit},indent=2)+'\n')
result={'status':'PASS','authoring_fragments':parts,'input_witnesses':len(inputs),'kit_files_unchanged':True,'binary_tex_formats_included':False,'original_scans_included':False,'private_transfer_helpers_included':False}
(D/'audit/package_preparation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
