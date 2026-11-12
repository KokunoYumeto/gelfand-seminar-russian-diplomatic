"""Exact checks for real-linear complexification of transverse 2-planes.

These computations support a rederivation of known results, not a novelty
claim.  Full 4x4 invariance equations provide a check independent of the
normal-form centralizer calculation used in the prose proof.
"""
from pathlib import Path
import sympy as s

I=s.eye(2)

def invariant_algebra(matrices):
    # P1=X, P2=Y, P3=graph(I), subsequent planes graph(A).
    variables=s.symbols('x0:16')
    X=s.Matrix(4,4,variables)
    planes=[s.Matrix.vstack(I,s.zeros(2)),s.Matrix.vstack(s.zeros(2),I),s.Matrix.vstack(I,I)]
    planes.extend(s.Matrix.vstack(I,A) for A in matrices)
    equations=[]
    for P in planes:
        annihilator=s.Matrix.hstack(*P.T.nullspace()).T
        equations.extend(annihilator*X*P)
    coefficient,_=s.linear_eq_to_matrix(equations,variables)
    basis=[s.Matrix(4,4,v) for v in coefficient.nullspace()]
    return basis,planes

def main():
    print('SymPy',s.__version__)
    J=s.Matrix([[0,-1],[1,0]])
    cases=[('scalar',[2*I],True),('distinct real eigenvalues',[s.diag(2,3)],False),
           ('real Jordan block',[s.Matrix([[2,1],[0,2]])],False),('nonreal eigenvalues',[J],True),
           ('commuting family',[J,2*I+3*J],True),
           ('noncommuting family',[J,s.Matrix([[0,-2],[s.Rational(1,2),0]])],False)]
    for name,matrices,expected in cases:
        all_graphs=[s.zeros(2),I]+matrices
        assert all(A.det()!=0 and (A-I).det()!=0 for A in matrices)
        assert all((A-B).det()!=0 for i,A in enumerate(all_graphs) for B in all_graphs[i+1:])
        nonscalar=next((A for A in matrices if A != A[0,0]*I),None)
        if nonscalar is None:
            result=True; B=J
        else:
            delta=s.trace(nonscalar)**2-4*nonscalar.det()
            result=bool(delta<0 and all(A*nonscalar == nonscalar*A for A in matrices))
            B=(2*nonscalar-s.trace(nonscalar)*I)/s.sqrt(-delta) if result else None
        assert result == expected
        basis,planes=invariant_algebra(matrices)
        if result:
            full=s.diag(B,B)
            assert s.simplify(full**2+s.eye(4)) == s.zeros(4)
            for P in planes:
                annihilator=s.Matrix.hstack(*P.T.nullspace()).T
                assert s.simplify(annihilator*full*P) == s.zeros(2)
        print(name,'centralizer criterion=',result,'full invariant algebra dimension=',len(basis))
        if name == 'noncommuting family':
            assert len(basis)==1 and basis[0] == s.eye(4)
        if name == 'distinct real eigenvalues':
            # All invariant operators are diag(a,b,a,b); their squares cannot
            # equal -I over R.  This checks impossibility directly in R4.
            for X in basis:
                assert X.is_diagonal()
            print('Direct obstruction: invariant J is diagonal over R; diagonal squares are nonnegative.')
        if name == 'real Jordan block':
            for X in basis:
                assert X.is_upper
            print('Direct obstruction: invariant J is real upper triangular; its diagonal squares cannot be -1.')
    t=s.symbols('t',real=True)
    A=s.diag(2,2+t)
    print('Transverse deformation diag(2,2+t): det A=',s.factor(A.det()),'det(A-I)=',s.factor((A-I).det()),'discriminant=',s.factor(s.trace(A)**2-4*A.det()))
    epsilon=s.symbols('epsilon',positive=True)
    A=s.Matrix([[2,1],[-epsilon,2]])
    print('Nonclosed complexifiable locus example: det A=',A.det(),'det(A-I)=',(A-I).det(),'discriminant=',s.factor(s.trace(A)**2-4*A.det()))
    print('PASS. Existence is finer than the intersection lattice; known four-plane classification is rederived, not claimed as new.')

if __name__ == '__main__':
    main()
