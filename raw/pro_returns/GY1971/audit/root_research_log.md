# Central research and verification log

Status date: 9 November 2026. This log records observed source evidence and
search limits, rather than treating a failed search as a mathematical result.

## Archive chronology and boundaries

- Opened https://old.mccme.ru/gelfand/notes/all-links.html . Its catalogue places
  Dobrushin's `19-Feb-72` between Buchstaber's 12-Feb-73 and 26-Feb-73 entries.
  Direct record-286 and record-288 pages failed through the web reader.
- Visually read attached scan GELFAND-P000480: the heading clearly reads
  `19/II-73`, R. L. Dobrushin, on field theory. Both supplied transcriptions
  correctly give 1973. The catalogue error is not an error of translation.
- Visually read GELFAND-P000364: Kirillov's polarization/quantization exposition
  continues through this page. Supplied record229 span P358–360 is not its actual
  mathematical span. P358–359 carry over Perelomov material already indexed as
  1970-228.7–13; no fresh occurrence is created merely from overlapping scans.
- P477 is a tail from the preceding semester; P478–479 are Buchstaber12Feb1973;
  P480 is Dobrushin19Feb1973; P481 starts Buchstaber26Feb1973. Those surrounding
  talks are not reassigned to the requested heading record286 or to Dobrushin.

## Ptak supplemental search

Searches (both engines; English and Russian): `Ptak critical exponent minimum
dimension liminf Banach spaces`, `critical exponent Banach lp`, `critical
exponent Ptak minimum`, `critical exponent Kirzhner`, `critical exponents
Tabachnikov`, `критический показатель Птак минимум`, `критические показатели
норм наименьш`, `Ptak critical exponents M(n)`, and a recent-results search
for `Ptak critical exponent 2025` (730-day filter). Results predominantly
concerned fixed spaces, matrix norms, polynomial norms, and different notions
of exponent. No verified answer to the exact minimum-over-all-norms asymptotic
question was obtained by these searches. This is an evidence limitation, not
certification that the problem is open.

Actually opened and read:

- https://www.mathnet.ru/eng/smj4558 and its full PDF
  https://www.mathnet.ru/php/getFT.phtml?jrnid=smj&option_lang=eng&paperid=4558&what=fullt .
  Kirzhner–Tabachnikov1971, Theorem1 and Corollaries2–3: finite critical exponent
  for unit spheres contained in an algebraic set avoiding0, including rational
  p in real and complex finite-dimensional ell-p spaces. Received14Jan1970;
  Russian issue May–June1971. This predates Ptak's September1971 talk.
- https://www.dml.cz/handle/10338.dmlcz/117923 and full primary PDF
  https://dml.cz/bitstream/handle/10338.dmlcz/117923/CasPestMat_101-1976-4_10.pdf .
  Ptak1976, sections1–2: isometric parts and the Hilbert-space critical exponent.
  Received17Nov1975. This is a later proof of an already published result.
- https://dml.cz/bitstream/handle/10338.dmlcz/127297/CzechMathJ_46-1996-2_15.pdf .
  Vavrin1996 interview with Ptak, pp347–348 and bibliography: motivation and
  quantitative extremal problem, no verified resolution of M(n) from this text.
- https://perenflo.com/publications confirms authors, year, volume, and pages
  of Enflo–Gurarii–Lomonosov–Lyubich1995. The journal/DOI full-text route failed.
  Search snippets concern a DIFFERENT orbit-length exponent allowing arbitrary
  operators, so they do not establish a lower bound for the notebook's
  contraction exponent. Not used as a solution of M(n).

## Dyson coefficient check

Opened primary paper mirror
https://www.marktomforde.com/academic/miscellaneous/images/Missed-Opportunities-Dyson.pdf .
Pages636–637, equations(1)–(3), confirm the leading factorq and the exact
five-variable lattice sum. Page635 footnote gives lecture and receipt17Jan1972;
publication September1972. Code check_dyson.py compares three exact algorithms.
The transcript's missing leading factor is independently exposed by the
constant term. The finite lattice computation is an audit, not a proof of
Dyson's all-coefficient identity and not a solution of the eta^26 question.

## Independent proof review: full de Rham grading

