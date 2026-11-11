from pathlib import Path
import re
P=Path(__file__).resolve().parent
for f in [P/'audit.md',P/'search_log.md']:
 s=f.read_text()
 for w in ['November','October','September','December','February','January','March','April','May','June','July','August']:
  s=re.sub(r'(\d)('+w+r')',r'\1 \2',s);s=re.sub(r'('+w+r')(\d)',r'\1 \2',s)
 s=re.sub(r'(Theorem|Corollary|Proposition|Definition|Conjecture|record|Record|records|item|items|class|Chapter|Version)(\d)',r'\1 \2',s)
 s=re.sub(r'(\d)(items|talks|talk|problems|references|corrections|entries|pages|days|results|paper|preprint|before|after|and|on|to|in|for|gives|factor|solutions|counterexample|independence|continuation|polynomial|announces|theorems|vectors|representations|arithmetic|bounds|read|statement|points|modules|groups|over|from|with|are|has|have|was|is|as|of|means|respectively|finite|printed|classification|citation|signature|date|formula|checks|after|hypothesis)\b',r'\1 \2',s)
 s=s.replace('C2counterexample','C2 counterexample').replace('K0factor','K0 factor').replace('classC','class C').replace('classD','class D').replace('classE','class E').replace('classA','class A').replace('Dproblems','D problems').replace('Stage2','Stage 2')
 s=re.sub(r'(?<=[,:;])(?=[A-Za-z0-9])',' ',s)
 # Do not modify URL syntax damaged by generic punctuation spacing.
 s=s.replace('https: //','https://').replace('http: //','http://')
 f.write_text(s)
# Large external source copies were temporary reading inputs; hashes/URLs survive.
for n in ['douglas_icm1978_volume.pdf','douglas_icm1978_volume.txt']:
 f=P/n
 if f.exists():f.unlink()
print('Audit prose spaced; temporary full proceedings copies removed.')
