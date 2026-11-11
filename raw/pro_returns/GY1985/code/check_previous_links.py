"""Validate earlier-year identifiers against the attached earlier index.

This checks identifier existence, not the asserted mathematical relationship.
"""
import json,re,sys
from pathlib import Path
D=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parent.parent
index=D/'code/authoring/work/previous_index.md'
if not index.exists():index=D.parent/'previous_index.md'
prior=index.read_text()
text='\n'.join((D/f'GY1985_{name}').read_text() for name in ['talks.json','items.json','problems.json','overview.tex','development.tex'])
pattern=r'(?<![A-Za-z0-9-])19\d{2}-\d+\.\d+(?!\d)'
known=set(re.findall(pattern,prior))
seen=sorted(x for x in set(re.findall(pattern,text)) if int(x[:4])<1985)
missing=sorted(set(seen)-known)
problems=json.loads((D/'GY1985_problems.json').read_text())
reused=[p['id'] for p in problems if not p['id'].startswith('GP-1985-')]
known_problems=set(re.findall(r'GP-19\d{2}-\d+',prior))
missing_problems=sorted(set(reused)-known_problems)
report={'status':'PASS' if not missing and not missing_problems else 'FAIL','earlier_occurrence_ids_checked':len(seen),'earlier_occurrence_ids':seen,'missing':missing,'reused_problem_ids':reused,'missing_problem_ids':missing_problems,'scope':'Existence of prior identifiers; exact recurrence versus contextual relationship remains an editorial/source judgment.'}
(D/'audit/previous_index_validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2));sys.exit(report['status']!='PASS')
