# Research and inspection log: GY1975, records 375–385

Status date: 10 November 2026. Academic-year identifier: **1975**, including the talks delivered in calendar year 1976.

## Scope and deliverables

This block contains eleven catalogue records, 375–385, with 78 occurrence items. Record 378 is the calendar-year heading and has no independent mathematical item. The record catalogue ranges are retained, but individual mathematical occurrences use their actual manuscript pages. `b_author.py` checkpoints the JSON and correction CSV after every added talk, item, correction and problem; its final editorial section applies the reviewed refinements. The final snapshot is in `b_talks.json`, `b_items.json`, `b_problems.json`, and `b_corrections.csv`.

The bibliography contains all 23 keys cited by this block. Four entries are reused verbatim from `references_cumulative.bib`: `bernstein1972continuation`, `dubrovinmatveevnovikov1976nonlinear`, `gelfandkirillov1966corps`, and `wilson1974confinement`. The shared Krichever key is `krichever1976zakharov`. The source ledger records the difference between a full result read, abstract-level result read, publisher metadata check, indirect historical attribution, and unresolved lead. A note of `verified` in BibTeX means that the cited resource was opened, not that every theorem in it was read.

## Record boundaries and attribution

| Catalogue record | Actual mathematical span in this block | Boundary decision |
|---|---|---|
| 375, Dubrovin, 27 October 1975 | P000625–P000626 | P000623–P000624 continue Krichever's preceding talk and belong to the preceding block. |
| 376, I. M. Gelfand, 10 November 1975 | P000627–top of P000628 | The polynomial functional equation occurs before Polyakov's heading. |
| 377, Polyakov, 10 November 1975 | P000628–P000630 | Ends before the calendar-year transition and the February heading. |
| 378, heading | No independent item | Calendar-year marker only; no mathematical content is duplicated from overlapping catalogue links. |
| 379, Krichever, 9 February 1976 | P000631–first lines of P000633 | The proof's final two lines precede the separate Drinfeld heading. |
| 380, Drinfeld, 9 February 1976 | P000633–P000634 | Includes Gelfand's reciprocity and division-ring interventions. |
| 381, Novikov, 23 February 1976 | P000635 | Novikov reports Brodskii's work; Fuchs's characteristic-cycle intervention is separately identified. Losik starts at the foot of the page. |
| 382, Losik, 23 February 1976 | P000635–P000637 | Includes Gabrielov's bundle correction; ends before the 1 March heading. |
| 383, catalogue Novikov, 1 March 1976 | P000638–P000641 | Manuscript explicitly says **Drinfeld (Volodya)**. Preserve the catalogue metadata and record the provenance discrepancy; use manuscript attribution at item level. |
| 384, S. I. Gelfand, 1 March 1976 | P000639–P000640 | Only the foot-of-P000639 explanation says “S. Gelf.” P000640 says merely “G.”, so the full-name attribution there remains uncertain. Drinfeld's module/sheaf material remains in 383. |
| 385, Drinfeld, 15 March 1976 | P000642–upper P000644 | The final Abel-map tangent paragraph precedes a divider and the heading **A. Polyakov**. The latter begins record 386, handled by the next block. |

These decisions were communicated to the adjoining agents. The later Hamiltonian confinement discussion in record 386 reuses **GP-1975-10**. The later higher-rank inverse question uses **GP-1975-26** in the adjoining block and is not merged with this block's rank-one question **GP-1975-14**.

## Scan inspection log

All of P000625–P000644 were visually inspected using the supplied PNG scans. P000623–P000624 are boundary context owned by the previous block; P000645 is already inside Polyakov's following talk. The following are observations from the images, rather than deductions from OCR alone.

