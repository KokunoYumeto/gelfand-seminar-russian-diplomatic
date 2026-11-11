# Records 658–662: research and verification notes

Status date: **11 November 2026**. This is the audit for the five assigned records, not the report for the entire academic year. The Russian transcription is authoritative. The assigned JSON files preserve notebook wording, mathematical reconstruction, and publication fate in separate fields.

## Delivered fragments and counts

The data contain **5 talks, 73 items, 3 problem records, 21 bibliography entries, and 49 correction/qualification rows**. All 21 cited works have at least a successfully opened primary document, publisher record, or author/primary archive record. Their annotations distinguish a theorem actually read from metadata alone. The source ledger has 50 distinct endpoints, including failed attempts; repeated successful opens are coalesced under one endpoint.

| Record | Speaker | Actual source ownership | Items |
|---|---|---|---:|
| 658 | A. M. Vershik | P001229 through upper P001231 | 18 |
| 659 | B. L. Feigin | Mid-P001231 through P001235 | 14 |
| 660 | B. L. Feigin | P001236 through upper P001238 | 13 |
| 661 | A. V. Zelevinsky | Mid-P001238 through P001240 | 8 |
| 662 | B. L. Feigin | P001241 through P001244 | 20 |

The supplied catalogue ranges overlap adjacent headings and are not mathematical ownership boundaries. P001228 belongs to the preceding record; P001245 begins the next record. Each occurrence uses the narrowest source page or span supporting it. Whole-page talk bounds necessarily overlap when two headings share a page, and the summaries specify the boundary.

Class counts are **E 66, F 6, C 1**. There are no A, B, or D items in this block. This is an evidential conclusion, not a quota. The Monster connection was already explicit in 1984; its later major development does not turn the short 1985 intervention into a previously unstated exact moonshine conjecture. The normal-ordering intervention has a later Krichever–Novikov comparison, but its underlying geometry and desired algebra are not specified, so it is F rather than an invented precise C/D problem.

By actual voice, there are 17 Vershik items, 44 Feigin items, 8 Zelevinsky items, and 4 interventions by Gelfand. Literal assessments: 5 correct; 43 correct with missing hypotheses; 18 false as written; 7 not determinable. Development fields: 47 none, 25 annotated, 1 developed in this chapter. The assessment axes matter: an E item can faithfully record a mathematical error, while an F item can concern a broadly established phenomenon whose exact notebook instance is unidentified.

## Manuscript examination

The PNGs **GELFAND-P001229 through GELFAND-P001244** were visually inspected, including all pages on which the formulas below depend. The important confirmed source readings are:

- The Fano picture shows only six visible line triples. The named Fano matroid requires seven; the missing line is explained but not drawn into the source.
- The source really says weight **two** and writes `2v'` after `L_-1 v'=v`; the Virasoro convention makes the correct source weight zero.
- The source word on P001236 is **тахионов**. Replacing this by ghosts is a mathematical emendation of a faithful reading, not a transcription correction.
- The creation exponential on P001237 really lacks `1/n`; its product index really is `j>1`, not `j>i`.
- The Cartan inequality is written with no off-diagonal qualification.
- The Vandermonde expression on P001239 has no `1/n!`; the rho exponent and factorial really contain `m`, although the flag dimension is `n`.
- The divided-difference denominator on P001240 is `x_(i+1)-x_i`, with numerator `f-s_i f`. The final adjacent-transposition indices are misplaced in two formulas.
- The P001241 Sugawara formula has no factor one-half.
- The P001242 vertex expansion has positive powers `z^j`, while its mode shift is written `i+n`.
- The cocycle identity on P001243 is explicitly imposed for all alpha and beta, making the temporarily waived evenness impossible.

Our supplied counterchecks and calculations are tagged `\ours` and `\oursComputed` in the reconstruction fields; source-only reconstructions retain their separate status.

Most rows in `corrections.csv` are consequently `faithful_error` or `ambiguity`, rather than alterations of the Russian transcription. No unclear crossed-out material was used to manufacture a theorem.

## The one C problem and the exact scope of the development

**1985-658.10 / GP-1985-42** is the fixed-dimensional simplicial realization-space claim. The notebook qualification is *более или менее любой*, “more or less any,” topology. The item does not present this as an exact full universality theorem. Its homotopy formulation is explicitly editorial.

The literature distinctions are essential:

1. Mnëv's 1985 Russian announcement, received 2 July 1984, has a real-configuration theorem and a simplicial-polytope assertion with unrestricted dimension. Theorems 1–4 were read. It does not settle fixed-dimensional simplicial universality.
2. Richter-Gebert–Ziegler's Main Theorem reports 1994 work, received January 1995 and published October 1995, for **general four-polytopes**.
3. Adiprasito–Padrol Theorem 2 uses **neighborly simplicial polytopes of dimension 2n−4 on 2n vertices**. It is a variable-dimensional theorem. The introduction judges earlier arguments for the simplicial part incomplete and supplies the missing proof; an announcement is not a checked complete proof of that part.
4. Their Conjecture 4 requires **neighborly four-polytopes**, a stronger restriction than simpliciality alone. Its target is an **open primary basic semialgebraic set defined over the integers**, up to stable equivalence.
5. Their realization model consists of **homogeneous vector configurations realizing the cone over the polytope, modulo GL(d+1)**. The chapter's fixed affine-frame, history-compatible stacking space is defined separately. No equivalence of the normalization conventions is assumed without proof.
6. The same primary paper records disconnected simplicial four-polytope realization spaces and trivial stacked realization spaces. Its Theorem 3 gives a stronger ball result for particular sewing families; the chapter does not claim that theorem as a new result.

