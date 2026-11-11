from pathlib import Path
p=Path('work/late_author.py')
s=p.read_text().replace(
r'''r''' + "'''Over the moduli of stable degree-zero bundles, forgetting a holomorphic connection gives a torsor",
r'''r''' + "'''Let \\(X\\) be a smooth projective complex curve of genus \\(g\\geq2\\). Over the moduli of stable degree-zero bundles, forgetting a holomorphic connection gives a torsor")
p.write_text(s)
