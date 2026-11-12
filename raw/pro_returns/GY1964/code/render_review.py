"""Render every chapter page and make labelled contact sheets for visual QA.

Usage: python code/render_review.py [PDF] [output-directory]
Full page PNGs are temporary review material. The contact sheets and JSON
inventory are retained with the deliverable, alongside a human review note.
"""
from pathlib import Path
import json
import hashlib
import math
import subprocess
import sys

import fitz
from PIL import Image, ImageDraw, ImageFont


def main():
    pdf=Path(sys.argv[1] if len(sys.argv)>1 else 'GY1964_test.pdf').resolve()
    out=Path(sys.argv[2] if len(sys.argv)>2 else 'evidence/visual').resolve()
    pages=out/'pages'
    pages.mkdir(parents=True,exist_ok=True)
    previous={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
              for p in pages.glob('page-*.png')}
    document=fitz.open(pdf)
    inventory=[]
    for i,page in enumerate(document):
        words=page.get_text('words')
        # Margin comparison includes running heads and page numbers. Small
        # glyph bearings are tolerated; full-page overflow is always flagged.
        outside=[list(w[:5]) for w in words if
                 w[0] < -0.5 or w[1] < -0.5 or
                 w[2] > page.rect.width+0.5 or w[3] > page.rect.height+0.5]
        body_margin=[list(w[:5]) for w in words if 58 < w[1] < page.rect.height-58
                     and (w[0] < 58 or w[2] > page.rect.width-58)]
        text=page.get_text()
        inventory.append({'page':i+1,'width':page.rect.width,'height':page.rect.height,
                          'words':len(words),'outside_page':outside,
                          'body_margin_flags':body_margin,
                          'text_start':text[:160],'text_end':text[-160:]})
    command=['pdftoppm','-r','90','-png',str(pdf),str(pages/'page')]
    for old in pages.glob('page-*.png'):old.unlink()
    p=subprocess.run(command,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (out/'render_output.txt').write_text(p.stdout)
    if p.returncode:raise RuntimeError(p.stdout)
    files=sorted(pages.glob('page-*.png'))
    if len(files)!=len(document):
        raise RuntimeError(f'Rendered {len(files)} pages, expected {len(document)}')
    font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',16)
    width,height=330,467
    cols,rows=4,4
    per_sheet=cols*rows
    sheets=[]
    for offset in range(0,len(files),per_sheet):
        selection=files[offset:offset+per_sheet]
        canvas=Image.new('RGB',(cols*(width+14)+14,rows*(height+36)+14),'#e9e9e9')
        draw=ImageDraw.Draw(canvas)
        for k,path in enumerate(selection):
            im=Image.open(path).convert('RGB')
            im.thumbnail((width,height),Image.Resampling.LANCZOS)
            x=14+(k%cols)*(width+14)+(width-im.width)//2
            y=14+(k//cols)*(height+36)
            canvas.paste(im,(x,y))
            draw.rectangle((x-1,y-1,x+im.width,y+im.height),outline='#9c9c9c')
            draw.text((x,y+height+5),f'Page {offset+k+1}',font=font,fill='#222222')
        name=f'contact_{offset+1:03d}_{offset+len(selection):03d}.jpg'
        canvas.save(out/name,quality=88)
        sheets.append(name)
    delta={'previous_render_available':bool(previous),
           'changed_pages':[i+1 for i,p in enumerate(files)
                            if previous.get(p.name)!=hashlib.sha256(p.read_bytes()).hexdigest()],
           'unchanged_pages':[i+1 for i,p in enumerate(files)
                              if previous.get(p.name)==hashlib.sha256(p.read_bytes()).hexdigest()]}
    (out/'render_delta.json').write_text(json.dumps(delta,indent=2)+'\n')
    result={'pdf':pdf.name,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
            'pages':len(document),'render_dpi':90,
            'contact_sheets':sheets,'inventory':inventory,
            'pages_with_full_page_overflow':[p['page'] for p in inventory if p['outside_page']],
            'pages_with_body_margin_flags':[p['page'] for p in inventory if p['body_margin_flags']]}
    (out/'page_inventory.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='inventory'},indent=2))
    print('Changed pages since previous render:',delta['changed_pages'])


if __name__=='__main__':main()
