from pathlib import Path
import re
base=Path(__file__).resolve().parents[3]
out=base/"work/pages"
out.mkdir(parents=True,exist_ok=True)
for lang in ("en","ru"):
 text=(base/f"upload/GY1965_{lang}.tex").read_text()
 pages=re.split(r"(?=\\SourcePage\{GELFAND-P\d+\})",text)[1:]
 for page in pages:
  num=re.search(r"GELFAND-(P\d+)",page).group(1)
  compact=re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}","[Diagram: inspect the corresponding scan; editorial description follows.]",page,flags=re.S)
  compact=re.sub(r"\\Needspace\{[^\n]*\}\n","",compact)
  (out/f"{num}_{lang}.txt").write_text(compact)
 print(lang,len(pages),"pages",sum((out/f"P{n:06d}_{lang}.txt").stat().st_size for n in range(88,140)),"compact bytes")
