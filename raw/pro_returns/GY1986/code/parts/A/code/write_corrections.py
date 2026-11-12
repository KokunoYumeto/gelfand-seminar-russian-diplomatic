#!/usr/bin/env python3
"""Write the slice-A correction ledger; none of the source files is edited."""
import csv
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
ROWS = []

def row(page, place, reads, proposed, evidence, kind='faithful_error', applies='both'):
    ROWS.append(dict(page=page, place=place, transcription_reads=reads,
                     should_read=proposed, evidence=evidence, applies_to=applies, type=kind))

row('P001257', 'Boundary fragment before the Kontsevich heading',
    'Page included in the catalogue range of record 667',
    'Preserve as a Beilinson continuation, indexed at 1986-667.4 only for catalogue containment; do not attribute it to Kontsevich.',
    'The next heading begins on P001258; the determinant-line discussion continues 1985-666.21 and is separately attributed in the item.', 'provenance')
row('P001258', 'Kontsevich session heading', '24/II-85; catalogue record 667: 1987-02-24',
    'Retain both readings and flag the conflict; the neighboring session headings read 1986. Do not silently select a priority date.',
    'Original scan directly inspected; the year 85 is visible. The catalogue date is preserved in talks.json.', 'provenance')
for page, records, catalogue, manuscript in [
    ('P001259','668','1987-02-24','24.2.86'),
    ('P001262','669 and 670','1987-03-03','3/III-86'),
    ('P001268','671','1987-03-10','10/III-86'),
    ('P001274','672 and 673','1987-03-24','24/III-86'),
    ('P001281','674 and 675','1987-04-07','7/IV-86'),
    ('P001287','676','1987-04-28','28.4.86'),
    ('P001290','677 and 678','1987-05-05','5/V-86')]:
    row(page, 'Date of records '+records, 'Catalogue: '+catalogue+'; manuscript: '+manuscript,
        'Preserve the catalogue date but display the manuscript date separately, with a discrepancy flag.',
        'Russian and English page headings agree on the manuscript year; 1986 dates are Mondays. Olshanskii 1987 independently records presentation by Gelfand on 5 May 1986.', 'provenance')
row('P001257-P001298', 'Overlapping catalogue page ranges', 'Adjacent catalogue ranges include parts of neighboring talks',
    'Use the named manuscript headings to assign items; retain the catalogue ranges as provenance only.',
    'Per-record summaries state the actual boundaries; in particular P001282 changes from Cherednik to Kogan, P001291 changes from Olshanskii to Cherednik, and P001298 changes to Ovsienko and Kazakov.', 'provenance')
row('P001258', 'Tangent-space quotient', r'\(\mathfrak g/\mathfrak k\)', r'\(\mathfrak g/\gamma\) for the decorated moduli problem, with the curve-dependent stabilizer retained.',
    'Scan and following Kodaira--Spencer formula; Kontsevich 1987, section 1; item 1986-667.2.')
row('P001260', 'Equation (16), determinant variation', r'\(\delta_y\delta_{\bar y}[\det\Delta_j/(\det N^{(j)}\det N^{(1-j)})]=c_j\)',
    'Interpret as curvature: mixed derivatives of the logarithm of the determinant-line norm, with the universal two-form and normalization supplied.',
    'Scan directly inspected; Belavin--Knizhnik 1986, section 3; item 1986-668.7. The missing logarithm is absent in the manuscript too.')
row('P001263', 'Example (9), pure weight filtration', r'\(W_a=H^a(C,\mathbb Z),\ W_{a+1}=0\)',
    r'\(W_{a-1}=0\), with the filtration considered over \(\mathbb Q\); preserve the written plus sign in the diplomatic text.',
    'Scan directly inspected; the very next definition (10) explicitly has the correct subscript a-1; item 1986-669.3.')
