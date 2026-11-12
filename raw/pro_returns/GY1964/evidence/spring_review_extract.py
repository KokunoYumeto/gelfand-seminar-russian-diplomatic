"""Read-only extraction for independent mathematical review of spring items."""
import json,sys,hashlib
from pathlib import Path
base=Path('/workspace/scratch/f63c951485b7/work/parts/spring')
a,b=map(int,sys.argv[1:3])
p=base/'items.json'
print('SNAPSHOT_SHA256',hashlib.sha256(p.read_bytes()).hexdigest())
items=json.loads(p.read_text())
print('ITEM_COUNT',len(items))
for x in items:
    if a<=x['record']<=b:
        print('\n##',x['id'],x['title'],x['pages'])
        for k in ['notes','statement','reconstruction','fate','present_status']:
            print(k.upper()+':',x[k])
        print('ASSESSMENT:',{k:x[k] for k in ['class','literal_correctness','publication_match','verification','problem']})
