"""Assemble reproducible chapter inputs, authoring records and checked outputs."""
from pathlib import Path
import shutil
import zipfile

BASE=Path(__file__).resolve().parent.parent
OUT=BASE/'deliverable/GY1976'
OUT.mkdir(parents=True,exist_ok=True)

def copy(src,dest):
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(src,dest)

for name in ['build_chapter.py','gelfand_companion.sty']:
    copy(BASE/'project/kit'/name,OUT/name)
for p in (BASE/'project/kit').iterdir():
    if p.is_file():copy(p,OUT/'code/kit_original'/p.name)
for name in ['previous_index.md','references_cumulative.bib']:
    copy(BASE/'project'/name,OUT/'code/inputs'/name)
for name in ['GY1976_prompt.md','GY1976_talks.md','GY1976_ru.tex','GY1976_en.tex']:
    copy(BASE/'upload'/name,OUT/'sources'/name)
for p in (BASE/'scans').rglob('*.png'):
    copy(p,OUT/'sources/scans'/p.name)
for p in Path('/usr/share/fonts/truetype/dejavu').glob('DejaVuSerif*.ttf'):
    if 'Condensed' not in p.name:copy(p,OUT/'fonts'/p.name)
copy(Path('/usr/share/doc/fonts-dejavu-core/copyright'),OUT/'fonts/LICENSE.txt')

for pre in ['early','middle','late','root']:
    for ext in ['talks.json','items.json','problems.json','corrections.csv','references.bib','meta.json']:
        copy(BASE/'work'/f'{pre}_{ext}',OUT/'code/segments'/f'{pre}_{ext}')
    copy(BASE/'work'/f'{pre}_research_log.md',OUT/'code/research'/f'{pre}_research_log.md')
    copy(BASE/'work'/f'{pre}_checks.tex',OUT/'code/research'/f'{pre}_checks.tex')
    for p in (BASE/'work').glob(pre+'_*.py'):
        if p.name!=pre+'_checks.py':copy(p,OUT/'code/authoring'/p.name)

for name in ['merge_chapter.py','compile_chapter.py','validate_chapter.py',
             'critical_checks.py','early_checks.py','middle_checks.py','render_and_audit.py',
             'write_frontmatter.py','prepare_delivery.py','package_delivery.py','editorial_layout_fixes.py',
             'editorial_bibliography_fixes.py']:
    p=BASE/'work'/name
    if p.exists():copy(p,OUT/'code'/name)
for name in ['critical_checks.json','early_checks_output.txt','middle_checks_output.txt',
             'middle_checks_output.json','middle_validation.json','late_validation_output.json',
             'middle_integration_bib_audit.json','late_correction_math_audit.json']:
    p=BASE/'work'/name
    if p.exists():copy(p,OUT/'code/output'/name)
for name in ['overview_template.tex','report_template.md']:
    copy(BASE/'work'/name,OUT/'code/templates'/name)
copy(BASE/'work/texmf/format_build.txt',OUT/'code/output/build/00_format_initial.txt')
for name in ['early_root_review.md','early_root43719_review.json']:
    copy(BASE/'work'/name,OUT/'code/research'/name)
print('Prepared inputs and audit records in',OUT)
