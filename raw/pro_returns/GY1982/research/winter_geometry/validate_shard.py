"""Validate the shard and generate the parent-integration audit files."""
from pathlib import Path
from collections import Counter
import csv
import json
import re

D = Path(__file__).resolve().parent
talks = json.loads((D/'talks.json').read_text())
items = json.loads((D/'items.json').read_text())
problems = json.loads((D/'problems.json').read_text())
corrections = list(csv.DictReader((D/'corrections.csv').open()))
bib = (D/'references.bib').read_text()
keys = re.findall(r'@\w+\{([^,]+)', bib)
assert len(keys) == len(set(keys)) == 44
assert [t['record'] for t in talks] == list(range(574, 586))
assert len(items) == 117 and len(problems) == 4 and len(corrections) == 37

fields = {'id', 'record', 'pages', 'kind', 'title', 'notes', 'statement',
          'reconstruction', 'class', 'fate', 'present_status',
          'literal_correctness', 'publication_match', 'verification',
          'development', 'problem', 'worth', 'refs', 'confidence'}
counts = Counter(i['record'] for i in items)
assert counts[579] == 0
assert next(t for t in talks if t['record'] == 579)['kind'] == 'heading'
for record in range(574, 586):
    assert [i['id'] for i in items if i['record'] == record] == [f'1982-{record}.{j}' for j in range(1, counts[record]+1)]
for item in items:
    assert fields <= item.keys(), item['id']
    assert set(item['refs']) <= set(keys), item['id']
    assert item['class'] in 'ABCDEF'
    assert item['literal_correctness'] in ('correct', 'correct with missing hypotheses', 'false as written', 'not determinable')
    assert item['publication_match'] in ('exact', 'partial', 'thematic only', 'none found')
    assert item['verification'] in ('read the result', 'publisher metadata checked', 'indirect', 'unresolved lead')
    assert item['confidence'] in ('high', 'medium', 'low')
    assert item['present_status'].startswith('As of November 2026:')
    if item['class'] in 'CD':
        assert item['worth']
    for field in ('notes', 'statement', 'reconstruction', 'fate', 'present_status', 'worth'):
        cited = set()
        for citation in re.findall(r'\\cite[tp](?:\[[^]]*\])?\{([^}]+)\}', item[field]):
            cited.update(citation.split(','))
        assert cited <= set(item['refs']), (item['id'], field, cited-set(item['refs']))

for problem in problems:
    assert set(problem['refs']) <= set(keys)
    assert problem['status_date'] == '2026-11'
    assert all(o.startswith('1981-') or o in {i['id'] for i in items} for o in problem['occurrences'])
for item in items:
    if item['problem']:
        assert item['problem'] in {p['id'] for p in problems}
        assert item['id'] in next(p for p in problems if p['id'] == item['problem'])['occurrences']

