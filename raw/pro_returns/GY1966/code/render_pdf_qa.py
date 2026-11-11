"""Render the PDF with Poppler and make numbered contact sheets for visual QA.

Usage: python code/render_pdf_qa.py /path/to/qa-output
Requires Pillow and PyMuPDF for image assembly and page count. These packages
are only needed for visual QA, not for data assembly or mathematical checks.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse
import json
import shutil
import subprocess
import fitz
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
ap = argparse.ArgumentParser()
ap.add_argument('output', type=Path)
ap.add_argument('--reuse-renders', action='store_true',
                help='validate existing PNGs and rerender only missing or invalid pages')
args = ap.parse_args()
out = args.output.resolve()
out.mkdir(parents=True, exist_ok=True)
pdf = ROOT / 'GY1966_test.pdf'
doc = fitz.open(pdf)
total = len(doc)
poppler = Path('/usr/bin/pdftoppm')
if not poppler.exists():
    poppler = Path(shutil.which('pdftoppm'))

def render(bounds):
    first, last = bounds
    result = subprocess.run([
        str(poppler), '-f', str(first), '-l', str(last), '-r', '85', '-png',
        str(pdf), str(out / 'page')
    ], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    return {'first': first, 'last': last, 'returncode': result.returncode,
            'stderr': result.stderr}

step = (total + 2) // 3
bounds = [(a, min(a + step - 1, total)) for a in range(1, total + 1, step)]
if args.reuse_renders:
    rendering = [{'reused_existing_renders': True}]
else:
    with ThreadPoolExecutor(max_workers=3) as pool:
        rendering = list(pool.map(render, bounds))

# The local Poppler multi-page run occasionally returned a truncated PNG while
# reporting success. Detect it by a full decode and retry that exact page as a
# separate single-file render. Never admit a partially decoded page to QA.
retried = []
for n in range(1, total + 1):
    path = out / f'page-{n:03d}.png'
    try:
        with Image.open(path) as im:
            im.convert('RGB')
    except (OSError, ValueError, SyntaxError):
        subprocess.run([
            str(poppler), '-f', str(n), '-l', str(n), '-singlefile', '-r', '85',
            '-png', str(pdf), str(path.with_suffix(''))
        ], check=True, capture_output=True, text=True)
        with Image.open(path) as im:
            im.convert('RGB')
        retried.append(n)

for start in range(1, total + 1, 12):
    canvas = Image.new('RGB', (1320, 1455), '#dddddd')
    draw = ImageDraw.Draw(canvas)
    last = min(start + 11, total)
    for j, n in enumerate(range(start, last + 1)):
        with Image.open(out / f'page-{n:03d}.png') as src:
            im = src.convert('RGB')  # Full decode detects truncated PNGs.
        im.thumbnail((320, 450))
        x, y = 10 + (j % 4) * 330, 25 + (j // 4) * 485
        canvas.paste(im, (x + (320 - im.width) // 2, y))
        draw.text((x + 5, y - 18), f'Page {n}', fill='black')
    canvas.save(out / f'contact-{start:03d}-{last:03d}.jpg', quality=90)

result = {'pages': total, 'dpi': 85, 'renderer': str(poppler),
          'rendering': rendering, 'decoded_all_pages': True,
          'single_page_retries_after_decode_failure': retried,
          'contact_sheets': (total + 11) // 12}
(out / 'render_log.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
