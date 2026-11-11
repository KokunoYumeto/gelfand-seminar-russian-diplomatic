"""Audit the built PDF and render contact sheets for human visual inspection.

Structural checks do not replace visual review. The latter is documented
separately in checks/visual_review.md after the rendered pages are inspected.
"""
import json
import math
import re
import subprocess
from pathlib import Path

import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
CHECKS = ROOT / 'checks'
QA = ROOT / 'qa'
QA.mkdir(exist_ok=True)
document = fitz.open(ROOT / 'GY1980_test.pdf')
items = json.loads((ROOT / 'GY1980_items.json').read_text())
talks = json.loads((ROOT / 'GY1980_talks.json').read_text())
texts = [page.get_text() for page in document]
text = '\n'.join(texts).replace('–', '-')
missing_items = [item['id'] for item in items if item['id'] not in text]
missing_records = [talk['record'] for talk in talks
                   if f"record {talk['record']}" not in text]
empty_pages = [i+1 for i, content in enumerate(texts) if len(content.strip()) < 8]
outside_page = []
for number, page in enumerate(document, 1):
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines', []):
            for span in line['spans']:
                x0, y0, x1, y1 = span['bbox']
                if x0 < -0.5 or y0 < -0.5 or x1 > page.rect.width+0.5 or y1 > page.rect.height+0.5:
                    outside_page.append({'page': number, 'text': span['text'], 'bbox': span['bbox']})

log = (ROOT / 'GY1980_test.log').read_text(errors='replace')
biblog = (CHECKS / 'bibtex_output.txt').read_text(errors='replace')
errors = {}
for name, expression in {
    'missing_glyphs': r'Missing character:',
    'undefined_citations_or_references': r'(?:Citation|Reference|Hyper reference)[^\n]*undefined|There were undefined',
    'unstable_references': r'Label\(s\) may have changed|Rerun to get (?:cross-references|outlines) right',
    'duplicate_labels': r'multiply defined',
    'latex_errors': r'LaTeX Error:|Missing \$ inserted|Undefined control sequence|^!',
    'overfull_boxes': r'Overfull \\[hv]box',
}.items():
    errors[name] = len(re.findall(expression, log, flags=re.M))
errors['bibtex_warnings'] = biblog.count('Warning--')
errors['items_missing_from_PDF'] = len(missing_items)
errors['records_missing_from_PDF'] = len(missing_records)
errors['empty_pages'] = len(empty_pages)
errors['text_outside_physical_page'] = len(outside_page)
toc = document.get_toc()
first_record_page = next((row[2] for row in toc if row[0] == 2), None)
errors['overview_exceeds_two_pages'] = int(first_record_page is None or first_record_page > 2)

font_result = subprocess.run(['pdffonts', str(ROOT / 'GY1980_test.pdf')],
                             text=True, capture_output=True, check=True)
(CHECKS / 'pdf_fonts.txt').write_text(font_result.stdout)

# Sixteen consecutive pages per sheet, all pages covered once.
thumbnail_width, label_height, gap = 285, 24, 12
thumbnail_height = math.ceil(document[0].rect.height / document[0].rect.width * thumbnail_width)
columns, rows = 4, 4
sheets = []
for start in range(0, len(document), columns*rows):
    canvas = Image.new('RGB',
                       (columns*(thumbnail_width+gap)+gap,
                        rows*(thumbnail_height+label_height+gap)+gap), '#d4d7da')
    draw = ImageDraw.Draw(canvas)
    for offset in range(min(columns*rows, len(document)-start)):
        page_number = start+offset
        page = document[page_number]
        pix = page.get_pixmap(matrix=fitz.Matrix(thumbnail_width/page.rect.width,
                                                 thumbnail_width/page.rect.width), alpha=False)
        thumbnail = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
        x = gap + offset % columns * (thumbnail_width+gap)
        y = gap + offset // columns * (thumbnail_height+label_height+gap)
        draw.text((x+4, y+5), f'Page {page_number+1}', fill='black')
        canvas.paste(thumbnail, (x, y+label_height))
    filename = f'contact_{start+1:03d}_{min(start+columns*rows, len(document)):03d}.png'
    canvas.save(QA / filename)
    sheets.append(filename)

representative_pages = [1, 2, 8, 12, 31, 61, 81, 96, 108, 109, 110, 111,
                        112, 113, 116, 117, 128, 131, len(document)]
for page_number in sorted(set(representative_pages)):
    subprocess.run(['pdftoppm', '-f', str(page_number), '-singlefile',
                    '-scale-to', '1500', '-png', str(ROOT / 'GY1980_test.pdf'),
                    str(QA / f'representative_{page_number:03d}')],
                   text=True, capture_output=True, check=True)

audit = {'pages': len(document), 'overview_page_range': [1, first_record_page],
         'expected_records': len(talks), 'expected_items': len(items),
         'errors': errors, 'missing_item_ids': missing_items,
         'missing_record_numbers': missing_records, 'empty_page_numbers': empty_pages,
         'outside_page_spans': outside_page,
         'underfull_box_diagnostics': log.count('Underfull \\hbox'),
         'bookmarks': toc, 'rendered_contact_sheets': sheets,
         'full_page_poppler_renders': sorted(set(representative_pages)),
         'structural_result': 'PASS' if not any(errors.values()) else 'FAIL'}
(CHECKS / 'pdf_audit.json').write_text(json.dumps(audit, indent=2, ensure_ascii=False) + '\n')
print('PDF pages:', len(document))
print('Overview occupies pages 1 through', first_record_page)
for key, value in errors.items():
    print(key, value)
print('Underfull-box diagnostics for visual review:', audit['underfull_box_diagnostics'])
print('Contact sheets rendered:', len(sheets), '(all pages)')
print('Full-page Poppler renders:', len(set(representative_pages)))
print('PDF structural audit:', audit['structural_result'])
raise SystemExit(int(any(errors.values())))
