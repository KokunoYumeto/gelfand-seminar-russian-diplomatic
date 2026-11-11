"""Final data, source-coverage, citation and compiled-output gates for GY1972.

Usage: python audit_deliverable.py CHAPTER_DIRECTORY PREVIOUS_INDEX
The supplied builder is also run separately; this independent gate checks
properties not enforced by that builder and records machine-readable results.
"""
from pathlib import Path
import collections
import csv
import hashlib
import json
import re
import sys
import fitz

out=Path(sys.argv[1]).resolve()
previous=Path(sys.argv[2]).read_text()
errors=[]
def require(condition,message):
    if not condition: errors.append(message)

talks=json.loads((out/'GY1972_talks.json').read_text())
items=json.loads((out/'GY1972_items.json').read_text())
problems=json.loads((out/'GY1972_problems.json').read_text())
corrections=list(csv.DictReader((out/'GY1972_corrections.csv').open()))
bib=(out/'GY1972_references.bib').read_text()
keys=re.findall(r'^@\w+\s*\{\s*([^,\s]+)',bib,re.M)
keyset=set(keys)
expected=[272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,
          287,289,290,292,291,293,294,295,296,298,297,299,300]
require([t['record'] for t in talks]==expected,'Requested record set/order mismatch.')
require(sum(t['kind']=='heading' for t in talks)==1,'Expected one heading.')
ids={i['id'] for i in items}; pids={p['id'] for p in problems}
require(len(ids)==len(items),'Duplicate item ID.')
require(len(keys)==len(keyset),'Duplicate bibliography key.')
require(len(pids)==len(problems),'Duplicate problem ID.')
enums={
 'kind':set('definition construction theorem claim conjecture question problem method remark'.split()),
 'class':set('ABCDEF'),
 'literal_correctness':{'correct','correct with missing hypotheses','false as written','not determinable'},
 'publication_match':{'exact','partial','thematic only','none found'},
 'verification':{'read the result','publisher metadata checked','indirect','unresolved lead'},
 'development':{'none','annotated','developed in this chapter'},
 'confidence':{'high','medium','low'},
}
required={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate',
          'present_status','literal_correctness','publication_match','verification','development',
          'problem','worth','refs','confidence'}
for item in items:
    require(required<=item.keys(),item['id']+': missing required fields.')
    for k,allowed in enums.items(): require(item[k] in allowed,item['id']+': invalid '+k)
    require('November 2026' in item['present_status'],item['id']+': undated status.')
    require(set(item['refs'])<=keyset,item['id']+': unknown bibliography key.')
    if item['class'] in ('C','D'): require(bool(item['worth']),item['id']+': missing development decision.')
    if item['problem']: require(item['problem'] in pids,item['id']+': missing problem entry.')
    latex='\n'.join(item[k] for k in ['notes','statement','reconstruction','fate','present_status','worth'])
    cited={key.strip() for group in re.findall(r'\\cite[pt]?\*?(?:\[[^]]*\])*\{([^}]+)\}',latex) for key in group.split(',')}
    require(cited<=set(item['refs']),item['id']+': citation missing from refs field.')
for record in expected:
    local=[i['id'] for i in items if i['record']==record]
    require(local==[f'1972-{record}.{n}' for n in range(1,len(local)+1)],f'{record}: nonconsecutive IDs.')
for problem in problems:
    require(problem['status_date']=='2026-11',problem['id']+': wrong status date.')
    require(set(problem['refs'])<=keyset,problem['id']+': unknown bibliography key.')
    for occurrence in problem['occurrences']:
        require(occurrence in ids or occurrence in previous,problem['id']+': unknown occurrence '+occurrence)
        if occurrence in ids:
            match=next(i for i in items if i['id']==occurrence)
            require(match['problem']==problem['id'],problem['id']+': nonreciprocal occurrence '+occurrence)
for item in items:
    if item['problem']:
        match=next(p for p in problems if p['id']==item['problem'])
        require(item['id'] in match['occurrences'],item['id']+': nonreciprocal problem field.')

