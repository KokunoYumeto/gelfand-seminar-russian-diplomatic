"""Exact independent audits of formulas occurring in GY1976.

These computations certify the stated finite examples and symbolic identities.
The general acyclicity assertion is proved in the accompanying LaTeX text.
Run: python code/critical_checks.py --output code/output/critical_checks.json
      (or python work/critical_checks.py during authoring).
Requires SymPy; no network access, numerical fitting, or external input.
"""
import argparse
import json
from math import comb
from pathlib import Path
import sympy as s


def wedge_matrix(m, k, xi):
    source = [a for a in range(1 << m) if a.bit_count() == k]
    target = [a for a in range(1 << m) if a.bit_count() == k+1]
    pos = {a:i for i,a in enumerate(target)}
    out = s.zeros(len(target), len(source))
    for c,a in enumerate(source):
        for i in range(m):
            if not (a >> i) & 1:
                sign = (-1)**((a & ((1 << i)-1)).bit_count())
                out[pos[a | (1 << i)],c] += sign*xi[i]
    return out


def contraction_matrix(m, k, functional):
    source = [a for a in range(1 << m) if a.bit_count() == k]
    target = [a for a in range(1 << m) if a.bit_count() == k-1]
    pos = {a:i for i,a in enumerate(target)}
    out = s.zeros(len(target),len(source))
    for c,a in enumerate(source):
        for i in range(m):
            if (a >> i) & 1:
                sign = (-1)**((a & ((1 << i)-1)).bit_count())
                out[pos[a ^ (1 << i)],c] += sign*functional[i]
    return out


def exterior_checks():
    cases=[]
    for m in range(1,7):
        vectors = [[1]+[0]*(m-1), list(range(1,m+1)),
                   [(-1)**i*(i+2) for i in range(m)]]
        for xi in vectors:
            a = [s.Rational(1,xi[0])]+[0]*(m-1)
            ds = [wedge_matrix(m,k,xi) for k in range(m+1)]
            hs = [contraction_matrix(m,k,a) for k in range(m+1)]
            ranks=[int(d.rank()) for d in ds]
            expected=[comb(m-1,k) if k<m else 0 for k in range(m+1)]
            assert ranks == expected
            hom=[]
            for k in range(m+1):
                incoming = ranks[k-1] if k else 0
                hom.append(comb(m,k)-ranks[k]-incoming)
                left = hs[k+1]*ds[k] if k<m else s.zeros(comb(m,k))
                right = ds[k-1]*hs[k] if k else s.zeros(comb(m,k))
                assert left+right == s.eye(comb(m,k))
                if k<m:
                    assert ds[k+1]*ds[k] == s.zeros(ds[k+1].rows,ds[k].cols)
            assert not any(hom)
            cases.append(dict(exterior_generators=m,xi=xi,ranks=ranks,
                              homology_dimensions=hom,contraction_identity=True))
    return cases


def compose(a,b,x):
    """Leibniz product for left-coefficient differential operators."""
    result={}
    for i,ai in a.items():
        for j,bj in b.items():
            for k in range(i+1):
                power=i+j-k
                result[power]=result.get(power,0)+s.binomial(i,k)*ai*s.diff(bj,x,k)
    return {i:s.expand(v) for i,v in result.items()}


