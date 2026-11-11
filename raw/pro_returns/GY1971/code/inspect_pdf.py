#!/usr/bin/env python3
"""Extract layout diagnostics and render contact sheets of every PDF page.

Requires PyMuPDF and Pillow. Raster files are review intermediates, not source
data. This tool detects geometry risks; a human/visual review is still required.
"""
import argparse
import json
import math
import pathlib
import re

import fitz
from PIL import Image, ImageDraw


def main():
    root=pathlib.Path(__file__).resolve().parents[1]
    p=argparse.ArgumentParser()
    p.add_argument('--output',type=pathlib.Path,default=root.parent/'pdf_review')
    p.add_argument('--detail-pages',default='1,2,3')
    args=p.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    doc=fitz.open(root/'GY1971_test.pdf')
    pages=[]; spans_outside=[]; suspected_overhang=[]; headings=[]
    texts=[]
    for i,page in enumerate(doc):
        text=page.get_text()
        texts.append(text)
        spans=[s for b in page.get_text('dict')['blocks'] if b.get('type')==0
               for line in b['lines'] for s in line['spans']]
        for s in spans:
            x0,y0,x1,y1=s['bbox']
            row={'page':i+1,'bbox':[round(v,2) for v in s['bbox']],'text':s['text']}
            if x0<0 or y0<0 or x1>page.rect.width+.5 or y1>page.rect.height+.5:
                spans_outside.append(row)
            if 60<y0<780 and (x0<60 or x1>535):
                suspected_overhang.append(row)
        pages.append({'page':i+1,'width':round(page.rect.width,2),
                      'height':round(page.rect.height,2),'characters':len(text),
                      'links':len(page.get_links()),'text_spans':len(spans)})
        for needle in ('Developments','Problem index','Corrections to the transcription',
                       'Bibliography','The grading check','An exact finite audit',
                       'Recovering the eighty-million'):
            if needle in text:
                headings.append({'text':needle,'page':i+1})
    overview_end=next(i+1 for i,t in enumerate(texts) if 'record 229;' in t)
    log=(root/'GY1971_test.log').read_text(errors='replace')
    warnings=[line for line in log.splitlines()
              if any(x in line for x in ('Warning:','Overfull','Underfull','Missing character:','! '))]
    audit={'pages':len(doc),'page_details':pages,'outside_physical_page':spans_outside,
           'potential_body_margin_overhang':suspected_overhang,
           'section_occurrences':headings,'first_talk_page':overview_end,
           'overview_pages':overview_end-1,'replacement_characters':sum(t.count('\ufffd') for t in texts),
           'final_log_warning_lines':warnings,'visual_review_required':True}
    (root/'audit'/'pdf_layout.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    (args.output/'extracted_text.txt').write_text('\n\n'.join(f'=== PAGE {i+1} ===\n{t}' for i,t in enumerate(texts)))
    cell_w,cell_h=320,475
    for sheet in range(math.ceil(len(doc)/16)):
        canvas=Image.new('RGB',(cell_w*4,cell_h*4),'#d8d8d8')
        draw=ImageDraw.Draw(canvas)
        for k in range(16):
            n=sheet*16+k
            if n>=len(doc):break
            page=doc[n]
            pix=page.get_pixmap(matrix=fitz.Matrix(304/page.rect.width,304/page.rect.width),alpha=False)
            im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
            x=(k%4)*cell_w+8;y=(k//4)*cell_h+24
            canvas.paste(im,(x,y))
            draw.text((x,y-19),f'PDF page {n+1}',fill='black')
        canvas.save(args.output/f'contact_{sheet+1:02d}.png')
    for number in [int(n) for n in args.detail_pages.split(',') if n.strip()]:
        if 1<=number<=len(doc):
            doc[number-1].get_pixmap(matrix=fitz.Matrix(1.4,1.4),alpha=False).save(args.output/f'page_{number:03d}.png')
    print(json.dumps({'pages':len(doc),'overview_pages':overview_end-1,
                      'physical_page_overruns':len(spans_outside),
                      'potential_margin_overhangs':len(suspected_overhang),
                      'headings':headings,'warnings':warnings},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
