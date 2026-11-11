"""Integrate the four independently authored, source-ordered fragments.

Run with optional workspace path; the packaged default uses code/inputs and
code/fragments. This script merges and validates data; it does not infer content.
"""
from pathlib import Path
import collections
import csv
import json
import re
import sys

DEST = Path(__file__).resolve().parents[1]
WORK = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEST / 'code'
FRAG = WORK / 'fragments'
INPUT = WORK / 'source_kit' if (WORK / 'source_kit').exists() else WORK / 'inputs'
CATALOGUE = (WORK / 'upload' / 'GY1967_talks.md' if (WORK / 'upload').exists()
             else INPUT / 'GY1967_talks.md')
audit = DEST / 'audit'
audit.mkdir(exist_ok=True)

def bib_entries(text):
    pattern = r'(?ms)^@\w+\s*\{\s*([^,\s]+)\s*,.*?(?=^@|\Z)'
    return {m.group(1): m.group(0).strip() for m in re.finditer(pattern, text)}

def bib_field(entry, name):
    m = re.search(r'\b'+name+r'\s*=\s*\{([^{}]*)\}', entry, re.I)
    return m.group(1).strip() if m else ''

cumulative = bib_entries((INPUT/'references_cumulative.bib').read_text())
doi_keys = {bib_field(v,'doi').lower():k for k,v in cumulative.items() if bib_field(v,'doi')}
talks, items, problems, corrections = [], [], [], []
references, duplicates, aliases, changes = {}, [], {}, []
for group in ('a','b','c','root'):
    folder = FRAG/group
    talks.extend(json.loads((folder/'talks.json').read_text()))
    items.extend(json.loads((folder/'items.json').read_text()))
    problems.extend(json.loads((folder/'problems.json').read_text()))
    with (folder/'corrections.csv').open(newline='') as file:
        corrections.extend(csv.DictReader(file))
    for key, entry in bib_entries((folder/'references.bib').read_text()).items():
        doi = bib_field(entry,'doi').lower()
        canonical = key if key in cumulative else doi_keys.get(doi,key)
        if canonical != key:
            aliases[key] = canonical
        if canonical in references:
            duplicates.append({'key':canonical,'later_fragment':group})
        else:
            references[canonical] = cumulative.get(canonical,entry.replace('{'+key+',','{'+canonical+',',1))

def clean(value):
    if isinstance(value, list): return [clean(x) for x in value]
    if isinstance(value, dict): return {k:clean(v) for k,v in value.items()}
    if not isinstance(value,str): return value
    value = re.sub(r"(?<=[A-Za-z])\\'s\b", "'s", value)
    for old,new in aliases.items():
        value = re.sub(r'(?<![A-Za-z0-9])'+re.escape(old)+r'(?![A-Za-z0-9])',new,value)
    return value

talks,items,problems,corrections = map(clean,(talks,items,problems,corrections))
cat = {int(m[1]):m[2] for m in re.finditer(r'record (\d+):.*?pages (P\d+-P\d+);',CATALOGUE.read_text())}
for talk in talks:
    expected=cat[talk['record']]
    if talk['pages'] != expected:
        changes.append({'record':talk['record'],'old_pages':talk['pages'],'catalogue_pages':expected})
        talk['pages']=expected

for item in items:
    if item['id']=='1967-145.3': item['development']='developed in this chapter'

# Explicit editorial changes from the independent citation and layout review.
override_file=DEST/'code/editorial_overrides.json'
if override_file.exists():
    overrides=json.loads(override_file.read_text())
    for name,rows in [('items',items),('problems',problems)]:
        for row in rows:
            if row['id'] in overrides.get(name,{}):
                row.update(overrides[name][row['id']])
    problems=[p for p in problems if p['id'] not in overrides.get('remove_problems',[])]

assert len(talks)==43 and {t['record'] for t in talks}==set(range(131,174))
assert [t['record'] for t in talks][32:34] == [164,163]
assert [t['record'] for t in talks][38:40] == [170,169]
for name,data in [('talks',talks),('items',items),('problems',problems)]:
    (DEST/f'GY1967_{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
fields=['page','place','transcription_reads','should_read','evidence','applies_to','type']
corrections.sort(key=lambda r:(int(re.search(r'\d+',r['page'])[0]),r['place']))
with (DEST/'GY1967_corrections.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(corrections)
for document in ('GY1967_overview.tex','GY1967_development.tex'):
    if (DEST/document).exists():
        for group in re.findall(r'\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}', (DEST/document).read_text()):
            for key in group.split(','):
                key=key.strip()
                if key not in references and key in cumulative:
                    references[key]=cumulative[key]

(DEST/'GY1967_references.bib').write_text('\n\n'.join(references[k] for k in sorted(references))+'\n')
result={'records':len(talks),'items':len(items),'classes':dict(sorted(collections.Counter(x['class'] for x in items).items())),
        'problems':len(problems),'corrections':len(corrections),'references':len(references),
        'source_order':[t['record'] for t in talks], 'aliases_to_cumulative':aliases,
        'duplicate_entries_coalesced':duplicates,'catalogue_range_normalizations':changes}
(audit/'integration.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
