"""Export a compact query/source audit without republishing retrieved papers."""
from pathlib import Path
import json
import re
import runpy

B = Path(__file__).resolve().parents[1]
audit = []
def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from strings(v)

for path in sorted((B/'code').glob('search*.json'),
                   key=lambda p:int(p.stem.removeprefix('search'))):
    data=json.loads(path.read_text())
    query=data.get('q',data.get('query',data.get('queries')))
    text='\n'.join(strings(data.get('r',data.get('result',data.get('results',{})))))
    source_records=[]
    for match in re.finditer(r'([^\n]*) \((https?://[^\n]+?)\)\n【([^】]+)】',text):
        title,url,ref=match.groups()
        if '; rewritten summary of ' in url:
            url=url.split(' ; rewritten summary of ')[0]
        source_records.append({'title':title.strip(),'url':url,'retrieval_ref':ref})
    urls=sorted(set(re.findall(r'https?://[^\s<>"{}]+',text)))
    urls=[u.rstrip('.,);\\') for u in urls]
    audit.append({
        'checkpoint':path.name,
        'checked':'2026-11-12',
        'request':query,
        'description':data.get('description',data.get('operation','')),
        'sources':source_records,
        'other_urls':sorted(set(urls)-{s['url'] for s in source_records}),
        'access_error_reported': any(x in text for x in (
            'not accessible via this tool','Internal Error',
            '403 Forbidden','Security checkpoint')),
        'query_logging_limitation':(
            'This checkpoint retained combined results and an operation description, '
            'but not a separate original web-request object.' if query is None else '')
    })
(B/'code/research_queries.jsonl').write_text(
    ''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in audit))

namespace=runpy.run_path(str(B/'code/build_references.py'))
entries=namespace['entries']((B/'references.bib').read_text())
def field(entry,key):
    match=re.search(r'\b'+key+r'\s*=\s*\{',entry)
    if not match:return ''
    start=entry.find('{',match.start());depth=0
    for end in range(start,len(entry)):
        if entry[end]=='{':depth+=1
        elif entry[end]=='}':
            depth-=1
            if depth==0:return entry[start+1:end]
    raise ValueError(key)

lines=[
    '# Evidence log: GY1986 records 682–697',
    '',
    'Status cutoff and source checking date: **12 November 2026**.',
    '',
    'The compact machine-readable query audit is **code/research_queries.jsonl**. '
    'It records each retained search/open/find request, actual returned primary URLs, '
    'retrieval references, and access failures. Raw **code/searchNN.json** files are '
    'internal retrieval checkpoints containing source excerpts; they are not needed '
    'for the reader-facing archive. One combined checkpoint, search31, retains its '
    'operation description and returned sources but not a separate request object.',
    '',
    '## Manuscript provenance and direct visual checks',
    '',
    '| Image | Inspection and consequence |',
    '|---|---|',
    '| P001298 | Text boundary coordinated with the preceding slice: Ginzburg occupies the top, Ovsienko the middle, Kazakov begins below. Catalogue overlap does not determine ownership. |',
    '| P001303 | Direct image inspection confirms D. I. Gurevich and 13 October, conflicting with record 684 catalogue speaker/date. Catalogue fields are preserved and every item uses actual manuscript pages. |',
    '| P001308 | Direct image inspection checks the additive monodromy exponent versus multiplicative Hecke parameter and the hyperelliptic specialization. The parameter identification is flagged as ambiguous rather than silently equating the two alphas. |',
    '| P001313 | Direct image inspection checks the Duistermaat–Heckman display and the attribution of the nilpotent-group speculation to the note-taker. |',
    '| P001318 | Direct image inspection confirms the literal Riccati right-hand side zero. The correction to minus a(x) is a mathematical emendation, independently calculated. |',
    '| P001319 | Direct image inspection confirms Beilinson, 10 November 1986; the coherent continuation through P001321 survives despite the catalogue empty page field. |',
    '| P001325 | Direct image inspection confirms the three angular integrations are written independently and the last eigenvalue is mu. The cyclic constraint and replacement of the last spectral factor are mathematical repairs. |',
    '| P001327 | Direct image inspection confirms finitely many morphisms in the preprojective definition and the omission of indecomposable in the perfect-element definition. Both are faithful mathematical errors, not claimed transcription mistakes. |',
    '| P001329 | Direct image inspection confirms the second Speh exponent n/2−1 and the missing final delta; the correct segment has decrement one. |',
    '',
    'The Russian and English transcriptions were compared throughout the assigned '
    'span; working extracts are **source_ru.tex** and **source_en.tex**. The image review '
    'was concentrated on disputed formulas and attributions, rather than claiming '
    'a complete fresh diplomatic transcription of every page.',
    '',
    '## Reference verification declarations',
    '',
    'Verified in BibTeX means the work or an authoritative publication record was '
    'opened; it does **not** mean every proof was read. Each declaration below states '
    'the actual level. The two entries marked unverified retain access limitations.',
    ''
]
for key,entry in sorted(entries.items()):
    url=field(entry,'url');doi=field(entry,'doi')
    lines += ['### '+key,'',
              '- Link: '+(url or 'https://doi.org/'+doi),
              '- Bibliographic flag: '+field(entry,'note'),
              '- Verification: '+field(entry,'annote'),'']
lines += [
    '## Saved computations and independent checks',
    '',
    '**code/check_annotations.py** and **.out** contain exact integer/rational arithmetic, '
    '80-digit beta-function versus cross-section quadrature, and symbolic operator '
    'identities. The rational coefficient has reduced denominator exactly 5. The '
    'slab probabilities agree with an independent root-agent calculation. The root '
    'agent separately developed and checked quantum-KdV grade-two PBW, Gram, and '
    'singular-vector calculations; this slice independently reviewed the written '
    'irreducible-quotient argument and found no positivity assumption or gap.',
    '',
    '**code/validate_slice.py** and **.out** check coverage, item numbering, every local '
    'problem link, the explicit external GP-1986-60 link, bibliography coverage, '
    'schema enumerations, and balanced inline/display delimiters. Integrated XeLaTeX '
    'and bibliography rendering are performed by the root assembly.',
    '',
    '## Source-access limitations that affect conclusions',
    '',
    '- The 2026 Burau and free-fermion ODE/IM papers were read as recent preprints. '
    'The chapter does not certify their proofs independently or convert their '
    'specific hypotheses into general settled claims.',
    '- The GLP 1987 rank condition on printed page 526 remained unclear in the '
    'available OCR and failed image/download routes. Only r≥7 is used. Unresolved '
    'verification of r=6 is not a claim that r=6 is mathematically open.',
    '- The GLP paper’s comment about r=5 records a 1987 limitation only. A present-day '
    'open status was neither asserted nor inferred from an unsuccessful search.',
    '- Full original proofs were not recovered for every bibliographic reference. '
    'Where a later primary treatment supplies the exact statement, the item '
    'identifies that treatment; metadata-only sources are not assigned unread theorem locators.',
    '- No class-D item was created from failed searching. The twelve class-F items '
    'state the missing data or identification explicitly and do not acquire invented '
    'open-problem identifiers.',
    '',
    'The downloaded Herrmann PDF and its rendered first page in **evidence/** are '
    'temporary verification material. The distributable evidence consists of this '
    'log, URLs, query audit, code, and calculation outputs; redistribution of the '
    'complete source PDF is unnecessary.',
]
(B/'evidence_log.md').write_text('\n'.join(lines)+'\n')
print(f'Wrote compact audit of {len(audit)} research checkpoints and {len(entries)} reference declarations.')
