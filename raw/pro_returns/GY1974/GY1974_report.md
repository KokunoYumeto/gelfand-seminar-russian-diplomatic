# GY1974: critical companion to the 1974–75 seminar records

**Status date: November 2026.** The chapter covers all 30 requested catalogue
records and audits the adjoining earlier-year material included in the supplied
page range. It contains **265 mathematical occurrences**, **10 definite
problem entries**, **78 bibliography entries**, and **92 critical corrections
or qualifications**. The seven prescribed data/text files, this report, the
generated chapter, the XeLaTeX PDF, the supplied renderer and style, and
reproducible verification code are included.

## 1. Counts and their interpretation

An occurrence is a distinct mathematical act in the notes: a definition,
construction, theorem, claim, method, question or substantive remark. Repeated
explanations in different meetings receive separate identifiers. A rhetorical
prompt does not automatically become an open problem. Headings without
mathematics remain register entries and contribute zero items.

| Class | Items |
|---|---:|
| A | 29 |
| B | 10 |
| C | 0 |
| D | 0 |
| E | 203 |
| F | 23 |

A means published soon after by the speaker or Gelfand; B means subsequently
developed by others; E means known before the talk; F means the intended claim
cannot be identified sufficiently. C and D are reserved for precise unresolved
remainders or genuinely undeveloped claims. There are no C/D selections here.
This is a bounded conclusion about these pages and the evidence found.

Five entries, 1974-331.1–4 and 1974-332.1, are compatibility aliases for previously
indexed March 1974 source occurrences. The raw count is 265; removing these
five exact source duplicates leaves **260**. This is not a count of unique
theorems: exposition repeated on different pages remains a distinct occurrence.
The adjoining boundary audit does not inflate either count.

### By record owner

| Record speaker | Items |
|---|---:|
| A. A. Kirillov | 4 |
| A. G. Kushnirenko | 11 |
| A. M. Polyakov | 14 |
| B. A. Dubrovin | 28 |
| B. M. Gurevich | 1 |
| Czesław Bessaga | 7 |
| Enrico Giusti | 29 |
| Graeme Segal | 31 |
| I. M. Gelfand | 19 |
| James King | 23 |
| M. I. Graev | 17 |
| R. L. Dobrushin | 9 |
| S. P. Novikov | 15 |
| V. I. Arnold | 1 |
| V. N. Tulovskii | 33 |
| Ya. G. Sinai | 23 |

This table uses the primary catalogue speaker even where an intervention is
attributed to someone else or the register label adds an attribution caveat.
The accompanying audit_counts.json also supplies counts using
explicit item-level speaker overrides, every record's count, and the zero-item
headings. Standardized names are used; material catalogue variants are noted.

### By primary area

| Primary area | Items |
|---|---:|
| Characteristic classes and complex geometry | 27 |
| Elliptic PDE and variational problems | 29 |
| Gauge field theory | 14 |
| Integrable systems and spectral theory | 59 |
| Microlocal analysis and differential operators | 33 |
| Newton polyhedra and singularities | 12 |
| Representations and current groups | 21 |
| Statistical mechanics and random fields | 32 |
| Topology, configurations and buildings | 38 |

These are exclusive groups assigned by the record's principal topic. Algebraic
geometry within finite-gap lectures is counted with integrable systems; the
Bernstein intervention is counted within the microlocal sequence. This prevents
double counting. Multiple subject tags would be useful for a website, but are
not a field in the prescribed schema.

### Assessment dimensions

| Literal correctness | Items |
|---|---:|
| not determinable | 28 |
| false as written | 36 |
| correct | 45 |
| correct with missing hypotheses | 156 |

| Publication match | Items |
|---|---:|
| thematic only | 18 |
| exact | 163 |
| partial | 79 |
| none found | 5 |

| Verification level | Items |
|---|---:|
| publisher metadata checked | 4 |
| read the result | 241 |
| indirect | 9 |
| unresolved lead | 11 |

| Correction type | Rows |
|---|---:|
| provenance | 10 |
| ambiguity | 28 |
| faithful_error | 54 |

