#!/usr/bin/env python3
"""Assemble independently authored blocks; keep the seven-file schema intact.

Usage: python code/integrate_chapter.py --source fragments --output chapter
The source folder contains a_, b_, c_ fragments and root development material.
The cumulative bibliography is used to preserve previously established keys.
"""
from pathlib import Path
import argparse
import collections
import csv
import json
import re
import shutil


def bibliography_entries(text, allow_duplicates=False):
    result = {}
    pattern = re.compile(r'@(\w+)\s*\{\s*([^,\s]+)\s*,')
    position = 0
    while match := pattern.search(text, position):
        start = match.start()
        brace = text.index('{', match.start())
        depth = 1
        i = brace + 1
        while i < len(text) and depth:
            if text[i] == '\\':
                i += 2
                continue
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
            i += 1
        if depth:
            raise ValueError('Unclosed BibTeX entry ' + match.group(2))
        key = match.group(2)
        if key in result and not allow_duplicates:
            raise ValueError('Duplicate BibTeX key ' + key)
        result[key] = text[start:i]
        position = i
    return result


def field(entry, name):
    match = re.search(r'\b' + re.escape(name) + r'\s*=\s*[{\"]', entry, re.I)
    if not match:
        return ''
    opening = entry[match.end() - 1]
    closing = '}' if opening == '{' else '"'
    i = match.end()
    start = i
    depth = 1
    while i < len(entry):
        if entry[i] == '\\':
            i += 2
            continue
        if opening == '{' and entry[i] == '{':
            depth += 1
        elif entry[i] == closing:
            depth -= 1
            if depth == 0:
                return entry[start:i]
        i += 1
    raise ValueError('Unclosed BibTeX field ' + name)


def doi(entry):
    return re.sub(r'^https?://(?:dx\.)?doi\.org/', '', field(entry, 'doi').lower()).strip()


def remap(value, mapping):
    if isinstance(value, list):
        return [remap(x, mapping) for x in value]
    if isinstance(value, dict):
        return {k: remap(v, mapping) for k, v in value.items()}
    if not isinstance(value, str):
        return value
    if value in mapping:
        return mapping[value]
    for old, new in mapping.items():
        value = re.sub(r'(?<![\w-])' + re.escape(old) + r'(?![\w-])', new, value)
    return value


