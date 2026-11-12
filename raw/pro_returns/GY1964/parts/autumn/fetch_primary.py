"""Fetch two already-opened primary PDFs for visual formula verification."""
from pathlib import Path
from urllib.request import urlopen
import subprocess

out = Path(__file__).resolve().parent / 'primary'
out.mkdir(exist_ok=True)
urls = {
    'dobrushin1965': 'https://www.mathnet.ru/php/getFT.phtml?jrnid=tvp&option_lang=eng&paperid=518&what=fullt',
    'linnik1957': 'https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=5081&what=fullt',
}
for name, url in urls.items():
    try:
        with urlopen(url, timeout=30) as response:
            data = response.read()
        if not data.startswith(b'%PDF'):
            raise ValueError('Response is not a PDF')
        path = out / (name + '.pdf')
        path.write_bytes(data)
        subprocess.run(['pdftoppm', '-f', '2', '-l', '3', '-scale-to', '2000', '-png', str(path), str(out / name)], check=True)
        print(name, len(data), 'bytes downloaded and pages 2--3 rendered')
    except Exception as exc:
        print(name, type(exc).__name__, str(exc))
