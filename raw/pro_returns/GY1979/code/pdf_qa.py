#!/usr/bin/env python3
"""Render every final PDF page, make contact sheets and inspect text bounds.

Generated full-page PNGs are temporary (.texruntime/pdf_qa); the contact sheets
and machine-readable results are included in the deliverable. Human findings
are recorded separately in code/visual_qa.md, not inferred from this script.
"""
from pathlib import Path
import hashlib, json, re
import fitz
from PIL import Image, ImageDraw, ImageFont

D=Path(__file__).resolve().parent.parent
pdf=D/'GY1979_test.pdf'
doc=fitz.open(pdf)
tmp=D/'.texruntime/pdf_qa';tmp.mkdir(parents=True,exist_ok=True)
contacts=D/'code/qa_contact_sheets';contacts.mkdir(parents=True,exist_ok=True)
try:
    font=ImageFont.truetype('DejaVuSans.ttf',14)
except OSError:
    font=ImageFont.load_default()
thumbs=[];outside=[];page_text={}
for i,page in enumerate(doc):
    pix=page.get_pixmap(matrix=fitz.Matrix(1,1),alpha=False)
    im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
    im.save(tmp/f'page_{i+1:03d}.png')
    thumb=im.copy();thumb.thumbnail((240,340))
    tile=Image.new('RGB',(256,372),'#dedede')
    tile.paste(thumb,((256-thumb.width)//2,24))
    ImageDraw.Draw(tile).text((8,4),f'Page {i+1}',font=font,fill='black')
    thumbs.append(tile)
    page_text[i+1]=page.get_text()
    for b in page.get_text('dict')['blocks']:
        for line in b.get('lines',[]):
            for span in line.get('spans',[]):
                if not span['text'].strip():continue
                x0,y0,x1,y1=span['bbox']
                if x0<-.5 or y0<-.5 or x1>page.rect.width+.5 or y1>page.rect.height+.5:
                    outside.append({'page':i+1,'text':span['text'],'bbox':span['bbox']})
sheets=[]
for first in range(0,len(thumbs),24):
    sheet=Image.new('RGB',(6*256,4*372),'#c4c4c4')
    for j,im in enumerate(thumbs[first:first+24]):sheet.paste(im,((j%6)*256,(j//6)*372))
    name=f'pages_{first+1:03d}_{min(first+24,len(thumbs)):03d}.jpg'
    sheet.save(contacts/name,quality=90)
    sheets.append(str((contacts/name).relative_to(D)))
sections={}
for label,pattern in [('first_record',r'record\s+462;'),('developments',r'Developments'),
                       ('corrections',r'Corrections'),('bibliography',r'Bibliography')]:
    hits=[i for i,t in page_text.items() if re.search(pattern,t)]
    sections[label]=hits[0] if hits else None
log=(D/'GY1979_test.log').read_text(errors='replace')
flags=[l for l in log.splitlines() if any(x in l for x in ('Overfull','Underfull','undefined','Missing character','LaTeX Error','Warning:'))]
result={'pdf':pdf.name,'bytes':pdf.stat().st_size,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'pages':len(doc),'page_size_points':list(doc[0].rect),'all_pages_rendered':True,
        'contact_sheets':sheets,'text_spans_outside_page':outside,'section_start_pages':sections,
        'log_flags':flags,
        'scope':'Text bounds and render success are automatic checks; human layout inspection is recorded in visual_qa.md.'}
(D/'code/pdf_qa_output.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
