"""Download public primary PDFs used to verify the critical companion.
No credentials or private data are used. Keeps the retrieved files in this fragment.
"""
from pathlib import Path
from urllib.request import urlopen, Request
import subprocess

root = Path(__file__).resolve().parent
sources = {
    'douglas_icm1978_volume.pdf': 'https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1978.2/ICM1978.2.ocr.pdf',
    'bdf1973_bulletin.pdf': 'https://www.ams.org/journals/bull/1973-79-05/S0002-9904-1973-13284-7/S0002-9904-1973-13284-7.pdf',
}
for filename, url in sources.items():
    try:
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urlopen(request, timeout=45).read()
        if not data.startswith(b'%PDF'):
            raise ValueError('Response is not a PDF')
        path = root / filename
        path.write_bytes(data)
        subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True)
        print(filename, len(data), 'bytes; extracted text')
    except Exception as exc:
        print(filename, type(exc).__name__, str(exc))
