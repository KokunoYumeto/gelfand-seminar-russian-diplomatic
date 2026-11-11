#!/usr/bin/env bash
# Reproducible workspace-only TeX setup for the installed TeX Live tree.
set -euo pipefail
GY_TEX_ROOT="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
source "$GY_TEX_ROOT/env.sh"
mkdir -p "$TEXMFHOME" "$TEXMFVAR" "$TEXMFCONFIG" "$TEXMFCACHE" "$VARTEXFONTS" "$GY_TEX_ROOT/formats"
python - "$GY_TEX_ROOT" <<'PY'
from pathlib import Path
import sys,json,subprocess
root=Path(sys.argv[1])
source=Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts')
if not source.is_dir():raise SystemExit('Required installed AMS font-map directory is absent: '+str(source))
entries=[];seen=set();sources=[]
for path in sorted(source.glob('*.map')):
 sources.append(str(path))
 for line in path.read_text().splitlines():
  if not line.strip() or line.lstrip().startswith('%'):continue
  key=line.split()[0]
  if key not in seen:entries.append(line);seen.add(key)
if not entries:raise SystemExit('No font-map entries found')
out=root/'texmf-home/fonts/map/dvips/gelfand';out.mkdir(parents=True,exist_ok=True)
for name in ('pdftex.map','psfonts.map'):(out/name).write_text('\n'.join(entries)+'\n')
conf=root/'texmf-home/dvipdfmx';conf.mkdir(parents=True,exist_ok=True)
(conf/'dvipdfmx.cfg').write_text('f pdftex.map\n')
checks={}
for name in ('latex.ltx','xelatex.ini','fontspec.sty','plainnat.bst','cmr10.pfb','pdftex.map','dvipdfmx.cfg'):
 command=['kpsewhich',name] if name!='dvipdfmx.cfg' else ['kpsewhich','-progname=xdvipdfmx','-format=other text files',name]
 p=subprocess.run(command,capture_output=True,text=True)
 checks[name]={'returncode':p.returncode,'path':p.stdout.strip()}
 if p.returncode:raise SystemExit('TeX lookup failed: '+name)
report={'font_map_entries':len(entries),'font_map_sources':sources,'lookups':checks,'system_directories_modified':False,'packages_downloaded':False}
(root/'setup_report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
PY
(
 cd "$GY_TEX_ROOT/formats"
 xetex -ini -etex -progname=xelatex -jobname=xelatex -interaction=nonstopmode -halt-on-error xelatex.ini
) > "$GY_TEX_ROOT/format_build.log" 2>&1
python - "$GY_TEX_ROOT" <<'PY'
from pathlib import Path
import sys,json
p=Path(sys.argv[1])/'formats/xelatex.fmt'
assert p.stat().st_size>0
print(json.dumps({'format':str(p),'size_bytes':p.stat().st_size,'format_log':str(p.parent.parent/'format_build.log')}))
PY
