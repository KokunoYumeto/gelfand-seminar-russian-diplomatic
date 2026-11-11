# Focused review of record 573 and problems from 571–573

Read-only review, 11 November 2026. Read all 17 staged items of record 573, GP-1982-03 and GP-1982-05–09, the corresponding 571 items, and both language versions of P001058–P001060. Visually inspected the original scans P001058 and P001059. P001060 starts Beilinson and is correctly excluded from record 573.

## Required correction: a single Virasoro notation and the covariance sign

The staged record initially fixed standard generators named \(L_n\) in 573.1, used them in 573.2/.5/.17, but then set \(\ell_n=-L_n\), \(h=-\Delta\) in 573.6. Those are two different meanings for \(L_n\).

The agreed repair reserves \(L_n\) for the notebook and uses \(\ell_n=-L_n\) consistently in modern statements:
\[
[\ell_n,\ell_m]=(n-m)\ell_{n+m}
+\frac c{12}(n^3-n)\delta_{n+m,0},\qquad h=-\Delta.
\]
The cubic term must be restored; negating all noncentral generators leaves the central coefficient unchanged in this conversion.

The recorded positive-sign primary law is additionally incompatible with the reverse Witt bracket. This is independent of the false uniqueness assertion. A quick Jacobi check uses
\[
D_0=z\partial_z+\delta,\qquad D_{-1}=\partial_z.
\]
If the recorded law is \([L_n,\varphi]=D_n\varphi\), then
\[
[L_0,[L_{-1},\varphi]]-[L_{-1},[L_0,\varphi]]
=[D_{-1},D_0]\varphi=\partial_z\varphi,
\]
whereas the reverse bracket demands \(-\partial_z\varphi\). The coherent law is positive for \(\ell_n\), and therefore negative for notebook \(L_n\). Field weight \(\delta\) and module weight \(h\) should remain distinct.

The last Laurent series also cannot silently use the same coefficient labels after this conversion. Modern extraction uses \(\ell_n=(2\pi i)^{-1}\oint z^{n+1}T(z)\,dz\) and \(T(z)=\sum\ell_nz^{-n-2}\); the notebook's \(z^{n-2}L_n\) requires coherent reindexing and signs.

These issues were sent to root and the autumn author. The autumn author confirmed that all modern fields will use \(\ell_n\), and that the covariance-sign correction receives its own ledger row.

## Neretin polynomial: correct under the conversion

No new false-as-written label is warranted for the polynomial. Setting the positive integer pair to \((1,2)\), multiplying the recorded polynomial by 16 gives
\[
16\Delta^2-2(c-5)\Delta+c.
\]
The standard level-two Gram factor is
\[
16h^2+(2c-10)h+c,
\]
which is exactly the same expression after \(h=-\Delta\). At \(c=0\), the nonzero root is \(\Delta=-5/8\), hence \(h=5/8\). Taking the least level among coincident reducibility conditions is the correct qualification.

## Classical Liouville and ghost checks: pass

For \(V=m_0^2e^\varphi\) and \(\Delta\varphi=V\), the improved tensor in 573.15 satisfies
\[
\partial_aT_{ab}=(\Delta\varphi-V)\varphi_b,\qquad
T_{aa}=2(\Delta\varphi-V).
\]
The improvement term is identically divergence free. These two calculations independently confirm the coefficient and sign.

Since \(\varphi_{z\bar z}=V/4\), the corrected holomorphic component satisfies
\[
\partial_{\bar z}(\varphi_z^2-2\varphi_{zz})=0,
\]
while the printed plus sign gives \(V\varphi_z\). The scan confirms both printed plus signs and the separate missing bar in the antiholomorphic conservation equation.

For the traceless symmetrized gradient \(P\), integration by parts gives \(P^*s=-2\,\operatorname{div}s\). Thus the notebook's corrected covector operator is \(\mathcal L=-P^*P/2\), as stated in 573.9. The positive/primed determinant qualification is appropriate.

## Liouville spectral theorem: pass with the stated restrictions

Opened the primary preprint https://arxiv.org/pdf/2005.11530, version 2 dated 11 November 2020. Read Sections 2.3–2.6, the explicit Theorem 6.25 statement, and the discussion identifying the descendant basis.

For \(0<\gamma<2\), \(\mu>0\), \(Q=2/\gamma+\gamma/2\), the cited construction has generalized states with \(P>0\), weights \((Q^2+P^2)/4\), and energies \((Q^2+P^2)/2+N+\bar N\). Theorem 6.25 gives the complete absolutely continuous resolution. The interacting descendant basis and Ward identities are explained in Section 2.6. These are generalized spectral states, not normalizable discrete primary eigenvectors.

Items 573.13–14 and GP-1982-09 preserve these restrictions and distinguish the constructed theory from the unrenormalized action at arbitrary target dimension. The cylinder sum is appropriately replaced by a spectral integral where required. No incorrect Casimir shift is inserted into the paper's stated Hamiltonian normalization.

## New problem statements: no substantive scope error found

- **GP-1982-05:** The existence question is correctly limited to the massless-Higgs/Prasad–Sommerfield model and does not infer a charge-one statement from a monopole–antimonopole picture. Opened the Taubes 1982 Part II publisher abstract and the 1989 erratum abstract. They support the stated existence chronology and the need for the correction. This review did not read their full proofs.
- **GP-1982-06:** Donaldson's original three-page announcement, Section 3, explicitly invokes Taubes Theorem 1.2 for arbitrary metric when harmonic 2-forms have the chosen duality. The \(H^2=0\) case meets that condition. Orientation and second-Chern-class signs in the item are coherent. Verification remains indirect through Donaldson.
- **GP-1982-07:** Opened Enss's full 1989 paper, Section 1, equations (1.12)–(1.13). It explicitly includes Coulomb forces, Dollard-modified channels, bound-pair channels and completeness of the continuous spectral subspace. For maximum standalone precision, add “in \(\mathbb R^3\), with positive finite particle masses” to the problem statement; this is already the setting of item 571.20.
- **GP-1982-08:** The question fixes covariance/null-state constraints and acknowledges the missing channel and three-point data. It does not turn underdetermination into a new open classification claim.
- **GP-1982-09:** The precise real-coupling realization matches the spectral source as described above.

Additional opened sources:

- https://link.springer.com/article/10.1007/BF01212170 — abstract and September 1982 publication metadata.
- https://link.springer.com/article/10.1007/BF01256496 — erratum abstract and 1989 metadata.
- https://scispace.com/pdf/self-dual-connections-and-the-topology-of-smooth-4-manifolds-27wazq56pq.pdf — original Donaldson announcement, Section 3.
- https://www.numdam.org/item/JEDP_1989____A0_0.pdf — full Enss paper, Section 1 and exact completeness statement.

**Conclusion:** correct the unified notation and primary covariance sign as agreed. The Neretin polynomial, Liouville improvement, ghost sign, restricted spectral theorem and new problem scopes otherwise pass the focused review.

## Patch verification

After writing the review, reread the autumn author's updated 573.1/.2/.3/.5/.6/.17. The modern statements now consistently use \(\ell_n=-L_n\), \(h=-\Delta\); 573.3 explicitly gives the covariance-sign repair; 573.17 states both the sign identification and coefficient reindexing. The distinct primary-covariance ledger row is present. These changes resolve the concrete consistency finding. Root must integrate this updated shard into the final staged JSON and rebuild it; the reviewer did not alter either.
