from pathlib import Path
import json

OUT=Path(__file__).resolve().parent
sources=[]

def ref(key,typ,author,title,year,url,scope,**fields):
    sources.append(dict(key=key,type=typ,author=author,title=title,year=str(year),url=url,
                        note=fields.pop('note','verified'),
                        annote='Checked 10 November 2026. '+scope,**fields))

ref('dirac1950generalized','article','Dirac, P. A. M.','Generalized {Hamiltonian} Dynamics',1950,
    'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F4C30A59B59BEE09E9CB6F07377B8BD3/S0008414X00025700a.pdf/div-class-title-generalized-hamiltonian-dynamics-div.pdf',
    'Full primary article opened and sections 2--9 read, especially the constraint classification, equations (34)--(39), and the ordering warning. Based on August 1949 Vancouver lectures; journal publication 1950. Regular constraint assumptions are retained.',
    journal='Canadian Journal of Mathematics',volume='2',pages='129--148',doi='10.4153/CJM-1950-012-1')
ref('gogilidze1996abelianization','article','Gogilidze, S. A. and Khvedelidze, A. M. and Pervushin, V. N.',
    'On {Abelianization} of First Class Constraints',1996,'https://arxiv.org/pdf/hep-th/9504153',
    'arXiv metadata opened; full PDF downloaded from the public arXiv URL and its text read locally. Section 1 equations (1.8)--(1.10) and section 2A give equivalent local commuting generators under independence. First arXiv submission 28 April 1995; journal 1996. Not used to claim first discovery of local coisotropic normal form.',
    journal='Journal of Mathematical Physics',volume='37',pages='1760--1771',doi='10.1063/1.531478',eprint='hep-th/9504153')
ref('faddeevpopov1974gravity','article','Faddeev, L. D. and Popov, V. N.',
    'Covariant quantization of the gravitational field',1974,'https://ufn.ru/ufn74/ufn74_6/ufn746b.pdf',
    'Full English primary review opened and read: sections 1--5, especially equations (3.20)--(3.21). Russian original Usp. Fiz. Nauk 111(3), 427--450, November 1973; English translation 1974. Introduction distinguishes Feynman one-loop ghost observations from the later all-order rules. The Russian-original DOI is not misassigned to the English translation.',
    journal='Soviet Physics Uspekhi',volume='16',number='6',pages='777--788')
ref('yangmills1954conservation','article','Yang, C. N. and Mills, R. L.',
    'Conservation of isotopic spin and isotopic gauge invariance',1954,
    'https://journals.aps.org/pr/pdf/10.1103/PhysRev.96.191',
    'Full original five-page article opened; gauge transformation, curvature and invariant-action equations read. Published 1 October 1954, received 28 June 1954; receipt is not a verified public preprint date. Used for the classical construction, not continuum quantum existence.',
    journal='Physical Review',volume='96',number='1',pages='191--195',doi='10.1103/PhysRev.96.191')
ref('kallosh1978modified','article','Kallosh, Renata',
    'Modified {Feynman} rules in supergravity',1978,
    'https://www.sciencedirect.com/science/article/pii/0550321378903401',
    'Publisher bibliographic data and abstract were returned in search, but direct opening returned 403; full original article was not read. Used as an explicitly indirect contemporary lead for modified ghost interactions, not for a model-independent termination theorem. Journal issue dated 14--21 August 1978; earlier public circulation not verified.',
    journal='Nuclear Physics B',volume='141',number='1--2',pages='141--152',doi='10.1016/0550-3213(78)90340-1',note='unverified')
ref('fuster2005brst','misc','Fuster, Andrea and Henneaux, Marc and Maas, Axel',
    '{BRST}-antifield Quantization: A Short Review',2005,'https://arxiv.org/pdf/hep-th/0506098',
    'Full primary author review opened. Sections 2.1--2.3 distinguish closed, open and reducible gauge algebras; sections 4--6 explain differential, observables and antighost/auxiliary pairs; sections 7--9 state quantum and gauge-independence qualifications. First arXiv circulation June 2005, revised August 2005; lectures in 2004. Used as later clarification, not as proof that the 1979 notebook states the later BV formalism.',
    eprint='hep-th/0506098',howpublished='arXiv preprint')
