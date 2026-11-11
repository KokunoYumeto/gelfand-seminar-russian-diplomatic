"""Final source and typesetting audit; run through author_early.py."""
from author_helpers import *

byid={x['id']:x for x in I}

# Names with accents are Unicode, not Python-escaped TeX accent commands.
for key,(kind,fields) in R.items():
 for field,value in list(fields.items()):
  if isinstance(value,str):
   fields[field]=value.replace("'{e}",'é').replace("'{E}",'É').replace(r'\`e','è')
R['griffiths1970periods'][1]['annote']='Full author-hosted text read, Theorems 3.1 and 4.3 and Sections 2--4. Invited lecture 29 August 1968; received 18 September 1969; March 1970 issue. These three dates are stated on the first page.'

ref('melamed1965formal',author='Melamed, V. B.',title='On formal solutions of certain nonlinear equations',journal='Sibirskii Matematicheskii Zhurnal',volume='6',number='1',year='1965',pages='165--177',url='https://www.mathnet.ru/rus/smj5123',annote='Russian full text read: analytic Banach-space equation (1), formal Puiseux series (2), and Theorems 1--2 on p. 175. Received 13 January 1964. This is a qualified precursor, not a verified priority claim for multivariable Artin approximation.')
ref('sakellaridisndcompact','misc',author='Sakellaridis, Yiannis',title='Representations of compact groups',year='n.d.',howpublished='Author-hosted Automorphic Project course notes',url='https://math.jhu.edu/~sakellar/automorphic-files/representations-compact.pdf',annote='Accessed 9 November 2026. Proposition 4.5 p. 5 and Theorem 5.1 p. 6 read; Haar probability normalization and the compact-group generality are explicit. No publication date inferred from search crawl dates.')
ref('gelfand1960elliptic',author='Gel\x27fand, I. M.',title='On elliptic equations',journal='Russian Mathematical Surveys',volume='15',number='3',year='1960',pages='113--123',doi='10.1070/RM1960v015n03ABEH004094',url='https://www.mathnet.ru/eng/rm7239',annote='Russian original: Uspekhi Mat. Nauk 15(3), 121--132; received 14 January 1960. Full English translation read, especially Section 2 pp. 119--123. Thematic background only for the underdetermined 1970 elliptic fragment.')

byid['1969-177.4'].update(
 statement=r'The first citation is V.~V. Pokornyi and P.~P. Rybin, on stabilization of a scalar formal implicit-function procedure. The second is identifiable as V.~B. Melamed\textquotesingle s 1965 paper. For its analytic equation in a complex Banach space, with compact linear part and one complex parameter, Theorem 1 says that all formal Puiseux solution branches converge near zero exactly when their set is finite; Theorem 2 gives a finite nonempty set of convergent branches if the zero solution at parameter zero is isolated.',
 fate=r'\citet[pp.~169--172]{pokornyirybin1960formal} was received in December 1958; \citet[Theorems 1--2, p.~175]{melamed1965formal} was received 13 January 1964 and published in 1965. Both are verified earlier contributions. Their stated scalar or one-parameter convergence conclusions do not identify the notebook\textquotesingle s suggested priority comparison with the arbitrary finite-jet approximation theorem of \citet{artin1968analytic}.',
 reconstruction=r'The precise earlier statements are supplied from the papers. Their identification does not recover an unstated equivalence of hypotheses or conclusions with Artin approximation.',
 present_status='As of 9 November 2026: both earlier references are identified and their relevant statements checked; the broad priority comparison remains too imprecise to certify.',
 refs=['pokornyirybin1960formal','melamed1965formal','artin1968analytic'])

