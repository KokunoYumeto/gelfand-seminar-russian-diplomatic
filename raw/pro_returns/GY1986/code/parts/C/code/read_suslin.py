"""Download the opened original Suslin paper and OCR the inspected pages.

The download is source evidence, not a redistribution deliverable. The introduction
and theorem page establish chronology and exact hypotheses. Intermediate pages
record the exploratory search for Theorem 5.2.
"""
from pathlib import Path
import subprocess
from urllib.request import urlopen

base=Path(__file__).resolve().parents[1]/'evidence'
url='https://www.maths.dur.ac.uk/users/herbert.gangl/Suslin_K3_Bloch_group.pdf'
pdf=base/'suslin1991_source.pdf'
with urlopen(url,timeout=45) as r:
    data=r.read()
pdf.write_bytes(data)
print('Opened',url,'bytes',len(data))
for page,name in [(1,'suslin_intro'),(16,'suslin_theorem'),
                  (18,'suslin_late-18'),(19,'suslin_late-19'),(21,'suslin_main')]:
    stem=base/name
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r','130',
                    '-png','-singlefile',str(pdf),str(stem)],check=True)
    subprocess.run(['tesseract',str(stem)+'.png',str(stem)],check=True)
    print('PDF page',page,'\n',stem.with_suffix('.txt').read_text())
