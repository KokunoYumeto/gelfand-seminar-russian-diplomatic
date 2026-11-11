#!/usr/bin/env python3
"""Additional semantic/schema checks beyond the supplied chapter builder.

Run from the extracted archive: python code/chapter_checks.py .
This validates the final data, counts records and assessment axes, checks
current-year and problem links, and records statistics used in the report.
"""
from pathlib import Path
import collections
import csv
import json
import re
import sys

TAG = 'GY1982'
EXPECTED = set(range(561,597)) | {598}
AXES = {
    'kind': {'definition','construction','theorem','claim','conjecture','question','problem','method','remark'},
    'class': set('ABCDEF'),
    'literal_correctness': {'correct','correct with missing hypotheses','false as written','not determinable'},
    'publication_match': {'exact','partial','thematic only','none found'},
    'verification': {'read the result','publisher metadata checked','indirect','unresolved lead'},
    'development': {'none','annotated','developed in this chapter'},
    'confidence': {'high','medium','low'},
}


def citations(text):
    matches = re.findall(r'\\cite[tp]?\*?(?:\[[^\]]*\])*\{([^}]+)\}',text)
    return {key.strip() for group in matches for key in group.split(',') if key.strip()}


def latex_text_issues(value):
    """Catch accidental Python escapes and raw superscripts/file underscores."""
    issues=[]
    if any(ord(c)<32 and c!='\n' for c in value):
        issues.append('control character')
    protected=re.sub(r'\\(?:nolinkurl|url|href|label|hyperref|cite[tp]?)\*?(?:\[[^\]]*\])*\{[^}]*\}','',value)
    if re.search(r'(?<!\\)[#%]',protected):
        issues.append('unescaped # or %')
    plain=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]|\\begin\{(?:align\*?|gather\*?|equation\*?)\}.*?\\end\{(?:align\*?|gather\*?|equation\*?)\}', '', protected, flags=re.S)
    if re.search(r'(?<!\\)[_^]',plain):
        issues.append('bare subscript or superscript outside math')
    return issues


def bib_entries(text):
    """Split conventional brace-delimited BibTeX entries, retaining source."""
    entries = {}
    for match in re.finditer(r'@([a-zA-Z]+)\s*\{\s*([^,\s]+)\s*,',text):
        start = match.start()
        i = text.index('{',start)
        depth = 0
        while i < len(text):
            char = text[i]
            escaped = i > 0 and text[i-1] == '\\'
            if char == '{' and not escaped:
                depth += 1
            elif char == '}' and not escaped:
                depth -= 1
                if depth == 0:
                    break
            i += 1
        if i == len(text):
            raise ValueError('Unbalanced bibliography entry '+match[2])
        if match[2] in entries:
            raise ValueError('Duplicate bibliography key '+match[2])
        entries[match[2]] = text[start:i+1]
    return entries


def bib_field(entry,name):
    match = re.search(r'\b'+re.escape(name)+r'\s*=\s*',entry,re.I)
    if not match:
        return ''
    start = match.end()
    if entry[start:start+1] == '{':
        depth = 1
        i = start+1
        while i < len(entry):
            escaped = i > 0 and entry[i-1] == '\\'
            if entry[i] == '{' and not escaped:
                depth += 1
            elif entry[i] == '}' and not escaped:
                depth -= 1
                if depth == 0:
                    return entry[start+1:i]
            i += 1
    elif entry[start:start+1] == '"':
        return re.split(r'(?<!\\)"',entry[start+1:],maxsplit=1)[0]
    return re.split(r'[,\n]',entry[start:],maxsplit=1)[0].strip()


