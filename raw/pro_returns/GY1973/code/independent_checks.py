"""Independent exact checks for GY1973, by the integrating reviewer.

Standard library only. The Vasserstein identity is checked on an
unisolvent grid, independently of the other reviewer's coefficient
arithmetic. Since its degree in each variable is at most five, 6 x 6
zero values prove the polynomial identity. Bernoulli finite sums are
checked directly; the all-moment p-adic limit is proved in the text.
"""
from fractions import Fraction as F
from math import comb
import json


class QI:
    """Gaussian rational, with exact arithmetic."""
    def __init__(self, real=0, imag=0):
        if isinstance(real, QI):
            self.r, self.i = real.r, real.i
        else:
            self.r, self.i = F(real), F(imag)

    def __add__(self, other):
        b = QI(other)
        return QI(self.r + b.r, self.i + b.i)

    __radd__ = __add__

    def __neg__(self):
        return QI(-self.r, -self.i)

    def __sub__(self, other):
        return self + (-QI(other))

    def __rsub__(self, other):
        return QI(other) + (-self)

    def __mul__(self, other):
        b = QI(other)
        return QI(self.r*b.r - self.i*b.i, self.r*b.i + self.i*b.r)

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = QI(other)
        d = b.r*b.r + b.i*b.i
        return self * QI(b.r/d, -b.i/d)

    def __rtruediv__(self, other):
        return QI(other) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        a = QI(1)
        for _ in range(n):
            a = a * self
        return a

    def __eq__(self, other):
        b = QI(other)
        return self.r == b.r and self.i == b.i

    def __repr__(self):
        return f"({self.r})+({self.i})i"


I = QI(0, 1)


def check_row(x, y):
    x, y = QI(x), QI(y)
    c = x*x+y*y-1
    f1 = QI(F(1, 2))
    f2 = (I*(x+2)-y)/2
    a, b = x+c*f1, y+c*f2
    t, s = x+1+I*y, x+1-I*y
    A, B = s*(a+1)-a-2, I*s*s/2
    assert s*t == 2*(a+1)
    assert b == t*t/(2*I)+I*t*a
    assert A*a+B*b == 1
    return True


grid_points = 0
for x in range(6):
    for y in range(6):
        check_row(x, y)
        grid_points += 1
for x, y in [
    (QI(0, 1), QI(1, -1)),
    (QI(F(1, 3), F(2, 5)), QI(F(-7, 4), F(5, 9))),
    (QI(-1), QI(0)),
    (QI(1), QI(0)),
]:
    check_row(x, y)
print("POLYNOMIAL ROW")
print(f"Three identities pass on {grid_points} exact grid points and 4 extra Gaussian-rational points.")
print("Degree in each variable of A*a+B*b-1 is at most 5; the grid is an exact identity certificate.")
print("This establishes the complex-coefficient claim, not real-coefficient reducibility.")


def bernoulli_numbers(n):
    b = [F(1)]
    for m in range(1, n+1):
        b.append(-sum(F(comb(m+1, j))*b[j] for j in range(m))/F(m+1))
    return b


B = bernoulli_numbers(12)


def bp(n, x):
    x = F(x)
    return sum(F(comb(n, j))*B[j]*x**(n-j) for j in range(n+1))


def vp_int(a, p):
    if not a:
        return None
    a = abs(a)
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v


def vp(x, p):
    x = F(x)
    if not x:
        return "infinity"
    return vp_int(x.numerator, p)-vp_int(x.denominator, p)


results = []
checks = 0
for p in (3, 5, 7):
    for k in range(10):
        limit = (4-F(2)**(1-k))*B[k+1]/F(k+1)
        assert limit == 2*(B[k+1]-bp(k+1, F(1, 2)))/F(k+1)
        valuations = []
        for m in range(1, 5):
            n = p**m
            direct = sum((-1 if 2*a<n else 1)*a**k for a in range(n))
            via_B = (bp(k+1, n)-2*bp(k+1, F(n+1, 2))+B[k+1])/F(k+1)
            assert direct == via_B
            valuations.append(vp(F(direct)-limit, p))
            checks += 1
        results.append({"p":p, "k":k, "limit":str(limit), "vp_error_m1_to_m4":valuations})
print("\nBERNOULLI MOMENTS")
print(f"{checks} direct finite sums agree exactly with the Bernoulli-polynomial formula.")
print("Convention B_1=-1/2; moments k=0: -1; k=1: 1/4; k=3: -1/32.")
print("N=p^m tends to 0 p-adically; the fixed rational polynomial formula proves the limit.")
print(json.dumps(results, indent=2))

# An independently chosen set of parameters checks the alternative entire
# implementation. These floating-point residuals are not its all-point proof.
import cmath
from math import pi

def entire_certificate(x, y):
    h=cmath.exp(1j*pi*(y-1)/2)
    if y==1:
        f=1j*pi/4-0.5
    elif y==-1:
        f=1j*pi/4+0.5
    else:
        f=(h-y)/(y*y-1)
    c=x*x+y*y-1
    b=y+c*f
    row=abs(b-(h+x*x*f))
    bezout=abs((-x*f/h)*x+b/h-1)
    return row,bezout

complex_points=[
    (2+3j,1),(-2+1j,-1),(1/3+2j,0),
    (-1.5-0.25j,2+0.5j),(0.75+0.5j,-0.2+3j),
    (1-0.75j,0.75-2j),(-2.25+1.25j,-3-0.5j)]
residuals=[entire_certificate(x,y) for x,y in complex_points]
assert max(max(r) for r in residuals)<1e-10
print("\nALTERNATIVE ENTIRE CERTIFICATE")
print("Seven independently selected complex pairs, including y=+1 and y=-1.")
print("Maximum row residual:",max(r[0] for r in residuals))
print("Maximum Bezout residual:",max(r[1] for r in residuals))
print("These are implementation checks only; removability and the growth bound are proved in the appendix.")