row('P001263', 'Example (9), purity hypothesis', 'A smooth complex manifold has pure Hodge structure in every degree',
    'For this standard assertion require a smooth proper complex algebraic variety, or an appropriate compact Kahler hypothesis; a general smooth open variety has mixed cohomology.',
    'Scan and Russian text; Deligne 1971, sections 2.1 and 3.2; item 1986-669.3.')
row('P001265', 'Particle-size comparison', r'Proton size approximately \(10^{-35}\,\mathrm{cm}\)',
    'Flag the numerical entry as inconsistent with the notebook comparison on P001269; do not silently manufacture a corrected measurement.',
    'The English and Russian entries agree; item 1986-670.1 records the discrepancy as a notebook error.')
row('P001266', 'Equation (10), Green kernel', 'One Abelian-integral factor and a theta function are written schematically',
    r'Complete the harmonic correction as a quadratic form in \(\operatorname{Im}\int\omega\), and use the prime form or specify the half-differential factors and normalization.',
    'Scan directly inspected; the second vector factor is suppressed. Belavin--Knizhnik 1986, section 2; item 1986-670.3.', 'ambiguity')
row('P001270', 'Equation for the harmonic winding representative', 'Both holomorphic and antiholomorphic terms appear with plus signs',
    r'\(x_{\mathrm{cl}}(z)=((\Lambda_1-\bar\tau\Lambda_2)z-(\Lambda_1-\tau\Lambda_2)\bar z)/(2i\operatorname{Im}\tau)\) for the two written shifts.',
    r'Original scan checked; direct substitution in \texttt{code/check\_editorial.py} verifies shifts by tau and 1 and reality. Item 1986-671.5.')
row('P001270', 'Equation (12), sign of the functional-integral action', 'A positive kinetic-action exponent is displayed in the Euclidean functional integral',
    r'Use \(e^{-S_E}\) for a positive Euclidean action. The later winding sum (21) already has the correct negative exponent; do not change that line.',
    'Russian and English formulas (12) and (21) have different sign conventions; compact-boson construction in Gross et al. 1985; item 1986-671.6.')
row('P001271', 'Question about modularity and self-duality', 'Modularity without naming the modular group or transformation representation',
    'Distinguish a scalar full-group transformation from modularity for a congruence subgroup or a vector-valued representation.',
    'Poisson summation and the heterotic lattice construction; item 1986-671.7 and GP-1986-02. This is a hypothesis clarification, not a new open problem.', 'ambiguity')
row('P001272-P001273', 'Root-operator commutator', 'Zero when the sum of the two roots is not a root',
    'Exclude opposite roots from the zero case; their bracket has Cartan and central terms, with the required cocycle conventions.',
    'Russian and English text; identified Frenkel--Kac construction, with direct-original access limitation retained in item 1986-671.9.')
row('P001276', 'Question about complexifying real codimension-two arrangements', 'Real codimension two without further conditions on intersections',
    'Keep individual real codimension two distinct from the extra even-codimension intersection hypothesis of a 2-arrangement, and distinguish a linear complex structure from topological equivalence.',
    'Russian text and original scan checked by the integrating researcher; Ziegler 1993 and Batzies 2007; item 1986-672.8 and GP-1986-03.', 'ambiguity')
row('P001278', 'Plane-curve Milnor-fibre formula', r'\(\mu=2g-(\text{holes})+1\)',
    r'\(\mu=2g+b-1\) when holes denotes the number \(b\) of boundary components of the Milnor fibre.',
    'Scan directly inspected and Russian text agrees. Milnor 1968; item 1986-673.4. This is an emendation of a faithful reading.')
row('P001279', 'Sentence following equation (7)', 'The logarithmic exponent k is the size of a Jordan block',
    r'A block of size \(s\) permits logarithmic degree at most \(s-1\); a given period need not attain that maximum.',
    'Original scan shows the insertion for block size; Varchenko 1982, sections 1--2; item 1986-673.7.')