def json_write(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def main():
    base = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, default=base / 'fragments')
    parser.add_argument('--output', type=Path, default=base / 'chapter')
    parser.add_argument('--cumulative', type=Path, default=base / 'references_cumulative.bib')
    parser.add_argument('--allow-incomplete', action='store_true')
    args = parser.parse_args()
    src, out = args.source.resolve(), args.output.resolve()
    out.mkdir(parents=True, exist_ok=True)
    audit = out / 'audit'
    audit.mkdir(exist_ok=True)

    data = {name: [] for name in ['talks', 'items', 'problems']}
    corrections = []
    supplied = {}
    duplicates = []
    for block in 'abc':
        for name in data:
            data[name].extend(json.loads((src / f'{block}_{name}.json').read_text()))
        corrections.extend(csv.DictReader((src / f'{block}_corrections.csv').open()))
        bibpath = src / f'{block}_references.bib'
        if not bibpath.exists() and args.allow_incomplete:
            continue
        for key, entry in bibliography_entries(bibpath.read_text()).items():
            if key in supplied:
                duplicates.append(key)
                # Prefer a full-text verification annotation, otherwise first block.
                if 'read' in field(entry, 'annote').lower() and 'read' not in field(supplied[key], 'annote').lower():
                    supplied[key] = entry
            else:
                supplied[key] = entry
    supplied.update(bibliography_entries((src / 'root_references.bib').read_text()))
    cumulative = bibliography_entries(args.cumulative.read_text(), allow_duplicates=True)
    cumulative_doi = {doi(v): k for k, v in cumulative.items() if doi(v)}
    mapping = {}
    for key, entry in supplied.items():
        existing = cumulative_doi.get(doi(entry)) if doi(entry) else None
        if key not in cumulative and existing and existing != key:
            mapping[key] = existing
    data = remap(data, mapping)
    corrections = remap(corrections, mapping)
    formatting_path = src / 'root_correction_formatting.json'
    if formatting_path.exists():
        for override in json.loads(formatting_path.read_text()):
            matches = [r for r in corrections if r['page'] == override['page']
                       and r['place'] == override['place']]
            if len(matches) != 1:
                raise ValueError('Correction formatting override does not identify one row: ' + str(override))
            matches[0].update(override['fields'])
    # Several source blocks use explicit plain-text formula transliterations.
    # Escape TeX-special characters only outside marked mathematical spans.
    for row in corrections:
        for key in ['place', 'transcription_reads', 'should_read', 'evidence']:
            chunks = re.split(r'(\\\(.*?\\\)|\\\[.*?\\\]|\$.*?\$)', row[key], flags=re.S)
            for n in range(0, len(chunks), 2):
                chunks[n] = re.sub(r'(?<!\\)([_&#%])', lambda m: '\\' + m.group(1), chunks[n])
                chunks[n] = re.sub(r'(?<!\\)\^', lambda m: r'\textasciicircum{}', chunks[n])
            row[key] = ''.join(chunks)
    fixed = {}
    for key, entry in supplied.items():
        new = mapping.get(key, key)
        if new != key:
            entry = re.sub(r'(@\w+\s*\{\s*)' + re.escape(key) + r'(?=\s*,)',
                           lambda m: m.group(1) + new, entry, count=1)
        fixed[new] = entry
    supplied = fixed

    data['talks'].sort(key=lambda x: x['record'])
    data['items'].sort(key=lambda x: (x['record'], int(x['id'].rsplit('.', 1)[1])))
    areas = [{'id': x['id'], 'record': x['record'], 'area': x.pop('area', 'Unassigned')}
             for x in data['items']]
    json_write(audit / 'area_assignments.json', areas)
    # A problem may genuinely recur across authoring blocks.
    problems = {}
    for problem in data['problems']:
        if problem['id'] not in problems:
            problems[problem['id']] = problem
        else:
            target = problems[problem['id']]
            target['occurrences'] = list(dict.fromkeys(target['occurrences'] + problem['occurrences']))
            target['refs'] = list(dict.fromkeys(target['refs'] + problem['refs']))
            if target['statement'] != problem['statement'] or target['status'] != problem['status']:
                raise ValueError('Problem text conflict requiring editorial review: ' + problem['id'])
    data['problems'] = list(problems.values())
    for item in data['items']:
        if item.get('problem') in problems:
            p = problems[item['problem']]
            if item['id'] not in p['occurrences']:
                p['occurrences'].append(item['id'])
    for name, values in data.items():
        json_write(out / f'GY1975_{name}.json', values)
    for name in ['root_development.tex', 'root_spectral_development.tex']:
        if not (src / name).exists():
            raise ValueError('Missing development fragment ' + name)
    development = '\n'.join((src / name).read_text() for name in
                            ['root_development.tex', 'root_spectral_development.tex'])
    development = remap(development, mapping)
    (out / 'GY1975_development.tex').write_text(development)
    for name in ['overview.tex', 'report.md']:
        p = src / ('root_' + name)
        if p.exists():
            (out / ('GY1975_' + name)).write_text(remap(p.read_text(), mapping))

    columns = ['page', 'place', 'transcription_reads', 'should_read', 'evidence', 'applies_to', 'type']
    corrections.sort(key=lambda x: (x['page'], x['place']))
    with (out / 'GY1975_corrections.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        writer.writerows(corrections)
    all_text = '\n'.join(json.dumps(x, ensure_ascii=False).replace('\\\\', '\\') for x in data.values())
    all_text += development + '\n' + '\n'.join(' '.join(r.values()) for r in corrections)
    for extra in ['GY1975_overview.tex', 'GY1975_report.md']:
        if (out / extra).exists():
            all_text += (out / extra).read_text()
    cited = set()
    for group in re.findall(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}', all_text):
        cited.update(k.strip() for k in group.split(','))
    for x in [*data['items'], *data['problems']]:
        cited.update(x.get('refs', []))
    bib = {}
    missing = []
    for key in sorted(cited):
        if key in supplied:
            bib[key] = supplied[key]
        elif key in cumulative:
            bib[key] = cumulative[key]
        else:
            missing.append(key)
    (out / 'GY1975_references.bib').write_text(
        '% Verified primary references and inherited bibliography keys.\n\n' +
        '\n\n'.join(bib.values()) + '\n')
    talk_by_id = {x['record']: x for x in data['talks']}
    counts = {
        'records': len(data['talks']), 'items': len(data['items']),
        'problems': len(data['problems']), 'references': len(bib),
        'corrections': len(corrections),
        'by_class': dict(collections.Counter(x['class'] for x in data['items'])),
        'by_area': dict(collections.Counter(x['area'] for x in areas)),
        'by_record_speaker': dict(collections.Counter(talk_by_id[x['record']]['speaker'] for x in data['items'])),
        'by_attributed_speaker': dict(collections.Counter(x.get('speaker') or talk_by_id[x['record']]['speaker'] for x in data['items'])),
        'by_record': dict(collections.Counter(x['record'] for x in data['items'])),
        'by_literal_correctness': dict(collections.Counter(x['literal_correctness'] for x in data['items'])),
        'by_publication_match': dict(collections.Counter(x['publication_match'] for x in data['items'])),
        'by_verification': dict(collections.Counter(x['verification'] for x in data['items'])),
        'by_development': dict(collections.Counter(x['development'] for x in data['items'])),
        'corrections_by_type': dict(collections.Counter(x['type'] for x in corrections)),
        'bib_key_remapping': mapping, 'duplicate_keys_across_blocks': duplicates,
        'missing_references': missing,
        'inherited_keys_without_block_entry': [k for k in bib if k not in supplied]
    }
    json_write(audit / 'counts.json', counts)
    for block in ['a', 'b', 'c', 'root']:
        for suffix in ['research.md', 'sources.json']:
            p = src / f'{block}_{suffix}'
            if p.exists():
                shutil.copy2(p, audit / p.name)
    for name in ['build_chapter.py', 'gelfand_companion.sty', 'CHAPTER_FORMAT.md']:
        shutil.copy2(base / 'kit' / name, out / name)
    print(json.dumps({k: counts[k] for k in ['records', 'items', 'problems', 'references', 'corrections', 'by_class', 'missing_references', 'bib_key_remapping']}, indent=2))
    if missing and not args.allow_incomplete:
        raise SystemExit('Missing bibliographic entries; assembly requires repair.')


if __name__ == '__main__':
    main()