These axes are independent. A classical E result may have a false literal
formula. An exact identification of the reconstructed theorem does not
establish every copied coefficient. “Verified” in the bibliography means the
indicated page, DOI destination or text was opened; it does not mean every
theorem in that work was read. The bibliography annotations and item-level
verification fields state the actual scope.

## 2. Main findings and their implications

### Finite-gap theory: contemporary results and prior exposition

Records 336, 339, 340 and 343 form a sustained sequence from monodromy and
spectral bands to Riccati densities, finite-gap polynomials, divisors, Abel maps
and Jacobian flows. A stationary higher-KdV equation implying finite-gap
spectrum and the converse are separate claims. Inverse reconstruction also
needs divisor information beyond the gap endpoints.

Chronology resolves several plausible misclassifications. Novikov's paper was
received on 18 February 1974 and the publisher dates it to July 1974; results
already contained there are E in September. The joint Dubrovin–Novikov
announcement was received on 3 June 1974 and published later that year; §3 gives
the converse and algebraic-geometric description. The fuller 1976 survey is
not treated as the first circulation of all its contents (Novikov, 1974;
Dubrovin & Novikov, 1974; Dubrovin et al., 1976).

The quartic coefficient 5/2 on P000555 makes the claimed Poisson bracket
nonzero; 5/8 gives involution after the parameter identification is stated.
A separate squared-eigenfunction calculation audits the spectral quintic.
It documents a discrepancy under explicit coordinates and preserves the
unresolved comparison with source sign conventions. The diplomatic text is
not silently repaired, and a later source's typographical difficulty is not
treated as evidence that the notebook's formula is correct.

### Elliptic regularity: the solution class controls the theorem

Giusti's lectures distinguish scalar regularity, partial regularity of systems
and discontinuous vectorial examples. Energy-class assumptions, coefficient
continuity, strong ellipticity, and the difference between regularity of a map
and of its gradient are restored. A strict Hausdorff-dimension bound below n−2
requires more than vanishing (n−2)-dimensional measure; the two statements are
not conflated (Mingione, 2006; De Filippis et al., 2026, §1.1, Equations 1.1–1.2).

For the tensor on P000565, substitution of the claimed radial solution fails
already away from the origin. Replacing the first coefficient by 4/(n−2)
gives a symmetric analytic bounded uniformly elliptic tensor and an energy-class
weak solution for n≥3. The audit verifies the energy integral and vanishing
flux at the puncture, not merely the pointwise equation. It proves existence,
not the unverified uniqueness assertion. Nor is this homogeneous system
automatically the Euler–Lagrange equation of a similar-looking functional
whose coefficients depend on the unknown.

### Topology: keep the low-dimensional cases and quotient hypotheses

Segal's configuration lecture separates earlier configuration-space
approximation from later signed-particle and scanning results. The cancellation
model has a different loop-space target from a sphere alone. The target and its
topology are matched explicitly rather than inferred from a crossed-out formula
(McDuff, 1975; Kallel, 1998).

The classifying-space lecture explains older category and building theory.
Its hyperplane proof was independently checked against a later dual-cover
argument. The meaningful qualifications are that thin categories are preorders
unless skeletal; zero is excluded from the building; quotient arguments need
cofibrations; and the Steinberg module uses reduced homology. In dimension two
over a finite field, the building has q+1 points, so ordinary H₀ has rank q+1
and reduced H₀ has rank q. The notebook's own base case detects the missing
tilde (Segal, 1968; Quillen, 1973, 1978).

### Newton data, gauge theory and probability

The two Newton questions remain distinct. The local Milnor-number theorem
provides a lower bound with equality under face nondegeneracy. The global
critical-point theorem provides an upper bound with equality under a condition
at infinity. A generic mixed-volume theorem would not preserve the
gradient-specific content (Kushnirenko, 1975, Theorems I–II).

The lattice discussion needs a specified gauge group, measure, action,
boundary and limit. The Bessel expression is an Abelian specialization;
normalized SU(2) Haar measure gives another one-plaquette integral. Area and
perimeter laws are not a universal two-phase theorem without a model and a
regime. Wilson's circulating 1974 work and later exact formulations are matched
within this restricted scope (Wilson, 1974).

