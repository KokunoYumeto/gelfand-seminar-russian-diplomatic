#!/usr/bin/env python3
"""Additional semantic/schema checks, complementing the supplied chapter builder.

Usage: python code/audit_data.py [chapter-directory]
This checks data consistency, not the truth of historical or mathematical claims.
"""
import collections
import csv
import json
import pathlib
import re
import sys


def bib_entries(text):
    entries = {}
    for m in re.finditer(r'(?m)^@(\w+)\s*\{\s*([^,\s]+)\s*,', text):
        start = text.index('{', m.start())
        depth = 0
        escaped = False
        for end in range(start, len(text)):
            ch = text[end]
            if escaped:
                escaped = False
                continue
            if ch == '\\':
                escaped = True
            elif ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    break
        else:
            raise ValueError('Unbalanced BibTeX entry: ' + m.group(2))
        key = m.group(2)
        if key in entries:
            raise ValueError('Duplicate BibTeX key: ' + key)
        entries[key] = text[m.start():end + 1]
    return entries


def cites(s):
    groups = re.findall(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}', s)
    return {k.strip() for g in groups for k in g.split(',') if k.strip()}


def main():
    root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parents[1]
    tag = 'GY1971'
    talks = json.loads((root / f'{tag}_talks.json').read_text())
    items = json.loads((root / f'{tag}_items.json').read_text())
    problems = json.loads((root / f'{tag}_problems.json').read_text())
    bib = bib_entries((root / f'{tag}_references.bib').read_text())
    corrections = list(csv.DictReader((root / f'{tag}_corrections.csv').open()))
    errors = []
    expected = set(range(229, 272)) | {286, 288}
    actual = {t['record'] for t in talks}
    if actual != expected or len(talks) != 45:
        errors.append(f'Record coverage mismatch: missing={expected-actual}, extra={actual-expected}')
    item_keys = {'id','record','pages','kind','title','notes','statement','reconstruction',
                 'class','fate','present_status','literal_correctness','publication_match',
                 'verification','development','problem','worth','refs','confidence'}
    enums = {
        'kind': {'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
        'class': set('ABCDEF'),
        'literal_correctness': {'correct','correct with missing hypotheses','false as written','not determinable'},
        'publication_match': {'exact','partial','thematic only','none found'},
        'verification': {'read the result','publisher metadata checked','indirect','unresolved lead'},
        'development': {'none','annotated','developed in this chapter'},
        'confidence': {'high','medium','low'},
    }
    by_id = {x['id']:x for x in items}
    if len(by_id) != len(items):
        errors.append('Duplicate occurrence identifiers')
    by_record = collections.defaultdict(list)
    for x in items:
        by_record[x['record']].append(x)
        missing = item_keys - set(x)
        if missing:
            errors.append(f'{x["id"]}: missing {sorted(missing)}')
        for key, values in enums.items():
            if x.get(key) not in values:
                errors.append(f'{x["id"]}: invalid {key}={x.get(key)!r}')
        for key in ('notes','statement','fate','present_status'):
            if not x.get(key, '').strip():
                errors.append(f'{x["id"]}: empty {key}')
        if x.get('class') in {'C','D'} and not x.get('worth','').strip():
            errors.append(f'{x["id"]}: C/D without worth assessment')
        text = '\n'.join(v for v in x.values() if isinstance(v,str))
        if not cites(text) <= set(x.get('refs',[])):
            errors.append(f'{x["id"]}: citations missing from refs: {cites(text)-set(x.get("refs",[]))}')
        if not set(x.get('refs',[])) <= set(bib):
            errors.append(f'{x["id"]}: refs missing from bibliography')
        if not re.search(r'2026|November',x.get('present_status','')):
            errors.append(f'{x["id"]}: undated present status')
        year = 1972 if x['record'] == 288 else 1971
        if not x['id'].startswith(f'{year}-{x["record"]}.'):
            errors.append(f'{x["id"]}: wrong academic-year prefix')
    for t in talks:
        r = t['record']
        if t.get('kind') not in {'talk','plan','heading','other'}:
            errors.append(f'Record {r}: invalid talk kind')
        if t.get('kind') == 'talk' and not by_record[r]:
            errors.append(f'Record {r}: talk has no mathematical item')
        ids = [x['id'] for x in by_record[r]]
        prefix = 1972 if r == 288 else 1971
        if ids != [f'{prefix}-{r}.{i}' for i in range(1,len(ids)+1)]:
            errors.append(f'Record {r}: nonconsecutive or reordered item numbers')
    by_problem = {p['id']:p for p in problems}
    if len(by_problem) != len(problems):
        errors.append('Duplicate problem identifiers')
    previous_path = root / 'code' / 'source_fragments' / 'previous_index.md'
    previous = previous_path.read_text() if previous_path.exists() else ''
    previous_ids = set(re.findall(r'\b\d{4}-\d+\.\d+\b', previous))
    for x in items:
        if x.get('problem'):
            p = by_problem.get(x['problem'])
            if not p or x['id'] not in p['occurrences']:
                errors.append(f'{x["id"]}: problem backlink missing')
    for p in problems:
        for occurrence in p['occurrences']:
            if occurrence.startswith(('1971-','1972-')) and occurrence not in by_id:
                errors.append(f'{p["id"]}: missing current occurrence {occurrence}')
            elif not occurrence.startswith(('1971-','1972-')) and occurrence not in previous_ids:
                errors.append(f'{p["id"]}: earlier occurrence not in supplied index: {occurrence}')
        if p.get('status_date') != '2026-11':
            errors.append(f'{p["id"]}: wrong status date')
        if not cites(p.get('statement','')+' '+p.get('status','')) <= set(p.get('refs',[])):
            errors.append(f'{p["id"]}: citation absent from problem refs')
        if not set(p.get('refs', [])) <= set(bib):
            errors.append(f'{p["id"]}: references missing from bibliography')
        if not p['id'].startswith('GP-1971-') and p['id'] not in previous:
            errors.append(f'{p["id"]}: earlier problem not in supplied index')
    for row in corrections:
        if row.get('applies_to') not in {'ru', 'en', 'both'}:
            errors.append(f'Correction {row.get("page")}: invalid applies_to')
        if row.get('type') not in {'', 'transcription', 'translation', 'ambiguity', 'faithful_error', 'provenance'}:
            errors.append(f'Correction {row.get("page")}: invalid type')
    for key, entry in bib.items():
        if not re.search(r'\b(?:url|doi)\s*=',entry,re.I):
            errors.append(f'{key}: no URL or DOI')
        if not re.search(r'\bnote\s*=\s*\{(?:verified|unverified)\}',entry,re.I):
            errors.append(f'{key}: missing required verification note')
    result = {
        'scope': 'Consistency checks only; source and proof audits are separate.',
        'records': len(talks), 'items':len(items), 'problems':len(problems),
        'references':len(bib), 'corrections':len(corrections),
        'by_class':dict(sorted(collections.Counter(x['class'] for x in items).items())),
        'by_verification':dict(sorted(collections.Counter(x['verification'] for x in items).items())),
        'by_confidence':dict(sorted(collections.Counter(x['confidence'] for x in items).items())),
        'by_record':{str(t['record']):len(by_record[t['record']]) for t in talks},
        'by_talk_kind':dict(collections.Counter(t['kind'] for t in talks)),
        'errors':errors,
    }
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