| Scan | Inspected features | Editorial consequence |
|---|---|---|
| P000625 | Dubrovin heading, spectral pencil, formal resolvent, first stationary commutator and bottom lemma | The initial sign is `Lambda'=[Lambda,Q]`; the lemma reverses it. The reversal is a faithful notebook error. |
| P000626 | Lax proof, spectral determinant, Bloch remark, Jacobian/torsor assertion | The proof repeats the reversed commutator. The phase space/Poisson bracket is not supplied; 375.7 is only a partial identification. |
| P000627 | Ant/cube and developed-curve drawings; torsion/curvature labels; lattice-relativity request and curriculum | No definite torsionful connection is specified. The diagrams motivate a programme rather than a theorem for arbitrary polyhedra. |
| P000628 | End of curriculum and Bernstein formula; Polyakov heading; tensor products; spin labels; color table; negative invariance phrase | The Lagrangian “cannot be invariant” wording is visible and is retained as an ambiguity, not silently negated or erased. |
| P000629 | Meson singlet, heavy-source diagrams, color Lagrangian, Wilson rectangle and ordered product | The middle singlet term has two bars. The action explicitly has `d^4x`, so the notes do provide four-dimensional motivation. Path ordering is explicit in the product. The phase line has `+ET`. |
| P000630 | Reversed antiparticle worldline, `exp(-iET)`, area claim, Gaussian formula and commutator term | The phase sign conflicts with the preceding `exp(iW), W=+ET`. A worldline representation does not itself prove an area law. |
| P000631 | Dated February heading; wave recursion, normalization bound, phase and school exercise | The normalization really says `i>1`, leaving the first integration function free. The next operator coefficient is allowed constant, but its phase term is absent. |
| P000632 | Algebraic-operator definition, quasianalyticity remark, Baker–Akhiezer normalization, elliptic example | The asymptotic is small `o(1/k)`, inconsistent with an allowed first correction; correct to `O(1/k)`. Divisor/nonspeciality hypotheses are omitted. |
| P000633 | End of Krichever proof and Drinfeld heading; Shabat attribution; reciprocity and extension remarks | Distinct interventions are not merged. The smooth-curve universal claim is literally too broad; the exact Shabat theorem remains unidentified. |
| P000634 | Filtered module, graded maps and sheaf transition | Correct quotient indices and the lower bound `i>=0` support the later correction on P000640. |
| P000635 | Novikov/Brodskii report, malformed radial equation, turning-point integral and inverse exponential; Fuchs drawings; Losik heading | The radial equation has a duplicated eigenvalue/sign conflict. The action lacks `1/pi`; the inverse integral lacks its lower endpoint. Fuchs's intervention precedes Losik. |
| P000636 | Frame-bundle diagram, connection form and affine fibers | Right-action/adjoint convention is retained. No torsion-free hypothesis is inserted. |
| P000637 | Quotient bundle, canonical connection, crossed-out and final model bundles | The source names `P` as the principal-bundle base; the correct base is the quotient. Gabrielov's final endomorphism-bundle expression supersedes the fixed Lie-algebra factor. |
| P000638 | Date `1/III-76`, Drinfeld (Volodya) heading, elliptic/genus-zero illustrations, gap formula | Confirms catalogue/manuscript speaker discrepancy. The literal `x=wp,y=wp'` normalization is wrong for the displayed cubic. |
| P000639 | Ordinary-point generator orders; leading coefficient; coordinate-independence assertion; gauge formula; S. Gelfand intervention | The list has `g+1` orders, although the prose says `g` generators. Independence of the local parameter is explicitly asserted and is false. The symmetric gauge equivalence does not require a sign correction. |
| P000640 | Initial “G.”, analytic Jacobian sketch, straight-line motion, filtration and generator proof | “G.” alone does not identify which Gelfand. The first quotient is visibly `M_i/M_(i+1)` despite an increasing filtration; later displays fix the intended denominator. |
| P000641 | Acyclic line bundle, pole filtration, exact sequence and two-chart gluing formula | Confirms the shift `M_i=H^0(L((i+1)P))` and numerator bound `M_(k deg(a_0)-1)`. Entire page belongs to the continued Drinfeld discussion. |
| P000642 | 15 March heading, rank-one recap, exhaustive filtration, higher-powers remark, gap formula | Gelfand's powers assertion is a separate mathematical item. The opening `A in H^0` symbol is recorded as an ambiguity corrected to equality. |
| P000643 | Relative line bundle, simple-pole operator, reciprocal `1/(b_0 z)`, value-at-zero argument, Picard tangent and boundary map | The reciprocal coefficient is genuine. General `B` must be specialized to germs for evaluation at zero. `H^1(O*)` needs its degree-zero component to mean the Jacobian. |
| P000644 | Velocity `ell'=eta_P/b_0`, Abel-map tangent paragraph, divider, Polyakov heading | The exact boundary is before Polyakov's heading. The tangent-image line needs genus at least one; in genus zero the Jacobian is zero. |

