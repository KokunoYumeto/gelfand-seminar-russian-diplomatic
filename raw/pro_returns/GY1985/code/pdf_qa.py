"""Inspect final PDF geometry and render pages for visual review.

Run: python code/pdf_qa.py [chapter_directory]
Requires PyMuPDF and Pillow. This does not validate mathematical content.
"""
import hashlib,json,math,sys
from pathlib import Path
import fitz
from PIL import Image,ImageDraw

base=Path(__file__).resolve().parent.parent
D=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else base
pdf=D/'GY1985_test.pdf'
out=D/'audit/pdf_qa';out.mkdir(parents=True,exist_ok=True)
doc=fitz.open(pdf)
checks=[];problems=[]
for index,page in enumerate(doc,1):
    spans=[s for b in page.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans'] if s['text'].strip()]
    outside=[s['text'] for s in spans if s['bbox'][0]<-0.5 or s['bbox'][1]<-0.5 or s['bbox'][2]>page.rect.width+0.5 or s['bbox'][3]>page.rect.height+0.5]
    checks.append({'page':index,'text_characters':len(page.get_text()),'text_spans':len(spans),'outside_page':outside})
    if outside or not spans:problems.append(index)

selected=[1,2,3,36,68,102,117,118,120,121,122,123,129,153,156,158,164]
selected=[n for n in selected if n<=len(doc)]
for number in selected:
    doc[number-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(out/f'page_{number:03d}.png')

thumb_width=205;cell_w=217;cell_h=310;columns=6;rows=7;per_sheet=columns*rows
sheets=[]
for start in range(0,len(doc),per_sheet):
    count=min(per_sheet,len(doc)-start)
    sheet=Image.new('RGB',(columns*cell_w,math.ceil(count/columns)*cell_h),'#e6e6e6')
    draw=ImageDraw.Draw(sheet)
    for j in range(count):
        page=doc[start+j]
        pix=page.get_pixmap(matrix=fitz.Matrix(thumb_width/page.rect.width,thumb_width/page.rect.width),alpha=False)
        im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
        x=(j%columns)*cell_w+6;y=(j//columns)*cell_h+4
        sheet.paste(im,(x,y));draw.text((x+3,y+im.height+3),str(start+j+1),fill='black')
    name=f'contact_{start+1:03d}_{start+count:03d}.png'
    sheet.save(out/name,optimize=True);sheets.append(name)

result={'status':'PASS' if not problems else 'REVIEW','pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':len(doc),'empty_or_outside_page_text':problems,'selected_rendered_pages':selected,'contact_sheets':sheets,'scope':'Automated page-boundary check plus render production; human visual review recorded separately. Text extraction control codes from mathematical fonts are not treated as missing glyphs; the XeLaTeX log independently checks missing characters.','page_checks':checks}
(out/'pdf_qa_output.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='page_checks'},indent=2))
