#!/usr/bin/env python3
"""Audit every PDF page and render contact sheets for visual inspection."""
import argparse,json,re
from pathlib import Path
import fitz
from PIL import Image,ImageDraw,ImageFont

parser=argparse.ArgumentParser()
parser.add_argument('directory',nargs='?',type=Path,default=Path('.'))
parser.add_argument('--render',action='store_true')
args=parser.parse_args()
d=args.directory.resolve();doc=fitz.open(d/'GY1987_test.pdf')
q=d.parent/'qa';q.mkdir(exist_ok=True)
pages=[];critical=[];margin_flags=[]
alltext=[]
for number,page in enumerate(doc,1):
    text=page.get_text();alltext.append(text)
    blocks=page.get_text('dict')['blocks']
    bounds=[]
    for block in blocks:
        for line in block.get('lines',[]):
            for span in line['spans']:
                if not span['text'].strip():continue
                x0,y0,x1,y1=span['bbox']
                bounds.append([x0,y0,x1,y1])
                if x0 < -0.75 or y0 < -0.75 or x1 > page.rect.width+0.75 or y1 > page.rect.height+0.75:
                    critical.append({'page':number,'kind':'off_page_text','text':span['text'],'bbox':span['bbox']})
                if 75 < y0 < page.rect.height-65 and (x0 < 57 or x1 > page.rect.width-57):
                    margin_flags.append({'page':number,'text':span['text'],'bbox':span['bbox']})
    if len(text.strip())<25:critical.append({'page':number,'kind':'unexpected_nearly_empty_page'})
    pages.append({'page':number,'characters':len(text),'first_line':text.splitlines()[0] if text else '',
                  'min_x':min((b[0] for b in bounds),default=None),'max_x':max((b[2] for b in bounds),default=None)})
logpath=d/'GY1987_test.log'
log=logpath.read_text(errors='replace') if logpath.exists() else ''
overfull=[]
for m in re.finditer(r'Overfull \\([hv])box \(([-.0-9]+)pt too (?:wide|high)\)([^\n]*)',log):
    overfull.append({'box':m.group(1),'points':float(m.group(2)),'context':m.group(3).strip()})
for token in ['Undefined control sequence','Missing character:','There were undefined citations','There were undefined references','Citation `','Label(s) may have changed','Rerun to get']:
    if token in log:critical.append({'kind':'final_tex_log_warning','token':token})
if re.search(r'^!',log,re.M):critical.append({'kind':'final_tex_error'})
result={'status':'PASS' if not critical else 'FAIL','pages':len(doc),
        'characters':sum(p['characters'] for p in pages),'critical':critical,
        'overfull_boxes':overfull,'margin_flags':margin_flags,'page_details':pages,
        'visual_review':'Contact sheets and selected full-resolution pages require recorded human/model inspection.'}
(d/'logs'/'pdf_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(q/'GY1987_extracted.txt').write_text('\n\f\n'.join(alltext),encoding='utf-8')
if args.render:
    thumb_width=340;thumb_height=481;label=25;cols=4;rows=5
    try:font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',17)
    except OSError:font=ImageFont.load_default()
    for start in range(0,len(doc),cols*rows):
        canvas=Image.new('RGB',(cols*(thumb_width+15)+15,rows*(thumb_height+label+15)+15),'#e5e7eb')
        draw=ImageDraw.Draw(canvas)
        for offset in range(min(cols*rows,len(doc)-start)):
            p=doc[start+offset]
            pix=p.get_pixmap(matrix=fitz.Matrix(thumb_width/p.rect.width,thumb_width/p.rect.width),alpha=False)
            img=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
            x=15+(offset%cols)*(thumb_width+15);y=15+(offset//cols)*(thumb_height+label+15)
            canvas.paste(img,(x,y));draw.text((x+4,y+thumb_height+3),str(start+offset+1),fill='black',font=font)
        canvas.save(q/f'contact_{start+1:03}_{min(start+cols*rows,len(doc)):03}.png')
    key_pages={1,2,3,len(doc)}|{x['page'] for x in margin_flags}
    for number,text in enumerate(alltext,1):
        if any(marker in text for marker in ['Joint spectra of stochastic matrices:','A Poisson-pencil repair','The complete attainable range',
                                            'Homology spheres and twisted','The complete two- and three-state','An order-five obstruction']):
            key_pages.update(range(max(1,number-1),min(len(doc),number+3)+1))
    for number in sorted(key_pages):
        doc[number-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(q/f'page_{number:03}.png')
    result['rendered_contact_sheets']=[p.name for p in sorted(q.glob('contact_*.png'))]
    result['rendered_detail_pages']=sorted(key_pages)
    (d/'logs'/'pdf_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['page_details','margin_flags']},ensure_ascii=False,indent=2))
raise SystemExit(0 if not critical else 1)
