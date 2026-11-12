"""Restore math delimiters after an authoring transport stripped unknown JS escapes.

This one-time source repair operates only on the newly appended records 694--697.
Balanced outer parentheses there were deliberately math delimiters; literal equation
numbers are kept. It does not alter source transcriptions or kit files.
"""
import ast, io, pathlib, re, tokenize
p=pathlib.Path('parts/B/code/assemble.py')
s=p.read_text()
lines=s.splitlines(keepends=True)
start=next(i+1 for i,line in enumerate(lines) if line.startswith("talk(694,"))
replacements=[]
def restore(x):
    spans=[];depth=0;begin=None
    for j,c in enumerate(x):
        if c=='(':
            if depth==0:begin=j
            depth+=1
        elif c==')' and depth:
            depth-=1
            if depth==0:
                body=x[begin+1:j]
                if (begin and x[begin-1]=='\\') or re.fullmatch(r'\d+(?:\.\d+)*|ii',body): continue
                if body.endswith('\\'):body=body[:-1]
                spans.append((begin,j+1,r'\('+body+r'\)'))
    for a,b,new in reversed(spans):x=x[:a]+new+x[b:]
    return x
for t in tokenize.generate_tokens(io.StringIO(s).readline):
    if t.type!=tokenize.STRING or t.start[0]<start or not t.string.startswith("r'"):continue
    old=ast.literal_eval(t.string);new=restore(old)
    if new!=old:replacements.append((t.start,t.end,repr(new)))
for (row,col),(endrow,endcol),v in reversed(replacements):
    assert row==endrow
    lines[row-1]=lines[row-1][:col]+v+lines[row-1][endcol:]
p.write_text(''.join(lines))
print('Repaired string literals:',len(replacements))