The completed `stacking_development.tex` proves a bounded statement: start with a fixed labelled rational simplex and a finite prescribed sequence of facet stackings. At each stage, the new vertex must be strictly beyond the selected facet and strictly beneath all others. The exact insertion region is open and convex. An explicit facet-barycenter plus short outward-normal section is continuous, and linear contraction in each fiber gives a strong deformation retraction. Induction contracts the **history-compatible** space. It is not asserted that every realization of the final combinatorial type admits this history.

The proof also shows that a nonempty simplicial realization space has rational points. Rationality is preserved by the usual rational stable equivalences and polyhedral stable projections. Thus the nonempty primary set `{t: t^2=2, t>0}`, which has no rational points, cannot be the arithmetic stable type of such a realization space. The open-set qualification is mathematically substantive; this arithmetic observation does not obstruct homotopy universality.

Root independently reviewed the section, strict-slack estimates, facet update, strong deformation retraction, induction and rational-point arguments. Root reported exact-rational checks of 14 insertion steps in dimensions 2, 3 and 4, including two four-dimensional histories, with independent enumeration of all candidate facets. Those computations belong to the root's integration files. The local proof contains an independently rederived unnormalized-gradient formula that matches the rational implementation.

### Status search and the 2026 lead

The status wording is intentionally bounded: **no resolution found in this search through November 2026**. The latest successfully opened source explicitly recording the constant-dimensional simplicial question as open is **Schaefer–Cardinal–Miltzow, 2024 version 1, entries CG68–CG69**. This is not a claim that every later publication was excluded.

On 11 November 2026, a fresh primary-search pass used:

- `simplicial 4-polytopes realization spaces universality conjecture 2025 2026`, with recency 730 days;
- `"2608.07233"`.

Search results `turn113academia8` and `turn113search1` returned **Thiago Holleben and Yirong Yang, “Polytopal Bier spheres and nonrealizable central symmetries,” arXiv:2608.07233**, reportedly submitted **7 August 2026**. The search abstract claims a new family of simplicial polytopes with noncontractible realization spaces via Smith theory. The exact URLs attempted were `https://arxiv.org/abs/2608.07233`, `https://arxiv.org/html/2608.07233v1`, and `https://arxiv.org/pdf/2608.07233`. All returned DisabledError (`turn115view0–2`). Accordingly **no theorem in that preprint has been verified or cited as support**, and its search abstract is not treated as fixed-dimensional-four universality. This lead is retained for a later source-access pass and does not affect the stacking proof.

The original Bokowski–Guedes de Oliveira 1990 isotopy PDF was also located, but its Portuguese archive returned 403. The already-known disconnected simplicial-four phenomenon is supported here through the successfully opened discussion in Adiprasito–Padrol, with that indirect provenance preserved.

## Other problems and unresolved identifications

**GP-1985-40** records the topology of real configuration realization spaces. General universality is established and was announced before this seminar. **GP-1985-41** records the fixed maximal-minor sign-class isotopy question. The general answer is negative. The asserted `n<=7` bound is supported indirectly by the stronger “fewer than nine elements” statement in Tsukamoto's introduction.

The exact **nineteen-column uniform rank-three counterexample** attributed to Mnëv was not located in the opened primary texts. Tsukamoto's thirteen-element examples have prescribed collinearities and must not be substituted for a nonzero-maximal-minor statement. That occurrence is F, even though the general negative answer is known. Searches followed Mnëv's 1985 announcement, later universality formulations, the small oriented-matroid literature through Tsukamoto, and the later simplicial isotopy papers.

The complex convexity/pi1 prompt, the tangent-space field-of-polytopes classification programme, and the question-marked four-dimensional-subspace fragment in R6 remain underspecified. Their plausible mathematical settings are marked as reconstructions. No new open problem is assigned to them.

For the five-point amplitude remark, the actual exponents and intended class of evaluation are missing. The companion provides a generic Euler double-integral evaluation in terms of 3F2, explicitly as an editorial model. It does not pretend that a special-function expression resolves a uniquely identified physical closed-form problem.

## String and vertex-operator verification

Frenkel's primary article is unusually close to the notebook sequence. It provides exact locators for the cocycle (1.2), finite root algebra (1.3), current bracket (1.4), Fock and vertex formulas (2.2–2.5), Theorems 2.1 and 2.2, Virasoro formulas (2.8–2.14), Wick Theorem 3.3 and following calculation, and the no-ghost argument in Theorem 4.1 and Lemmas 4.2–4.3. The article's copyright and standard bibliography say 1985; the OCR header says 1986. The conference was Chicago 1982. No exact first-circulation day or publication month is inferred from these facts.

