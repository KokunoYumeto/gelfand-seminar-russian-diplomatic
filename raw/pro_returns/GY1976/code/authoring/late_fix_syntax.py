from pathlib import Path
p=Path('work/late_author.py')
s=p.read_text().replace("'Ulam's problem for a random real sequence'",'"Ulam\'s problem for a random real sequence"')
p.write_text(s)
