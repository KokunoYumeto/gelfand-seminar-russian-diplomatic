from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request,fitz
p=Path(__file__).parent/'primary';p.mkdir(exist_ok=True)
urls={
'parthasarathy1988':'https://repository.ias.ac.in/82619/1/1-Pub.pdf',
'reshetikhin1987i':'https://math.berkeley.edu/~reshetik/Publications/QGInv-1-1987.pdf',
'reshetikhin1987ii':'https://math.berkeley.edu/~reshetik/Publications/QGInv-2-1987.pdf',
'kashiwaraschapira1985':'https://www.numdam.org/item/AST_1985__128__1_0.pdf',
'gorodentsevrudakov1987':'https://projecteuclid.org/journals/duke-mathematical-journal/volume-54/issue-1/Exceptional-vector-bundles-on-projective-spaces/10.1215/S0012-7094-87-05409-3.pdf',
'rudakov1988markov':'https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1170&what=fullteng',
'rudakov1988quadric':'https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1205&what=fullteng',
'appel1977reducibility':'https://projecteuclid.org/journalArticle/Download?urlid=10.1215/ijm/1256049012',
'hall1935':'https://deltadbu.github.io/UCAS_algorithm_course/Lectures/Hall1935.pdf',
'gon2008':'https://www.ams.org/notices/200811/tx081101382p.pdf',
}
def run(kv):
 k,u=kv
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})
  b=urllib.request.urlopen(req,timeout=30).read()
  if not b.startswith(b'%PDF'):return f'{k}: response not PDF'
  (p/(k+'.pdf')).write_bytes(b)
  d=fitz.open(stream=b,filetype='pdf'); t='\n'.join(f'\nPDF_PAGE {i+1}\n'+x.get_text() for i,x in enumerate(d));(p/(k+'.txt')).write_text(t)
  return f'{k}: {len(b)} bytes; {len(d)} pages; {len(t)} text chars; {u}'
 except Exception as e:return f'{k}: {type(e).__name__}: {e}'
with ThreadPoolExecutor(max_workers=5) as pool:
 rs=list(pool.map(run,urls.items()))
(p/'download_log.txt').write_text('\n'.join(rs))
print('\n'.join(rs))
