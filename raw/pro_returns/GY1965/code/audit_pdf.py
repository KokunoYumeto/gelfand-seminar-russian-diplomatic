#!/usr/bin/env python3
"""Audit the built PDF and optionally make contact sheets for visual inspection.

Requires PyMuPDF and Pillow. Usage:
  python code/audit_pdf.py . --contact-dir /path/to/temporary/contact-sheets

The numerical checks complement, but do not replace, visual inspection.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re

import fitz
from PIL import Image, ImageDraw


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('chapter', type=Path)
    parser.add_argument('--contact-dir', type=Path)
    args = parser.parse_args()
    root = args.chapter.resolve()
    pdf = root / 'GY1965_test.pdf'
    doc = fitz.open(pdf)
    items = json.loads((root / 'GY1965_items.json').read_text())
    texts = [p.get_text() for p in doc]
    combined = '\n'.join(texts)
    missing = [i['id'] for i in items if i['id'] not in combined]
    outside = []
    for index, page in enumerate(doc, 1):
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines', []):
                for span in line['spans']:
                    x0, y0, x1, y1 = span['bbox']
                    if x0 < -0.5 or y0 < -0.5 or x1 > page.rect.width+0.5 or y1 > page.rect.height+0.5:
                        outside.append({'page': index, 'text': span['text'], 'bbox': span['bbox']})
    aux = (root / 'GY1965_test.aux').read_text()
    anchors = {}
    for match in re.finditer(r'\\newlabel\{item:([^}]+)\}\{\{[^}]*\}\{([^}]+)\}\{[^}]*\}\{([^}]+)\}', aux):
        anchors[match.group(1)] = {'page': match.group(2), 'destination': match.group(3)}
    anchor_missing = [i['id'] for i in items if i['id'] not in anchors]
    distinct = len({a['destination'] for a in anchors.values()})
    links = [link for page in doc for link in page.get_links()]
    internal = [link for link in links if link['kind'] in (fitz.LINK_GOTO, fitz.LINK_NAMED)]
    invalid_links = [link for link in internal if not 0 <= link.get('page', -1) < len(doc)]
    names = doc.resolve_names()
    unresolved_anchors = [a['destination'] for a in anchors.values() if a['destination'] not in names]
    result = {
        'pdf': pdf.name,
        'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'pages': len(doc),
        'page_size_points': list(doc[0].rect),
        'catalogue_items': len(items),
        'missing_item_ids_in_extracted_text': missing,
        'item_anchors': len(anchors),
        'distinct_item_destinations': distinct,
        'missing_item_anchors': anchor_missing,
        'unresolved_item_destinations': unresolved_anchors,
        'text_spans_outside_page': outside,
        'internal_links': len(internal),
        'invalid_internal_links': invalid_links,
        'bibliography_destinations': sum(k.startswith('cite.') for k in names),
        'pymupdf_version': fitz.VersionBind,
        'section_pages': {},
    }
    markers = ['Scope and editorial position', 'A bounded answer to the Weyl-field',
               'Problem index', 'Corrections', 'Bibliography']
    for marker in markers:
        result['section_pages'][marker] = [i+1 for i,t in enumerate(texts) if marker in t]
    result['overview_pages'] = next((i+1 for i,t in enumerate(texts) if 'record 53;' in t), None)
    result['passed'] = not (missing or anchor_missing or unresolved_anchors or outside or invalid_links) and distinct == len(items)
    out = root / 'evidence/pdf_audit.json'
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    if args.contact_dir:
        args.contact_dir.mkdir(parents=True, exist_ok=True)
        cols, rows, tile_w, tile_h = 4, 5, 260, 390
        for first in range(0, len(doc), cols*rows):
            sheet = Image.new('RGB', (cols*tile_w, rows*tile_h), '#dddddd')
            draw = ImageDraw.Draw(sheet)
            for offset in range(min(cols*rows, len(doc)-first)):
                p = doc[first+offset]
                pix = p.get_pixmap(matrix=fitz.Matrix(0.41,0.41), alpha=False)
                im = Image.frombytes('RGB', [pix.width,pix.height], pix.samples)
                x, y = offset%cols*tile_w, offset//cols*tile_h
                sheet.paste(im, (x+(tile_w-im.width)//2, y+24))
                draw.text((x+10,y+7),f'Page {first+offset+1}',fill='black')
            sheet.save(args.contact_dir/f'contact_{first+1:03}_{min(first+cols*rows,len(doc)):03}.png')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if not result['passed']:
        raise SystemExit('PDF audit requires review.')


if __name__ == '__main__':
    main()
