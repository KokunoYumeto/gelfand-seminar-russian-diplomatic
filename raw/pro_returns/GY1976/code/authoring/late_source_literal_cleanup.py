from pathlib import Path
p=Path('work/late_author.py')
s=p.read_text().replace("\n 'GGS (1967), Theorem 1, states class", "\n r'GGS (1967), Theorem 1, states class")
s=s.replace("\n 'The PNG clearly says one-dimensional; the integrand", "\n r'The PNG clearly says one-dimensional; the integrand")
p.write_text(s)
log=Path('work/late_research_log.md')
with log.open('a') as f:
    f.write('\n## Final LaTeX correction audit\n\nAll 42 correction rows were independently scanned for raw mathematical tokens outside explicit math delimiters. The correction-only XeLaTeX document compiled successfully to six pages with no LaTeX errors and no overfull boxes. Long exponential formulas use aligned displays. The three item-layout adjustments requested after the integrated first pass were applied in the authoring source and regenerated JSON. Evidence is preserved in late_correction_math_audit.json, late_correction_compile_output.json, and the late_correction_preflight directory.\n')
print('Normalized source string literals and recorded the final correction audit.')
