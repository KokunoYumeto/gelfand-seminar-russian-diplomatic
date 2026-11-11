"""Render every page and make labeled contact sheets for visual PDF review."""
from pathlib import Path
import hashlib,json,math,subprocess,sys
from PIL import Image,ImageDraw,ImageFont
from pypdf import PdfReader

D=Path(sys.argv[1]).resolve();PDF=D/'GY1977_test.pdf'
PAGES=D.parent/'pdf_review_pages';PAGES.mkdir(exist_ok=True)
OUT=D/'code/output/qa';OUT.mkdir(parents=True,exist_ok=True)
reader=PdfReader(PDF);texts=[p.extract_text() or '' for p in reader.pages]
subprocess.run(['pdftoppm','-r','78','-png',str(PDF),str(PAGES/'page')],check=True)
files=sorted(PAGES.glob('page-*.png'))
assert len(files)==len(reader.pages)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',14)
cols=5;rows=5;tw=205;th=290;gap=12;label=23
sheets=[]
for base in range(0,len(files),cols*rows):
    sheet=Image.new('RGB',(cols*(tw+gap)+gap,rows*(th+label+gap)+gap),'#eeeeee')
    draw=ImageDraw.Draw(sheet)
    for j,p in enumerate(files[base:base+cols*rows]):
        with Image.open(p) as im:
            im=im.convert('RGB');im.thumbnail((tw,th))
            x=gap+(j%cols)*(tw+gap);y=gap+(j//cols)*(th+label+gap)
            sheet.paste(im,(x,y));draw.rectangle((x-1,y-1,x+im.width,y+im.height),outline='#bcbcbc')
            draw.text((x,y+th+2),f'Page {base+j+1}',fill='black',font=font)
    dest=OUT/f'contact_{base+1:03d}_{min(base+cols*rows,len(files)):03d}.png'
    sheet.save(dest);sheets.append(str(dest))

markers=['1977-419.1','1977-429.8','1977-435.16','1977-440.5','1977-444.10','1977-457.25',
         'Integral information in the formal','literal KP normalization','thirteen-coin convention',
         'Independent checks of the spectral','Problem index','Corrections to the transcription','Bibliography']
locations={m:[n+1 for n,t in enumerate(texts) if m in t] for m in markers}
result={'pdf_pages':len(reader.pages),'pdf_sha256':hashlib.sha256(PDF.read_bytes()).hexdigest(),
        'page_text_lengths':[len(t) for t in texts],'nearly_empty_pages':[i+1 for i,t in enumerate(texts) if len(t.strip())<40],
        'markers':locations,'contact_sheets':sheets,'full_page_render_directory':str(PAGES),
        'visual_review':'pending; contact sheets and selected full pages must be inspected by a reviewer'}
(OUT/'render_manifest.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
