"""Render the final evidence log from audited reference records and manual limits."""
from pathlib import Path
import re

root = Path(__file__).resolve().parent
bib = (root / 'references.bib').read_text()

def field(entry, key):
    m = re.search(r'\b'+re.escape(key)+r'\s*=\s*\{', entry)
    if not m:
        return ''
    start = m.end()
    depth = 1
    for i in range(start, len(entry)):
        if entry[i] == '{':
            depth += 1
        elif entry[i] == '}':
            depth -= 1
            if not depth:
                return entry[start:i]
    raise ValueError(key)

parts = ["""# Records 545–555: final research and provenance log

**Audit date: 11 November 2026.** The attached Russian diplomatic transcription controls the English translation; all thirteen scans GELFAND-P001001 through P001013 were visually inspected. Mathematical corrections were not mislabelled as better readings of faithfully copied signs. Actual heading order: 545, 546, 547, 549, 548, 550, 552, 553, Fuchs intervention 551, 554, 555. Kirillov 556 begins on P001014. Overlapping catalog windows are not independent content boundaries.

## Sources, exact result locators and verification levels

The following entries reproduce the final audited bibliography annotations. **Verified means that the identified source was opened, not that every original proof was read.** Publisher metadata, author abstract, full theorem text, and an inaccessible original are distinguished separately. DOI values below identify attempted or opened routes as the annotations state.
"""]
for entry in re.split(r'(?m)(?=^@)', bib):
    m = re.match(r'@\w+\{([^,]+),', entry)
    if not m:
        continue
    url, doi, note, annote = [field(entry,k) for k in ['url','doi','note','annote']]
    parts.append(f"\n### {m.group(1)} — {note}\n\nURL: {url}\n")
    if doi:
        parts.append(f"\nDOI: https://doi.org/{doi}\n")
    parts.append('\n'+annote+'\n')

