from pathlib import Path
import re
target=Path('work/late_references.bib')
out=target.read_text()
sources=[Path('project/references_cumulative.bib'),Path('work/middle_references.bib')]
keys=['gelfand1967planes','gelfand1969forms','gabrielovgelfandlosik1975calculus','gabrielovgelfandlosik1975computation','drinfeld1977commutative','krichever1978commutative']
entries={}
for source in sources:
    for chunk in re.split(r'(?m)(?=^@)',source.read_text()):
        m=re.match(r'@\w+\{([^,]+),',chunk)
        if m: entries.setdefault(m.group(1),chunk.strip())
for key in keys:
    if re.search(r'@\w+\{'+re.escape(key)+r',',out): continue
    entry=entries[key]
    if key.startswith('gabrielovgelfand'):
        entry=re.sub(r',\s*annote=\{[^}]*\}',',\n verificationrecord={Full original Russian primary paper opened in this task. Section1 section-change and degeneracy-chain calculus and the hypersimplex construction checked against P694--696. Earlier cumulative entry verified metadata only; this task upgrades the source reading while preserving the key.}',entry)
    out+='\n\n'+entry+'\n'
target.write_text(out)
print('Copied or retained: '+', '.join(keys))
print('References: '+str(len(re.findall(r'(?m)^@',out))))
