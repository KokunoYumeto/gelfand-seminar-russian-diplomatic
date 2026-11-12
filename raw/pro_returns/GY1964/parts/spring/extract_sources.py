from pathlib import Path
import re
out=Path(__file__).parent
for lang in ['en','ru']:
 text=(Path('upload')/f'GY1964_{lang}.tex').read_text()
 pages=re.split(r'(?=\\SourcePage\{GELFAND-P\d+\})',text)
 result=[]
 for p in pages:
  m=re.match(r'\\SourcePage\{GELFAND-P(\d+)\}',p)
  if m and 62<=int(m[1])<=90:
   # Drawings remain available in full source; this reading extract only removes drawing instructions.
   p=re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}','[DRAWING: inspect original scan]',p,flags=re.S)
   result.append(p)
 (out/f'source_{lang}_62_90.txt').write_text('\n'.join(result))
print('Created reduced reading extracts of P000062–P000090; full source and scans remain authoritative.')
