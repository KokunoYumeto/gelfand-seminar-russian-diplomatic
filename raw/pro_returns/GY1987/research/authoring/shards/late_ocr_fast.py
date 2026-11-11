from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,os
b=Path(__file__).parent
p=b/'qes_ocr'
def run(im):
 out=im.with_suffix('.txt')
 if not out.exists():
  r=subprocess.run(['tesseract',str(im),'stdout','-l','rus','--tessdata-dir',str(b/'tessdata')],capture_output=True,text=True,env={**os.environ,'OMP_THREAD_LIMIT':'1'},timeout=90)
  out.write_text(r.stdout)
 return out
with ThreadPoolExecutor(max_workers=4) as pool:
 for x in pool.map(run,sorted(p.glob('*.png'))): print(x.stem,flush=True)
(b/'ushveridze1989_ocr.txt').write_text('\n'.join('\nPAGE '+x.stem+'\n'+x.read_text() for x in sorted(p.glob('*.txt'))))
