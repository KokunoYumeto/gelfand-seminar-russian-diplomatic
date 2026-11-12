# Independent cross-review of autumn records 2–14

Reviewer: winter-records research agent. Review date: 12 November 2026.

## Scope and independence

I read the notes, precise statements, reconstruction, fate, present-status, and assessment fields for all 83 items in work/parts/autumn/items.json, records 2–14. I checked mathematical consistency and the relation between the recorded question and the stated fate. I also read the class definitions in CHAPTER_FORMAT.md and the overview/report prose in work/code/make_report.py. The generated report was not yet present when the review began, so the report findings concern its generator.

The review used direct mathematical checks and the evidence limitations already recorded in the items. It did not repeat the literature search, independently authenticate every cited source, or reread every manuscript scan. For the Lorentz-group convention and invariant-extension hypothesis, I checked the English and Russian source transcriptions on P000027–P000028; they say Lorentz group without specifying a connected component and explicitly refer to a distribution invariant off the origin. The review did not edit the autumn files.

Reviewed snapshots:

- items.json SHA-256: 28e1d62943f86c3bb33fdc6459cc7fcea312c741c33020b501c79bf3eb51b3ee.
- make_report.py SHA-256: d11aaa403923c0da287f77db69b2789bc0acfdbf6d0cabf62cb16ed0b667cb82.

## Concrete corrections

### 1. Item 1964-12.3: proper versus proper orthochronous Lorentz group

The statement currently says that for the “proper Lorentz group” one must distinguish the two time orientations. That terminology is insufficient: determinant +1 alone allows a transformation that reverses both time and one spatial coordinate. For example, diag(-1,-1,1,…,1) preserves the Minkowski form, has determinant +1, and interchanges future and past timelike vectors.

If the intended group is the identity component, replace “proper Lorentz group” by “proper orthochronous Lorentz group (the identity component).” Since the notebook does not specify this component, the reconstruction should label that choice explicitly. An equally safe formulation is:

> For the identity component of the Lorentz group, future and past timelike orbits are distinct; for the full proper group they may be interchanged. The notebook does not specify the component. In either convention, reduction to a distribution in the quadratic invariant needs separate analysis at the light cone and origin.

This correction preserves the existing limitation: the complete invariant-surjectivity theorem was not read and should not be asserted.

### 2. Item 1964-12.4: invariance on the punctured space is a required hypothesis

The statement begins “Suppose a distribution on the punctured space has an extension of bounded order.” It must explicitly assume that this distribution is invariant under the group action and that the group fixes the origin. Otherwise the differences between an extension and its transforms need not be supported at the origin, and the finite-dimensional delta-jet cocycle argument does not follow.

Minimal correction:

> Suppose a G-invariant distribution on the punctured space, for an action fixing the origin, has an extension of bounded order.

Retain the existing requirement that all transform differences lie in one finite-dimensional invariant jet space and depend continuously on the group element. With those hypotheses, the cocycle argument for a connected semisimple group is sound: if b(g)=g·ũ-ũ is a coboundary g·v-v, then ũ-v is the invariant extension. The source transcription already supplies the missing invariance assumption, so this is a repair of the modern statement.

### 3. Item 1964-9.2: finiteness of the partition function

Stability alone does not imply that the displayed integral over unrestricted momenta is finite. A Hamiltonian identically zero is bounded below but its momentum integral over Euclidean space diverges.

Minimal correction: explicitly assume T>0 and 0<Z_N<∞ before defining F_N and its derivatives. Alternatively, specify the usual positive quadratic kinetic energy plus a stable potential on a finite-volume configuration domain, with a nonempty admissible set of positive measure. The existing “when derivatives exist” qualification can remain.

This does not affect the corrected distinction between physical free energy and reduced minus-log free energy.

### 4. Overview/report: qualify what the class-E count establishes chronologically

The overview defines E as “prior mathematics”; the report table says “Known before the talk.” Those are the required schema labels, but the surrounding prose needs to distinguish an editorial expository classification from independently verified pre-talk publication chronology.

In particular, 1964-6.5 explicitly says that exact theorem-by-theorem priority was not established from the metadata of the 1973 book. Items 6.2 and 6.6–6.8 similarly rely on direct reconstruction and/or later thematic sources. The Thoma entries 11.1 and 13.4 correctly distinguish notebook evidence of knowledge by October 1964 from the uncertain public-distribution date behind the publisher's issue label. These restrictions should remain visible in the aggregate report.

Suggested report addition:

> Class E records the editorial identification of prior or expository mathematics. It is not a uniformly verified claim about the first publication date of every reconstructed statement. Where only a later source or a direct mathematical reconstruction was checked, the item says so; some record-6 assertions lack an independently established pre-talk theorem-level publication date. The notebook can establish that a result was known by the lecture without establishing when it first circulated publicly. Class-E counts must therefore not be read as counts of independently audited priority claims.

A shorter overview qualification would suffice:

> Class E identifies prior/expository mathematics; exact pre-talk publication chronology is verified only to the extent stated in each item's fate.

No class reassignment is required merely to implement this reporting caveat. A claimed audited chronological result would require additional evidence rather than stronger wording.

## Other findings

No further material mathematical inconsistency was found in the 83 reviewed items. In particular, the completed-measure pushforward argument in 6.2 is sound under its stated finite Radon/Hausdorff/continuous hypotheses; the surface-group H¹ formula retains both invariant dimensions; the entropy refinement in 10.3 correctly uses determinant one and the inverse derivative bound; the rational affine-group character classification in 13.4 has a valid finite-factor argument; and the torus discussion in 12.7 correctly separates the unavoidable constant-mode obstruction from the reduced small-divisor equation.

The self-avoiding-walk entries preserve the ambiguity of the notebook's sampling law. The report likewise requires the law to be specified before assigning a modern exponent question. This does not currently overstate the source as posing the exact modern uniform-walk conjecture.

The reviewed fate narratives generally distinguish a modern reconstruction from a read theorem and retain the limitations of partial or thematic publication matches. No additional broad search or optional numerical testing was needed for this cross-review.
