from pathlib import Path
from PIL import Image,ImageChops
out=Path('work/late_scan_crops');out.mkdir(exist_ok=True)
for p in range(685,707):
 im=Image.open(f'scans/GELFAND-P{p:06}.png').convert('RGB')
 bw=im.convert('L').point(lambda x:255 if x<180 else 0)
 box=bw.getbbox()
 if box: im=im.crop(box)
 im.thumbnail((1600,2400))
 im.save(out/f'P{p:06}.png')
print('22 examination crops prepared from unchanged originals.')
