"""Reproducibly assemble the shard bibliography, preserving cumulative keys."""
import pathlib,re,json
D=pathlib.Path(__file__).parent
items=json.loads((D/'items.json').read_text())
needed=sorted({k for x in items for k in x['refs']})
cumulative=(D.parents[1]/'references_cumulative.bib').read_text()
existing={}
for key in needed:
 matches=list(re.finditer(r'@\w+\{'+re.escape(key)+r'\s*,',cumulative))
 if not matches:continue
 start=matches[-1].start();p=cumulative.index('{',start);depth=1;i=p+1
 while depth:
  depth+=(cumulative[i]=='{')-(cumulative[i]=='}');i+=1
 existing[key]=cumulative[start:i]
new={}
audit={}
def prose_spacing(text):
 text=re.sub(r'(?<=[A-Za-z])(?=(?:19|20)\d{2}\b)',' ',text)
 text=re.sub(r'(?<=\d)(?=(?:January|February|March|April|May|June|July|August|September|October|November|December))',' ',text)
 for word in ['volume','issue','pages','received','Received','presented','Presented','published','publication','section','sections','Section','Theorem','Theorems','Lemma','Proposition','Remark','eq.','at','and','degree','mod']:
  text=re.sub(r'\b'+re.escape(word)+r'(?=\d)',word+' ',text)
 return text.replace('TheoremA','Theorem A').replace('sectionI','section I').replace('issue268','issue 268').replace('Invent66','Invent. 66').replace('pp.155','pp. 155').replace('pp.96','pp. 96').replace('pp.11','pp. 11').replace('Page96','Page 96')
def add(key,author,title,year,url,locator,level='result read',typ='article',**fields):
 locator=prose_spacing(locator)
 if key=='gee2026modularity':fields.pop('publisher',None)
 title=title.replace(r'\textquotesingle\textquotesingle{}',"''")
 for name in ['journal']:
  if name in fields:fields[name]=fields[name].replace(r'\textquotesingle ',"'")
 data=dict(author=author,title=title,year=str(year),url=url,**fields,note='verified',annote=f'Checked 11 November 2026. {level}. {locator}')
 new[key]='@'+typ+'{'+key+',\n'+''.join('  '+k+' = {'+v+'},\n' for k,v in data.items())+'}'
 audit[key]=dict(opened_url=url,verification=level,locator_and_scope=locator)
