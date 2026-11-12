"""Create non-authoritative page excerpts for review; preserve original inputs."""
from pathlib import Path
import re, json, hashlib, zipfile

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'root_notes'
OUT.mkdir(exist_ok=True)
manifest = []
for p in sorted((ROOT / 'upload').iterdir()):
    manifest.append({'name':p.name, 'size':p.stat().st_size,
                     'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
for lang in ['en','ru']:
    s=(ROOT/'upload'/f'GY1986_{lang}(2).tex').read_text()
    sections=re.split(r'(?=\\SourcePage\{GELFAND-P\d+\})',s)[1:]
    page_map={}
    for section in sections:
        pid=re.search(r'\\SourcePage\{GELFAND-(P\d+)\}',section).group(1)
        # Remove only graphic path code; retain text, equations and editorial notes.
        clean=re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}',
                     '[DIAGRAM: consult original source and scan]',section,flags=re.S)
        clean=re.sub(r'\\(?:begin|end)\{GelfandAdjacentEvidence\}(?:\{[^}]*\}){0,2}','',clean)
        clean=re.sub(r'\\Needspace\{[^\n]*\}\s*','',clean)
        clean=re.sub(r'\n{3,}','\n\n',clean)
        page_map[pid]=clean
    (OUT/f'pages_{lang}.json').write_text(json.dumps(page_map,ensure_ascii=False,indent=2))
    for start,end in [(1257,1296),(1297,1331),(1332,1384)]:
        (OUT/f'{lang}_{start}_{end}.tex').write_text('\n'.join(page_map.get(f'P{i:06d}','') for i in range(start,end+1)))
    print(lang,len(page_map),'pages',sum(len(v) for v in page_map.values()),'review characters')
(OUT/'input_manifest.json').write_text(json.dumps(manifest,indent=2))
print('Inputs hashed:',len(manifest))
