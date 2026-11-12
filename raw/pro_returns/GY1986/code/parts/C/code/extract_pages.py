"""Reproduce bilingual source-page extracts used for the slice audit."""
from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
workspace=root.parents[1]
for lang in ('en','ru'):
    source=workspace/'upload'/f'GY1986_{lang}(2).tex'
    text=source.read_text()
    matches=list(re.finditer(r'\\SourcePage\{GELFAND-P(\d+)\}',text))
    count=0
    for i,m in enumerate(matches):
        page=int(m.group(1))
        if 1329 <= page <= 1384:
            stop=matches[i+1].start() if i+1<len(matches) else len(text)
            (root/'evidence'/f'{page:06d}_{lang}.txt').write_text(text[m.start():stop])
            count+=1
    print(lang,count,'page extracts')
