# Independent audit of the Goldsheid development

Audit date: 11 November 2026. The parent research agent verified that the original manuscript on P001018 states the norm of the difference of **orthogonal projectors**, with target `1/sqrt(2)`. The checks below use exactly that metric. They independently rederive the proposed arguments; they make no unsupported claim about the completeness of the literature search.

## 1. Symmetric-unitary coordinates for a real Lagrangian

Identify the ambient real Euclidean symplectic space with \(\mathbb C^n\), with symplectic form the imaginary part of the Hermitian inner product. If \(L\) is Lagrangian, an orthonormal real basis is the column set of a unitary matrix \(U\). Thus \(L=U\mathbb R^n\).

Let \(Cz=\overline z\) and put \(S=UU^T\). Then \(S\) is symmetric unitary. The antiunitary involution fixing \(L\) is

\[
C_L=UCU^*=S C,
\]

so

\[
P_Lz=\tfrac12(z+S\overline z).
\]

A coordinate product plane \(F=D_\theta\mathbb R^n\), with \(D_\theta=\operatorname{diag}(e^{i\theta_j})\), has

\[
P_F=\tfrac12(I+D_\theta^2 C).
\]

Since \(C\) is a real isometry, the exact norm relation is

\[
\|P_L-P_F\|_{\mathbb R}=\tfrac12\|S-D_\theta^2\|_{\mathbb C}.
\]

Every diagonal unitary is \(D_\theta^2\) for some \(\theta\), so no candidates are lost. Conversely, for any symmetric unitary \(S\), the map \(SC\) is an antiunitary involution because \(S\overline S=I\). Its fixed space is a real Lagrangian of dimension \(n\). The reduction is therefore an equivalence, not merely one implication.

## 2. Scalar-phase upper bound

The eigenvalues of \(S\) lie on the unit circle. Among at most \(n\) points there is an empty circular arc of length at least \(2\pi/n\), counting multiplicities without affecting the argument. The complementary closed arc has length at most \(2\pi-2\pi/n\). Let \(z\) be its midpoint. Every eigenvalue lies at angular distance at most \(\pi-\pi/n\) from \(z\), so its chordal distance from \(z\) is at most

\[
2\sin\left(\frac{\pi-\pi/n}{2}\right)=2\cos\frac{\pi}{2n}.
\]

Unitary normality gives \(\|S-zI\|=\max_j|\lambda_j-z|\), hence

\[
\inf_{F\text{ product}}\|P_L-P_F\|\le\cos\frac{\pi}{2n}.
\]

This handles \(n=1\) exactly and proves the target \(1/\sqrt2\) for \(n=2\). **It does not disprove a dimension-independent upper bound.** It only supplies an upper bound that tends to one.

For the symmetric-unitary swap matrix \(S=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), every column of \(S-D\), for diagonal unitary \(D\), has norm \(\sqrt2\). Thus \(\|S-D\|\ge\sqrt2\). Taking \(D=iI\) attains equality, since the eigenvalues of \(S\) are \(\pm1\). This verifies sharpness in dimension two.

## 3. Individual coordinate vectors do not control the selected plane

For a coordinate complex line \(E_j\), viewed as a real two-plane, the compression of \(P_L\) to \(E_j\) has trace one. Indeed, \(P_L+J P_LJ^{-1}=I\), and \(E_j\) is \(J\)-invariant, so the two compressed traces are equal and sum to two. Consequently its largest eigenvalue is at least \(1/2\). There is a unit vector \(f_j\in E_j\) with \(\operatorname{dist}(f_j,L)\le1/\sqrt2\).

These vectors are mutually orthogonal and span a product plane, but the individual estimates do not bound that plane’s projector gap. Explicitly, let

\[
v=(1,\ldots,1)/\sqrt n,\qquad L=\mathbb Rv\oplus i v^\perp,
\]

where \(v^\perp\) is the real orthogonal complement in \(\mathbb R^n\). This is Lagrangian. For \(f_j=i e_j\),

\[
\operatorname{dist}(f_j,L)=1/\sqrt n.
\]

Their span is \(F=i\mathbb R^n\), but \(iv\in F\cap L^\perp\), so \(\|P_L-P_F\|=1\). The example is valid for every \(n\), with the intended small individual distances as \(n\) grows.

## 4. Explicit six-dimensional failure of the sharp target

Let \(\omega=e^{2\pi i/3}\), and use indices \(i,j\in\{0,1,2\}\). Put

\[
V_{ij}=\omega^{ij}/\sqrt3,\qquad
S=\begin{pmatrix}0&V\\V^T&0\end{pmatrix}.
\]

