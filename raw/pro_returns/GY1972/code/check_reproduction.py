"""Check the archived reviewed inputs reproduce the delivered chapter sources.

Usage: python code/check_reproduction.py RELEASE_DIRECTORY
No LaTeX engine or mathematical computation is repeated. The assembly and
supplied builder run in a temporary sibling directory, then every generated
source is compared byte for byte with the release.
"""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

root=Path(sys.argv[1]).resolve()
files=['GY1972_'+suffix for suffix in [
    'talks.json','items.json','problems.json','overview.tex','development.tex',
    'corrections.csv','references.bib','report.md','chapter.tex','test.tex']]
files.append('assembly_metrics.json')
commands=[]
with tempfile.TemporaryDirectory(prefix='GY1972_reproduction_',dir=root.parent) as tmp:
    out=Path(tmp)
    run=subprocess.run([sys.executable,str(root/'code/assemble.py'),str(out)],
                       capture_output=True,text=True,check=True)
    commands.append({'command':'python code/assemble.py TEMP_DIRECTORY',
                     'returncode':run.returncode,'stdout':run.stdout})
    shutil.copy2(root/'build_chapter.py',out/'build_chapter.py')
    run=subprocess.run([sys.executable,'build_chapter.py','GY1972'],cwd=out,
                       capture_output=True,text=True,check=True)
    commands.append({'command':'python build_chapter.py GY1972',
                     'returncode':run.returncode,'stdout':run.stdout})
    compared=[]
    for name in files:
        original=(root/name).read_bytes()
        regenerated=(out/name).read_bytes()
        assert original==regenerated, f'Assembly/builder output differs: {name}'
        compared.append({'file':name,'identical':True,
                         'sha256':hashlib.sha256(original).hexdigest()})
summary={'status':'passed','files_compared':len(compared),
         'byte_for_byte_comparison':compared,'commands':commands}
(root/'reproduction_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({'status':'passed','files_compared':len(compared)},indent=2))
