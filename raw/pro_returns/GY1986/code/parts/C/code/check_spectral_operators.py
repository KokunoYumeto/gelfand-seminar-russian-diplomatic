"""Two exact checks of the P001362 operator pair (our computation).

The first composes differential operators using the Leibniz formula. The
second evaluates both compositions on vector monomials by direct repeated
differentiation and compares at four nonzero rational spectral parameters.
No result is inferred numerically. The uncorrected manuscript matrix is also
tested to exhibit the failure, rather than merely checking an emendation.
"""
import sympy as s
from math import comb

z=s.symbols('z', nonzero=True)
I=s.diag(1,-1)
A=s.Matrix([[0,1],[-1,0]])
A_bad=s.Matrix([[0,1],[1,0]])

def compose(p,q):
    out={}
    for i,a in p.items():
        for j,b in q.items():
            for k in range(i+1):
                order=i-k+j
                out[order]=out.get(order,s.zeros(2))+comb(i,k)*a*b.diff(z,k)
    return {k:v.applyfunc(s.simplify) for k,v in out.items()}

def ops(a):
    c=-(I+a)/2
    return {1:I,0:a/z},{2:I,1:a/z,0:c/z**2}

def symbolic(a):
    p,q=ops(a);pq,qp=compose(p,q),compose(q,p)
    return {k:(pq.get(k,s.zeros(2))-qp.get(k,s.zeros(2))).applyfunc(s.simplify)
            for k in sorted(set(pq)|set(qp))}

correct=symbolic(A)
bad=symbolic(A_bad)
assert all(v==s.zeros(2) for v in correct.values())
assert bad[0]==2*s.eye(2)/z**3
assert all(v==s.zeros(2) for k,v in bad.items() if k!=0)
print('Leibniz coefficient check: corrected commutator is zero.')
print('Manuscript matrix commutator:',bad[0])

def m1_direct(f,a):
    return I*f.diff(z)+a*f/z

def m2_direct(f,a):
    return I*f.diff(z,2)+a*f.diff(z)/z-(I+a)*f/(2*z**2)

cases=0
for a,expected_multiplier in [(A,0),(A_bad,2)]:
    for degree in range(7):
        for basis in [s.Matrix([1,0]),s.Matrix([0,1])]:
            f=z**degree*basis
            residual=m1_direct(m2_direct(f,a),a)-m2_direct(m1_direct(f,a),a)
            for point in [s.Rational(1),s.Rational(-2),s.Rational(3,2),s.Rational(5,3)]:
                value=residual.subs(z,point).applyfunc(s.simplify)
                expected=(expected_multiplier*f/z**3).subs(z,point)
                assert value==expected,(degree,basis,point,value,expected)
                cases+=1
print(f'Independent direct-action check: {cases} exact rational vector comparisons passed.')
