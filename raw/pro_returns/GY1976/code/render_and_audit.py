"""Render the built chapter with Poppler and preserve compact visual-QA sheets.

Visual inspection remains an editorial task; no image heuristic is
presented as proof that the typography is correct.
"""
from pathlib import Path
import argparse
import json
import re
import subprocess
import fitz
from PIL import Image, ImageDraw

def main():
    ap=argparse.ArgumentParser();ap.add_argument('directory',nargs='?',default='.')
    ap.add_argument('--render-dir',default=None);a=ap.parse_args();d=Path(a.directory).resolve()
    visual=d/'code/output/visual';visual.mkdir(parents=True,exist_ok=True)
    temp=Path(a.render_dir).resolve() if a.render_dir else d/'code/output/page_renders'
    temp.mkdir(parents=True,exist_ok=True)
    pdf=d/'GY1976_test.pdf';log=(d/'GY1976_test.log').read_text(errors='replace')
    document=fitz.open(pdf)
    page_text=[p.get_text() for p in document]
    (d/'code/output/GY1976_pdf_text.txt').write_text('\n\n'.join(
        f'===== PDF PAGE {i+1} =====\n'+s for i,s in enumerate(page_text)))
    overfull=re.findall(r'Overfull \\[hv]box.*?(?=\n\n|\Z)',log,re.S)
    warnings=[s for s in log.splitlines() if 'Warning:' in s or s.startswith('Missing character:')]
    result={'pages':len(document),'latex_error_count':len(re.findall(r'^!',log,re.M)),
        'undefined_citation_or_reference_count':len(re.findall(r'undefined',log,re.I)),
        'missing_character_count':len(re.findall(r'Missing character:',log)),
        'overfull_box_count':len(overfull),'overfull_boxes':overfull,'warnings':warnings,
        'first_record_pdf_page':next((i+1 for i,s in enumerate(page_text) if 'record 397;' in s),None),
        'empty_text_pages':[i+1 for i,s in enumerate(page_text) if len(s.strip())<10],
        'visual_review':'pending editorial inspection'}
    (d/'code/output/pdf_audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    subprocess.run(['pdftoppm','-r','65','-png',str(pdf),str(temp/'page')],check=True,
                   stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    paths=sorted(temp.glob('page-*.png'),key=lambda p:int(p.stem.split('-')[-1]))
    if len(paths)!=len(document):raise ValueError('Incomplete Poppler rendering')
    thumb_w=260;thumb_h=390;cols=4;rows=5;per=cols*rows
    for start in range(0,len(paths),per):
        subset=paths[start:start+per];sheet=Image.new('RGB',(cols*thumb_w,rows*thumb_h),'#e7e7e7')
        draw=ImageDraw.Draw(sheet)
        for j,path in enumerate(subset):
            im=Image.open(path).convert('RGB');im.thumbnail((thumb_w-16,thumb_h-32))
            x=(j%cols)*thumb_w+(thumb_w-im.width)//2;y=(j//cols)*thumb_h+25
            sheet.paste(im,(x,y));draw.text(((j%cols)*thumb_w+9,(j//cols)*thumb_h+6),f'PDF page {start+j+1}',fill='black')
        sheet.save(visual/f'contact_{start+1:03d}_{start+len(subset):03d}.jpg',quality=88)
    print(json.dumps({k:v for k,v in result.items() if k not in ['overfull_boxes','warnings']},indent=2))

if __name__=='__main__':main()