byid['1969-180.2']['present_status']=r'As of 9 November 2026: the bounded \(C^1\)/smooth strong-continuity existence variant is proved in this chapter; no verdict is asserted for every possible interpretation of the unspecified 1969 group.'
byid['1969-183.2']['fate']=r'These are the standard compact-group Fourier norms used in the compact-group case described by \citet[pp.~293--294]{russo1974fourier} and in \citet{hewittross1970abstract}. The missing root is a mathematical emendation, not an established reading of the handwriting.'
byid['1969-183.3'].update(
 fate=r'This is the classical compact-group Plancherel theorem. The exact probability-Haar formula was checked in \citet[Theorem 5.1, p.~6]{sakellaridisndcompact}; the older book treatment is \citet[Theorem 28.43]{hewittross1970abstract}. Neither later exposition is asserted to be the origin of the theorem.',
 refs=['sakellaridisndcompact','hewittross1970abstract'],verification='read the result')
byid['1969-183.4'].update(
 fate=r'The finite-matrix-coefficient density statement was checked in \citet[Proposition 4.5, p.~5]{sakellaridisndcompact}. Together with the displayed \(L^1\)-to-operator-norm estimate it gives the recorded conclusion: first approximate by a finite Fourier polynomial, then bound every remaining coefficient by the approximation error. This is classical Peter--Weyl theory.',
 refs=['sakellaridisndcompact'],verification='read the result',development='annotated',reconstruction='The short approximation proof is supplied to make the precise operator-norm conclusion explicit.')

replacements={
 '1970-184.2':('Lemma 26.5.1','Lemma 10.17.2'),
 '1970-184.3':('Section 26.5','Section 10.17'),
 '1970-184.7':('Lemmas 6.17.1--6.17.2','Lemmas 6.17.1--6.17.3'),
 '1970-184.9':('Lemma 26.5.1 and construction following it','Lemmas 10.17.2 and 26.5.1'),
 '1970-184.11':('Lemma 26.5.4','Lemmas 10.17.6 and 26.5.4'),
 '1970-184.17':('Section 17.3','Lemma 6.31.6'),
 '1970-187.6':('Sections 6.2 and 6.7','Definition 6.3.1 and Definition 6.7.1'),
 '1970-187.8':('Section 18.1','Lemma 17.3.1, applied to the constant sheaf of integers'),
 '1970-190.2':('Lemma 26.7.4','Definition 17.10.1 and Lemmas 17.10.5, 26.7.1 and 26.7.4'),
 '1970-190.3':('Lemmas 26.7.1--26.7.4','Lemma 26.5.4 and Section 26.7'),
 '1970-190.5':('Lemma 26.5.1','Lemma 10.17.8'),
}
for ident,(old,new) in replacements.items():
 assert old in byid[ident]['fate'],(ident,old)
 byid[ident]['fate']=byid[ident]['fate'].replace(old,new)
byid['1970-184.7']['fate']=byid['1970-184.7']['fate'].replace('1970-187.6','1970-187.7')
byid['1970-188.1'].update(
 fate=r'Targeted English and Russian searches combining Gelfand, elliptic systems without lower-order terms and parity of solutions yielded no exact match. \citet[Section 2, pp.~119--123]{gelfand1960elliptic} studies homotopy invariants and indices of specified elliptic boundary problems, and discusses operators without lower-order terms. It is thematic background; it does not determine the missing operator or make the fragment an index-theorem question.',
 refs=['gelfand1960elliptic'],publication_match='thematic only',verification='read the result')
byid['1970-188.3'].update(
 fate=r'\citet[Section 2, especially pp.~120--123]{gelfand1960elliptic} gives a related topological research programme, including the Fredholm index as kernel dimension minus adjoint-kernel dimension. This is not a count of individual solutions modulo two. No exact parity theorem was located in the checked sources; the notebook direction remains unidentified.',
 refs=['gelfand1960elliptic'],publication_match='thematic only',verification='read the result')

