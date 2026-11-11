"""Exact and independent checks for the finite-jet cohomology annotation.

Method A: symbolic substitution through degree four.
Method B: independently implemented integer coefficient convolution through
degree seven, deterministic randomized and exhaustive residue tests.
Neither replaces the literature proof of the closed-commutator theorem.
"""
from pathlib import Path
import itertools, json, random
import sympy as s

OUT=Path(__file__).resolve().parent/'output';OUT.mkdir(exist_ok=True)
t=s.symbols('t')
a,b,c,A,B,C=s.symbols('a b c A B C')
f=t+a*t**2+b*t**3+c*t**4
g=t+A*t**2+B*t**3+C*t**4
h=s.Poly(s.series(f.subs(t,g),t,0,5).removeO(),t)
aa,bb,cc=[h.coeff_monomial(t**k) for k in (2,3,4)]
x=lambda a,b,c:a
y=lambda a,b,c:b-a*a
z=lambda a,b,c:c-a**3-2*a*(b-a*a)
w=lambda a,b,c:c-3*a*b+2*a**3
assert s.expand(aa-a-A)==0
assert s.expand(y(aa,bb,cc)-y(a,b,c)-y(A,B,C))==0
assert s.expand(z(aa,bb,cc)-z(a,b,c)-z(A,B,C)-y(a,b,c)*A)==0
assert s.expand(w(A,B,C)-w(aa,bb,cc)+w(a,b,c)-a*y(A,B,C))==0

def mul(p,q,N=7):
    ans=[0]*(N+1)
    for i in range(N+1):
        for j in range(N+1-i):ans[i+j]+=p[i]*q[j]
    return ans

def compose(p,q,N=7):
    ans=[0]*(N+1);power=[1]+[0]*N
    for k in range(N+1):
        for i in range(N+1):ans[i]+=p[k]*power[i]
        power=mul(power,q,N)
    return ans

def chars(p):
    a,b,c,d,e,f=p[2:8]
    return (a,b-a*a,(d+c+b*(b+1)//2)%2,(f+d*b+d)%2)

def primitive(p):
    a,b,c=p[2:5]
    return c-3*a*b+2*a**3

def beta(p,q,j):
    pq=compose(p,q)
    return (chars(p)[j]+chars(q)[j]-chars(pq)[j])//2

rng=random.Random(1977441)
cases=1500
for run in range(cases):
    p=[0,1]+[rng.randrange(-50,51) for _ in range(6)]
    q=[0,1]+[rng.randrange(-50,51) for _ in range(6)]
    r=[0,1]+[rng.randrange(-50,51) for _ in range(6)]
    pq=compose(p,q);qr=compose(q,r)
    cp,cq,cpq=chars(p),chars(q),chars(pq)
    assert cpq[:2]==tuple(cp[i]+cq[i] for i in range(2))
    assert cpq[2:]==tuple((cp[i]+cq[i])%2 for i in range(2,4))
    assert primitive(q)-primitive(pq)+primitive(p)==cp[0]*cq[1]
    for j in (2,3):
        assert beta(q,r,j)-beta(pq,r,j)+beta(p,qr,j)-beta(p,q,j)==0
        assert 2*beta(p,q,j)==cp[j]+cq[j]-cpq[j]

# Exhaustive residue check for epsilon_1: its integer-valued binomial term
# depends on b modulo four; all other relevant coordinates need only parity.
residues=[]
for a,c,d in itertools.product(range(2),repeat=3):
    for b in range(4):residues.append([0,1,a,b,c,d,0,0])
for p in residues:
    for q in residues:
        assert chars(compose(p,q))[2]==(chars(p)[2]+chars(q)[2])%2

# epsilon_2 is a polynomial over F_2 in the six displayed coefficients.
residues2=[[0,1]+list(v) for v in itertools.product(range(2),repeat=6)]
for p in residues2:
    for q in residues2:
        assert chars(compose(p,q))[3]==(chars(p)[3]+chars(q)[3])%2

result={'symbolic_composition':{'a':str(aa),'b':str(bb),'c':str(cc)},
        'heisenberg_coordinate':'z=c-a^3-2a(b-a^2)',
        'cup_primitive':'w=c-3ab+2a^3; delta(w)(f,g)=a(f)*(b(g)-a(g)^2)',
        'symbolic_identities':'all exact identities verified',
        'random_seed':1977441,'integer_triples_checked':cases,'coefficient_range':[-50,50],
        'epsilon1_residue_pairs':len(residues)**2,'epsilon2_residue_pairs':len(residues2)**2,
        'bockstein_cocycle_checks':2*cases,
        'warning':'Finite checks do not prove the closed-commutator classification or compute the full cohomology ring.'}
(OUT/'jet_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