# Explicit ledger crosswalk. Row numbers are auxiliary and local to this shard;
# page/place pairs remain valid when the parent sorts the combined CSV.
false_to_rows = {
    '1982-575.1': [2], '1982-576.7': [3],
    '1982-577.2': [4], '1982-577.3': [5], '1982-577.6': [6],
    '1982-577.7': [6, 7], '1982-577.10': [9], '1982-577.11': [10],
    '1982-577.13': [11, 12, 13, 14], '1982-577.15': [15],
    '1982-577.18': [16], '1982-577.21': [14, 16],
    '1982-578.3': [17, 18, 19], '1982-578.4': [20], '1982-578.7': [21],
    '1982-582.1': [24], '1982-582.3': [25], '1982-582.5': [26], '1982-582.7': [27],
    '1982-583.6': [29], '1982-583.8': [30], '1982-583.11': [31],
    '1982-584.2': [32], '1982-585.3': [34], '1982-585.5': [33],
    '1982-585.8': [35], '1982-585.9': [36], '1982-585.10': [37],
}
assert set(false_to_rows) == {i['id'] for i in items if i['literal_correctness'] == 'false as written'}
false_to_corrections = {
    item_id: [[corrections[n-1]['page'], corrections[n-1]['place']] for n in rows]
    for item_id, rows in false_to_rows.items()
}
crosswalk = {
    'row_number_convention': '1-based data rows, excluding the header; page/place pairs are stable for integration',
    'false_as_written_to_corrections': false_to_corrections,
    'false_as_written_to_shard_rows': false_to_rows,
    'shared_formula_notes': {
        '1982-577.7': 'Row 6 fixes the ODE coefficient/stress-tensor normalization; row 7 fixes the separate assertion that all accessory parameters are real.',
        '1982-577.11': 'Shared row 10 identifies both the missing Laurent conformal-weight shift and the missing Kronecker delta.',
        '1982-577.13': 'Row 11 is the contour/area charge; rows 12–14 are the missing weight powers at three distinct occurrences.',
        '1982-577.21': 'Row 14 is the missing x^n on the right; shared row 16 is the missing one-half in the oscillator sum on the left.',
        '1982-578.3': 'Rows 17–19 separately identify the potential derivative, wall profile and thickness normalization.',
    },
}
(D/'correction_map.json').write_text(json.dumps(crosswalk, ensure_ascii=False, indent=2)+'\n')

# One primary area per item makes counts additive; secondary areas preserve the
# overlap without double-counting. The root may coarsen this taxonomy.
record_areas = {
    574: ('Representation theory', ['D-modules', 'Perverse sheaves', 'Algebraic geometry']),
    575: ('Operator algebras and geometry', ['Schubert calculus', 'Continuous geometry']),
    576: ('Supergeometry', ['Gauge theory', 'Algebraic geometry']),
    577: ('Conformal field theory', ['Liouville uniformization', 'Virasoro representations']),
    578: ('Classical field theory', ['Solitons', 'Strings', 'Gauge theory']),
    579: ('Metadata', []),
    580: ('Representation theory', ['Infinite-dimensional groups', 'Gaussian measures']),
    581: ('Representation theory', ['Semi-infinite homology', 'String constraints']),
    582: ('Representation theory', ['Infinite-dimensional groups', 'Functional analysis']),
    583: ('Symplectic geometry', ['Equivariant localization', 'Orbit method']),
    584: ('Symplectic geometry', ['Representation theory', 'Weight multiplicities']),
    585: ('Spectral perturbation theory', ['Combinatorics', 'Algebraic geometry']),
}
item_areas = {i['id']: record_areas[i['record']][0] for i in items}
for n in (8, 9, 10, 13, 19, 20, 24):
    item_areas[f'1982-585.{n}'] = 'Combinatorics'
for n in (11, 12):
    item_areas[f'1982-585.{n}'] = 'Algebraic geometry'
areas = {
    'classification_rule': 'One primary area per item for additive counts; record-level secondary areas indicate overlap.',
    'records': [{
        'record': r, 'primary_area': record_areas[r][0], 'secondary_areas': record_areas[r][1],
        'item_count': counts[r], 'items': [i['id'] for i in items if i['record'] == r],
        'class_counts': dict(sorted(Counter(i['class'] for i in items if i['record'] == r).items())),
    } for r in range(574, 586)],
    'areas_by_item': item_areas,
    'item_counts_by_area': dict(sorted(Counter(item_areas.values()).items())),
}
(D/'area_by_record.json').write_text(json.dumps(areas, ensure_ascii=False, indent=2)+'\n')