The three most consequential distinctions are:

- The full vertex contains zero-mode powers. An oscillator-stripped series, a plane primary field, and a cylinder-normalized field are distinct. In particular, a norm-two screening is `Res Y dz`, equivalently `Res X dz/z` for `X=zY`; the bare shift-only formula cannot be inserted unchanged into that assertion.
- The physical constrained space is positive **semidefinite** at nonzero momentum; its quotient by null/spurious states is positive **definite**. Zero momentum is exceptional. DDF commutators contain the central value `(c,a0)` and the transverse Gram matrix until both are normalized. A single DDF vacuum generates its compatible momentum tower, not every momentum sector.
- Equal momentum norm is insufficient to identify zero and nonzero null Fock modules. On level one, L1 has rank zero at zero momentum and rank one at nonzero null momentum. This is a direct correction, not a speculative new representation-theoretic problem.

The original 1972 Goddard–Thorn and DDF publisher endpoints were inaccessible; their exact statements were checked through the opened primary Frenkel and Borcherds formulations instead. The ambiguous-initial Schwarz 1973 reading recommendation is plausibly John H. Schwarz, *Dual resonance theory*, Physics Reports 8,269–335, also cited by Frenkel. The further Green–Schwarz review is not uniquely identified from the notebook. These reading-list uncertainties are not converted into mathematical open problems.

Frenkel–Kac's publisher metadata was opened, but its issue month conflicts with its received/revised dates. Only the unambiguous year 1980 is used. The FLM 1984 PNAS publisher page was successfully opened after repeated PMC/PubMed failures: it identifies **Arne Meurman** and gives publication **15 May 1984**, plus an abstract announcing the graded Monster action and J-character. Borcherds 1992 Theorem 1.1 and sections 5–6 were read for the later proof and no-ghost application.

## Second checks of explicit editorial calculations

`check_formulas.py` is executable and saves `check_formulas_output.txt`. It ran successfully; the saved output records its final differential-operator refinement. The tests use exact SymPy 1.14.0 arithmetic.

| Check | Independent implementation | Result and scope |
|---|---|---|
| Top Schubert class | Groebner reduction modulo the elementary symmetric ideal, n=2,3,4 | Vandermonde equals n! times the top monomial; rho^N equals N! times it |
| Divided differences | Substitution definition, reduced longest-word recursion, braid and square-zero on a nontrivial polynomial | Correct denominator gives top-to-one; notebook denominator gives -1 at n=2 |
| Sugawara half | Polynomial oscillator model at the level-two vacuum, d=1,2,26 | Correct L2 L-2 vacuum is d/2; omitted halves give 2d |
| Vertex 1/n | Differential commutator with multiplication by an exponential, frequencies 1–6, test state u^3+u+1 | Correct factor is k z^n; missing denominator gives n k z^n |
| Laurent shift | 25 exact coefficient comparisons | Positive-exponent expansion gives X_(i-n), not X_(i+n) |
| Null momenta | Lorentzian 2-by-2 Gram calculation, embedded in the higher-dimensional argument | Same zero norm, but L1 ranks 0 and 1 |
| Euler model | Exact elementary double integration versus terminating 3F2 | Both give 11/18 at a=b=c=d=1,e=-2 |

These finite checks audit signs and constants. They are not claimed as proofs for all ranks, levels or parameter values. The general divided-difference and top-class identities are read in BGG/LS; the oscillator corrections follow directly from the algebraic commutators. The five-point formula follows independently by binomial expansion and beta integration under the stated convergence hypotheses. The E8 exercise is verified by the evenness calculation and the index/covolume calculation in the occurrence itself.

## Recurrence and presentation

The previous index was searched for exact matches. Related earlier entries include 1971-239.1–2, 1979-483.1, 1979-484.3, and 1982-575.1 for Schubert geometry; 1982-562.8 and 1982-566.9 for normal ordering and boson mode conventions. Existing GP-1982-03 concerns Virasoro Verma reducibility and singular vectors, and GP-1982-09 concerns the Liouville spectrum. Neither is the physical quotient/no-ghost question here. No earlier problem ID was reused without an exact statement match.

For a website, the natural first links are the actual source interval and the three evidentiary fields. Formula corrections should remain visible as faithful notebook errors, not replace the source transcription. Cross-links should connect the three Feigin lectures on the same zero-mode and no-ghost conventions; the repeated DDF constructions; Zelevinsky's top class, operator sign and recurrence; and the precise GP-1985-42 distinction between general4, variable-dimensional simplicial, and fixed4 claims. The separate literal-correctness and publication-match fields carry more information than the single A–F label.

## File and audit boundaries

The root agent integrates and compiles the chapter. This block writes only under `work/virasoro/`. The source ledger records endpoints rather than quoting their text. A few failed DOI attempts predate compaction and have no individual retained tool reference; their `ref` is blank and the failure is stated, rather than falsely assigning a neighbouring source ID. They are not used as verified bibliography entries.
