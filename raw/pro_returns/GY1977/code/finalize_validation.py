"""Validate the final compiled, visually reviewed chapter before packaging.

Usage: python code/finalize_validation.py CHAPTER_DIRECTORY [ORIGINAL_KIT]
This records mechanical checks; it does not automate the documented visual
inspection or establish the mathematical results by itself.
"""
from pathlib import Path
import hashlib,json,re,subprocess,sys
from pypdf import PdfReader

D=Path(sys.argv[1]).resolve()
OUT=D/'code/output'
kit=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else D/'code/source_inputs/kit'
errors=[]
def require(test,message):
    if not test:errors.append(message)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

pdf=D/'GY1977_test.pdf'
reader=PdfReader(pdf)
texts=[p.extract_text() or '' for p in reader.pages]
fulltext='\n'.join(texts)
log=(D/'GY1977_test.log').read_text()
blg=(D/'GY1977_test.blg').read_text()
commands=json.loads((OUT/'compile_commands.json').read_text())
data=json.loads((OUT/'data_validation.json').read_text())
render=json.loads((OUT/'qa/render_manifest.json').read_text())
review=json.loads((OUT/'visual_review.json').read_text())
items=json.loads((D/'GY1977_items.json').read_text())
checks={
    'LaTeX_errors':len(re.findall(r'^!',log,re.M)),
    'LaTeX_warnings':len(re.findall(r'LaTeX Warning:',log)),
    'package_warnings':len(re.findall(r'Package [^\n]* Warning:',log)),
    'overfull_boxes':len(re.findall(r'Overfull \\',log)),
    'missing_glyphs':len(re.findall(r'Missing character:',log)),
    'undefined_references_or_citations':len(re.findall(r'(?:Reference|Citation)[^\n]*undefined',log)),
    'BibTeX_warnings':len(re.findall(r'Warning--',blg)),
    'BibTeX_errors':len(re.findall(r'error message',blg)),
}
for name,count in checks.items():require(count==0,f'{name}: {count}')
require(len(commands)==6 and all(c['returncode']==0 for c in commands),'Prescribed compilation command failed or missing')
require(data['result']=='PASS' and not data['errors'] and not data['warnings'],'Canonical-data validation incomplete')
require(render['pdf_sha256']==digest(pdf),'Page renders do not correspond to final PDF')
require(render['pdf_pages']==len(reader.pages),'Rendered page count differs')
require(not render['nearly_empty_pages'],'An abnormally sparse page needs review')
require(review['result']=='PASS' and review['pdf_sha256']==digest(pdf),'Visual review is missing, incomplete or stale')
require(review['thumbnail_pages']==list(range(1,len(reader.pages)+1)),'Not every page was visually inspected as a thumbnail')
require((OUT/'visual_review.md').is_file(),'Written visual review missing')
missing=[i['id'] for i in items if not re.search(re.escape(i['id'])+r'(?!\d)',fulltext)]
require(not missing,'Occurrence IDs absent from PDF: '+', '.join(missing))
require('1.1' in texts[1] and re.search(r'V\.\s*G\.\s*Drinfeld',texts[1]),'Two-page overview boundary changed; inspect manually')

bib=(D/'GY1977_references.bib').read_text()
bib_keys=set(re.findall(r'(?m)^\s*@\w+\s*\{\s*([^,\s]+)\s*,',bib))
bbl_keys=set(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}',(D/'GY1977_test.bbl').read_text()))
require(bbl_keys==bib_keys,'Printed bibliography does not contain exactly all bibliography entries')

fonts=subprocess.run(['pdffonts',str(pdf)],check=True,capture_output=True,text=True).stdout
info=subprocess.run(['pdfinfo',str(pdf)],check=True,capture_output=True,text=True).stdout
(OUT/'pdffonts.txt').write_text(fonts)
(OUT/'pdfinfo.txt').write_text(info)
font_rows=[line.split() for line in fonts.splitlines()[2:] if line.strip()]
require(bool(font_rows) and all(row[-5]=='yes' for row in font_rows),'One or more PDF fonts are not embedded')
require(' (A4)' in info,'PDF page dimensions are not A4')
require(bool(re.search(r'Encrypted:\s+no',info)),'PDF unexpectedly encrypted')
require(bool(re.search(r'JavaScript:\s+no',info)),'PDF unexpectedly contains JavaScript')

kit_matches={name:bool((kit/name).is_file() and digest(D/name)==digest(kit/name))
             for name in ['build_chapter.py','gelfand_companion.sty','CHAPTER_FORMAT.md']}
require(all(kit_matches.values()),'The supplied chapter kit has changed')

result={
    'result':'FAIL' if errors else 'PASS',
    'pdf_pages':len(reader.pages),'pdf_sha256':digest(pdf),
    'compiled_commands':commands,'diagnostics':checks,
    'font_count':len(font_rows),'all_fonts_embedded':all(r[-5]=='yes' for r in font_rows),
    'paper':'A4','encrypted':reader.is_encrypted,
    'all_occurrence_ids_found':not missing,'occurrence_count':len(items),
    'printed_bibliography_entries':len(bbl_keys),'overview_pages':[1,2],
    'records':data['records'],'problems':data['problems'],
    'source_page_locators':data['pages_with_item_locators'],
    'supplied_kit_unchanged':kit_matches,
    'typography_repairs':'Canonical text and development only; see repair_typesetting.py and output/typesetting_repairs.json.',
    'visual_review':'See visual_review.md, visual_review.json, and qa/ contact sheets.',
    'errors':errors,
}
(OUT/'build_validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
sys.exit(bool(errors))
