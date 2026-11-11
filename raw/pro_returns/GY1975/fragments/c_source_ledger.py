import json,re
from pathlib import Path
P=Path(__file__).resolve().parent
bib=(P/'c_references.bib').read_text()+'\n'+(P/'root_references.bib').read_text()
table='''arnowittfickler1962quantization|turn39view1|abstract; received and publication dates|publisher metadata checked
schwinger1962relativistic|turn41view2|abstract radiation-gauge formulation; received and publication dates|publisher metadata checked
reinhardt2018coulomb|turn50view4|Section2 equations1--5; Section3 instantaneous Coulomb energy|read the result
wilson1974confinement|turn41view0|SectionsI--III, link variables, Haar integral, Wilson loop|read the result
jaffewitten2000yangmills|turn41view1|Sections1,4,5; confinement distinguished from mass gap|read the result
consuljain1973poisson|turn30view0|Sections2--3; equation3.1|read the result
roiter1968brauerthrall|turn35view2|primary metadata; received20 March1968; theorem read through Ringel|publisher metadata checked
ringel2006foundation|turn30view1,turn40view4,turn40view5,turn42view2|Sections1.5,3.1 corollary,6,7.3; author bibliography for publication|read the result
bernsteingelfandponomarev1973coxeter|turn48view2|Sections2--3 reflection functors and roots|read the result
roiter1978roots|turn139view3,turn143view3|condition(*) and Lemma1 p202; Proposition4 p205; Lemma6 p206|read the result
berezinleites1975supermanifolds|turn39view2,turn40view3|pp505--508 sheaf definition, morphisms, integration|read the result
berezinkac1970lie|turn50view1,turn51view0|Section3.5 Theorem4 formal Lie correspondence; Sections3--5|read the result
bordemann2000superpoisson|turn40view1,turn42view4,turn51view3|Theorems1.3--1.4 and Corollary1.1|read the result
onsager1944crystal|turn50view2|abstract; transfer construction and Clifford algebra SectionsII--VII; thermodynamic limit|read the result
lieb1967squareice|turn62view0|abstract exact square-ice entropy; received/publication metadata|publisher metadata checked
krichever1978commutative|turn50view0,turn51view1,turn62view2|Theorems1.1,2.3; introduction correcting1977 implementation; received15 February1977|read the result
duistermaatguillemin1975spectrum|turn35view1|publisher metadata only; received20 October1974, publicationFebruary1975|publisher metadata checked
zelditch1998wave|turn72view1,turn120view0|Introduction local wave-trace expansion, equation0.1; Section1; arXiv journal reference and upload date|read the result
berardhelffer2018sturm|turn72view3,turn121view3|Theorems1.4 and2.15; first circulation2017, revision2018, journal issue2020|read the result
berardhelffer2018courant|turn42view3,turn71view0,turn143view2,turn145view0|Theorem1.1; Statement1.2; Section3 Neumann triangle; PDF title-page author order|read the result
gelfandfuchs1970formal|turn116view2,turn117view2,turn139view0|Theorem0.3, pp327--328 and continuous cochains|read the result
gelfandkalininfuchs1972hamiltonian|turn11view2,turn145view1|primary metadata; original theorem reproduced by Mikami pp151--152|indirect
perchik1975dissertation|turn103view0,turn104view4|Harvard1975 row; title and advisor Bott|publisher metadata checked
perchik1976cohomology|turn27view0,turn101view3,turn105view1|original DOI/publisher fetches failed; mathematical theorem read in Mohammadzadeh--Fuchs2014 Theorem2.1|indirect
mohammadzadehfuchs2014cohomology|turn11view1,turn12view2,turn15view0,turn105view1|Sections1--2; Theorem2.1 and table Russianpp68--69; m86 extracted text discrepancy only|read the result
kotschickmorita2009gkf|turn15view1,turn27view1,turn77view0,turn77view2|Sections2--3 definitions and GKF factorization; Section5 Theorem8; Remark9 inconsistent superscript; Section6 stable rank|read the result
mikami2016metoki|turn95view3,turn97view1,turn104view2,turn145view1|p151 infinitude question; Theorem1.1 recalls GKF, Theorem1.2 proves Metoki factorization|read the result
moritasakasaisuzuki2015computations|turn97view0,turn104view3,turn119search6|Introduction; Remark2.1 p148; Section5 stable versus fixed rank|read the result
buchstaber1975twovaluedI|turn101view0,turn103view2,turn104view0,turn105view0|Section3 averaging coalgebra; Section4 generalized translations|read the result
einstein1916foundation|turn64view2,turn116view5,turn121view0,turn139view2|primary translation Sections3--4,12,14--20; publisher metadata|read the result
fouresbruhat1952cauchy|turn116view0|Introduction pp141--143, result statement; subsequent full-text access timed out|read the result
fouresbruhat1958fluids|turn116view1,turn117view1,turn139view1|Section2 constraint propagation; Sections4--6 dust; Sections9--12 fluids and sound cone|read the result
kruskal1960maximal|turn75view0,turn121view2|abstract maximal extension; received1959, publication1960; full mirror inaccessible|publisher metadata checked
godel1949cosmological|turn64view1|Sections2--3, metric with dust and cosmological constant, closed timelike circles|read the result
suslin1976projective|turn48view1,turn144view0|SectionIII Theorems2--3, not Theorem1; p1066 received26 February1976; presentation12 March1976|read the result
quillen1976projective|turn116view3|publisher metadata; received1 March1976, publicationDecember1976; proof not read|publisher metadata checked
monceuryengui2017suslin|turn72view0,turn75view1,turn75view2|Theorem3.1; Lemma4.1 p117; Algorithm4.2; distinguishes general-ring lemma from algorithm hypothesis|read the result'''
extra={
'wilson1974confinement':['https://hep.physics.uoc.gr/Erasmus-IP-2013/files/lectures/Rabinovici/Wilson.pdf'],
'ringel2006foundation':['https://www.math.uni-bielefeld.de/~ringel/publ-new.html'],
'roiter1978roots':['https://www.mathnet.ru/php/getFT.phtml?jrnid=tm&option_lang=eng&paperid=2511&what=fullt'],
'berezinleites1975supermanifolds':['https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=39282&what=fullt'],
'bordemann2000superpoisson':['https://arxiv.org/pdf/math/0003218'],
'zelditch1998wave':['https://arxiv.org/pdf/math/0002037'],
'berardhelffer2018sturm':['https://arxiv.org/pdf/1706.08247'],
'gelfandfuchs1970formal':['https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=2418&what=fullteng'],
'mohammadzadehfuchs2014cohomology':['https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=3145&what=fullt'],
'kotschickmorita2009gkf':['https://arxiv.org/html/0910.3414v1'],
'buchstaber1975twovaluedI':['https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=2079&what=fullteng'],
'einstein1916foundation':['https://en.wikisource.org/wiki/The_Foundation_of_the_Generalised_Theory_of_Relativity','https://sites.pitt.edu/~jdnorton/teaching/Einstein_graduate/pdfs/Einstein_GR_1916.pdf'],
'suslin1976projective':['https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=40545&what=fullt']}
sources=[]
for line in table.splitlines():
    k,refs,loc,v=line.split('|')
    m=re.search(r'@\w+\{'+re.escape(k)+r',',bib); assert m,k
    e=bib.find('\n}',m.start()); entry=bib[m.start():e]
    url=re.search(r'url\s*=\s*\{([^}]+)\}',entry)[1]
    dm=re.search(r'doi\s*=\s*\{([^}]+)\}',entry)
    sources.append(dict(key=k,url=url,doi=dm[1] if dm else None,opened_urls=[url]+extra.get(k,[]),result_ref_ids=refs.split(','),locators=loc,verification=v,full_text_accessed=v=='read the result',checked_on='2026-11-10',note='The original publisher fetch failed; use later primary restatement for the mathematical result.' if k=='perchik1976cohomology' else ''))