add('drinfeld1983hamiltonian','Drinfeld, V. G.','Hamiltonian structures on Lie groups, Lie bialgebras and the geometric meaning of the classical Yang--Baxter equations',1983,'https://www.mathnet.ru/eng/dan45858','Full Russian three-page paper opened and read, section4 definition and Theorem2, Theorem3 on integration, section7 on skew solutions. Presented24May1982, received4June1982, published1983. Actual issue268(2), not notebook issue5. This source confirms the Lie-bialgebra terminology, not the unrestricted nonskew operator classification.',journal='Doklady Akademii Nauk SSSR',volume='268',number='2',pages='285--287')
add('krichever1983hessians','Krichever, I. M.',r'``Hessians\textquotesingle\textquotesingle{} of integrals of the {Korteweg--de Vries} equation and perturbations of finite-zone solutions',1983,'https://www.mathnet.ru/eng/dan46140','Full Russian PDF read: Theorems 1--3, Lemmas 1--3, equations (6), (13)--(19). Presented 19 October 1982; received 23 November 1982. Submission is not evidence of public circulation.',journal='Doklady Akademii Nauk SSSR',volume='270',number='6',pages='1312--1317')
add('wodzicki1984values','Wodzicki, Mariusz','Values at the positive integral points of the zeta-function of the {Hill} operator with a finite-zone potential',1984,'https://www.mathnet.ru/eng/faa1431','Full Russian PDF, Theorems 1--2 and section 4 read. Russian pages 67--69; English pages 55--57. Received 25 July 1983. Final paragraph explicitly records a Manin-seminar report in November 1982.',journal='Functional Analysis and Its Applications',volume='18',number='1',pages='55--57',doi='10.1007/BF01076366')
add('semenov1983classical','Semenov-Tian-Shansky, M. A.','What is a classical {$r$}-matrix?',1983,'https://www.mathnet.ru/eng/faa1574','Full Russian PDF read: section 1 Theorem 1; section 4 Proposition 9 and Theorem 11 (including factor 2); section 5 Theorem 13, equations (22)--(23). Received 15 April 1983, revised 16 May 1983. The quadratic theorem assumes a skew R on an associative algebra with invariant trace pairing.',journal='Functional Analysis and Its Applications',volume='17',number='4',pages='259--272',doi='10.1007/BF01076717')
add('segalwilson1985loop','Segal, Graeme and Wilson, George','Loop groups and equations of {KdV} type',1985,'https://www.numdam.org/item/PMIHES_1985__61__5_0.pdf','Full primary paper consulted: sections 2--3, 5--6, 8--10; Proposition 2.7 (dense continuous-loop image), Proposition 6.1 (index), Propositions 5.1, 5.5, 5.9, Corollaries 5.12 and 5.18, Proposition 5.17, equation (5.19), Propositions 8.2--8.3 and 8.6, Theorem 9.11. These seminar notes themselves document March--April 1983 circulation.',journal=r'Publications Math\'ematiques de l\textquotesingle IH\'ES',volume='61',pages='5--65',doi='10.1007/BF02698802')
add('novikov1982hamiltonian','Novikov, S. P.','The {Hamiltonian} formalism and a many-valued analogue of {Morse} theory',1982,'https://homepage.mi-ras.ru/~snovikov/74.pdf','Author-hosted full text, sections 4--5 read for Dirac periods and many-valued map-space actions. Publisher metadata at https://www.mathnet.ru/eng/rm3819 opened; received 22 April 1982.',journal='Russian Mathematical Surveys',volume='37',number='5',pages='1--56',doi='10.1070/RM1982v037n05ABEH004020')
add('gubarevkozlov2023rota','Gubarev, Vsevolod and Kozlov, Roman',r'{Rota--Baxter} operators on {$\operatorname{Cur}(\mathfrak{sl}_2(\mathbb C))$}',2023,'https://ieja.net/files/papers/volume-33/15-IEJA-3522.pdf','Section 2.1, Proposition 2.5 and proof read for ordinary sl2 weight-one Rota--Baxter operators. Their current-Lie-conformal classification is a different main theorem. The involution B to -Id-B is retained when using the finite-dimensional normal forms. Received 13 September 2022; accepted 8 November 2022.',journal='International Electronic Journal of Algebra',volume='33',pages='247--269',doi='10.24330/ieja.1218727')
add('kontsevichvishik1994geometry','Kontsevich, Maxim and Vishik, Simeon','Geometry of determinants of elliptic operators',1994,'https://arxiv.org/pdf/hep-th/9406140','Full primary preprint read, sections 1--2 on admissibility, cuts and anomaly. Posted 21 June 1994, explicitly an abridgement of hep-th/9404046 (April 1994). Logarithmic symbols and classical order-zero log differences are distinguished.',typ='misc',eprint='hep-th/9406140',archivePrefix='arXiv',doi='10.48550/arXiv.hep-th/9406140')
add('castillogarate2015anomaly',r'Castillo-Garate, Victor and Friedman, Eduardo and M\u{a}ntoiu, Marius','The multiplicative anomaly of three or more commuting elliptic operators',2015,'https://intlpress.com/api/bgcloud-front/resource/pdf/volume/1806603322847031297-1806603322847031297-e1c0090d83aec9716fd5626a68b4a5ae.pdf','Full journal PDF opened successfully earlier in this run; equation (1) and preceding hypotheses read. Later repeated fetch returned 403; this does not erase the successful full-text reading. The formula is for commuting positive invertible elliptic self-adjoint pseudodifferential operators, positive orders, same bundle on a closed manifold. Not a theorem for arbitrary noncommuting or cut-incompatible products.',journal='Mathematical Research Letters',volume='22',number='3',pages='665--673')
add('page1975compact','Page, Lavon Barry','Compact {Hankel} operators and the {F. and M. Riesz} theorem',1975,'https://msp.org/pjm/1975/56-1/pjm-v56-n1-p20-p.pdf','Full paper read, pages 221--223: a proof of Hartman (1958) compact-Hankel theorem. Received 25 September 1973; published November 1975. The unitary-loop QC equivalence is our marked elementary Calkin-algebra deduction, not a theorem quoted verbatim from Page.',journal='Pacific Journal of Mathematics',volume='56',number='1',pages='221--223')
add('drinfeldsokolov1985lie','Drinfeld, V. G. and Sokolov, V. V.','Lie algebras and equations of {Korteweg--de Vries} type',1985,'https://math.berkeley.edu/~frenkel/Drinfeld-Sokolov.pdf','Full English translation read in section 3.7 (Miura transformation, Proposition 3.26) and section 6. Russian original 1984, Itogi 24,81--180; English publication 1985. Introduction identifies the 1981 announcement; MathNet intd72 verifies DOI and both publication dates.',journal='Journal of Soviet Mathematics',volume='30',number='2',pages='1975--2036',doi='10.1007/BF02105860')
add('drinfeldsokolov1981equations','Drinfeld, V. G. and Sokolov, V. V.','Equations of {Korteweg--de Vries} type, and simple {Lie} algebras',1981,'https://www.mathnet.ru/eng/dan44415','Publisher metadata checked: received 27 November 1980, published 1981. Earlier announcement is explicitly cited as such by the 1984/1985 full survey. No equation-level claim is based on an unread original.',level='publisher metadata checked',journal='Doklady Akademii Nauk SSSR',volume='258',number='1',pages='11--16')
add('shiota1986characterization','Shiota, Takahiro','Characterization of {Jacobian} varieties in terms of soliton equations',1986,'https://link.springer.com/article/10.1007/BF01388967','Publisher metadata and displayed references only. Bibliography records 1983 Kyoto seminar notes separately from the June 1986 article. Full theorem was not read, and this is not claimed to solve the all-abelian-varieties programme.',level='publisher metadata checked',journal='Inventiones Mathematicae',volume='83',pages='333--382',doi='10.1007/BF01388967')
add('atiyahbott1984moment','Atiyah, M. F. and Bott, R.','The moment map and equivariant cohomology',1984,'https://www.math.stonybrook.edu/~mmovshev/MAT570Spring2008/BOOKS/atiyahbott_moment.pdf','Full primary PDF, sections 2--8 read, especially integration formula (3.8), invariant Cartan complex, parity specialization and fixed-point denominator. Received 20 December 1982. Bibliography gives Berline--Vergne Rennes 1982 and DH Utrecht 1982 preprints, so 1984 is not a first-circulation date.',journal='Topology',volume='23',number='1',pages='1--28',doi='10.1016/0040-9383(84)90021-1')
add('duistermaatheckman1982variation','Duistermaat, J. J. and Heckman, G. J.','On the variation in the cohomology of the symplectic form of the reduced phase space',1982,'https://www.math.ru.nl/~heckman/','Author bibliography opened for exact journal/date/pages, including the distinct 1983 addendum. Original full article was not retrieved. Exact mathematical statements read in Atiyah--Bott 1984 sections 6--7, which explicitly identify the 1982 theorem and its assumptions.',level='primary-author metadata checked; result checked in contemporary primary treatment',journal='Inventiones Mathematicae',volume='69',pages='259--268',doi='10.1007/BF01399506')
add('boxercalegarigeepilloni2021surfaces','Boxer, George and Calegari, Frank and Gee, Toby and Pilloni, Vincent','Abelian surfaces over totally real fields are potentially modular',2021,'https://numdam.org/item/10.1007/s10240-021-00128-2.pdf','Theorems 1.1.2 and 1.1.3 and discussion pp.155--157 read. Continuation/functional equation in 1.1.2; potential automorphy in 1.1.3; the latter does not control poles over the original field. Publisher page opened: received 25 December 2018, accepted 27 October 2021, online first 29 November 2021, online issue 28 December 2021. Gee 2026 Remark 2.7 confirms preprint online at end of 2018.',journal=r'Publications Math\'ematiques de l\textquotesingle IH\'ES',volume='134',pages='153--501',doi='10.1007/s10240-021-00128-2')
add('boxercalegarigeepilloni2025modularity','Boxer, George and Calegari, Frank and Gee, Toby and Pilloni, Vincent','Modularity theorems for abelian surfaces',2025,'https://arxiv.org/pdf/2502.20645','Version 1 posted 28 February 2025. Theorems A and B and section 9.5 read. Theorem B: smooth genus-two curve y^2=f(x), degree5, mod3 image GSp4(F3), good ordinary reduction of the curve at2 and3. These conditions cannot be omitted. General genus-two meromorphic continuation and actual modularity are not conflated.',typ='misc',eprint='2502.20645',archivePrefix='arXiv',primaryClass='math.NT')
add('gee2026modularity','Gee, Toby','Modularity theorems for abelian surfaces',2026,'https://epubs.siam.org/doi/full/10.1137/25M1806697','Author research account read: section1, Theorems1.4--1.5, Remark2.7, and discussion of future lifting/classicality work. Gives precise current scope and end-2018 preprint chronology. Section2.7 is not a section; the correct locator is Remark2.7.',typ='incollection',booktitle='Proceedings of the International Congress of Mathematicians 2026, Volume 3: Invited Lectures (Sections 1--4)',pages='377--395',publisher='European Mathematical Society and SIAM',doi='10.1137/25M1806697')
add('cassounogues1982series',r'Cassou-Nogu\`es, Pierrette',r'S\'eries de {Dirichlet}',1982,'https://www.numdam.org/item/AST_1982__94__1_0.pdf','Full primary research report read, opening pages and sectionI, Lemma1 and Shintani-cone series discussion. Proceedings of 1981 Metz arithmetic days, published1982. It reports Shintani1976 for totally real fields and provides polynomial-series extensions; it does not state an ordinary elliptic torus-operator realization. Original Shintani1976 text not obtained. The distinct 1981 AIF paper was not cited because publisher metadata names Philippe while its scanned title page says Pierrette.',typ='incollection',booktitle=r'Journ\'ees arithm\'etiques---Metz, 1981',series=r'Ast\'erisque',number='94',pages='1--15',publisher=r'Soci\'et\'e math\'ematique de France')
# Preserve cumulative identities while documenting the pages actually opened here.
reused_audit={
'seeley1968powers':('https://www.mathnet.ru/eng/mat458','Publisher metadata and full Russian PDF opened. Introduction pp.96--98 read: non-self-adjoint principal-symbol ray condition, complex powers and the shifted-zeta index cancellation. Page96 calls the source a preprint. The distinct 1967 proceedings article is not silently substituted.','result read'),
'apery1979irrationalite':('https://numdam.org/item/AST_1979__61__11_0.pdf','Full original read; irrationality theorem and proof pp.11--13; publication1979 after 1978 report.','result read'),
'atiyah1982convexity':('https://www.math.stonybrook.edu/~azinger/mat562/Atiyah82.pdf','Theorem1 and hypotheses read; compact connected Hamiltonian action. Received27March1981; publication1982.','result read'),
'atiyahbottpatodi1973heat':('https://link.springer.com/article/10.1007/BF01425417','Publisher page opened for metadata. Local-density mathematics verified against Gilkey first-edition text and APS I.','publisher metadata checked; mathematics in other cited primary source'),
'atiyahpatodisinger1975spectral1':('https://webhomes.maths.ed.ac.uk/~v1ranick/papers/aps001.pdf','Theorem3.10 and section4 signature discussion read; product collar, kernel correction, eta convention. Received25March1974.','result read'),
'atiyahpatodisinger1976spectral3':('https://webhomes.maths.ed.ac.uk/~v1ranick/papers/aps003.pdf','Theorem4.5 and opening discussion read; odd-dimensional eta regularity. Received24January1975.','result read'),
'breuilconraddiamondtaylor2001modularity':('https://virtualmath1.stanford.edu/~conrad/papers/tswfinal.pdf','TheoremA and Introduction read: every elliptic curve over Q modular. Not the entire modularity-lifting proof.','result read'),
'deligne1974weil':('https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf','Section1 local zeta and Theorem1.6 purity read. July1973 lectures; received20September1973; publication1974.','result read'),
'gilkey1981residue':('https://pages.uoregon.edu/gilkey/dirPDF/gilkeyAdvances.pdf','Theorem0.1 and Introduction read: all-dimensional global eta regularity for classical elliptic self-adjoint positive-order operators; local residue need not vanish.','result read'),
'gilkey1984invariance':('https://darkwing.uoregon.edu/~gilkey/dirPDF/InvarianceTheory1Ed.pdf','Full first-edition electronic reprint opened; sections1.7,1.10,2.4--2.6, Chapter3, and sections4.3--4.4 consulted. Original1984, electronic reprint1996.','result read'),
'nist2026dlmf':('https://dlmf.nist.gov/25.11','Official sections25.11,25.6,25.4 opened for Hurwitz zeta, even/negative values and functional equation. Access2026 is not discovery date.','formulas read'),
'wodzicki1982spectral':('https://link.springer.com/article/10.1007/BF01404760','Publisher metadata opened: February1982, Invent66,115--135. Full original unread. Exact operator-domain/cut statements checked in Kontsevich--Vishik1994 and Gilkey book.','publisher metadata checked')}
for key,(url,locator,level) in reused_audit.items():
 if key not in existing:raise ValueError('Cumulative key missing '+key)
 locator=prose_spacing(locator)
 audit[key]=dict(opened_url=url,verification=level,locator_and_scope=locator)
 # Preserve cumulative identity, replacing only the access annotation for this run.
 entry=existing[key]
 am=re.search(r'\bannote\s*=\s*\{',entry)
 if am:
  start=am.end();depth=1;i=start
  while depth:
   depth+=(entry[i]=='{')-(entry[i]=='}');i+=1
  entry=entry[:start]+f'Checked 11 November 2026. {level}. {locator}'+entry[i-1:]
 existing[key]=entry
 if key=='nist2026dlmf':
  existing[key]=existing[key].replace('https://dlmf.nist.gov/2.4','https://dlmf.nist.gov/25.11')
for key in needed:
 if key not in audit:raise ValueError('No opened-source audit '+key)
entries=[]
for key in needed:
 entry=existing.get(key,new.get(key))
 if entry is None:raise ValueError(key)
 entries.append(entry)
(D/'references.bib').write_text('\n\n'.join(entries)+'\n')
(D/'source_audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(f'{len(entries)} bibliography entries; {len(existing)} cumulative keys reused; {len(audit)} audited opened sources.')
