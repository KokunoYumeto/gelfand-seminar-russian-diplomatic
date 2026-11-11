# Targeted independent review of records 322 and 323

Reviewer: `/root/manin_fuchs`; 9 November 2026. Reviewed the latest statements, reconstructions, and fate annotations in `work/fragments/autumn_representations/items.json`. No autumn files were edited. **No concrete mathematical correction is requested.** This is a targeted check of stable-rank/K2 distinctions and derived-functor hypotheses, not a new current-status search.

## Record 322: stable rank and K2

The definition uses two independent reduction coefficients and the unit-ideal meaning of unimodularity. The nonzero-K2 theorem asserts existence of an obstructed triple, so it is compatible with reducibility of one particular triple over complex coefficients. Matsumoto's field theorem allows the Milnor and ordinary algebraic K2 conventions to be identified here.

I independently reopened Vaserstein–Suslin (1976), §19, printed p. 994. It explicitly attributes the nonzero-K2 lower bound to Krusemeyer, gives stable rank two for fields algebraic over finite fields, and distinguishes other vanishing-K2 fields as an unresolved case at the time. I also reopened Suslin (1980), printed pp. 589–590; its introduction preserves the same distinction and does not replace it by the notebook's unconditional dichotomy. Thus items 322.3–322.4 correctly separate the verified theorem from the stronger published assertion. The fragment does not infer a 2026 open-problem classification solely from an older unresolved statement.

Weibel (2013), Chapter III, Exercise 6.5, printed p. 243, explicitly gives \(K_2(\overline{\mathbb Q})=0\) (written multiplicatively as the trivial group). I reopened and located that exercise. This confirms the counterexample in 322.5 to the claimed classification of all fields with vanishing K2. The counterexample alone does not determine the stable rank of the polynomial ring, as the fragment correctly states.

The real disk-degree obstruction applies to real-valued continuous coefficients; it does not obstruct the complex polynomial certificate in 322.9. The explicit complex formulation is therefore correctly separated from the earlier real example and from the unidentified winding invariant. Stable symplectic K1 is defined by the direct limit rather than an unjustified finite-rank identification.

Primary references reopened for this review:

- Vaserstein, L. N., & Suslin, A. A. (1976). Serre's problem on projective modules over polynomial rings, and algebraic K-theory. *Mathematics of the USSR-Izvestiya, 10*(5), 937–1001. §19, p. 994. [Full text](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=2227&what=fullteng). Web retrieval: `turn181view0`, exact passage `turn182view0`.
- Suslin, A. A. (1980). Reciprocity laws and the stable rank of polynomial rings. *Mathematics of the USSR-Izvestiya, 15*(3), 589–623. Introduction, pp. 589–590. [Full text](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=1759&what=fullteng). Web retrieval: `turn181view1`, exact passage `turn182view2`.
- Weibel, C. A. (2013). *The K-book: An introduction to algebraic K-theory*. American Mathematical Society. Chapter III, Exercise 6.5, p. 243. [Author-hosted full text](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.pdf). Web retrieval: `turn180view2`, exact exercise `turn181view3`.

## Record 323: derived constructions

The following checks use the explicitly stated hypotheses and elementary properties of complexes; I did not reopen every already-verified Stacks/Weibel reference in this targeted pass.

- Bounded-above projective resolutions have the comparison theorem used in 323.2 and 323.6. Their Hom complexes are determined up to chain homotopy, which is stronger than merely recording graded cohomology.
- The acyclic nonsplit complex of abelian groups in 323.3 is correctly distinguished from a contractible complex.
- The internal Hom uses a product over source degrees and the differential \(d\phi=d_N\phi-(-1)^{|\phi|}\phi d_P\). These are the correct totalization and signs; they give \(d^2=0\).
- The doubly infinite complex with differential \(\varepsilon\) over \(k[\varepsilon]/(\varepsilon^2)\) is acyclic because kernel and image both equal \(\varepsilon A\). It is not contractible, since \(dh+hd\) has image in that ideal. This correctly demonstrates why arbitrary unbounded complexes of free modules cannot replace the bounded-above hypothesis.
- A bounded-above projective complex is K-projective, so the computation of derived Hom against an arbitrary target complex in 323.8 is valid. The result naturally lies in \(D(\mathbb Z)\) for a general noncommutative coefficient ring, and its cohomology gives shifted morphisms in the derived category.
- For an additive contravariant left-exact functor, degree reversal sends a bounded-above projective replacement to a bounded-below complex. The variance \(D^-(A)^{\mathrm{op}}\to D^+(B)\) in 323.9 is correct.
- The universal transformation for a total right derived functor has the direction \(Q_BF\to RFQ_A\). Precomposition gives \(\operatorname{Nat}(RF,G)\to\operatorname{Nat}(Q_BF,GQ_A)\), as in 323.10. The fragment correctly separates that direct map from its inverse when a universal factorization has already been established, and does not assert existence without hypotheses.

The parent was informed that these targeted statements pass the independent mathematical check.
