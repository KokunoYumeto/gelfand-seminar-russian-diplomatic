#!/usr/bin/env python3
"""Render every PDF page as a contact sheet and selected pages in detail.

Requires Poppler (pdftoppm), Pillow and PyMuPDF. The images are intermediate
review artifacts; the final review record records what was actually inspected.
"""
from pathlib import Path
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import math
import subprocess
from PIL import Image,ImageOps,ImageDraw
import fitz

ITEMS=['1982-561.6','1982-562.1','1982-565.6','1982-573.3',
       '1982-573.6','1982-573.14','1982-574.3','1982-577.6',
       '1982-581.8','1982-583.8','1982-585.15','1982-586.4',
       '1982-590.3','1982-592.8','1982-595.5']


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf',type=Path)
    parser.add_argument('directory',type=Path)
    parser.add_argument('--index',type=Path)
    args=parser.parse_args()
    pdf=args.pdf.resolve(); out=args.directory.resolve()
    thumbs=out/'thumbnails'; details=out/'details'; contacts=out/'contacts'
    for folder in [thumbs,details,contacts]:folder.mkdir(parents=True,exist_ok=True)
    doc=fitz.open(pdf)
    selected={1,2,len(doc)}
    located={}
    section_pages={}
    for number,page in enumerate(doc,1):
        text=page.get_text()
        for item in ITEMS:
            if item not in located and item in text:
                located[item]=number;selected.add(number)
        for section in ['Developments','Problem index','Corrections to the transcription','Bibliography']:
            if section not in section_pages and section in text:
                section_pages[section]=number
    for start,end in [(section_pages['Developments'],section_pages['Problem index']),
                      (section_pages['Corrections to the transcription'],section_pages['Bibliography'])]:
        if end-start<7:selected.update(range(start,end+1))
        else:selected.update([start,start+1,(start+end)//2,end-1])
    selected.add(section_pages['Bibliography'])
    completed=subprocess.run(['pdftoppm','-r','60','-png',str(pdf),str(thumbs/'page')],
                             stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    if completed.returncode:raise SystemExit(completed.stdout)
    images=sorted(thumbs.glob('page-*.png'))
    if len(images)!=len(doc):raise RuntimeError('Thumbnail page count mismatch')
    contact_files=[]
    width,height,cols,rows=250,375,5,4
    for offset in range(0,len(images),cols*rows):
        batch=images[offset:offset+cols*rows]
        canvas=Image.new('RGB',(cols*width,rows*height),(235,237,239))
        draw=ImageDraw.Draw(canvas)
        for index,path in enumerate(batch):
            thumb=Image.open(path).convert('RGB')
            thumb.thumbnail((width-12,height-28))
            x=(index%cols)*width+(width-thumb.width)//2
            y=(index//cols)*height+22
            canvas.paste(thumb,(x,y))
            draw.text(((index%cols)*width+9,(index//cols)*height+5),f'Page {offset+index+1}',fill=(20,25,30))
        name=f'contact_{offset//(cols*rows)+1:02d}.png'
        canvas.save(contacts/name)
        contact_files.append({'file':str(contacts/name),'pages':[offset+1,offset+len(batch)]})
    def detail(number):
        path=details/f'page_{number:03d}'
        run=subprocess.run(['pdftoppm','-f',str(number),'-l',str(number),'-r','120',
                            '-singlefile','-png',str(pdf),str(path)],
                           stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        if run.returncode:raise RuntimeError(run.stdout)
        return {'page':number,'file':str(path.with_suffix('.png'))}
    with ThreadPoolExecutor(max_workers=3) as pool:
        detail_files=list(pool.map(detail,sorted(selected)))
    result={'pdf':str(pdf),'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
            'pages':len(doc),'renderer':'Poppler pdftoppm',
            'thumbnail_dpi':60,'detail_dpi':120,
            'section_pages':section_pages,'item_pages':located,
            'contact_sheets':contact_files,'detail_pages':detail_files}
    target=args.index or out/'render_index.json'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'pages':len(doc),'contacts':len(contact_files),
                      'detail_pages':sorted(selected),'index':str(target)},indent=2))


if __name__=='__main__':main()
