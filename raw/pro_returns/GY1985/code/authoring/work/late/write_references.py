"""Write the independently checked bibliography and source audit for records 663--666.
The URL log records what was opened, not blanket proof verification.
"""
import json,re
from pathlib import Path
HERE=Path(__file__).resolve().parent
cum=json.loads((HERE.parent/'code/cumulative_keys.json').read_text())
entries=[]; sources=[]

def add(key,kind='article',scope='publisher metadata checked',locator='',**fields):
    fields['note']='verified'
    fields['annote']='Checked 11 November 2026. '+scope+'. '+locator
    entries.append('@'+kind+'{'+key+',\n'+''.join('  '+k+' = {'+str(v)+'},\n' for k,v in fields.items())+'}\n')
    sources.append(dict(key=key,checked='2026-11-11',verification=scope,locator=locator,
                        url=fields.get('url',''),doi=fields.get('doi','')))

def reuse(key,scope,locator):
    e=cum[key]
    # Nested-brace fields are left intact; only append our distinct audit field.
    e=e.rstrip()[:-1].rstrip().rstrip(',')+',\n  audit = {Checked 11 November 2026. '+scope+'. '+locator+'},\n}\n'
    entries.append(e)
    url=re.search(r'url\s*=\s*\{([^}]+)\}',e)
    sources.append(dict(key=key,checked='2026-11-11',verification=scope,locator=locator,url=url.group(1) if url else ''))

reuse('polyakov1981quantum','read the result','Original four-page article, especially scalar determinant and Weyl anomaly. Formal path-integral status retained.')
reuse('belavinpolyakovzamolodchikov1984infinite','read the result','Section 2, equations (2.12)--(2.21), stress tensor and Schwarzian transformation; received 22 November 1983.')
reuse('shiota1986characterization','publisher metadata checked','Publisher landing page and bibliography; 1983 Kyoto xerox notes are an earlier circulation record, not the journal date. Exact theorem is checked through Krichever 2006, Introduction.')

add('dubrovinkrichevernovikov1976schrodinger',author='Dubrovin, B. A. and Krichever, I. M. and Novikov, S. P.',
    title='The {Schrödinger} equation in a periodic field and {Riemann} surfaces',journal='Doklady Akademii Nauk SSSR',volume='229',number='1',pages='15--18',year='1976',
    url='https://people.sissa.it/~dubrovin/Papers/1976/dubrovin_krichever_novikov_1976.pdf',scope='read the result',
    locator='Author-hosted English original translation, sections 1--4, Lemmas 1--3 and Theorem 1. Russian metadata also opened at https://www.mathnet.ru/eng/dan40452. Received 19 February 1976. Last paragraph requires complete curve data, not just any algebraic subcurve.')
add('veselovnovikov1984potential',author='Veselov, A. P. and Novikov, S. P.',title='Finite-gap two-dimensional {Schrödinger} operators. Potential operators',journal='Doklady Akademii Nauk SSSR',volume='279',number='4',pages='784--788',year='1984',
    url='https://homepage.mi-ras.ru/~snovikov/91.pdf',scope='read the result',
    locator='Author-hosted English translation: Theorem 1 (potential/Prym), Theorem 2 (sufficient reality conditions), Theorem 3 (Bloch completeness). Russian metadata https://www.mathnet.ru/eng/dan9334 also opened; received 5 March 1984. No unrestricted necessity assertion inferred.')
add('veselovnovikov1984explicit',author='Veselov, A. P. and Novikov, S. P.',title='Finite-gap two-dimensional potential {Schrödinger} operators. Explicit formulas and evolution equations',journal='Doklady Akademii Nauk SSSR',volume='279',number='1',pages='20--24',year='1984',
    url='https://www.mathnet.ru/eng/dan9374',scope='read the result',
    locator=r'Russian full text opened through option_lang=rus getFT. Section II, Theorem 1 and equations (4)--(6), and Theorem 2 read. Received 6 June 1984. The final approximation conjecture is not imported as an unrecorded seminar occurrence. The printed operator commutator convention is distinguished from this chapter\textquotesingle s independently checked convention.')
add('manakov1976inverse',author='Manakov, S. V.',title='The method of the inverse scattering problem, and two-dimensional evolution equations',journal='Uspekhi Matematicheskikh Nauk',volume='31',number='5 (191)',pages='245--246',year='1976',url='https://www.mathnet.ru/eng/rm3978',scope='read the result',
    locator='Full two-page Russian paper, equation (5) and fixed-energy construction. Received 28 January 1976. The introductory blanket no-Lax wording is not accepted as a theorem without hypotheses.')
add('grinevichnovikov1985analogs',author='Grinevich, P. G. and Novikov, R. G.',title='Analogs of multisoliton potentials for the two-dimensional {Schrödinger} operator',journal='Functional Analysis and Its Applications',volume='19',number='4',pages='276--285',year='1985',doi='10.1007/BF01077292',url='https://www.mathnet.ru/eng/faa1403',
    locator='Math-Net metadata and title; Russian pages 32--42. Received 30 October 1984. R. G. Novikov is not S. P. Novikov. Full construction not read.')