P.extend([
 dict(id='GP-1966-13',title='Entire minimal-graph Bernstein problem',statement=r'For which dimensions \(m\) must every smooth entire solution \(u:\mathbb R^m\to\mathbb R\) of the minimal-surface equation be affine?',occurrences=['1966-114.6','1969-174.4'],status=r'As of November 2026: resolved. Every such graph is affine for \(m\leq7\); non-affine entire graphs exist for \(m\geq8\). The counterexamples were published in 1969 by \citet{bombieridegiorgigiusti1969minimal}. The later Russian translation is not the result\textquotesingle s discovery date.',status_date='2026-11',refs=['bombieridegiorgigiusti1969minimal']),
 dict(id='GP-1969-01',title='Irreducible representations of an interval current group',statement=r'After fixing the regularity and topology of a group of maps \([0,1]\to SU(2)\), classify its continuous irreducible unitary representations up to equivalence. Distinguish operator-norm continuity from strong continuity; the notebook specifies neither the map category nor this convention.',occurrences=['1969-180.1'],status=r'As of November 2026: partly developed, with an archival ambiguity. In the smooth compact-semisimple setting, norm-continuous irreducibles are finite evaluation tensors \citep[Theorem 4.11; group theorem 4.15 in the arXiv version]{janssensneeb2015norm}; preprint 2013, online 2014, print 2015. Positive-energy and measurable-current results impose other hypotheses \citep{janssensneeb2024positive,araki1970factorizable}. The checked literature does not supply a full strong-continuity classification for every interpretation of the notebook.',status_date='2026-11',refs=['janssensneeb2015norm','janssensneeb2024positive','araki1970factorizable']),
 dict(id='GP-1969-02',title='Interval support of an irreducible current-group representation',statement=r'In a specified continuous unitary representation category for \(SU(2)\)-valued interval currents, does there exist an irreducible representation nontrivial on currents supported in every nonempty open subinterval? Equivalently in the full-support case, no proper closed subset carries the representation in the sense recorded on P000291.',occurrences=['1969-180.2'],status=r'As of November 2026: the chapter proves existence for strong continuity on \(C^1([0,1],SU(2))\), with irreducibility also on the smooth subgroup and full interval support. This constructed representation has no strongly continuous uniform-topology extension. Smooth norm-continuous irreducibles instead have finite support \citep{janssensneeb2015norm}. The high-dimensional energy theorem does not apply to an interval, whose energy representation is reducible \citep{ismagilov1976unitary,ismagilov1981segment}. These are precise positive and negative variants; the unrecorded archival category and broader classification remain unresolved here. No historical novelty is claimed for the construction.',status_date='2026-11',refs=['janssensneeb2015norm','ismagilov1976unitary','ismagilov1981segment']),
 dict(id='GP-1969-03',title='Analytic approximation of formal solutions',statement=r'Given analytic equations \(F(x,y)=0\) over \(\mathbb C\) and a formal solution \(\widehat y(x)\) with the prescribed constant term, does every finite jet of \(\widehat y\) extend to a convergent solution of the same equations?',occurrences=['1969-175.3','1969-177.1'],status=r'As of November 2026: resolved affirmatively by \citet{artin1968analytic}, published December 1968. For every \(c\), a convergent solution can be chosen congruent to \(\widehat y\) modulo \((x)^c\). Raynaud presented the result at Bourbaki in June 1969; that exposition appeared in 1971 \citep[Theorem 1]{raynaud1969artin}. The given formal series itself need not converge.',status_date='2026-11',refs=['artin1968analytic','raynaud1969artin'])
])

