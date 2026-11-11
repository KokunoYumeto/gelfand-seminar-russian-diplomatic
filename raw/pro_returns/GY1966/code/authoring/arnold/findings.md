# Records 115–118: completed research handoff

Status date: **2026-11-09**. The actual subject is singularity theory, not hydrodynamics. The first two records are Arnold's 21 and 28 November 1966 lectures. Records 117–118 are a year heading and a future seminar plan.

## Deliverables and counts

The deliverables in this directory are `talks.json`, `items.json`, `problems.json`, `corrections.csv`, `references.bib`, and the deliberately empty `development.tex`. The reproducible authoring scripts and the exact computation script/output are also included.

| Record | Actual content pages | Items | A | B | C | D | E | F |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 115 | P000173–P000178 | 21 | 1 | 4 | 0 | 0 | 14 | 2 |
| 116 | P000179–P000186 | 25 | 1 | 13 | 0 | 0 | 11 | 0 |
| 117 | Catalogue P000186–P000188 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 118 | P000187, top | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | | **46** | **2** | **17** | **0** | **0** | **25** | **2** |

All 46 items belong to V. I. Arnold's talks and to differential topology/singularity theory. There is one recurring problem, **GP-1965-03**, with occurrences `1965-72.5` and `1966-115.8`. There are 27 correction/qualification rows: scan readings, translation corrections, faithful mathematical errors, unresolved ambiguities, and provenance distinctions are explicitly typed. The bibliography has ten entries, all opened and marked verified, with separate annotations specifying whether the mathematical result or only metadata was read.

Earlier progress messages said 47 items (21 + 26); the completed JSON has **46 (21 + 25)**. No item has been omitted to force a total: the preliminary arithmetic was incorrect.

## Source boundaries and scan work

Both full transcriptions and the page chunks were consulted. All fifteen scans P000173 through P000187 were visually inspected, including the diagrams. Decisive rereads included the quotient exponent P000176; the critical-extension and dimension-difference displays P000180; the definition of μ P000181; the intrinsic-derivative arrows P000182; the real-pencil and moduli drawings P000183–184; the local-algebra list P000186; and the surname in the P000187 plan.

The MCCME catalogue intervals overlap. The 21 November lecture starts on P000173, after P000172's preceding material; the 28 November date starts P000179. Arnold's lecture ends on P000186. P000187 opens with the prospective plan and then starts Kirillov's lecture, assigned elsewhere. The heading record 117 contributes no theorem. Record 118's catalogue title is 13-Feb-67 but its date field says “no date”; the JSON preserves an empty date and explains the title. The English plan's “Dynkin” is the clear Russian **Дынин**, hence **Dynin**.

## Main publication matches and chronology

### Arnold's 1968 survey

The closest match is V. I. Arnold, *Singularities of smooth mappings*, Russian Mathematical Surveys 23(1), 1–43 (1968), DOI 10.1070/RM1968v023n01ABEH001232. Its opening identifies the 1966 lecture origin. Full text opened at:

https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=5591&what=fullteng

The relevant inspected parts are §1 (Morse/Whitney and the perturbed square, especially Example 6, pp.4–5), §2 (jets and Boardman/Morin material), §3 (intrinsic quadratic differential, binary pencils, and the quadratic-map dimension argument), and §4 (local algebras and preparation). This accounts for close matches without attributing older classical material to Arnold as new research. The explicit perturbation and four-dimensional real examples are A; Morse, Whitney, jets, and elementary pencil geometry are E.

### Boardman's theorem and two substantive formula errors

J. M. Boardman, *Singularities of differentiable maps*, Publications Mathématiques de l'IHÉS 33, 21–57 (1967), DOI 10.1007/BF02684585. Opened:

https://www.numdam.org/item/PMIHES_1967__33__21_0.pdf

The universal-stratum statements were read in Theorems 6.1–6.3, printed p.46. Definitions 6.4–6.5, pp.46–47, resolve the codimension formula: for source dimension m and target dimension n the coefficient is **n − m + i₁**, and μ counts nonincreasing bounded sequences with **j₁ > 0**. Both notebook omissions are visible in the scans and are therefore faithful errors, not mistranscriptions. The independent length-one rank-stratum test forces the same corrections.

The 1965 circulation date is explicitly notebook testimony, while the publication year is 1967. §2 supports coordinate-independent Jacobian extensions; §7 supplies the higher intrinsic-derivative framework. The missing target-coordinate check is elementary: target diffeomorphisms preserve the target maximal ideal, so its pulled-back ideal is unchanged. It is a resolved proof exercise, not an orphan conjecture.

### Mather's classification and the corrected elliptic family

J. N. Mather, *Stability of C∞ mappings, IV. Classification of stable germs by R-algebras*, Publications Mathématiques de l'IHÉS 37, 223–248. Opened:

https://www.numdam.org/item/PMIHES_1969__37__223_0.pdf

Theorems A and B, pp.223–225, were read, along with the source–target linearization and regular-intersection criterion. The manuscript receipt is 1 June 1968. The journal volume is dated 1969, but the scan's printing colophon says 1970; the JSON and bibliography preserve this distinction. The paper itself temporarily uses “stable” as shorthand for “infinitesimally stable,” announcing the equivalence proof separately. The chapter does not mistake its introductory convention for a proof of the global equivalence theorem. For Mather II, the official publisher metadata were opened, while the germ statement was read in Mather IV and Arnold.

J. N. Mather, *Stability of C∞ mappings. VI. The nice dimensions*, Lecture Notes in Mathematics 192, 207–253 (1971); full Russian translation in Uspekhi Matematicheskikh Nauk 29(1), 129–158 (1974), opened:

https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=4325&what=fullt