parts.append(r"""
## Additional opened chronology and metadata checks

- https://ag-schrader.userpage.physik.fu-berlin.de/schrader-publ.html — entry 34 identifies the 1981 Heisenberg Symposium and 1982 chapter. This is earlier circulation than the 1982 seminar and 1984 full convergence paper.
- https://link.springer.com/book/10.1007/3-540-11560-9 — print publication in 1982; do not use the chapter's 2005 digitization date as its original date.
- https://arxiv.org/abs/1005.2386 — Navarro–Navarro first submission 13 May 2010, last revision 20 December 2010, 2011 journal reference and authors checked.
- https://arxiv.org/abs/2310.18802 — Gawlik–Neunteufel v1 28 October 2023, v2 23 November 2023. Full preprint Theorem 4.1 and Corollary 4.3, pp. 16–17, were read; negative-Sobolev consistency for the densitized tensor does not mean convergence of stationary solutions. The publisher search extract at https://academic.oup.com/imajna/article/46/1/500/8093615 gives online 26 March 2025 and a 2026 issue. The item cites the theorem numbering of the full preprint actually read.
- https://www.mathunion.org/icm/proceedings — official entry for Vancouver 1974, volume I. After the web reader rejected the 55 MB file, the complete linked volume was downloaded locally and **all of McMullen's pp. 491–495 were read**. Pages 493–494 explicitly discuss lattice valuations and Ehrhart reciprocity. https://www.cambridge.org/core/books/abs/convex-polytopes-and-polyhedra/references/97B142345B729D5BC8B6B636E2809285, entry 218, independently checks title, pagination and year.
- https://ammann.app.uni-regensburg.de/preprints/alnv1/index.html — author page dates writing 19 November 2002 and update 26 November 2002, with 2004 journal metadata. The full preprint was read; its modified extended Weyl-algebra axioms are not treated as exact copies of Guillemin's inaccessible original.
- The 14 MB Kashiwara–Schapira volume was downloaded after the same reader size limit. **Theorem 9.2.3 pp. 164–165; Corollary 9.3.3 p. 166; Remark 9.3.4; Theorem 10.1.1 p. 174 and surrounding proofs were read.** The general equality of microsupport and characteristic variety is therefore verified from full text, not merely a catalog.
- https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/en/publishing-house/journals-and-series/studia-mathematica/all/143/3/111821/fonctionnelles-invariantes-et-courants-basiques — the opened publisher route for the Abouqateb–El Kacimi abstract, whose normalized canonical URL is used in the bibliography.

## Search routes and explicit limits

Routine author/title searches used the available second search engine; uncertain identifications, primary verification, and current status checks used system1. Primary targets included Math-Net, Numdam, arXiv, author university pages and bibliographies, publisher records, and the official IMU proceedings. Math-Net and zbMATH-related title searches did not supply a Soviet short announcement for these Western topology talks. The successful routes were backward references: ALNV to Guillemin, the McDuff author bibliography to her exact abstract, Milnor's full article to the older Sah–Wagoner/Steinberg work, and the congress volume to McMullen. No unsuccessful search is evidence of permanent nondevelopment.

Live MCCME pages for 545 and 548–551 could not be read through the web reader. Attached catalog and actual scans remain the primary source. No bibliography entry pretends the live archive pages were verified.

For the Friedlander–Milnor conjecture, searches on 11 November 2026 included `"Friedlander-Milnor conjecture" 2025 2026` (system1, recency 730 days), `"Milnor" "Lie groups made discrete" conjecture solved`, and the Dranishnikov title. Search returned 2008 text with misleading recent crawl dates, a renewed 2021 Amrani proof claim, historical Morel/Wendt discussion, and a 2025 primary publisher extract. MathOverflow was used only to locate primary work, not to certify 2026 status. Amrani's abstract and version history were opened: v3 was withdrawn in 2016 and v4 renewed the claim in 2021. No independently verified proof or journal acceptance was obtained. Dranishnikov's original `/pii/` and `/abs/pii/` routes both returned 403; the primary search extract contains Introduction Conjecture 1.1 and concerns more general abelian topological groups. This is a status lead, not a verified full proof or a counterexample among Lie groups. The general exact question therefore retains C with explicit limits.

For Haefliger, searches combined his name with PSL2(Z), SL(2,Z), projective circle, smooth functions, coboundaries, coinvariants, invariant distributions, and French `modulaire`, `fonctions` and `feuilles minimales`. No exact primary theorem resolving the displayed smooth two-generator equation was found. Haefliger's 1980 title is an inaccessible related lead; the later invariant-functional result has compact-group hypotheses. The source explicitly says leaves are minimal submanifolds of a Riemannian manifold, so geometric minimality is not confused with every leaf being dense. No explanation of why the question remained open or was neglected is asserted without evidence.

The source's “Brin, about 1946” attribution remains unresolved. Scan inspection and searches combining the name with polyhedral curvature, solid angles, Euler characteristic and seminar chronology did not identify an exact reference. The date is not silently changed and no particular Brin is guessed. Ginzburg's initials are catalog provenance: the manuscript gives only the surname. MacPherson explicitly offers proposed titles; the record is a plan, with three distinct mathematical topics retained.

## Previous-index exact recurrence check

The prior index was searched for Lovelock, Regge, Friedlander, made discrete, discretization, coinvariants, coboundaries, Haefliger, Pontryagin, second/lower-order equations and curvature actions. **No exact pre-existing problem ID was found. New IDs are GP-1981-20 through GP-1981-23; none is reused.**

Thematic links: 1975-394.5 and 1976-407.13–14 discuss Einstein equations; 1979-465.24 discusses Euler/Pontryagin integrals. 1971-250.4 contrasts discrete and topological general linear groups; 1971-257.3 concerns acyclic coinvariants in a different K-theoretic construction. GP-1974-14 is a current-group representation problem, not the modular-circle equation. 1976-415.1 and .6 give Young-diagram and path background, not this beta-number complement identity. 1980-524.2 is symplectic-reduction background. None was merged merely because of similar keywords.

## Independent theorem and computational checks

The Haefliger **continuous** theorem has a complete proof in `development.tex`. Absence of invariant probabilities, weak-star compactness and lower semicontinuity give a positive total-variation defect. Taking absolute variation passes it to signed measures. Hahn–Banach plus an explicitly bounded convergent residual series gives exact continuous solutions. An independent team audit reproduced the argument and all norms, and gave the alternative Banach closed-range proof. A strict epsilon-prime below epsilon avoids a boundary-attainment issue. No numerical epsilon, linear right inverse, or smooth regularity theorem is claimed. The smooth question still requires distribution-level obstruction analysis and derivative/closed-range estimates; smooth density alone cannot imply surjectivity.

The program `code/check_partition_and_metric.py` was run successfully. Independent row-list and beta-subset enumerations agree on 251 partitions across rectangles through 4, and 3431 across the 49 rectangles through 6. The wrong source generating function fails a deliberate one-box negative control. Independent symbolic Gram Jacobians for n=1,…,5 reproduce the missing product of lengths; a positive-definite orthonormal example and the one-edge density provide additional separate checks. Complete code and output are saved. Finite enumeration is not presented as an unbounded proof.

## Completion and packaging

11 records; 60 items; 4 new problems; 41 correction/provenance rows; 25 references, of which 20 have an opened verified source and 5 inaccessible originals are marked unverified. Classes: A13, B2, C4, D0, E36, F5. Every item has an area. Root integrates and builds the single chapter. **Exclude `source_cache/` from the ZIP:** it contains 68 MB of downloaded primary evidence, not original deliverable work. Include the data, development, code and its output, and final log/report as appropriate to the root package.
""")
(root / 'research_log.md').write_text('\n'.join(parts))
print('Final research log written')