add('grinevich1986rational',author='Grinevich, P. G.',title='Rational solitons of the {Veselov--Novikov} equations are reflectionless two-dimensional potentials at fixed energy',journal='Theoretical and Mathematical Physics',volume='69',number='2',pages='1170--1172',year='1986',
    url='https://www.mathnet.ru/php/archive.phtml?jrnid=tmf&option_lang=eng&paperid=5229&wshow=paper',
    locator='Math-Net title and publication data; Russian pages 307--310. No unrecorded rational formula reconstructed from this metadata.')
add('novikovhenkin1987dbar',author='Novikov, R. G. and Henkin, G. M.',title=r'The {$\bar\partial$}-equation in the multidimensional inverse scattering problem',journal='Russian Mathematical Surveys',volume='42',number='3',pages='109--180',year='1987',doi='10.1070/RM1987v042n03ABEH001419',url='https://www.mathnet.ru/eng/rm2537',
    locator='Math-Net metadata; received 23 October 1986. A later analytic theory, not evidence that the unnamed December 1985 claim was already proved.')
add('grinevichnovikov1988negative',author='Grinevich, P. G. and Novikov, S. P.',title='Two-dimensional inverse scattering problem for negative energies and generalized-analytic functions. {I}. Energies below the ground state',journal='Functional Analysis and Its Applications',volume='22',number='1',pages='19--27',year='1988',doi='10.1007/BF01077719',url='https://www.mathnet.ru/eng/faa1082',
    locator='Math-Net metadata; Russian pages 23--33, received 19 February 1987. This author is S. P. Novikov. The energy and ground-state qualifications prevent a blanket all-energy reading.')
add('belavinknizhnik1986complex',author='Belavin, A. A. and Knizhnik, V. G.',title='Complex geometry and the theory of quantum strings',journal='Soviet Physics JETP',volume='64',number='2',pages='214--228',year='1986',url='https://strings.itp.ac.ru/Papers/belavin1986.pdf',scope='read the result',
    locator='Sections 2--6 read, especially (2.19)--(2.21), determinant curvature in section 3, global Mumford form in section 5, and genus-two/three formulas (6.14), (6.19). Submitted 18 February 1986; English issue August 1986; Russian ZhETF 91, 364--390. Printed formulas are compared with separately derived normalization checks.')
add('quillen1985determinants',author='Quillen, Daniel',title='Determinants of {Cauchy--Riemann} operators over a {Riemann} surface',journal='Functional Analysis and Its Applications',volume='19',number='1',pages='31--34',year='1985',doi='10.1007/BF01086022',url='https://www.mathnet.ru/eng/faa1334',scope='read the result',
    locator='Russian full text (pages 37--41) read: sections 1--4, dual cohomology line convention, determinant norm and smoothness proposition. Received 18 June 1984. Quillen uses (det ker D)* tensor det coker D; dualizing reverses the spectral factor.')
add('beilinsonmanin1986mumford',author='Beilinson, A. A. and Manin, Yu. I.',title='The {Mumford} form and the {Polyakov} measure in string theory',journal='Communications in Mathematical Physics',volume='107',number='3',pages='359--376',year='1986',doi='10.1007/BF01220994',url='https://link.springer.com/article/10.1007/BF01220994',
    locator='Publisher landing page and abstract, September 1986 issue. Full article not read: Project Euclid access was blocked. The detailed theorem is cross-checked in the opened Bost Bourbaki exposition, sections 3.2--3.3. The February 1986 seminar is itself a circulation witness.')
add('raysinger1973complex',author='Ray, D. B. and Singer, I. M.',title='Analytic torsion for complex manifolds',journal='Annals of Mathematics',volume='98',number='1',pages='154--177',year='1973',doi='10.2307/1970909',url='https://annals.math.princeton.edu/1973/98-1/p05',
    locator='Journal metadata opened. Torus determinant normalization read in Kokotov 2007, section 5.0.1, equation (5.1), not inferred from this landing page.')
add('kokotov2007polyhedral',kind='misc',author='Kokotov, Alexey',title='Compact polyhedral surfaces of an arbitrary genus and determinant of {Laplacian}',year='2007',howpublished='Max Planck Institute for Mathematics preprint 2007-127',url='https://webdoc.sub.gwdg.de/ebook/serien/e/mpi_mathematik/2007/127.pdf',scope='read the result',
    locator='Preprint dated 17 October 2007. Section 5.0.1, equation (5.1), flat-torus determinant with the metric |dz| squared; reference 35 points to Ray--Singer 1973. Only the needed normalization is used.')
