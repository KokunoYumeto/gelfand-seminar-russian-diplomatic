# Independent review of record663

Reviewed `work/late/items.json`, items1985-663.1–15, independently of the root checking code. Reopened the original author-hosted texts of Dubrovin–Krichever–Novikov1976 and Veselov–Novikov1984 (potential operators). All four principal mathematical corrections in the record—ordinary Lax versus a Manakov triple, Baker–Akhiezer derivative placement, the reality sign, and the Novikov–Veselov commutator—are correct under the conventions actually written in the reconstructed statements. No change to the main signs is required.

## 1. Novikov–Veselov commutator: independent expansion

Put `D = partial_z`, `E = partial_bar_z`, with commuting derivatives; write multiplication coefficients on the left. Let

`L = D E + V`,
`P = D^3 + E^3 + u D + v E`,
`B = D(u) + E(v)` (multiplication).

The full expansion is

```
[P,L] + B L
 = (3 D(V) - E(u)) D^2
 + (3 E(V) - D(v)) E^2
 + (3 D^2(V) - D E(u)) D
 + (3 E^2(V) - D E(v)) E
 + D^3(V) + E^3(V) + u D(V) + v E(V)
   + (D(u)+E(v)) V.
```

The `DE` coefficient cancels exactly; the order-three mixed terms cancel in the individual commutators. Thus `E(u)=3 D(V)` and `D(v)=3 E(V)` kill every positive-order term. With real `V` and `v=bar(u)`, the second equation is the conjugate of the first, and the scalar term is

`D^3(V) + E^3(V) + D(u V) + E(v V)`.

This confirms663.13 exactly. The notebook's swapped auxiliary derivatives and swapped B derivatives are not consistent with `L=DE+V` and this `P`. The text is also right to distinguish `D composed with M_u`, acting on V as `D(uV)`, from the scalar `D(u)` multiplying V.

Suggested independent polynomial substitution for the root code: in formal independent coordinates z,w, choose any polynomial V, integrate `u_w=3 V_z` and `v_z=3 V_w`, then evaluate the entire operator on several unrelated polynomials. This checks the raw expansion without relying only on substituting its coefficient formulas. For a real specialization, use real x,y and Wirtinger derivatives; reality of V and v=conjugate(u) then need to be checked independently.

## 2. Baker–Akhiezer reconstruction and gauge

At puncture1 write

`psi = exp(i k z) (1 + xi1/k + O(k^-2))`.

Start with a general monic second-order operator `L=DE+aE+cD+b`. Its order-k term at this puncture is `i k c`, so the normalization forces `c=0`. Its order-one term becomes `i E(xi1)+b`, hence `b=-i E(xi1)`.

At puncture2 write

`psi = c2 exp(i k w)(1+xi2/k+...)`, with `w=bar(z)`.

The order-k coefficient of `(DE+aE+b)psi` is `i k (D(c2)+a c2)`, forcing `a=-D(log c2)`. Thus663.5 has the correct barred first-order operator and negative derivative coefficient for the stated positive `DE` leading term and oscillatory exponentials. The sign would change if the leading operator were `-DE`; the factor i would disappear with nonoscillatory `exp(kz)` conventions. Mixing those conventions is precisely what must be avoided.

Multiplying psi by a nonzero function c gives `L' = M_c L M_c^-1`. This can reintroduce both first-order derivatives; it does not preserve the `c1=1` gauge automatically. The item says only conjugation, so it is correct. One optional sentence could clarify that the displayed normal form presumes the gauge has subsequently been restored.

The author-hosted retyped English1984 file itself contains apparent normalization/typesetting defects in equation(3), including a positive coefficient and an implausible logarithm of xi1. The record appropriately rederives the formula rather than importing those defects. The1976 text uses a different sign/exponential convention. Do not change663.5 merely to agree with an isolated formula in either rendering.

## 3. The antiholomorphic reality sign

The minus sign in663.10 is right for `exp(i k1 z)` and `exp(i k2 bar(z))` when tau exchanges the punctures and preserves D itself. Near puncture1, the condition

`w2(tau(P)) = -conjugate(w1(P))`

implies `k2(tau(P))=-conjugate(k1(P))`. Therefore `conjugate(psi(tau(P)))` has the same exponential `exp(i k1 z)` as psi, not its inverse. With the plus sign it would have `exp(-i k1 z)`.

To see the coefficient consequence, after the holomorphic-involution reduction makes c2 constant, uniqueness gives

`conjugate(psi(tau(P))) = conjugate(c2) psi(P)`.

At the other puncture this implies `|c2|=1`; at the first puncture it gives `xi1=-conjugate(xi2)`. The positive-DE potential can equally be read at the second puncture as `b=-i D(xi2)`. Hence

`conjugate(b) = i E(conjugate(xi2)) = -i E(xi1) = b`.

This checks the reality claim without relying solely on a printed sign. Theorem2 in the reopened Veselov–Novikov1984 original explicitly has the minus sign, tauD=D, commuting sigma and tau, and exchanged punctures. Its later Theorem4 adds real-locus conditions for smoothness. The record correctly treats the theorem as sufficient and refuses an unrestricted necessity claim.

A plus sign can occur under other exponential conventions or after composing involutions, but then the divisor-invariance condition can change: replacing tau by sigma*tau need not preserve D. Thus a free ± in the same fixed convention is not innocuous.

## 4. Holomorphic involution and Prym statement

The residue proof behind663.9 is sound. Let omega have divisor `D+sigma(D)-P1-P2`, normalize its residues to +1 and -1, and consider `psi(P)psi(sigma(P))omega`. Its only poles are at the punctures because the zeros of omega cancel the Baker-function poles. The exponentials cancel because the local parameters are odd. The residues are 1 and `-c2^2`, so `c2^2=1`, hence c2 is constant on each connected regular parameter domain. The first-order coefficient vanishes.