Sinai's contour and phase-diagram lecture matches the subsequent Pirogov–Sinai
publication closely. Its finite list must concern appropriate extremal
periodic or translation-invariant phases: convex mixtures alone prevent a
literal assertion of only k Gibbs measures. Dobrushin's conditional-law
programme is older; its existence and uniqueness theorems have specified
hypotheses. No classification of every specification or every phase is claimed
(Dobrushin, 1968; Pirogov & Sinai, 1975, 1976).

### Microlocal and complex-analytic conventions

Tulovskii's sequence is checked against Hörmander (1971) and Duistermaat and
Hörmander (1972). Fourier signs are fixed consistently. Conic homogeneity is
essential in the normal-form statement: a radial Hamilton vector cannot
become nonradial under a homogeneous canonical transformation. A Lagrangian
leaf need not be either Euclidean space or a torus; a complete cylinder gives
a fully checked counterexample.

King's divisor formulas require current-degree conventions, multiplicities,
the Poincaré–Lelong sign and a Stokes boundary term. Raw growth integrals and
radially integrated characteristics are different quantities. The radius
power and Jensen normalization are explicit. The curvature comparison uses
the actual positivity and determinant inequalities, and the notebook's
opposite Ricci convention is identified (Griffiths & King, 1973; Griffiths, 1971).

## 3. Difficulties and source-search methods

The productive route was usually from a precise formula or construction to
a short original announcement, and then to a fuller text. Math-Net supplied
Soviet metadata, receipt dates and many original PDFs. Author-hosted papers,
NUMDAM, publisher pages and arXiv supplied other primary texts. Later work
sometimes located an earlier reference or checked a normalization; that
indirect step is declared.

The principal difficulties were:

1. Distinguishing an exact answer from thematic resemblance, especially for
   entire-function data, p-adic analogies and the elliptic-resolution proposal.
2. Separating circulation and publication dates, including the two 1974
   finite-gap papers, Wilson's preprint and the 1973 current-group paper.
3. Comparing coordinates when the notebook and an accessible source both
   contain apparent typographical or normalization problems.
4. Preserving unreadable fragments instead of assigning a theorem that the
   speaker might plausibly have discussed.
5. Resolving the erroneous opening year and overly wide record-page envelopes.

The group research logs identify read results, metadata-only checks and
failed leads. A failed fetch is not evidence that a work does not exist.
Sometimes the indexed primary-PDF result remained readable after direct
fetches timed out; the access route is recorded. No absence-of-hit argument
is used to create a class D item. The search was bounded, and is not represented
as an exhaustive search of every bibliography or unpublished archive.

## 4. Why there is no Stage 2 open-problem selection

No C/D item survives the precise-statement test. Definite questions have
established answers in stated settings; attractive unfinished directions
lack essential quantifiers, topology, normalization or admissible objects.
They are retained as F or limited partial matches.

For example, arbitrary entire functions of order one need not be compatible
with an energy-independent Schrödinger potential. A concrete pair fails;
a common exponential factor, conversely, can produce entire data from
polynomial data without changing the potential. The verification section
proves the exact local compatibility criterion and factor invariance.
Marchenko and Ostrovskii's normalized periodic inverse theorem and Gesztesy's
infinite-genus construction are relevant later results, but neither is an
answer for arbitrary unnormalized entire pairs (Marchenko & Ostrovskii, 1975;
Gesztesy, 1999).

The development file is an **editorial verification appendix**. Proved and
computed statements have the prescribed markers, exact hypotheses and no
novelty claims. Where no historical evidence was found for abandonment of a
programme, its reason is left unknown. A further run would first need a
chosen precise formulation; it cannot responsibly promise a general solution
to the notebook's unformulated directions.

## 5. Independent checking and reproducibility

