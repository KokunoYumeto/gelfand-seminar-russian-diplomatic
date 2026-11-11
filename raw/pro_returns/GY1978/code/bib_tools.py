"""Brace-aware BibTeX inventory and cumulative-key comparison (standard library)."""
from pathlib import Path
import re, json


def entries(text):
    result = []
    pos = 0
    pat = re.compile(r'@(\w+)\s*([\{(])\s*([^,\s]+)\s*,')
    while match := pat.search(text, pos):
        opener = match.group(2)
        closer = '}' if opener == '{' else ')'
        depth = 1
        i = match.end()
        while i < len(text) and depth:
            c = text[i]
            if c == '\\':
                i += 2
                continue
            if c == opener:
                depth += 1
            elif c == closer:
                depth -= 1
            i += 1
        if depth:
            raise ValueError(f'Unbalanced entry {match.group(3)}')
        block = text[match.start():i]
        fields = {}
        fp = re.compile(r'\s*,?\s*([a-zA-Z_]+)\s*=\s*([\{"])')
        field_pos = match.end() - match.start()
        while f := fp.match(block, field_pos):
            j = f.end()
            start = j
            if f.group(2) == '{':
                level = 1
                while j < len(block) and level:
                    if block[j] == '\\':
                        j += 2
                        continue
                    level += (block[j] == '{') - (block[j] == '}')
                    j += 1
                fields[f.group(1).lower()] = block[start:j-1]
            else:
                while j < len(block) and block[j] != '"':
                    j += 2 if block[j] == '\\' else 1
                fields[f.group(1).lower()] = block[start:j]
                j += 1
            field_pos = j
        result.append({'key': match.group(3), 'type': match.group(1), 'text': block, 'fields': fields})
        pos = i
    return result


def normalized(value):
    return re.sub(r'[^a-z0-9]', '', value.lower())