ref('nielsen1975gauge','article','Nielsen, N. K.',
    'On the gauge dependence of spontaneous symmetry breaking in gauge theories',1975,
    'https://www.sciencedirect.com/science/article/pii/0550321375903016',
    'Publisher metadata/abstract found in search; direct publisher access returned 403 and the original full text was not read. Used only as the original publication lead; the actual effective-action identity was read in Espinosa et al. 2015, section 2.1. Journal publication 22 December 1975; earlier public circulation not verified.',
    journal='Nuclear Physics B',volume='101',number='1',pages='173--188',doi='10.1016/0550-3213(75)90301-6',note='unverified')
ref('espinosa2015higgstory','misc',
    r'Espinosa, Jos{\'e} R. and Giudice, Gian F. and Morgante, Enrico and Riotto, Antonio and Senatore, Leonardo and Strumia, Alessandro and Tetradis, Nikolaos',
    'The cosmological {Higgstory} of the vacuum instability',2015,
    'https://www.slac.stanford.edu/pubs/slacpubs/16500/slac-pub-16698.pdf',
    'Primary PDF downloaded from the public SLAC report server after browser retrieval timed out. Section 2.1 equation (1) and the immediately following stationary-action consequence read locally. arXiv metadata independently opened: first submission 18 May 2015, revision 4 September 2015. Used only for the Nielsen-identity clarification, not the cosmological claims.',
    eprint='1505.04825',howpublished='SLAC-PUB-16698; arXiv preprint')
ref('becchirouetstora1975renormalization','article','Becchi, C. and Rouet, A. and Stora, R.',
    'Renormalization of Gauge Theories',1975,'https://numdam.org/item/RCP25_1975__22__A10_0.pdf',
    'Full 58-page primary report opened. Abstract and the sections on Slavnov identities, gauge independence and physical unitarity inspected. Strasbourg RCP25 volume 22, exposition 10, pp.1--57; report dated April 1975. The work recalls announcements in 1974. Its proof has semisimple massive Higgs-model, linear-gauge and renormalization hypotheses, not arbitrary gauge systems.',
    journal=r'Les rencontres physiciens-math{\'e}maticiens de Strasbourg--RCP25',volume='22',pages='1--57')
ref('gribov1978quantization','article','Gribov, V. N.',
    'Quantization of non-{Abelian} gauge theories',1978,
    'https://www.sciencedirect.com/science/article/pii/055032137890175X',
    'Publisher search returned the original article metadata and abstract, but direct access returned 403. An open academic mirror returned503 on download. Original full text not read. The 1978 global-gauge ambiguity is used as an explicitly qualified publication lead, not a general nonperturbative gauge-fixing theorem.',
    journal='Nuclear Physics B',volume='139',number='1--2',pages='1--19',doi='10.1016/0550-3213(78)90175-X',note='unverified')
ref('bering1997geometry','misc','Bering, K.',
    'Geometry of the {BFV} Theorem',1997,'https://arxiv.org/pdf/hep-th/9709003',
    'Full 16-page primary paper opened; section II, equation (II.6), sections V.2--V.3 and equations (V.8)--(V.9) read. It explicitly excludes global Gribov obstructions and phase-space boundaries and assumes existence of the path integral. Field-dependent BRST flow is not an ordinary canonical transformation. First arXiv submission September 1997; opened revision 5 February 1998. Original BFV publications are cited in its introduction.',
    eprint='hep-th/9709003',howpublished='UUITP-14/97; arXiv preprint')
ref('batalinvilkovisky1977relativistic','article','Batalin, I. A. and Vilkovisky, G. A.',
    'Relativistic {S}-matrix of dynamical systems with boson and fermion constraints',1977,
    'https://www.sciencedirect.com/science/article/pii/0370269377905536',
    'Publisher metadata and abstract were found in search; direct opening returned 403. Original text not read. Bering1997 supplies an independently read later description and bibliography. This is the Hamiltonian BFV-era publication, not the later Lagrangian BV antibracket construction. Published 15 August 1977; prior public circulation not verified.',
    journal='Physics Letters B',volume='69',number='3',pages='309--312',doi='10.1016/0370-2693(77)90553-6',note='unverified')
