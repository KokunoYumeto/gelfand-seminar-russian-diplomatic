from pathlib import Path
import re,sys
lang=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3])
s=Path(f'upload/GY1964_{lang}.tex').read_text()
parts=re.split(r'(?=\\SourcePage\{GELFAND-P\d+\})',s)
for part in parts:
 m=re.search(r'\\SourcePage\{GELFAND-P(\d+)\}',part)
 if m and a<=int(m[1])<=b:
  part=re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}','[diagram: scan inspection required]',part,flags=re.S)
  part=re.sub(r'\\begin\{minipage\}[^\n]*','',part)
  part=re.sub(r'\\(?:end\{minipage\}|Needspace\{[^}]*\}|par(?![A-Za-z])|smallskip|noindent|centering|raggedright|hfill|medskip)','',part)
  print(part)
