"""Remove accidental patch prefixes from authoring source before execution."""
from pathlib import Path
p=Path(__file__).with_name('late_author.py')
s=p.read_text()
p.write_text('\n'.join(line[1:] if line.startswith('+') else line for line in s.split('\n')))