The audits use independent derivations. The Riccati identity is checked through
the product of two Schrödinger solutions and their constant Wronskian.
The Hamiltonian bracket is checked by coefficient differentiation and exact
polynomial arithmetic. The radial tensor is checked by contraction, divergence,
ellipticity and the weak extension through the origin. The logarithmic integral
is proved using real dilogarithm identities, then checked by a convergent series
and a separately transformed numerical integral.

Code and output distinguish exact algebra from numerical evidence. Finite
rational substitutions supplement the proof; they are not proofs for every
parameter. Decimal truncation bounds are not presented as rounding bounds.
Constant-potential and one-dimensional checks test convention-sensitive signs.
The final validation record gives the actual schema and TeX build outcomes.

To rebuild from this directory:

    python3 build_chapter.py GY1974
    xelatex -interaction=nonstopmode -halt-on-error GY1974_test.tex
    bibtex GY1974_test
    xelatex -interaction=nonstopmode -halt-on-error GY1974_test.tex
    xelatex -interaction=nonstopmode -halt-on-error GY1974_test.tex

The supplied renderer and style are retained. Supporting generation scripts
and input parts preserve the editorial assembly; the seven prescribed files
are the authoritative editable data. Third-party article PDFs are not
redistributed; their bibliography links point to the sources.

## 6. What the classification and format miss

A–F compresses independent facts. This year needs separate fields for an old
theorem, false copied formula, corrected reconstruction, unresolved reading
and later thematic realization. The most useful schema additions would be:

- **Source-event identity and aliases:** canonical ID, source date, catalogue
  date, date confidence and exact-duplicate relationship.
- **Evidence location:** a page region or paragraph anchor distinct from the
  catalogue's broad page envelope.
- **Typed relationships:** same source occurrence, repeats, uses, special case,
  related but not equivalent, and corrected by.
- **Claim-level chronology:** received, first circulated and published dates,
  each with evidence and precision.
- **Verification locator:** result and page, access route, and original proof
  versus later restatement versus metadata.
- **Conventions:** Fourier, Poisson and curvature signs and measure normalizations
  when a comparison depends on them.

These are proposals, not silent changes to the seven-file schema. A later
revision should distinguish an unidentifiable intended theorem from a known
false literal claim with several possible repairs. It should also allow
uncertain historical A/E chronology without implying mathematical uncertainty.

## 7. Website presentation

A reader entering a talk should first see its actual source span, any provenance
warning, a short outline and the item list. Each item should offer separately
labelled notebook, precise-statement and reconstruction panels. Fate and
present status should follow, with visible correctness, publication-match,
verification and confidence fields.

The opening 331/332 entries need prominent links to their canonical earlier
occurrences; otherwise a year comparison would count them as new activity.
Wide page envelopes must not create false attribution. Segal's October lecture
should open P000575–P000578 first; Polyakov's heading/content date mismatch needs
a visible warning.

The finite-gap sequence should be traversable across 336, 339, 340 and 343,
with links from the Hamiltonian and entire-function items to their audits.
The two Newton questions should appear together with their different inequality
directions. Current-group existence should link to the 1969 questions as related
material without marking a broader prior classification problem solved.
The categorical lectures should link to 1973-308/309 and the earlier building.
Each correction should link backward to its scan and forward to its evidence.

Search should include original and reconstructed formulas, speaker aliases,
canonical problem IDs and multiple subject tags. “Open problems” should filter
precise questions by status, rather than collect every notebook question mark
or F item. Faithful mathematical errors must remain distinguishable from
transcription and translation mistakes.

## 8. Source-boundary audit and detailed research notes

The supplied page range begins within the preceding year's material. The
following research notes preserve the attribution audit, exact locators and
unresolved limits. They supplement the occurrence data and do not add hidden
items to its counts.

