# GY1974: critical companion to the 1974–75 seminar records

**Status date: November 2026.** The chapter covers all 30 requested catalogue
records and audits the adjoining earlier-year material included in the supplied
page range. It contains **__N__ mathematical occurrences**, **__P__ definite
problem entries**, **__R__ bibliography entries**, and **__K__ critical corrections
or qualifications**. The seven prescribed data/text files, this report, the
generated chapter, the XeLaTeX PDF, the supplied renderer and style, and
reproducible verification code are included.

## 1. Counts and their interpretation

An occurrence is a distinct mathematical act in the notes: a definition,
construction, theorem, claim, method, question or substantive remark. Repeated
explanations in different meetings receive separate identifiers. A rhetorical
prompt does not automatically become an open problem. Headings without
mathematics remain register entries and contribute zero items.

__CLASS_TABLE__

A means published soon after by the speaker or Gelfand; B means subsequently
developed by others; E means known before the talk; F means the intended claim
cannot be identified sufficiently. C and D are reserved for precise unresolved
remainders or genuinely undeveloped claims. There are no C/D selections here.
This is a bounded conclusion about these pages and the evidence found.

Five entries, 1974-331.1–4 and 1974-332.1, are compatibility aliases for previously
indexed March 1974 source occurrences. The raw count is __N__; removing these
five exact source duplicates leaves **__U__**. This is not a count of unique
theorems: exposition repeated on different pages remains a distinct occurrence.
The adjoining boundary audit does not inflate either count.

### By record owner

__SPEAKER_TABLE__

This table uses the primary catalogue speaker even where an intervention is
attributed to someone else or the register label adds an attribution caveat.
The accompanying audit_counts.json also supplies counts using
explicit item-level speaker overrides, every record's count, and the zero-item
headings. Standardized names are used; material catalogue variants are noted.

### By primary area

__AREA_TABLE__

These are exclusive groups assigned by the record's principal topic. Algebraic
geometry within finite-gap lectures is counted with integrable systems; the
Bernstein intervention is counted within the microlocal sequence. This prevents
double counting. Multiple subject tags would be useful for a website, but are
not a field in the prescribed schema.

### Assessment dimensions

__CORRECTNESS_TABLE__

__MATCH_TABLE__

__VERIFICATION_TABLE__

__CORRECTION_TABLE__

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

__BOUNDARY_TABLE__

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

__FINAL_VALIDATION__

__REPORT_REFERENCES__