# Evidence log: all URLs were opened and their stated locators inspected.
source('melamed1965formal','https://www.mathnet.ru/php/getFT.phtml?jrnid=smj&option_lang=rus&paperid=5123&what=fullt','equations (1)--(2), pp. 165--166; Theorems 1--2, p. 175','One-parameter analytic Banach-space equation with compact linear part; convergence of every formal Puiseux branch iff finitely many branches; isolated zero gives finite nonempty set. Not the full multivariable finite-jet approximation theorem.')
source('sakellaridisndcompact','https://math.jhu.edu/~sakellar/automorphic-files/representations-compact.pdf','Proposition 4.5 p. 5; Theorem 5.1 p. 6','Finite matrix coefficients dense in continuous functions; exact dimension-weighted compact-group Plancherel identity with Haar probability measure.')
source('sakellaridisndcompact','https://math.jhu.edu/~sakellar/','author homepage and Automorphic Project links','Authorship and hosting verified; PDF undated.','publisher metadata checked')
source('gelfand1960elliptic','https://www.mathnet.ru/eng/rm7239','bibliographic record','1960 original and translation; received 14 January 1960.','publisher metadata checked')
source('gelfand1960elliptic','https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=rus&paperid=7239&what=fullteng','Section 2 pp. 119--123, especially index definition p. 120','Thematic elliptic/topological programme, not an identification of the 1970 parity or solvability fragment.')
source('griffiths1970periods','https://publications.ias.edu/sites/default/files/periodsofintegral.pdf','p. 228 dates; Section 2 pp. 231--233; Theorem 3.1 pp. 235--236; Theorem 4.3 p. 238 and discussion pp. 238--239','1968 invited lecture and 1969 receipt precede seminar; quasi-unipotence, regular singularity, algebraic local system, logarithmic/Puiseux expansions and moderate growth.')
source('russo1974fourier','https://escholarship.org/content/qt65k902bf/qt65k902bf_noSplash_9be3e3ddbaa125102cfb74474d5305ad.pdf','Introduction and Theorem 1 pp. 293--294','Primary later statement of compact-open-subcharacter extremizers, explicitly attributing compact-group case to Hewitt--Ross; Kunze background. Presented 1971, received 1973, published 1974.')
source('hewittross1970abstract','https://link.springer.com/book/10.1007/978-3-662-26755-4','publisher record; Section 43 attribution read in Russo 1974','1970 Volume II publication. Its original proof of compact-group extremizers was not read; the claim is indirectly verified through Russo.','publisher metadata checked')
source('vanhove1951relations','https://www.persee.fr/doc/barb_0001-4141_1951_num_37_1_70660','publisher record and first page','1951 attribution; exact modern prequantization assertion verified separately in Kostant.','publisher metadata checked')
source('kostant1970quantization','https://link.springer.com/chapter/10.1007/BFb0079068','publisher chapter record','LNM170 (1970), pp. 87--208; the 1973 Russian translation read is not the first publication.','publisher metadata checked')
source('connes1994noncommutative','https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf','Chapter V, Section 1 beta, Theorem 8, p. 464','Central direct-integral decomposition into factors on separable Hilbert space; historical note distinguishes 1939 development from 1949 publication.')
source('mcduff1969uncountably','https://annals.math.princeton.edu/1969/90-2/p07','publisher issue date and bibliographic record','September 1969 publication precedes 6 October 1969 notebook report.','publisher metadata checked')
source('grothendieck1960ega1','https://www.numdam.org/item/PMIHES_1960__4__5_0/','publisher record','EGA I, IHES 4 (1960), 5--228, publication 28 January 1960. Full PDF over reader size limit; modern results read in Stacks.','publisher metadata checked')
source('steinberg1965regular','https://www.numdam.org/item/PMIHES_1965__25__49_0.pdf','definition p. 49; Theorems 1.5 p. 50 and 8.1 p. 70; Remark 8.7','Correct centralizer dimension r and fundamental-character differential criterion under simply connected semisimple hypotheses. Does not supply an ADE claim from the notebook fragment.')

