"""Render every PDF page and make numbered contact sheets for visual review.

Requires Poppler and Pillow. Images are review intermediates, not deliverables.
"""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--directory', type=Path, default=ROOT/'.build-cache'/'review')
parser.add_argument('--reuse', action='store_true', help='Verify existing rendered pages; repair incomplete PNGs.')
args = parser.parse_args()
destination = args.directory.resolve()
pages = destination/'pages'
contacts = destination/'contacts'
pages.mkdir(parents=True, exist_ok=True)
contacts.mkdir(parents=True, exist_ok=True)
pdftoppm = '/usr/bin/pdftoppm' if Path('/usr/bin/pdftoppm').exists() else shutil.which('pdftoppm')
command = [pdftoppm, '-scale-to', '1000', '-png', str(ROOT/'GY1967_test.pdf'), str(pages/'page')]
previous = {path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in pages.glob('page-*.png')}
if not args.reuse:
    subprocess.run(command, check=True)
images = sorted(pages.glob('page-*.png'))
repaired = []
for path in images:
    try:
        with Image.open(path) as image:
            image.load()
    except OSError:
        page_number = int(path.stem.split('-')[-1])
        repair_prefix = pages/f'repair-{page_number:03d}'
        subprocess.run([pdftoppm, '-f', str(page_number), '-l', str(page_number),
                        '-singlefile', '-scale-to', '1000', '-png',
                        str(ROOT/'GY1967_test.pdf'), str(repair_prefix)], check=True)
        repair = repair_prefix.with_suffix('.png')
        with Image.open(repair) as image:
            image.load()
        repair.replace(path)
        repaired.append(page_number)
thumb_width, thumb_height, pad, label, columns, rows = 250, 354, 14, 24, 4, 4
outputs = []
for offset in range(0, len(images), columns*rows):
    sheet = Image.new('RGB', (columns*(thumb_width+pad)+pad,
                             rows*(thumb_height+label+pad)+pad), '#d8d8d8')
    draw = ImageDraw.Draw(sheet)
    for index, path in enumerate(images[offset:offset+columns*rows]):
        page = Image.open(path).convert('RGB')
        page.thumbnail((thumb_width, thumb_height))
        x = pad + (index % columns)*(thumb_width+pad)
        y = pad + (index // columns)*(thumb_height+label+pad)
        sheet.paste(page, (x, y+label))
        draw.text((x, y+3), f'PDF page {offset+index+1}', fill='black')
    output = contacts/f'contact-{offset//(columns*rows)+1:02d}.png'
    sheet.save(output)
    outputs.append(str(output))
result = {'pdf': str(ROOT/'GY1967_test.pdf'), 'rendered_pages':len(images),
          'maximum_dimension_pixels':1000, 'contact_sheets':outputs,
          'command':command, 'repaired_incomplete_png_pages':repaired}
current = {path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in images}
result['rendered_page_sha256'] = current
result['changed_from_previous_render'] = [name for name,value in current.items() if previous.get(name)!=value]
(ROOT/'audit'/'render_output.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
