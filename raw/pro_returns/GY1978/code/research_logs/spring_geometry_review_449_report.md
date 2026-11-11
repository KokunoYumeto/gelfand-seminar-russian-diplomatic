# Independent review: P000807 and report prose

Date: 2026-11-10. Reviewed the full P000807 Russian and English transcript page, original PNG, `work/physics_autumn/449_items.json` occurrences13–15, and `work/root/make_report.py`. No peer file was edited.

## Mathematical findings

**449.14 passes.** For u(r)=(1+r²)^(−1), direct four-dimensional radial integration with sphere measure2π² gives ∫u⁴=π²/6 and ∫|∇u|²=4π²/3. The quotient of the squared latter integral by the former is32π²/3. Nonzero equality profiles belong to the homogeneous energy space but notL²: their squared radial integrand behaves as2π²c²/r. The scan displays the same constant and equality profile. The primary Talenti1976 paper was independently opened at https://math.jhu.edu/~js/Math646/talenti.sobolev.pdf; its main theorem and Eqs.(1)–(3) support the specialization. The inequality also holds forH¹ functions, but no nonzero equality profile lies there; the item's intended homogeneous-space emphasis is sound.

**449.15 passes, with a useful convention clarification.** Define Δ=Σ_j∂_j² explicitly. Exact radial differentiation gives

Δ[c/(r²+ρ²)]+[c/(r²+ρ²)]³ = c(c²−8ρ²)/(r²+ρ²)³.

Thus c=√8ρ gives exactly the recorded focusing equation. Variation of ∫(1/2|∇φ|²−1/4φ⁴) gives−Δφ−φ³, so the signs agree. For this bubble both ∫|∇φ|² and∫φ⁴ equal32π²/3, and the action is8π²/3. The scan clearly marks the Yang–Mills attribution as Zakharov's insertion. No gauge ansatz is given; retaining F for that identification is warranted. The scalar bubble does not establish the missing Yang–Mills reduction.

**449.13 is correctly identified as a historical method, but its statement can be narrowed.** Independently opened and read the primary Lipatov1977 paper, especially§§2–4, at https://www.jetp.ras.ru/cgi-bin/dn/e_045_02_0216.pdf. It explicitly uses contour coefficient extraction, negative-coupling saddles and collective coordinates. Its§4,p221 distinguishes n=4,D=4 because skeleton diagrams and diagrams with simple one-loop insertions contribute comparably. The authored reconstruction already says this is not a constructive proof; nevertheless “for a specified ... perturbative functional ... saddles ... control factorial growth” can be read too universally. Suggested replacement: “In Lipatov's regulated, renormalized scalar φ⁴ calculation, negative-coupling saddles yield the formal factorial large-order contribution; collective coordinates, fluctuation determinants and the prescribed renormalization determine powers and prefactors.” This describes the identified calculation without asserting saddle dominance for arbitrary functionals or a continuum existence theorem.

The beta-function sign claim is correct. It can be made exact: with t=log(Λ/μ²), and cutoffΛ and bare coupling fixed, β=dλ/dlogμ impliesψ=dλ/dt=−β/2. There is a factor of two in addition to the opposite sign. No numerical asymptotic coefficient or unrecorded error bound should be added.

The numerical/algebraic checks above were executed independently with SymPy and also derived directly by the radial formula Δf=f″+3f′/r. They agree.

## Report findings

Two definite wording changes are needed in the web chronology paragraph:

1. Trépreau's2006 publication is a **book chapter** in *Inspired by S. S. Chern*, Nankai Tracts11,399–433, not a journal version.
2. “The primary correction and proof were read” overstates the recorded read level. The spring researcher read Chern–Griffiths correctionpp78–79 and Trépreau§§1.1–1.5,2.1–2.4, including exact Theorems1.1/2.4 and the rank-bound proof. The complete algebraization proof was not independently audited. Suggested replacement: “The primary correction and the exact statements and hypotheses of Trépreau's theorems were read; the complete algebraization proof was not independently audited.”

Otherwise the spring chronology is correct:1978 original assertion;1981 normality restriction and two acknowledged defects;4August2005 first preprint;2006 unrestricted theorem publication. The exact range n≥3,d≥2n and general-position/regular holomorphic qualifications are preserved in the occurrence data.

Coverage and count cross-checks passed: exactly54 source PNGs, preciselyP000786–P000825 andP000829–P000842;52 belong to main-year assigned/source-established records andP000841–P000842 are Kallosh next-year boundary evidence. The fifteen delivered records comprise the fourteen commissioned entries plus457Fuchs. Records451/452 can remain zero-occurrence structural entries. Spring contribution remains43 items:38E,1B,4F, with source spans830–833,834–836,837–840. The delivered spring occurrence IDs/counts agree with their final author files. The report's cumulative-bibliography statistic was recomputed:896 entries,749 unique keys, exactly as stated.

The report's description of the independent contact, rationalR and Ising checks agrees with the saved proofs, code and reciprocal peer reviews. The tensor asymptotic counterexample must retain its nonzero-growth/unrestricted-boundary scope; the spring files already do so. The same-session assignment of the undated Zamolodchikov intervention is an editorial reconstruction, as the talk summary says; the directly observed speaker change and continuation are not in doubt.