ref('fradkinfradkina1978quantization','article','Fradkin, E. S. and Fradkina, T. E.',
    'Quantization of relativistic systems with boson and fermion first- and second-class constraints',1978,
    'https://www.sciencedirect.com/science/article/pii/0370269378901351',
    'Cumulative bibliography key reused. Publisher metadata and abstract returned in search, but direct publisher opening gave 403 and INSPIRE displayed an empty JavaScript shell. Original proof not read; used as an explicitly indirect graded Hamiltonian-constraint publication lead. Published 2 January 1978. The August 1977 report date found in search is not independently verified as a public circulation date.',
    journal='Physics Letters B',volume='72',number='3',pages='343--348',doi='10.1016/0370-2693(78)90135-1',note='unverified')
ref('senjanovic1976path','article',r'Senjanovi{\'c}, P.',
    'Path integral quantization of field theories with second-class constraints',1976,
    'https://www.sciencedirect.com/science/article/pii/0003491676900622',
    'Publisher metadata found in search; original publisher access returned 403. The public Croatian reprint lead https://hrcak.srce.hr/file/489576 returned 418, so it was not read. Used only as an indirect original measure-formula lead with article-page locator, not an invented internal equation number. Published 10 September 1976; receipt is not public circulation. A 1991 erratum is a further unverified lead.',
    journal='Annals of Physics',volume='100',number='1--2',pages='227--261',doi='10.1016/0003-4916(76)90062-2',note='unverified')
ref('gibbonshawking1977action','article','Gibbons, G. W. and Hawking, S. W.',
    'Action integrals and partition functions in quantum gravity',1977,
    'https://www.fis.uc.cl/~mbanados/Cursos/TopicosRelatividadAvanzada/GibbonsHawking3.pdf',
    'Primary article PDF opened, downloaded and the first two pages rendered and read visually because the scan had no extractable text. Section II equation (2.1) and p.2753 give the extrinsic-curvature boundary term and reference subtraction. Published 15 May 1977; received 4 October 1976, which is not a verified public preprint date.',
    journal='Physical Review D',volume='15',pages='2752--2756',doi='10.1103/PhysRevD.15.2752')
ref('yau1977calabi','article','Yau, Shing-Tung',
    "{Calabi}'s conjecture and some new results in algebraic geometry",1977,
    'https://pmc.ncbi.nlm.nih.gov/articles/PMC431004/',
    'Primary PNAS/PMC metadata opened. The public scanned first-page image linked by PMC was downloaded and read visually: Theorem1 on p.1798 distinguishes prescribed Ricci form in a fixed class, c1=0 and c1<0. It does not assert universal nonzero-cosmological-constant Einstein metrics. The announcement appeared in May 1977 and credits Aubin in the negative case.',
    journal='Proceedings of the National Academy of Sciences of the United States of America',volume='74',number='5',pages='1798--1799',doi='10.1073/pnas.74.5.1798')
ref('yau1978ricci','article','Yau, Shing-Tung',
    r'On the {Ricci} curvature of a compact {K\"ahler} manifold and the complex {Monge--Amp\`ere} equation, I',1978,
    'https://onlinelibrary.wiley.com/doi/10.1002/cpa.3160310304',
    'Publisher article metadata opened successfully; full 1978 proof not independently read in this audit. The theorem itself was read in the primary 1977 announcement. Full article publication May1978, volume31 issue3. Used to establish publication fate rather than imply full proof verification.',
    journal='Communications on Pure and Applied Mathematics',volume='31',number='3',pages='339--411',doi='10.1002/cpa.3160310304')
ref('zagier2007dilogarithm','incollection','Zagier, Don','The dilogarithm function',2007,
    'https://www.maths.dur.ac.uk/users/herbert.gangl/zagier_dilog.pdf',
    'Cumulative key reused; full author chapter opened. Chapter I sections1,3,4 and equation(4.1) checked for the standard and Bloch-Wigner functions and ideal tetrahedron volume; Chapter II section1.A checked for Rogers normalization and the exact five-argument identity. Chapter I reprints an earlier 1988 essay. None of these classical identities is dated to 2007 as a discovery.',
    booktitle='Frontiers in Number Theory, Physics, and Geometry II',editor='Cartier, Pierre and Julia, Bernard and Moussa, Pierre and Vanhove, Pierre',publisher='Springer',address='Berlin',pages='3--65')
