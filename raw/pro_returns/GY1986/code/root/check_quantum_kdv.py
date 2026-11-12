"""Independent PBW calculation of the level-two quantum KdV charge.

All calculations are exact over Q(c,h).  Negative-mode words are reduced
using Virasoro commutators, rather than by entering the proposed matrix.
"""
from functools import lru_cache
import json
from pathlib import Path
import sympy as s

c,h=s.symbols('c h')

def add(target,source,factor=1):
    for word,coefficient in source.items():
        target[word]=s.expand(target.get(word,0)+factor*coefficient)
    return {word:coefficient for word,coefficient in target.items() if coefficient != 0}

@lru_cache(None)
def normal(word):
    for i in range(len(word)-1):
        a,b=word[i:i+2]
        if a < b:
            swapped=word[:i]+(b,a)+word[i+2:]
            fused=word[:i]+(a+b,)+word[i+2:]
            return add(dict(normal(swapped)),normal(fused),b-a)
    return {word:s.Integer(1)}

def prepend(n,vector):
    result={}
    for word,coefficient in vector.items():
        result=add(result,normal((n,)+word),coefficient)
    return result

@lru_cache(None)
def act(m,word):
    if m < 0:
        return normal((-m,)+word)
    if m == 0:
        return {word:h+sum(word)}
    if not word:
        return {}
    a,rest=word[0],word[1:]
    result=prepend(a,act(m,rest))
    result=add(result,act(m-a,rest),m+a)
    if m == a:
        result=add(result,{rest:s.Integer(1)},c*s.Rational(m**3-m,12))
    return result

def act_vector(m,vector):
    result={}
    for word,coefficient in vector.items():
        result=add(result,act(m,word),coefficient)
    return result

def partitions(n,largest=None):
    if n == 0:
        yield ()
        return
    for first in range(min(n,largest or n),0,-1):
        for tail in partitions(n-first,first):
            yield (first,)+tail

def gram(left,right):
    v={right:s.Integer(1)}
    for m in left:
        v=act_vector(m,v)
    return s.factor(v.get((),0))

def charge(level):
    basis=list(partitions(level))
    scalar=(h+level)**2-(c+2)*(h+level)/12+c*(5*c+22)/2880
    columns=[]
    for word in basis:
        v={word:scalar}
        for n in range(1,level+1):
            v=add(v,prepend(n,act(n,word)),2)
        columns.append([s.factor(v.get(b,0)) for b in basis])
    return basis,s.Matrix.hstack(*[s.Matrix(x) for x in columns]),scalar

def main():
    print('SymPy',s.__version__)
    print('Convention: [L_m,L_n]=(m-n)L_(m+n)+c(m^3-m)delta_(m+n,0)/12')
    basis,I3,q=charge(2)
    B=s.simplify(I3-q*s.eye(2))
    expected=s.Matrix([[8*h+c,12*h],[6,8*h+4]])
    assert B == expected
    G=s.Matrix([[gram(x,y) for y in basis] for x in basis])
    assert s.simplify(G*I3-I3.T*G) == s.zeros(2)
    discriminant=s.factor(s.trace(B)**2-4*B.det())
    assert s.simplify(discriminant-((c-4)**2+288*h)) == 0
    print('PBW basis:',basis)
    print('I3 scalar q_2:',q)
    print('I3 - q_2 I:',B)
    print('Contravariant Gram matrix:',G)
    print('Gram determinant:',s.factor(G.det()))
    print('Eigenvalue discriminant:',discriminant)
    print('Gram symmetry G I3 = I3^T G: PASS')
    parameters={c:s.Integer(1),h:-s.Rational(1,32)}
    specialized=I3.subs(parameters)
    eigenvalue=s.trace(specialized)/2
    nilpotent=specialized-eigenvalue*s.eye(2)
    assert nilpotent != s.zeros(2) and nilpotent**2 == s.zeros(2)
    assert G.subs(parameters).det() == -s.Rational(81,1024)
    print('c=1, h=-1/32 I3:',specialized)
    print('Repeated eigenvalue:',eigenvalue)
    print('Nonzero nilpotent part:',nilpotent)
    print('Nilpotent part squared:',nilpotent**2)
    print('Specialized Gram determinant:',G.subs(parameters).det())
    # A different algebraic check: solve annihilation equations for a singular
    # level-two vector, and separately check level-one nonvanishing.
    annihilation=s.Matrix([[3,4*h+2],[4*h+c/2,6*h]])
    assert annihilation.subs(parameters).det() != 0
    assert (2*h).subs(parameters) != 0
    print('Level-one singular-vector obstruction 2h:',(2*h).subs(parameters))
    print('Level-two singular-vector equation determinant:',annihilation.subs(parameters).det())
    # Rerun the PBW algorithm at different grades and parameters; this is a
    # meaningful check of the commutator implementation, not evidence for
    # any all-grade spectral claim.
    for level in [1,3,4]:
        bs,M,_=charge(level)
        for cv,hv in [(s.Integer(1),s.Integer(2)),(-s.Integer(2),s.Rational(1,8))]:
            sub={c:cv,h:hv}
            H=s.Matrix([[gram(x,y).subs(sub) for y in bs] for x in bs])
            T=M.subs(sub)
            assert H*T == T.T*H
        print('Independent Gram-symmetry check, level',level,'dimension',len(bs),': PASS')
    print('All exact checks passed. No all-level diagonalizability is asserted.')

if __name__ == '__main__':
    main()