# No raw TeX-sensitive math tokens remain in prose. Math environments and
# citation arguments are protected before this lexical screen.
latex_fields=[]
for item in items:
    latex_fields.extend((item['id'],k,item[k]) for k in ['notes','statement','reconstruction','fate','present_status','worth'])
for talk in talks: latex_fields.append((str(talk['record']),'summary',talk['summary']))
for problem in problems:
    latex_fields.extend((problem['id'],k,problem[k]) for k in ['statement','status'])
for row in corrections:
    latex_fields.extend((row['page'],k,row[k]) for k in ['place','transcription_reads','should_read','evidence'])
for identifier,field,value in latex_fields:
    plain=re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]|\$.*?\$|\\(?:url|href)\{[^}]*\}', '', value,flags=re.S)
    require(not re.search(r'(?<!\\)[_^&#%]',plain),identifier+': raw TeX token in '+field)
    require(value.count(r'\(')==value.count(r'\)'),identifier+': inline math delimiters in '+field)
    require(value.count(r'\[')==value.count(r'\]'),identifier+': display math delimiters in '+field)
    require(not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',value),identifier+': control character in '+field)

coverage=set()
for item in items:
    span=[int(x) for x in re.findall(r'P(\d{6})',item['pages'])]
    require(bool(span),item['id']+': no source-page ID.')
    if span: coverage.update(range(min(span),max(span)+1))
require(coverage==set(range(450,480))|set(range(481,501)),'Unexpected new source-page coverage.')

log=(out/'GY1972_test.log').read_text()
require(not re.search(r'^!|LaTeX Error|Package .* Error',log,re.M),'LaTeX error remains.')
require('Overfull' not in log,'Overfull box remains.')
require('Missing character' not in log,'Missing font character remains.')
require('undefined' not in log.lower(),'Undefined reference remains.')
require('Label(s) may have changed' not in log,'Unstable references remain.')
blg=(out/'GY1972_test.blg').read_text()
require(not re.search(r'Warning--|error message',blg,re.I),'BibTeX warning/error remains.')
bbl=(out/'GY1972_test.bbl').read_text()
printed_bib=len(re.findall(r'\\bibitem\[',bbl))
require(printed_bib==len(keys),'Not every bibliography entry appears in the compiled bibliography.')

pdf=fitz.open(out/'GY1972_test.pdf')
text='\n'.join(p.get_text() for p in pdf)
require(ids<=set(re.findall(r'1972-\d+\.\d+',text)),'An item ID is missing from the PDF.')
require(len(pdf.get_toc())>=len(talks),'Missing document navigation bookmarks.')
first_talk_page=next((row[2] for row in pdf.get_toc() if 'Gabrielov, 1972-09-25' in row[1]),None)
require(first_talk_page is not None and first_talk_page<=3,'Overview exceeds two pages before the first talk.')

summary=dict(status='passed' if not errors else 'failed',errors=errors,
             records=len(talks),talks=sum(t['kind']=='talk' for t in talks),items=len(items),
             classes={c:sum(i['class']==c for i in items) for c in 'ABCDEF'},
             problems=len(problems),references=len(keys),printed_bibliography_entries=printed_bib,
             corrections=len(corrections),pdf_pages=len(pdf),overview_first_talk_page=first_talk_page,
             new_source_pages=sorted(coverage),prior_owned_pages=[449,480],
             compiler_errors=len(re.findall(r'^!|LaTeX Error|Package .* Error',log,re.M)),
             overfull_boxes=log.count('Overfull'),underfull_boxes=log.count('Underfull'),
             missing_glyph_warnings=log.count('Missing character'),
             undefined_references='undefined' in log.lower(),
             pdf_sha256=hashlib.sha256((out/'GY1972_test.pdf').read_bytes()).hexdigest(),
             visual_review='See visual_qa.json; machine checks do not replace rendered-page inspection.')
(out/'validation_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
raise SystemExit(1 if errors else 0)