The Fourier matrix \(V\) is unitary, and therefore \(S\) is symmetric unitary with zero diagonal. A completely explicit corresponding Lagrangian is

\[
L=\{(V\overline z,z):z\in\mathbb C^3\}\subset\mathbb C^3\oplus\mathbb C^3.
\]

For two such vectors the Hermitian inner product is \(2\operatorname{Re}(z^*w)\), so the symplectic form vanishes. The real dimension is six. An orthonormal real basis is

\[
\frac{(Ve_j,e_j)}{\sqrt2},\qquad
\frac{(-iVe_j,ie_j)}{\sqrt2},\qquad j=0,1,2.
\]

Suppose a diagonal unitary \(D=\operatorname{diag}(d_0,\ldots,d_5)\) satisfied \(\|S-D\|\le\sqrt2\). Since

\[
(S-D)^*(S-D)=2I-S^*D-D^*S,
\]

this would imply \(H=(S^*D+D^*S)/2\ge0\). Every diagonal entry of \(H\) is zero. A positive semidefinite Hermitian matrix satisfies \(|H_{ij}|^2\le H_{ii}H_{jj}\), so \(H=0\). Using symmetry of \(S\), the off-diagonal equation becomes

\[
\overline{S_{ij}}d_j+\overline{d_i}S_{ij}=0,
\qquad d_id_j=-S_{ij}/\overline{S_{ij}}
\quad(S_{ij}\ne0).
\]

The zeroth row and zeroth column of \(V\) are positive real. Hence all first-block phases \(d_i\) are equal, all second-block phases \(d_{3+j}\) are equal, and their product is \(-1\). The entry \(V_{11}=\omega/\sqrt3\) instead requires their product to be \(-\omega^2\), a contradiction.

Thus every diagonal unitary satisfies \(\|S-D\|>\sqrt2\). The torus of diagonal unitaries is compact and the norm is continuous, so its minimum is also strictly larger than \(\sqrt2\). The Lagrangian above therefore has

\[
\inf_{F\text{ product}}\|P_L-P_F\|>1/\sqrt2.
\]

This disproves the exact manuscript constant under the verified orthogonal-projector convention.

## 5. Quantitative obstruction for odd Fourier sizes

The stronger estimate was checked independently, including conjugations and factors of two. Let \(m\ge3\) be odd, \(V=F_m\) with \(V_{ij}=\exp(2\pi\mathrm{i}\,ij/m)/\sqrt m\), and use the same block construction in \(\mathbb C^{2m}\). Write a diagonal unitary as \(D=\operatorname{diag}(A,B)\), with \(A=\operatorname{diag}(a_i)\), \(B=\operatorname{diag}(b_j)\). Then

\[
H=\frac{S^*D+D^*S}{2}
=\frac12\begin{pmatrix}0&C\\C^*&0\end{pmatrix},
\qquad C=\overline V B+A^*V.
\]

The block Hermitian matrix has eigenvalues equal to plus and minus one half of the singular values of \(C\). Therefore

\[
\|S-D\|^2=2+\|C\|.
\]

Both summands defining \(C\) are unitary, and direct expansion gives

\[
\|C\|_F^2
=2m+2\operatorname{Re}\sum_{i,j}\overline{a_i}\,\overline{b_j}\,V_{ij}^2.
\]

The entrywise-square matrix \(K=(V_{ij}^2)\) is \(1/\sqrt m\) times a Fourier matrix with columns permuted by multiplication by two modulo \(m\). Oddness ensures that this multiplication is a permutation. Thus \(\|K\|=1/\sqrt m\). Since both phase vectors have Euclidean norm \(\sqrt m\),

\[
\left|\sum_{i,j}\overline{a_i}\,\overline{b_j}\,V_{ij}^2\right|
=|a^*K\overline b|\le\sqrt m.
\]

It follows that

\[
\|C\|_F^2\ge2m-2\sqrt m,\qquad
\|C\|\ge\frac{\|C\|_F}{\sqrt m}
\ge\sqrt{2-\frac{2}{\sqrt m}},
\]

and consequently

\[
\inf_{F\text{ product}}\|P_L-P_F\|
\ge\frac12\sqrt{2+\sqrt{2-2/\sqrt m}}.
\]

As odd \(m\to\infty\), this lower bound tends to

\[
\tfrac12\sqrt{2+\sqrt2}=\cos(\pi/8).
\]

Therefore every proposed universal constant strictly below \(\cos(\pi/8)\) is excluded by a sufficiently large member of the family. The estimate does **not** exclude the endpoint \(\cos(\pi/8)\), and it does not decide whether a universal constant in \([\cos(\pi/8),1)\) exists. Calling that interval unresolved in the global literature requires the parent’s separate literature review; it is only the region undecided by this argument.
