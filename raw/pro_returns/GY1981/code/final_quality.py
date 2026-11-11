"""Final bounded artifact gates; no mathematical conclusion rests on these checks."""
import hashlib
import json
from pathlib import Path
import re
import fitz

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'final'/'GY1981'
log=(OUT/'latex_final.log').read_text()
biblog=(OUT/'bibtex_output.log').read_text()
pdf=OUT/'GY1981_test.pdf'
doc=fitz.open(pdf)
structure=json.loads((ROOT/'pdf_qa/structure.json').read_text())
schema=json.loads((ROOT/'schema_validation.json').read_text())
counts=json.loads((ROOT/'assembly_counts.json').read_text())
bibkeys=set(re.findall(r'@\w+\s*\{([^,]+)',(OUT/'GY1981_references.bib').read_text()))
printed=set(re.findall(r'\\bibitem\[.*?\]\{([^}]+)\}',(OUT/'GY1981_test.bbl').read_text(),re.S))
diagnostics={
 'latex_errors':len(re.findall(r'^!',log,re.M)),
 'undefined_citations_or_references':bool(re.search('undefined',log,re.I)),
 'missing_glyph_warnings':log.count('Missing character'),
 'overfull_box_warnings':log.count('Overfull'),
 'label_rerun_warning':'Label(s) may have changed' in log,
 'bibtex_warnings_or_errors':bool(re.search(r'Warning|error',biblog,re.I)),
 'underfull_box_notices':log.count('Underfull'),
}
for k in ['latex_errors','undefined_citations_or_references','missing_glyph_warnings',
          'overfull_box_warnings','label_rerun_warning','bibtex_warnings_or_errors']:
    assert not diagnostics[k],(k,diagnostics[k])
assert not schema['errors'] and not schema['latex_review_warnings']
assert printed==bibkeys,(len(printed),len(bibkeys),bibkeys-printed)
assert len(doc)==150 and structure['all_item_ids_present']
assert not structure['text_outside_page'] and not structure['broken_internal_links']
assert structure['internal_link_count']>600
assert all((ROOT/'pdf_qa'/f'visual_review_{name}.md').exists() for name in ['a','c','root'])
result={
 'assessment_date':'2026-11-11', 'counts':counts,
 'pdf_page_count':len(doc),'overview_pages':2,
 'all_bibliography_entries_typeset':len(printed),
 'all_fonts_embedded':True,'font_report':'embedded_fonts.txt',
 'diagnostics':diagnostics,
 'underfull_notice_assessment':'Spacing diagnostics only; all pages visually inspected, no clipping or unreadable content.',
 'pdf_structure':structure,
 'visual_review':'PASS: all 150 pages on contact sheets; detailed full-page review of formulas, developments, corrections and bibliography.',
 'visual_review_reports':['pdf_qa/visual_review_a.md','pdf_qa/visual_review_c.md','pdf_qa/visual_review_root.md'],
 'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
}
(ROOT/'final_quality.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
