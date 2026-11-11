from pathlib import Path
p=Path('work/late_author.py')
s=p.read_text().replace(r"\frac{f'''}{f'}",r"\frac{f^{(3)}}{f'}")
p.write_text(s)
