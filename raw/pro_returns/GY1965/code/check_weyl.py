"""Exact checks for the bounded Weyl-field development and the PBW count.

Finite checks audit formulas; the accompanying proofs, not these tests,
establish the general statements. Run from any directory. Requires SymPy.
"""
from itertools import product
from math import comb
from random import Random
import argparse
import sympy as s

parser=argparse.ArgumentParser()
parser.add_argument('--seed',type=int,default=1965)
args=parser.parse_args()
x=s.symbols('x')

def clean(a):
    return {i:s.cancel(v) for i,v in a.items() if s.cancel(v)!=0}

def plus(a,b):
    out=dict(a)
    for j,v in b.items(): out[j]=out.get(j,0)+v
    return clean(out)

def scale(a,k): return clean({i:k*v for i,v in a.items()})

def mul(a,b):
    out={}
    for i,ai in a.items():
        for j,bj in b.items():
            for k in range(i+1):
                power=i-k+j
                out[power]=out.get(power,0)+s.binomial(i,k)*ai*s.diff(bj,x,k)
    return clean(out)

def power(a,n):
    out={0:s.Integer(1)}
    for _ in range(n): out=mul(out,a)
    return out

def image_p(f,b):
    # Parameters encode T_b L_f, so p maps to (p+b)/f'.
    fp=s.diff(f,x)
    return clean({1:1/fp,0:b/fp})

def transform(a,f,b):
    P=image_p(f,b)
    out={}
    for i,ai in a.items():
        out=plus(out,scale(power(P,i),ai.subs(x,f)))
    return out

def same(a,b):
    return not plus(a,scale(b,-1))

def rational_sub(a,f): return s.cancel(a.subs(x,f))

def pair_product(f,b,g,c):
    # Apply (f,b) after (g,c); coordinate images compose contravariantly.
    return rational_sub(g,f),s.cancel(b+s.diff(f,x)*rational_sub(c,f))

def mobius_inverse(f):
    y=s.symbols('y')
    return s.cancel(s.solve(s.together(f-y),x)[0].subs(y,x))

rng=Random(args.seed)
matrices=[(1,0,0,1),(0,1,1,0),(1,1,0,1),(2,1,1,1),(1,0,0,-1)]
while len(matrices)<10:
    a,b,c,d=(rng.randint(-3,3) for _ in range(4))
    if a*d-b*c and (a,b,c,d) not in matrices:
        matrices.append((a,b,c,d))
changes=[s.cancel((a*x+b)/(c*x+d)) for a,b,c,d in matrices]
shifts=[s.Integer(0),1/x,1/(2*x),1/x**2,x,3/(x-1)-2/(x+2)]
checks={'commutators':0,'inverses':0,'composition':0,'monomial_action':0,'finite_group':0,'pbw_counts':0}

for f,b in product(changes,shifts):
    P=image_p(f,b)
    Q={0:f}
    assert same(plus(mul(P,Q),scale(mul(Q,P),-1)),{0:s.Integer(1)})
    checks['commutators']+=1
    u=mobius_inverse(f)
    # Inverse pair from b + f' c(f) = 0.
    c=s.cancel(-rational_sub(b,u)/rational_sub(s.diff(f,x),u))
    for target in ({0:x},{1:s.Integer(1)}):
        assert same(transform(transform(target,u,c),f,b),target)
        assert same(transform(transform(target,f,b),u,c),target)
    checks['inverses']+=1
    # Independent operator-on-functions evaluation, without mul().
    for degree in (0,1,2,5,9):
        test=x**degree
        act=lambda z:s.cancel(s.diff(z,x)/s.diff(f,x)+(b/s.diff(f,x))*z)
        assert s.cancel(act(f*test)-f*act(test)-test)==0
        checks['monomial_action']+=1

for trial in range(40):
    f,g=rng.sample(changes,2)
    b,c=rng.sample(shifts,2)
    F,B=pair_product(f,b,g,c)
    for target in ({0:x},{1:s.Integer(1)},{2:1/x,1:x**2,0:1/(x-2)}):
        assert same(transform(transform(target,g,c),f,b),transform(target,F,B))
    checks['composition']+=1

# An explicit nontrivial C2 cocycle.
f=-x
a=1/(x*x-1)
b=2*a
F,B=pair_product(f,b,f,b)
assert s.cancel(F-x)==0 and s.cancel(B)==0
F,B=pair_product(x,-a,f,b)
F,B=pair_product(F,B,x,a)
assert s.cancel(F+x)==0 and s.cancel(B)==0
checks['finite_group']+=2

# Implementers checked independently by logarithmic differentiation.
positive=[(3/(x-1)-2/(x+2),(x-1)**-3*(x+2)**2),
          (1/x,x**-1),(s.Integer(0),s.Integer(1))]
for h,u in positive: assert s.cancel(h+s.diff(u,x)/u)==0

# Negative controls: these must be detected as wrong.
wrong_sign=s.cancel(s.diff(x**-1,x)/(x**-1)-1/x)
assert wrong_sign!=0
f=1/x
b=s.Integer(0)
c=x
F,B=pair_product(f,b,x,c)
assert s.cancel(B-(b+c.subs(x,f)))!=0

# Independent PBW count: dynamic programming by number of variables and degree.
def count_tuples(num_vars,max_degree):
    exact=[1]+[0]*max_degree
    for _ in range(num_vars):
        exact=[sum(exact[:degree+1]) for degree in range(max_degree+1)]
    return sum(exact)

for n in range(5):
    for k in range(5):
        for N in (0,1,2,3,7,10,13):
            m=2*n+k
            assert count_tuples(m,N)==comb(N+m,m)
            checks['pbw_counts']+=1

print('Research computation: exact rational arithmetic, not numerical sampling.')
print(f'Seed: {args.seed}; SymPy: {s.__version__}')
for label,num in checks.items(): print(f'{label}: {num} PASS')
print('Logarithmic-derivative implementers: 3 PASS')
print('Negative controls: wrong conjugation sign and missing chain-rule factor both rejected.')
print('h=3/(x-1)-2/(x+2): implementer (x-1)^(-3)*(x+2)^2, residual 0.')
print('h=1/(2*x): nonintegral residue; noninner by proof. Twice h=1/x has implementer x^(-1).')
print('h=1/x^2: double pole, excluded by proved criterion.')
print('h=x: polynomial part, excluded by proved criterion.')
print('C2 example: x -> -x, p -> -p-2/(x^2-1); square identity, averaged translation removes cocycle.')
print('PBW edge cases included n=k=0 and N=0; binomial identity passed throughout.')
print('All requested finite checks passed. No conclusion about the full automorphism group is inferred.')
