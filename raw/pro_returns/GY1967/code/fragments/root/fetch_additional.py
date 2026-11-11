"""Reproducible retrieval of identified primary-source PDFs for reading only."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib, json, urllib.request

BASE = Path(__file__).resolve().parents[2]
DEST = BASE/'work/literature'
SOURCES = {
 'kervairemilnor1963spheres': 'https://people.math.rochester.edu/faculty/doug/otherpapers/kervaire-milnor.pdf',
 'serre1953classes': 'https://www.college-de-france.fr/media/jean-pierre-serre/UPL6839232787883948296_Serre_C_the__orie.pdf',
 'schmid1978icm_volume': 'https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1978.1/ICM1978.1.ocr.pdf',
 'griffithsschmid1969locally': 'https://publications.ias.edu/sites/default/files/locallyhomogeneous.pdf',
 'novikov1964homotopy': 'https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=rus&paperid=2959&what=fullt',
 'novikov1966abelian': 'https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=2826&what=fullt',
 'milnor1966torsion_ru': 'https://www.mathnet.ru/php/getFT.phtml?jrnid=mat&option_lang=eng&paperid=419&what=fullt',
}
def fetch(kv):
 key, url = kv
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=45) as response: data=response.read()
  pdf=data.startswith(b'%PDF')
  (DEST/(key+('.pdf' if pdf else '.html'))).write_bytes(data)
  return dict(key=key,url=url,bytes=len(data),pdf=pdf,sha256=hashlib.sha256(data).hexdigest())
 except Exception as exc: return dict(key=key,url=url,error=str(exc))
if __name__=='__main__':
 DEST.mkdir(parents=True,exist_ok=True)
 with ThreadPoolExecutor(max_workers=4) as pool: result=list(pool.map(fetch,SOURCES.items()))
 output=json.dumps(result,ensure_ascii=False,indent=2)
 (Path(__file__).parent/'fetch_additional_output.json').write_text(output+'\n')
 print(output)