Exactly two fixed points in the smooth k=0 setting is also consistent with the checked1984 theorem. By Riemann–Hurwitz, if the quotient genus is h, then genus(Gamma)=2h; the Prym dimension is h=genus(Gamma)/2. This verifies663.11. The source says that extra fixed points prevent the stated divisor equation; the reconstructed restriction is justified.

## 5. Ordinary Lax counterexample and scope

For `L=-Dx^2-Dy^2+u(x,t)` and `A=-4Dx^3+6u Dx+3u_x`, direct commutation gives

`[A,L] = 6u u_x - u_xxx` (multiplication).

The `Dx^2` coefficients are `-12u_x+12u_x=0`; the `Dx` coefficients are `-12u_xx+6u_xx+6u_xx=0`; the scalar terms are `-4u_xxx+3u_xxx+6u u_x`. Thus663.1 is correct.

For a particularly transparent nonrigidity check, take a smooth periodic KdV solution with initial data u(x,0)=sin(x). At time zero, `u_t=cos(x)+3sin(2x)`, whereas infinitesimal translation is a constant multiple of `u_x=cos(x)`. A rotation would introduce a y-dependent term proportional to `y cos(x)`, so it cannot account for this evolution either. This uses the standard existence of smooth periodic KdV evolution; the differential identity is independently exact. If an entirely explicit unbounded example is useful, `u(x,t)=x/(1-6t)` solves the same equation on t<1/6 and changes the magnitude of its gradient, which rigid Euclidean motions cannot do. State that this latter example is unbounded if used.

One can also add any fixed smooth periodic `v(y)` to L without changing the commutator, since A commutes with `-Dy^2+v(y)`. That yields a separable two-variable example, although it still does not challenge a theorem explicitly restricted to nonseparable genuinely two-dimensional potentials. The record's limitation to refuting the unrestricted notebook wording is therefore correct.

## 6. Kernel preservation is not full-spectrum isospectrality

For a constant energy E0 define `Q=L-E0`. If

`Q_t=[A,Q]+B Q`, `psi_t=A psi`,

then `(Q psi)_t=(A+B)Q psi`. This proves formal compatibility at that one energy. To transport actual kernels through time one needs the relevant well-posed linear evolution; the record appropriately says formal compatibility. There is no implication that every spectral value of L is preserved. Likewise an ordinary differential-operator Lax identity implies functional-analytic isospectrality only when its conjugating evolution exists with appropriate domains;663.1 does not claim more.

## Result of review

No algebraic sign correction is needed in663.1,663.3,663.5,663.9–11,663.13. The present wording correctly separates all-energy ordinary Lax evolution from fixed-energy Manakov triples, and reality from global smoothness. The optional concrete nonrigidity example and the explicit full commutator expansion above can strengthen the checking appendix. Other663 items retain appropriate source/scope qualifications; no further theorem was inferred from their vague inverse-scattering announcements.

### Sources reopened for this independent review

- https://homepage.mi-ras.ru/~snovikov/91.pdf — tool refs turn124view0 and turn125view0; Theorems1,2,4, residue proof and convention comparison.
- https://people.sissa.it/~dubrovin/Papers/1976/dubrovin_krichever_novikov_1976.pdf — tool ref turn124view1; Section3 Lemmas1–3 and contrasting exponent/operator conventions.


## Addendum: root's global two-soliton counterexample and checking appendix

I independently reviewed the record663 propositions in `work/late/checks.tex` and the corresponding checking implementation after their completion. The Novikov–Veselov and Baker–Akhiezer proofs agree with the independent derivations above. No mathematical issue was found.

For the new explicit tau function `T=1+r+s+rs/9`, with `r=exp(2x-8t)` and `s=exp(4x-64t)`, positivity makes `U=-2 partial_x^2 log(T)` globally smooth and real for every real x and t. The six unordered pairs of exponential modes have bilinear polynomial values `0,0,864,-96,0,0` in lexicographic pair order. The only nonzero contributions share the exponential rs and cancel as `864/9-96=0`; the ordered-pair sum has a common factor two. Thus `(D_x^4+D_x D_t)T.T=0` exactly. Dividing by `2T^2` gives `q_xt+q_xxxx+6q_xx^2=0`, q=log T, and differentiating gives `U_t=6UU_x-U_xxx` with precisely the signs in the Lax operator.

To check nonrigidity by a route distinct from the root's rational derivative implementation, I evaluated logarithmic-derivative cumulants using the four exponent weights. If `M_j=sum(a_i k_i^j)` and `N_j=sum(a_i omega_i k_i^j)` at a point, then

```
q_xxx = M3/M0 - 3 M2 M1/M0^2 + 2 M1^3/M0^3,
q_xxt = N2/M0 - (2 N1 M1 + N0 M2)/M0^2 + 2 N0 M1^2/M0^3.
```

Exact rational arithmetic gives at t=0:

| (r,s) | U_x | U_t | U_t/U_x |
|---|---:|---:|---:|
| (1,1) | -648/343 | 19872/343 | -92/3 |
| (2,4) | 1399968/357911 | -25782912/357911 | -89524/4861 |

The second point is x=(log 2)/2, so both samples lie on the same t=0 solution. Both spatial derivatives are nonzero and the ratios differ. A time-dependent translation would have a ratio constant in x. A continuous Euclidean motion preserving a nonconstant, y-independent potential cannot change its direction of variation; consequently its connected motion reduces to x-translation (with irrelevant translation in y), which this calculation excludes. The proof correctly limits itself to refuting the unrestricted notebook wording and does not assert a genuinely two-dimensional decaying scattering counterexample.
