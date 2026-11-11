from pathlib import Path
import urllib.request,subprocess
p=Path(__file__).resolve().parent
u='https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1992&what=fullteng'
try:
 d=urllib.request.urlopen(u,timeout=30).read(); (p/'rudakov1974_source.pdf').write_bytes(d)
 print('Downloaded',len(d),'bytes, PDF magic',d[:4])
 subprocess.run(['pdftoppm','-f','30','-l','31','-scale-to','1800','-png','-singlefile',str(p/'rudakov1974_source.pdf'),str(p/'rudakov1974_page30')],check=True)
except Exception as e:print(type(e).__name__,str(e))
