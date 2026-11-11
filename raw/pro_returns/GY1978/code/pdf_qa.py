"""Inspect the compiled PDF and render review sheets (PyMuPDF and Pillow).

Usage: python code/pdf_qa.py [preview-directory]
The preview directory is an inspection intermediate, not a source dependency.
"""
from pathlib import Path
import json,sys,re
import fitz
from PIL import Image,ImageDraw

ROOT=Path(__file__).resolve().parents[1]
OUT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT/'code'/'qa_previews'
OUT.mkdir(parents=True,exist_ok=True)
doc=fitz.open(ROOT/'GY1978_test.pdf')
metrics={'pages':len(doc),'page_sizes':sorted(set((round(p.rect.width,2),round(p.rect.height,2)) for p in doc)),
         'blank_pages':[],'outside_page_spans':[],'body_margin_outliers':[],
         'section_locations':{title:page for level,title,page in doc.get_toc()},'review_sheets':[]}
texts=[]
for i,p in enumerate(doc):
    txt=p.get_text();texts.append(txt)
    if len(txt.strip())<15:metrics['blank_pages'].append(i+1)
    for b in p.get_text('dict')['blocks']:
        for line in b.get('lines',[]):
            for span in line['spans']:
                x0,y0,x1,y1=span['bbox']
                if x0<-1 or y0<-1 or x1>p.rect.width+1 or y1>p.rect.height+1:
                    metrics['outside_page_spans'].append({'page':i+1,'bbox':span['bbox'],'text':span['text']})
                if y0>60 and y1<p.rect.height-60 and (x0<60 or x1>p.rect.width-60):
                    metrics['body_margin_outliers'].append({'page':i+1,'bbox':span['bbox'],'text':span['text']})
alltext='\n'.join(texts)
metrics['text_characters']=len(alltext)
metrics['replacement_character_count']=alltext.count('\ufffd')
metrics['item_headers_found']=len(set(re.findall(r'1978-\d+\.\d+',alltext)))
for start in range(0,len(doc),20):
    thumbw,thumbh=300,425
    canvas=Image.new('RGB',(4*thumbw,5*(thumbh+28)), '#e1e5e9')
    draw=ImageDraw.Draw(canvas)
    for idx in range(start,min(start+20,len(doc))):
        pix=doc[idx].get_pixmap(matrix=fitz.Matrix(.5,.5),alpha=False)
        im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
        im.thumbnail((thumbw-12,thumbh-12))
        cell=idx-start;cx=(cell%4)*thumbw;cy=(cell//4)*(thumbh+28)
        canvas.paste(im,(cx+(thumbw-im.width)//2,cy+24))
        draw.text((cx+10,cy+5),f'Page {idx+1}',fill='#101828')
    name=f'pages_{start+1:03d}_{min(start+20,len(doc)):03d}.jpg'
    canvas.save(OUT/name,quality=85)
    metrics['review_sheets'].append(name)
(ROOT/'code/pdf_qa.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n')
(OUT/'extracted_text.txt').write_text(alltext)
print(json.dumps({k:v for k,v in metrics.items() if k not in ['body_margin_outliers']},ensure_ascii=False,indent=2))
print('Body-margin outliers:',len(metrics['body_margin_outliers']))
