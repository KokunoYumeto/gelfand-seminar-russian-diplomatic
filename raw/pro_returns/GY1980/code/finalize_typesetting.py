"""Idempotent, content-preserving LaTeX repairs found during compilation.

Apply to the staged item batches and integrated items before build_chapter.py.
The separate format_corrections.py handles the corrections CSV.
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPLACEMENTS = {
    ('1980-498.6', 'notes'): {
        'D_X action by Leibniz': r'\(D_X\) action by Leibniz',
        'pulled-back D_Y action': r'pulled-back \(D_Y\) action',
    },
    ('1980-498.6', 'statement'): {
        'The coefficients a_i are functions': r'The coefficients \(a_i\) are functions',
    },
    ('1980-498.6', 'present_status'): {
        'O_X scalar extension': r'\(O_X\) scalar extension',
    },
    ('1980-506.13', 'reconstruction'): {
        'The scan clearly reads c_1=N;': r'The scan clearly reads \(c_1=N\);',
    },
    ('1980-492.5', 'statement'): {
        'A precise nearby standard example is hyperbolic three-space':
        'A precise standard model is hyperbolic three-space',
    },
    ('1980-495.8', 'notes'): {
        r'followed by \(\mathbb E_x\exp(-\int_0^\infty V(B_s)ds)\le(1-C)^{-1}\).':
        r'followed by \[\mathbb E_x\exp(-\int_0^\infty V(B_s)ds)\le(1-C)^{-1}.\]',
    },
    ('1980-496.8', 'statement'): {
        'the natural global-sections/localization adjunction':
        'the natural adjunction between global sections and localization',
    },
    ('1980-519.4', 'statement'): {
        'A precise verified polynomial-coefficient statement is: over a characteristic-zero field, if':
        'The verified theorem for polynomial coefficients states the following. Over a field of characteristic zero, if',
    },
    ('1980-525.2', 'statement'): {
        'For repulsive inverse-power pair potentials in the usual three-dimensional classical scattering convention, homogeneity yields the displayed relative-speed exponent.':
        'For repulsive inverse-power pair potentials, homogeneity yields the displayed relative-speed exponent in the usual classical scattering convention in three dimensions.',
    },
    ('1980-527.8', 'notes'): {
        r'the potential energy is \(\int_\Omega\int_1^{g^{-1}(x)}p(\rho)\rho^{-2}\,d\rho\,dx\).':
        r'the potential energy is \[\int_\Omega\int_1^{g^{-1}(x)}p(\rho)\rho^{-2}\,d\rho\,dx.\]',
    },
    ('1980-526.2', 'reconstruction'): {
        'requires p<r (the notebook writes only ell<n)':
        r'requires \(p<r\) (the notebook writes only \(\ell<n\))',
    },
}

CORRECTION_PROSE = {
    'item1980-505.1': 'item 1980-505.1',
    'Atiyah1982 Theorem2-prime': r"\citet[Theorem~2']{atiyah1982convexity}",
    'Atiyah1982 pp13-14': r'\citet[pp.~13--14]{atiyah1982convexity}',
    'Danilov1978 bibliography[26]': r'\citet[bibliography, no.~26]{danilov1978toric}',
    'Lecture Notes in Mathematics339(1973)': 'Lecture Notes in Mathematics 339 (1973)',
    'Khovanskii1978 section1': r'\citet[\S1]{khovanskii1978genus}',
    'Khovanskii1978 section3 Theorem2': r'\citet[\S3, Theorem~2]{khovanskii1978genus}',
    'Kazarnovskii1981 Definition3 and Theorem1': r'\citet[Definition~3 and Theorem~1]{kazarnovskii1981zeros}',
    'Mironov 2012 Thm3.4': r'\citet[Theorem~3.4]{mironov2012higher}',
    'Arnold1966': r'\citet{arnold1966geometrie}',
    'Olshanskii1981 Cor5.8': r'\citet[Corollary~5.8]{olshanskii1981cones}',
    'Olshanskii1981 §1': r'\citet[\S1]{olshanskii1981cones}',
    'record509': 'record 509',
    'record512': 'record 512',
    'record513': 'record 513',
    'dated1991': 'dated 1991',
    '23February1981': '23 February 1981',
    '2March1981': '2 March 1981',
    'the23February': 'the 23 February',
    'October1979': 'October 1979',
    'February1980': 'February 1980',
    'A.G.Khovanskii': 'A. G. Khovanskii',
    'I.M.Gelfand': 'I. M. Gelfand',
    'Theorem5': 'Theorem 5',
    'theorem13': 'theorem 13',
    'theorem14': 'theorem 14',
    'theorem15': 'theorem 15',
    'Lecture Notes339': 'Lecture Notes 339',
}

for path in [*(ROOT / 'parts').glob('*_items.json'), ROOT / 'GY1980_items.json']:
    data = json.loads(path.read_text())
    changed = 0
    for item in data:
        for (identifier, field), pairs in REPLACEMENTS.items():
            if item['id'] != identifier:
                continue
            before = item[field]
            for old, new in pairs.items():
                item[field] = item[field].replace(old, new)
            changed += item[field] != before
    if changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(path.relative_to(ROOT), 'changed fields:', changed)

for path in [*(ROOT / 'parts').glob('*_corrections.csv'), ROOT / 'GY1980_corrections.csv']:
    with path.open(newline='') as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    changed = 0
    for row in rows:
        old = r'Two homogeneous quadrics in \(\mathbb P^3\); affine common levels are two-dimensional cones and special fibres may be singular.'
        new = r'The projective intersection is defined by two homogeneous quadrics in \(\mathbb P^3\). Affine common levels are cones of dimension two, and special fibres may be singular.'
        if row['evidence'] == old:
            row['evidence'] = new
            changed += 1
        for field in ['place', 'transcription_reads', 'should_read', 'evidence']:
            before = row[field]
            for old, new in CORRECTION_PROSE.items():
                row[field] = row[field].replace(old, new)
            changed += before != row[field]
    if changed:
        with path.open('w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
    print(path.relative_to(ROOT), 'reflowed correction cells:', changed)

for path in [*(ROOT / 'parts').glob('*_problems.json'), ROOT / 'GY1980_problems.json']:
    data = json.loads(path.read_text())
    changed = 0
    for problem in data:
        if problem['id'] != 'GP-1980-27':
            continue
        before = problem['status']
        problem['status'] = problem['status'].replace(
            r'Kazarnovskii1981 \S1(c)', r'\citet[\S1(c)]{kazarnovskii1981zeros}')
        problem['status'] = problem['status'].replace(
            'Kazarnovskii2024', r'\citet{kazarnovskii2024distribution}')
        changed += before != problem['status']
    if changed:
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(path.relative_to(ROOT), 'problem citation typography:', changed)

# Match the primary Numdam record without mixing two different series numbers.
# https://www.numdam.org/item/SB_1980-1981__23__111_0/ (opened 11 Nov 2026).
for path in [ROOT / 'parts/spring_references.bib', ROOT / 'GY1980_references.bib']:
    before = path.read_text()
    pattern = r'(@incollection\{esnault1981classification,.*?\n\})'
    def clean_esnault(match):
        entry = match.group(1)
        entry = entry.replace('year={1981}, volume={23}, pages={111--131}',
                              'year={1981}, pages={111--131}')
        entry = entry.replace('series={Lecture Notes in Mathematics}, number={901}',
                              r"series={S\'eminaire Bourbaki}, number={23}")
        return entry
    after = re.sub(pattern, clean_esnault, before, flags=re.S)
    if after != before:
        path.write_text(after)
    print(path.relative_to(ROOT), 'bibliography series correction:', after != before)

path = ROOT / 'GY1980_development.tex'
before = path.read_text()
after = re.sub(r'(?m)^(\\begin\{(?:lemma|proposition|example|corollary)\}\[.*\]\\ours(?:Computed)?)$',
               r'\1\\quad', before)
after = after.replace(r'\begin{proof}[Exact computational proof and algebraic smoothness check]',
                      r'\begin{proof}[Exact computation and smoothness]')
after = after.replace(
    r'with \(r=4\), \(s=10\); these are incongruent to zero modulo \(4\).',
    r'with \(r=4\) and \(s=10\), since \(4\nmid10\).')
if after != before:
    path.write_text(after)
print(path.relative_to(ROOT), 'result-label spacing and proof-heading reflow:', after != before)
print('Typesetting repairs complete; mathematical content and identifiers preserved.')
