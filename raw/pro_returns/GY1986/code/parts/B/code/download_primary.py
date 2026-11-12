"""Download only explicitly researched primary papers for visual source checking."""
import pathlib, urllib.request
base=pathlib.Path('parts/B/evidence');base.mkdir(exist_ok=True)
for name,url in [
 ('gelfand_lidskii_ponomarev_1987.pdf','https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=47859&what=fullt'),
 ('herrmann_1983_wordproblem.pdf','https://www2.mathematik.tu-darmstadt.de/~herrmann/fm4.pdf')]:
    try:
        data=urllib.request.urlopen(url,timeout=30).read()
        if not data.startswith(b'%PDF'):raise ValueError('not a PDF')
        (base/name).write_bytes(data);print(name,len(data),url)
    except Exception as exc:print(name,type(exc).__name__,str(exc))
