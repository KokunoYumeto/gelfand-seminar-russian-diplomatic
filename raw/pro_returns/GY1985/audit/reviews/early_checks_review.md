# Independent final review: checking appendix and records 664–666

Reviewed 11 November 2026: `work/late/checks.tex`, the corresponding parts of `work/code/check_mathematics.py`, all 16 mathematical items of record 664 and all 21 of record 666. Record 665 is a year heading, with no separate mathematical assertion to audit. This review concerns mathematical consistency and normalization; it is not a claim to have independently re-proved every cited analytic theorem. The separate record 663 review is in `late_review.md`.

## Required wording corrections identified

1. **1985-664.12, last sentence of the statement:** for the stated Euclidean Gaussian `Z=integral exp(-S)`, the logarithmic variation is **the negative expectation** of the action variation, plus the chosen measure and zero-mode contributions: `delta log Z = -<delta S> + ...`. The current phrase “is the expectation” omits that minus sign. The displayed variation of the action itself is correct.
2. **1985-664.4 and the hyperelliptic proposition in checks.tex:** explicitly include **compact** (or smooth projective), and connected, in the curve hypotheses. The proof and dimensions are correct for smooth compact connected complex curves; the unqualified phrase “smooth connected complex curve” could include noncompact curves with infinite-dimensional spaces of sections.

Both points were sent directly to the parent for integration. No root or late files were edited by this reviewer.

## Hyperelliptic basis and rank: confirmed

For a smooth compact hyperelliptic curve of genus `g>=2`, choose the quotient coordinate with infinity unbranched and write `y^2=f(x)`, `deg f=2g+2`, with simple roots. Near a branch point, `x-a=t^2`, `y=t` times a unit. Thus `dx^2/y^2` has order zero and `dx^2/y` has order one. At either infinity, `s=1/x` gives orders `2g-2-k` for `x^k dx^2/y^2` and `g-3-j` for `x^j dx^2/y`. These agree with every exponent in the appendix.

The products of the basis `x^i dx/y`, `0<=i<=g-1`, span exactly the `2g-1` first-family forms. The `g-2` second-family forms have the opposite hyperelliptic-involution parity, hence cannot belong to that image. Independence within either family is polynomial independence in the function field. Their total is `3g-3=h^0(K^2)` by Riemann–Roch. This proves both the rank and the cokernel, including the empty second family and zero cokernel when `g=2`.

For the surjective genus-two and nonhyperelliptic cases, the kernel count is independently `g(g+1)/2-(3g-3)=(g-2)(g-3)/2`. Matone–Volpato §3.1, immediately before Proposition 3.2, explicitly states exactly the required Max Noether scope. Its checked introductory convention is a smooth closed Riemann surface. No coefficient or small-genus defect was found.

## Finite determinant duality and Quillen reciprocal: confirmed

For the two-term complex `E1 --T--> E2`, the determinant-of-complex line is `det E1 tensor (det E2)^-1`. With orthonormal singular vectors and `T e_i = sigma_i f_i`, the cohomology unit maps to an ambient determinant vector multiplied by `product sigma_i^-1`. Thus the ambient norm pulled back to the cohomology line is the cohomology norm divided by that product, exactly as stated in the appendix and items 666.5–6.

The scalar check also detects continuity at a kernel jump: for `T=a`, the fixed ambient frame `e/f` has cohomological Hodge norm `|a|` when `a!=0`; multiplying by the reciprocal spectral factor `(|a|^2)^-1/2` makes its norm constant. The opposite factor would give `|a|^2` and fail to extend as a positive smooth metric at `a=0`. This is independent confirmation beyond the numerical diagonal examples.