add('matonevolpato2013determinantal',author='Matone, Marco and Volpato, Roberto',title='Determinantal characterization of canonical curves and combinatorial theta identities',journal='Mathematische Annalen',volume='355',pages='327--362',year='2013',doi='10.1007/s00208-012-0787-z',url='https://arxiv.org/abs/math/0605734',scope='read the result',
    locator='arXiv v3 (13 January 2012) full text: section 3.1 preceding Proposition 3.2 and section 4.1, equation (4.1). First arXiv version 30 May 2006; Springer online publication 1 February 2012; January 2013 issue, verified on publisher page. Noether exception and nonsingular odd theta characteristic are explicit.')
add('fay1973theta',kind='book',author='Fay, John D.',title='Theta Functions on {Riemann} Surfaces',series='Lecture Notes in Mathematics',volume='352',publisher='Springer',year='1973',doi='10.1007/BFb0060090',url='https://link.springer.com/book/10.1007/BFb0060090',
    locator='Publisher metadata and table of contents only, prime form chapter pages 16--36. Relevant modern theta formulas read in Matone--Volpato; no claim to have read the full book.')
add('krichever2006linear',kind='incollection',author='Krichever, I. M.',title='Integrable linear equations and the {Riemann--Schottky} problem',booktitle='Algebraic Geometry and Number Theory',series='Progress in Mathematics',volume='253',pages='497--514',publisher='Birkhäuser',year='2006',url='https://www.math.columbia.edu/department/krichever/pdfs/2005-2009/2006-ILEATRP.pdf',scope='read the result',
    locator='Author-hosted full text, Introduction (Shiota KP characterization) and Theorem 1.1 (auxiliary linear equation). First preprint April 2005; chapter 2006. Bibliographic pages cross-checked in Matone--Volpato publisher bibliography.')
add('knizhnik1986analytic',author='Knizhnik, V. G.',title='Analytic fields on {Riemannian} surfaces',journal='Physics Letters B',volume='180',number='3',pages='247--254',year='1986',doi='10.1016/0370-2693(86)90304-7',url='https://www.itp.ac.ru/en/persons/knizhnik-vadim-genrikhovich/',
    locator='Landau Institute author bibliography checked; 13 November 1986 publication. Publisher full text returned an access failure. Thematic comparator only for the incomplete last stress-tensor line of record 664.')
add('belavinetal1986loops',author='Belavin, A. A. and Knizhnik, V. G. and Morozov, A. Yu. and Perelomov, A. M.',title='Two- and three-loop amplitudes in the bosonic string theory',journal='Physics Letters B',volume='177',number='3--4',pages='324--328',year='1986',url='https://www.itp.ac.ru/en/persons/knizhnik-vadim-genrikhovich/',
    locator='Landau Institute Knizhnik bibliography checked, entry for Physics Letters B 177. Same-year JETP Letters announcement listed separately. Explicit formulas checked through Belavin--Knizhnik 1986 section 6, not through an unread full text of this letter.')
add('witten2012revisited',kind='misc',author='Witten, Edward',title='Superstring Perturbation Theory Revisited',year='2012',howpublished='arXiv:1209.5461',url='https://arxiv.org/abs/1209.5461',scope='read the result',
    locator='First preprint 25 September 2012; v4 dated 5 November 2023. HTML v4 read selectively: sections 6.4 (infrared poles), 6.6 (integration cycle), 7.6 (tadpoles), 8 (supersymmetry). No claim to have read every page; these qualifications refute an unqualified statement that everything converges.')
add('bost1987determinants',kind='incollection',author='Bost, Jean-Benoît',title='Fibrés déterminants, déterminants régularisés et mesures sur les espaces de modules des courbes complexes',booktitle='Séminaire Bourbaki 1986/87, exposé 676',series='Astérisque',volume='152--153',pages='113--149',year='1987',publisher='Société Mathématique de France',url='https://numdam.org/book-part/SB_1986-1987__29__113_0/',scope='read the result',
    locator='Full Numdam PDF read, sections 2.2--2.3 and 3: Theorems 2.1, 2.2, 3.1, 3.2, 3.3, Proposition 2.3; genus at least 3 constancy on pages 141--142. Exposé dated February 1987. OCR of some formulas is imperfect; determinant conventions are independently checked algebraically in this chapter.')
add('favalepirolatorelli2023forms',kind='misc',author='Favale, Filippo Francesco and Pirola, Gian Pietro and Torelli, Sara',title='Holomorphic 1-forms on the moduli space of curves',year='2023',howpublished='arXiv:2009.10490, version 4',url='https://arxiv.org/pdf/2009.10490',scope='read the result',
    locator='Version 4, 19 May 2023; manuscript dated 15 April 2023. Theorem 3.4, genus at least 4 smooth locus: holomorphic functions constant and first cohomology vanishing. The genus at least 3 claim in the chapter instead uses the separately read Bost argument.')

(HERE/'references.bib').write_text('\n'.join(entries))
(HERE/'sources.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'entries':len(entries),'verified_urls':len(sources)},indent=2))
