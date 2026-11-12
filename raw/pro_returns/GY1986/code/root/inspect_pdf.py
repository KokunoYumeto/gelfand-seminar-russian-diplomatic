"""Check every page's text bounds and render representative pages for QA."""
from pathlib import Path
import json, subprocess
import fitz
from PIL import Image, ImageDraw

OUT=Path(__file__).resolve().parents[2]
CODE=OUT/"code"/"root"
QA=OUT.parent/"root_notes"/"pdf_qa"

def main():
    QA.mkdir(parents=True,exist_ok=True)
    doc=fitz.open(OUT/"GY1986_test.pdf")
    checks=[];empty=[];texts=[]
    for i,page in enumerate(doc):
        text=page.get_text();texts.append(" ".join(text.split()).casefold())
        if not text.strip():empty.append(i+1)
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines",[]):
                for span in line.get("spans",[]):
                    if not span["text"].strip():continue
                    x0,y0,x1,y1=span["bbox"]
                    if x0<15 or y0<10 or x1>page.rect.width-15 or y1>page.rect.height-10:
                        checks.append({"page":i+1,"text":span["text"],"bbox":span["bbox"]})
    landmarks={
        "first_page":1,"overview_end":2,"early_record":4,
        "quantum_kdv_development":"a level-two calculation and a jordan obstruction",
        "quantum_kdv_jordan":"a jordan block in an irreducible quotient",
        "unitary_development":"evaluation, error control, and a failed extension",
        "unitary_moment_formula":"all-rank convergent evaluation",
        "unitary_counterexample":"failure of a specific permutation-only extension",
        "complex_structure_development":"an annotation on simultaneous complex structures",
        "cube_development":"an exact audit of the cube",
        "problem_index":"problem index",
        "corrections":"corrections to the transcription and translation",
        "corrected_resolvent":"resolvent square root",
        "source_order_schwarz":"1986-707.1",
        "bibliography":"bibliography",
        "last_page":len(doc),
    }
    chosen={}
    for name,needle in landmarks.items():
        if isinstance(needle,int):chosen[name]=needle;continue
        hits=[i+1 for i,t in enumerate(texts) if needle in t]
        if name=="bibliography":
            hits=[i+1 for i,page in enumerate(doc)
                  if any(line.strip()=="Bibliography" for line in page.get_text().splitlines())]
        # Short mentions in the overview are not the actual index or section.
        if name in {"problem_index","corrections","bibliography"}:
            hits=[n for n in hits if n>130]
        if hits:chosen[name]=hits[0]
    for page in sorted(set(chosen.values())):
        prefix=QA/f"page_{page:03d}"
        subprocess.run(["pdftoppm","-f",str(page),"-l",str(page),"-r","115",
                        "-png","-singlefile",str(OUT/"GY1986_test.pdf"),str(prefix)],
                       check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    pages=sorted(set(chosen.values()))
    thumbw=420;thumbh=620;columns=3;rows=(len(pages)+columns-1)//columns
    canvas=Image.new("RGB",(columns*thumbw,rows*thumbh),"#e5e5e5")
    draw=ImageDraw.Draw(canvas)
    for index,page in enumerate(pages):
        im=Image.open(QA/f"page_{page:03d}.png").convert("RGB")
        im.thumbnail((thumbw-20,thumbh-30))
        x=(index%columns)*thumbw+(thumbw-im.width)//2
        y=(index//columns)*thumbh+25
        canvas.paste(im,(x,y))
        draw.text(((index%columns)*thumbw+12,(index//columns)*thumbh+5),
                  f"PDF page {page}",fill="black")
    canvas.save(QA/"contact_sheet.png")
    fonts=subprocess.run(["pdffonts",str(OUT/"GY1986_test.pdf")],
                         text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,check=True)
    (CODE/"pdffonts.out").write_text(fonts.stdout)
    record={
        "pages":len(doc),"empty_pages":empty,
        "text_spans_near_or_outside_paper_edge":checks,
        "selected_pages":chosen,
        "render_method":"Poppler pdftoppm, 115 dpi, full-page PNGs",
        "contact_sheet":"Intermediate inspection image; not part of the reading copy.",
        "visual_review":"Pending direct inspection of rendered pages.",
    }
    (CODE/"pdf_inspection.json").write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(record,ensure_ascii=False,indent=2))
    if empty or checks:
        raise SystemExit("Inspect potential blank pages or clipping before delivery.")

if __name__=="__main__":
    main()
