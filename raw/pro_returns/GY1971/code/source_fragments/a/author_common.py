import json,csv,pathlib
D=pathlib.Path(__file__).parent

def load(n):
 p=D/n
 return json.loads(p.read_text()) if p.exists() else []

def save(n,x):
 (D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')

def talks(xs):save('talks.json',xs)

def items(record,xs):
 old=[i for i in load('items.json') if i['record']!=record]
 for k,x in enumerate(xs,1):
  x={'id':f'1971-{record}.{k}','record':record,**x}
  for a,b in {'reconstruction':'','class':'E','literal_correctness':'correct with missing hypotheses','publication_match':'partial','verification':'read the result','development':'annotated','problem':'','worth':'','refs':[],'confidence':'high'}.items():x.setdefault(a,b)
  old.append(x)
 order={229:0,230:1,231:2,232:3,233:4,235:5,234:6,236:7,237:8,238:9,239:10,240:11,241:12,242:13,243:14}
 old.sort(key=lambda x:(order[x['record']],int(x['id'].split('.')[-1])))
 save('items.json',old)

def I(p,k,t,n,s,f,status,**kw):
 return {'pages':p,'kind':k,'title':t,'notes':n,'statement':s,'fate':f,'present_status':'As of November 2026, '+status,**kw}

def corrections(xs):
 path=D/'corrections.csv';hdr=['page','place','transcription_reads','should_read','evidence','applies_to','type']
 old=list(csv.DictReader(path.open())) if path.exists() else []
 for x in xs:
  z=dict(zip(hdr,x))
  if z not in old:old.append(z)
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=hdr);w.writeheader();w.writerows(old)

def problems(xs):
 old=load('problems.json');d={x['id']:x for x in old}
 for x in xs:d[x['id']]=x
 save('problems.json',list(d.values()))