| Earlier item | Source page | Audited content | Class |
|---|---|---|:---:|
| 1973-330.6 | P000550 | Polynomial-exponential solutions and Bargmann potentials | E |
| 1973-330.7 | P000550 | The interpolation problem and its missing normalization | F |
| 1973-330.8 | P000550 | The polynomial Wronskian and the absent leading factor | E |
| 1973-330.9 | P000550 | Cubic time evolution of the interpolation data | E |
| 1973-330.10 | P000550 | The incomplete third-order auxiliary equation | F |
| 1973-330.11 | P000550 | Logarithmic derivatives, the spectral shift and the Miura sign | E |
| 1973-333.1 | P000552 | The sign of the Laplace--Beltrami operator | E |
| 1973-333.2 | P000552 | Heat-kernel expansion and trace | E |
| 1973-333.3 | P000552 | The small-time heat-trace expansion | E |
| 1973-333.4 | P000552 | Curvature contractions | E |
| 1973-333.5 | P000552 | The integrated scalar-curvature coefficient | E |
| 1973-333.6 | P000552 | The quadratic integrated heat coefficient | E |
| 1973-333.7 | P000552 | The missing off-diagonal Gaussian | E |
| 1973-333.8 | P000552 | Sakai and the fourth heat coefficient | E |
| 1973-333.9 | P000552 | Koblenz’s claimed independent fourth-coefficient computation | F |
| 1973-333.10 | P000552 | The lattice-point and Riemann-zero analogy | F |
| 1973-333.11 | P000552-P000553 | Closed billiard paths and oscillatory spectral density | E |
| 1973-333.12 | P000552 | Cauchy smoothing and convergence | E |
| 1973-333.13 | P000553 | The heat trace is not the displayed oscillatory trace | E |
| 1973-333.14 | P000553 | The unspecified general spectral-gap question | F |
| 1973-333.15 | P000553 | Exact spectral doublets on the circle | E |
| 1973-333.16 | P000553 | Shnirelman’s all-index close-neighbor theorem | B |
| 1973-333.17 | P000553 | The tentative three-torus comparison | F |
| 1973-333.18 | P000553 | Half-wave propagation and its trace | E |
| 1973-333.19 | P000553 | Unit-speed singularity propagation and caustics | E |
| 1973-333.20 | P000553 | Closed-geodesic contributions to a wave trace | E |

The complete boundary statements, modern qualifications and source locators
are printed in the verification appendix and preserved in
[early_boundary.json](code/generation/parts/early_boundary.json).
These are checks of existing prior identifiers. They are excluded from the
265 current-package item rows and from the ten problem entries.

The detailed research records are:

- [Early lectures and boundary pages](code/generation/parts/early_research.md):
  records 331–341, source chronology, regularity and finite-gap checks.
- [Middle lectures](code/generation/parts/middle_research.md):
  records 342–347 and 349–351, configurations, Newton data, gauge measures
  and current groups.