# Source-audit prose is maintained in the readable report. Its first link in
# every key section is a successfully opened source. Failed additional URLs are
# explained in the prose and are not added to opened_url.
notes = (D/'research_notes.md').read_text()
source_sections = dict(re.findall(r'^### ([a-z0-9]+)\n\n(.*?)(?=^### |^## |\Z)', notes, re.S | re.M))
assert set(source_sections) == set(keys), (set(keys)-set(source_sections), set(source_sections)-set(keys))
metadata_only = {
    'beilinsonbernstein1981localisation', 'vonneumann1960continuous', 'manin1983flags',
    'kobayashi1974monopoles', 'grosswilczek1973ultraviolet', 'marsdenweinstein1974reduction',
}
indirect = {
    'gelfandfuchs1968circle', 'duistermaatheckman1982variation', 'bloch1958perturbations',
    'levykeller1963instability', 'hochstadt1964instability',
}
source_audit = {}
for key in keys:
    section = source_sections[key].strip()
    url = re.search(r'\]\((https?://[^\s]+)\)', section).group(1)
    # Keep the locator and limitations explicit, including failed full-text access.
    prose = re.sub(r'\[([^]]+)\]\((https?://[^\s]+)\)', r'\1 (\2)', section)
    source_audit[key] = {
        'opened_url': url,
        'verification': 'publisher metadata checked' if key in metadata_only else ('indirect' if key in indirect else 'read the result'),
        'locator_and_scope': prose,
        'checked': '2026-11-11',
    }
(D/'source_audit.json').write_text(json.dumps(source_audit, ensure_ascii=False, indent=2)+'\n')

# Character, math delimiter and brace checks supplement the root XeLaTeX build.
latex_values = []
for row in talks:
    latex_values.append((f"talk {row['record']}", row['summary']))
for row in items:
    latex_values.extend((f"{row['id']} {field}", row[field]) for field in ('notes', 'statement', 'reconstruction', 'fate', 'present_status', 'worth'))
for row in problems:
    latex_values.extend((f"{row['id']} {field}", row[field]) for field in ('statement', 'status'))
for n, row in enumerate(corrections, 1):
    latex_values.extend((f"correction {n} {field}", value) for field, value in row.items() if field not in ('type', 'applies_to'))
for location, value in latex_values:
    assert not any(ord(ch) < 32 and ch != '\n' for ch in value), (location, 'control character')
    assert value.count(r'\(') == value.count(r'\)'), (location, 'inline math delimiters')
    assert value.count(r'\[') == value.count(r'\]'), (location, 'display math delimiters')
    without_math = re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]', '', value, flags=re.S)
    without_math = re.sub(r'\\cite[tp](?:\[[^]]*\])?\{[^}]*\}', '', without_math)
    assert not re.search(r'(?<!\\)[_^]', without_math), (location, 'bare sub/superscript', without_math)
    stripped = re.sub(r'\\[{}]', '', value)
    depth = 0
    for ch in stripped:
        if ch == '{': depth += 1
        if ch == '}': depth -= 1
        assert depth >= 0, (location, 'closing brace')
    assert depth == 0, (location, 'brace balance')

report = {
    'status': 'passed', 'records': len(talks), 'items': len(items),
    'problems': len(problems), 'corrections': len(corrections), 'references': len(keys),
    'class_counts': dict(sorted(Counter(i['class'] for i in items).items())),
    'literal_correctness_counts': dict(sorted(Counter(i['literal_correctness'] for i in items).items())),
    'verification_counts': dict(sorted(Counter(i['verification'] for i in items).items())),
    'correction_type_counts': dict(sorted(Counter(c['type'] for c in corrections).items())),
    'false_as_written_to_corrections': false_to_corrections,
    'checks': ['consecutive record and occurrence IDs', 'heading has zero mathematical items',
               'required schema fields and enums', 'problem occurrence links', 'all citation keys exist and are listed in refs',
               'all 44 bibliography keys have an opened-URL audit', 'every false-as-written item maps to correction rows',
               'no control characters or bare math scripts in LaTeX fields', 'balanced math delimiters and braces'],
    'latex_build': 'Parent performs the supplied complete-chapter XeLaTeX/BibTeX build; this is a shard validation.',
}
(D/'validation_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({k: v for k, v in report.items() if k not in ('false_as_written_to_corrections', 'checks')}, ensure_ascii=False, indent=2))
