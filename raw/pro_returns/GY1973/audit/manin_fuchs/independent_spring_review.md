# Independent spring review

Reviewer: `/root/manin_fuchs`; 9 November 2026. The latest spring fragment contains 100 items. No spring files were edited. The longer calculation and scope record is `spring_review.md` in this directory.

## Two convention qualifications

1. **1973-327.12, real forms of KP.** The commutator and elimination are correct:

   \[
   (4\alpha u_t+u_{xxx}+6uu_x+4\lambda u_x)_x+3\beta^2u_{zz}=0.
   \]

   The sentence that nonzero rescalings give both signs needs a real-form qualification. With real nonzero \(\beta\), real rescaling cannot change the relative sign of \(u_{xxxx}\) and \(u_{zz}\), because their scaling factors involve even powers. Suggested replacement: “For real nonzero \(\beta\), real rescalings give the positive transverse sign of KP; a purely imaginary \(\beta\) with the corresponding reality reduction gives the opposite real form.” No change to the displayed elimination is needed. This finding follows directly from the operators displayed in 327.11.

2. **1973-333.19, half-wave time orientation.** With \(U(t)=e^{+it\sqrt L}\) from 333.18 and the output-first primed relation from 329.7, the canonical relation is the graph of geodesic flow at time \(-t\). In Euclidean coordinates, stationarity of \((x-y)\cdot\xi+t|\xi|\) gives \(x=y-t\xi/|\xi|\). Suggested insertion: “With our positive-exponential convention, the primed canonical relation is the graph of geodesic flow at time \(-t\).” The current wording does not specify an orientation; the statements about \(|t|\), caustics and closed-geodesic lengths are unaffected.

## Independent primary verification of the strong torus theorem

Shnirel'man, A. I. (1975). The asymptotic multiplicity of the spectrum of the Laplace operator. *Uspekhi Matematicheskikh Nauk, 30*(4[184]), 265–266. [Metadata](https://www.mathnet.ru/eng/rm4279); [full primary text](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=4279&what=fullt).

I opened and visually inspected both pages. They explicitly define \(\Lambda=\sqrt{-\Delta}\), assume a smooth sufficiently near-Euclidean metric on \(T^2\), and state the adjacent-neighbor bound for **every \(k>1\)** and **every \(N\)**. The text distinguishes Lazutkin's positive-density subsequence result. Four invariant KAM tori paired by time reversal appear in the proof. The receipt date is 7 May 1974. Item 333.16's spectral parameter, quantifiers, hypotheses and chronology are therefore supported by the primary paper. Web trail: `turn175search0`, `turn176view0`, `turn177view0`, screenshots `turn178view0` and `turn178view1`.

## Other checks

The reviewed Lax and Floquet signs, half-trace discriminant convention, soliton speed and phase-shift factors, Miura identity, Whitham phase compatibility, stable gauge-group interpretation, and Fock normalization are consistent. The wavefront-kernel section assigns the zero-output and zero-input covector exclusions correctly and includes the composition support condition. The heat coefficients and Cauchy-smoothing thresholds are correct: convergence requires \(n<4\) for Laplacian eigenvalues and \(n<2\) for square-root frequencies. The exact-versus-thematic distinctions for absent Green/Whitham content, billiard versus closed-manifold trace formulas, and incomplete gap questions are suitably restrained. These checks do not imply that every bibliography entry was independently reopened by this reviewer.

Both qualifications and the Shnirelman verification were sent to the parent. No additional material issue was identified in the checked spring statements.