The introduction gives the density criterion; §7, printed pp.150–151 of the translation, gives the five stable real corank-two algebra families and their lengths. The historical paragraph is unusually useful: Mather announced a classification in a letter to Morin in autumn 1965; it contained an error; Morin corrected it; Arnold described the corrected result. This history is not conflated with a claim that the precise notebook mixed-monomial error is the same error in the letter.

The notebook writes its three-generator elliptic family as `(x^a, xy^(a−1), x²+y²)`. The final classification requires `(x^a, x^(a−1)y, x²+y²)`. For odd a the literal mixed monomial is redundant. The first mismatch is a=3: length six instead of five. The notebook's IV and V labels are also reversed relative to the final table; that is a naming/provenance issue, separate from the wrong monomial.

### Earlier sources and verification distinctions

- Malgrange's *Ideals of Differentiable Functions* (1966) was opened at https://mathweb.tifr.res.in/Documents/Publications/Studies/SM_03-Ideals-of-Differentiable-Functions.pdf . Its preface records 1964 lectures and July 1965 preparation. Chapters III and V are the analytic and smooth preparation context; Arnold §4 states the precise finite-module consequence used here. Smooth coefficients need not be unique and the module is not asserted to be free.
- Thom's *Les singularités des applications différentiables* (1956), https://www.numdam.org/item/AIF_1956__6__43_0.pdf , was opened and Part I checked for pre-lecture rank/transversality provenance.
- Whitney's 1955 plane-map paper's metadata and abstract were checked in the curated author bibliography, entry 102, https://celebratio.org/Whitney_H/article/219/ . Its JSTOR endpoint did not expose the original article. Accordingly the original proof is not called inspected; Arnold is the opened source for the normal forms.
- Mather's July 1970 *Notes on Topological Stability*, https://webhomes.maths.ed.ac.uk/~v1ranick/surgery/mather.pdf , were opened for the isotopy framework, especially §11.
- Mather's *Stratifications and mappings* was opened at https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=5110&what=fullt . The first page identifies a 1971 Harvard preprint translated by A. N. Varchenko in 1972. The theorem on printed p.88 gives finitely many generic topological germ types outside a finite-jet exceptional set of codimension greater than the source dimension. The article calls its proof a sketch. This is a precise later development of the topological theme, but it is not silently equated to the notebook's countable partition outside infinite codimension.

## What remains unidentified, and why there is no C/D development

Two F items retain their uncertainty. The “trefoil knot” caption accompanies planar drawings but specifies no lift into three dimensions; only the large-circle winding number two is well defined. The threshold “from 12, infinitely many invariants” specifies neither scalar versus functional moduli nor the germ class and quantifiers. Searches and the close Arnold/Mather sources do not justify substituting the precise dimension-nine modulus theorem for this separate line.

The Thom countable-topological-partition announcement is B with **partial match / indirect verification**, not an exact-match solved claim. The later finite generic classification is explicitly stated with its different exceptional-set quantifier. There is no defensible precise current open problem in this gap alone.

Other question marks are ordinary proof obligations: target-coordinate invariance, intrinsic Hessian invariance, the Boardman table, and local algebra length. The finite analytic equal-dimensional case of length/multiplicity is established; the unrestricted real or unequal-dimensional interpretation is false or lacks the required meaning. Converting any of these into a new unsolved problem would be misleading. Consequently no C/D item qualifies for Stage 2. `development.tex` is intentionally comments only.

## Independent checks and limitations

`check_singularities.py` uses only Python's standard library and exact rational arithmetic. Its output is `check_singularities_output.json`; run with `python parts/arnold/check_singularities.py` from the project root. The first attempted SymPy import was unavailable, so the final script instead includes a short exact polynomial/Groebner implementation and a separate degree-by-degree relation-rank implementation. There are no unrecorded library requirements.

The checks passed:

1. **246 Boardman symbols** (length at most five, entries at most four) were counted both by exhaustive enumeration and by recursive counting; the relevant table values and the unequal-dimensional rank-stratum reduction agree.
2. The literal and repaired elliptic algebra lengths for **a = 3,…,8** were computed twice, by standard monomials of an exact Groebner basis and by exact ranks of homogeneous relation matrices. A third, symbolic normal-form derivation explains the parity: modulo `y² = −x²` and `x^a = 0`, `xy^(a−1)` is redundant for odd a and equals a nonzero multiple of `x^(a−1)y` for even a. Thus the error is structural, not a numerical artifact.
3. The normal Jacobian linearization of both four-dimensional examples has determinant **−1**. An explicit inverse checks this independently.
4. The real Jacobian of `z² + ε conjugate(z)` is `4x² + 4y² − ε²`; the Wirtinger formula gives the same result.
5. Enumerating jet monomials agrees with the binomial dimension for one to four variables and orders zero to four.

The notebook's intrinsic Hessian invariance was also re-derived from the source/target chain rules. The raw cubic counterexample `x²` under `x=u+au²` is direct and exact. These checks are editorial annotations, marked `\oursComputed` where computations enter the occurrence index; they are not presented as newly solved research questions. Finite tests do not stand in for Boardman's universal theorem.

## Method observations for the overall report

The A–F taxonomy is about provenance and research fate, while literal correctness is independent: a B can contain a faithfully copied false formula. These lectures strongly demonstrate the value of the separate assessment columns. “Verified reference” must likewise be separated from “read exact theorem”; the Whitney and Mather II entries deliberately preserve that distinction.

Citation locators need both the original publication year and translation-page coordinates. Formula comparison should always include a minimal test case: order-one jets and length-one Boardman symbols exposed errors that plausible-looking displays can conceal. Final-family nomenclature should not erase historically different notebook labels. Diagram-dependent claims without specified ambient structures should remain F rather than become elaborate reconstructions.
