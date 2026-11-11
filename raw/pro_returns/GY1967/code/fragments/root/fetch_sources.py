"""Download already identified open scholarly sources for local result checks.
The PDFs are working material, not redistributed in the deliverable.
"""
import concurrent.futures
import hashlib
import json
import pathlib
import urllib.request

BASE = pathlib.Path(__file__).resolve().parents[2]
DEST = BASE / 'work' / 'literature'
DEST.mkdir(parents=True, exist_ok=True)
SOURCES = {
 'hormander1968spectral': 'https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6063-11511_2006_Article_BF02391913.pdf',
 'auyeung1969sphere': 'https://www.ams.org/journals/proc/1969-020-02/S0002-9939-1969-0234968-6/S0002-9939-1969-0234968-6.pdf',
 'davis1968shell': 'https://acta.bibl.u-szeged.hu/14177/1/math_029_fasc_001_002_069-086.pdf',
 'basshellerswan1964whitehead': 'https://www.numdam.org/item/PMIHES_1964__22__61_0.pdf',
 'hsiangshaneson1969fake': 'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/hsiashan1.pdf',
 'hsiangwall1969tori': 'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/hsiawall2.pdf',
 'milnor1966torsion': 'https://www.ams.org/bull/1966-72-03/S0002-9904-1966-11484-2/S0002-9904-1966-11484-2.pdf',
 'dumas2011invariants': 'https://lmbp.uca.fr/~fdumas/fichiers/B-Mat60.pdf',
 'buchstaber_bibliography': 'https://www.mi.ras.ru/index.php?c=pubs&id=9162&l=0&showall=show&showmode=sci',
 'schmid1968landing': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC286000/',
}

def get(pair):
 key, url = pair
 try:
  request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (scholarly verification)'})
  with urllib.request.urlopen(request, timeout=30) as response:
   data = response.read()
  ext = '.pdf' if data.startswith(b'%PDF') else '.html'
  (DEST/(key+ext)).write_bytes(data)
  return {'key': key, 'url': url, 'bytes': len(data), 'format': ext, 'sha256': hashlib.sha256(data).hexdigest()}
 except Exception as exc:
  return {'key': key, 'url': url, 'error': str(exc)}

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 results = list(pool.map(get, SOURCES.items()))
log = json.dumps(results, ensure_ascii=False, indent=2)
(pathlib.Path(__file__).parent/'fetch_sources_output.json').write_text(log+'\n')
print(log)
