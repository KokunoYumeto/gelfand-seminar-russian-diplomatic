from pathlib import Path
import re

D=Path(__file__).resolve().parent
for name in ['author_early.py','author_remaining.py']:
    p=D/name
    s=p.read_text()
    # In single-quoted Python literals, TeX closing apostrophes would silently
    # concatenate adjacent strings. These replacements happen in source code.
    s,n=re.subn(r"``([^'\n]*?)''",lambda m:r'\textquotedblleft '+m[1]+r'\textquotedblright{}',s)
    s=s.replace('compact-semisisimple','compact-semisimple')
    s=s.replace('1970-187.6.','1970-187.7.')
    p.write_text(s)
    print(name,'paired TeX quotations corrected:',n)