The corrections CSV distinguishes transcription/translation issues, ambiguities, provenance differences and **faithful mathematical errors**. None of the checked commutator, singlet, radial-normalization or Picard corrections is presented as an OCR repair merely because the original equation is wrong.

## Literature decisions and chronology

### Matrix finite-gap hierarchy

The 1976 Dubrovin–Matveev–Novikov survey and Dubrovin's 1977 matrix paper were opened and their relevant sections read. The received dates, respectively 2 June 1975 and 7 December 1976, are labelled as receipt dates. They do not establish pre-talk public circulation. The 1977 paper's translation copyright is 1978, but its journal volume is 1977.

The source gives an algebraic quotient written `M_Gamma/pi=J(Gamma)`. The companion's discussion of regular spectral data and an open nonsingular-potential chart is explicitly a modern restriction, not a quotation of different source hypotheses. The bare Lax equation proves constancy of spectral invariants. Because the notebook provides no Poisson bracket, leaf or independence conditions, its stronger Hamiltonian-integrability claim is marked **partial identification** rather than reconstructed as a theorem on an unspecified Hamiltonian structure.

### Geometry and gauge theory

A final self-review separated the classical symmetry/current assertion from the unidentified electrical-engineering metaphor on P000629. The former is indexed as 377.9 beside the electrical-engineering remark; subsequent record-377 items are renumbered in source order. Noether (1918) was opened in its primary English translation; Section 1, Theorems I–II were read. The translation appeared in 1971; the 2005 repository deposit and 2018 revision are later access events. Thus this is E, while 377.8 remains F for the unspecified programme.

Regge's 1961 publisher abstract supplies a documented pre-talk polyhedral-relativity comparison; its full proof was not read. The 1972 Halperin–Toledo theorem and García's 1972 universal-connection theorem were read in primary full text. These establish the E classification of the corresponding precise statements, while the broad programme for arbitrary polyhedra remains insufficiently specified.

Wilson's 1974 primary paper was read at the loop, screening, lattice and leading strong-coupling arguments. The fixed-lattice mechanism precedes the November 1975 talk. It does not prove the four-dimensional continuum assertion. The notebook already writes `d^4x`; the reconstruction supplies the **pure gauge**, zero-temperature, infinite-volume, renormalization and external-representation restrictions. Massive external probes do not by themselves remove dynamical light-quark screening. The current Clay page and Jaffe–Witten problem description were opened, with existence/mass gap kept separate from confinement.

The Jaffe–Witten standalone PDF is undated. Its bibliography year is therefore `n.d.` rather than presenting the Millennium announcement date as a verified circulation date of that version. The key retains `2000` as a stable mnemonic. The official book contents also confirm the contribution's page range 129–152.

### Krichever and Drinfeld

Krichever's 1976 original was read at the Baker–Akhiezer conditions, theorem and zero-curvature corollary. It was received 8 October 1975 and presented to the Academy 24 October 1975, but neither datum alone proves circulation before the relevant seminar. Drinfeld's entire 1977 four-page original was read, particularly Propositions 1–2 and Corollary 2; its receipt date is 14 April 1976. It explicitly credits Krichever and the Gelfand seminar.

The correspondence requires a generic/acyclic degree-`g-1` line bundle and a unit principal-part or leading-coefficient germ. A point on the whole Jacobian, without that second datum or the acyclicity condition, is insufficient. The higher-rank inverse problem occurring later in the notebook is a separately quantified question, not a recurrence of the rank-one problem here.

The opened Krichever 1977 survey recalls seminar reports in November–December 1975, while the preceding notebook block has a 20 October heading. This is a provenance discrepancy, not a reason to overwrite the notebook date; the preceding agent handles that survey reference.

For the order-two/order-three example and formal powers, Mulase's author-hosted primary article was read at its explicit formulas. Its reference to Wallenberg 1903 and Schur 1905 is an **indirect historical attribution**: the original papers were not opened. The displayed modern calculation was independently checked below. The item is E because it is an explicitly classical example, with the historical verification limit stated.

