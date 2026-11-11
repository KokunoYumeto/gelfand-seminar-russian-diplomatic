"""Deterministic, idempotent LaTeX repair of the 45 middle correction rows.

The supplied chapter builder inserts these four cells directly into LaTeX.
Run this after finalize.py if regenerating the original correction checkpoint.
Only corrections.csv is changed; row metadata, ordering and count are preserved.
"""
from pathlib import Path
import csv
import re

P = Path(__file__).resolve().parent
F = P / 'corrections.csv'
FIELDS = ['page', 'place', 'transcription_reads', 'should_read', 'evidence', 'applies_to', 'type']
with F.open(newline='') as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 45, 'Unexpected correction count: review before repairing.'

# Each tuple supplies place, transcription, critical reading and evidence.
# Raw Python strings below contain ONE backslash for each LaTeX command.
cells = {
1: (
    r'Record 428 boundary',
    r'The catalogue routing window includes P000718',
    r'S. I. Gelfand begins on P000719; P000718 belongs to the preceding Dickey--Novikov material',
    r'Heading and continuity of the formulas; independently checked with the early-record editor.'),
2: (
    r'Uploaded scan integrity',
    r'The supplied PNG ends after 10,722 bytes',
    r'Use the complete 169,042-byte original recovered from the archive',
    r'Recovered \url{https://old.mccme.ru/gelfand/notes/chapter_011/11_part_000018.png}; the supplied file is its exact prefix, and downloaded neighboring P000721/P000723 match the supplied files byte for byte. The full recovered page was visually read; see \texttt{work/code/output/scan\_722\_recovery.json}.'),
3: (
    r'Quadratic central element',
    r'\(4E_-E_+-H^2+2H\)',
    r'\(4E_-E_++H^2+2H\)',
    r'The complete recovered P000722 and P000726 scans retain the minus sign. Standard positive matrix generators on P000722 give \([E_+,E_-]=H\); a direct commutator check requires \(+H^2\). This is a notebook error, not a transcription correction.'),
4: (
    r'Right pair of arrows in the three-vertex diagram',
    r'\(e_{13},e_{31}\) arrow labels',
    r'For left modules, \(e_{ij}:L_j\to L_i\); reverse the inconsistent right-hand labels',
    r'The right pair conflicts with the displayed matrix units while the left pair uses the left-module convention. A global transpose does not repair both pairs. Scan inspected.'),
5: (
    r'Upper-left matrix order',
    r'Vanishing positions transposed relative to P000723',
    r'State the left/right-module convention and transpose the entire order if changing it',
    r'P000723 and P000724 scans give different off-diagonal vanishing patterns. They can describe opposite/transposed orders but are not literally the same presentation without a convention change.'),
6: (
    r'Compact generator spectrum',
    r'\(\operatorname{Spec}(X_0)\subset2\mathbb{Z}\)',
    r'\(\operatorname{Spec}(X_0)\subset2i\mathbb{Z}\)',
    r'For \(X_0=E_+-E_-\), the compact generator acts skew-Hermitian in the usual unitary convention. P000729 explicitly gives \(2ik\) on the Fourier vectors, confirming the missing \(i\).'),
7: (
    r'Normalizer of the left ideal',
    r'Smallest subalgebra in which \(J\) is a two-sided ideal',
    r'Largest such subalgebra: the normalizer \(N(J)\)',
    r'The displayed normalizer definition and quotient require the largest subalgebra preserving the ideal. Scan confirms the adjective.'),
8: (
    r'Casimir on functions homogeneous of degree \(s\)',
    r'\(-s^2+2s\)',
    r'\(s(s+2)\) in the displayed homogeneous-degree convention',
    r'Substituting \(E_+=x_1\partial_{x_2}\), \(E_-=x_2\partial_{x_1}\), and \(H=x_1\partial_{x_1}-x_2\partial_{x_2}\) into the corrected central element gives \(s(s+2)\). Scan checked.'),
9: (
    r'Second parameter at the trivial central character',
    r'\(z=0\) at \(s=0\) and \(s=2\); the dual reducibility point is \(s=2\)',
    r'The second point is \(s=-2\) in the stated homogeneous-degree convention',
    r'The corrected Casimir eigenvalue \(s(s+2)\) vanishes at \(0\) and \(-2\). The dual principal-series extension occurs at degree \(-2\); the notation \(s=2\) uses the opposite parameter convention.'),
10: (
    r'Weyl reflection on the principal-series parameter',
    r'\(s\mapsto2-s\)',
    r'\(s\mapsto-s-2\) for functions homogeneous of degree \(s\)',
    r'The notebook mixes the homogeneous-degree parameter with its negative; \(2-s\) is the reflection for the latter convention. It cannot be combined unchanged with the preceding formulas.'),
11: (
    r'First gauge-group example',
    r'\(\operatorname{SU}(1)\)',
    r'\(\operatorname{U}(1)\)',
    r'\(\operatorname{SU}(1)\) is trivial; the electromagnetic abelian example is \(\operatorname{U}(1)\). The scan confirms \(\operatorname{SU}(1)\), so the notebook itself is corrected.'),
12: (
    r'Topological charge formula',
    r'\(\int F\wedge F\)',
    r'Include an invariant trace and normalization; for example, \(-\frac{1}{8\pi^2}\int\operatorname{tr}(F\wedge F)\) in a fixed anti-Hermitian convention',
    r'Matrix-valued curvature must be traced to obtain a scalar characteristic number. Orientation and self-duality conventions determine its sign.'),
13: (
    r'Action minimizers',
    r'Strict local minima at self-dual fields',
    r'Absolute minima within a fixed topological sector, with gauge and moduli zero directions',
    r'Gauge-equivalent connections and distinct instantons of the same charge have the same action. The scan retains strict; the Bogomolny decomposition gives the qualified statement.'),
14: (
    r'Pullback of an instanton',
    r'An arbitrary continuous map of the sphere pulls an instanton back to an instanton',
    r'Conformal diffeomorphisms preserve the relevant self-duality equation; arbitrary continuous maps do not',
    r'Continuity alone does not define a pulled-back smooth connection, and a general smooth pullback need not preserve the Hodge star. Scan checked.'),
15: (
    r'Multi-instanton parameter attribution',
    r"\(5n+4\) parameters attributed to 't Hooft",
    r'Jackiw--Nohl--Rebbi family; distinguish raw parameters, redundancies and gauge quotient',
    r"Atiyah--Hitchin--Singer, PNAS 74 (1977), p.2662 explicitly distinguish the \(5n\) family of 't Hooft from the \(5n+4\) family of Jackiw et al.; both primary pages read."),
16: (
    r'Self-dual Lax pair',
    r'The spectral parameter occurs with the same relative signs in both factors',
    r'Choose compatible opposite relative signs for the stated self-duality convention',
    r'Direct expansion of the commutator and comparison with the corrected pair on P000741 reveal the relative-sign inconsistency; absolute signs depend on the chosen complex coordinates.'),
17: (
    r'Twistor fibre',
    r'All linear complex structures on \(\mathbb{R}^4\) form \(\mathbb{CP}^1\)',
    r'Orthogonal complex structures compatible with a fixed orientation form \(\mathbb{CP}^1\)',
    r'Without orthogonality the space is \(\operatorname{GL}^{+}(4,\mathbb{R})/\operatorname{GL}(2,\mathbb{C})\), not a two-sphere. The metric/orientation hypotheses are missing from the notebook.'),
18: (
    r'Top projection arrow',
    r'\(\mathbb{CP}^3\leftarrow S^4\)',
    r'\(\mathbb{CP}^3\longrightarrow S^4\)',
    r'The twistor fibration projects complex lines to quaternionic lines. The scan confirms the reversed arrow.'),
19: (
    r'Fibre label in the bottom diagram',
    r'\(\mathbb{CP}^2\)',
    r'\(\mathbb{CP}^1\)',
    r'The fibre is the projective line of complex lines in one quaternionic line; scan inspected.'),
20: (
    r'Integrability criterion',
    r'Two arbitrary spanning fields commute',
    r'The distribution is involutive; a suitable local coordinate frame can be chosen commuting',
    r'Vanishing of the commutator of every chosen spanning pair is stronger than Frobenius involutivity. The source is abbreviated.'),
21: (
    r'Definition of an inner function',
    r'\(\lvert u\cdot e^{it}\rvert\)',
    r'\(\lvert u(e^{it})\rvert\)',
    r'The definition of an inner function uses boundary values of \(u\) on the unit circle. The handwritten juxtaposition denotes evaluation; literal multiplication would make the formula incorrect.'),
22: (
    r'Singular inner factor',
    r'Positive sign in the singular-measure exponential',
    r'Negative sign for a positive singular measure',
    r'The Poisson kernel has positive real part, so the singular inner factor is \(\exp\bigl(-\int\frac{\zeta+z}{\zeta-z}\,d\mu(\zeta)\bigr)\); the scan confirms the positive sign.'),
23: (
    r'Polynomial linear combination',
    r'The final coefficient is \(u_{r+1}\)',
    r'The final coefficient is \(u_r\) for the displayed list \(u_1,\ldots,u_r\)',
    r'The number of listed functions and degree \(r-1\) determine the final index; scan inspected.'),
24: (
    r'Hamiltonian of pole motion',
    r'\(\frac12\sum_i p_i^2+\sum_{i<j}(q_i-q_j)^{-2}\)',
    r'\(\frac12\sum_i p_i^2-4\sum_{i<j}(q_i-q_j)^{-2}\) when \(p_i=q_{i,y}\)',
    r'Laurent expansion for precisely the notebook KP equation and \(u=-2\sum_j(x-q_j)^{-2}\) gives \(q_{i,yy}=-8\sum_{j\ne i}(q_i-q_j)^{-3}\). Independently verified by the assembler in \texttt{work/code/check\_kp.py}. Other time/Poisson conventions must be explicit.'),
25: (
    r'Lax operator and time sign',
    r'\(L_2=D^3+\frac32uD+u\); \([\partial_y-L_1,\partial_t-L_2]=0\)',
    r'\(M=D^3+\frac32uD+w\), \(w_x=\frac34(u_{xx}+u_y)\); \([\partial_y-L_1,\partial_t+M]=0\) for the notebook equation',
    r'The scan unmistakably ends with \(+u\). Direct operator expansion yields the displayed correction for the notebook KP sign; changing the time sign changes the PDE. Independent symbolic check saved by the assembler.'),
26: (
    r'Record 435 date',
    r'Catalogue: 21 September 1977',
    r'Source heading: 21 November 1977 (21/XI/77)',
    r'The manuscript XI is clear and underlined; transcriptions retain it. Catalogue date is retained only as catalogue metadata.'),
27: (
    r'Equation (3) summation index',
    r'\(\sum_{i=1}^r A_\mu^{ij}s_j\)',
    r'\(\sum_{j=1}^r A_\mu^{ij}s_j\)',
    r'The free index is \(i\) and the repeated vector index is \(j\); the scan confirms lower summation index \(i\).'),
28: (
    r'Equation (2), duality convention',
    r'\(F_{\mu\nu}=\varepsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}\)',
    r'Include \(1/2\) if summing over both ordered complementary indices; no factor if a single ordered complementary pair is intended',
    r'The preceding sentence describes a complementary pair, while the formula resembles Einstein summation. Record the convention instead of silently adding a factor.'),
29: (
    r'Quaternionic conjugation notation',
    r'The antilinear map on \(\mathbb{C}^4\) is called an involution',
    r'It squares to \(-1\) on \(\mathbb{C}^4\); its projectivization is a fixed-point-free involution',
    r'Substitution in the written coordinate formula gives \(\sigma^2=-\operatorname{id}\), while multiplication by \(-1\) acts trivially projectively.'),
30: (
    r'Pulled-back curvature criterion',
    r'\(D^*F=0\)',
    r'\((D^*F)^{2,0}=0\), together with the conjugate condition for a unitary connection',
    r'The following coordinate equations and the twistor construction require vanishing of a type component, not the entire nonzero instanton curvature.'),
31: (
    r'Composition with quaternionic antilinear map',
    r'\(\ell\circ\sigma\)',
    r'\(\overline{\ell}\circ\sigma\) with the appropriate conjugate target',
    r'The source composition of a complex-linear map with \(\sigma\) is antilinear; target conjugation is required for the claimed complex-linear monad map. Scan checked.'),
32: (
    r'Upper tensor-product arrow',
    r'\(H\otimes\mathbb{C}\)',
    r'\(H\otimes\mathbb{C}^4\)',
    r'The next construction uses four columns for every basis vector and a \(4n\) by \(4n\) Gram matrix; the exponent \(4\) is absent in the scan.'),
33: (
    r'Basis of \(I\)',
    r'\(e_1,\ldots,e_r\)',
    r'\(e_1,\ldots,e_n\)',
    r'The declared dimension of \(I\) is \(n\), and the vectors \(e_{ij}\) run through \(n\) rows. Scan checked.'),
34: (
    r'Frame of the orthogonal complement',
    r'\(L^\perp\) is generated globally by \(2n\) sections over \(S^4\)',
    r'The displayed affine formulas give a frame on the \(\mathbb{R}^4\) chart; no such global frame on \(S^4\) is implied',
    r'For nonzero instanton charge the complement has nontrivial Chern class and cannot be globally framed by exactly its rank many independent sections. The formulas use affine \(x\) coordinates.'),
35: (
    r'Equation (7), occupation density',
    r'\(a^*(k^{\prime})a(k)\)',
    r'\(a^*(k)a(k)\)',
    r'The extra prime is visible in the scan but no independent \(k^{\prime}\) is integrated or defined; the free number density needs equal arguments.'),
36: (
    r'Equation (18), relativistic energy',
    r'\(\sqrt{p_k^2+M(\alpha_k)}\)',
    r'\(\sqrt{p_k^2+M(\beta_k)^2}\) in the preceding parameter convention',
    r'The preceding text makes \(\beta\) the internal period parameter and \(\alpha\) the initial phase. The mass must be squared and cannot depend on the time phase. Scan inspected.'),
37: (
    r'Equation (21), Poisson bracket order',
    r'\(\{u_t(x),u(y)\}=\gamma\delta(x-y)\)',
    r'\(\{u(x),u_t(y)\}=\gamma\delta(x-y)\) in the convention of equation (3)',
    r'The notebook reverses the order relative to its initial canonical bracket without changing the sign.'),
38: (
    r'Breather endpoint',
    r'\(0<\alpha\leq\pi/2\)',
    r'\(0<\alpha<\pi/2\) for a finite-period breather',
    r'At \(\alpha=\pi/2\), the frequency \(m\cos\alpha\) vanishes. It is a separatrix limit; the mass formula alone does not make the endpoint periodic.'),
39: (
    r'Equation (26), commutator convention',
    r'\([\pi(x),u(y)]=i\delta(x-y)\)',
    r'\([u(x),\pi(y)]=i\delta(x-y)\) in the usual convention matching equation (3)',
    r'The printed order is reversed relative to the earlier Poisson bracket. A different commutator convention would have to be stated.'),
40: (
    r'Unnumbered interaction after equation (26)',
    r'\(m^2\gamma^{-1}(1-\cos\gamma u)\)',
    r'Specify the field and coupling rescaling; canonical normalization is \(m^2\beta^{-2}(1-\cos\beta\varphi)\)',
    r'The displayed potential has quadratic term \(m^2\gamma u^2/2\) and hence does not preserve mass \(m\) under the usual canonical kinetic term. A convention ambiguity is retained.'),
41: (
    r'Equation (32), stationary phase',
    r'\(\widetilde{\Psi}(mx/t)e^{ix^2/(2mt)}\)',
    r'\(\sqrt{m/(2\pi t)}e^{-i\pi/4}\widehat{\Psi}(mx/t)e^{imx^2/(2t)}\) for the stated Fourier normalization',
    r'Critical point \(p=mx/t\) and phase value \(mx^2/(2t)\) follow directly. The missing amplitude depends on the Fourier convention but includes \(t^{-1/2}\). Scan checked.'),
42: (
    r'Stationary sine-Gordon fluctuation potential',
    r'\(q(x)=1/\cosh^2x\)',
    r'\(K=-\partial_x^2+m^2-2m^2\operatorname{sech}^2(mx)\)',
    r'Korepin--Faddeev 1975, equation (16), and the second variation of the stated kink give the negative coefficient, factor two and asymptotic mass. The translation zero mode must be excluded from the determinant.'),
43: (
    r'No-higher-corrections conjecture',
    r'\(M=8m/\gamma-m/\pi\) exactly',
    r'Specify the renormalized mass convention before deciding the claim',
    r'The physical lightest-breather mass gives \(M/m_1=[2\sin(\pi\xi/2)]^{-1}\), \(\xi=\gamma/(8\pi-\gamma)\), whose expansion has a nonzero \(\gamma/192\) term. This does not determine a differently renormalized parameter \(m\).'),
44: (
    r'Final handwritten sentence',
    r'\ru{Массивные частицы появляются как солитоны} / Massive particles appear as solitons',
    r'\ru{Массивные частицы рассеиваются как солитоны} / Massive particles scatter like solitons',
    r'The verb \ru{рассеиваются} is legible in the scan, independently read by both the record editor and chapter assembler. This changes the meaning to a scattering comparison.'),
45: (
    r'Record 436 envelope endpoint',
    r'Catalogue routing window includes these pages in Faddeev material',
    r'These pages begin S. I. Gelfand, 13 February 1978; combine with the continuation under record 438',
    r'Date and speaker heading on P000753; mathematical continuation on P000756. The late-record editor handles this adjacent precursor explicitly.'),
}
assert set(cells) == set(range(1, 46))
metadata_before = [(r['page'], r['applies_to'], r['type']) for r in rows]
display_fields = ['place', 'transcription_reads', 'should_read', 'evidence']
for number, row in enumerate(rows, 1):
    row.update(zip(display_fields, cells[number]))
    for name in display_fields:
        value = row[name]
        assert value.count(r'\(') == value.count(r'\)'), (number, name, 'unbalanced math')
        assert '\\\\' not in value, (number, name, 'doubled backslash')
        assert not re.search(r'[\x00-\x1f]', value), (number, name, 'control character')
        # Remove inline math, URL arguments and escaped underscores, then check
        # the two text-mode characters that caused the original build failures.
        text = re.sub(r'\\\(.*?\\\)', '', value)
        text = re.sub(r'\\url\{[^}]*\}', '', text)
        text = text.replace(r'\_', '')
        assert not re.search(r'[_^]', text), (number, name, 'naked sub/superscript')
        assert not re.search(r'(?<!\\)[%&#$]', text), (number, name, 'unescaped special character')
assert metadata_before == [(r['page'], r['applies_to'], r['type']) for r in rows]
with F.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(rows)
print('Repaired 45 correction rows; preserved order, page, type and applies_to.')
