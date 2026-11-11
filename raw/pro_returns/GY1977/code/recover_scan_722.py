"""Recover the one truncated attachment from its identified MCCME record.

The original upload is never modified. Matching complete neighbouring images
establishes the page mapping, and a prefix comparison tests the damaged file.
"""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urljoin
from PIL import Image
import hashlib,io,json,re

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'work/code/output';OUT.mkdir(parents=True,exist_ok=True)
TARGET=ROOT/'work/recovered_scans';TARGET.mkdir(exist_ok=True)
url='https://old.mccme.ru/gelfand/notes/record-429.html'
with urlopen(url,timeout=30) as response:
    html=response.read().decode('utf-8')
urls=[urljoin(url,u) for u in re.findall(r'<img src="([^"]+)"',html)]
assert len(urls)==8
rows=[]
for page,index in [(721,2),(722,3),(723,4)]:
    source=urls[index]
    with urlopen(source,timeout=30) as response:data=response.read()
    with Image.open(io.BytesIO(data)) as im:
        im.verify()
    with Image.open(io.BytesIO(data)) as im:
        im.load();size=im.size
    original=(ROOT/'scans'/f'GELFAND-P{page:06d}.png').read_bytes()
    rows.append({'page':page,'url':source,'bytes':len(data),'size':size,
                 'sha256':hashlib.sha256(data).hexdigest(),
                 'identical_to_attachment':data==original,
                 'attachment_is_prefix':data.startswith(original)})
    if page==722:
        (TARGET/f'GELFAND-P{page:06d}.png').write_bytes(data)
assert rows[0]['identical_to_attachment'] and rows[2]['identical_to_attachment']
assert rows[1]['attachment_is_prefix']
result={'record_url':url,'result':'Recovered complete original without altering attachment','files':rows}
(OUT/'scan_722_recovery.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
