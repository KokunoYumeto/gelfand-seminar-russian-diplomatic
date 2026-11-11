"""Exact checks of editorial corrections; finite checks are not general theorems.
Run: python work/virasoro/check_formulas.py
The symbolic derivations and hypothesis restrictions remain in items.json.
"""
from pathlib import Path
import sympy as S
log=[]
def say(s):
    log.append(str(s)); print(s)
def dd(f,x,i):
    swapped=f.xreplace({x[i]:x[i+1],x[i+1]:x[i]})
    return S.cancel((f-swapped)/(x[i]-x[i+1])).expand()
say('Exact editorial checks, SymPy '+S.__version__)
for n in range(2,5):
    x=S.symbols('x1:'+str(n+1)); N=n*(n-1)//2
    es=[sum(S.prod(t) for t in __import__('itertools').combinations(x,k)) for k in range(1,n+1)]
    G=S.groebner(es,*x,domain=S.QQ)
    top=S.prod(x[i]**(n-1-i) for i in range(n-1))
    delta=S.prod(x[i]-x[j] for i in range(n) for j in range(i+1,n))
    rho=sum((n-1-i)*x[i] for i in range(n))
    r1=G.reduce((delta-S.factorial(n)*top).expand())[1]
    r2=G.reduce((rho**N-S.factorial(N)*top).expand())[1]
    assert r1==r2==0
    f=top
    word=[i for length in range(n-1,0,-1) for i in range(length)]
    for i in word:f=dd(f,x,i)
    assert f==1
    say(f'n={n}: Vandermonde/n! and rho^N/N! equal top class modulo symmetric ideal; reduced top-word gives 1')
x=S.symbols('x1:4'); f=x[0]**5*x[1]**3*x[2]+x[0]**2*x[2]**4
assert dd(dd(f,x,0),x,0)==0
assert S.expand(dd(dd(dd(f,x,0),x,1),x,0)-dd(dd(dd(f,x,1),x,0),x,1))==0
assert dd(x[0],x,0)==1
say('Divided differences: square-zero and braid checked on a nontrivial polynomial; notebook denominator sends x1 to -1')
for d in (1,2,26):
    u=S.symbols('u0:'+str(d)); creation=sum(t*t for t in u)
    correct=S.Rational(1,2)*sum(S.diff(creation/2,t,2) for t in u)
    unscaled=sum(S.diff(creation,t,2) for t in u)
    assert correct==S.Rational(d,2) and unscaled==2*d
    say(f'd={d}: L2 L-2 vacuum={correct}; missing both halves gives {unscaled}')
u,k,zz=S.symbols('u k zz')
psi=u**3+u+1
for n in range(1,7):
    E=S.exp(k*u*zz**n/n)
    badE=S.exp(k*u*zz**n)
    assert S.simplify(n*S.diff(E*psi,u)-E*n*S.diff(psi,u)-k*zz**n*E*psi)==0
    assert S.simplify(n*S.diff(badE*psi,u)-badE*n*S.diff(psi,u)-n*k*zz**n*badE*psi)==0
say('Creation exponential: differential-operator commutators on u^3+u+1 checked for n=1..6; 1/n gives k z^n, omitted denominator gives n k z^n (first failure n=2)')
z=S.symbols('z'); X={i:S.Symbol('X'+('m' if i<0 else 'p')+str(abs(i))) for i in range(-4,5)}
series=sum(v*z**i for i,v in X.items())
count=0
for n in range(-2,3):
    shifted=S.expand(z**n*series)
    for i in range(-2,3):
        assert shifted.coeff(z,i)==X[i-n]
        count+=1
say(f'Laurent convention z^i: {count} coefficient checks give X_(i-n); at i=1,n=2 the coefficient is X_-1, not X_3')
g=S.diag(-1,1); zero=S.Matrix([0,0]); null=S.Matrix([1,1])
assert (null.T*g*null)[0]==0 and (zero.T*g*zero)[0]==0
assert (zero.T*g).rank()==0 and (null.T*g).rank()==1
say('Null momentum correction: equal norms 0; level-one L1 ranks 0 and 1 for zero and nonzero null momentum')
a,b=S.symbols('a b',real=True)
integral=S.integrate(S.integrate((1-a*b)**2,(a,0,1)),(b,0,1))
series_value=S.hyperexpand(S.hyper([1,1,-2],[2,2],1))
assert integral==series_value==S.Rational(11,18)
say('Five-point editorial Euler model: finite e=-2 specialization matches 3F2 exactly at 11/18; not a verification of unspecified notebook exponents')
say('All checks passed. These finite examples audit signs/constants; general identities are justified separately by source theorems or algebraic derivation.')
Path('work/virasoro/check_formulas_output.txt').write_text('\n'.join(log)+'\n')
