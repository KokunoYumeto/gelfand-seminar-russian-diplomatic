# Integrating editor's research and verification log

Research date: 10 November 2026. This log distinguishes successful access from failed retrieval. Search-result dates were not used as publication dates. The supplied Russian transcription and scans govern notebook readings; external papers govern later mathematical claims.

## Whole-packet provenance

The 30 records requested in the attachment are retained in source order. The earlier index already contains 1973-331.1–.4 and 1973-332.1. P000551 bears 25/III–74, while the supplied catalogue lists 25 March 1975. P000550 and P000552–P000553 are neighbouring 1973–74 material; they are accounted for in the boundary audit, rather than falsely attributed to the named records of this packet. Catalogue dates and archival evidence therefore need separate fields in a future format. This run preserves the requested 1974-prefixed IDs and explains the duplicate occurrences explicitly.

## Entire-function inverse-potential programme, P000567–P000568

Both Russian transcription and scan read first order of growth and not necessarily periodic. The displayed Riccati convention is chi = -i psi'/psi. No normalizations, admissibility conditions, reality, or global regularity class are stated. A precise global inverse theorem cannot be inferred from the phrase alone. Class F records this lack of a uniquely recoverable formulation; it does not mean that inverse spectral theory was undeveloped.

Searches (both search engines used, primary-source verification):

- “Gesztesy infinite genus limit stationary KdV equation entire functions F infinity R infinity”.
- “Gelfand entire functions first order growth potentials R P finite gap inverse spectral 1974”.
- “Marchenko Ostrovskii characterization spectrum Hill operator 1975 entire functions”.
- “Gesztesy Integrable Systems in the Infinite Genus Limit pdf”.
- “Marchenko Ostrovskii Theorem 5 1975 spectrum”.

Successful opens:

1. Marchenko and Ostrovskii (1975), Math-Net metadata, https://www.mathnet.ru/eng/sm3807. DOI 10.1070/SM1975v026n04ABEH002493. English full text opened through the page's PDF link: https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=3807&what=fullteng. Theorem 5.1 pp. 535–536 and its proof were inspected (retrieval references turn18view2, turn22view1, turn34view0). The introduction abbreviates the theorem number as 5; the displayed result is 5.1. Received 3 February 1975. This is a real-periodic, normalized inverse problem, not an arbitrary entire pair.
2. Gesztesy (1999), https://arxiv.org/abs/solv-int/9907009, and the author's full text https://arxiv.org/html/solv-int/9907009v1 (turn18view0, turn22view0, turn24view1–2, turn34view1). Submission history establishes 7 July 1999. The HTML's dynamic recompilation date is not the circulation date. Equation (2.10) verifies the finite-polynomial identity; Hypotheses 3.1–3.2 and Eq. (3.14) make clear how much extra structure the infinite-genus theory assumes. The archive cites the verified preprint version; no journal date was inferred from an unverified secondary listing.

Access limitations: the initial cached Math-Net hash PDF URL redirected to the home page; a fresh publisher PDF link worked. Direct arXiv PDF retrieval failed, but the full HTML version worked. The putative journal DOI 10.57262/die/1356123242 did not open, and an old author-CV URL returned 404; neither was counted as successful verification. No Class D assertion is based on any failed retrieval.

## Independent mathematical audit

`root_audit.tex` proves a local necessary-and-sufficient compatibility criterion, common-factor invariance, and two order-one examples. These are explicitly editorial verification notes, with no claim of novelty or of solving an unspecified global problem. The squared-eigenfunction identity is derived both from the Riccati formula and independently from a pair of solutions and their constant Wronskian.

`root_code/check_spectral_compatibility.py` uses only the Python standard library. It checks the cleared polynomial identities exactly over the rationals, then repeats a sign-sensitive nonconstant example at sixteen rational (x,E) values. All checks pass. An initial attempt to use SymPy found that dependency unavailable; the final reproducible check has no such dependency. Finite checks are not used to infer a theorem.

The remaining issue is formulation: choose the energy variable, remove common factors, fix spectral zeros/divisors and realness, then control high-energy behaviour and global continuation. No new open problem was manufactured from these missing hypotheses.