Forster is cited only as a later textbook reference to classical curve theory. The publisher page and author's contents were opened; repeated attempts to open the full CNRS-hosted PDF returned 502. The item verification field therefore says **publisher metadata checked**, never “read the result.” These exposition dates are not treated as dates of discovery of Riemann–Roch, Abel–Jacobi or the gap theorem.

### Brodskii and the radial inverse problem

The named author is **M. A. Brodskii**, not the seminar reporter S. P. Novikov. The exact match is the two-page 1976 UMN note, pp.253–254, received 18 June 1975. Its radial scalar equation, endpoint conditions, high-frequency sampling theorem and Abel inversion were read. The notebook's “elastic sphere” phrase is narrowed to this scalar model; recovering one coefficient of this equation is not recovery of every elastic parameter of a general solid.

The B label records the author/reporter difference. It does **not** claim that Brodskii later developed an idea first posed by Novikov. There is an additional chronology caveat: Levshin's own 2004 retrospective, opened in this research, lists a 1975 Computational Seismology 8 paper, pp.162–168, on the inverse problem of torsional oscillations. That 1975 primary text was not recovered. Its exact overlap with the scalar UMN theorem remains unverified; the companion consequently does not claim to have established the earliest public version. This is explicitly reflected in 381.1–2 and the source ledger.

The inversion kernel itself is classical. The modern Paternain–Salo–Uhlmann presentation was read at Theorems 2.2.1 and 2.2.3 and the historical remark. Travel-time inversion is distinguished from Brodskii's spectral sampling. The UMN corollary is a **necessary** compatibility condition, not a necessary-and-sufficient description of all exact doubly indexed spectra. The notebook lacks the extra specifications needed to isolate a precise residual range conjecture. No artificial C problem is created from those omissions.

## Bounded calculations supplied in this task

The following are labelled `\ours` or `\oursComputed` in the relevant item reconstructions. They check classical formulas or explain an emendation; none is asserted to be an original research result. `code/b_checks.py` reproduces the symbolic and numerical parts and writes `computations/b_checks_output.json` relative to the package root, independent of the invocation directory.

### 1. Abel normalization and its lower endpoint (`\oursComputed`)

Assume `f>0`, `q(r)=r f(r)` smooth, `q(0)=0`, `q(1)=1`, and `q'>0`. Let `psi=q^{-1}` and define the normalized action

\[
m(\tau)=\frac1\pi\int_{\psi(\tau)}^1
 \sqrt{\tau^{-2}f(r)^2-r^{-2}}\,dr,
\qquad M(\tau)=\tau m(\tau),\quad 0<\tau<1.
\]

Changing variables `s=q(r)` gives

\[
M(\tau)=\frac1\pi\int_\tau^1
 \sqrt{s^2-\tau^2}\,a(s)\,ds,
\qquad a(s)=\frac{d}{ds}\log\psi(s).
\]

Differentiation is valid on each compact interior interval and yields

\[
M'(\tau)=-\frac{\tau}{\pi}\int_\tau^1
 \frac{a(s)}{\sqrt{s^2-\tau^2}}\,ds.
\]

For fixed `eta>0`, all integrals below are absolutely integrable. Reverse their order and substitute
`tau^2=eta^2+(s^2-eta^2)u` in the inner integral:

\[
\int_\eta^s\frac{\tau\,d\tau}
 {\sqrt{s^2-\tau^2}\sqrt{\tau^2-\eta^2}}
 =\frac12\int_0^1\frac{du}{\sqrt{u(1-u)}}=\frac\pi2.
\]

Consequently,