searches=[
dict(items=['1975-393.2','1975-393.8'],problem_ids=['GP-1975-20','GP-1975-21'],engine='system1',date='2026-11-10',queries=['"Perchik" "infinitely" cohomology Hamiltonian','"Hamiltonian" "H_2" "cohomology" 2025 2026 Fuchs','"ham_2" "infinite" cohomology 2024 2025 2026'],result_ref_ids=['turn119search0','turn119search6','turn119search7','turn119search3'],outcome='No exact later resolution located. Recent Hamiltonian Lie-algebra actions on moduli-space cohomology are not computations of this Lie algebra cohomology. Verified explicit open statements are Mohammadzadeh--Fuchs2014 and Mikami2016, with different question strengths.'),
dict(items=['1975-391.7','1975-391.12'],problem_ids=['GP-1975-24'],engine='system1',date='2026-11-10',queries=['"Shnirelman" "eigenvalues" "Weierstrass"','"Shnirelman" "Abel" "geodesics"'],result_ref_ids=['turn150search0','turn150search1'],outcome='No exact source recovered for the global Abel distribution or the unnormalized elliptic-function sketch. Quantum ergodicity results concern eigenfunction measures and are not an exact match.'),
dict(items=['1975-389.4'],problem_ids=[],engine='system1',date='2026-11-10',queries=['"Berezin" "64" "particles" superalgebra'],result_ref_ids=['turn150search6','turn150search7','turn150search8','turn150search9'],outcome='No exact identification. Later superalgebras with64 odd generators do not determine the unnamed total64-dimensional algebra in the1976 note.'),
dict(items=['1975-388.6'],problem_ids=[],engine='system1, root coordinated',date='2026-11-10',queries=['Roiter integral quadratic forms divisibility root criterion','"Weyl roots and equivalences of integral quadratic forms"'],result_ref_ids=['turn139view3','turn143view3'],outcome='Initial identification gap resolved. Roiter1978 Proposition4 exactly supplies finite/connected affine criterion, with positivity condition. Root supplied the lead; this agent independently opened and read the original.'),
dict(items=['1975-393.11'],problem_ids=[],engine='system2, earlier targeted search',date='2026-11-10',queries=['Adams Liulevicius Buhstaber work two-valued formal groups1975'],result_ref_ids=['turn95view2','turn101view1','turn103view1','turn146view1'],outcome='Bibliographical lead: Adams and Liulevicius1975, Topology14(4),291--296, DOI10.1016/0040-9383(75)90011-7. Publisher fetch failed; May bibliography PDF opened but text not extractable. Not used for a mathematical theorem. The averaging construction was read directly in Buchstaber1975PartI.')]
out=dict(block='386-396',status_date='2026-11-10',sources=sources,unresolved_and_resolved_searches=searches,verification_policy='Opened metadata is distinguished from reading a mathematical result. An opened publisher page does not mean its full proof was read. Received/presentation/thesis dates are not automatically public circulation dates. No unlocated result is called nonexistent.')
(P/'c_sources.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(len(sources),'source records written')