ref('apery1979irrationalite','article',r'Ap{\'e}ry, Roger',
    r'Irrationalit{\'e} de $\zeta(2)$ et $\zeta(3)$',1979,
    'https://numdam.org/item/AST_1979__61__11_0.pdf',
    'Full original four-page PDF opened and read. Journal pages11--13 establish the irrationality result; proceedings of the 1978 arithmetic meeting, published1979. Does not identify the particular dilogarithmic formula intended by the notebook list.',
    journal=r'Ast{\'e}risque',volume='61',pages='11--13')
ref('gabrielovgelfandlosik1975computation','article',"Gabrielov, A. M. and Gel'fand, I. M. and Losik, M. V.",
    'Combinatorial computation of characteristic classes',1975,
    'https://www.mathnet.ru/eng/faa2234',
    'Cumulative key reused. Publisher metadata and linked full Russian PDF opened. Section1, condition(A), Proposition10 and Theorem1 (Russian p.18) read: the rational cycle represents p1 under linearizability and configuration-space connectivity. The proof continuation in partII was inspected but not independently rederived. Received2December1974; public preprint date not verified. Russian original9(2),12--28; English9(2),103--115.',
    journal='Functional Analysis and Its Applications',volume='9',number='2',pages='103--115',doi='10.1007/BF01075446')
ref('goncharov1993classical','incollection','Goncharov, A. B.',
    r'The classical polylogarithms, algebraic {K}-theory and $\zeta_F(n)$',1993,
    'https://sasha-goncharov.github.io/AKTheory93.pdf',
    'Author-hosted full chapter opened. Section3 pp.115--117 identifies the earlier GGL dilogarithm and Wigner volume cocycle; equation(12) read from the page image to confirm degree3 and measurable/continuous comparison. This is a checked exposition of the 1970s observations; original Wigner circulation date remains unverified.',
    booktitle='The Gelfand Mathematical Seminars, 1990--1992',publisher=r'Birkh\"auser',pages='113--135')
ref('pereirapirio2009web','book',r'Pereira, Jorge Vit{\'o}rio and Pirio, Luc',
    "An Invitation to Web Geometry: From Abel's Addition Theorem to the Algebraization of Codimension One Webs",2009,
    'https://library.impa.br/cbm/27CBM/27CBM_03.pdf',
    'Full author book hosted by IMPA opened. Introduction p.6 and section6.1.4 p.190 checked: explicit Bol five-web, six Abelian relations, and nonalgebraizability. Bibliography item21 gives Bol1936; that original proof was not separately opened. PrefaceMay2009, courseJuly2009. No general web-classification problem is inferred from the notebook name.',
    publisher='IMPA',series='27th Brazilian Mathematical Colloquium',isbn='978-85-244-0291-3')
ref('gabrielovgelfandlosik1976local','article',"Gabrielov, A. M. and Gel'fand, I. M. and Losik, M. V.",
    'A local combinatorial formula for the first class of {Pontryagin}',1976,
    'https://www.mathnet.ru/eng/faa2124',
    'MathNet publisher metadata and linked full Russian primary text opened. Theorems1--3 checked: a local rational codimension-four Pontryagin cycle with a configuration-space connectivity condition. No specific dilogarithm formula was located in this short paper. Russian original10(1),14--17; English10(1),12--15. Received29September1975, not verified public preprint circulation.',
    journal='Functional Analysis and Its Applications',volume='10',number='1',pages='12--15',doi='10.1007/BF01075766')
ref('beilinson1980regulators','article','Beilinson, A. A.',
    'Higher regulators and values of {L}-functions of curves',1980,
    'https://www.mathnet.ru/eng/faa1800',
    'MathNet publisher metadata and linked full Russian primary PDF opened and read. Section1 equation(1), Lemma1 and the subsequent localization paragraph exactly match the complex regulator and real-part relation. Section2 has further arithmetic claims not silently attributed to the notebook. Received21December1979; no earlier public preprint date verified. The notebook independently documents the 19November1979 seminar. Russian original14(2),46--47; English14(2),116--118.',
    journal='Functional Analysis and Its Applications',volume='14',number='2',pages='116--118',doi='10.1007/BF01086554')
