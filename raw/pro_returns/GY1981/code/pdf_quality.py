"""Check final PDF structure and render every page with Poppler for visual QA."""
import json
from pathlib import Path
import re
import subprocess
import sys
import fitz
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
PDF=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'final/GY1981/GY1981_test.pdf'
OUT=Path(sys.argv[2]) if len(sys.argv)>2 else ROOT/'pdf_qa'
OUT.mkdir(parents=True,exist_ok=True)
doc=fitz.open(PDF)
texts=[p.get_text() for p in doc]
bad_bounds=[]
bad_links=[]
external=internal=0
for n,p in enumerate(doc,1):
    for w in p.get_text('words'):
        if w[0]<-0.5 or w[1]<-0.5 or w[2]>p.rect.width+0.5 or w[3]>p.rect.height+0.5:
            bad_bounds.append([n,list(w[:5])])
    for link in p.get_links():
        if link.get('kind') in {fitz.LINK_GOTO,fitz.LINK_NAMED}:
            internal+=1
            if not 0<=link.get('page',-1)<len(doc):bad_links.append([n,link])
        if link.get('kind')==fitz.LINK_URI:external+=1
items=json.loads(PDF.with_name('GY1981_items.json').read_text())
combined='\n'.join(texts)
missing=[i['id'] for i in items if i['id'] not in combined]
locators={}
for phrase in [
 'record 530;', '1981-536.7', '1981-540.1', '1981-546.15',
 '1981-550.3', 'Haefliger’s modular-group coinvariant equation',
 'An explicit six-plane refutes', 'A Fourier-family obstruction',
 'An explicit first-order differential operator',
 'GP-1981-40: Uniform', 'Corrections to the transcription', 'Bibliography']:
    locators[phrase]=[n+1 for n,t in enumerate(texts) if phrase in t]
quality={
 'pdf_pages':len(doc),'page_size_points':[doc[0].rect.width,doc[0].rect.height],
 'all_pages_have_text':all(t.strip() for t in texts),
 'all_item_ids_present':not missing,'missing_item_ids':missing,
 'text_outside_page':bad_bounds,'broken_internal_links':bad_links,
 'internal_link_count':internal,'external_link_count':external,
 'overview_ends_on_page':locators['record 530;'][0],
 'locator_pages':locators,
 'visual_review':'pending; contact sheets cover every page',
}
(OUT/'structure.json').write_text(json.dumps(quality,indent=2)+'\n')
(OUT/'full_text.txt').write_text(combined)
if '--structure-only' in sys.argv:
    print(json.dumps(quality,indent=2));sys.exit(0)
thumbs=OUT/'pages';thumbs.mkdir(exist_ok=True)
subprocess.run(['pdftoppm','-r','42','-png',str(PDF),str(thumbs/'page')],check=True,capture_output=True)
images=sorted(thumbs.glob('page-*.png'))
assert len(images)==len(doc)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',16)
cols,rows=5,5
for start in range(0,len(images),cols*rows):
    cellw,cellh=260,390
    sheet=Image.new('RGB',(cols*cellw,rows*cellh),(218,221,225))
    draw=ImageDraw.Draw(sheet)
    for k,path in enumerate(images[start:start+cols*rows]):
        im=Image.open(path).convert('RGB');im.thumbnail((244,356))
        x=(k%cols)*cellw+(cellw-im.width)//2;y=(k//cols)*cellh+26
        sheet.paste(im,(x,y));draw.text(((k%cols)*cellw+10,(k//cols)*cellh+5),str(start+k+1),font=font,fill=(0,0,0))
    sheet.save(OUT/f'contact_{start+1:03d}_{min(start+25,len(images)):03d}.png')
selected={1,2,len(doc)}
for nums in locators.values():
    if nums:selected.add(nums[0])
for n in sorted(selected):
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-r','115','-singlefile','-png',str(PDF),str(OUT/f'selected_{n:03d}')],check=True,capture_output=True)
print(json.dumps(quality,indent=2))
