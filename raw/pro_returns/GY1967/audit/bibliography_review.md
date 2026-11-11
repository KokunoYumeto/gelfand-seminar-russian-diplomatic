# Independent bibliography audit: fragments a and b

Reviewer: `/root/records_155_166`. Date: 9 November 2026. Scope: read-only comparison of `fragments/a/references.bib`, `fragments/b/references.bib`, their research audits, and `source_kit/references_cumulative.bib`. No a/b or root integration files were edited.

## Result and exact key recommendations

**No accidental new-key duplicate work, conflicting publication metadata, or demonstrated DOI/URL identity mismatch was found in a/b. No replacement citation key is required.** There are28 entries in a and21 in b. Seven entries correctly reuse cumulative keys; their author/title/year/publication/DOI/URL fields match the cumulative entries exactly.

| Fragment | Incoming key | Canonical key to retain | Recommendation |
|---|---|---|---|
| a | `kirillov1962unitary` | `kirillov1962unitary` | Keep; merge once. |
| a | `smale1967dynamical` | `smale1967dynamical` | Keep; merge once; distinguish this fragment’s metadata opening from the earlier cumulative full-text opening. |
| a | `spatzier2016rigidity` | `spatzier2016rigidity` | Keep; merge once. |
| b | `grothendieck1957homological` | `grothendieck1957homological` | Keep the first-installment citation and its explicit note. |
| b | `gelfandkirillov1966corps` | `gelfandkirillov1966corps` | Keep; do not replace by the distinct Doklady announcement key. |
| b | `dumas2011invariants` | `dumas2011invariants` | Keep; merge once. |
| b | `lauritzenthomsen2026duality` | `lauritzenthomsen2026duality` | Keep; the added annote records current reading scope rather than a different work. |

All other a/b keys identify works absent from the cumulative bibliography. There is no duplicate work shared between a and b. The related `gelfandkirillov1966fields` in the cumulative file is a **different publication**, Doklady167(3),503–505, rather than the IHÉS31,5–19 article. Similarly `mumford1965picard` is not the cumulative GIT book `mumford1965invariant`, and `hormander1965l2` is neither `hormander1965pseudo` nor `hormander1971fourier`. These must not be conflated by author/year matching.

## Duplicate keys already present in the cumulative file

The cumulative file has141 physical entries but133 unique keys. These eight keys each appear twice:

- `kohnnirenberg1965algebra`
- `malgrange1966ideals`
- `boardman1967singularities`
- `arnold1968singularities`
- `mather1969stability`
- `mather1970topological`
- `mather1971nice`
- `hormander1965pseudo`

**Exact action:** retain each key unchanged and emit only one entry for it. There is no conflicting identity metadata to reconcile. Six duplicate pairs are identical in all parsed fields. The Malgrange and Arnold pairs differ only in `annote`: the later versions give more precise reading-scope statements and should be preferred or combined. For Malgrange, the later annote clarifies that the exact finite-module formulation was read in Arnold1968, rather than implying full independent theorem checking in the book. Do not silently re-promote that annotation to a stronger verification claim.

The a/b repeats of existing cumulative entries differ only in added or updated `annote` for Kirillov1962, Smale1967, Spatzier2016 and Lauritzen–Thomsen2026. For Smale the cumulative prior full-text reading and the current fragment’s failed full-text retrieval can both be true; preserve their distinct provenance rather than treating them as a publication conflict.

## Targeted metadata checks

Only concrete apparent discrepancies were reopened; there was no wholesale literature re-search.

1. **`nilsson1964growth`: retain1964 and the present key.** The publisher page at https://link.springer.com/article/10.1007/BF02591142 was independently reopened as `turn150view0`. It expressly dates publication and the issue to October1964, volume5,pp463–476, with the exact DOI. The familiar1965 citation in other bibliographies is already disclosed in a’s audit. No replacement by a guessed `nilsson1965growth` is recommended.

2. **`grothendieck1957homological`: retain119–183 with the installment note.** https://www.jstage.jst.go.jp/article/tmj1949/9/2/9_2_119/_article independently reopened as `turn150view1`; it confirms1957,volume9,issue2,pp119–183 and DOI10.2748/tmj/1178244839. The complete paper’s119–221 span is a different bibliographic scope across installments. The existing entry already explains this; replacing the pages alone while keeping the issue2 DOI record would lose that distinction.

