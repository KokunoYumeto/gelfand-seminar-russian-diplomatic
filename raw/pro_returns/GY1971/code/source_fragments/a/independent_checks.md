# Independent check of item 1971-256.8

Checked: November 2026, independently by the records 229–243 agent after its own fragment handoff.

## Verdict

The cusp counterexample in the saved item is correct for every prime p, including p = 2 and p = 3. The interpretation of the historical assertion as a comparison between ordinary algebraic K-theory and Karoubi–Villamayor theory is explicitly a modern reconstruction. The deduction from the later literature is appropriately marked \ours. It does not require a conjectural calculation or an unmentioned regularity assumption on the cusp.

## Sources actually opened and passages read

1. Hesselholt and Nikolaus, *Algebraic K-theory of planar cuspidal curves*, https://arxiv.org/pdf/1903.08295: Theorem A on PDF p.1 and the normalization/relative-theory discussion on p.3. The theorem assumes a perfect F_p-algebra and coprime integers a,b ≥ 2; it does not assume that p is prime to ab. It is stated for the ordinary relative algebraic K-groups, not merely an unspecified completion.
2. https://arxiv.org/abs/1903.08295: first submission 20 March 2019, revision 17 July 2019 verified. The 2020 publication metadata are documented by the authoring agent; this check independently verifies the preprint dates.
3. Weibel's author-hosted Chapter IV, https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.IV.pdf: Definition 11.4 and Lemma 11.4.1 (KV indexing and natural comparison), Corollary 11.5.2 (polynomial homotopy invariance), Theorem 11.8 (regular-ring comparison), Exercise 11.5 (positive grading), Corollary 1.13 (finite-field K-groups), and the homotopy-fibre long exact sequence in §1.2.

Query used to locate the latter: “Weibel K book IV theorem 11.8 Karoubi Villamayor K theory exercise 11.5 homotopy invariant.” Only the author's text, not search snippets or third-party discussions, supports the mathematical check.

## Check of the ring and homotopy

Let k = F_p and A = k[x,y]/(y²−x³), with x mapping to t² and y to t³. Every polynomial modulo the relation has the form f(x)+y g(x). Its image has even powers of t from the first term and odd powers at least three from the second; these cannot cancel. Thus A embeds in k[t] with image k[t²,t³], so it is an integral domain in every characteristic.

Let ε:A→k be the augmentation at x=y=0 and i:k→A the constants. They satisfy εi=id. The map H:A→A[s] defined by H(x)=s²x and H(y)=s³y is well-defined because H(y²−x³)=s⁶(y²−x³). Its endpoints are iε and id_A.

For any polynomial-homotopy-invariant group-valued functor F, the two evaluations A[s]→A induce the same homomorphism: each is inverse to the isomorphism induced by constants A→A[s]. Hence F(i)F(ε)=id and F(ε)F(i)=id. Applying Weibel IV Corollary 11.5.2 gives KV₂(A)≅KV₂(k). The field k is regular, so Theorem 11.8 identifies KV₂(k) with K₂(k), and Corollary 1.13 gives K₂(F_p)=0. Therefore KV₂(A)=0.

## Check of nonzero relative K₂

Take a=2, b=3, r=1 in Hesselholt–Nikolaus Theorem A. With I=(x,y), its formula reads

K₂(A,I) ≅ W_S(k)/(V₂W_{S/2}(k)+V₃W_{S/3}(k)),

where S={m>0 : ℓ(2,3,m)≤1}, and ℓ counts positive integer solutions of 2i+3j=m. Since ℓ(2,3,1)=0, 1 belongs to S.

Projection to Witt coordinate 1 is a surjective additive map W_S(k)→k: the first Witt addition polynomial is ordinary addition. For any Verschiebung V_d with d>1, its first coordinate is zero. Thus both denominator subgroups are contained in the kernel, and coordinate 1 descends to a surjection from the displayed quotient onto k. Because k is nonzero, K₂(A,I) is nonzero.

This reasoning does not use division by 2 or 3 and does not use the later p-typical decomposition that temporarily chooses b prime to p. The big-Witt theorem itself applies uniformly.

## Check of relative versus absolute K₂

The relevant exact segment is

K₃(A) → K₃(k) → K₂(A,I) → K₂(A) → K₂(k).

The ring section i makes K₃(A)→K₃(k) surjective. Consequently the connecting map into K₂(A,I) is zero, and the relative-to-absolute map is injective. Since K₂(k)=0, that map is also surjective. Therefore K₂(A,I)≅K₂(A)≠0.

The split augmentation is essential to this justification: nonzero relative K₂ and K₂(k)=0 alone would not exclude a nonzero connecting image from K₃(k). The saved item includes the split augmentation, so no gap remains.

## Attribution and integration note

The relative K-group formula is Hesselholt–Nikolaus's theorem; regular comparison, homotopy invariance and finite-field vanishing are literature inputs. The particular cusp diagnostic, coordinate-1 nonvanishing argument and assembly of the comparison counterexample are the supplied verification deduction. The existing \ours marker is appropriate. No alteration of the authoring agent's item was made during this check.

The result establishes that absence of zero divisors is insufficient for K_n(A)→KV_n(A) to be an isomorphism. It does not claim that this cusp is the earliest known counterexample or that the 2019/2020 computation was available to the 1972 seminar.