ref('weibel2013kbook','book','Weibel, Charles A.','The {K}-Book: An Introduction to Algebraic {K}-Theory',2013,
    'https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.pdf',
    'Cumulative key reused; full author-hosted book opened. III.6.1 Matsumoto presentation and III.5.5/III.5.5.2 stable universal Steinberg extension and stability read. These are precise modern statements of older results, not evidence of a 2013 discovery or proof of an unrestricted finite-rank notebook formula.',
    series='Graduate Studies in Mathematics',volume='145',publisher='American Mathematical Society')
ref('weinberg1967leptons','article','Weinberg, Steven','A Model of Leptons',1967,
    'https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.19.1264',
    'Cumulative key reused; full three-page original opened and read. Equations1--4 give field content, potential and Yukawa term; equations5--14 give breaking, masses and currents. Published20November1967, received17October1967; receipt is not a public preprint date. The model has massless minimal neutrinos and tree-level relations.',
    journal='Physical Review Letters',volume='19',pages='1264--1266',doi='10.1103/PhysRevLett.19.1264')
ref('higgs1964broken','article','Higgs, Peter W.','Broken Symmetries and the Masses of Gauge Bosons',1964,
    'https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.13.508',
    'Full two-page primary article opened and read. Equations1--4 display the Abelian model, scalar fluctuations, shifted vector and mass. Footnote3 qualifies the classical analysis; the paper acknowledges the independent Englert-Brout work. Published19October1964, received31August1964; no earlier public date verified here.',
    journal='Physical Review Letters',volume='13',pages='508--509',doi='10.1103/PhysRevLett.13.508')
ref('kobayashimaskawa1973cp','article','Kobayashi, Makoto and Maskawa, Toshihide',
    '{CP}-Violation in the Renormalizable Theory of Weak Interaction',1973,
    'https://theory.tifr.res.in/~amol/flavour/lec10/kmpaper.pdf',
    'Full six-page primary article opened; the discussion of complex quark mixing and the six-quark construction on pp.654--657 read. Journal publicationFebruary1973; received1September1972, not a verified public preprint date. The model allows a physical CP phase, so generic three-generation mixing cannot be described by a real orthogonal matrix.',
    journal='Progress of Theoretical Physics',volume='49',number='2',pages='652--657',doi='10.1143/PTP.49.652')
ref('deblasdittmaierkogler2026electroweak','incollection','de Blas, J. and Dittmaier, S. and Kogler, R.',
    'Electroweak Model and Constraints on New Physics',2026,
    'https://pdg.lbl.gov/2026/reviews/rpp2026-rev-standard-model.pdf',
    'Current primary PDG author review opened. Section10.1 and its equations give group, representations, Higgs potential, masses and currents; section10.2 states radiative/scheme qualifications; section10.4.1 gives measured vector masses. RevisedMay2026; PDF stamped1June2026. Used as a current check, not a discovery date.',
    booktitle='Review of Particle Physics 2026',publisher='Particle Data Group',chapter='10')
ref('gonzalezgarciawendell2026neutrinos','incollection','Gonzalez-Garcia, M. C. and Wendell, R.',
    'Neutrino Masses, Mixing, and Oscillations',2026,
    'https://pdg.lbl.gov/2026/reviews/rpp2026-rev-neutrino-mixing.pdf',
    'Current primary PDG author review opened. Sections14.1--14.2 distinguish the massless minimal Standard Model from mass extensions and oscillations. RevisedMarch2026; opened PDF datedAugust2026. Used to prevent the 1979 massless model from becoming a current empirical assertion or a claim deciding Dirac versus Majorana nature.',
    booktitle='Review of Particle Physics 2026',publisher='Particle Data Group',chapter='14')
ref('ceccucciligetisakai2026ckm','incollection','Ceccucci, A. and Ligeti, Z. and Sakai, Y.',
    'The {CKM} Quark-Mixing Matrix',2026,
    'https://pdg.lbl.gov/2026/reviews/rpp2026-rev-ckm-matrix.pdf',
    'Current primary PDG author review opened. Section12.1 equations(12.1)--(12.3) read for Yukawa matrices, biunitary diagonalization, unitary CKM matrix, three angles and one phase. RevisedMarch2026. Used to check the exact restriction under which a real orthogonal matrix is possible.',
    booktitle='Review of Particle Physics 2026',publisher='Particle Data Group',chapter='12')