- [Segal's classifying-space lecture](code/generation/parts/extra_research.md):
  record 348, nerve conventions, the building proof and reduced homology.
- [Entire-function compatibility audit](code/generation/parts/root_research.md):
  exact local conditions and the limits of later inverse-spectral matches.
- [Later lectures](code/generation/parts/late_research.md):
  records 352–361, microlocal normal forms, Gibbs measures, divisors and curvature.

The consolidated bibliography has one entry per key. All contributing
verification annotations, including those attached to duplicate keys, remain
available in bibliography_verification.json. This preserves differences in
which sections were read without creating duplicate works.

## 9. Final build and validation

The final standalone PDF contains **143 pages**. The overview occupies pages
1–2. All 30 catalogue records and all 265 occurrence identifiers are present;
the problem index contains ten entries, including two reused earlier-year
problem identifiers. The 26 boundary-audit rows remain separate from the
current-year occurrence count.

The supplied builder completed successfully. XeLaTeX and BibTeX completed the
required sequence, followed by two passes after the final layout repairs.
The final log has **no TeX errors, undefined citations or references, missing
glyphs, font warnings, overfull boxes, or pending rerun warning**. BibTeX reports
no warnings or errors. The remaining underfull-paragraph diagnostics concern
ordinary spacing in justified text; the inspected pages show no clipped text
or obscured formulas.

The visual review checked pages 1, 2, 60, 107, 110, 123 and 138, covering the
two-page overview, occurrence entries, exact computations, a proof, the problem
index/correction transition, and the bibliography. The packaged four-face
DejaVu Serif family renders the Russian alphabet, including Ё/ё. The renderer
and style are byte-identical to the supplied kit; presentation repairs are
recorded in the source data and the explicit assembly layout file.

The structural validation checks record coverage and order, consecutive unique
item identifiers, reciprocal problem links, earlier occurrence identifiers
against the supplied index, bibliography keys, rendered citations, correction
types, and PDF text coverage. Its machine-readable results and hashes are in
validation.json. Independent regeneration from the packaged snapshots is
recorded in code/reproduction_check.json; the mathematical reruns match their
saved outputs. The mathematical proofs were additionally checked independently
as described in the verification appendix and research logs. Structural and
build checks do not replace that mathematical or historical judgment.


## References cited in this report

The selective list below covers the 21 works cited in this report. De Filippis, Mingione, and Nowak's 2026 revision supplies the later restatement used in the regularity discussion. The complete **78-entry bibliography**, including verification scopes, result locators, and distinctions between metadata and full-text checks, is in **GY1974_references.bib**. Entries below use only the metadata recorded there; dates identify the cited publication or preprint version, not necessarily the first circulation of its results.

De Filippis, C., Mingione, G., & Nowak, S. (2026). *Partial regularity in nonlocal systems I* [Preprint, revised July 8, 2026]. arXiv. [https://arxiv.org/abs/2501.08405](https://arxiv.org/abs/2501.08405)

Dobrushin, R. L. (1968). The description of a random field by means of conditional probabilities and conditions of its regularity. *Theory of Probability and Its Applications, 13*(2), 197–224. [https://doi.org/10.1137/1113026](https://doi.org/10.1137/1113026)

Dubrovin, B. A., Matveev, V. B., & Novikov, S. P. (1976). Non-linear equations of Korteweg–de Vries type, finite-zone linear operators, and Abelian varieties. *Russian Mathematical Surveys, 31*(1), 59–146. [https://doi.org/10.1070/RM1976v031n01ABEH001446](https://doi.org/10.1070/RM1976v031n01ABEH001446)

Dubrovin, B. A., & Novikov, S. P. (1974). A periodicity problem for the Korteweg–de Vries and Sturm–Liouville equations. Their connection with algebraic geometry. *Doklady Akademii Nauk SSSR, 219*(3), 531–534. [https://people.sissa.it/~dubrovin/Papers/1974/dubrovin_novikov_1974_dan.pdf](https://people.sissa.it/~dubrovin/Papers/1974/dubrovin_novikov_1974_dan.pdf)

Duistermaat, J. J., & Hörmander, L. (1972). Fourier integral operators. II. *Acta Mathematica, 128*, 183–269. [https://doi.org/10.1007/BF02392165](https://doi.org/10.1007/BF02392165)

Gesztesy, F. (1999). *Integrable systems in the infinite genus limit* (arXiv:solv-int/9907009v1) [Preprint]. arXiv. [https://doi.org/10.48550/arXiv.solv-int/9907009](https://doi.org/10.48550/arXiv.solv-int/9907009)

Griffiths, P. A. (1971). Holomorphic mappings into canonical algebraic varieties. *Annals of Mathematics, 93*(3), 439–458. [https://publications.ias.edu/sites/default/files/holomorphicmapping71.pdf](https://publications.ias.edu/sites/default/files/holomorphicmapping71.pdf)

Griffiths, P. A., & King, J. (1973). Nevanlinna theory and holomorphic mappings between algebraic varieties. *Acta Mathematica, 130*, 145–220. [https://publications.ias.edu/sites/default/files/nevanlinna.pdf](https://publications.ias.edu/sites/default/files/nevanlinna.pdf)

Hörmander, L. (1971). Fourier integral operators. I. *Acta Mathematica, 127*, 79–183. [https://doi.org/10.1007/BF02392052](https://doi.org/10.1007/BF02392052)

Kallel, S. (1998). *Spaces of particles on manifolds and generalized Poincaré dualities* (arXiv:math/9810067v1) [Preprint]. arXiv. [https://arxiv.org/pdf/math/9810067](https://arxiv.org/pdf/math/9810067)

Kushnirenko, A. G. (1975). Newton polyhedron and Milnor numbers. *Functional Analysis and Its Applications, 9*(1), 71–72. [https://doi.org/10.1007/BF01078188](https://doi.org/10.1007/BF01078188)

Marchenko, V. A., & Ostrovskii, I. V. (1975). A characterization of the spectrum of Hill's operator. *Mathematics of the USSR-Sbornik, 26*(4), 493–554. [https://doi.org/10.1070/SM1975v026n04ABEH002493](https://doi.org/10.1070/SM1975v026n04ABEH002493)

McDuff, D. (1975). Configuration spaces of positive and negative particles. *Topology, 14*(1), 91–107. [https://doi.org/10.1016/0040-9383(75)90038-5](https://doi.org/10.1016/0040-9383(75)90038-5)

Mingione, G. (2006). Regularity of minima: An invitation to the dark side of the calculus of variations. *Applications of Mathematics, 51*(4), 355–426. [https://doi.org/10.1007/s10778-006-0110-3](https://doi.org/10.1007/s10778-006-0110-3)

Novikov, S. P. (1974). The periodic problem for the Korteweg–de Vries equation. *Functional Analysis and Its Applications, 8*(3), 236–246. [https://doi.org/10.1007/BF01075697](https://doi.org/10.1007/BF01075697)

Pirogov, S. A., & Sinai, Ya. G. (1975). Phase diagrams of classical lattice systems. *Theoretical and Mathematical Physics, 25*(3), 1185–1192. [https://doi.org/10.1007/BF01040127](https://doi.org/10.1007/BF01040127)

Pirogov, S. A., & Sinai, Ya. G. (1976). Phase diagrams of classical lattice systems: Continuation. *Theoretical and Mathematical Physics, 26*(1), 39–49. [https://doi.org/10.1007/BF01038255](https://doi.org/10.1007/BF01038255)

Quillen, D. (1973). Higher algebraic K-theory: I. In *Algebraic K-theory I: Higher K-theories* (Lecture Notes in Mathematics, Vol. 341, pp. 85–147). Springer. [https://doi.org/10.1007/BFb0067053](https://doi.org/10.1007/BFb0067053)

Quillen, D. (1978). Homotopy properties of the poset of nontrivial p-subgroups of a group. *Advances in Mathematics, 28*(2), 101–128. [https://doi.org/10.1016/0001-8708(78)90058-0](https://doi.org/10.1016/0001-8708(78)90058-0)

Segal, G. (1968). Classifying spaces and spectral sequences. *Publications Mathématiques de l'IHÉS, 34*, 105–112. [https://doi.org/10.1007/BF02684591](https://doi.org/10.1007/BF02684591)

Wilson, K. G. (1974). Confinement of quarks. *Physical Review D, 10*(8), 2445–2459. [https://doi.org/10.1103/PhysRevD.10.2445](https://doi.org/10.1103/PhysRevD.10.2445)

### Version and identification notes

De Filippis, Mingione, and Nowak's manuscript was first posted on January 14, 2025; the bibliography cites its July 8, 2026 revision. It is used only for the explicitly delimited restatement of classical local partial regularity, not as that result's first proof. Kallel's cited arXiv version was posted on October 11, 1998; its first page records an earlier September 1996 circulation. Gesztesy is cited in the verified 1999 preprint version, without substituting an unchecked later journal edition.

The report's Dubrovin–Novikov (1974) citation refers to the **Doklady announcement received on June 3, 1974**, as specified in the report's chronology. It does not refer to the separate JETP paper with a different title and submission date. Dobrushin (1968) refers here to the conditional-distribution paper whose existence and uniqueness theorems were read; the separate 1968 uniqueness paper remains in the complete bibliography but is not needed to disambiguate this report's citation.

The supplied metadata for Quillen's 1973 chapter does not name the volume's editors; none have been inferred. McDuff's 1975 metadata was verified, while the signed-particle target was checked indirectly through Kallel (1998); the complete bibliography preserves that verification distinction.


