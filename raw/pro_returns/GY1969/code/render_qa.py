#!/usr/bin/env python3
"""Render every PDF page and make labelled contact sheets for visual review."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import io
import json
import re
import subprocess
import sys

D = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(".").resolve()
Q = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else D / "output/visual_review"
(Q / "pages").mkdir(parents=True, exist_ok=True)
if "--reuse-pages" not in sys.argv:
    subprocess.run(["/usr/bin/pdftoppm", "-scale-to", "1000", "-png", str(D / "GY1969_test.pdf"), str(Q / "pages/page")], check=True)
subprocess.run(["/usr/bin/pdftotext", "-layout", str(D / "GY1969_test.pdf"), str(Q / "pdf_text.txt")], check=True)
pages = sorted((Q / "pages").glob("page-*.png"))
repaired = []
previous_repairs = []
if (Q / "render_manifest.json").exists():
    previous_repairs = json.loads((Q / "render_manifest.json").read_text()).get(
        "png_files_repaired_by_individual_rerender", [])
for path in pages:
    try:
        with Image.open(path) as im:
            im.load()
    except OSError:
        number = int(path.stem.split("-")[-1])
        subprocess.run(["/usr/bin/pdftoppm", "-f", str(number), "-l", str(number),
                        "-singlefile", "-scale-to", "1000", "-png", str(D / "GY1969_test.pdf"),
                        str(path.with_suffix(""))], check=True)
        with Image.open(path) as im:
            im.load()
        repaired.append(number)
font_path = D / "fonts/DejaVuSerif.ttf"
font = ImageFont.truetype(str(font_path), 15)
tile_w, tile_h = 250, 370
sheets = []
small_sheets = []
def save_and_check_png(im, path):
    # Finish encoding before writing, then force a complete decode for validation.
    encoded = io.BytesIO()
    im.save(encoded, format="PNG")
    path.write_bytes(encoded.getvalue())
    with Image.open(path) as check:
        check.load()

for start in range(0, len(pages), 24):
    batch = pages[start:start+24]
    sheet = Image.new("RGB", (tile_w * 4, tile_h * 6), "#d9dfe5")
    draw = ImageDraw.Draw(sheet)
    for j, path in enumerate(batch):
        im = Image.open(path).convert("RGB")
        im.thumbnail((tile_w - 12, tile_h - 32))
        x, y = (j % 4) * tile_w, (j // 4) * tile_h
        sheet.paste(im, (x + (tile_w - im.width)//2, y + 22))
        draw.text((x + 8, y + 3), f"Page {start+j+1}", font=font, fill="#172331")
    path = Q / f"contact_{start+1:03d}_{start+len(batch):03d}.png"
    save_and_check_png(sheet, path)
    sheets.append(path.name)
    sheet.thumbnail((700, 1600))
    small_path = path.with_name(path.stem + "_small.png")
    save_and_check_png(sheet, small_path)
    small_sheets.append(small_path.name)
text_pages = (Q / "pdf_text.txt").read_text().split("\f")
if text_pages and not text_pages[-1].strip():
    text_pages.pop()
lengths = [len(re.findall(r"\S+", text)) for text in text_pages]
result = {"rendered_pages": len(pages), "extracted_pages": len(text_pages),
          "contact_sheets": sheets, "words_per_page": lengths,
          "review_size_contact_sheets": small_sheets,
          "all_contact_sheets_decoded_successfully": True,
          "png_files_repaired_by_individual_rerender": sorted(set(previous_repairs + repaired)),
          "pages_with_under_35_words": [i+1 for i,n in enumerate(lengths) if n < 35]}
(Q / "render_manifest.json").write_text(json.dumps(result, indent=2))
print(json.dumps({k:v for k,v in result.items() if k != "words_per_page"}, indent=2))