row('P001284', 'Equation (10), Virasoro commutator', r'\(L_{n-m}\)', r'\(L_{n+m}\)',
    'Scan directly inspected; the mode grading and Furuuchi--Ohta 2006 oscillator conventions determine the sum; item 1986-675.5.')
row('P001285', 'Equation (21), level-two constraint', r'\(\partial_\mu h_{\mu\nu}=A_\nu\)',
    r'The right side involves the level-two vector \(B_\nu\) of equation (16), up to its stated normalization, rather than the separate level-one vector \(A_\nu\).',
    'Original scan directly inspected. Equation (16) uses B for the coefficient of the mode -2; item 1986-675.7 renames it C for clarity.')
row('P001287', 'RTT relation, left side only', r'\(L^2(-\lambda_2)\)', r'\(L^2(\lambda_2)\) in the convention of the same equation on its right side.',
    'Original scan directly inspected; the unmatched minus sign is present in both transcriptions and incompatible with the coefficient presentation; item 1986-676.1.')
row('P001287', 'Quantum-determinant antisymmetrizer', 'Tensor degree n used where the matrix size is N',
    r'Use the top antisymmetrizer on \((\mathbb C^N)^{\otimes N}\); the finite level \(n\) is a different parameter.',
    'Original scan checked; quantum determinant definition in Molev--Nazarov--Olshanski 1996; item 1986-676.2.')
row('P001287', 'Possible quantum-determinant poles', r'\(i=0,\ldots,n-1\)', r'\(i=0,\ldots,N-1\) for the N shifted matrix factors, with orders controlled by the finite level.',
    'Original scan checked; item 1986-676.3 separates matrix size N from level n.')
row('P001289', 'Last line, symmetric-group order', r'\(S_n\), ord. \(n\)', r'\(S_n\) has order \(n!\); retain the written ord. n as notebook notation.',
    'Original scan directly inspected; the Russian abbreviation is por. n. Item 1986-676.6.')
row('P001291', 'Highest-weight-vector uniqueness', 'A unique highest-weight vector',
    'A unique highest-weight line in an irreducible highest-weight module; a vector requires a normalization.',
    'Russian and English highest-weight setup; item 1986-678.1.', 'ambiguity')
row('P001292', 'Two-dimensional antisymmetrization coefficient', r'Coefficient \(1/4\) in the scalar mixed determinant',
    r'Coefficient \(1/2\) for the normalized projector \((I-P)/2\).',
    r'Original scan directly inspected. \texttt{code/check\_editorial.py} computes the projector matrix exactly and also checks A=B=I; item 1986-678.3.')
row('P001293', 'First closure axiom', r'\(\overline{A\cap B}=\bar A\cap\bar B\)',
    r'Monotonicity: \(A\subseteq B\Rightarrow\operatorname{cl}(A)\subseteq\operatorname{cl}(B)\). Preserve the displayed stronger false identity as notebook text.',
    'Original scan directly inspected; the following span example and Oxley closure axioms determine the intended definition; item 1986-680.1.')
row('P001293', 'Closed singleton assertion', r'\(\bar e_i=e_i\) for a vector configuration',
    'Add simplicity: exclude zero vectors and parallel pairs. Looplessness alone is insufficient.',
    'Scan and vector-span example; Oxley and Gelfand--Serganova; item 1986-680.2.', 'ambiguity')
row('P001294', 'Two-generator Coxeter example', 'A finite integer product-order relation may still give an infinite rank-two group',
    r'The rank-two group has order \(2m\) for finite \(m\). Infinity requires the omitted product-order relation, written \(m=\infty\).',
    'Scan directly inspected; Coxeter 1934, introduction; item 1986-680.4.')
row('P001294', 'Icosahedral group discussion', 'The successive groups of order 120 are not distinguished',
    'Distinguish the full icosahedral reflection group H3 from the binary icosahedral subgroup of SU(2); the 600-cell has tetrahedral three-dimensional facets.',
    'Original scan inspected; Coxeter 1934 order table on p.618; item 1986-680.5.', 'ambiguity')
