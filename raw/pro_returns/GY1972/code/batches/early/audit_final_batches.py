"""Read-only schema, citation, status, and editorial-marker audit of all batches."""
from pathlib import Path
import collections
import csv
import hashlib
import json
import re

BASE = Path(__file__).resolve().parents[1]
REQUIRED = set("id record pages kind title notes statement reconstruction class fate present_status literal_correctness publication_match verification development problem worth refs confidence".split())
ENUMS = {
    "kind": set("definition construction theorem claim conjecture question problem method remark".split()),
    "class": set("ABCDEF"),
    "literal_correctness": {"correct", "correct with missing hypotheses", "false as written", "not determinable"},
    "publication_match": {"exact", "partial", "thematic only", "none found"},
    "verification": {"read the result", "publisher metadata checked", "indirect", "unresolved lead"},
    "development": {"none", "annotated", "developed in this chapter"},
    "confidence": {"high", "medium", "low"},
}
CITE = re.compile(r"\\cite[A-Za-z]*\*?(?:\[[^\]]*\]){0,2}\{([^}]+)\}")
MARKER = re.compile(r"\\ours(?:Computed)?\b")
DATE = re.compile(r"(?:9 November 2026|November 2026|2026-11(?:-09)?)")
SELF_WORK = re.compile(r"\b(?:independent(?:ly)?|counterexample|elementary editorial verification|direct check|our proof|we prove|we compute|computed|recomputed|exact rational|re-derive|rederive|rerun|re-run)\b", re.I)


def bib_entries(text):
    starts = list(re.finditer(r"(?m)^\s*@([A-Za-z]+)\s*\{\s*([^,\s]+)\s*,", text))
    entries = []
    for i, start in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(text)
        block = text[start.end():end]
        fields = {}
        for hit in re.finditer(r"(?m)(?:^|,)\s*([A-Za-z_]+)\s*=\s*([\{\"])", block):
            pos = hit.end()
            if hit.group(2) == '"':
                stop = pos
                while stop < len(block) and (block[stop] != '"' or block[stop - 1] == '\\'):
                    stop += 1
            else:
                depth, stop = 1, pos
                while stop < len(block) and depth:
                    char = block[stop]
                    if char == '{' and (stop == 0 or block[stop-1] != '\\'):
                        depth += 1
                    elif char == '}' and (stop == 0 or block[stop-1] != '\\'):
                        depth -= 1
                    if depth:
                        stop += 1
            fields[hit.group(1).lower()] = block[pos:stop].strip()
        entries.append((start.group(2), fields))
    return entries


