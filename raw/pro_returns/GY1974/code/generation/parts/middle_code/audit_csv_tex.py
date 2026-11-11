#!/usr/bin/env python3
"""Repair TeX delimiters in early correction cells, then audit early/extra CSVs.

Only explicit correction-string literals and their matching CSV cells are changed.
No full generator runs and no final chapter files are modified.
"""
import ast
import csv
import io
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PARTS = ROOT / 'parts'
CSV_PATH = PARTS / 'early_corrections.csv'
GEN_PATH = PARTS / 'early_code' / 'build_early.py'
CHANGES = {
    ('quartic term in V', 'evidence'): r'The literal bracket equals \(15q_1^3(q_1p_2-p_1)\). The corrected coefficient gives zero and agrees with Dubrovin--Novikov (1974), section 4.',
    ('maximal negligible set', 'transcription_reads'): r'A maximal \(Z_\sigma\)-set exists',
    ('growth at infinity', 'evidence'): r'\(R\) has degree \(2N+1\), and the next source line already contains \(kE^N\).',
    ('polynomiality implication', 'evidence'): r'An entire \(E^N+\exp(-E)\) has the same leading asymptotic on the positive real axis but is not a polynomial.',
    ('Riccati coefficient derivative order', 'should_read'): r'Before integration by parts the maximum derivative order is \(2n\)',
    ('Riccati coefficient derivative order', 'evidence'): r'The recurrence gives \(\chi_3=u_{xx}-u^2\). The source exponent \(n-1\) is itself palaeographically provisional.',
    ('first factor of Giusti tensor', 'evidence'): r'The scan clearly gives 1. The literal residual is \(-(3/2)(n-1)x_k/r^3\); both factors \(4/(n-2)\) make it zero and agree with Mingione (2006), equation 3.3.',
    ('spectral constant term', 'evidence'): r'Exact polynomial expansion with \(u=q_1\) and \(P=E^2+q_1E/2+(q_1^2-2q_2+2c)/16\) forces the displayed negative sign. Available published formulas use signs whose complete normalization correspondence has not been established.',
    ('polynomial Wronskian normalization', 'evidence'): r'For leading coefficients \(p,q\), the left side has leading coefficient \(-2ipq\). The earlier pair \(Pe^{+i\zeta x},Qe^{-i\zeta x}\) has the opposite sign in this Wronskian convention.',
    ('Riccati spectral shift and Miura coefficients', 'transcription_reads'): r'\(f_x+f^2=q\), plus-sign equations with coefficient 3',
    ('Riccati spectral shift and Miura coefficients', 'should_read'): r'For \(-y_{xx}+Vy=\zeta^2y\): \(f_x+f^2=V-\zeta^2\); use a consistently normalized Miura identity',
    ('Riccati spectral shift and Miura coefficients', 'evidence'): 'The exact conditional identity is given in boundary row 1973-330.11. The overwritten sign and time scaling do not permit a unique literal replacement.',
    ('Laplacian sign', 'transcription_reads'): r'Positive spectrum and \(\exp(-t\Delta)\), but coordinate \(\operatorname{div}\operatorname{grad}\)',
    ('Laplacian sign', 'should_read'): r'Use \(L=-\operatorname{div}\operatorname{grad}\) for positive eigenvalues, or reverse spectrum and heat signs',
    ('off-diagonal heat expansion', 'transcription_reads'): r'\((4\pi t)^{-n/2}\) times power series near the diagonal',
    ('off-diagonal heat expansion', 'should_read'): r'Include \(\exp(-d_g(x,y)^2/(4t))\) off the diagonal',
    ('Cauchy spectral smoothing', 'transcription_reads'): r'Unqualified convolution with \(\varepsilon/(\lambda^2+\varepsilon^2)\)',
    ('Cauchy spectral smoothing', 'should_read'): r'Specify cutoff or a convergent regularization; divide by \(\pi\) for a normalized Cauchy kernel',
    ('oscillatory trace versus heat trace', 'should_read'): r'For \(\lambda_k=\sqrt{\mu_k}\), use \(\operatorname{Tr}(\exp(i z\sqrt L))\); heat trace uses \(\exp(-z\mu_k)\)',
    ('global propagation front', 'transcription_reads'): r'\(|x-y|=t\)',
    ('global propagation front', 'should_read'): r'Use geodesic Hamilton flow; distance \(=t\) describes only a short-time normal-neighborhood front',
}

with CSV_PATH.open(newline='') as handle:
    reader = csv.DictReader(handle)
    fields = reader.fieldnames
    rows = list(reader)
