#!/usr/bin/env python3
"""Read-only cross-slice identity audit; writes results only under parts/A."""
from pathlib import Path
from collections import defaultdict
import importlib.util,json,re

OUT=Path(__file__).resolve().parents[1]
ROOT=OUT.parents[1]
spec=importlib.util.spec_from_file_location('root_assembly',ROOT/'deliverable/code/root/assemble_chapter.py')
assembly=importlib.util.module_from_spec(spec);spec.loader.exec_module(assembly)
entries={};same_doi=defaultdict(list);same_title=defaultdict(list);same_statement=defaultdict(list)
for label in ['A','B','C']:
    for key,block in assembly.bib_entries((ROOT/f'parts/{label}/references.bib').read_text()).items():
        entries[(label,key)]=block
        doi=assembly.doi(block)
        if doi: same_doi[doi].append([label,key])
        m=re.search(r'title\s*=\s*\{([^\n]+)',block)
        if m:
            title=re.sub('[^a-z0-9]','',m.group(1).lower())
            same_title[title].append([label,key])
    for item in json.loads((ROOT/f'parts/{label}/items.json').read_text()):
        same_statement[item['statement']].append([label,item['id'],item['pages']])

result={
 'same_doi_different_keys':{k:v for k,v in same_doi.items() if len({x[1] for x in v})>1},
 'same_title_different_keys':{k:v for k,v in same_title.items() if len({x[1] for x in v})>1},
 'exact_duplicate_statements':{k:v for k,v in same_statement.items() if len(v)>1},
 'shared_same_key_sources':{k:v for k,v in same_doi.items() if len(v)>1 and len({x[1] for x in v})==1},
 'source_order_correction':'On P001298 record 683 Ovsienko precedes record 682 Kazakov. Add swap (683,682) if claiming manuscript order.',
 'area_corrections':{
    '669':'Mixed Hodge structures: default should be Algebraic geometry, cohomology, and Hodge theory.',
    '673':'Hypersurface singularities and Hodge theory: use the same algebraic/Hodge area rather than Arrangements and topology.',
    '687':'Hodge--de Rham degeneration and the Deligne--Illusie proof: use algebraic/Hodge area, not Quantum groups.',
    '690':'Moment map and orbital integral, plus a super-symmetric-group question: no modular lattice content; default should be representation theory, with an override for the super question if useful.'},
 'narrative_precision':'The affine Hecke correction is a positive-square versus inverse-square error, not merely a sign change.'
}
text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
(OUT/'code/audit_integration.out').write_text(text)
print(text)
