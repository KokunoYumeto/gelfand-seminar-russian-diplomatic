"""Check the final delivery gates; write a compact machine-readable result.

Run after assembly, TeX compilation, and code/audit_final.py.
PyMuPDF is used only for PDF inspection; the mathematical checks use stdlib.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re
import fitz

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
required = [
    'GY1966_talks.json', 'GY1966_items.json', 'GY1966_problems.json',
    'GY1966_overview.tex', 'GY1966_development.tex', 'GY1966_corrections.csv',
    'GY1966_references.bib', 'GY1966_report.md', 'GY1966_chapter.tex',
    'GY1966_test.tex', 'GY1966_test.pdf', 'build_chapter.py',
    'gelfand_companion.sty'
]
assert all((ROOT / f).is_file() and (ROOT / f).stat().st_size for f in required)
items = json.loads((ROOT / 'GY1966_items.json').read_text())
counts = dict(Counter(x['class'] for x in items))
assert counts == {'A': 22, 'B': 45, 'C': 3, 'E': 185, 'F': 22}
assert len(items) == 277
chapter = (ROOT / 'GY1966_chapter.tex').read_text()
assert chapter.count(r'\begin{GSitem}') == 277
assert chapter.count(r'\GStalk{') == 38
log = (HERE / 'build/xelatex_final.log').read_text()
for pattern in [r'^!', r'Overfull', r'undefined', r'Missing character',
                r'LaTeX Warning:', r'Package .* Warning:', r'Font Warning:']:
    assert not re.search(pattern, log, re.M), pattern
biblog = (HERE / 'build/GY1966_test.blg').read_text()
assert not re.search(r'^Warning--|error message|I found no|I couldn.t open', biblog, re.M | re.I)
math_outputs = {}
for name in ['pair_partitions', 'singularities', 'sturm_endpoint', 'editorial_algebra']:
    path = HERE / f'check_{name}_output.json'
    obj = json.loads(path.read_text())
    assert str(obj['status']).lower() == 'pass' or str(obj['status']).lower().endswith('checks passed'), (name, obj['status'])
    math_outputs[name] = {'status': obj['status'],
                          'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
audit = json.loads((HERE / 'final_audit.json').read_text())
checks = audit['checks']
assert len(checks) == 15 and all(x['passed'] for x in checks)
doc = fitz.open(ROOT / 'GY1966_test.pdf')
assert len(doc) == 146
texts = [p.get_text() for p in doc]
assert all(t.strip() for t in texts)
assert not any('\ufffd' in t for t in texts)
assert not any(re.search(r'\[proved here\][A-Za-z]', t) for t in texts)
result = {
    'status': 'PASS', 'audit_date': '2026-11-09', 'pdf_pages': len(doc),
    'records': 38, 'items': len(items), 'problems': 21, 'references': 78,
    'corrections': 108, 'classes': {k: counts.get(k, 0) for k in 'ABCDEF'},
    'structured_audit_groups_passed': len(checks),
    'final_tex_errors_or_unresolved_warnings': 0,
    'underfull_line_diagnostics': log.count('Underfull \\hbox'),
    'mathematical_outputs': math_outputs,
    'core_file_sha256': {f: hashlib.sha256((ROOT / f).read_bytes()).hexdigest()
                         for f in required},
    'visual_review': 'All 146 pages inspected; see code/visual_qa.md.',
    'limits': 'Production gates and finite computations do not replace source verification or proofs.'
}
(HERE / 'verification_summary.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ['status', 'pdf_pages', 'items',
                                       'structured_audit_groups_passed',
                                       'final_tex_errors_or_unresolved_warnings']}, indent=2))
