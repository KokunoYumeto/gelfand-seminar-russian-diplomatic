"""Reproduce reduced paired scans used in the last visual source audit.

These previews are temporary analysis aids, not separate deliverables.
Original supplied page images are never edited.
"""
from pathlib import Path
from PIL import Image,ImageDraw

root=Path(__file__).resolve().parents[1]
workspace=root.parents[1]
groups=[['001371','001372'],['001379','001381'],
        ['001383','001384'],['001365','001366']]
for group in groups:
    out=Image.new('RGB',(1800,1500),'white')
    draw=ImageDraw.Draw(out)
    for j,page in enumerate(group):
        im=Image.open(workspace/'work'/f'GELFAND-P{page}.png').convert('RGB')
        im.thumbnail((890,1450))
        out.paste(im,(j*900,35))
        draw.text((j*900+10,5),'P'+page,fill='black')
    out.save(root/'evidence'/('review_'+'_'.join(group)+'.png'))
    print('reviewed pair',','.join(group))