Quillen's original §1 explicitly defines the dual line `(det ker D)^* tensor det coker D`. His §3 multiplies the squared Hodge norm on that line by `exp(-zeta'(0))`, confirming that dualizing to the notebook line reverses the factor. The original notebook PNG P001254 visibly defines `det ker / det coker` and visibly multiplies by the square root, so the recorded error is a faithful convention mismatch, not a conjectural transcription repair. Items 666.2, .5–7 and .13 consistently maintain the corrected convention.

## Beltrami wedge: confirmed

With the base period fixed and `mu=eta/y`, differentiation of `(tau+mu bar(tau))/(1+mu)` at `eta=0` gives `d tau=-2i d eta`. Therefore `d eta=(i/2)d tau` and `d bar(eta)=(-i/2)d bar(tau)`. Antisymmetry gives `d bar(eta) wedge d eta = -(1/4)d tau wedge d bar(tau)`.

Independently, `eta=p+iq` gives `(delta Re tau,delta Im tau)=(2q,-2p)`, whose real Jacobian is +4. The two complex wedge orders are opposite, again giving the minus sign. The smallness condition `|eta|<y` is sufficient: the new imaginary part is `y(1-|mu|^2)/|1+mu|^2>0`. Both the appendix and item 664.8 correctly restrict the differential identity to the tangent space at the base point. P001250 was inspected directly and has exactly the opposite wedge orders claimed by the correction.

## Todd coefficient, curvature and anomaly cancellation: confirmed

Writing `x=c1(K)`, the relevant Todd class is `Td(T)=x/(exp(x)-1)=1-x/2+x^2/12+...`. The degree-two term of `exp(jx) Td(T)` is `(j^2/2-j/2+1/12)x^2`, namely `(6j^2-6j+1)x^2/12`. Thus the coefficient, the symmetry under `j -> 1-j`, and `c1=1`, `c2=13` are all correct.

For `lambda_j=det R pi_* K^j`, the positive coefficient `c_j/12` in item 666.13 is consistent with Grothendieck–Riemann–Roch and with dualizing Bost's operator determinant convention. The stated `c1=-i/(2pi) partial bar(partial) log h` is the usual cohomological line convention. Metric independence for a sum of coefficients zero does not imply global trivialization; items 666.10 and .13–15 explicitly preserve that distinction. No missing sign was found in the conformal-ratio formulation or the thirteen/twenty-six explanation.

## Torus area and modular density: confirmed

Kokotov §5.0.1, equation (5.1), explicitly uses the metric `|dz|^2` on the lattice generated by `1,tau` and gives `C (Im tau)^2 |eta(tau)|^4`. This directly supports the flat area-y convention in item 664.10. For a constant metric rescaling `g'=c g`, the Laplacian becomes `Delta'=c^-1 Delta`; hence `det' Delta'=c^-zeta(0) det' Delta`. On a flat torus with the constant zero mode removed, `zeta(0)=-1`, so the determinant scales by `c`. Setting `c=1/y` gives precisely `C y |eta|^4` for unit area. The appendix states the same scaling via `Delta'=y Delta`.

The one-loop measure `d^2tau y^-14 |eta|^-48` has weights `-4+28-24=0`. Changing to `q=exp(2pi i tau)` gives `|dq/q|^2(-log|q|)^-14 |Delta(q)|^-2`, up to a constant. Thus items 664.10–11 and 666.1 agree. The cusp asymptotic in 666.17, `|eta|^-48=exp(4pi y)(1+O(exp(-2pi y)))`, proves divergence with the stated sign and exponent. Local anomaly cancellation cannot change that conclusion.

## Other consistency observations

The genus-two theta-constant density has compatible modular weights: the real measure has weight -6, `(det Im Omega)^-13` contributes +26, and `|chi10|^-2` contributes -20. The even-characteristic restriction and removal of the decomposable locus are correctly retained. The cautious genus-three statement does not pretend that a square root on Siegel space has already been globally specified.

Bost's proof of Theorem 3.3 explicitly uses, for genus at least three, complete curves through any two moduli points and the Satake compactification with boundary of codimension at least two. This supports the pluriharmonic-constancy argument in item 666.21 while preserving the positive-scalar ambiguity. Its distinction from Teichmüller space and from the genus-two case is appropriate.

Apart from the two wording corrections above, I found no inconsistency between the checked formulas and the reconstructed items in records 664–666.

## Sources reopened during this review

- Quillen (1985), Russian original, §§1 and 3: https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=rus&paperid=1334&what=fullt — refs `turn139view0`, `turn142view0`, `turn143view0`.
- Bost (1987), §§2.2–2.6 and proof of Theorem 3.3: https://www.numdam.org/article/SB_1986-1987__29__113_0.pdf — refs `turn137view0`, `turn139view1`, `turn139view2`, `turn142view1`, `turn143view1`; some displayed equations are poorly extracted, so the coefficient and sign conclusions also use the independent calculations above.
- Kokotov (2007), §5.0.1 equation (5.1), with the scaling discussion around (4.5): https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2007/127.pdf — refs `turn135view1`, `turn137view3`, `turn142view3`.
- Matone–Volpato, version 3, §3.1 before Proposition 3.2: https://arxiv.org/pdf/math/0605734 — refs `turn135view3`, `turn137view4`.
- Belavin–Knizhnik (1986), equations (2.21), (3.3)–(3.6), and §6: https://strings.itp.ac.ru/Papers/belavin1986.pdf — refs `turn137view1`, `turn139view4`, `turn143view2`.
