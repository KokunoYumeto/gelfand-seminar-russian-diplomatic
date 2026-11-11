"""Small brace-aware BibTeX reader used for this chapter's bibliography audit.

The supplied entries use literal braced/quoted values, not string macros.
Repeated fields are retained in the diagnostic list and resolved to the last
value (the current-run verification annotation) on serialization.
"""
import re
import unicodedata


def entries(text):
    out = []
    for m in re.finditer(r'(?m)^@(\w+)\s*\{\s*([^,]+),', text):
        i, start = m.end(), m.start()
        fields, duplicates = {}, []
        while i < len(text):
            while i < len(text) and (text[i].isspace() or text[i] == ','):
                i += 1
            if text[i] == '}':
                i += 1
                break
            fm = re.match(r'(\w+)\s*=\s*', text[i:])
            if not fm:
                raise ValueError(f'Bad field in {m.group(2)} near {text[i:i+70]!r}')
            name = fm.group(1).lower()
            i += fm.end()
            val_start = i
            if text[i] == '{':
                depth = 1
                i += 1
                while depth:
                    if text[i] == '{' and text[i-1] != '\\':
                        depth += 1
                    if text[i] == '}' and text[i-1] != '\\':
                        depth -= 1
                    i += 1
            elif text[i] == '"':
                i += 1
                while not (text[i] == '"' and text[i-1] != '\\'):
                    i += 1
                i += 1
            else:
                while i < len(text) and text[i] not in ',}\n':
                    i += 1
            if name in fields:
                duplicates.append(name)
            fields[name] = text[val_start:i].strip()
        out.append(dict(kind=m.group(1), key=m.group(2).strip(), fields=fields,
                        duplicates=duplicates, original=text[start:i]))
    return out


def value(entry, field):
    return entry['fields'].get(field, '').strip().strip('{}"')


def canonical_text(text):
    text = unicodedata.normalize('NFKD', text).lower()
    return re.sub(r'[^a-z0-9]', '', text)


def doi(entry):
    text = value(entry, 'doi').lower().strip()
    if not text:
        url = value(entry, 'url').lower()
        m = re.search(r'(10\.\d{4,9}/[^\s{}]+)', url)
        text = m.group(1) if m else ''
    return re.sub(r'^https?://(?:dx\.)?doi\.org/', '', text)


def serialize(entry):
    fields = ',\n'.join(f'  {k} = {v}' for k, v in entry['fields'].items())
    return f"@{entry['kind']}{{{entry['key']},\n{fields}\n}}\n"


if __name__ == '__main__':
    from pathlib import Path
    root = Path(__file__).resolve().parent
    old = entries((root/'references_cumulative.bib').read_text())
    first = {}
    for e in old:
        first.setdefault(e['key'], e)
    by_doi, by_title = {}, {}
    for e in first.values():
        if doi(e): by_doi.setdefault(doi(e), e['key'])
        by_title.setdefault(canonical_text(value(e, 'title')), e['key'])
    for part in 'abcd':
        p = root/'parts'/part/'references.bib'
        if not p.exists(): continue
        for e in entries(p.read_text()):
            if e['duplicates']:
                print('DUPLICATE FIELD', part, e['key'], e['duplicates'])
            if e['key'] in first: continue
            k = by_doi.get(doi(e)) or by_title.get(canonical_text(value(e, 'title')))
            if k: print('REUSE', part, e['key'], '->', k)
    print('AUDIT parsed', len(old), 'cumulative entries;',len(first),'unique keys.')