\[
2\int_\eta^1\frac{M'(\tau)}{\sqrt{\tau^2-\eta^2}}\,d\tau
=-\int_\eta^1 a(s)\,ds
=\log\psi(\eta),
\]

because `psi(1)=1`. This proves the lower endpoint `eta` and the coefficient 2 **for the action containing `1/pi`**. If the notebook's unnormalized action is retained, the coefficient must be `2/pi`.

For the independent constant-profile check, take `f=1`, hence `psi(eta)=eta`:

\[
M(\tau)=\frac{\sqrt{1-\tau^2}-\tau\arccos\tau}{\pi},
\qquad M'(\tau)=-\frac{\arccos\tau}{\pi}.
\]

Numerical quadrature after the endpoint-regularizing substitution
`tau^2=eta^2+(1-eta^2)sin^2(theta)` reproduces `log(eta)` at
`eta=0.1,0.3,0.7,0.95` with absolute error below `4e-61` at 60-digit working precision. This numerical agreement is a check; the kernel composition is the proof. Keeping both the notebook's unnormalized action and coefficient 2 would instead produce `eta^pi`, already wrong for this constant profile.

### 2. The commuting school exercise (`\oursComputed`)

For `L=-D^2+u`, `M=D^3+vD+w`, the three possibly nonzero coefficients in `[L,M]` are

\[
[D^2]:-2v'-3u',\qquad
[D]:-v''-2w'-3u'',\qquad
[1]:-w''-u'''-vu'.
\]

They give `v=-3u/2+c1`, `w=-3u'/4+c2` and

\[
u'''-6uu'+4c_1u'=0.
\]

Integrating once, multiplying by `2u'`, and integrating again gives

\[
(u')^2=2u^3-4c_1u^2+2c_3u+c_4.
\]

This includes singular cubic degenerations. The check script uses the noncommutative Leibniz multiplication rule, not ordinary polynomial multiplication in `D`, and verifies all three coefficients symbolically. The exercise gets GP-1975-12; the broader older finite-gap/stationary-KdV problem GP-1974-10 is related but has different quantifiers.

### 3. The higher-powers example (`\oursComputed`)

Over `C(x)`, set

\[
P=D^2-2x^{-2},\qquad R=D^3-3x^{-2}D+3x^{-3}.
\]

Exact differential-operator multiplication verifies `[P,R]=0` and `R^2=P^3`. In the formal pseudodifferential ring let `Q=R P^{-1}`. Then `Q^2=P`, `Q^3=R`; all integers at least two belong to the additive semigroup generated by two and three, so every `Q^m`, `m>=2`, is differential. If `Q` were differential, order and leading coefficient force `Q=D+a`. The coefficient of `D` in `Q^2=P` forces `a=0`, contradicting its constant coefficient. This supplies a precise category and example for Gelfand's remark without asserting an unverified operator-domain statement on a Hilbert space.

### 4. The cusp obstruction (`\ours`)

The subring `C[D^2,D^3]` is isomorphic to `C[t^2,t^3]`. The element `t` lies in its fraction field and is integral over it, satisfying the monic equation `T^2-t^2=0`, but is absent from the subring: every nonconstant monomial there has degree at least two. Thus the ring is not integrally closed. A smooth affine complex curve has a normal coordinate ring, so this subring cannot be the function ring of a smooth affine curve. This disproves the notebook's unrestricted literal claim and does not identify or disprove an unknown more qualified Shabat theorem.

### 5. Additional short checks

The shift `x=1+w`, `y=w'/2` converts `(w')^2=4w^3-4w` into the displayed elliptic cubic. At an ordinary point, functions of orders `g+1,...,2g+1` generate by the leading-term induction supplied in 383.4, so there are `g+1` functions in that list. Rescaling `z` to `c z+O(z^2)` multiplies normalized leading coefficients by `c^{-k}`, hence `b` by `c^{-1}`. The stationary Lax commutator is `[D+Q,Lambda]=Lambda'+[Q,Lambda]`, fixing the notebook's sign. Finally, integrating `ell'=eta_P/b_0` gives the local Picard lift in 385.8; a global ordered divisor path is not thereby guaranteed.

## Open and unidentified items

Only 377.10 receives C: the precisely restricted four-dimensional continuum area-law/positive-string-tension problem. The chapter contribution is its scope, the distinction from fixed-lattice results and the source corrections; no toy computation is offered as a development of that open continuum problem.

There are no D items. Searches using both available engines did not identify a definite theorem behind the noncommutative electrical-engineering metaphor, the quasianalyticity analogy, or the unqualified Shabat attribution. The division-ring extension and reciprocity remarks lack their necessary objects and quantifiers. These remain F, not purported unresolved modern conjectures. The exact queries, useful results, unsuccessful access attempts and interpretation limits are in `b_sources.json`.

## Validation boundary

Local checks verify schema fields, consecutive occurrence numbering, complete reference-key resolution, permissible item kinds, dated statuses, and the bounded formulas above. The root agent performs the integrated chapter build, BibTeX, XeLaTeX and final package QA. This block does not modify another agent's fragments or the integrated final deliverables.
