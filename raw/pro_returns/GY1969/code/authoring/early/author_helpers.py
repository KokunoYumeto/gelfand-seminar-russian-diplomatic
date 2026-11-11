from pathlib import Path
import json, csv, re
D=Path(__file__).resolve().parent
T=[]; I=[]; P=[]; C=[]; R={}; S=[]
def talk(record,date,speaker,pages,title,summary,kind='talk'):
 T.append(dict(record=record,date=date,speaker=speaker,pages=pages,title=title,kind=kind,summary=summary))
def item(record,pages,kind,title,notes,statement,fate,refs=(),cls='E',reconstruction='',status='',literal='correct with missing hypotheses',match='exact',verification='read the result',development='none',problem='',worth='',confidence='high',speaker=None):
 year=1969 if record<=183 else 1970
 n=1+sum(x['record']==record for x in I)
 d=dict(id=f'{year}-{record}.{n}',record=record,pages=pages,kind=kind,title=title,notes=notes,statement=statement,reconstruction=reconstruction,**{'class':cls},fate=fate,present_status=status or 'As of 9 November 2026: established in the stated scope; no open problem is asserted by this item.',literal_correctness=literal,publication_match=match,verification=verification,development=development,problem=problem,worth=worth,refs=list(refs),confidence=confidence)
 if speaker:d['speaker']=speaker
 I.append(d); return d['id']
def correction(page,place,reads,should,evidence,applies='both',kind='faithful_error'):
 C.append(dict(page=page,place=place,transcription_reads=reads,should_read=should,evidence=evidence,applies_to=applies,type=kind))
def ref(key,kind='article',**fields):
 fields.setdefault('note','verified'); R[key]=(kind,fields)
def source(key,url,locator,evidence,level='read the result'):
 S.append(dict(key=key,url=url,locator=locator,evidence=evidence,verification=level,access_date='2026-11-09'))
def checkpoint():
 for fn,data in [('talks',T),('items',I),('problems',P),('sources',S)]:
  (D/(fn+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 with (D/'corrections.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type']);w.writeheader();w.writerows(C)
 bib=''
 for key,(kind,fields) in R.items():
  bib+='@'+kind+'{'+key+',\n'+',\n'.join('  '+k+' = {'+str(v)+'}' for k,v in fields.items())+'\n}\n\n'
 (D/'references.bib').write_text(bib)
 print(f'Saved {len(T)} records, {len(I)} items, {len(P)} problems, {len(C)} corrections, {len(R)} references.')