row('P001294', 'Bruhat-order definition', 'A reduced word occurs inside another reduced word',
    'Read as a subsequence of a reduced expression, not necessarily a consecutive substring; translated orders require a least element, not merely some minimal element.',
    'Scan and Gelfand--Serganova 1987, section 8; item 1986-680.6.', 'ambiguity')
row('P001295', 'Seven-point nonrepresentability example', 'Not every matroid is representable, illustrated by the seven listed triples',
    'The listed Fano matroid is nonrepresentable over the real or complex field but representable exactly in characteristic two; specify the field.',
    'Original scan inspected; the written triples identify the Fano lines. Oxley, Theorem 4.1; item 1986-680.8.', 'ambiguity')
row('P001295', 'Polynomial/exterior duality example near page foot', r'\(x_ix_n-x_kx_i\)', r'\(x_ix_k-x_kx_i\), with the same two indices in both products.',
    'Original scan and Russian/English formula; the immediately preceding commutator definition and paired dual monomial fix the intended index; item 1986-680.10.')
row('P001296', 'Coefficient sum in the quadratic-dual calculation', r'\(\sum a_{ij}x_ix_k\)', r'\(\sum a_{ij}x_ix_j\)',
    'Original scan inspected; repeated coefficient indices and the following symmetric-matrix condition determine the correction; item 1986-680.11.')
row('P001297', 'Definition of the subgroup in the symmetric space', 'Compact subgroup',
    'In the cited algebraic compactification theorem use the symmetric algebraic subgroup from an involution, with the specified normalizer. The abbreviation does not license an arbitrary compact real subgroup.',
    'Scan inspected; De Concini--Procesi setup explicitly recalled in Chirivi--Maffei 2004, section 1; item 1986-681.1.', 'ambiguity')
row('P001297', 'Normal-crossings parenthesis', 'Boundary codimension k and coordinate vanishing equations are conflated',
    r'The union is \(z_1\cdots z_k=0\), of codimension one; the intersection is \(z_1=\cdots=z_k=0\), of codimension k.',
    'Original scan and Chirivi--Maffei 2004, Proposition 1.1; item 1986-681.2.')
row('P001297', 'Picard restriction', 'An isomorphism onto the Picard group of the closed orbit',
    'Restriction is injective; its image is the specified subgroup generated by the relevant weights, not generally the entire Picard group.',
    'Original scan inspected; Chirivi--Maffei 2004, Propositions 1.2--1.4, citing De Concini--Procesi 1983, Proposition 8.1; item 1986-681.3.')
row('P001297', 'Commuting finite Hecke generators', r'\(j\ne i,i+1\)', r'\(|i-j|>1\)',
    'Original scan inspected; the written asymmetric exclusion incorrectly includes the adjacent generator i-1; Mathas 2004, section 2; item 1986-681.4.')
row('P001298', 'Proposed affine evaluation', r'\(X_{n-1}\mapsto qT_{n-1}^{2}\)', r'\(X_{n-1}\mapsto qT_{n-1}^{-2}\), and use inverse products recursively with the written Bernstein relation.',
    r'Original scan has the positive square. Exact noncommutative reduction and independent regular-representation check are in \texttt{code/check\_editorial.py}; item 1986-681.5.')
row('P001298', 'Transition after Cherednik polynomial-relation question', 'The full page is inside more than one catalogue range',
    'Assign the upper Hecke question to record 681 with Cherednik as intervention speaker; assign the lower named Ovsienko and Kazakov contributions to their own records.',
    'Original scan inspected; the speaker headings and change of subject are explicit; no page-level attribution is imposed.', 'provenance')

with (OUT/'corrections.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type'])
    writer.writeheader()
    writer.writerows(ROWS)
print(f'Saved {len(ROWS)} correction/provenance entries.')
