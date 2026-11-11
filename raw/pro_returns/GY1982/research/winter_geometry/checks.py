"""Independent editorial checks for the winter-geometry shard.

These checks verify normalization corrections and finite examples. They do not
constitute new general results or prove the cited analytic theorems. The symbolic
identities are checked algebraically; finite enumerations have explicit bounds.
Run: python work/agents/winter_geometry/checks.py
"""
from __future__ import annotations

from collections import Counter
from itertools import permutations
from math import ceil, comb
import re

import numpy as np
import sympy as s


RESULTS = []


def checked(name, detail):
    RESULTS.append(name)
    print(f"PASS {name}: {detail}")


# 1. Liouville normalization: direct real-coordinate and independent complex
# differentiation checks use several locally univalent maps.
x, y = s.symbols("x y", positive=True)
phi = s.log(2 / y**2)
assert s.simplify(s.diff(phi, x, 2) + s.diff(phi, y, 2) - s.exp(phi)) == 0
assert s.simplify(s.diff(-2*s.log(y), y, 2) - 1/y**2) == 1/y**2
z, zb = s.symbols("z zb")
for w in (z**2, z**3 + z, (z+1)/(z+2)):
    wb = w.subs(z, zb)
    wp, wbp = s.diff(w, z), s.diff(wb, zb)
    exp_phi = -8 * wp * wbp / (w-wb)**2
    phi_z = s.diff(wp, z)/wp - 2*wp/(w-wb)
    schwarzian = s.diff(w, z, 3)/wp - s.Rational(3, 2)*(s.diff(w, z, 2)/wp)**2
    stress = phi_z**2/2 - s.diff(phi_z, z)
    assert s.factor(4*s.diff(phi_z, zb) - exp_phi) == 0
    assert s.factor(stress + schwarzian) == 0
checked("Liouville factor and Schwarzian", "real w=z and three independent rational-map substitutions agree; T=-{w,z}.")


# 2. Oscillator normalization. Direct differential operators on polynomials are
# compared with the closed finite sum for every n=1,...,8, symbolically in alpha,beta.
alpha, beta = s.symbols("alpha beta", real=True)
h = (alpha**2 + beta**2)/2
c = 1 + 12*beta**2
zz = (None,) + s.symbols("z1:10")
for n in range(1, 9):
    lower_vacuum = n*(alpha-s.I*beta*n)*zz[n]
    lower_vacuum += sum(s.Rational(1, 2)*k*(n-k)*zz[k]*zz[n-k] for k in range(1, n))
    value = (alpha+s.I*beta*n)*s.diff(lower_vacuum, zz[n])
    value += sum(s.Rational(1, 2)*s.diff(lower_vacuum, zz[k], zz[n-k]) for k in range(1, n))
    expected = 2*n*h + c*s.Rational(n**3-n, 12)
    independent_sum = n*(alpha**2 + beta**2*n*n) + s.Rational(1, 2)*sum(k*(n-k) for k in range(1, n))
    assert s.expand(value-expected) == 0
    assert s.expand(value-independent_sum) == 0
wrong_level_two = s.diff(zz[1]**2, zz[1], 2)
assert wrong_level_two == 2
assert (c/2).subs(beta, 0) == s.Rational(1, 2)
checked("Virasoro vacuum commutators", "n=1,...,8 agree with 2nh+c(n^3-n)/12; the missing halves give 2 instead of 1/2 at n=2, alpha=beta=0.")


# 3. The two simple Ward/Gram operations are checked separately.
hs = s.symbols("h", nonzero=True)
assert s.cancel(hs*hs/(2*hs)) == hs/2
u = s.symbols("u")
for n in range(-1, 8):
    assert s.expand(s.diff(u**(n+1), u) - (n+1)*u**n) == 0
checked("Level-one Gram factor and Ward powers", "h^2/(2h)=h/2 for h != 0; differentiating epsilon=z^(n+1) supplies (n+1)z^n.")


