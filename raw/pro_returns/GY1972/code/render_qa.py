"""Render the compiled chapter and make numbered contact sheets for visual QA.

Usage: python render_qa.py CHAPTER_DIRECTORY QA_DIRECTORY
Uses system Poppler plus Pillow/PyMuPDF. The JSON gives structural checks;
contact sheets and selected full-size pages must also be inspected visually.
"""
from pathlib import Path
import json
import re
import shutil
import subprocess
import sys
import fitz
from PIL import Image, ImageOps, ImageDraw

chapter = Path(sys.argv[1]).resolve()
qa = Path(sys.argv[2]).resolve()
qa.mkdir(parents=True,exist_ok=True)
pages = qa/'pages'
pages.mkdir(exist_ok=True)
pdf = chapter/'GY1972_test.pdf'
poppler = '/usr/bin/pdftoppm' if Path('/usr/bin/pdftoppm').exists() else shutil.which('pdftoppm')
subprocess.run([poppler,'-r','60','-png',str(pdf),str(pages/'page')],check=True)
doc = fitz.open(pdf)
all_text = '\n'.join(page.get_text() for page in doc)
items = json.loads((chapter/'GY1972_items.json').read_text())
missing = sorted({item['id'] for item in items}-set(re.findall(r'1972-\d+\.\d+',all_text)))
assert not missing, missing
outside = []
for n,page in enumerate(doc,1):
    for word in page.get_text('words'):
        x0,y0,x1,y1,text,*_ = word
        if x0 < -0.5 or y0 < -0.5 or x1>page.rect.width+0.5 or y1>page.rect.height+0.5:
            outside.append(dict(page=n,word=text,box=[x0,y0,x1,y1]))
assert not outside, outside
rendered=sorted(pages.glob('page-*.png'),key=lambda p:int(p.stem.rsplit('-',1)[1]))
assert len(rendered)==len(doc)
contact_paths=[]
for offset in range(0,len(rendered),12):
    batch=rendered[offset:offset+12]
    sheet=Image.new('RGB',(1080,2148),'#e9e9e9')
    draw=ImageDraw.Draw(sheet)
    for j,file in enumerate(batch):
        image=Image.open(file).convert('RGB')
        image.thumbnail((342,496))
        x=(j%3)*360+9; y=(j//3)*537+25
        sheet.paste(image,(x,y))
        draw.text((x,y-18),f'Page {offset+j+1}',fill='black')
    dest=qa/f'contact_{offset+1:03d}_{offset+len(batch):03d}.png'
    sheet.save(dest)
    contact_paths.append(dest.name)
selected=[1,2,4,29,45,49,52,54,68,79,94,104,108,113,114,115,116,119,121,130,136,142]
for n in selected:
    if n<=len(doc):
        subprocess.run([poppler,'-f',str(n),'-singlefile','-r','115','-png',str(pdf),str(qa/f'detail_{n:03d}')],check=True)
summary=dict(pdf_pages=len(doc),all_item_ids_present=True,items_checked=len(items),
             no_text_boxes_outside_page=True,rendered_page_count=len(rendered),
             contact_sheets=contact_paths,detail_pages=selected,
             bookmarks=doc.get_toc(),manual_visual_review='pending')
(qa/'render_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:summary[k] for k in ['pdf_pages','all_item_ids_present','items_checked','no_text_boxes_outside_page','rendered_page_count','contact_sheets']},indent=2))
