"""Repair opening math delimiters lost while transporting raw literal strings.

Only raw triple-quoted LaTeX fields with unequal delimiter counts are changed.
Ordinary balanced parentheses, including those inside formulas, are respected.
The subsequent validation independently checks the resulting JSON fields.
"""
from pathlib import Path
import re

p=Path(__file__).with_name('write_fragment.py')
text=p.read_text()
changes=[]

def repair(match):
    field=match.group(1)
    if field.count('\\(')==field.count('\\)'):
        return match.group(0)
    stack=[]
    inserts=[]
    for i,ch in enumerate(field):
        if ch not in '()':
            continue
        escaped=(i>0 and field[i-1]=='\\')
        if ch=='(':
            stack.append((i,escaped))
        elif escaped:
            if not stack:
                raise ValueError('No opening parenthesis for math closer: '+field)
            start,proper=stack.pop()
            if not proper:
                inserts.append(start)
        elif stack and not stack[-1][1]:
            stack.pop()
    for i in reversed(sorted(inserts)):
        field=field[:i]+'\\'+field[i:]
    if field.count('\\(')!=field.count('\\)'):
        raise ValueError('Repair failed: '+field)
    changes.append(len(inserts))
    return 'r"""'+field+'"""'

text=re.sub('r"""(.*?)"""',repair,text,flags=re.S)
text=text.replace("r'``Unimodular'' is read", "r'The historical term unimodular is read")
p.write_text(text)
print(f'Restored {sum(changes)} delimiters in {len(changes)} fields.')