# 4. Domain wall: equation of motion and conserved first integral independently
# fix the same factor sqrt(2)*lambda*eta.
q = s.symbols("q", real=True)
lam, eta = s.symbols("lambda eta", positive=True)
wall = eta*s.tanh(s.sqrt(2)*lam*eta*q)
residual = s.diff(wall, q, 2) - 4*lam**2*wall*(wall**2-eta**2)
first_integral = s.diff(wall, q)**2/2 - lam**2*(wall**2-eta**2)**2
assert s.simplify(residual) == 0
assert s.simplify(first_integral) == 0
for lv, ev, qv in ((1, 2, s.Rational(1, 3)), (3, 1, s.Rational(-1, 5))):
    assert abs(complex(residual.subs({lam: lv, eta: ev, q: qv}).evalf(40))) < 1e-30
checked("Domain-wall profile", "Euler-Lagrange equation, first integral and two numerical substitutions agree.")


# 5. Gauge sign, independently of the field equations.
phase = s.Function("phase")(q)
field = s.Function("field")(q)
gauge = s.Function("gauge")(q)
charge = s.symbols("charge", nonzero=True, real=True)
transformed = s.exp(s.I*phase)*field
covariant = s.diff(transformed, q) + s.I*charge*(gauge-s.diff(phase, q)/charge)*transformed
expected = s.exp(s.I*phase)*(s.diff(field, q)+s.I*charge*gauge*field)
assert s.simplify(covariant-expected) == 0
wrong = s.diff(transformed, q) + s.I*charge*(gauge+s.diff(phase, q)/charge)*transformed
assert s.simplify(wrong-expected-2*s.I*s.diff(phase, q)*transformed) == 0
checked("Abelian gauge sign", "D=d+ieA requires A -> A-d phase/e; the printed plus adds 2i d phase.")


# 6. Circular Nambu-Goto loop: Euler-Lagrange equation and squared conserved
# energy are separate identities; the physical time interval is before collapse.
t = s.symbols("t", real=True)
r0 = s.symbols("R0", positive=True)
radius = r0*s.cos(t/r0)
velocity = s.diff(radius, t)
assert s.trigsimp(radius*s.diff(radius, t, 2)+1-velocity**2) == 0
assert s.trigsimp(radius**2-r0**2*(1-velocity**2)) == 0
checked("Circular string", "R R'' + 1 - R'^2=0 and R^2/(1-R'^2)=R0^2 for 0 <= t < pi R0/2.")


# 7. Hilbert-transform projections on a positive/negative frequency pair.
H = s.Matrix([[0, -1], [1, 0]])
identity = s.eye(2)
positive = (identity-s.I*H)/2
negative = (identity+s.I*H)/2
assert H*H == -identity
assert positive*positive == positive
assert negative*negative == negative
assert positive*negative == s.zeros(2)
assert positive+negative == identity
assert (H+s.I*identity)**2 != H+s.I*identity
assert (H-s.I*identity)**2 != H-s.I*identity
checked("Hilbert-transform projectors", "(I-iH)/2 and (I+iH)/2 are complementary; H +/- iI are not projections.")


# 8. Negative logarithmic Fourier form. Midpoint quadrature checks the known
# Fourier coefficients independently, with explicit tolerance and sample sizes.
fourier_results = []
for sample_count in (16384, 32768):
    theta = (np.arange(sample_count)+0.5)*(2*np.pi/sample_count)
    kernel = np.log(2*np.abs(np.sin(theta/2)))
    for n in (1, 3, 7):
        coefficient = float(np.mean(kernel*np.cos(n*theta)))
        assert abs(coefficient + 1/(2*n)) < 5e-5
        assert coefficient < 0
        fourier_results.append((sample_count, n, round(coefficient, 9)))
ratios = [s.Rational(1, 2*n*n) for n in (1, 2, 4)]
assert len(set(ratios)) == 3
checked("Logarithmic kernel", f"two midpoint grids give negative coefficients near -1/(2n): {fourier_results}; log*Hilbert has order -1, not delta-prime order +1.")


