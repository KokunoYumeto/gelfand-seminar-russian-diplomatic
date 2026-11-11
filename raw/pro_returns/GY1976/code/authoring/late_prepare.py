from pathlib import Path
import re
for lang in ['en','ru']:
    txt=Path('upload/GY1976_'+lang+'.tex').read_text()
    chunks=re.split(r'(?=\\SourcePage\{GELFAND-P\d+\})',txt)
    for c in chunks[1:]:
        m=re.match(r'\\SourcePage\{GELFAND-P(\d+)\}',c)
        p=int(m.group(1))
        if 685<=p<=706:
            c=re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}','[DIAGRAM: SEE ORIGINAL]',c,flags=re.S)
            c=re.sub(r'\\(?:begin|end)\{GelfandAdjacentEvidence\}(?:\{[^}]*\})*','',c)
            c=re.sub(r'\n\s*\n\s*\n','\n\n',c)
            Path(f'work/late_{p}_{lang}.txt').write_text(c)
print('Prepared 44 page text extracts (diagrams retained by caption; original TEX and PNG remain authoritative).')