errors, warnings, review, batch_counts = [], [], [], {}
all_items, all_talks, all_problems, all_bib = {}, {}, {}, collections.defaultdict(list)
hashes = {}
for batch in sorted(p for p in BASE.iterdir() if p.is_dir() and (p / 'items.json').exists()):
    prefix = batch.name
    payloads = {}
    for name in ('items.json', 'talks.json', 'problems.json'):
        data = (batch / name).read_bytes()
        hashes[f'{prefix}/{name}'] = hashlib.sha256(data).hexdigest()
        payloads[name] = json.loads(data)
        if not isinstance(payloads[name], list):
            errors.append(f'{prefix}/{name}: root is not an array')
    bibliography = (batch / 'references.bib').read_text()
    entries = bib_entries(bibliography)
    keys = [key for key, fields in entries]
    for key, count in collections.Counter(keys).items():
        if count > 1:
            errors.append(f'{prefix}: bibliography key {key} duplicated {count} times')
    for key, fields in entries:
        all_bib[key].append((prefix, fields))
        if not (fields.get('url') or fields.get('doi')):
            errors.append(f'{prefix}: {key} has no parsed url or doi')
        if fields.get('note') not in ('verified', 'unverified'):
            warnings.append(f'{prefix}: {key} note is {fields.get("note")!r}')
    batch_counts[prefix] = {'items': len(payloads['items.json']), 'talks': len(payloads['talks.json']),
                            'problems': len(payloads['problems.json']), 'bib_keys': len(keys),
                            'classes': dict(collections.Counter(x.get('class') for x in payloads['items.json']))}
    record_ids = collections.defaultdict(list)
    for item in payloads['items.json']:
        ident = item.get('id', '<missing>')
        tag = f'{prefix}/{ident}'
        missing = REQUIRED - item.keys()
        if missing:
            errors.append(f'{tag}: missing fields {sorted(missing)}')
        extra = item.keys() - REQUIRED - {'speaker'}
        if extra:
            warnings.append(f'{tag}: additional fields {sorted(extra)}')
        for field in REQUIRED - {'record', 'refs'}:
            if field in item and not isinstance(item[field], str):
                errors.append(f'{tag}: {field} is not a string')
        if not isinstance(item.get('record'), int):
            errors.append(f'{tag}: record not integer')
        refs = item.get('refs')
        if not isinstance(refs, list) or not all(isinstance(x, str) for x in refs):
            errors.append(f'{tag}: refs is not a list of strings')
            refs = []
        for field, allowed in ENUMS.items():
            if item.get(field) not in allowed:
                errors.append(f'{tag}: invalid {field}={item.get(field)!r}')
        for field in ('pages', 'title', 'notes', 'statement', 'fate', 'present_status'):
            if not item.get(field, '').strip():
                errors.append(f'{tag}: empty {field}')
        if not DATE.search(item.get('present_status', '')):
            errors.append(f'{tag}: status lacks November 2026 date')
        if item.get('class') in ('C', 'D') and not item.get('worth', '').strip():
            errors.append(f'{tag}: C/D item lacks worth statement')
        if ident in all_items:
            errors.append(f'{tag}: globally duplicated occurrence ID')
        all_items[ident] = item
        m = re.fullmatch(r'1972-(\d+)\.(\d+)', ident)
        if not m or int(m.group(1)) != item.get('record'):
            errors.append(f'{tag}: malformed/mismatched occurrence ID')
        else:
            record_ids[item['record']].append(int(m.group(2)))
        cited = set()
        combined = '\n'.join(v for v in item.values() if isinstance(v, str))
        for hit in CITE.finditer(combined):
            cited.update(k.strip() for k in hit.group(1).split(','))
        for key in cited - set(refs):
            errors.append(f'{tag}: citation {key} missing from refs')
        for key in set(refs) - set(keys):
            errors.append(f'{tag}: refs key {key} missing from local bibliography')
        if len(refs) != len(set(refs)):
            warnings.append(f'{tag}: duplicate refs')
        if item.get('class') != 'F' and not refs:
            warnings.append(f'{tag}: non-F item has no references')
        if item.get('development') == 'developed in this chapter' and not MARKER.search(combined):
            review.append({'id': tag, 'reason': 'developed item without inline ours marker', 'text': item.get('reconstruction', '')})
        reconstruction = item.get('reconstruction', '')
        if SELF_WORK.search(reconstruction) and not MARKER.search(combined):
            review.append({'id': tag, 'reason': 'possible original work without ours marker', 'text': reconstruction})
        controls = sorted(set(ord(c) for c in combined if ord(c) < 32 and c not in '\n\r\t'))
        if controls:
            errors.append(f'{tag}: control characters {controls}')
        for left, right in ((r'\(', r'\)'), (r'\[', r'\]')):
            if combined.count(left) != combined.count(right):
                errors.append(f'{tag}: unequal {left}/{right} math delimiters')
    for record, seq in record_ids.items():
        if sorted(seq) != list(range(1, len(seq) + 1)):
            errors.append(f'{prefix}: record {record} has nonconsecutive IDs {seq}')
    for talk in payloads['talks.json']:
        record = talk.get('record')
        if record in all_talks:
            errors.append(f'{prefix}: globally duplicated talk {record}')
        all_talks[record] = talk
        missing = set('record date speaker pages title kind summary'.split()) - talk.keys()
        if missing:
            errors.append(f'{prefix}/talk{record}: missing {sorted(missing)}')
        if talk.get('kind') not in ('talk', 'plan', 'heading', 'other'):
            errors.append(f'{prefix}/talk{record}: invalid kind {talk.get("kind")!r}')
    for problem in payloads['problems.json']:
        ident = problem.get('id')
        if ident in all_problems:
            warnings.append(f'{prefix}: problem {ident} appears in multiple batches; reconcile at merge')
        all_problems[ident] = problem
        missing = set('id title statement occurrences status status_date refs'.split()) - problem.keys()
        if missing:
            errors.append(f'{prefix}/{ident}: problem fields missing {sorted(missing)}')
        if not str(problem.get('status_date', '')).startswith('2026-11'):
            errors.append(f'{prefix}/{ident}: wrong/missing problem status date')
        for key in problem.get('refs', []):
            if key not in keys:
                errors.append(f'{prefix}/{ident}: problem key {key} missing from local bibliography')

for ident, item in all_items.items():
    if item['record'] not in all_talks:
        errors.append(f'{ident}: no corresponding talk')
    problem = item.get('problem')
    if problem:
        if problem not in all_problems:
            errors.append(f'{ident}: missing problem-index object {problem}')
        elif ident not in all_problems[problem].get('occurrences', []):
            errors.append(f'{ident}: missing from problem {problem} occurrences')
for pid, problem in all_problems.items():
    for ident in problem.get('occurrences', []):
        if ident.startswith('1972-') and ident not in all_items:
            warnings.append(f'{pid}: 1972 occurrence {ident} absent (check prior-chapter carryover)')
        elif ident in all_items and all_items[ident].get('problem') != pid:
            errors.append(f'{pid}: occurrence {ident} has nonreciprocal problem link')

# Only DOI/title differences for the same key are flagged.  Abstract fields may
# legitimately contain batch-specific access/verification notes.
for key, records in all_bib.items():
    if len(records) > 1:
        for field in ('doi', 'title', 'year'):
            values = {f.get(field, '').strip().lower() for batch, f in records if f.get(field)}
            if len(values) > 1:
                warnings.append(f'shared key {key} has differing {field}: {sorted(values)}')

out = {'batches': batch_counts, 'total_items': len(all_items), 'total_talks': len(all_talks),
       'classes': dict(collections.Counter(x['class'] for x in all_items.values())),
       'errors': errors, 'warnings': warnings, 'editorial_marker_review': review,
       'source_sha256': hashes}
destination = Path(__file__).with_name('final_batch_audit.json')
destination.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: out[k] for k in ('batches', 'total_items', 'total_talks', 'classes', 'errors', 'warnings', 'editorial_marker_review')}, ensure_ascii=False, indent=2))
