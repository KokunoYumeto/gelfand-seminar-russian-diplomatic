"""Compare final page renders with an earlier reviewed render set.

Usage: python code/compare_render_hashes.py BASELINE.json PAGE_DIR PDF OUTPUT.json
The baseline maps page-NNN.png names to SHA-256 values. Pixel identity lets
an earlier documented inspection carry forward without claiming a new view.
This script does not perform visual inspection of the changed pages.
"""
from pathlib import Path
import hashlib,json,sys
baseline_path=Path(sys.argv[1]);pages=Path(sys.argv[2]);pdf=Path(sys.argv[3]);dest=Path(sys.argv[4])
baseline=json.loads(baseline_path.read_text())
final={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(pages.glob('page-*.png'))}
assert set(baseline)==set(final),'Page set changed; review new pagination explicitly'
changed=[int(n[5:8]) for n,h in final.items() if baseline[n]!=h]
unchanged=[int(n[5:8]) for n,h in final.items() if baseline[n]==h]
result={'final_pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'page_count':len(final),
        'changed_pages':changed,'unchanged_pages':unchanged,'final_page_hashes':final,
        'scope':'Hash comparison only; changed pages require an actual visual inspection.'}
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['unchanged_pages','final_page_hashes']},indent=2))
