#!/usr/bin/env python3
"""Compute additive report tables and source coverage from the final data."""
from pathlib import Path
from collections import Counter,defaultdict
import argparse
import csv
import json
import re

AREA_GROUPS={
    'Representation theory and homological algebra':[561,566,574,575,580,581,582,584],
    'Quantum field theory, strings, and conformal theory':[562,563,565,567,569,571,572,573,576,577,578],
    'Dynamical systems and perturbation theory':[564,585],
    'Symplectic and integral geometry, and localization':[568,570,583,593,596],
    'Integrable systems and Hamiltonian methods':[586,588,589,591,592,594],
    'Spectral analysis and index theory':[587,590],
    'Arithmetic geometry and zeta functions':[595,598],
}
CLASS_NAMES={
    'A':'Speaker-associated near-contemporary publication',
    'B':'Established later development by others',
    'C':'Specified partial resolution',
    'D':'Documented lack of development',
    'E':'Known before the talk',
    'F':'Formulation or identification unresolved',
}


def table(headings,rows):
    return '\n'.join(['| '+' | '.join(headings)+' |',
                      '| '+' | '.join('---' for _ in headings)+' |']+
                     ['| '+' | '.join(str(x) for x in row)+' |' for row in rows])


def source_pages(text):
    matches=[int(m) for m in re.findall(r'P(\d{6})',text)]
    if len(matches)==2:
        return list(range(matches[0],matches[1]+1))
    return matches


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory',type=Path,nargs='?',default=Path('.'))
    args=parser.parse_args()
    root=args.directory
    talks=json.loads((root/'GY1982_talks.json').read_text())
    items=json.loads((root/'GY1982_items.json').read_text())
    problems=json.loads((root/'GY1982_problems.json').read_text())
    counts=Counter(x['class'] for x in items)
    by_record=Counter(x['record'] for x in items)
    areas={str(r):area for area,records in AREA_GROUPS.items() for r in records}
    areas['579']='Editorial heading'
    if set(map(int,areas))!=set(t['record'] for t in talks):
        raise ValueError('Area table must cover every catalog record exactly once.')
    by_area=Counter()
    for x in items:by_area[areas[str(x['record'])]]+=1
    by_speaker=Counter()
    speaker_records=Counter()
    for t in talks:
        if t['kind']=='heading':continue
        by_speaker[t['speaker']]+=by_record[t['record']]
        speaker_records[t['speaker']]+=1
    statistics={'items':len(items),'class_counts':{c:counts[c] for c in 'ABCDEF'},
                'by_speaker':dict(sorted(by_speaker.items())),
                'by_area':dict(by_area),'area_rule':'One primary reporting area per record; interventions stay within that record.',
                'previous_problem_ids':[p['id'] for p in problems if not p['id'].startswith('GP-1982-')]}
    tables={
        'CLASS_TABLE':table(['Class','Meaning','Items','Share'],
                           [(c,CLASS_NAMES[c],counts[c],f'{counts[c]/len(items):.1%}') for c in 'ABCDEF']+
                           [('Total','',len(items),'100%')]),
        'SPEAKER_TABLE':table(['Catalog speaker','Records','Items'],
                             [(s,speaker_records[s],by_speaker[s]) for s in sorted(by_speaker)]+
                             [('Total mathematical records',sum(speaker_records.values()),len(items))]),
        'AREA_TABLE':table(['Primary reporting area','Records','Items'],
                          [(area,len(records),by_area[area]) for area,records in AREA_GROUPS.items()]+
                          [('Total',sum(len(rs) for rs in AREA_GROUPS.values()),len(items))]),
    }
    axes=[]
    for field,label in [('literal_correctness','Literal correctness'),
                        ('publication_match','Publication match'),
                        ('verification','Verification'),('development','Development'),
                        ('confidence','Confidence')]:
        axis=Counter(x[field] for x in items)
        axes.append(table([label,'Items'],sorted(axis.items())))
    tables['AXIS_TABLES']='\n\n'.join(axes)
    earlier=[]
    for p in problems:
        previous=[i for i in p['occurrences'] if not i.startswith('1982-')]
        if previous:
            current=[i for i in p['occurrences'] if i.startswith('1982-')]
            earlier.append([p['id'],p['title'],', '.join(previous),', '.join(current)])
    tables['EARLIER_PROBLEMS']=table(['Reused ID','Question','Earlier occurrences','This year'],earlier)
    coverage=defaultdict(list)
    source_map=[]
    for talk in talks:
        group=[x for x in items if x['record']==talk['record']]
        spans=[]
        for x in group:
            spans.append({'item':x['id'],'source':x['pages']})
            for page in source_pages(x['pages']):coverage[page].append(x['id'])
        source_map.append({'record':talk['record'],'catalog_pages':talk['pages'],'item_spans':spans})
    coverage_report={'mathematical_page_range':'P001026-P001114',
                     'covered_pages':len(coverage),
                     'uncovered_pages':[f'P{n:06d}' for n in range(1026,1115) if n not in coverage],
                     'out_of_year_item_pages':[f'P{n:06d}' for n in coverage if not 1026<=n<=1114],
                     'excluded_boundary_page':'P001115: Deligne, 5 September 1983',
                     'records_in_source_order':source_map,
                     'page_occurrences':{f'P{n:06d}':coverage[n] for n in sorted(coverage)}}
    for name,value in [('area_by_record',areas),('report_statistics',statistics),
                       ('report_tables',tables),('source_coverage',coverage_report)]:
        (root/'code'/f'{name}.json').write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(statistics,ensure_ascii=False,indent=2))
    print('Uncovered source pages:',coverage_report['uncovered_pages'])
    print('Out-of-year item pages:',coverage_report['out_of_year_item_pages'])


if __name__=='__main__':
    main()
