#!/usr/bin/env python3
"""Make a page/record/item crosswalk, including the three year-boundary pages."""
from pathlib import Path
import csv
import hashlib
import json
import re
from audit_chapter import page_numbers

D=Path(__file__).resolve().parent.parent
items=json.loads((D/'GY1979_items.json').read_text())
talks=json.loads((D/'GY1979_talks.json').read_text())
rows=[]
for p in range(840,919):
    occurrences=[x['id'] for x in items if p in page_numbers(x['pages'])]
    records=[str(t['record']) for t in talks if p in page_numbers(t['pages'])]
    if p==840:
        disposition='Prior-year carry-in; already indexed, not duplicated'
        boundary='1978-460.12--1978-460.20; see boundary inventory'
    elif p>=917:
        disposition='September 1980 carry-out; outside records 462--488'
        boundary='22 September 1980; see boundary inventory'
    else:
        disposition='Current academic-year content'
        boundary=''
    rows.append({'source_page':f'P{p:06d}', 'disposition':disposition,
                 'record_source_ranges':'; '.join(records),
                 'occurrences_on_page':'; '.join(occurrences),
                 'boundary_note':boundary})
with (D/'code/source_coverage.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
uncovered=[r['source_page'] for r in rows if r['disposition']=='Current academic-year content'
           and not r['occurrences_on_page']]
result={'page_envelope':79,'current_year_pages':76,'boundary_pages':3,
        'current_pages_without_item_pointer':uncovered,
        'note':'Page pointers index source content; adjoining catalog envelopes are not independent evidence of speaker attribution.'}
(D/'code/source_coverage_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