The reviewer for records 244–258 checked the graded-loop proof, endpoint kernels,
the domain-preserving unitary involution, and gluing compatibility. It found no
error. A separate suspension calculation gives Gamma P Gamma = -P*, hence
index(P)=0, with a unitary connection preserving the grading. This applies to
the full de Rham operator and degree-preserving unitary flat twists. It cannot
be transferred to an unspecified restriction such as the odd signature operator.
Root also opened the full Atiyah–Patodi–Singer III paper at
https://webhomes.maths.ed.ac.uk/~v1ranick/papers/aps003.pdf and read section 7,
Theorem 7.4 and the following suspension discussion on printed pages 94–95.
The first page dates receipt to 24 January 1975 and publication to 1976.

## Godbillon–Vey and eta-power fate checks

- Opened Thurston's original paper at
  https://scispace.com/pdf/noncobordant-foliations-of-s-3-46sv22bo5y.pdf .
  The theorem on printed page 513 gives GV(F_P)[S^3]=4*pi*Area(P). It distinguishes
  concordance invariance from the false assertion of arbitrary deformation
  invariance. Communicated 15 December 1971; published July 1972.
- Opened Monastyrskii's full 1980 article through
  https://www.mathnet.ru/eng/rm9350 and its English full-text link. The appendix
  on printed pages 200–201 identifies the eta^26 identity with dual-root data for
  F4. The historical question is not presented as still open.

## Exact mass calculation

Opened https://arxiv.org/pdf/math/0012231 (King, v3 dated 17 October 2001).
Section 2, preprint page 3, gives the even-unimodular mass formula. Section 6,
pages 16–17, explicitly compares ceil(2m_32)=80,618,466 with the refined lower
bound 1,162,109,024 and states Corollary 17. The attached notebook's rough count
is thus recognizable only with the positivity/evenness/genus qualifications and
as a lower bound, not a class number.

code/check_mass.py evaluates the classical formula with exact rational
arithmetic. Bernoulli recurrence and the Stirling-number finite sum agree through
B_30; rank-8 and rank-16 reciprocal-automorphism checks agree. The rank-32
ceiling is exactly 80,618,466. The output retains the full rational mass. This
computational audit claims no new mass formula or complete classification.

The records 244–258 reviewer independently checked this code and argument:
the two Bernoulli formulas, the normalization n=8k, the rank-16 automorphism
orders (including the half-spin gluing issue for D16+), the exact ceiling
expression, and the direction of the class-number inequality. No error found.

## Quillen circulation before the 1972 journal article

Searching backward from the 1972 Annals paper exposed the Nice ICM1970 address.
The official full volumes (47MB and 73MB) exceeded the web reader's size limit;
the individual historical MathUnion article URL timed out and then failed.
The full primary-author text was successfully opened and read in the OCR mirror
https://paperzz.com/doc/7814310/cohomology-of-groups---international-mathematical-union .
Section 2, pp49–50, already gives the Lang/étale spectral sequence, the
classifying topos, and the odd-prime finite-GL cohomology formula with
r=ord_l(q). Section 3, pp50–51, states the plus construction and Brauer lift;
Theorem 1 identifies the Adams-operation fibre; Theorem 2 gives the algebraic
closure and Frobenius action. The 1972 seminar occurrences of these already
announced results are E, not B just because the full Annals paper came later.
The primary text is cited as quillen1971cohomology. The volume's 1971 publication
date was separately checked in the author-hosted full Grayson2013 paper,
https://www.graysonfamily.org/dan/Papers/qs-published-final.pdf, reference 57.
That paper's section 4 also explicitly dates the announcement to work of1969–70.

## Independent Dyson code review

The reviewer for records 259–288 independently checked the enumerator and both
coefficient algorithms. Residues (1,2,3,4,0) label the five coordinates, so no
5! division is appropriate. The zero-sum constraint, exhaustive square-root
bound, denominator 288, ten-factor Vandermonde sign, product truncation after
the leading q, and logarithmic-derivative recurrence were all checked; no error
was found. Both finite runs agree. No all-n proof is inferred from that agreement.

## Independent cusp-ring diagnostic

Root opened https://arxiv.org/pdf/1903.08295 and read Theorem A on PDF page 1,
including the hypotheses that the coefficient algebra is perfect over F_p and
the two exponents are coprime. The displayed big-Witt-vector quotient applies
without requiring p to be prime to both exponents. The records 229–243 reviewer
separately checked this theorem, Weibel's author-hosted Chapter IV, the positive
grading contraction and the split relative-to-absolute K-theory sequence. It
found no error for any prime, including 2 and 3. The full independent derivation
is retained in code/source_fragments/a/independent_checks.md. This is an editorial
counterexample to the notebook's domain hypothesis, not an original K-group
calculation and not a C/D research development.
