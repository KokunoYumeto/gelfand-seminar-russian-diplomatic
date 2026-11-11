#!/usr/bin/env python3
"""Assemble independently researched tranches without losing source order.

Usage: python code/assemble.py --parts code/parts --output .
Only standard-library modules are needed. Bibliography aliases are merged by
an identical DOI, or an already identical key; all renamings are logged.
"""
from __future__ import annotations
import argparse
import collections
import csv
import json
from pathlib import Path
import re

SOURCE_ORDER = [53,54,55,56,57,58,59,60,62,61,63,64,66,67,65,68,
                69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,88]
TRANCHES = ['early', 'middle', 'root', 'late']
TAG = 'GY1965'

def rewrite(value, replacements):
    if isinstance(value, str):
        for old, new in replacements.items():
            if old != new:
                value = value.replace(old, new)
        return value
    if isinstance(value, list):
        return [rewrite(x, replacements) for x in value]
    if isinstance(value, dict):
        return {k: rewrite(v, replacements) for k,v in value.items()}
    return value

def bib_entries(text):
    matches = list(re.finditer(r'(?m)^@\w+\s*\{\s*([^,\s]+)\s*,', text))
    for i, match in enumerate(matches):
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        yield match.group(1), text[match.start():end].strip()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--parts', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    data = {kind: [] for kind in ['talks', 'items', 'problems']}
    for tranche in TRANCHES:
        for kind in data:
            path = args.parts / f'{tranche}_{kind}.json'
            data[kind].extend(json.loads(path.read_text(encoding='utf-8')))
    by_record = {t['record']: t for t in data['talks']}
    assert len(by_record) == len(data['talks']) == 37
    assert set(by_record) == set(range(53,90))
    data['talks'] = [by_record[r] for r in SOURCE_ORDER]
    record_position = {record: i for i,record in enumerate(SOURCE_ORDER)}
    data['items'].sort(key=lambda x: (record_position[x['record']],
                                     int(x['id'].split('.')[-1])))
    positions = {x['id']: i for i,x in enumerate(data['items'])}
    data['problems'].sort(key=lambda p: min(positions[o] for o in p['occurrences']
                                            if o in positions))
    problem_map = {p['id']: f'GP-1965-{i:02}'
                   for i,p in enumerate(data['problems'],1)}
    references, doi_to_key, reference_map, duplicate_notes = {}, {}, {}, []
    for tranche in TRANCHES:
        text = (args.parts / f'{tranche}_references.bib').read_text(encoding='utf-8')
        for key, entry in bib_entries(text):
            if key=='donsker1951invariance':
                # This is a numbered monograph in a memoir series, rather than
                # an article with a missing journal-volume field.
                entry=entry.replace('@article{','@book{',1)
                entry=entry.replace('journal = {Memoirs of the American Mathematical Society}',
                                    'series = {Memoirs of the American Mathematical Society}')
                entry=entry.replace('number = {6},',
                                    'number = {6},\n  publisher = {American Mathematical Society},')
            doi_match = re.search(r'(?i)\bdoi\s*=\s*\{([^{}]+)\}', entry)
            doi = doi_match.group(1).lower().strip() if doi_match else None
            canonical = key if key in references else doi_to_key.get(doi) if doi else None
            if canonical:
                reference_map[key] = canonical
                duplicate_notes.append({'key':key,'canonical':canonical,
                                        'reason':'same key' if canonical==key else 'identical DOI'})
            else:
                references[key] = entry
                reference_map[key] = key
                if doi:
                    doi_to_key[doi] = key
    replacements = {**reference_map, **problem_map}
    data = rewrite(data, replacements)
    # Typesetting-only changes to long mathematical formulas. These leave
    # content and classification unchanged and prevent unbreakable inline
    # mathematics from extending beyond the page.
    display_formulas = {
      'Exterior-power traces give the de Rham numerator':
        r'\sum_{q=0}^n(-1)^q\operatorname{tr}(\Lambda^q A)=\det(I-A)',
      'Change of coordinates and cotangent transformation':
        r'\widetilde\sigma(y,\eta)=\sigma(\kappa^{-1}(y),D\kappa(\kappa^{-1}(y))^T\eta)',
      'Root-system classification and its scope':
        r'A_n,B_n,C_n,D_n,E_6,E_7,E_8,F_4,G_2',
      'Angular Sobolev regularity sufficient for L2 boundedness':
        r'M=\operatorname*{ess\,sup}_x\sum_{m,k}(1+m)^{2q}|a_{mk}(x)|^2<\infty',
    }
    for item in data['items']:
        formula = display_formulas.get(item['title'])
        if formula:
            before=r'\('+formula+r'\)'
            after=r'\['+formula+r'\]'
            assert before in item['statement'],item['id']
            item['statement']=item['statement'].replace(before,after)
        if item['id']=='1965-77.9':
            item['statement']=item['statement'].replace('functional-analytic','functional analytic')
            item['statement']=item['statement'].replace(
                'smooth volume-preserving fluid motions',
                'smooth fluid motions that preserve volume')
        if item['id']=='1965-58.2':
            item['statement'] = 'Over an algebraically closed field \\(k\\), '+item['statement'][0].lower()+item['statement'][1:]
        if item['id']=='1965-74.10':
            item['statement']=item['statement'].replace(
                r'when \(f\ne0\).',
                r'when \(f\) is a nonzero germ at zero; for example, take '
                r'\(f(x)=e^{-1/x^2}\) for \(x\ne0\) and \(f(0)=0\).')
        if item['id']=='1965-75.6':
            item['statement']=item['statement'].replace(
                'For a local holomorphic row frame and a metric linear in the first argument,',
                r'For a local holomorphic column frame \(s=(s_i)\), with '
                r'\(Ds=\theta s\), and a metric linear in the first argument,')
        if item['id']=='1965-77.3':
            item['statement']=item['statement'].replace(
                'for a no-slip steady solution',
                'for a steady incompressible Navier--Stokes solution')
            item['statement']=item['statement'].replace(
                'in a bounded domain with Poincare constant',
                r'in a bounded domain with viscosity \(\nu>0\), homogeneous '
                'no-slip boundary conditions and Poincare constant')
            item['statement']=item['statement'].replace(
                'every sufficiently regular solution with the same forcing obeys',
                'every sufficiently regular solution with the same forcing and '
                'boundary conditions obeys, on its interval of existence,')
            item['statement']=item['statement'].replace(
                'it does not by itself prove its existence as viscosity varies.',
                'it does not by itself prove the equilibrium\'s existence as viscosity '
                'varies or global existence of the evolving classical solution. '
                r'Here \(\lambda_1\) means \(\|\nabla w\|_2^2\ge '
                r'\lambda_1\|w\|_2^2\), and the gradient bound uses the pointwise '
                'matrix operator norm (the Frobenius norm also suffices).')
        if item['id']=='1965-63.8':
            item['statement']=item['statement'].replace(
                'It equals an unweighted count only under special unit-weight conditions.',
                'Unit local weights suffice for equality with an unweighted count; '
                'they are not necessary for equality of the total sums.')
            item['reconstruction'] += (
                r' \ours\ On \(\mathbb{RP}^1\), the map \(x\mapsto3x\) '
                r'has fixed points zero and infinity, with derivatives \(3\) and '
                r'\(1/3\) in their respective local coordinates. Its weights '
                r'\(1/2\) and \(3/2\) sum to the unweighted count \(2\), '
                r'even though neither weight is one. This independently checked '
                r'example prevents treating a sufficient normalization as necessary.')
    for talk in data['talks']:
        if talk['record']==74:
            talk['summary']=talk['summary'].replace('division/preparation theorem','division and preparation theorem')
    # Normalize alias removal to avoid repeated keys in the machine-readable lists.
    for kind in ['items','problems']:
        for entry in data[kind]:
            entry['refs'] = list(dict.fromkeys(entry['refs']))
    corrections = []
    for tranche in TRANCHES:
        with (args.parts / f'{tranche}_corrections.csv').open(encoding='utf-8',newline='') as stream:
            corrections.extend(rewrite(list(csv.DictReader(stream)), replacements))
    corrections.sort(key=lambda row: row['page'])
    # Presentation-only fixes: the source tranches also contain plain-text
    # mathematical snippets, whereas the supplied table inserts cells as TeX.
    correction_tex_fixes = {
        '(Box u,u)=||du||^2+||d*u||^2':r'\((\Box u,u)=\|du\|^2+\|d^*u\|^2\)',
        'x^2=0':r'\(x^2=0\)',
        'after F^1(B)':r'after \(F^1(B)\)',
        'Box=dd*+d*d':r'\(\Box=dd^*+d^*d\)',
        '(d/dt)*=-d/dt':r'\((d/dt)^*=-d/dt\)',
        'Re(z)=(z+conjugate(z))/2':r'\(\operatorname{Re}z=(z+\overline z)/2\)',
        'trace z+conjugate(z)':r'trace \(z+\overline z\)',
    }
    for row in corrections:
        for field in ['evidence','should_read']:
            row[field] = rewrite(row[field], correction_tex_fixes)
    for kind, entries in data.items():
        (args.output / f'{TAG}_{kind}.json').write_text(
            json.dumps(entries,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    columns = ['page','place','transcription_reads','should_read','evidence','applies_to']
    with (args.output / f'{TAG}_corrections.csv').open('w',encoding='utf-8',newline='') as stream:
        writer = csv.DictWriter(stream,fieldnames=columns)
        writer.writeheader(); writer.writerows(corrections)
    (args.output / f'{TAG}_references.bib').write_text(
        '% Checked source bibliography; access date 9 November 2026.\n\n'+
        '\n\n'.join(references.values())+'\n',encoding='utf-8')
    log = {'source_order': SOURCE_ORDER, 'problem_ids': problem_map,
           'reference_aliases': {k:v for k,v in reference_map.items() if k!=v},
           'duplicate_reference_entries':duplicate_notes,
           'counts':{'records':len(data['talks']),'items':len(data['items']),
                     'classes':dict(collections.Counter(x['class'] for x in data['items'])),
                     'problems':len(data['problems']),'references':len(references),
                     'corrections':len(corrections)}}
    (args.output/'evidence').mkdir(exist_ok=True)
    (args.output/'evidence/assembly.json').write_text(
        json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(log,ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
