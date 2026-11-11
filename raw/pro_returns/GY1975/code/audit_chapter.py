#!/usr/bin/env python3
"""Additional schema, coverage, citation, chronology and provenance checks.

This complements, and does not replace, the supplied build_chapter.py.
"""
from pathlib import Path
import argparse
import collections
import csv
import json
import re
import sys
from integrate_chapter import bibliography_entries, field, doi


TALK_FIELDS = {'record', 'date', 'speaker', 'pages', 'title', 'kind', 'summary'}
ITEM_FIELDS = {'id', 'record', 'pages', 'kind', 'title', 'notes', 'statement',
               'reconstruction', 'class', 'fate', 'present_status',
               'literal_correctness', 'publication_match', 'verification',
               'development', 'problem', 'worth', 'refs', 'confidence'}
PROBLEM_FIELDS = {'id', 'title', 'statement', 'occurrences', 'status', 'status_date', 'refs'}
ENUMS = {
    'kind': {'definition', 'construction', 'theorem', 'claim', 'conjecture',
             'question', 'problem', 'method', 'remark'},
    'class': set('ABCDEF'),
    'literal_correctness': {'correct', 'correct with missing hypotheses', 'false as written', 'not determinable'},
    'publication_match': {'exact', 'partial', 'thematic only', 'none found'},
    'verification': {'read the result', 'publisher metadata checked', 'indirect', 'unresolved lead'},
    'development': {'none', 'annotated', 'developed in this chapter'},
    'confidence': {'high', 'medium', 'low'}
}
CITE = re.compile(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}')


def citations(text):
    return {k.strip() for group in CITE.findall(text) for k in group.split(',')}


def strings(value):
    if isinstance(value, dict):
        for key, val in value.items():
            for path, text in strings(val):
                yield (str(key) + '.' + path, text)
    elif isinstance(value, list):
        for key, val in enumerate(value):
            for path, text in strings(val):
                yield (str(key) + '.' + path, text)
    elif isinstance(value, str):
        yield ('', value)