3. **`sinai1968markov`: retain the English C-diffeomorphisms title.** https://www.mathnet.ru/eng/faa2756 independently reopened as `turn150view2`; publisher metadata gives that title, Russian64–89, translation61–82, DOI10.1007/BF01075361 and receipt20October1967. The Russian manuscript’s Cyrillic U is explained in a’s annotation. No DOI, translation-pagination or title mismatch exists.

4. **`schmudgen2018moment`: the linked abstract supports the mathematical sentence, but its locator should be Abstract.** https://arxiv.org/abs/1712.06360 independently reopened as `turn152view0`. It states cylinder-measure representation under stronger positivity or Carleman conditions and gives first submission18December2017. The fragment’s metadata correctly distinguishes circulation2017 from publication2018. Its full-text retrieval was not successful, so a citation to “Introduction” is more specific than its documented access. The attempted independent DOI open at https://doi.org/10.4310/ARKIV.2018.v56.n2.a14 failed (`turn153view0`); this is an access failure, not evidence that the DOI is wrong.

5. **ArXiv versus journal identifiers are not mismatches.** The Schmüdgen, Premet, Infusino and Lauritzen–Thomsen URLs refer to author preprints while their entries may carry journal or arXiv DOIs. Distinct URL strings alone do not identify distinct works. In particular `2610.15469v2` matches the base DOI10.48550/arXiv.2610.15469; the explicit version belongs in the URL/howpublished field, not in a newly invented key.

## Verification-label audit

The format defines `note={verified}` as “URL or DOI opened”; it does **not** mean every original proof was read. This distinction is respected in the bibliography annotations. No entry should be downgraded merely because it was verified through publisher metadata rather than full text, provided its item-level statement does not claim stronger access.

### Fragment a

The complete `research.md` became available during this audit and was read. Its28-source URL/tool-ID list covers all28 bibliography entries. Metadata/indirect limits are explicit for Schwartz1965, Kirillov1962 in this fragment, Smale1967 in this fragment, and the limited Nilsson original reading. Full primary results used instead are named: Alikhani-Koopaei for Schwartz, Spatzier for the modern Anosov statements, Leray for Nilsson’s period theorem. Therefore the `verified` flags are supported by the saved audit; no key or flag replacement is recommended.

Items with `verification=read the result` and more than one source need to be read with their explanatory fate fields. For example1967-139.4 reads Leray’s exact theorem while expressly limiting the Nilsson claim, and1967-140.3 reads Spatzier’s theorem rather than claiming fresh access to Smale’s original proof. These are not contradictory verification labels.

### Fragment b

At the start of this audit, `research.md` was still a six-source checkpoint even though the bibliography had21 entries. This was a real **documentation gap**, not evidence that the other sources had not been opened. Its owner confirmed that the full audit was being saved and that Grothendieck and Schmüdgen were metadata/abstract-only, while the other principal cited results were read. All21 entries already have source URLs, and almost all have detailed annotations.

The verification risks requiring care are:

- **1967-142.3:** change `\citet[Introduction]{schmudgen2018moment}` to `\citet[Abstract]{schmudgen2018moment}`. The exact content is in the opened abstract. The key and `note={verified}` remain unchanged. This recommendation was sent directly to b’s owner.
- **Grothendieck locators in1967-143.7 and1968-152.4–152.6:** Grothendieck’s original full text was not read in this task. The accompanying Mumford pages are the read-result evidence. Existing `annote` correctly limits Grothendieck verification; the chapter must not summarize the combined `read the result` field as proof that every cited original was read. No key replacement is required. If additional prose is needed, say “the stated application was read in Mumford; Grothendieck provides the bibliographic homological framework.”
- **Mumford/Premet checkpoint wording:** the initial audit said visual/full-text reading was pending, while final bibliography annotations say it was completed. Preserve the completed audit update rather than leaving both states unexplained in the final package.

## Reproducible comparison

`bibliography_audit.py` parses the three files without mutating them and writes `bibliography_parsed.json` and `bibliography_comparison.txt`. It compares keys, exact DOI/URL identities, normalized titles and all publication fields; potentially similar work families were then checked manually. These files are saved under fragment c. This audit does not claim independent full-text re-verification of all49 a/b works.