def main(directory):
    d = Path(directory)
    talks = json.loads((d/f'{TAG}_talks.json').read_text())
    items = json.loads((d/f'{TAG}_items.json').read_text())
    problems = json.loads((d/f'{TAG}_problems.json').read_text())
    bibliography = bib_entries((d/f'{TAG}_references.bib').read_text())
    corrections = list(csv.DictReader((d/f'{TAG}_corrections.csv').open()))
    errors = []
    def check(condition,message):
        if not condition:
            errors.append(message)
    records = [t['record'] for t in talks]
    check(len(records)==37 and set(records)==EXPECTED,'The 37 catalog records are not covered exactly once.')
    check(len(set(records))==len(records),'Duplicate record.')
    check(records==list(range(561,593))+[594,593,596,595,598],
          'The complete record sequence must follow the notebook source order.')
    check(records.index(594)<records.index(593),'11 April source order must place Wilson before Ginzburg.')
    check(records.index(596)<records.index(595),'18 April source order must place Ginzburg before Beilinson.')
    catalog_path=d/'research/inputs/GY1982_talks.md'
    catalog_checked=False
    if catalog_path.exists():
        original=catalog_path.read_text()
        pattern=r'record (\d+):.*?\((\d{4}-\d{2}-\d{2}|no date)\); pages (P\d{6}-P\d{6});'
        expected_catalog={int(m[1]):(m[2] if m[2]!='no date' else '',m[3]) for m in re.finditer(pattern,original)}
        check(set(expected_catalog)==EXPECTED,'The supplied catalog metadata did not parse into all 37 records.')
        for talk in talks:
            check((talk['date'],talk['pages'])==expected_catalog.get(talk['record']),
                  f'Record {talk["record"]}: date or catalog page range differs from the supplied catalog.')
        catalog_checked=True
    by_record = collections.defaultdict(list)
    ids = set()
    problems_by_id = {p['id']:p for p in problems}
    check(len(problems_by_id)==len(problems),'Duplicate problem ID.')
    required = ['id','record','pages','kind','title','notes','statement','reconstruction',
                'class','fate','present_status','literal_correctness','publication_match',
                'verification','development','problem','worth','refs','confidence']
    for item in items:
        name = item.get('id','<missing>')
        for field in required:
            check(field in item,f'{name}: missing {field}')
        check(name not in ids,f'Duplicate item {name}')
        ids.add(name)
        check(item.get('record') in EXPECTED,f'{name}: unexpected record')
        by_record[item['record']].append(item)
        check(name.startswith('1982-'),f'{name}: IDs must use the academic-year start, 1982')
        for field,values in AXES.items():
            check(item.get(field) in values,f'{name}: invalid {field}: {item.get(field)}')
        if item.get('class') in {'C','D'}:
            check(bool(item.get('worth')),f'{name}: C/D requires an assessment of development value')
        if item.get('problem'):
            check(item['problem'] in problems_by_id,f'{name}: missing problem object')
            if item['problem'] in problems_by_id:
                check(name in problems_by_id[item['problem']]['occurrences'],f'{name}: problem back-link missing')
        item_cites = citations(' '.join(v for v in item.values() if isinstance(v,str)))
        check(item_cites <= set(item.get('refs',[])),f'{name}: cited keys missing from refs: {item_cites-set(item.get("refs",[]))}')
        check(set(item.get('refs',[])) <= set(bibliography),f'{name}: reference key absent from bibliography')
        check('P001115' not in item.get('pages',''),f'{name}: next academic-year page must not be assigned a mathematical item')
        for field,value in item.items():
            if isinstance(value,str):
                check(not any(ord(c)<32 and c != '\n' for c in value),f'{name}: control character in {field}')
        for field in ['notes','statement','reconstruction','fate','present_status','worth']:
            for issue in latex_text_issues(item.get(field,'')):
                check(False,f'{name}.{field}: {issue}')
        check('2026' in item.get('present_status',''),f'{name}: present status needs an explicit date')
    for record,group in by_record.items():
        check([x['id'] for x in group]==[f'1982-{record}.{i}' for i in range(1,len(group)+1)],f'Record {record}: nonconsecutive item IDs')
    for talk in talks:
        check(talk.get('kind') in {'talk','plan','heading','other'},f'Record {talk["record"]}: invalid kind')
        if talk.get('kind')=='talk':
            check(bool(by_record[talk['record']]),f'Record {talk["record"]}: talk with no items')
    for problem in problems:
        for occurrence in problem['occurrences']:
            if occurrence.startswith('1982-'):
                check(occurrence in ids,f'{problem["id"]}: unknown current occurrence {occurrence}')
        check(problem['status_date']=='2026-11',f'{problem["id"]}: inconsistent status month')
        pc = citations(problem['statement']+' '+problem['status'])
        check(pc<=set(problem['refs']),f'{problem["id"]}: problem refs do not include citations')
        check(set(problem['refs'])<=set(bibliography),f'{problem["id"]}: reference key absent from bibliography')
        for field in ['statement','status']:
            for issue in latex_text_issues(problem[field]):
                check(False,f'{problem["id"]}.{field}: {issue}')
    for n,row in enumerate(corrections,2):
        check(row.get('applies_to') in {'ru','en','both'},f'corrections row {n}: invalid applies_to')
        check(row.get('type') in {'transcription','translation','ambiguity','faithful_error','provenance'},f'corrections row {n}: invalid type')
        for field in ['place','transcription_reads','should_read','evidence']:
            for issue in latex_text_issues(row[field]):
                check(False,f'corrections row {n}.{field}: {issue}')
    all_cites = set()
    for suffix in ['overview.tex','development.tex']:
        source=(d/f'{TAG}_{suffix}').read_text()
        check(not re.search(r'@@[A-Z_]+@@',source),suffix+': unresolved template placeholder')
        all_cites |= citations(source)
    for container in [talks,items,problems,corrections]:
        for obj in container:
            all_cites |= citations(' '.join(x for x in obj.values() if isinstance(x,str)))
    check(all_cites<=set(bibliography),'Missing globally cited bibliography entries: '+str(all_cites-set(bibliography)))
    for key,entry in bibliography.items():
        check(bool(bib_field(entry,'url') or bib_field(entry,'doi')),key+': bibliography needs URL or DOI')
        check(bib_field(entry,'note').strip() in {'verified','unverified'},key+': missing verification note')
    stats = {
        'records':len(talks),'items':len(items),'problems':len(problems),'references':len(bibliography),
        'corrections':len(corrections),'class_counts':dict(sorted(collections.Counter(x['class'] for x in items).items())),
        'record_kinds':dict(collections.Counter(t['kind'] for t in talks)),
        'by_record':{str(t['record']):len(by_record[t['record']]) for t in talks},
        'by_catalog_speaker':dict(collections.Counter({speaker:sum(len(by_record[t['record']]) for t in talks if t['speaker']==speaker) for speaker in {t['speaker'] for t in talks}})),
        'assessment_axes':{field:dict(collections.Counter(x[field] for x in items)) for field in AXES},
        'correction_types':dict(collections.Counter(x['type'] for x in corrections)),
        'source_order':records,'supplied_catalog_dates_and_ranges_checked':catalog_checked,'errors':errors,
    }
    (d/'code'/'validation_statistics.json').write_text(json.dumps(stats,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(stats,indent=2,ensure_ascii=False))
    print('PASS: all additional checks.' if not errors else 'FAIL: '+str(len(errors))+' errors.')
    return bool(errors)


if __name__=='__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv)>1 else '.'))