def page_numbers(text):
    nums = [int(x) for x in re.findall(r'P0*(\d+)', text)]
    if len(nums) == 2 and '-' in text:
        return set(range(nums[0], nums[1] + 1))
    return set(nums)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', nargs='?', type=Path,
                        default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--catalog', type=Path)
    parser.add_argument('--previous-index', type=Path)
    args = parser.parse_args()
    root = args.directory.resolve()
    errors, warnings = [], []
    talks = json.loads((root / 'GY1975_talks.json').read_text())
    items = json.loads((root / 'GY1975_items.json').read_text())
    problems = json.loads((root / 'GY1975_problems.json').read_text())
    bib = bibliography_entries((root / 'GY1975_references.bib').read_text())
    corrections = list(csv.DictReader((root / 'GY1975_corrections.csv').open()))
    by_record = {t['record']: t for t in talks}
    if [t['record'] for t in talks] != list(range(363, 397)):
        errors.append('Catalogue records must be exactly 363–396, once each, in source order.')
    for t in talks:
        if set(t) != TALK_FIELDS:
            errors.append(f"record{t['record']}: schema keys differ: {set(t) ^ TALK_FIELDS}")
        if t['kind'] not in {'talk', 'plan', 'heading', 'other'}:
            errors.append(f"record{t['record']}: bad kind")
    ids = {x['id'] for x in items}
    by_item_id = {x['id']: x for x in items}
    if len(ids) != len(items):
        errors.append('Duplicate item ID')
    problems_by_id = {p['id']: p for p in problems}
    if len(problems_by_id) != len(problems):
        errors.append('Duplicate problem ID')
    cover = set()
    refs_used = set()
    for x in items:
        name = x['id']
        if set(x) - {'speaker'} != ITEM_FIELDS:
            errors.append(f'{name}: schema keys differ: {(set(x)-{"speaker"}) ^ ITEM_FIELDS}')
        for key, allowed in ENUMS.items():
            if x.get(key) not in allowed:
                errors.append(f'{name}: invalid {key}={x.get(key)}')
        if not re.fullmatch(r'1975-' + str(x['record']) + r'\.\d+', name):
            errors.append(name + ': invalid academic-year identifier')
        pages = page_numbers(x['pages'])
        if not pages or not pages <= set(range(603, 659)):
            errors.append(name + ': invalid source pages')
        cover |= pages
        if x['record'] in by_record and not pages <= page_numbers(by_record[x['record']]['pages']):
            warnings.append(name + ': item pages extend outside catalogue scan envelope')
        if x['class'] in 'CD' and not x['worth'].strip():
            errors.append(name + ': class C/D lacks development decision')
        refs_used.update(x['refs'])
        used = set().union(*(citations(t) for _, t in strings(x)))
        if not used <= set(x['refs']):
            errors.append(name + ': cited works missing from refs: ' + str(used-set(x['refs'])))
        if x['problem']:
            if x['problem'] not in problems_by_id:
                errors.append(name + ': unknown problem ID ' + x['problem'])
            elif name not in problems_by_id[x['problem']]['occurrences']:
                errors.append(name + ': missing reciprocal problem occurrence')
    per_record = collections.defaultdict(list)
    for x in items:
        per_record[x['record']].append(x['id'])
    for record, record_ids in per_record.items():
        if record_ids != [f'1975-{record}.{i}' for i in range(1, len(record_ids) + 1)]:
            errors.append(f'record{record}: nonconsecutive item numbering')
    if per_record[378]:
        errors.append('Year heading378 should not manufacture mathematical items.')
    for p in problems:
        if set(p) != PROBLEM_FIELDS:
            errors.append(p['id'] + ': bad problem schema')
        if not re.fullmatch(r'2026-11(?:-10)?', p['status_date']):
            warnings.append(p['id'] + ': unexpected status_date')
        for occurrence in p['occurrences']:
            if occurrence.startswith('1975-') and occurrence not in ids:
                errors.append(p['id'] + ': unknown current occurrence ' + occurrence)
            elif occurrence.startswith('1975-') and by_item_id[occurrence]['problem'] != p['id']:
                errors.append(p['id'] + ': missing reciprocal item problem field at ' + occurrence)
        refs_used.update(p['refs'])
        used = set().union(*(citations(t) for _, t in strings(p)))
        if not used <= set(p['refs']):
            errors.append(p['id'] + ': cited works absent from refs')
    if args.previous_index:
        prior = args.previous_index.read_text()
        for p in problems:
            if not p['id'].startswith('GP-1975-') and p['id'] not in prior:
                errors.append('Unverified older problem ID ' + p['id'])
            for occurrence in p['occurrences']:
                if not occurrence.startswith('1975-') and occurrence not in prior:
                    errors.append('Unverified older occurrence ID ' + occurrence)
    if args.catalog:
        catalog = args.catalog.read_text()
        for record, date, pages in re.findall(r'record (\d+):.*?\(([^)]+)\); pages ([^;]+);', catalog):
            record = int(record)
            if record not in by_record:
                continue
            t = by_record[record]
            if date != 'no date' and t['date'] != date:
                errors.append(f'record{record}: date differs from catalogue')
            if t['pages'] != pages:
                warnings.append(f'record{record}: scan envelope differs from catalogue')
    for path, text in strings([talks, items, problems, corrections]):
        if re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', text):
            errors.append(path + ': control character in text')
        if re.search(r',\s*(area|literal|refs|speaker|verification|confidence|problem|development)\s*=', text):
            errors.append(path + ': possible authoring keyword leak')
        if r"\'s" in text:
            errors.append(path + ': LaTeX accent used as an English apostrophe')
        if '\\slashed' in text:
            errors.append(path + ': unsupported slashed macro')
    all_text = '\n'.join(t for _, t in strings([talks, items, problems, corrections]))
    for name in ['GY1975_overview.tex', 'GY1975_development.tex']:
        if (root / name).exists():
            all_text += (root / name).read_text()
        else:
            errors.append('Missing ' + name)
    refs_used.update(citations(all_text))
    if refs_used - set(bib):
        errors.append('Missing bibliography keys: ' + ', '.join(sorted(refs_used-set(bib))))
    doi_to_keys = collections.defaultdict(list)
    for key, entry in bib.items():
        if not field(entry, 'url') and not field(entry, 'doi'):
            errors.append(key + ': neither URL nor DOI')
        if field(entry, 'note') not in {'verified', 'unverified'}:
            errors.append(key + ': verification note must be explicit')
        if doi(entry):
            doi_to_keys[doi(entry)].append(key)
    for d, keys in doi_to_keys.items():
        if len(keys) > 1:
            warnings.append('Same DOI under multiple keys: ' + ', '.join(keys))
    for row in corrections:
        if row['applies_to'] not in {'ru', 'en', 'both'}:
            errors.append('Invalid correction language ' + row['page'])
        if row['type'] not in {'transcription', 'translation', 'ambiguity', 'faithful_error', 'provenance', ''}:
            errors.append('Invalid correction type ' + row['page'])
    result = {'passed': not errors, 'errors': errors, 'warnings': warnings,
              'records': len(talks), 'items': len(items), 'problems': len(problems),
              'references': len(bib), 'corrections': len(corrections),
              'item_page_coverage': sorted(cover),
              'source_pages_without_item_range': sorted(set(range(603, 659)) - cover),
              'unused_bibliography_keys': sorted(set(bib)-refs_used)}
    dest = root / 'audit'
    dest.mkdir(exist_ok=True)
    (dest / 'data_audit.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(bool(errors))


if __name__ == '__main__':
    main()
