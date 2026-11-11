"""Typeset the already audited root-block correction log as valid LaTeX."""
import csv
from pathlib import Path

p = Path(__file__).resolve().parent/'corrections.csv'
rows = list(csv.DictReader(p.open()))
changes = {
 'Orbit label after the invariants': {
  'transcription_reads':r'\(\Omega_{c_1,c_2}\)',
  'should_read':r'\(\Omega_{c_2,c_3}\)',
  'evidence':r'The same discussion fixes \(\operatorname{tr}X^2\) and \(\operatorname{tr}X^3\); the inconsistent subscripts are present in the scan.'},
 'Riemann–Roch multiplicity formula': {
  'transcription_reads':r'\(X=p^{-1}(y_0)\)',
  'should_read':r'\(X=\mu^{-1}(\nu)/T\), with descended prequantum data'},
 'Fractional derivative integral': {
  'should_read':r'Insert \(1/\Gamma(-p)\), initially \(\operatorname{Re}p<0\), then continue'},
 'Darboux coordinates for odd binary forms': {
  'transcription_reads':r'Overwritten sign before the \(p_{n-1}\) term',
  'should_read':r'Use a minus sign before \(p_{n-1}\) and alternating signs thereafter.'},
 'Space of lines identified with cotangent space': {
  'transcription_reads':r'\(T^*\mathbb R^2\)',
  'should_read':r'Locally \(T^*\mathbb R^2\); globally oriented lines form \(T^*S^2\).',
  'evidence':r'Givental 1983, Example 1, explicitly uses the reduced \(T^*S^{n-1}\). Orientation is not stated in the notes.'},
 'Index formula with a possible boundary': {
  'transcription_reads':r'\(M\) possibly has boundary, followed by \(\operatorname{ind}D=\int\alpha_0\)',
  'should_read':r'Assume \(M\) is closed for this equality, or specify a boundary realization and correction.'},
 'Hypothesis preceding the uncorrected signature formula': {
  'transcription_reads':r'\(\partial M\ne\varnothing\)',
  'should_read':r'\(\partial M=\varnothing\) for formulas (6)--(7) without a boundary term'},
 'div–grad–curl base dimension': {
  'transcription_reads':r'In \(\mathbb R^4\)',
  'should_read':r'On \(\mathbb R^3\), acting on a scalar plus a three-component vector',
  'evidence':r'The same example explicitly says \(\mathbb R^3\) on P001024; standard curl in this matrix is three-dimensional.'},
 'Square of the vector-calculus matrix': {
  'transcription_reads':r'All positive \(\operatorname{div},\operatorname{grad},\operatorname{curl}\) entries square to \(\Delta I\)',
  'should_read':r'With conventional operators use upper-right \(-\operatorname{div}\) and obtain \(-\Delta I\); the displayed all-positive matrix has vector block \(2\operatorname{grad}\operatorname{div}-\Delta I_3\).',
  'evidence':r'Independent symbolic multiplication and \(\operatorname{curl}\operatorname{curl}=\operatorname{grad}\operatorname{div}-\Delta\) verify the correction.'},
 'Boundary restriction in (15)': {
  'transcription_reads':r'\(P_A(f|_A)=0\)',
  'should_read':r'\(P_A(f|_Y)=0\), \(Y=\partial M\)'},
 'Normal tangential operator attributed to APS': {
  'transcription_reads':r'\(A\) normal; eta defined through real parts of eigenvalues'},
 'Boundary operator domain and codomain': {
  'transcription_reads':r'\(A:E|_Y\to F|_Y\) with spectral eigenspaces',
  'should_read':r'\(D=\sigma(\partial_u+A)\), \(A:E|_Y\to E|_Y\) after identifying bundles by the normal symbol'},
 'Positive spectral projector and zero-mode term': {
  'transcription_reads':r'\(P_+\) projects to positive eigenfunctions, with correction \(-(h+\eta)/2\)'},
 'The sum of the two spectral halves': {
  'transcription_reads':r'\(\zeta(A)=\zeta_+(A)+\zeta_-(A)\)',
  'should_read':r'For functions of \(s\) use \(\zeta_{|A|}\); at zero state the phase and regularity conventions.'},
 'First argument of zeta in (16)': {
  'transcription_reads':r'Overwritten \(0\) or \(\theta\)',
  'should_read':r'\(\zeta_\theta^A(0,x)\)'},
 'Integer symbol in (19)': {
  'transcription_reads':r'\(\rho(i),\rho_\ell,b_{m(i-1)-n}/\lambda^\ell\)',
  'should_read':r'Use \(\ell\) consistently for the integer argument and symbol index'},
 'Range in the hint following (d)': {
  'transcription_reads':r'All integer points \(>0\)',
  'evidence':r'The scan clearly has \(>0\), as already noted diplomatically.'},
 'Pseudodifferential scope of (d)': {
  'transcription_reads':r'\(\rho(\ell)=0\) for every nonpositive integer after mentioning pseudodifferential operators',
  'should_read':r'Keep general zero-value independence; other integer values are governed by \(\operatorname{Res}(\Pi A^{-\ell})\). Even differential operators can have nonzero cut differences at negative integers.'},
 'Second sum of the shift formula (20)': {
  'transcription_reads':r'\(t^k\sum_{\mu=1}^n(-1)^\mu\delta_\mu/[\mu\binom{k+\mu}{k}]\)',
  'should_read':r'Insert \(t^\mu\) in each summand, giving \(t^{k+\mu}\).',
  'evidence':r'The extra factor is absent in the scan. The binomial complex-power expansion and the \(t=0\) check both show it is necessary.'},
}
for row in rows:
    row.update(changes.get(row['place'], {}))
with p.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(f'Normalized {len(rows)} correction rows; mathematical readings unchanged.')
