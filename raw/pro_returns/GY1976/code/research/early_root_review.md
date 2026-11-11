# Independent review of record 437

Reviewer: early-records agent. Date: 2026-11-10. No root files edited.

## Verdict

The contraction proof, raw point-case counterexample and twist-sign proof in `root_checks.tex` are correct. The remaining mathematical items were checked for grading, fibre/sheaf distinctions, stable equivalence, and hypotheses. No further mathematical defect was found beyond the precision and locator improvements below.

## Exact replacement for occurrence 1977-437.19

`early_root43719_review.json` contains proposed replacements for `statement` and `reconstruction`, plus a locator suggestion. It keeps the notebook's raw tensor convention separate from the modern dual-module convention. Both internal degree and cohomological degree are specified, and the representative is the degree-zero kernel of the Tate complex.

The relevant EFS conventions were read directly in the opened full preprint:

- https://arxiv.org/pdf/math/0104203, version 2, 8 June 2001: §1, pp. 4–5, for dual free modules and shifts; §2, p. 6, for the Hom differential and both gradings; Corollary 2.4, p. 8, for exactness except at the first term; Theorem 3.7, pp. 17–18; the initial construction in §4, p. 18, for the minimal Tate completion.
- Web refs: turn111view1, turn112view2, turn112view3, turn114view0 and turn114view1.

### Independent index derivation

Write internal shifts as `Q(a)_j = Q_(a+j)` and cochain shifts as `K[a]^j = K^(a+j)`. Put `Z_m = ker(T^m -> T^(m+1))`. For the large cutoff `N`, the regraded kernel `Z_N(N)` has its injective resolution in cochain degree zero after shifting the tail by `[N](N)`. Reciprocity gives

`L(Z_N(N))` quasi-isomorphic to `M_(>=N)(N)`.

After sheafification the right side is `E(N)`. Directly from the chapter's convention,

`L(Q(N)) = L(Q)[-N](N)`.

It follows that `L(Z_N)` is quasi-isomorphic to `E[N]`. Each exact sequence

`0 -> Z_m -> T^m -> Z_(m+1) -> 0`

has a free middle term, whose associated linear sheaf complex is acyclic by the independent contraction proof. Therefore `L(Z_(m+1))` is quasi-isomorphic to `L(Z_m)[1]`. Iterating gives `L(Z_N) = L(Z_0)[N]` in the derived category. Cancelling the shift yields `L(Z_0)` quasi-isomorphic to `E` in degree zero. Since `E` is locally free, the bounded locally free complex is locally split away from that term; its derived fibres have no other homology. Hence `Z_0` is proper and `Phi(Z_0) = E`. This derivation confirms that the desired kernel is `ker(T^0 -> T^1)`, with no extra twist.

Two small cases check the indexing independently: for a point and `E = O`, `Z_0` is the one-dimensional trivial exterior module in degree zero; for `P^1` and `E = O(-1)`, the resulting linear complex is the Euler kernel `O^2 -> O(1)`, whose degree-zero cohomology is `O(-1)`.

## Locator corrections

The actual first two pages of the BGG paper were viewed:

https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/BGG-3.pdf

Web refs turn111view0, turn113view0 and turn113view1. The `L_xi` complex, special proper/“faithful” condition, Euler-rank observation and free-module acyclicity are in **§2**, English pp. 212–213. Change the §3 locators in occurrences 1977-437.6, .7, .8 and .10 to §2. The derived functor is in §3; the existing §3 reference for .15 is appropriate. Remark 2 after Theorem 1 has exactly the chapter's positive twist and cokernel grading convention.

## Chronology qualification

The BGG paper was received on 10 January 1978, before the scan's lecture date of 13 February 1978. Class A is defensible under the kit's literal later-publication definition, but the text must say that it refers to subsequent publication of current work, without implying that its discovery or first private circulation followed the lecture. The receipt date is already preserved in the bibliography; a short explicit overview sentence resolves the potential ambiguity.

## Other checked points

- Contraction works over every field because the algebra is defined as an exterior algebra, including the square-zero relations in characteristic two.
- The rank formula `binomial(m-1,r)` is the rank from exterior degree `r` to `r+1`.
- The local-freeness argument for a proper module legitimately uses elimination of invertible minors, rather than relying only on constancy of Euler characteristic.
- The intrinsic non-abelian-category example is valid: the hyperplane multiplication map is monic and epic among vector bundles but is not invertible. The point exception is correctly included.
- Finite generation in .18 concerns the truncated graded section module; the quotient-category and localization statements in .21–.23 have the needed coherence and grading hypotheses.
