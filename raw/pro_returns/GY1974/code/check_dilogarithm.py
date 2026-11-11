"""Two independent checks of the notebook's symmetric dilogarithm integral.
The numerical agreement checks the reading, and is not an identity proof.
Uses only Python standard-library decimal and math.
"""
from decimal import Decimal, localcontext
import math

def series(precision):
 with localcontext() as c:
  c.prec=precision
  a=Decimal(5).sqrt()-2
  odd_sum=Decimal(0)
  power=a
  for j in range(precision*2):
   odd_sum+=power/Decimal(2*j+1)**2
   power*=a*a
  value=a.ln()*((1+a)/(1-a)).ln()-4*odd_sum
  print('decimal precision',precision,'series integral',value)
  print('tail absolute bound <',4*power/((1-a*a)*Decimal(4*precision+1)**2))

def quadrature(n):
 # t=a exp(-v) removes the logarithmic endpoint singularity;
 # integrate f(t)+f(-t) with the Jacobian over 0<=v<=80.
 a=math.sqrt(5)-2
 h=80/n
 def g(v):
  t=a*math.exp(-v)
  return 2*t*math.log(t)/(1-t*t)+math.log1p(-t)-math.log1p(t)
 value=(g(0)+g(80)+sum((4 if j%2 else 2)*g(j*h) for j in range(1,n)))*h/3
 print('Simpson subintervals',n,'integral',repr(value),'difference from -pi²/6',value+math.pi**2/6)
for prec in [50,90]: series(prec)
for n in [20000,40000]:quadrature(n)
print('negative pi²/6 (double precision)',-math.pi**2/6)