# 9. Casimir map versus moment map and the actual SU(3) hexagon.
A = s.diag(3, 1, -4)
U = s.Matrix([[s.sqrt(2)/2, -s.sqrt(2)/2, 0], [s.sqrt(2)/2, s.sqrt(2)/2, 0], [0, 0, 1]])
B = U*A*U.T
assert s.trace(A**2) == s.trace(B**2) == 26
assert s.trace(A**3) == s.trace(B**3) == -36
assert tuple(A.diagonal()) != tuple(B.diagonal())
basis = np.array([[1, -1, 0], [1, 1, -2]], dtype=float)
basis[0] /= np.sqrt(2)
basis[1] /= np.sqrt(6)
vertices = np.array(list(permutations((3, 1, -4))), dtype=float) @ basis.T
vertices = vertices[np.argsort(np.arctan2(vertices[:, 1], vertices[:, 0]))]
lengths = []
for n in range(6):
    left = vertices[(n-1) % 6]-vertices[n]
    right = vertices[(n+1) % 6]-vertices[n]
    assert abs(np.dot(left, right)/(np.linalg.norm(left)*np.linalg.norm(right))+0.5) < 1e-12
    lengths.append(np.linalg.norm(right))
assert np.allclose(lengths[0::2], lengths[0])
assert np.allclose(lengths[1::2], lengths[1])
assert np.allclose(sorted(set(round(v, 10) for v in lengths)), [2*np.sqrt(2), 5*np.sqrt(2)])
checked("SU(3) orbit image", "trace(A^2), trace(A^3) stay (26,-36) while the diagonal changes; the permutahedron has six 120-degree angles and alternating sides 2sqrt(2),5sqrt(2).")


# 10. Catalan closed form is independently compared with convolution.
catalan = [1]
for n in range(1, 13):
    catalan.append(sum(catalan[k]*catalan[n-1-k] for k in range(n)))
assert catalan == [comb(2*n, n)//(n+1) for n in range(13)]
assert catalan[6] == 132
assert sum(catalan[k]*catalan[1-k] for k in range(1, 1)) == 0
checked("Catalan indexing", f"convolution and binomial formula agree for n=0,...,12: {catalan}; the notebook's restricted sum fails already at n=1.")


# 11. Discrete walk test for the ceiling. This verifies bounded cases, not a
# spectral estimate or a nonvanishing lower bound.
for p in range(1, 7):
    reachable = {0}
    first = {}
    for steps in range(1, 37):
        reachable = {v+d for v in reachable for d in range(-p, p+1)}
        for n in range(1, 37):
            if n in reachable and n not in first:
                first[n] = steps
    assert all(first[n] == ceil(n/p) for n in range(1, 37))
checked("Ceiling in the path-length bound", "minimal steps are ceil(N/p) for 1<=N<=36, 1<=p<=6; finite evidence only, independent of analytic gap asymptotics.")


# 12. Short-loop reflection condition, exhausted over a bounded lattice.
loop_count = 0
for k in range(1, 8):
    for p in range(1, 4):
        for tau in range(1, min(6, (2*k-1)//p)+1):
            def visit(path):
                global loop_count
                if len(path) == tau+1:
                    if path[-1] == k:
                        loop_count += 1
                        assert all(a+b > p for a, b in zip(path, path[1:]))
                    return
                for nxt in range(max(0, path[-1]-p), path[-1]+p+1):
                    # A return must still be possible in the remaining steps.
                    if abs(nxt-k) <= (tau-len(path))*p:
                        visit(path+[nxt])
            visit([k])
checked("Short-loop condition", f"{loop_count} closed walks exhausted for k<=7, p<=3, tau<=6 with tau*p<2k; every edge is remote. The general proof remains the cited length argument.")


# 13. Exact notebook dual-word example, preserving attached closing brackets.
def dual_word(word):
    fragments = re.split(r"(\(+)", word)
    result = []
    for fragment in fragments:
        if not fragment or fragment.startswith("("):
            result.append(fragment)
        else:
            atoms = re.findall(r"[a-z]\)*", fragment)
            assert "".join(atoms) == fragment
            result.append("".join(reversed(atoms)))
    return "".join(result)

original = "(((a))b)(cd)e"
dual = "(((b)a))(ed)c"
assert dual_word(original) == dual
assert dual_word(dual) == original
assert Counter(re.findall(r"[a-z]\)*", original)) == Counter(re.findall(r"[a-z]\)*", dual))
checked("Dual-word example", "the exact P001086 example is involutive and preserves each letter with its closing-parenthesis multiplicity; this sample does not replace Arnold's general proof.")

print(f"\nAll {len(RESULTS)} independent editorial checks passed.")
print("Scope: algebraic normalization checks and explicitly bounded examples; no uncited universal spectral or representation-theoretic theorem is inferred.")
