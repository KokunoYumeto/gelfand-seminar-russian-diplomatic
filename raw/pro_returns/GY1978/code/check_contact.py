"""Independent symbolic audit of the literal P000835 contact formula.

The Jacobiator convention is [f,[g,h]]+[g,[h,f]]+[h,[f,g]].
No numerical sampling is used for the general-function identity.
"""
import sympy as s

x, y, z, epsilon = s.symbols('x y z epsilon')
xyz = (x,y,z)
f,g,h = [s.Function(name)(x,y,z) for name in ('f','g','h')]

def bracket(f,g,sign):
    X = lambda u: s.diff(u,x)
    Y = lambda u: s.diff(u,y)+sign*x*s.diff(u,z)
    Z = lambda u: s.diff(u,z)
    return f*Z(g)-g*Z(f)+X(f)*Y(g)-X(g)*Y(f)

def jacobi(f,g,h,sign):
    return s.expand(bracket(f,bracket(g,h,sign),sign)
        +bracket(g,bracket(h,f,sign),sign)
        +bracket(h,bracket(f,g,sign),sign))

det = s.det(s.Matrix([[s.diff(u,v) for v in xyz] for u in (f,g,h)]))
assert s.simplify(jacobi(f,g,h,epsilon)-(epsilon+1)*det)==0
print('General Jacobiator = (epsilon+1) det(rows grad(f), grad(g), grad(h)).')
for sign in (1,-1):
    values=[s.expand(bracket(a,b,sign)) for a,b in ((x,y),(y,z),(z,x))]
    print('epsilon =',sign,': [x,y], [y,z], [z,x] =',values,
          '; cyclic [f,[g,h]] =',jacobi(x,y,z,sign))
    print('Opposite nesting [[f,g],h] =',-jacobi(x,y,z,sign))

# A second symbolic check uses unrelated polynomial triples.
triples=[(x*x+y,y*z+x,z*z+x*y),
         (x*z+y*y,x*y+z,y*z+x*x)]
for num,(a,b,c) in enumerate(triples,1):
    localdet=s.det(s.Matrix([[s.diff(u,v) for v in xyz] for u in (a,b,c)]))
    assert s.expand(jacobi(a,b,c,1)-2*localdet)==0
    assert jacobi(a,b,c,-1)==0
    print('Polynomial triple',num,': plus-model Jacobiator =',s.expand(jacobi(a,b,c,1)),
          '; corrected-model Jacobiator = 0.')
print('All symbolic assertions passed. SymPy',s.__version__)