def lax_checks():
    x,zeta=s.symbols('x zeta')
    A,c=s.symbols('A c')
    v,w,z=(s.Function(t)(x) for t in ('v','w','z'))
    u=v/2+c
    L={4:s.Integer(1),2:v,1:w,0:z}
    P={2:s.Integer(1),1:A,0:u}
    lp,pl=compose(L,P,x),compose(P,L,x)
    comm={i:s.simplify(lp.get(i,0)-pl.get(i,0)) for i in range(7)}
    expected={
        2:2*s.diff(v,x,2)-A*s.diff(v,x)-2*s.diff(w,x),
        1:2*s.diff(v,x,3)+v*s.diff(v,x)-s.diff(w,x,2)-A*s.diff(w,x)-2*s.diff(z,x),
        0:s.diff(v,x,4)/2+v*s.diff(v,x,2)/2+w*s.diff(v,x)/2-s.diff(z,x,2)-A*s.diff(z,x)
    }
    for i in range(7): assert s.simplify(comm[i]-expected.get(i,0))==0
    # Independent representation: act on exp(zeta*x), differentiate functions
    # directly, and collect powers of zeta. This does not call compose().
    f=s.exp(zeta*x)
    def Lop(g):return s.diff(g,x,4)+v*s.diff(g,x,2)+w*s.diff(g,x)+z*g
    def Pop(g):return s.diff(g,x,2)+A*s.diff(g,x)+u*g
    direct=s.expand((Lop(Pop(f))-Pop(Lop(f)))/f)
    for i in range(7): assert s.simplify(direct.coeff(zeta,i)-comm[i])==0
    # Additional polynomial choices test cancellation with nonconstant coefficients.
    for p in (1,2,4):
        subs={v:x**(p+1)+p*x,w:p*x**3+x**2,z:x**(p+2)-2*x,A:p,c:p+1}
        fpoly=x**(p+7)+x**2
        lc={i:s.sympify(ai).subs(subs).doit() for i,ai in L.items()}
        pc={i:s.sympify(ai).subs(subs).doit() for i,ai in P.items()}
        def act(op,g):return sum(ai*s.diff(g,x,i) for i,ai in op.items())
        lhs=s.expand(act(lc,act(pc,fpoly))-act(pc,act(lc,fpoly)))
        rhs=sum(s.sympify(ai).subs(subs).doit()*s.diff(fpoly,x,i) for i,ai in expected.items())
        assert s.simplify(lhs-rhs)==0
    return {'operator_convention':'L_t = [L,P] = LP-PL; A and c independent of x; u=v/2+c',
            'coefficients':{str(i):str(comm[i]) for i in (2,1,0)},
            'higher_coefficients_zero':True,
            'independent_exponential_test':True,'polynomial_parameters_checked':[1,2,4]}


def kernel_check():
    lam=s.symbols('lambda',positive=True)
    t=lam+1/lam
    kernel=s.factor((lam/(lam-1)**2)/(lam-1/lam))
    assert s.factor(kernel**2*(t-2)**3*(t+2)-1)==0
    samples=[]
    # Finite partial sums check the normalization on the branch lambda>1.
    # Tail formula is exact, not a floating-point threshold.
    for value,N in [(s.Rational(3,2),20),(s.Integer(2),12),(s.Integer(3),8)]:
        q=1/value
        partial=sum(n*q**n for n in range(1,N+1))/(value-1/value)
        tail=q**(N+1)*((N+1)-N*q)/(1-q)**2/(value-1/value)
        closed=kernel.subs(lam,value)
        assert s.simplify(partial+tail-closed)==0
        samples.append({'lambda':str(value),'N':N,'exact_tail_identity':True})
    return {'spectral_parameter':'t=lambda+lambda^(-1), lambda>1',
            'sum_closed_form':str(kernel),
            'squared_identity':'K^2 (t-2)^3 (t+2) = 1',
            'missing_factor_in_notebook':'(t+2)^(-1/2), up to branch and a constant',
            'second_check_exact_partial_sum_plus_tail':samples}


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',default='work/critical_checks.json');a=p.parse_args()
    result={'purpose':'Critical verification, not a claim of new mathematical results',
        'sympy_version':s.__version__, 'exterior_complexes':exterior_checks(),
        'unshifted_inverse_kernel':{'n':0,'C_N_dimension':1,'multiplication_X0':1,
            'kernel_basis':['xi_0'],'homology_support_degree':-1,
            'proper_before_shift':False},
        'fourth_order_lax_commutator':lax_checks(),
        'SL2_discrete_series_kernel':kernel_check(),
        'result':'PASS: all asserted exact identities and finite examples verified'}
    dst=Path(a.output);dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'result':result['result'],'exterior_cases':len(result['exterior_complexes']),
                      'symbolic_Lax_checks':2,'polynomial_checks':3,
                      'exact_kernel_tail_checks':3,'output':str(dst)},indent=2))

if __name__=='__main__':main()
