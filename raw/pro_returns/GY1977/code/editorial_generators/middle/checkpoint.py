import json,csv
from pathlib import Path
P=Path(__file__).resolve().parent

def load(name,default):
    f=P/name
    return json.loads(f.read_text()) if f.exists() else default
items=load('items.json',[]); talks=load('talks.json',[]); problems=load('problems.json',[]); areas=load('areas.json',{}); references=load('references.json',[])
def begin(record):
    global items
    items=[i for i in items if i['record']!=record]
    for k in list(areas):
        if k.startswith(f'1977-{record}.'): del areas[k]
def item(record,pages,kind,title,notes,statement,fate,refs,*,reconstruction='',cls='E',status='',literal='correct with missing hypotheses',match='exact',verification='read the result',development='none',problem='',worth='',confidence='high',area='Representation theory',speaker=None):
    n=1+sum(i['record']==record for i in items); ident=f'1977-{record}.{n}'
    d=dict(id=ident,record=record,pages=pages,kind=kind,title=title,notes=notes,statement=statement,reconstruction=reconstruction,**{'class':cls},fate=fate,present_status=status or 'As of 10 November 2026, this is an established result in the stated scope.',literal_correctness=literal,publication_match=match,verification=verification,development=development,problem=problem,worth=worth,refs=refs,confidence=confidence)
    if speaker: d['speaker']=speaker
    items.append(d); areas[ident]=area
    return ident
def talk(record,date,speaker,pages,title,summary):
    global talks
    talks=[t for t in talks if t['record']!=record]
    talks.append(dict(record=record,date=date,speaker=speaker,pages=pages,title=title,kind='talk',summary=summary))
def prob(ident,title,statement,occurrences,status,refs):
    global problems
    problems=[p for p in problems if p['id']!=ident]
    problems.append(dict(id=ident,title=title,statement=statement,occurrences=occurrences,status=status,status_date='2026-11',refs=refs))
def audit(key,url,verification,locator,evidence):
    global references
    references=[r for r in references if not(r['key']==key and r['url']==url)]
    references.append(dict(key=key,url=url,verification=verification,locator=locator,opened_url_evidence=evidence))
def save():
    for name,data in [('items.json',sorted(items,key=lambda x:tuple(map(int,x['id'].replace('1977-','').split('.'))))),('talks.json',sorted(talks,key=lambda x:x['record'])),('problems.json',problems),('areas.json',areas),('references.json',references)]:
        (P/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def corr(page,place,reads,should,evidence,applies='both',kind='faithful_error'):
    f=P/'corrections.csv'
    exists=f.exists()
    with f.open('a',newline='') as out:
        w=csv.writer(out)
        if not exists:w.writerow(['page','place','transcription_reads','should_read','evidence','applies_to','type'])
        w.writerow([page,place,reads,should,evidence,applies,kind])