stack_sources=[
 ('006D','Definition 6.3.1','Presheaves and morphisms as natural transformations.'),
 ('006S','Definition 6.7.1; Remark 6.7.2','Sheaf gluing, sheaf morphisms and the terminal value on the empty open.'),
 ('007X','Lemmas 6.17.1--6.17.3','Canonical sheafification, preservation of stalks and universal property.'),
 ('008C','Lemmas 6.21.1, 6.21.3--6.21.5 and intervening construction','Pushforward is a sheaf; inverse-image presheaf, sheafification, stalks and adjunction.'),
 ('009H','Lemmas 6.30.2, 6.30.6--6.30.7 and 6.30.9','Sheaves defined on an open basis and extension to all opens.'),
 ('00A5','Lemma 6.31.6','Extension by zero for abelian sheaves; adjunction and stalks.'),
 ('00CM','Definition 10.9.1; Proposition 10.9.3; Lemma 10.9.4','Localization of rings and universal property; zero-ring edge case.'),
 ('00DY','Definition 10.17.1; Lemmas 10.17.2, 10.17.6 and 10.17.8','Spectrum topology, radicals, principal opens and quasi-compactness.'),
 ('01HR','Lemma 26.5.1; Definition 26.5.3; Lemma 26.5.4','Affine spectrum, localization inclusions, structure sheaf, module sheaf and exactness.'),
 ('01I6','Lemmas 26.7.1, 26.7.4--26.7.7','Module-sheaf universal property, global recovery, affine equivalence and arbitrary sums.'),
 ('01BE','Definition 17.10.1','Quasi-coherence defined using arbitrary local free presentations.'),
 ('01BH','Lemma 17.10.5','Local free-presentation formulation of quasi-coherence.'),
 ('01JO','Lemmas 26.17.2--26.17.4 and 26.17.6','Affine fiber-product formula, compatibility with open restrictions and gluing.'),
 ('01KH','Lemmas 26.21.1--26.21.2; Definition 26.21.3','Affine diagonals, diagonal immersions, and separated morphisms.'),
 ('01AF','Lemmas 17.3.1, 17.3.3--17.3.4','Module-sheaf abelian category, left exactness and extension by zero.'),
 ('01DF','Lemma 19.4.1','Enough injectives for abelian sheaves; skyscraper-product construction.'),
 ('01DZ','Section 20.2','Derived-functor cohomology via injective resolutions.'),
 ('01EO','Lemmas 20.11.6 and 20.11.9','Acyclic-cover Cech comparison and basis criterion; hypotheses essential.'),
 ('01X8','Lemmas 30.2.1--30.2.2 and 30.2.6','Quasi-coherent cohomology vanishes in positive degree on affines; affine-cover Cech computation.'),
]
for tag,loc,evidence in stack_sources:
 source('stacks2026foundations','https://stacks.math.columbia.edu/tag/'+tag,loc,evidence)

# Correct accidental Python control-character escapes, without silently changing
# meaningful mathematical backslashes. Fail validation on any other controls.
def normalize(value):
 if isinstance(value,str):
  return value.replace('\textquotesingle',r'\textquotesingle').replace('compact-semisisimple','compact-semisimple')
 if isinstance(value,list): return [normalize(v) for v in value]
 if isinstance(value,dict): return {k:normalize(v) for k,v in value.items()}
 return value
for seq in [T,I,P,C,S]:
 seq[:]=[normalize(x) for x in seq]
for row in C:
 row['evidence']=row['evidence'].replace('previous_index.md',r'\nolinkurl{previous_index.md}')
 if row['place']=='classical admissible displacements':
  row['transcription_reads']=r'\(C^1(\Sigma)\)'
  row['should_read']=r'\(C^1(\overline A)\), with the trace inequality on \(\Sigma\)'
 if row['place']=='sphere two-form and primitive':
  row['transcription_reads']=r'\(\Omega=a\,dz\wedge d\bar z/(1+|z|^2)^2\), \(\omega=(a/i)(z\,d\bar z-\bar z\,dz)/(1+|z|^2)\)'
  row['should_read']=r'\(d\omega=(2a/i)\,dz\wedge d\bar z/(1+|z|^2)^2\); choose a consistent real symplectic normalization'
 if row['place']=='localization applied to all principal opens':
  row['transcription_reads']=r'\(0\notin S\) is required, followed by \(S=\{f^n:n\geq0\}\) for every \(f\)'
 if row['place']=='subregular centralizer condition':
  row['evidence']=row['evidence'].replace('SL_n',r'\(SL_n\)')
checkpoint()
