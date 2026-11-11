"""Check correction-table math delimiters and unsafe sub/superscripts."""
import csv
from pathlib import Path

root = Path(__file__).resolve().parent
with (root / 'corrections.csv').open(newline='', encoding='utf-8') as handle:
    rows = list(csv.DictReader(handle))

errors = []
checked_fields = 0
for row in rows:
    for field in ('transcription_reads', 'should_read', 'evidence'):
        checked_fields += 1
        text = row[field]
        active = None
        depth = 0
        i = 0
        while i < len(text):
            pair = text[i:i + 2]
            if pair in (r'\(', r'\['):
                if active is not None:
                    errors.append((row['place'], field, 'nested math delimiter'))
                active = pair
                i += 2
                continue
            if pair in (r'\)', r'\]'):
                expected = {r'\)': r'\(', r'\]': r'\['}[pair]
                if active != expected:
                    errors.append((row['place'], field, 'unmatched math delimiter'))
                active = None
                i += 2
                continue
            if text[i] == '\\':
                # Escaped literal, a command prefix, or a matrix row break.
                i += 2
                continue
            if text[i] in '_^' and active is None:
                errors.append((row['place'], field, f'outside-math {text[i]}'))
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
                if depth < 0:
                    errors.append((row['place'], field, 'unmatched closing brace'))
            i += 1
        if active is not None:
            errors.append((row['place'], field, 'unclosed math delimiter'))
        if depth != 0:
            errors.append((row['place'], field, 'unbalanced braces'))

assert len(rows) == 39, f'Correction count changed: {len(rows)}'
for error in errors:
    print(error)
assert not errors, f'{len(errors)} correction-table LaTeX errors'
print(f'{len(rows)} rows, {checked_fields} prose fields checked.')
print('0 outside-math underscores/carets; all math delimiters and braces balanced.')
