#!/usr/bin/env python3
"""Audit saved computations, cutoff stability, and the claimed finite totals."""
import csv
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
datasets = {}
checks = {}
for limit in (40, 90, 150):
    folder = root / 'computations' / f'm{limit}'
    metadata = json.loads((folder / 'perchik_verification.json').read_text())
    with (folder / 'perchik_coefficients.csv').open() as stream:
        rows = list(csv.DictReader(stream))
    values = {int(r['m']): int(r['relative_euler_characteristic']) for r in rows}
    assert set(values) == set(range(-1, limit + 1))
    assert values == {int(k): v for k, v in metadata['coefficients'].items()}
    assert metadata['all_laurent_rows_agree']
    assert metadata['positive_product_cutoff'] == 2 * limit + 2
    datasets[limit] = values
    checks[f'm{limit}_csv_matches_output'] = True
for limit in (40, 90):
    assert all(datasets[limit][m] == datasets[150][m] for m in datasets[limit])
    checks[f'cutoff_m{limit}_matches_m150'] = True

v = datasets[150]
assert sum(abs(v[m]) for m in range(-1, 36)) == 57
assert sum(v[m] != 0 for m in range(1, 151)) == 135
assert sum(abs(v[m]) for m in range(1, 151)) == 9701705312
assert v[35] == 10 and v[86] == -22044 and v[129] == 7151485
assert v[130] == 41831534 and v[150] == 1408548898
checks['notebook_lower_bound_57'] = True
checks['nonzero_positive_weights_135'] = True
checks['sum_absolute_coefficients_9701705312'] = True
checks['published_checkpoints_35_and_129_agree'] = True
checks['m86_text_extraction_discrepancy'] = {
    'computed': -22044,
    'retrieved_pdf_text': -2204,
    'interpretation': 'Check page image before calling this a printed error.'
}
checks['sha256'] = {
    str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
    for p in sorted((root / 'computations').glob('m*/perchik_coefficients.csv'))
}
out = root / 'computations' / 'independent_audit.json'
out.write_text(json.dumps(checks, indent=2) + '\n')
print(json.dumps(checks, indent=2))
