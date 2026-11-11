# Records 663–666: research, provenance, and verification

## Scope

The fragment has four catalogue records, including the empty mathematical heading 665, and 52 mathematical items: 15 in 663, 16 in 664, and 21 in 666. All 15 original leaves P001245–P001259 were inspected against the diplomatic Russian and English. Core attribution ends at P001257. P001258 and P001259 contain separately headed Kontsevich and Morozov talks and belong to adjacent records 667 and 668, respectively. They are itemized in a separate supplement to avoid both silently omitting supplied mathematical material and assigning it to Beilinson.

The source spans in the supplied catalogue overlap substantially. In particular, P001244 still belongs to Feigin; Novikov begins on P001245. Knizhnik begins in the middle of P001248. The year-1986 catalogue heading is not an independent mathematical leaf or talk. These decisions are grounded in manuscript headings, not inferred from subject matter alone.

## Publication identification

### Novikov

Math-Net searches for the exact phrases 'finite-gap two-dimensional Schrödinger operators' and their Russian equivalents found Dubrovin–Krichever–Novikov (1976) and the two Veselov–Novikov papers of 1984. The author-hosted 1976 English translation was read in full at the relevant lemmas and theorem. The author-hosted 1984 potential-operator paper was read for the involutions, Prym construction and reality conditions. Math-Net's English full-text link for the explicit-formula paper redirected to metadata; switching through the actual Russian full-text link supplied the original five pages. Section II, Theorem 1 and formulas (4)–(6) settle the existence of the hierarchy before the seminar. The final approximation conjecture in that publication is not imported as an occurrence because the notebook does not state it.

The Manakov two-page original was opened and read, including equation (5), to establish the fixed-energy provenance. Its own broad introductory no-Lax wording is not treated as a theorem with missing universal hypotheses. The elementary two-soliton counterexample in the check appendix is fully verified here and does not rely on interpreting that sentence charitably. Independent review rederived the commutator, Baker–Akhiezer coefficients, reality sign, residue argument and Prym dimension. Oscillatory exponentials, the sign of the leading Schrödinger operator, and the placement of the first-order derivative must be fixed together; isolated formulas in later retypings can differ or contain errors.

The short rational-soliton announcement is matched only partially to Grinevich–R. G. Novikov (1985) and Grinevich (1986), whose metadata were checked. The phrase that rapidly decaying inverse scattering is essentially solved lacks energy, decay, exceptional-set and data hypotheses. Later publications by R. G. Novikov–Henkin (1987) and Grinevich–S. P. Novikov (1988) have different authors and scopes. Their metadata establish later thematic development, not an exact proof of the notebook slogan. Consequently this occurrence is F, not D or a fabricated open problem.

### Knizhnik and Beilinson

The full Belavin–Knizhnik JETP paper (1986) supplies the main exact comparison: determinant/Gram factors in section 2, curvature in section 3, the global Mumford-form construction in section 5, and low-genus theta formulas in section 6. Its submitted date is 18 February 1986; this is kept distinct from the December and February seminar dates and the August English issue. The Landau Institute author bibliography verifies the Knizhnik analytic-fields paper and the four-author low-genus announcement. Publisher full text for the analytic-fields paper was not accessible, so the last incomplete stress-tensor expression remains F rather than being reconstructed from its title.

Quillen's original Russian paper was obtained through Math-Net and read, especially sections 1–4. It uses the dual of the determinant line written in the notebook. The positive spectral factor in Quillen's convention must be inverted on det H^0 divided by det H^1. A complete finite-dimensional singular-value proof, a one-dimensional acyclic example, and exact rational examples independently check the direction of the factor. Bost's 1987 Bourbaki exposition explicitly distinguishes the conventions and states the anomaly, curvature, Mumford isomorphism and remaining multiplicative constant. The full exposition was opened, but OCR loses some formulas; algebraic coefficient checks were therefore made separately rather than describing uncertain OCR as visual verification.

The Beilinson–Manin 1986 publisher page and abstract were accessible; its Project Euclid full text was blocked by an access page. Its metadata identify a direct subsequent publication by the speaker, while the exact geometric statement is checked in the accessible Belavin–Knizhnik and Bost sources. The item verification and bibliography annotation make this limitation explicit.

The canonical-curve multiplication exception was checked in Matone–Volpato, section 3.1; the nonsingular odd characteristic in section 4.1. This paper first circulated in 2006, appeared online in 2012, and belongs to a 2013 journal issue. Those dates are not collapsed into one. Fay's book metadata and contents were opened, but the full book was not read. The explicit hyperelliptic basis in the appendix proves the exceptional cokernel dimension uniformly, including genus two.

The torus determinant was checked in Kokotov's 2007 preprint, section 5.0.1, equation (5.1), and the original Ray–Singer 1973 metadata were opened. The flat metric |dz|^2 has area Im τ; the unit-area metric changes one determinant power. A normalization ambiguity is retained in the ledger instead of declaring that a context-free formula is simply false.

Shiota's 1986 publisher page and bibliography were checked. The earlier 1983 Kyoto seminar notes are a separate circulation witness, not a journal date. The precise KP-recognition statement and a later auxiliary-equation refinement were read in Krichever's 2006 author-hosted chapter. The general Schottky problem is indexed as GP-1985-60, while the unnamed marginal relations are not invented. The supplied earlier index has contextual Jacobian/theta items but does not state the same exact problem with an existing problem identifier.

Witten's superstring treatment was read selectively in version 4 (2023), especially the integration-cycle, infrared-pole and tadpole qualifications. It is used to explain why 'everything converges' is not a single quantified theorem. It does not support an all-model or all-genus convergence assertion.

## Classification decisions

The late fragment has A1/B6/C0/D0/E41/F4. Beilinson's direct subsequent Mumford-form publication is A. Belavin–Knizhnik curvature and the named low-genus results are B relative to the listed principal speaker, with interventions and credit stated explicitly. The 1976/1984 spectral constructions and the Quillen construction are E. Four incomplete statements are F: the higher-dimensional curve criterion, the blanket rapidly decaying scattering claim, the incomplete higher-genus stress formula, and unqualified superstring convergence. None gives a definite orphan question suitable for Stage 2.

The A–F axis cannot itself encode all authorship and chronology. A later exact geometric formalization can implement already circulating ideas; a faithful handwritten formula can be false even when its surrounding theorem is old. The literal-correctness, reconstruction, first-circulation and verification fields carry those distinctions.

## Checks and audit trail

`code/check_mathematics.py` contains two implementations of the differential-operator identities; the explicit two-soliton PDE and an independent Hirota-bilinear calculation; Laurent leading-term cancellation; a real and complex Beltrami Jacobian comparison; determinant singular-value examples; the Todd coefficient; modular weights; and local-order/dimension checks for hyperelliptic quadratic differentials. It also checks the Stage 2 stacking constructions by exact rational arithmetic and independently enumerates all supporting facets. The proof appendix states exactly which general facts are proved and which finite computations merely check the implementation.

The initial unsimplified symbolic two-soliton differentiation was interrupted because intermediate expressions expanded unnecessarily. Replacing each rational derivative by its exact cancelled form made the full check finish; the resulting identity is unchanged. This is a performance correction, not a changed mathematical claim. All completed assertions pass. Two independent reviewers checked the record-663 signs and the explicit nonrigidity example; their review is included in the audit directory.

No online source's `verified` marker means that every theorem in it was read. `sources.json` records the exact URL, locator and verification scope for all 24 references in this fragment. Failed access attempts are retained above. The historical manuscript and the source publications remain separate evidentiary layers.
