#!/usr/bin/env python3
"""Merge independently researched record groups into the seven-file schema.

Usage from the delivered chapter directory:
  python code/merge_fragments.py
The default inputs are the frozen source_fragments snapshot. For initial
authoring, --inputs and --cumulative may point to the working directories.
This script does not establish the truth of any mathematical statement.
"""
import argparse
import collections
import csv
import json
import pathlib
import re

from audit_data import cites
from latex_text import normalize_record


def split_bib(text):
    """Return all balanced entries, including repeated cumulative keys."""
    out = []
    for m in re.finditer(r'(?m)^@(\w+)\s*\{\s*([^,\s]+)\s*,', text):
        depth = 0
        escape = False
        for end in range(text.index('{', m.start()), len(text)):
            ch = text[end]
            if escape:
                escape = False
            elif ch == '\\':
                escape = True
            elif ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    break
        else:
            raise ValueError('Unbalanced entry: ' + m.group(2))
        out.append((m.group(2), text[m.start():end + 1]))
    return out


def field(entry, name):
    m = re.search(r'\b' + name + r'\s*=\s*\{([^{}]*)\}', entry, re.I)
    return m.group(1).strip() if m else ''


def doi(entry):
    return re.sub(r'^https?://(?:dx\.)?doi\.org/', '', field(entry, 'doi')).lower()


def rewrite_citations(value, aliases):
    if isinstance(value, list):
        return [rewrite_citations(v, aliases) for v in value]
    if isinstance(value, dict):
        result = {k: rewrite_citations(v, aliases) for k, v in value.items()}
        if 'refs' in result:
            result['refs'] = list(dict.fromkeys(aliases.get(k, k) for k in value['refs']))
        return result
    if not isinstance(value, str):
        return value
    pat = r'(\\cite\w*\*?(?:\[[^\]]*\])*\{)([^}]+)(\})'
    return re.sub(pat, lambda m: m[1] + ','.join(aliases.get(k.strip(), k.strip())
                                               for k in m[2].split(',')) + m[3], value)


def main():
    root = pathlib.Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', type=pathlib.Path,
                        default=root / 'code' / 'source_fragments')
    parser.add_argument('--cumulative', type=pathlib.Path)
    parser.add_argument('--root-bib', type=pathlib.Path,
                        default=root / 'audit' / 'root_references.bib')
    parser.add_argument('--allow-missing-bib', action='store_true')
    args = parser.parse_args()
    cumulative_path = args.cumulative or args.inputs / 'references_cumulative.bib'
    all_cumulative = split_bib(cumulative_path.read_text())
    variants = collections.defaultdict(list)
    for k, e in all_cumulative:
        variants[k].append(e)
    # Later cumulative entries normally contain the more recent verification.
    # Research fragments may override their metadata, while preserving the key.
    bibliography = {k: entries[-1] for k, entries in variants.items()}
    cumulative_doi = {}
    for k, e in all_cumulative:
        if doi(e):
            cumulative_doi.setdefault(doi(e), k)
    talks, items, problems, corrections = [], [], [], []
    fragment_entries = []
    for group in ('a', 'b', 'c'):
        directory = args.inputs / group
        for target, name in ((talks, 'talks'), (items, 'items'), (problems, 'problems')):
            target.extend(json.loads((directory / f'{name}.json').read_text()))
        with (directory / 'corrections.csv').open(newline='') as f:
            corrections.extend(csv.DictReader(f))
        if (directory / 'references.bib').exists():
            fragment_entries.extend(split_bib((directory / 'references.bib').read_text()))
    fragment_entries.extend(split_bib(args.root_bib.read_text()))
    aliases = {}
    chosen_doi = dict(cumulative_doi)
    for k, entry in fragment_entries:
        d = doi(entry)
        canonical = k if k in variants else chosen_doi.get(d, k) if d else k
        if canonical != k:
            aliases[k] = canonical
            entry = re.sub(r'(^@\w+\s*\{\s*)' + re.escape(k) + r'(?=\s*,)',
                           lambda m: m[1] + canonical, entry)
        if d:
            chosen_doi.setdefault(d, canonical)
        bibliography[canonical] = entry
    talks, items, problems, corrections = [rewrite_citations(x, aliases)
                                           for x in (talks, items, problems, corrections)]
    prose_escapes = []
    for records, fields in (
        (talks, ('summary',)),
        (items, ('notes', 'statement', 'reconstruction', 'fate', 'present_status', 'worth')),
        (problems, ('statement', 'status')),
        (corrections, ('place', 'transcription_reads', 'should_read', 'evidence'))):
        for record in records:
            changed = normalize_record(record, fields)
            if changed:
                prose_escapes.append({'identifier': record.get('id', record.get('record', record.get('page'))),
                                      'fields': changed})
    order = {t['record']: i for i, t in enumerate(talks)}
    items.sort(key=lambda x: (order[x['record']], int(x['id'].split('.')[1])))
    problems.sort(key=lambda x: x['id'])
    # Exact duplicate rows only; distinct assessments on the same page survive.
    columns = ['page', 'place', 'transcription_reads', 'should_read', 'evidence',
               'applies_to', 'type']
    unique = {tuple(r.get(k, '') for k in columns): r for r in corrections}
    corrections = sorted(unique.values(), key=lambda r: (r['page'], r['place']))
    used = {'mccme2026gelfand'}
    for x in items + problems:
        used.update(x.get('refs', []))
    for x in (talks, items, problems, corrections):
        used.update(cites(json.dumps(x, ensure_ascii=False).replace('\\\\', '\\')))
    for suffix in ('overview.tex', 'development.tex'):
        path = root / ('GY1971_' + suffix)
        if path.exists():
            content = rewrite_citations(path.read_text(), aliases)
            path.write_text(content)
            used.update(cites(content))
    missing = sorted(used - bibliography.keys())
    audit = {'records': len(talks), 'items': len(items), 'problems': len(problems),
             'corrections': len(corrections), 'selected_references': len(used),
             'citation_key_aliases': aliases, 'missing_references': missing,
             'prose_special_character_escapes': prose_escapes,
             'repeated_cumulative_keys_used': {k: len(variants[k]) for k in used
                                              if len(variants.get(k, [])) > 1}}
    (root / 'audit' / 'merge.json').write_text(json.dumps(audit, indent=2) + '\n')
    print(json.dumps(audit, indent=2))
    if missing and not args.allow_missing_bib:
        return 1
    for name, data in (('talks', talks), ('items', items), ('problems', problems)):
        (root / f'GY1971_{name}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    with (root / 'GY1971_corrections.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(corrections)
    (root / 'GY1971_references.bib').write_text('\n\n'.join(bibliography[k] for k in sorted(used)
                                                           if k in bibliography) + '\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