assert len(rows) == 41
source = GEN_PATH.read_bytes()
lines = source.splitlines(keepends=True)
starts = [0]
for line in lines:
    starts.append(starts[-1] + len(line))
tree = ast.parse(source)
calls = {}
for node in ast.walk(tree):
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'correction':
        if len(node.args) >= 5 and isinstance(node.args[1], ast.Constant):
            calls[node.args[1].value] = node
arg_index = {'transcription_reads': 2, 'should_read': 3, 'evidence': 4}
replacements = []
changed_cells = 0
for row in rows:
    place = row['place']
    for field in arg_index:
        key = (place, field)
        if key not in CHANGES:
            continue
        new = CHANGES[key]
        node = calls[place].args[arg_index[field]]
        old_source = ast.literal_eval(node)
        assert old_source == row[field], (key, 'generator/CSV mismatch', old_source, row[field])
        if row[field] != new:
            literal = ('r' + repr(new).replace('\\\\', '\\')) if "'" not in new else repr(new)
            assert ast.literal_eval(literal) == new
            start = starts[node.lineno - 1] + node.col_offset
            end = starts[node.end_lineno - 1] + node.end_col_offset
            replacements.append((start, end, literal.encode()))
            row[field] = new
            changed_cells += 1
for start, end, literal in sorted(replacements, reverse=True):
    source = source[:start] + literal + source[end:]
ast.parse(source)
if replacements:
    GEN_PATH.write_bytes(source)
    with CSV_PATH.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

# Check every textual field, respecting escaped TeX math delimiters. The CSV
# enum field "type" is metadata, not a raw TeX prose cell.
def check_cell(text, label):
    assert not re.search(r'[\x00-\x08\x0b-\x1f\x7f]', text), (label, 'control character')
    stack = []
    for match in re.finditer(r'\\[()\[\]]', text):
        token = match.group()
        if token in (r'\(', r'\['):
            assert not stack, (label, 'nested math delimiter')
            stack.append(token)
        else:
            assert stack and stack.pop() == {r'\)': r'\(', r'\]': r'\['}[token], (label, 'mismatched math delimiter')
    assert not stack, (label, 'unclosed math delimiter')
    prose = re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]', '', text, flags=re.S)
    assert not re.search(r'(?<!\\)[_%^$&#]', prose), (label, 'raw TeX-sensitive prose', prose)
    assert not re.search(r'\\S[IVXLCDM]+\b', text), (label, 'joined section command')
    depth = 0
    for match in re.finditer(r'(?<!\\)[{}]', text):
        depth += 1 if match.group() == '{' else -1
        assert depth >= 0, (label, 'unbalanced brace')
    assert depth == 0, (label, 'unbalanced brace')

# Extract literal arrays/calls without executing generators, avoiding writes.
early_source = ast.parse(GEN_PATH.read_text())
early_rows = {}
for node in ast.walk(early_source):
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'correction' and len(node.args) >= 5:
        if isinstance(node.args[1], ast.Constant):
            early_rows[ast.literal_eval(node.args[1])] = [ast.literal_eval(arg) for arg in node.args[:5]]
extra_source = ast.parse((PARTS / 'root_code' / 'build_extra.py').read_text())
extra_literal = None
for node in ast.walk(extra_source):
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'corrections' for t in node.targets):
        extra_literal = ast.literal_eval(node.value)
assert extra_literal is not None
for prefix, count in [('early', 41), ('extra', 6)]:
    with (PARTS / f'{prefix}_corrections.csv').open(newline='') as handle:
        all_rows = list(csv.DictReader(handle))
    assert len(all_rows) == count
    for number, row in enumerate(all_rows, 1):
        for field, value in row.items():
            if field != 'type':
                check_cell(value, f'{prefix} row {number} {field}')
        if prefix == 'early':
            original = early_rows[row['place']]
            for i, field in enumerate(['page', 'place', 'transcription_reads', 'should_read', 'evidence']):
                # A subsequent, already existing provenance override deliberately
                # replaces only this evidence cell; it has no math syntax.
                if field == 'evidence' and row['place'] == 'date of records 331--332':
                    continue
                assert row[field] == original[i], (prefix, number, field, 'canonical mismatch')
        else:
            assert list(row.values()) == extra_literal[number - 1], (prefix, number, 'canonical mismatch')
    print(f'{prefix}: audited all {count} rows; math delimiters, braces, control characters, stray TeX syntax, canonical correspondence PASS')
print(f'Updated {changed_cells} cells in {len({place for place, field in CHANGES})} early rows; extra required no changes.')
