#!/usr/bin/env python3
"""Derive chapter statistics, source coverage and the final overview/report."""
import collections
import csv
import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parents[1]


def pages(value):
    result = set()
    for start, end in re.findall(r'P0*(\d+)(?:\s*[-–]\s*P0*(\d+))?', value):
        result.update(range(int(start), int(end or start) + 1))
    return result


def speaker(value):
    value = re.sub(r'\s+', ' ', value).strip()
    value = re.sub(r'\s*\(intervention\)', '', value).strip()
    value = re.sub(r';\s*translated by.*$', '', value).strip()
    names = {'Morava':'Jack Morava', 'Birman':'M. Sh. Birman',
             'Kazhdan':'D. A. Kazhdan', 'Vaserstein':'L. N. Vaserstein',
             'Vasserstein':'L. N. Vaserstein', 'Kirillov':'A. A. Kirillov',
             'Atiyah':'M. F. Atiyah', 'Gabrielov':'A. M. Gabrielov',
             'Fuchs':'D. B. Fuchs', 'Fuks':'D. B. Fuchs',
             'Dobrushin':'R. L. Dobrushin', 'Pták':'Vlastimil Pták',
             'Ptak':'Vlastimil Pták'}
    for part, name in names.items():
        if part in value:
            return name
    if 'Gelfand' in value:
        return 'S. I. Gelfand' if value.startswith('S') else 'I. M. Gelfand'
    return value


def area(item):
    r = item['record']
    if r in (229,234): return 'Symplectic and microlocal geometry'
    if r in (231,235): return 'Representation theory and finite geometry'
    if r in (232,236,239,243,244): return 'Differential geometry and foliations'
    if r in (233,237,252,261,263): return 'Operator analysis and scattering'
    if r in (240,241,242): return 'Differential calculus and jets'
    if r in (246,247,249,250,253,256,257,258,259):
        if item['id'] == '1971-246.9': return 'Number theory, lattices and modular forms'
        return 'Algebraic and hermitian K-theory'
    if r in (238,248,251,254,262): return 'Algebraic geometry, Hodge theory and residues'
    if r in (255,260) or item['id'] in ('1971-265.10','1971-265.11'):
        return 'Homotopy theory and group cohomology'
    if r in (265,266,267): return 'Categories, sheaves and homological algebra'
    if r in (268,270): return 'Bordism and formal groups'
    if r == 269:
        return ('Mathematical physics' if item['id'].endswith('.5')
                else 'Number theory, lattices and modular forms')
    if r == 288: return 'Mathematical physics'
    raise ValueError('No area assigned to ' + item['id'])


def table(headers, rows):
    def cell(x): return str(x).replace('|', r'\|').replace('\n',' ')
    return '\n'.join(['| ' + ' | '.join(map(cell, headers)) + ' |',
                      '| ' + ' | '.join('---' for _ in headers) + ' |'] +
                     ['| ' + ' | '.join(map(cell, row)) + ' |' for row in rows])


def write_csv(name, rows, fields):
    with (ROOT/'audit'/name).open('w', newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields)
        w.writeheader(); w.writerows(rows)