ref('hustonrabbertzzanderighi2026qcd','incollection','Huston, J. and Rabbertz, K. and Zanderighi, G.',
    'Quantum Chromodynamics',2026,'https://pdg.lbl.gov/2026/reviews/rpp2026-rev-qcd.pdf',
    'Current primary PDG author review opened. Section9.1 equations(9.1)--(9.2), fundamental quark and adjoint gluon representations, and trace/Casimir conventions read. RevisedAugust2025 in the 2026 review, PDF stamped1June2026. These confirm older QCD structure without asserting a mathematical continuum existence proof.',
    booktitle='Review of Particle Physics 2026',publisher='Particle Data Group',chapter='9')
ref('wilson1974confinement','article','Wilson, Kenneth G.','Confinement of quarks',1974,
    'https://hep.physics.uoc.gr/Erasmus-IP-2013/files/lectures/Rabinovici/Wilson.pdf',
    'Cumulative key reused; full15-page original opened. SectionsII andIV, and the limitations in sectionVI read: strong-coupling lattice area law is not a Lorentz-invariant continuum construction. Published15October1974, received12June1974. The cumulative bibliography also records an INSPIRE February1974 CLNS262 preprint lead; that date was not independently reverified in this batch.',
    journal='Physical Review D',volume='10',number='8',pages='2445--2459',doi='10.1103/PhysRevD.10.2445')
ref('gliozzipepewiese2010width','article','Gliozzi, F. and Pepe, M. and Wiese, U.-J.',
    'The Width of the Confining String in {Yang--Mills} Theory',2010,'https://arxiv.org/pdf/1002.4888',
    'Full four-page primary paper opened and read. Equations(1)--(3) give effective-string energy and logarithmic mean-square width; figures2--3 compare (2+1)-dimensional SU(2) Monte Carlo data. First arXiv submission26February2010, journal2010. This is conditional effective theory plus numerical evidence, not a full four-dimensional continuum proof. The 1981 Luscher-Munster-Weisz precursor is identified in its references.',
    journal='Physical Review Letters',volume='104',pages='232001',doi='10.1103/PhysRevLett.104.232001',eprint='1002.4888')
ref('bulava2019string','article',r'Bulava, John and H{\"o}rz, Ben and Knechtli, Francesco and Koch, Vanessa and Moir, Graham and Morningstar, Colin and Peardon, Mike',
    'String breaking by light and strange quarks in {QCD}',2019,'https://arxiv.org/pdf/1902.04006',
    'Full primary paper opened. Introduction, section4, equation(4.4) and energy-level/string-breaking discussion read. Numerical lattice QCD with dynamical light and strange quarks; not an analytic continuum theorem. First arXiv submission11February2019, journal2019. Used to qualify asymptotic confinement formulations with dynamical fundamental matter.',
    journal='Physics Letters B',volume='793',pages='493--498',doi='10.1016/j.physletb.2019.05.018',eprint='1902.04006')
ref('jaffewitten2000yangmills','misc','Jaffe, Arthur and Witten, Edward','Quantum {Yang--Mills} Theory','n.d.',
    'https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf',
    'Cumulative key reused. Full official problem description opened; sections1--2,5 and6.5 read. Section5 lists confinement as an extension distinct from the formal existence-and-mass-gap statement. The standalone PDF is undated; the key uses the Millennium announcement year, not a claimed circulation date of this version.',
    howpublished='Official problem description, Clay Mathematics Institute')
ref('clay2026yangmills','misc','{Clay Mathematics Institute}','{Yang--Mills} and the Mass Gap',2026,
    'https://www.claymath.org/millennium/yang-mills-the-maths-gap/',
    'Cumulative key reused. Official live problem page opened and labeled Unsolved on the check date. It confirms the status of existence/mass gap; it is not used to equate this with the separate positive-static-string-tension assertion.')

def bibtex(s):
    fields={k:v for k,v in s.items() if k not in ('key','type')}
    return '@'+s['type']+'{'+s['key']+',\n'+''.join('  '+k+' = {'+str(v)+'},\n' for k,v in fields.items())+'}\n'

(OUT/'references.bib').write_text('\n'.join(bibtex(s) for s in sources))
(OUT/'research_sources.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n')
