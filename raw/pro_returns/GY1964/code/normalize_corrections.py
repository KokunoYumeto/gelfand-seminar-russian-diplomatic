"""Normalize the three frozen correction ledgers without editing their semantics.

Run from any working directory:
    python work/code/normalize_corrections.py
    python work/code/normalize_corrections.py --check-only

The explicit cell targets below preserve the recorded assertions, including
incorrect signs and uncertain alternatives, while converting mathematical
shorthand into delimited LaTeX. The original hashes pin the reviewed inputs.
The exact before/after ledger makes a second run idempotent and auditable.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from pathlib import Path

WORK = Path(__file__).resolve().parents[1]
LOG = WORK / "evidence/correction_typesetting_changes.json"
GROUPS = ("autumn", "winter", "spring")
COUNTS = {"autumn": 65, "winter": 21, "spring": 33}
ORIGINAL_HASHES = {
    "autumn": "47f5ae6bd0eb0d09245264f28140ef5886acb3f279a229490a9f8c22b3ab3e2b",
    "winter": "068204931647087114404cc09dfd5b38b2ff602b5ea67732d14fd074e5d8d57a",
    "spring": "2008420518dadb45b914f5b41491d67ed0cd3cafb9f8341f41e5074dbc0808b7",
}
ALIASES = {
    "t": "transcription_reads", "c": "should_read",
    "e": "evidence", "p": "place",
}
TARGETS: dict[tuple[str, int, str], str] = {}


def target(group: str, row: int, field: str, value: str) -> None:
    key = (group, row, ALIASES[field])
    assert key not in TARGETS, key
    TARGETS[key] = value


def A(row: int, field: str, value: str) -> None:
    target("autumn", row, field, value)


def W(row: int, field: str, value: str) -> None:
    target("winter", row, field, value)


def S(row: int, field: str, value: str) -> None:
    target("spring", row, field, value)


# Autumn: retain mathematical errors in the transcription column.
A(2, "t", r"\(S_A(J)=\operatorname{Sym}_A(J)\) used without qualification")
A(2, "c", r"For general \(J\) use the Rees algebra \(\bigoplus J^n\); \(\operatorname{Sym}(J)\) works when \(J\) is of linear type.")
A(3, "t", r"\ru{Выбр.} ideals containing all positive-degree polynomials")
A(4, "t", r"Fractions of degree 1: \(J_U\)")
A(4, "e", r"The source distinguishes \(O_U\) and \(J_U\) but the surrounding localization wording is compressed; item 1964-2.4.")
A(5, "t", r"\(f=N^{-1}\log Z\) called convex")
A(5, "c", r"With the positive-log convention \(f\) is concave; minus the potential is convex.")
A(5, "e", r"Both transcripts and scan; perspective \(f(v)=v\,s(1/v)\), item 1964-3.2. Russian convexity vocabulary can be older/ambiguous, so this is a mathematical convention note.")
A(6, "t", r"\(\partial f/\partial v=0\)")
A(6, "c", r"\(\partial f/\partial v\) is constant on an affine coexistence segment; it need not vanish.")
A(6, "e", r"Visible zero retained in the transcription. Pressure \(p=T\partial_v f\); item 1964-3.3.")
A(7, "t", r"\(Z(V,N)\) approximately \(\exp(-Nf(v,T))\)")
A(7, "c", r"With the earlier definition \(f=\lim N^{-1}\log Z\), the exponent is \(+Nf\), up to \(o(N)\).")
A(8, "t", r"\(D\ell^{(\nu-1)/\nu}\)")
A(8, "c", r"\(D\ell^{\nu-1}\), since \(\ell\) is side length; alternatively \(DV^{(\nu-1)/\nu}\).")
A(8, "e", r"The fractional exponent is visible on P7; P10 writes the surface scale \(\ell^{\nu-1}\). Item 1964-3.8.")
A(9, "t", r"all remaining small contours followed by \(\sum_{i=1}^{M}\)")
A(9, "c", r"For the remaining contours use \(i>M\), as on P10.")
A(10, "t", r"\(e^{U/T}\)")
A(10, "c", r"Reconcile \(U\) with the earlier negative energy before choosing the sign; no silent replacement.")
A(10, "e", r"Earlier P3 uses negative occupied-bond energy with \(e^{-U/T}\); scan P8 changes convention or sign.")
A(11, "p", r"\(Q(T)\) series")
A(11, "t", r"\(S_\nu e(1-e^{-1/(2T)})\) and \(3\exp\{-1/(2T)\}^k\)")
A(12, "t", r"\(S_3=1/(C\sqrt{\pi})\)")
A(12, "c", r"The geometrically intended constant is \(1/(6\sqrt{\pi})\); C/c/6 remains a glyph ambiguity.")
A(13, "t", r"A closing brace precedes \(>\varepsilon\)")
A(13, "c", r"Place the comparison with \(\varepsilon\) inside the event braces in the modern statement.")
A(14, "t", r"\((G\cap S_\ell)/V_\ell\)")
A(14, "c", r"For a density in \(S_\ell\) divide its volume by \(|S_\ell|\); distinguish this from a global-volume fraction.")
A(14, "e", r"Scan visibly has \(V_\ell\); the claimed local-density deduction needs the subcube normalization.")
A(15, "t", r"Turn with probability \(1/3\), but returning is forbidden")
A(16, "t", r"\(2.6^n<\text{count}<2.8^n\); conjecture \(e^n\)")
A(16, "c", r"Under the square-lattice SAW reading the exponential base is below \(e\); under nonbacktracking the exact count is \(4\) times \(3^{n-1}\).")
A(17, "c", r"The mathematical CCR is \([\phi(f),\pi(g)]=i\hbar(\int fg)I\), after smearing and domain specification.")
A(18, "t", r"\(\lVert[\phi,\omega]\rVert=\lVert B\phi\rVert^2+\lVert\omega\rVert^2\)")
A(19, "c", r"Skew-adjoint in the energy inner product, consistent with \(A=-A^*\) on P11.")
A(19, "e", r"The block generator \(\bigl(\begin{smallmatrix}0&I\\-B^2&0\end{smallmatrix}\bigr)\) is skew-adjoint; scan says self-adjoint twice. Item 1964-4.3.")
A(20, "t", r"\(v'=Av+K_{u(\cdot)}\)")
A(20, "c", r"\(v'=Av+DK(u(\cdot))v\)")
A(20, "e", r"The factor \(v\) after the derivative of \(K\) is absent in the scan. Item 1964-4.5.")
A(22, "t", r"arbitrary subset \(A\subset X\) before \(f(\mu)(A)\)")
A(22, "c", r"The set tested for image-measure measurability must be \(A\subset Y\).")
A(22, "e", r"The source alternates \(A\) and \(B\) and visibly says \(X\); definition of pushforward, item 1964-6.2.")
A(23, "t", r"Take a non-Borel subset of \(Y\setminus X\); it is nonmeasurable")
A(23, "e", r"Visible parenthesis reads non-Borel. The complement \(Y\setminus X\) itself works under the preceding construction; item 1964-6.3.")
A(25, "t", r"for every \(B\) compact there exists a compact \(k\)")
A(25, "c", r"For every Borel \(B\) and \(\varepsilon>0\) require compact \(K\subset B\) with \(\mu(B\setminus K)<\varepsilon\).")
A(25, "e", r"Scan shows compact after \(B\); as written the condition is tautological by \(K=B\). Item 1964-6.4.")
A(26, "t", r"\(\mu(\widehat X\setminus X)=0\)")
A(26, "c", r"Use completed measurability or outer measure when \(X\) need not be Borel in the compactification.")
A(26, "e", r"No Borel hypothesis on \(X\) is stated; item 1964-6.4.")
A(28, "t", r"\(\operatorname{Hom}(E,F)\) is of the same kind for any topology between pointwise and compact convergence")
A(28, "c", r"Specify the locally convex/Suslin hypotheses and topology; do not assert arbitrary \(\operatorname{Hom}(E,F)\) is itself Frechet.")
A(30, "e", r"Counterexample \(X_t=Zt\) with unbounded \(Z\) excludes a coefficient-one common modulus; item 1964-6.8.")
A(31, "c", r"A safe formulation excludes simple factors locally isomorphic to \(\mathrm{SL}_2(\mathbb R)\); the shorthand is not a general matrix-size criterion.")
A(32, "t", r"If \(\Gamma\) is not discrete, Weil theorem holds although \(H^1\) is nonzero")
A(34, "t", r"\(\lVert h\rVert=\inf(\lVert h_1\rVert^2+\lVert h_2\rVert^2)\)")
A(34, "c", r"\(\lVert h\rVert^2=\inf(\lVert h_1\rVert^2+\lVert h_2\rVert^2)\)")
A(36, "t", r"\(\lambda H\ge H\) iff \(\lambda\ge1\)")
A(36, "c", r"Add \(H\) nonzero; the zero Hilbert subspace satisfies the order for every nonnegative scalar.")
A(37, "t", r"\(H^1\) corresponds to \(-\Delta+\lambda\)")
A(37, "c", r"Its positive reproducing kernel as a subspace of \(D'\) is \((-\Delta+\lambda)^{-1}\), for \(\lambda>0\).")
A(38, "t", r"\(\lim H(\text{join})/n=h(\xi)\)")
A(38, "c", r"Distinguish one-step \(H(\xi)\) from the entropy rate \(h(T,\xi)\).")
A(38, "e", r"Scan reuses \(h\); modern definition and inverse-image refinements in item 1964-10.1.")
A(39, "t", r"The bound is attained; \(n\) may be replaced by \(n-1\) for invertible maps")
A(39, "c", r"The 1965 published theorem is \(n\log_2\lambda\); the \(n-1\) bound is justified here by a later Lyapunov/Ruelle route.")
A(40, "t", r"minus \(\log Z\) per particle called free energy, then differentiated")
A(40, "c", r"Physical \(F_N=-T\log Z_N\); the displayed minus-log quantity is reduced free energy \(F_N/(NT)\).")
A(41, "t", r"\(S\) is convex in two variables")
A(41, "c", r"With positive logarithmic entropy and the usual stable short-range limit, \(S\) is concave in extensive densities.")
A(43, "t", r"Every invariant function is \(T\) of the quadratic form")
A(45, "t", r"No solution; irrational \(\alpha\) well approximated")
A(45, "c", r"\(PE=\delta\) always fails for a derivative on a compact torus because of the constant mode. The reduced equation additionally has small-divisor obstructions.")
A(45, "e", r"Scan shows \(\alpha\) with no independent power; Greenfield--Wallach1972 theorem/proposition; item 1964-12.7.")
A(46, "t", r"\(e^{2\pi i a/p}\)")
A(46, "c", r"Use multiplicative characters: \(\chi_j(u^r)=\exp(2\pi i j r/(p-1))\).")
A(46, "e", r"The visible expression uses the additive denominator \(p\); item 1964-13.2.")
A(47, "t", r"\(S_aT_bS_a^{-1}=T_{ab}\) and \(S_ae_k=e_{ak}\)")
A(47, "c", r"These conventions give \(S_ae_k\) proportional to \(e_{a^{-1}k}\); alternatively reverse the conjugation convention consistently.")
A(48, "t", r"\(T_gf(x)=f(gx)\)")
A(48, "c", r"For a left representation take \(T_gf(x)=f(g^{-1}x)\), or state a right/antirepresentation convention.")
A(49, "t", r"\(a\ne0\)")
A(49, "c", r"\(a\ne1\)")
A(49, "e", r"Scan distinctly has zero; first row must exclude the separate translation rows \(a=1\). Item 1964-13.3.")
A(50, "e", r"\(S_3\) standard character restricts to the mean of two \(A_3\) characters. Scan remains abbreviated; item 1964-13.6.")
A(51, "t", r"arbitrary real \(a_k\) in product \(\prod a_k^{n_k}\)")
A(51, "c", r"For extreme characters \(a_k=\sum\alpha_i^k+(-1)^{k-1}\sum\beta_i^k\), with nonnegative decreasing parameters and sum \(\le1\).")
A(52, "t", r"\(G_0\) isomorphic to \(G\) and \(G/G_0\) finite")
A(52, "c", r"\(G\) must have an abelian subgroup of finite index; it may be chosen normal.")
A(52, "e", r"The scan reads izom. \(G\), not abelian. This is a mathematical emendation, not an OCR correction. Item 1964-13.8.")
A(53, "c", r"Keep determinant/topology unspecified in the source; the \(\mathrm{SL}_2(\mathbb Q)\) solution is an explicitly conditional identification.")
A(53, "e", r"Later determinant-one matrix supports the interpretation, but not an unqualified \(\mathrm{GL}_2\) claim; item 1964-13.9.")
A(54, "t", r"conjugacy class determined by \(\alpha+\delta\)")
A(54, "c", r"Valid for regular semisimple \(\mathrm{SL}_2\) over an algebraically closed field; false universally.")
A(57, "c", r"Retain as the notebook attribution, not a verified exact citation for the complete \(\mathrm{SL}_2\) finite-field classification.")
A(60, "e", r"Equation has three coordinates \(x,y,z\). This removes the English intrinsic-dimension ambiguity.")
A(61, "t", r"\(\xi^2+m=0\bmod q\) is solvable")
A(61, "c", r"For the cited theorem require fixed \(q>3\) and Legendre symbol \(\bigl(\frac{-m}{q}\bigr)=1\), together with admissible \(m\) modulo 8.")
A(62, "c", r"Retain 48 as unresolved shorthand; do not identify it with a universal \(q\)-dependent transition degree.")

# Winter.
W(1, "t", r"\(\operatorname{coker}K\)")
W(1, "c", r"\(\operatorname{coker}T\)")
W(1, "e", r"The scan introduces no second operator \(K\); this is a notebook notation slip.")
W(3, "t", r"\((i/h)\psi_t=\Delta\psi-U\psi/h^2\); \(\int p\,dx\)")
W(3, "c", r"Consistent modern normalization \(ih\psi_t=-h^2\Delta\psi/2+U\psi\); action integral \(\int(p\,dx-H\,dt)\)")
W(4, "t", r"\(\lambda=-n^2\)")
W(4, "c", r"\(\lambda_n=n^2\) for the displayed \(-y''\) operator")
W(5, "t", r"first eigenfunction has Morse index 1; \(n\) zeros")
W(5, "c", r"With indexing from 1, index of \(L-\lambda_j\) is \(j-1\) and the first \(m\) span has at most \(m-1\) interior zeros")
W(6, "t", r"infinite index for all \(N\); fundamental group of a surface")
W(6, "c", r"Triangle quotient \(\Delta(2,3,N)\); finite for \(N=2,3,4,5\) and generally an orbifold group")
W(7, "t", r"upper-right \(H\) Hermitian independently of \(A\)")
W(7, "c", r"upper-right \(X(A^*)^{-1}\), \(X\) Hermitian, or use pairs \((A,X)\)")
W(8, "t", r"\(I\) primary, \(I\) contains \(J\) prime, \(J\) contains \(I^2\)")
W(8, "c", r"Use \(P\) prime and \(Q\) \(P\)-primary with \(P^2\) contained in \(Q\) contained in \(P\)")
W(8, "e", r"P000050 explicitly says \(I\) and \(J\) were interchanged; scans confirm the inconsistency.")
W(9, "t", r"all operators \(\sum P_i\partial_i\)")
W(9, "c", r"all derivations \(\sum P_i\partial_i\); general differential operators include higher derivatives")
W(10, "t", r"\(T(X)\), tangent bundle")
W(10, "c", r"\(T^*(X)\), cotangent bundle, unless a metric identification is chosen")
W(11, "t", r"\(m\) increases by factor 6, fields increase by 8")
W(11, "c", r"\(m\) increases by factor 16, fields increase by 8")
W(11, "e", r"Scan shows 6; the displayed \(m=2^{c+4d}(2a+1)\) and \(d+1\) imply 16.")
W(12, "t", r"\(K_R(S^i)=\pi_i(BO)\)")
W(12, "c", r"Reduced \(KO\) of \(S^i\) equals \(\pi_i(BO)\) for \(i>0\)")
W(13, "t", r"cyclic group of order \(f(k)\)")
W(13, "c", r"cyclic group of order \(2^{f(k)}\)")
W(13, "e", r"The scan states order \(f(k)\) but later says add the generator \(2^{f(k)}\) times; the latter matches Adams.")
W(14, "t", r"the image of \(A-\lambda\) is dense for all complex \(\lambda\)")
W(14, "c", r"density for \(A-i\) and \(A+i\) (equivalently the appropriate nonreal parameters)")
W(15, "t", r"\(\int \exp(it\lambda)/(iA-\lambda)\,d\lambda\)")
W(15, "c", r"spectral integral \(\int\exp(it\lambda)\,dE_A(\lambda)\), or a specified normalized resolvent-jump formula")
W(16, "t", r"densities for all \(f\in L^2\)")
W(16, "c", r"use \(L^2_0\) for a probability-preserving system and distinguish absolute continuity from equivalent Lebesgue maximal type")
W(18, "t", r"product of \(\mathbb Z/2\) with finitely many nonzero coordinates")
W(18, "c", r"direct sum of \(\mathbb Z/2\) for the stated finite-support group")
W(20, "c", r"projective special linear group \(\mathrm{PSL}(2,\mathbb F_5)\)")
W(20, "e", r"The scan omits the quotient; \(\mathrm{SL}(2,\mathbb F_5)\) has order120 whereas the rotational group has order60.")

# Spring: long formulas are placed in displays when useful.
S(1, "t", r"If \(A\) is simple, there are no Lie ideals either.")
S(1, "c", r"False literally: for \(A=M_2(\mathbb C)\), \(\mathbb C I\) and \(\mathfrak{sl}_2(\mathbb C)\) are proper nonzero Lie ideals. The intended quotient/involution theorem is not specified.")
S(2, "t", r"Uniform \(e^n=0\); the associative algebra is nilpotent, glossed as every element nilpotent.")
S(2, "e", r"Russian abbreviation and explanatory clause do not give the same condition. The scan supports the uniform-\(n\) correction but does not supply characteristic or a theorem statement. Item 1964-37.4.")
S(3, "t", r"\(P(x,d/dx)\) and \(P(x,d/dx,y,d/dy)\); are they isomorphic?")
S(3, "c", r"Interpret as \(A_1\) versus \(A_2\), not the fixed-rank Dixmier endomorphism conjecture.")
S(4, "t", r"Positive sum of pair logarithms called \(W\), together with \(\exp(-\beta W)\).")
S(4, "c", r"With \(\exp(-\beta W)\), set \[W=-\sum_{i<j}\log|\exp(i\theta_i)-\exp(i\theta_j)|.\]")
S(4, "e", r"The eigenangle density requires a positive power of the Vandermonde; the later integral uses \(\exp(+\beta\sum\log)\). Item 1964-39.3.")
S(5, "p", r"Claimed exact \(\beta=2\) gap expression")
S(5, "t", r"\(R_2(\alpha)=\exp(N^2\log\cos(\alpha/2))\).")
S(5, "c", r"Not an exact finite-CUE probability; \(N=1\) gives \(1-\alpha/\pi\). Treat only an appropriately qualified leading-energy approximation.")
S(5, "e", r"Scan and both transcriptions give equality. Elementary \(N=1\) check and the distinction from later determinant asymptotics. Items 1964-39.5 and 42.1.")
S(6, "t", r"\(R_\beta(\alpha)=\exp(+\beta(F(\alpha)-F(0)))\) while \(F\) is minimized.")
S(6, "c", r"For \(F=-\beta^{-1}\log\Psi\), use \(\exp(-\beta(F(\alpha)-F(0)))\); otherwise explicitly define the opposite sign convention for \(F\).")
S(6, "e", r"Scan confirms positive exponent. The normalization \(\Psi(\alpha)/\Psi(0)\) and usual minimized-free-energy convention fix the sign. Item 1964-39.4.")
S(7, "p", r"Middle \(W\) formula")
S(7, "t", r"\(W=\sum\log|\exp(i\theta_i-i\theta_j)|\).")
S(7, "c", r"The interaction depends on \(|\exp(i\theta_i)-\exp(i\theta_j)|\), with its energy sign separately specified.")
S(8, "p", r"Notation \(Z_p\) in finite-field counting discussion")
S(8, "t", r"\(Z_p\) and its algebraic closure.")
S(8, "c", r"Here \(Z_p\) means the finite field \(\mathbb F_p\), not the \(p\)-adic integers.")
S(9, "t", r"\(R_1(t)\sim At^{17/8}\exp(-t^2/4-t/2)\).")
S(9, "c", r"For the identified standard even sine kernel, the power is \(-1/8\); retain the manuscript \(17/8\) in the notes field.")
S(9, "e", r"Scan and Russian EvidenceBlock both confirm \(17/8\); Ehrhardt Introduction gives \(-(1/8)\log(s)\). The parameter normalization remains separately uncertain. Item 1964-42.3.")
S(10, "p", r"Relation between \(m,n\) and gap parameter")
S(10, "t", r"\(2m\ge n\) or \(2m=n\); \(t=\alpha n\).")
S(10, "c", r"Keep the relation ambiguous; the finite cosine matrix naturally scales with \(m\alpha\) and cannot automatically be identified with the standard \(s\).")
S(10, "e", r"The handwritten relation is thick and not securely an equality; \(t=\alpha n\) is underlined twice. No invented rescaling. Item 1964-42.3.")
S(11, "t", r"\(M_{n,k}\to G_{n,k}\) with fibre written \(S_k\).")
S(11, "c", r"The unit sphere in a \(k\)-dimensional real plane is \(S^{k-1}\); retain \(S_k\) only as historical notation.")
S(11, "e", r"The definition says a \(k\)-plane and one point of its unit sphere; the subscript is not a claim of dimension \(k\). Item 1964-45.2.")
S(12, "c", r"For the half-line use the Jost function on the specified \(\sqrt z\) sheet and a relative resolvent trace, not the ordinary trace of the individual resolvent.")
S(13, "t", r"Integral of \(|\lambda|^sW'/W\) equals sum of eigenvalue powers.")
S(14, "t", r"\((1/4)(y'(0)-y'(\pi))\).")
S(14, "c", r"Retain \(y'\) and mark it unidentified; do not silently replace it by \(q(0)+q(\pi)\).")
S(14, "e", r"Scan confirms \(y\) with prime in both terms. No definition of this \(y\) is supplied. Item 1964-47.6.")
S(15, "t", r"\(\delta(0)=0\).")
S(15, "c", r"\(\delta(0)\) is not a defined pointwise value; state an explicit spectral/resolvent regularization before taking a trace.")
S(16, "t", r"\(\operatorname{Tr}(AB-BA)=0\) without assumptions.")
S(16, "c", r"Both \(AB\) and \(BA\) trace class suffice; trace class of the commutator alone does not. \([S^*,S]\) has rank one and trace one.")
S(17, "t", r"Kernel involving \(P_1P'_2-P_2P'_1\) over a single displayed defining-function difference.")
S(19, "p", r"Subscript \(p\) in exactness discussion")
S(19, "t", r"\(F'_p\to F_p\to F''_p\) is not necessarily onto.")
S(19, "c", r"Do not interpret \(p\) automatically as a stalk. The line labels presheaves; stalks of an exact sequence of sheaves are exact.")
S(19, "e", r"Scan has “\ru{предпучки}” under the first object and distinguishes the inclusion functor below. The handwriting alone does not define \(p\). Item 1964-49.5.")
S(20, "t", r"\(0\to C\to\Omega^0\to\Omega\to0\).")
S(20, "e", r"Russian and English leave the final \(\Omega\) unspecified; scan confirms the truncated sequence. Item 1964-49.7.")
S(21, "t", r"\(T^*T-TT^*\ge0\) is necessary and sufficient.")
S(21, "c", r"Necessary only; subnormality requires the full positivity conditions. Weights \(1,1,2,2,\ldots\) give a hyponormal non-subnormal unilateral shift.")
S(22, "t", r"P84 \(a_{mn}=(Ae_n,e_m)\), but P85 defines \(a_{mn}^{(p)}=(p(A)e_m,e_n)\).")
S(22, "c", r"Use \(a_{mn}^{(p)}=(p(A)e_n,e_m)\) consistently with the lower-Hessenberg convention.")
S(23, "t", r"\(\lim\lVert p(P_nAP_n)\rVert=d>0\) after convergence applied to \(e\).")
S(23, "c", r"The inference supplies \[\lim\lVert p(P_nAP_n)e\rVert=\lVert p(A)e\rVert>0;\] it does not supply operator-norm convergence.")
S(23, "e", r"Scan visibly omits \(e\) in this one line while surrounding formulas contain it; the published Halmos proof uses the vector norm. Item 1964-50.10.")
S(24, "t", r"Conflicting half-\(d\) threshold directions; assertion of monotonic decrease is cancelled.")
S(24, "e", r"Both scans reviewed. The terminal norm is zero and initial norm exceeds \(3d/4\), but monotonicity is neither needed nor established. Halmos 1966 pp.435--437. Item 1964-50.10.")
S(25, "t", r"\(\lVert T\rVert<1\) or \(\lVert T\rVert\le1\); \(I-T^*T\) compact.")
S(25, "e", r"The scan does not securely distinguish the signs. Coercivity \(I-T^*T\ge(1-\lVert T\rVert^2)I\) diagnoses the strict reading. Item 1964-50.12.")
S(26, "t", r"Both \(T^n\to0\) and \((T^*)^n\to0\) have crossed arrows.")
S(26, "c", r"Retain failure of strong convergence to zero for both power sequences, with \(\lVert T\rVert\le1\) and \(\dim H>1\).")
S(27, "t", r"\(1/2,1/4\), then \(1/8\) or \(1/6\).")
S(27, "c", r"Retain the third-entry uncertainty; the geometric \(2^{-n}\) choice is a literature-supported reconstruction, not a certain decipherment.")
S(28, "c", r"Adjoin the obligatory lattice endpoints \(0\) and \(H\); the completed integer-chain question has an affirmative Domar construction.")
S(29, "t", r"\(Af(x)=\int_0^x f(y)\,d\mu(y)\) on the real line; lattice isomorphic to \(\operatorname{supp}(\mu)\).")
S(29, "c", r"False for \(\mu=(1/2)\mathbf1_{[-1,1]}\,dx\) with oriented integration: negative-side and positive-side support spaces are incomparable invariant subspaces.")
S(31, "t", r"\(\int_0 u(t)\exp(int)\,dt=0\), \(n=1,2,\ldots\), with no upper limit.")
S(31, "c", r"Use upper limit \(2\pi\) in the stated circle normalization. Keep the positive exponent: it correctly eliminates negative Fourier coefficients.")
S(31, "e", r"Scan shows lower zero only and the circle \(2\pi\) immediately above. Item 1964-50.24.")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def lint_cell(text: str) -> list[str]:
    """Check delimiters, braces, math-only tokens, and unmarked Cyrillic."""
    errors: list[str] = []
    mode: str | None = None
    braces = 0
    text_only: list[str] = []
    i = 0
    while i < len(text):
        token = text[i:i + 2]
        if token in (r"\(", r"\["):
            if mode:
                errors.append("nested math opener")
            mode = token
            text_only.extend("  ")
            i += 2
            continue
        if token in (r"\)", r"\]"):
            if mode != {r"\)": r"\(", r"\]": r"\["}[token]:
                errors.append("unmatched math closer")
            mode = None
            text_only.extend("  ")
            i += 2
            continue
        ch = text[i]
        if ch == "\\" and i + 1 < len(text) and text[i + 1] in "{}%&#$_\\":
            text_only.extend("  " if mode else token)
            i += 2
            continue
        if ch == "$":
            errors.append("unexpected dollar delimiter")
        if ch == "{":
            braces += 1
        elif ch == "}":
            braces -= 1
            if braces < 0:
                errors.append("unmatched closing brace")
                braces = 0
        if not mode and ch in "_^&%#":
            errors.append(f"unescaped text-mode {ch}")
        text_only.append(" " if mode else ch)
        i += 1
    if mode:
        errors.append("unclosed math")
    if braces:
        errors.append("unclosed brace")
    outside = "".join(text_only)
    math_commands = (
        r"\\(?:operatorname|mathbb|mathfrak|bigoplus|sum|prod|frac|tfrac|partial|"
        r"Delta|Gamma|Omega|alpha|beta|lambda|mu|nu|xi|theta|phi|psi|pi|hbar|ell|"
        r"varepsilon|le|ge|ne|subset|in|to|int|log|exp|lim|lVert|rVert|cap|"
        r"setminus|widetilde|widehat|quad|cdot)\b"
    )
    if re.search(math_commands, outside):
        errors.append("math-only command outside delimiters")
    without_russian = re.sub(r"\\ru\{[^{}]*\}", "", text)
    if re.search("[А-Яа-яЁё]", without_russian):
        errors.append("Cyrillic outside ru wrapper")
    if re.search(r"(?<!\\)æ|\\ae\b", text):
        # No such glyph occurs in these inputs. Enforce the agreed rendering
        # if a future correction uses the index symbol.
        if r"\text{\ae}" not in text:
            errors.append("ae requires text-in-math treatment")
    return errors


def read_group(group: str):
    path = WORK / "parts" / group / "corrections.csv"
    raw = path.read_bytes()
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8")))
    rows = list(reader)
    assert len(rows) == COUNTS[group], (group, len(rows))
    assert reader.fieldnames is not None
    return path, raw, reader.fieldnames, rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    previous = json.loads(LOG.read_text()) if LOG.exists() else None
    loaded = {g: read_group(g) for g in GROUPS}
    changes = []
    files = []
    outputs = {}
    for group, (path, raw, fields, rows) in loaded.items():
        expected = {ORIGINAL_HASHES[group]}
        if previous:
            expected.update(f["after_sha256"] for f in previous["files"] if f["group"] == group)
        if sha(raw) not in expected:
            raise SystemExit(f"{group}: input differs from the frozen original and logged normalized output")
        if not args.check_only:
            for (g, number, field), after in TARGETS.items():
                if g != group:
                    continue
                row = rows[number - 1]
                before = row[field]
                if before == after:
                    continue
                changes.append({
                    "group": group,
                    "file": str(path.relative_to(WORK)),
                    "row": number,
                    "page": row["page"],
                    "place": row["place"],
                    "field": field,
                    "before": before,
                    "after": after,
                })
                row[field] = after
        errors = []
        for number, row in enumerate(rows, 1):
            for field in ("place", "transcription_reads", "should_read", "evidence"):
                errors.extend(f"{group}:{number}:{field}: {e}" for e in lint_cell(row[field]))
        if errors:
            raise SystemExit("\n".join(errors))
        stream = io.StringIO(newline="")
        writer = csv.DictWriter(stream, fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
        new = stream.getvalue().encode("utf-8")
        outputs[group] = new
        files.append({
            "group": group, "file": str(path.relative_to(WORK)), "rows": len(rows),
            "before_sha256": sha(raw), "after_sha256": sha(new),
        })
    if args.check_only:
        print("CHECK PASS: 119 rows; balanced braces and math; no raw math-only commands or unmarked Cyrillic.")
        return
    if not changes and previous:
        print("IDEMPOTENT: all normalized targets already present; exact original change log retained.")
        print("CHECK PASS: all 119 rows.")
        return
    # All ledgers are validated before any is replaced.
    for group, (path, _, _, _) in loaded.items():
        path.write_bytes(outputs[group])
    payload = {
        "purpose": "Correction-ledger LaTeX normalization; source assertions and ambiguities retained",
        "script": "code/normalize_corrections.py",
        "files": files,
        "changed_cells": len(changes),
        "changes": changes,
        "verification": {
            "rows_checked": sum(COUNTS.values()),
            "delimiter_and_brace_errors": 0,
            "raw_math_command_errors": 0,
            "unmarked_cyrillic_errors": 0,
            "ae_occurrences": 0,
            "compile": "Main chapter compilation remains with the root agent.",
        },
    }
    LOG.parent.mkdir(parents=True, exist_ok=True)
    LOG.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    for group in GROUPS:
        entries = [x for x in changes if x["group"] == group]
        print(f"{group}: {COUNTS[group]} rows; {len({x['row'] for x in entries})} rows changed; {len(entries)} cells normalized.")
    print(f"TOTAL: {len(changes)} exact before/after cell changes logged.")
    print("CHECK PASS: all 119 rows; balanced math/braces; no raw math-only commands or unmarked Cyrillic.")
    print("Retained source signs, uncertain alternatives, missing factors, and disputed exponents.")
    print(f"Change log: {LOG}")


if __name__ == "__main__":
    main()
