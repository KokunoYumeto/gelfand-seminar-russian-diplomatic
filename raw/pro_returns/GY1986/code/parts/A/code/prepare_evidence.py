#!/usr/bin/env python3
"""Extract an auditable page slice without modifying the supplied transcriptions."""
from pathlib import Path
import re

base=Path(__file__).resolve().parents[3]
out=base/'parts/A/evidence'
out.mkdir(exist_ok=True, parents=True)
for lang in ('ru','en'):
    source=(base/f'upload/GY1986_{lang}(2).tex').read_text()
    pages=list(re.finditer(r'\\SourcePage\{GELFAND-(P\d+)\}',source))
    for i,m in enumerate(pages):
        number=int(m.group(1)[1:])
        if 1257<=number<=1298:
            text=source[m.start():pages[i+1].start() if i+1<len(pages) else len(source)]
            (out/f'{m.group(1)}_{lang}.tex').write_text(text)
    for low,high in ((1257,1269),(1270,1283),(1284,1298)):
        text='\n'.join((out/f'P{n:06d}_{lang}.tex').read_text() for n in range(low,high+1))
        # Reader aid only: full page extracts above remain the citation authority.
        text=re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', '[DIAGRAM: consult source scan]',text,flags=re.S)
        (out/f'pages_{low}_{high}_{lang}_reader.txt').write_text(text)

