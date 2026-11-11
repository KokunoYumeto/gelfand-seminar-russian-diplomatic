#!/usr/bin/env bash
set -euo pipefail
GY_TEX_ROOT="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
source "$GY_TEX_ROOT/env.sh"
python - "$GY_TEX_ROOT" <<'PY'
from pathlib import Path
import sys,shutil
root=Path(sys.argv[1]);out=root/'smoke';out.mkdir(exist_ok=True)
shutil.copyfile(root.parent/'kit/gelfand_companion.sty',out/'gelfand_companion.sty')
fonts=out/'fonts';fonts.mkdir(exist_ok=True)
for name in ('DejaVuSerif.ttf','DejaVuSerif-Bold.ttf','DejaVuSerif-Italic.ttf','DejaVuSerif-BoldItalic.ttf'):
 shutil.copyfile(Path('/usr/share/fonts/truetype/dejavu')/name,fonts/name)
PY
cd "$GY_TEX_ROOT/smoke"
xelatex -interaction=nonstopmode -halt-on-error smoke.tex > "$GY_TEX_ROOT/smoke_first.log" 2>&1
bibtex smoke > "$GY_TEX_ROOT/smoke_bibtex.log" 2>&1
xelatex -interaction=nonstopmode -halt-on-error smoke.tex > "$GY_TEX_ROOT/smoke_second.log" 2>&1
xelatex -interaction=nonstopmode -halt-on-error smoke.tex > "$GY_TEX_ROOT/smoke_final.log" 2>&1
pdftotext smoke.pdf "$GY_TEX_ROOT/smoke_text.txt"
pdffonts smoke.pdf > "$GY_TEX_ROOT/smoke_fonts.txt"
pdftoppm -f 1 -singlefile -r 110 -png smoke.pdf "$GY_TEX_ROOT/smoke_first_page" > "$GY_TEX_ROOT/smoke_render.log" 2>&1
python - "$GY_TEX_ROOT" <<'PY'
from pathlib import Path
import json,sys
root=Path(sys.argv[1]);log=(root/'smoke_final.log').read_text();txt=(root/'smoke_text.txt').read_text()
assert 'Output written on smoke.pdf' in log
assert 'undefined' not in log.lower()
assert 'Missing character' not in log
assert 'русская цитата' in txt and 'Williamson (2016' in txt
report={'xelatex_passes':3,'bibtex_passes':1,'output':'smoke/smoke.pdf','russian_text_extracted':True,'citation_resolved':True,'undefined_citations_or_references':False,'missing_character_warnings':False,'font_report':'smoke_fonts.txt','visual_render':'smoke_first_page.png'}
(root/'smoke_report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
PY
