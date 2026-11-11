"""Validate the supplied PNG files without changing them; write an auditable report."""
from pathlib import Path
from PIL import Image
import hashlib, json

ROOT = Path(__file__).resolve().parents[2]
rows = []
for p in sorted((ROOT / 'scans').glob('*.png')):
    row = {'page':p.stem, 'bytes':p.stat().st_size,
           'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
    try:
        with Image.open(p) as im:
            row.update(width=im.width,height=im.height,mode=im.mode)
            im.verify()
        with Image.open(p) as im:
            im.load()
        row['status']='valid'
    except Exception as exc:
        row.update(status='invalid',error=f'{type(exc).__name__}: {exc}')
    rows.append(row)
out = ROOT / 'work/code/output'
out.mkdir(parents=True,exist_ok=True)
(out/'scan_integrity.json').write_text(json.dumps(rows,indent=2)+'\n')
print(f'Files: {len(rows)}; valid: {sum(r["status"]=="valid" for r in rows)}')
for row in rows:
    if row['status']!='valid': print(row)
