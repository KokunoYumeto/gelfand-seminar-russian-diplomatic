#!/usr/bin/env python3
"""Check PDF structure and render every page with Poppler for visual inspection.

The JSON is an automated audit, not a substitute for inspecting the rendered
contact sheets and the detailed mathematical pages.  No PDF content is edited.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import json
import re
import subprocess
import sys

import fitz
from PIL import Image, ImageDraw, ImageFont


parser = argparse.ArgumentParser()
parser.add_argument('directory', type=Path)
parser.add_argument('--render-dir', type=Path)
args = parser.parse_args()
root = args.directory.resolve()
render = (args.render_dir or root / 'audit' / 'rendered').resolve()
render.mkdir(parents=True, exist_ok=True)
pdf = root / 'GY1975_test.pdf'
doc = fitz.open(pdf)
counts = json.loads((root / 'audit/counts.json').read_text())
items = json.loads((root / 'GY1975_items.json').read_text())
text = '\n'.join(page.get_text() for page in doc)
(render / 'pdf_text.txt').write_text(text)
missing_items = [x['id'] for x in items if x['id'] not in text]
outside_page = []
outer_margin = []
empty_pages = []
for n, page in enumerate(doc, 1):
    if len(page.get_text().strip()) < 20:
        empty_pages.append(n)
    for word in page.get_text('words'):
        x0, y0, x1, y1, content = word[:5]
        if x0 < -0.5 or y0 < -0.5 or x1 > page.rect.width + 0.5 or y1 > page.rect.height + 0.5:
            outside_page.append({'page': n, 'text': content, 'bbox': list(word[:4])})
        if x0 < 45 or x1 > page.rect.width - 45:
            outer_margin.append({'page': n, 'text': content, 'bbox': list(word[:4])})

logs = root / 'build_logs'
passes = sorted(logs.glob('pass_*.log'), key=lambda p: int(p.stem.split('_')[-1]))
last = passes[-1]
last_text = last.read_text()
diagnostics = [line for line in last_text.splitlines() if re.search(
    r'Overfull|Warning|Missing character|undefined|^!|LaTeX Error', line)]
underfull = [line for line in last_text.splitlines() if 'Underfull' in line]
bib_diagnostics = [line for line in (logs / 'pass_2.log').read_text().splitlines()
                   if re.search(r'Warning|error|couldn.t|not found', line, re.I)]
markers = {
    'first_talk': '1975-09-15',
    'perchik_development': 'A certified finite development of the',
    'spectral_development': 'What the Abel spectral-phase limit requires',
    'problem_index': 'Problem index',
    'corrections': 'Corrections to the transcription',
    'bibliography': 'Bibliography',
}
locations = {key: [i + 1 for i, page in enumerate(doc)
                   if needle in re.sub(r'\s+', ' ', page.get_text())]
             for key, needle in markers.items()}
result = {
    'pdf': pdf.name,
    'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'pages': len(doc),
    'page_size_points': list(doc[0].rect)[2:],
    'items_expected': counts['items'],
    'missing_item_ids': missing_items,
    'empty_pages': empty_pages,
    'text_outside_page': outside_page,
    'text_in_outer_margin': outer_margin,
    'last_tex_log': last.name,
    'last_tex_diagnostics': diagnostics,
    'underfull_spacing_notices': underfull,
    'bibtex_diagnostics': bib_diagnostics,
    'section_pages': locations,
    'python': sys.version,
    'packages': {name: importlib.metadata.version(name)
                 for name in ['PyMuPDF', 'Pillow', 'sympy', 'mpmath']},
    'automated_pass': not (missing_items or empty_pages or outside_page or outer_margin
                           or diagnostics or bib_diagnostics),
    'visual_review': 'Rendered contact sheets require separate human/model inspection.',
}
subprocess.run(['pdftoppm', '-r', '44', '-png', str(pdf), str(render / 'page')],
               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
pages = sorted(render.glob('page-*.png'))
assert len(pages) == len(doc), (len(pages), len(doc))
tile_width, tile_height = 380, 565
cols, rows = 4, 4
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
sheets = []
for start in range(0, len(pages), cols * rows):
    contact = Image.new('RGB', (cols * tile_width, rows * tile_height), '#d8d8d8')
    draw = ImageDraw.Draw(contact)
    for offset, path in enumerate(pages[start:start + cols * rows]):
        im = Image.open(path).convert('RGB')
        im.thumbnail((tile_width - 16, tile_height - 36))
        x = (offset % cols) * tile_width + (tile_width - im.width) // 2
        y = (offset // cols) * tile_height + 26
        contact.paste(im, (x, y))
        draw.text(((offset % cols) * tile_width + 10,
                   (offset // cols) * tile_height + 5),
                  f'Page {start + offset + 1}', fill='black', font=font)
    out = render / f'contact_{start // (cols * rows) + 1:02d}.png'
    contact.save(out)
    sheets.append(out.name)
result['rendered_pages'] = len(pages)
result['contact_sheets'] = sheets
(root / 'audit/pdf_audit.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
if not result['automated_pass']:
    raise SystemExit(1)
