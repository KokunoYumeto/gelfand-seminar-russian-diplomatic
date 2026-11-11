from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request,subprocess,fitz
base=Path(__file__).parent
lang=base/'tessdata';lang.mkdir(exist_ok=True)
p=lang/'rus.traineddata'
if not p.exists():p.write_bytes(urllib.request.urlopen('https://raw.githubusercontent.com/tesseract-ocr/tessdata_fast/main/rus.traineddata').read())
doc=fitz.open(base/'ushveridze1989.pdf')
imgs=base/'qes_ocr';imgs.mkdir(exist_ok=True)
for i,page in enumerate(doc):
 p=imgs/f'p{i+1:02}.png'
 if not p.exists():page.get_pixmap(matrix=fitz.Matrix(1.8,1.8)).save(p)
def run(p):
 r=subprocess.run(['tesseract',str(p),'stdout','-l','rus','--tessdata-dir',str(lang)],capture_output=True,text=True)
 return p.stem,r.stdout
with ThreadPoolExecutor(max_workers=6) as pool:
 rs=list(pool.map(run,sorted(imgs.glob('*.png'))))
(base/'ushveridze1989_ocr.txt').write_text('\n'.join('\nPAGE '+n+'\n'+t for n,t in rs))
print('OCR completed',len(rs),'pages')
