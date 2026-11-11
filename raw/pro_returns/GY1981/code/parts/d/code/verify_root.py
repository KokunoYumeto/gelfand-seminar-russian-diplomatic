"""Independent finite checks for the root block. No numerical search proves optimality."""
import json
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import differential_evolution
import sympy as sp

np.set_printoptions(precision=12,suppress=True)
out=[]
def report(s):
    print(s,flush=True);out.append(str(s))
def norm(a):return np.linalg.norm(a,2)

report(f'numpy={np.__version__}; scipy={scipy.__version__}; sympy={sp.__version__}')
report('Random projector checks: seeds 1982 and 2026; n=1,2,3,6,9; 4 samples each.')
max_projection_error=0.0;max_gap_error=0.0;max_scalar_excess=0.0
for seed in [1982,2026]:
    rng=np.random.default_rng(seed)
    for n in [1,2,3,6,9]:
        for trial in range(4):
            U,_=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
            S=U@U.T
            Q=np.vstack([U.real,U.imag])
            P=Q@Q.T
            P_formula=.5*np.block([[np.eye(n)+S.real,S.imag],[S.imag,np.eye(n)-S.real]])
            max_projection_error=max(max_projection_error,norm(P-P_formula))
            theta=rng.uniform(0,2*np.pi,n)
            R=np.vstack([np.diag(np.cos(theta)),np.diag(np.sin(theta))])
            gap=norm(P-R@R.T)
            complex_gap=.5*norm(S-np.diag(np.exp(2j*theta)))
            max_gap_error=max(max_gap_error,abs(gap-complex_gap))
            angles=np.sort(np.mod(np.angle(np.linalg.eigvals(S)),2*np.pi))
            gaps=np.diff(np.r_[angles,angles[0]+2*np.pi])
            j=int(np.argmax(gaps)); phi=angles[j]+gaps[j]/2+np.pi
            scalar_gap=.5*norm(S-np.exp(1j*phi)*np.eye(n))
            bound=np.cos(np.pi/(2*n))
            max_scalar_excess=max(max_scalar_excess,scalar_gap-bound)
assert max_projection_error<1e-12 and max_gap_error<1e-12 and max_scalar_excess<1e-12
report(f'max projector formula error={max_projection_error:.3e}')
report(f'max real/complex norm discrepancy={max_gap_error:.3e}')
report(f'max scalar bound excess={max_scalar_excess:.3e}')

S=np.array([[0.,1.],[1.,0.]])
report(f'swap sharp example gap with D=iI={.5*norm(S-1j*np.eye(2)):.12f}')
assert abs(.5*norm(S-1j*np.eye(2))-2**-.5)<1e-13

report('Coordinatewise example (not a counterexample to existential approximation):')
for n in [2,3,7,11]:
    v=np.ones(n)/np.sqrt(n)
    P=np.block([[np.outer(v,v),np.zeros((n,n))],[np.zeros((n,n)),np.eye(n)-np.outer(v,v)]])
    F=np.diag(np.r_[np.zeros(n),np.ones(n)])
    distances=np.sqrt(np.diag(np.eye(2*n)-P)[n:])
    assert np.max(abs(distances-1/np.sqrt(n)))<1e-12
    assert abs(norm(P-F)-1)<1e-12
    report(f'n={n}, each distance={distances[0]:.12f}, span gap={norm(P-F):.12f}')

report('Fourier block counterexamples: exact theorem uses all odd m>=3; finite numerical checks follow.')
for m in [3,5,7,11]:
    V=np.exp(2j*np.pi*np.outer(np.arange(m),np.arange(m))/m)/np.sqrt(m)
    S=np.block([[np.zeros((m,m)),V],[V.T,np.zeros((m,m))]])
    Qc=np.block([[V,-1j*V],[np.eye(m),1j*np.eye(m)]])/np.sqrt(2)
    Q=np.vstack([Qc.real,Qc.imag])
    J=np.block([[np.zeros((2*m,2*m)),-np.eye(2*m)],[np.eye(2*m),np.zeros((2*m,2*m))]])
    assert norm(Q.T@Q-np.eye(2*m))<1e-12
    assert norm(Q.T@J@Q)<1e-12
    assert norm(Qc@Qc.T-S)<1e-12
    lower=.5*np.sqrt(2+np.sqrt(2-2/np.sqrt(m)))
    rng=np.random.default_rng(1981+m)
    for k in range(7):
        a=np.exp(1j*rng.uniform(0,2*np.pi,m));b=np.exp(1j*rng.uniform(0,2*np.pi,m))
        C=V.conj()@np.diag(b)+np.diag(a.conj())@V
        D=np.diag(np.r_[a,b])
        assert abs(norm(S-D)**2-(2+norm(C)))<1e-11
        assert np.linalg.norm(C,'fro')**2>=2*m-2*np.sqrt(m)-1e-11
        assert .5*norm(S-D)>=lower-1e-12
    report(f'm={m}, n={2*m}, rigorous lower bound={lower:.12f}, norm(V entrywise-squared)={norm(V*V):.12f}')
report(f'limiting universal lower bound cos(pi/8)={np.cos(np.pi/8):.12f}')
report('Optional numerical minimization for m=3: feasible values are upper bounds only.')
m=3
V=np.exp(2j*np.pi*np.outer(np.arange(m),np.arange(m))/m)/np.sqrt(m)
S=np.block([[np.zeros((m,m)),V],[V.T,np.zeros((m,m))]])
for seed in [1981,2026]:
    fit=differential_evolution(lambda theta:.5*norm(S-np.diag(np.exp(1j*theta))),[(0,2*np.pi)]*(2*m),rng=np.random.default_rng(seed),maxiter=250,popsize=10,tol=1e-8,polish=True)
    report(f'seed={seed}; feasible gap={fit.fun:.12f}; optimizer success={fit.success}; not a certified optimum')

report('Symbolic vector-calculus principal-symbol multiplication:')
x,y,z=sp.symbols('x y z',real=True)
v=sp.Matrix([x,y,z]);C=sp.Matrix([[0,-z,y],[z,0,-x],[-y,x,0]])
q=x*x+y*y+z*z
M=sp.zeros(4);M[0,1:4]=v.T;M[1:4,0]=v;M[1:4,1:4]=C
expected=sp.diag(q,0,0,0);expected[1:4,1:4]=2*v*v.T-q*sp.eye(3)
assert sp.simplify(M*M-expected)==sp.zeros(4)
N=M.copy();N[0,1:4]=-v.T
assert sp.simplify(N*N+q*sp.eye(4))==sp.zeros(4)
report('All-positive matrix square = diag(q, 2vv^T-qI3); corrected matrix square = -qI4: exact PASS.')

report('Shift-residue coefficient checked by direct differentiation of the finite Pochhammer product:')
s=sp.symbols('s')
for k in range(7):
    for mu in range(1,7):
        j=k+mu
        lhs=sp.diff((-1)**j*sp.prod(s+r for r in range(j))/sp.factorial(j),s).subs(s,-k)
        rhs=sp.Rational((-1)**mu,mu)/sp.binomial(k+mu,k)
        assert sp.simplify(lhs-rhs)==0
report('42 exact checks k=0..6, mu=1..6: coefficient=(-1)^mu/[mu binom(k+mu,k)], multiplied by t^(k+mu): PASS.')
report('All assertions passed. Numerical checks corroborate the independently proved statements; they do not establish a uniform upper bound.')
Path(__file__).with_name('verify_root_output.txt').write_text('\n'.join(out)+'\n')