def main():
    talks=json.loads((ROOT/'GY1971_talks.json').read_text())
    items=json.loads((ROOT/'GY1971_items.json').read_text())
    problems=json.loads((ROOT/'GY1971_problems.json').read_text())
    corrections=list(csv.DictReader((ROOT/'GY1971_corrections.csv').open()))
    tmap={t['record']:t for t in talks}
    classes=collections.Counter(x['class'] for x in items)
    core=collections.Counter(x['class'] for x in items if x['record']!=288)
    kinds=collections.Counter(t['kind'] for t in talks)
    lead=collections.Counter(speaker(tmap[x['record']]['speaker']) for x in items)
    attributed=collections.Counter(speaker(x.get('speaker') or tmap[x['record']]['speaker']) for x in items)
    speaker_records=collections.defaultdict(list)
    for t in talks:
        if t['kind'] in ('talk','plan'):
            speaker_records[speaker(t['speaker'])].append(t['record'])
    areas=collections.Counter(area(x) for x in items)
    verification=collections.Counter(x['verification'] for x in items)
    correct=collections.Counter(x['literal_correctness'] for x in items)
    match=collections.Counter(x['publication_match'] for x in items)
    confidence=collections.Counter(x['confidence'] for x in items)
    correction_types=collections.Counter(x['type'] for x in corrections)
    by_record=collections.Counter(x['record'] for x in items)
    values={**{c:classes[c] for c in 'ABCDEF'}, 'TOTAL':len(items),
            'HEADINGS':kinds['heading'], 'PLANS':kinds['plan'],
            'CORE':sum(core.values()), 'OUTLIER':len(items)-sum(core.values()),
            'PROBLEMS':len(problems), 'CORRECTIONS':len(corrections),
            'TALKS':kinds['talk'], 'CORE_TALKS':kinds['talk']-1}
    overview=(ROOT/'code'/'overview_template.tex').read_text()
    for key,value in values.items(): overview=overview.replace('@@'+key+'@@',str(value))
    assert '@@' not in overview
    (ROOT/'GY1971_overview.tex').write_text(overview)
    labels={'A':'Published soon after by the speaker or Gelfand',
            'B':'Subsequently developed by others',
            'C':'Partly developed; exact verification limits stated',
            'D':'No development identified after documented searching',
            'E':'Already known or circulated before the talk',
            'F':'Not securely identifiable in the recorded form'}
    sections={
      'CLASS_TABLE':table(['Class','Meaning','Core 1971–72','Requested 1973 record','Total'],
                          [(c,labels[c],core[c],classes[c]-core[c],classes[c]) for c in 'ABCDEF']),
      'SPEAKER_TABLE':table(['Speaker','Catalogue records (including plan)','Items under lead speaker','Items with explicit interventions reassigned'],
                            [(s,', '.join(map(str,speaker_records[s])) or 'intervention only',lead[s],attributed[s])
                             for s in sorted(set(lead)|set(attributed)|set(speaker_records))]),
      'AREA_TABLE':table(['Primary area','Items'],sorted(areas.items(),key=lambda x:(-x[1],x[0]))),
      'RECORD_TABLE':table(['Record','Critical date','Kind','Actual source span / boundary anchor','Items'],
                          [(t['record'],t['date'] or 'undated',t['kind'],t['pages'],by_record[t['record']]) for t in talks]),
      'VERIFICATION_TABLE':table(['Verification level','Items'],verification.items()),
      'CORRECTNESS_TABLE':table(['Literal correctness','Items'],correct.items()),
      'MATCH_TABLE':table(['Publication match','Items'],match.items()),
      'CONFIDENCE_TABLE':table(['Confidence','Items'],confidence.items()),
      'CORRECTION_TABLE':table(['Correction type','Rows'],sorted(correction_types.items())),
      'PROBLEM_TABLE':table(['Problem','Definite question','Occurrences'],
                           [(p['id'],p['title'],', '.join(p['occurrences'])) for p in problems])}
    report=(ROOT/'code'/'report_template.md').read_text()
    for key,value in {**values,**sections}.items(): report=report.replace('@@'+key+'@@',str(value))
    assert '@@' not in report
    (ROOT/'GY1971_report.md').write_text(report)
    source_pages=set(range(358,452))|set(range(477,482))
    excluded={358:'Perelomov carryover, already in 1970-228.',
              359:'Perelomov carryover, already in 1970-228.',
              450:'Gabrielov, 25 September 1972; outside requested record 271 heading.',
              451:'Continuation of Gabrielov, 25 September 1972; unrequested record.',
              477:'Tail of Buchstaber, 20 November 1972; outside requested year heading.',
              478:'Buchstaber, 12 February 1973; unrequested record 287.',
              479:'Continuation of Buchstaber, 12 February 1973; unrequested record 287.',
              481:'Buchstaber, 26 February 1973; unrequested record 289.'}
    rows=[]
    for page in sorted(source_pages):
        occurrences=[x['id'] for x in items if page in pages(x['pages'])]
        substantive=[str(t['record']) for t in talks if t['kind']!='heading' and page in pages(t['pages'])]
        headings=[str(t['record']) for t in talks if t['kind']=='heading' and page in pages(t['pages'])]
        status='boundary context' if page in excluded else 'requested 1973 exception' if page==480 else 'core 1971–72'
        rows.append({'page':f'P{page:06d}','coverage':status,'records':'; '.join(substantive),
                     'catalogue_heading_anchors':'; '.join(headings),'items':'; '.join(occurrences),
                     'boundary_explanation':excluded.get(page,'')})
        assert occurrences or page in excluded, f'Unaccounted substantive page {page}'
        assert not(occurrences and page in excluded),f'Out-of-scope material assigned at {page}'
    write_csv('source_coverage.csv',rows,list(rows[0]))
    catalogue_path=ROOT/'code'/'source_fragments'/'catalogue_records.json'
    catalogue={x['record']:x for x in json.loads(catalogue_path.read_text())}
    boundaries=[{'record':t['record'],'catalogue_date':catalogue[t['record']]['date'],
                 'critical_date':t['date'],'catalogue_span':catalogue[t['record']]['pages'],
                 'critical_span':t['pages'],'kind':t['kind'],'basis':t['summary']}
                for t in talks]
    write_csv('record_boundaries.csv',boundaries,list(boundaries[0]))
    assignments=[{'item':x['id'],'record':x['record'],'primary_area':area(x),
                  'lead_speaker':speaker(tmap[x['record']]['speaker']),
                  'attributed_speaker':speaker(x.get('speaker') or tmap[x['record']]['speaker'])}
                 for x in items]
    write_csv('item_classification.csv',assignments,list(assignments[0]))
    stats={**values,'by_class':dict(classes),'by_area':dict(areas),
           'by_lead_speaker':dict(lead),'by_attributed_speaker':dict(attributed),
           'by_record':dict(by_record),'by_verification':dict(verification),
           'by_literal_correctness':dict(correct),'by_publication_match':dict(match),
           'by_confidence':dict(confidence),'correction_types':dict(correction_types),
           'source_pages':len(source_pages),'core_pages':90,'exception_pages':1,'boundary_context_pages':8}
    (ROOT/'audit'/'statistics.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:stats[k] for k in values},indent=2))


if __name__=='__main__': main()
