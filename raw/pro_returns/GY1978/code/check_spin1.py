"""Exact critical audit of notebook P818 (14), P819 (16).
Necessary condition is [h12+h23,[h12,h23]]=K23-K12 for
an analytic regular difference-form R matrix. This checks only that class.
"""
import sympy as s
from pathlib import Path
S=[s.Matrix([[0,0,0],[0,0,-1],[0,1,0]]),s.Matrix([[0,0,1],[0,0,0],[-1,0,0]]),s.Matrix([[0,-1,0],[1,0,0],[0,0,0]])]
I=s.eye(3)
def comm(a,b): return a*b-b*a
assert comm(S[0],S[1])==S[2]
assert comm(S[1],S[2])==S[0]
assert comm(S[2],S[0])==S[1]
x=sum([s.kronecker_product(a,a) for a in S],s.zeros(9))
t=s.symbols('t')
h=x*x+t*x
h12=s.kronecker_product(h,I);h23=s.kronecker_product(I,h)
D=comm(h12+h23,comm(h12,h23)).applyfunc(s.factor)
trip=lambda i:(i//9,(i//3)%3,i%3)
entries=[]
for i in range(27):
 for j in range(27):
  if trip(i)[0]!=trip(j)[0] and trip(i)[2]!=trip(j)[2] and D[i,j]!=0:
   entries.append((trip(i),trip(j),s.factor(D[i,j])))
print('Generators satisfy [S1,S2]=S3 and cyclic identities.')
print('Eigenvalues of X=sum S_a tensor S_a:',x.eigenvals())
print('Eigenvalues of h=X^2-2X:',h.subs(t,-2).eigenvals())
print('Forbidden simultaneous first/third-site transitions:')
for r,c,v in entries[:6]: print(r,c,v,'at t=-2:',v.subs(t,-2))
assert entries
r,c,v=entries[0]
print('Witness:',r,c,v,'=',v.subs(t,-2))
assert v.subs(t,-2)!=0
# Independent verification: construct real cross-product action directly using epsilon;
# use explicit nested index sums instead of Kronecker products and matrix products.
eps=lambda a,b,c:s.LeviCivita(a,b,c)
x2=s.Matrix(9,9,lambda row,col:sum(eps(row//3,a,col//3)*eps(row%3,a,col%3) for a in range(3)))
assert x2==x
hh=s.Matrix(9,9,lambda i,j:sum(x2[i,k]*x2[k,j] for k in range(9))-2*x2[i,j])
A=lambda u,v:hh[3*u[0]+u[1],3*v[0]+v[1]]*int(u[2]==v[2])
B=lambda u,v:int(u[0]==v[0])*hh[3*u[1]+u[2],3*v[1]+v[2]]
T=[trip(i) for i in range(27)]
C=lambda u,v:sum(A(u,k)*B(k,v)-B(u,k)*A(k,v) for k in T)
val=sum((A(r,k)+B(r,k))*C(k,c)-C(r,k)*(A(k,c)+B(k,c)) for k in T)
print('Independent epsilon-index contraction witness:',val)
assert val==v.subs(t,-2)
# The six explicit words used in the displayed finite proof. This calculation
# independently uses flip/contraction tensors, not the generator construction.
a,c=s.symbols('a c')
P=s.zeros(9);K0=s.zeros(9)
for i in range(3):
 for j in range(3):
  P[3*j+i,3*i+j]=1
  if i==j:
   for k in range(3):K0[3*k+k,3*i+j]=1
assert x==K0-P
AA=s.kronecker_product(a*K0+c*P,I)
BB=s.kronecker_product(I,a*K0+c*P)
print('Six-term proof table, row001 column212, h=aK+cP:')
for name,mat in [('AAB',AA*AA*BB),('ABA',AA*BB*AA),('BAA',BB*AA*AA),('BAB',BB*AA*BB),('BBA',BB*BB*AA),('ABB',AA*BB*BB)]:
 print(name,s.factor(mat[1,23]))
# Verify controls by solving K from partial traces, then checking full identity.
def ptr_first(M): return s.Matrix(9,9,lambda i,j:sum(M[9*a+i,9*a+j] for a in range(3)))
def ptr_last_pair(M): return s.Matrix(3,3,lambda i,j:sum(M[3*a+i,3*a+j] for a in range(3)))
for tv in [-2,-1,0,1,2]:
 Dt=D.subs(t,tv)
 # If D=I tensor K - K tensor I, partial trace over first tensor factor gives
 # Q=3K-tr_1(K) tensor I. Impose tr(K)=0, then tr_1(Q)=3tr_1(K).
 Q=ptr_first(Dt)
 K=(Q+s.kronecker_product(ptr_last_pair(Q)/3,I))/3
 residual=Dt-(s.kronecker_product(I,K)-s.kronecker_product(K,I))
 nonzero=sum(v!=0 for v in residual)
 print('t=',tv,'full condition residual nonzero entries=',nonzero)
