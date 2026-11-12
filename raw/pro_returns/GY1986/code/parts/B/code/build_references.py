"""Reuse exact cumulative keys and add the independently researched references."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[3]
B = ROOT / 'parts/B'
required = {key for filename in ('items.json', 'problems.json')
            for row in json.loads((B / filename).read_text())
            for key in row['refs']}

def entries(text):
    result = {}
    for match in re.finditer(r'@\w+\s*\{\s*([^,\s]+)\s*,', text):
        start = text.find('{', match.start())
        level = 0
        for end in range(start, len(text)):
            if text[end] == '{':
                level += 1
            elif text[end] == '}':
                level -= 1
                if level == 0:
                    result[match.group(1)] = text[match.start():end + 1]
                    break
        else:
            raise ValueError('Unbalanced entry: ' + match.group(1))
    return result

cumulative = entries((ROOT / 'work/references_cumulative.bib').read_text())
new = entries((B / 'code/new_references.bib').read_text())
assert not (new.keys() & cumulative.keys()), 'New keys must reuse the existing entry'
out = {}
for key in sorted(required):
    out[key] = cumulative[key] if key in cumulative else new[key]

# These annotations describe our actual use in this slice, rather than carrying
# forward a verification claim or an unrelated application from an earlier year.
annotations = {
    'berezingelfand1956spherical':
        'Primary Math-Net metadata opened in this slice; original Russian proof not reread. Historical attribution of orbital integration is partial, not an assertion that the notebook formula appears verbatim in this paper.',
    'gelfandshilov1964generalized':
        'English-edition catalogue and authorized MCCME Russian-book contents opened; exact relevant chapter text was not retrieved. Russian first edition 1958, English 1964. Homogeneous distributions and analytic continuation provide context; the directly supplied Gaussian-mixture positivity calculation is marked ours.',
    'collinssniady2006integration':
        'Full primary arXiv paper read, especially section 2, Corollary 2.4, including the unrestricted finite-N interpretation. First posted 26 February 2004; publication 2006. The companion applies the polynomial moment formula to the convergent exponential series and marks its own estimates separately.',
    'ryzhikova1987decidability':
        'Full four-page Russian primary text read: main theorem and Lemmas 1--3. For each fixed field, recognition of identities is decidable; the proof gives a finite-dimensional witness bound and the prime-field reduction. Received 16 May 1986; presented by Gelfand 3 March 1986. These are manuscript dates, not automatically public preprint circulation. English translation 1988. The earlier exact problem GP-1985-20 is distinct from the finite-basis problem indexed here.',
}
def set_field(entry, field, value):
    match = re.search(r'\b' + re.escape(field) + r'\s*=\s*\{', entry)
    if match:
        start = entry.find('{', match.start())
        depth = 0
        for end in range(start, len(entry)):
            if entry[end] == '{':
                depth += 1
            elif entry[end] == '}':
                depth -= 1
                if depth == 0:
                    return entry[:start + 1] + value + entry[end:]
    pos = entry.rfind('}')
    before = entry[:pos].rstrip()
    if not before.endswith(','):
        before += ','
    return before + '\n  ' + field + ' = {' + value + '}\n}'

for key, annotation in annotations.items():
    if key in out:
        out[key] = set_field(out[key], 'annote', annotation)
for key, entry in out.items():
    assert re.search(r'\b(?:url|doi)\s*=', entry), key
    assert re.search(r'\bnote\s*=\s*\{(?:un)?verified\}', entry), key
(B / 'references.bib').write_text(
    '% GY1986 records 682--697; checked 12 November 2026.\n\n'
    + '\n\n'.join(out.values()) + '\n')
print(f'{len(out)} entries; {sum(k in cumulative for k in out)} cumulative keys reused; '
      f'{sum(k in new for k in out)} new entries')
