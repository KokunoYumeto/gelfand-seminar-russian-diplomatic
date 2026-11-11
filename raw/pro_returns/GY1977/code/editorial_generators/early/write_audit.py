import csv
import json
import re
from pathlib import Path

OUT = Path(__file__).parent
ROOT = OUT.parents[1]
entries = {}
audit = []

def ref(key, author, title, year, url, verification, locator, evidence,
        journal='', volume='', number='', pages='', doi='', typ='article', extra=None,
        opened_url=None):
    fields = dict(author=author, title=title, year=str(year))
    for name, value in [('journal',journal),('volume',volume),('number',number),
                        ('pages',pages),('doi',doi),('url',url),('note','verified'),
                        ('annote',evidence)]:
        if value:
            fields[name] = value
    fields.update(extra or {})
    entries[key] = '@'+typ+'{'+key+',\n'+',\n'.join(
        '  '+name+' = {'+value+'}' for name,value in fields.items())+'\n}\n'
    audit.append(dict(key=key,url=url,verification=verification,locator=locator,
                      opened_url=opened_url or url,evidence=evidence,
                      checked_on='2026-11-10'))

ref('atiyahward1977instantons', 'Atiyah, M. F. and Ward, R. S.',
    'Instantons and algebraic geometry', 1977,
    'https://link.springer.com/article/10.1007/BF01626514',
    'publisher metadata checked','Publisher abstract; received and publication dates',
    'Publisher abstract and bibliographic metadata opened. Received 31 May 1977; published June 1977. Full theorem and proof were not obtained; the exact correspondence is not claimed to have been checked in full text.',
    journal='Communications in Mathematical Physics',volume='55',number='2',pages='117--124',doi='10.1007/BF01626514')
ref('tits1977margulis','Tits, Jacques',
    'Travaux de {Margulis} sur les sous-groupes discrets de groupes de {Lie}',1977,
    'https://www.numdam.org/item/SB_1975-1976__18__174_0.pdf',
    'read the result','Exposé 482, §§1--3 and §5; Theorems 1--2',
    'Full Bourbaki report read: definitions, arithmeticity theorem, local-field superrigidity statements and restriction-of-scalars deduction. Lecture February 1976, revision April 1976, publication 1977. This is a contemporary exposition of Margulis, not a new priority claim for Tits.',
    journal='Séminaire Bourbaki',volume='1975/76',pages='174--190',extra={'number':'482'})
ref('margulis1974arithmetic','Margulis, G. A.',
    'Arithmetic properties of discrete subgroups',1974,
    'https://www.mathnet.ru/eng/rm4323','publisher metadata checked',
    'Abstract and received date; Russian original pp. 49--98',
    'MathNet metadata and abstract opened. Received 16 July 1973. The scope is the earlier nonuniform case; this entry does not verify the full cocompact higher-rank theorem.',
    journal='Russian Mathematical Surveys',volume='29',number='1',pages='107--156',doi='10.1070/RM1974v029n01ABEH001281')
ref('borelharishchandra1962arithmetic','Borel, Armand and {Harish-Chandra}',
    'Arithmetic subgroups of algebraic groups',1962,
    'https://www.mathnet.ru/eng/mat302','read the result',
    'Theorems 7.8 and 9.4; proof of 7.8 in full Russian translation',
    'Full Russian translation opened and read at Theorems 7.8 and 9.4, including the semisimple finite-volume theorem and rational-character criterion. Original Annals paper 1962; translation Matematika 8(2), 19--72, 1964.',
    journal='Annals of Mathematics',volume='75',number='3',pages='485--535',
    opened_url='https://www.mathnet.ru/php/getFT.phtml?jrnid=mat&option_lang=eng&paperid=302&what=fullt')
ref('parker2009lattices','Parker, John R.','Complex hyperbolic lattices',2009,
    'https://www.maths.dur.ac.uk/users/j.r.parker/img/Lattices.pdf','read the result',
    '§2.1, p. 3; author publication list for volume and date',
    'Full author-hosted paper opened; §2.1 read for the rank-one landscape and its explicitly open complex-hyperbolic case. Author publication list https://maths.dur.ac.uk/users/j.r.parker/ confirms Contemporary Mathematics 501 (2009), 1--42. The underlying Corlette and Gromov--Schoen proofs were not independently read.',
    typ='incollection',volume='501',pages='1--42',extra={'booktitle':'Discrete Groups and Geometric Structures','series':'Contemporary Mathematics','publisher':'American Mathematical Society'})
ref('falbelpasquinelli2023hybrid','Falbel, Elisha and Pasquinelli, Irene',
    'Complex hyperbolic orbifolds and hybrid lattices',2023,
    'https://link.springer.com/article/10.1007/s10711-022-00762-y','read the result',
    'Introduction: higher-dimensional nonarithmetic lattice question',
    'Full publisher article opened and introduction read. Published 18 January 2023. It explicitly describes existence of nonarithmetic complex-hyperbolic lattices in dimension at least four as open. Searches through 10 November 2026 found no later resolution; absence from a search is not a proof of current openness.',
    journal='Geometriae Dedicata',volume='217',pages='28',doi='10.1007/s10711-022-00762-y')
ref('dyson1946pennies','Dyson, F. J.','1931. The problem of the pennies',1946,
    'https://www.cambridge.org/core/journals/mathematical-gazette/article/1931-the-problem-of-the-pennies/DFE3B6FA5CEDE824F9B4456EDC2DF808',
    'publisher metadata checked','Publisher title, original issue date, pp. 231--234',
    'Cambridge publisher metadata opened. Original October 1946 issue is distinguished from the later online posting. Full Dyson construction was not read; the balanced-ternary construction and identity-only versus identity-plus-sign proof in this assignment are independent calculations.',
    journal='The Mathematical Gazette',volume='30',number='291',pages='231--234',doi='10.2307/3611225')
ref('yu2026mirror','Yu, Chenglong',
    'A nonarithmetic lattice from a mirror in the {Couwenberg--Heckman--Looijenga} construction',2026,
    'https://arxiv.org/abs/2611.00270','read the result','Introduction p. 1; Theorem 1.1 statement p. 2',
    'Full preprint opened and introduction and Theorem1.1 statement read. Submitted 30 October2026; manuscript dated29October. The introduction still restricts known nonarithmetic complex-hyperbolic examples to dimensions two and three; the new theorem concerns PU(2,1). Its full proof was not independently checked and no journal publication is asserted.',
    typ='misc',extra={'eprint':'2611.00270','archivePrefix':'arXiv','primaryClass':'math.GT'},
    opened_url='https://arxiv.org/pdf/2611.00270')
ref('shannon1948communication','Shannon, Claude E.','A mathematical theory of communication',1948,
    'https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf',
    'read the result','§6, Theorem 2 and properties 2, 3, 5, 6',
    'Full original paper opened; entropy characterization, equiprobable case, independence and conditional-entropy identities read. The correction of the notebook sign is also forced by the elementary nonnegativity calculation.',
    journal='The Bell System Technical Journal',volume='27',pages='379--423, 623--656',doi='10.1002/j.1538-7305.1948.tb01338.x')
ref('kirzhnitslinde1972macroscopic','Kirzhnits, D. A. and Linde, A. D.',
    'Macroscopic consequences of the {Weinberg} model',1972,
    'https://sitp.stanford.edu/publications/macroscopic-consequences-weinberg-model',
    'publisher metadata checked','Author-institution publication record; publisher bibliographic listing',
    'Author-institution record opened. Publisher full text was unavailable. This supports bibliographic identification of the temperature-dependent symmetry-restoration program, not verification of a precise potential or theorem. The quartic toy potential in the item is explicitly our illustration.',
    journal='Physics Letters B',volume='42',number='4',pages='471--474')
ref('bennett1982thermodynamics','Bennett, Charles H.',
    'The thermodynamics of computation---a review',1982,
    'https://www.cpt.univ-mrs.fr/~verga/pdfs/Bennett-1982fk.pdf','read the result',
    'Abstract; pp. 927--929, Fig. 12 and demon-memory discussion',
    'Full paper opened; reversible measurement and irreversible memory resetting discussion read. Received 8 May 1981, published 1982. Used as a later clarification, not as a claim that the 1977 notes already contained this analysis.',
    journal='International Journal of Theoretical Physics',volume='21',number='12',pages='905--940',doi='10.1007/BF02084158')
ref('hawking1975particle','Hawking, S. W.','Particle creation by black holes',1975,
    'https://the-center-of-gravity.com/documents/26/Hawking_Particle-Creation-by-Black-Holes.pdf',
    'read the result','§1; §2 Eq. (2.29) and fermionic discussion; §3 Eq. (3.1)',
    'Full original article opened at a public mirror. Introduction, radiation spectrum including greybody factor, fermionic alternative and first-law discussion read. Received 12 April 1975. Project Euclid access failed; that failed route is not counted as opened full text.',
    journal='Communications in Mathematical Physics',volume='43',number='3',pages='199--220',doi='10.1007/BF02345020')
ref('prsa2016nominal',r'Pr{\v s}a, Andrej and Harmanec, Petr and Torres, Guillermo and others',
    'Nominal values for selected solar and planetary quantities: {IAU 2015 Resolution B3}',2016,
    'https://arxiv.org/pdf/1605.09788','read the result','Table 1, nominal solar mass parameter',
    'Full resolution paper opened and Table 1 read. Preprint 31 May 2016; resolution adopted 2015; journal publication 2016. The nominal solar mass parameter is used only for the transparent present-day numerical check of the notebook radius, not retroactively as a 1977 measurement.',
    journal='The Astronomical Journal',volume='152',number='2',pages='41',doi='10.3847/0004-6256/152/2/41')
ref('chruscielcostaheusler2012stationary',r'Chru{\'s}ciel, Piotr T. and Costa, Jo{\~a}o Lopes and Heusler, Markus',
    'Stationary black holes: Uniqueness and beyond',2012,
    'https://link.springer.com/article/10.12942/lrr-2012-7','read the result',
    'Theorem 3.3 and surrounding hypotheses',
    'Full review theorem read with its four-dimensional electrovac, asymptotically flat, analytic, regular stationary and connected-horizon hypotheses. Used to prevent the informal no-hair sentence from being treated as an unrestricted theorem.',
    journal='Living Reviews in Relativity',volume='15',pages='7',doi='10.12942/lrr-2012-7')
ref('hawking1971colliding','Hawking, S. W.','Gravitational radiation from colliding black holes',1971,
    'https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.26.1344',
    'publisher metadata checked','Publisher abstract and dates',
    'Publisher abstract and metadata opened. Received 11 March 1971; published 24 May 1971. The collision-energy bound is stated in the abstract; the full global area-theorem proof was not read at this URL.',
    journal='Physical Review Letters',volume='26',pages='1344--1346',doi='10.1103/PhysRevLett.26.1344')
ref('bekenstein1973entropy','Bekenstein, Jacob D.','Black holes and entropy',1973,
    'https://journals.aps.org/prd/abstract/10.1103/PhysRevD.7.2333',
    'publisher metadata checked','Primary abstract: area-proportional entropy and generalized second law',
    'Primary publisher abstract read for the proposed entropy-area proportionality and generalized second law. Received 2 November 1972; published 15 April 1973. Full microscopic derivation was not read; the exact one-quarter normalization is sourced separately to Hawking.',
    journal='Physical Review D',volume='7',pages='2333--2346',doi='10.1103/PhysRevD.7.2333')
ref('hawking1976thermodynamics','Hawking, S. W.','Black holes and thermodynamics',1976,
    'https://doi.org/10.1103/PhysRevD.13.191','publisher metadata checked',
    'Publisher abstract: temperature and entropy normalization',
    'DOI resolved to publisher abstract; explicit temperature and entropy normalization read there. Received 30 June 1975; published 15 January 1976. This audit does not claim that the full article was read.',
    journal='Physical Review D',volume='13',pages='191--197',doi='10.1103/PhysRevD.13.191',
    opened_url='https://journals.aps.org/prd/abstract/10.1103/PhysRevD.13.191')
ref('wald2015bekenstein','Wald, Robert M.','Jacob David Bekenstein',2015,
    'https://physicstoday.aip.org/obituaries/jacob-david-bekenstein','read the result',
    'Personal recollection, account of graduate study under John Wheeler',
    'Full personal recollection by a contemporary and fellow graduate student read. Published 1 December 2015. Used only for the historical supervisor correction, not as a technical physics source.',
    journal='Physics Today',volume='68',number='12',doi='10.1063/PT.3.3029')
ref('unruh1976notes','Unruh, W. G.','Notes on black-hole evaporation',1976,
    'https://journals.aps.org/prd/abstract/10.1103/PhysRevD.14.870',
    'publisher metadata checked','Publisher abstract and publication date',
    'Primary abstract and metadata opened; published 15 August 1976. Full derivation was not obtained. Exact Rindler-coordinate and thermal normalization formulas were checked in the separately cited full review.',
    journal='Physical Review D',volume='14',pages='870--892',doi='10.1103/PhysRevD.14.870')
ref('crispinohiguchimatsas2008unruh',r'Crispino, Lu{\'i}s C. B. and Higuchi, Atsushi and Matsas, George E. A.',
    'The {Unruh} effect and its applications',2008,
    'https://arxiv.org/pdf/0710.5373','read the result',
    '§II.B, Eqs. (2.34)--(2.37); Eq. (2.125); §II.I',
    'Full author preprint opened; Rindler transformation, thermal occupation and KMS interpretation read. First preprint 29 October 2007; journal publication 1 July 2008. Used as explicit mathematical clarification of the 1976 effect, with chronology distinguished.',
    journal='Reviews of Modern Physics',volume='80',number='3',pages='787--838',doi='10.1103/RevModPhys.80.787')
ref('penziaswilson1965antenna','Penzias, A. A. and Wilson, R. W.',
    'A measurement of excess antenna temperature at 4080 Mc/s',1965,
    'https://articles.adsabs.harvard.edu/pdf/1965ApJ...142..419P','read the result',
    'Original letter, pp. 419--421',
    'Full three-page primary letter read. The reported 3.5 plus or minus 1 K is a single-frequency excess measurement; it is not misrepresented as an original full black-body spectral measurement. Letter dated 13 May 1965, observations July 1964--April 1965.',
    journal='The Astrophysical Journal',volume='142',pages='419--421',doi='10.1086/148307')
ref('gelfanddikii1977resolvent',"Gel'fand, I. M. and Dikii, L. A.",
    'The resolvent and {Hamiltonian} systems',1977,
    'https://www.mathnet.ru/eng/faa2064','read the result',
    '§1; §2 Eq. (8), Theorems 1--2 and proof, Russian pp. 13--18',
    'Full original Russian article opened and formal calculus, Hamiltonian matrix, evolutionary Lie algebra and Jacobi proof read. Received 22 December 1976; published 1977 issue 2, preceding the October talk. Constants require care in the printed variational-kernel shorthand.',
    journal='Functional Analysis and Its Applications',volume='11',number='2',pages='93--105',doi='10.1007/BF01081887',
    opened_url='https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2064&what=fullt')
ref('gelfanddikii1978jets',"Gel'fand, I. M. and Dikii, L. A.",
    'The calculus of jets and nonlinear {Hamiltonian} systems',1978,
    'https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=1979&what=fullt',
    'read the result','Introduction and §1',
    'Full Russian article opened, introduction and §1 read for the local-functional and jet calculus. It is not substituted for the exact later conceptual proof of the first-bracket Jacobi identity.',
    journal='Functional Analysis and Its Applications',volume='12',number='2',pages='81--94')
ref('lebedevmanin1979volterra','Lebedev, D. R. and Manin, Yu. I.',
    "The {Gel'fand--Dikii Hamiltonian} operator and the coadjoint representation of the {Volterra} group",1979,
    'https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=1935&what=fullt',
    'read the result','Introduction; Eq. (1); §5 theorem and Eq. (5); §6 invariant proof',
    'All seven pages of the primary Russian article read. The introduction explicitly identifies the cumbersome old Jacobi verification; §§5--6 identify the coefficient-linear first bracket and give the invariant proof. Received 10 November 1978. The 1978 ITEF preprint no. 155 is independently listed in Gelfand--Dorfman 1979, reference 7; independent Adler work is acknowledged.',
    journal='Functional Analysis and Its Applications',volume='13',number='4',pages='268--273',doi='10.1007/BF01078365')
ref('gelfanddorfman1979hamiltonian',"Gel'fand, I. M. and Dorfman, I. Ya.",
    '{Hamiltonian} operators and algebraic structures related to them',1979,
    'https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=rus&paperid=1933&what=fullt',
    'read the result','§1 Theorems 1.1--1.3; §3; §7 p. 29; bibliography no. 7',
    'Full original Russian article opened. Abstract Hamiltonian criterion and Lie-bracket construction read; §7 scalar Hamiltonian pair and its reference to Lax Moscow lectures in 1976 read; bibliography verifies Lebedev--Manin ITEF preprint 155 (1978). Received 16 April 1979. The third-order KdV operator is a precise specialization of the displayed §7 family.',
    journal='Functional Analysis and Its Applications',volume='13',number='4',pages='248--262',doi='10.1007/BF01078363')

# Reuse exact cumulative keys and bibliographic metadata, while recording this
# assignment's own verification separately from earlier chapters' annotations.
cumulative = (ROOT/'references_cumulative.bib').read_text()
reused = {
    'krichever1976zakharov':('publisher metadata checked','MathNet publication record and received date',
        'https://www.mathnet.ru/eng/dan40219',
        'MathNet metadata opened in this assignment. Received 8 October 1975, published 1976. The earlier cumulative entry records an independently opened full Russian text; this assignment does not promote its own metadata check to a new full-text verification.'),
    'krichever1977methods':('read the result','§§1--2; Appendix 2, pp. 205--207',
        'https://www.math.columbia.edu/department/krichever/pdfs/1975-1979/1977-MOAGITTONE0.pdf',
        'Full author-hosted article read at the spectral-curve construction and Appendix 2 rational KdV pole dynamics. The appendix identifies the Airault--McKean--Moser result and its hypotheses. Related construction circulated in 1975 seminar discussions; publication 1977.'),
    'krichever1978commutative':('read the result','Introduction, correction of the 1977 arbitrary-rank treatment',
        'https://www.math.columbia.edu/department/krichever/pdfs/1975-1979/1978-CROOLDO0.pdf',
        'Full author-hosted paper opened; historical introduction on Burchnall--Chaundy and correction to the earlier arbitrary-rank assertion read. Received 15 February 1977; Russian publication 1978. The exact Jacobson attribution in the notebook remains unverified.')}
for key,(verification,locator,url,evidence) in reused.items():
    match = re.search(r'@\w+\{'+re.escape(key)+',',cumulative)
    if not match:
        raise ValueError('Missing cumulative key '+key)
    start=match.start(); depth=0; end=None
    for pos in range(cumulative.index('{',start),len(cumulative)):
        if cumulative[pos]=='{' and (pos==0 or cumulative[pos-1]!='\\'): depth+=1
        if cumulative[pos]=='}' and (pos==0 or cumulative[pos-1]!='\\'):
            depth-=1
            if depth==0: end=pos+1; break
    entries[key]=cumulative[start:end]+'\n'
    audit.append(dict(key=key,url=url,opened_url=url,verification=verification,
                      locator=locator,evidence=evidence,checked_on='2026-11-10',
                      cumulative_key_reused=True))

items=json.loads((OUT/'items.json').read_text())
used={key for item in items for key in item['refs']}
assert used==set(entries), (used-set(entries),set(entries)-used)
(OUT/'references.bib').write_text('\n'.join(entries[key] for key in sorted(entries)))
(OUT/'references.json').write_text(json.dumps(sorted(audit,key=lambda a:a['key']),ensure_ascii=False,indent=2)+'\n')

rows=[]
def correction(page,place,reads,should,evidence,applies='both',typ='faithful_error'):
    rows.append(dict(page=page,place=place,transcription_reads=reads,should_read=should,
                     evidence=evidence,applies_to=applies,type=typ))
correction('P000705','Opening date','Handwritten 5/IV--77; catalogue date 1977-09-05',
    'Retain the catalogue date with a provenance note; do not silently change the visible IV into IX.',
    'P705 scan visually inspected; the supplied catalogue and handwriting conflict. No independent chronological document resolves this conflict.',typ='provenance')
correction('P000706','Projective quotient notation','C^4/C^* and H^2/H^*',
    'Remove the origin before projectivizing.',
    'P706 scan and both transcriptions preserve the shorthand; the zero vector is not a projective point.')
correction('P000706-P000707','Quaternionic real structure','The quaternionic antilinear map is called an involution.',
    'On C^4 the lift J has J^2=-1; the induced projective map has square 1.',
    'P706--P707 scans and displayed coordinate map checked; this is a distinction between lift and projectivization, not evidence of a transcription mistake.',typ='ambiguity')
correction('P000706','Instanton/bundle correspondence','Self-dual connections correspond to holomorphic bundles on CP^3.',
    'Specify rank, determinant, unitary reality data, triviality on real twistor lines, and the relevant equivalence classes.',
    'The notebook statement is abbreviated. Atiyah--Ward1977 publisher abstract supports the correspondence, but its full detailed theorem was not obtained; supplied conditions are a modern reconstruction.')
correction('P000707','Manin algebraic-type criterion','L_3 not in C[L_1,L_2]',
    'Retain the expression with an ambiguity note: L_2 is a time-evolution operator in a Lax pair and need not commute with L_1.',
    'P707 scan visually inspected; the commuting spectral ring must be distinguished from the displayed evolution pair.',typ='ambiguity')
correction('P000707','Genus of the spectral curve','Rational solutions correspond to genus zero.',
    'Specify geometric genus of the normalization when a singular rational degeneration is intended.',
    'Krichever1977, §§1--2 and Appendix2; singular rational curves can retain positive arithmetic genus.',typ='ambiguity')
correction('P000707','Polynomial relation attribution','Jacobson, 1930s, is named for a polynomial relation of operators.',
    'Preserve the historical attribution as unresolved; distinguish the Burchnall--Chaundy theorem for commuting scalar ordinary differential operators.',
    'P707 scan and Krichever1978 introduction checked. No exact Jacobson source was identified; no replacement attribution is claimed to correct handwriting.',typ='ambiguity')
correction('P000710','Algebraic matrix-entry rigidity','Every lattice in SL(n,R) is conjugate to matrices with algebraic entries.',
    'Impose the higher-rank hypotheses, in particular n>=3 for this formulation.',
    'P710 scan; Tits1977 superrigidity/arithmeticity statement. The n=2 formulation admits deformations and is false without qualification.')
correction('P000711','Nonarchimedean places','Use Q_p for the p-adic realization of the number-field coefficients.',
    'For a coefficient field K use all nonarchimedean completions K_v, or the equivalent restriction-of-scalars representation over Q_p.',
    'P711 scan and Tits1977 §5 deduction; primes and embeddings of a general number field cannot be suppressed in the exact argument.')
correction('P000712','Catalogue record 422 overlap','Kirzhnits record spans pages also assigned to Drinfeld and the subsequent physics report.',
    'Treat the bracketed notice of Kirzhnits as a heading; assign P712 formulas to record423 and the distinct later contributions to records424--425.',
    'P712--P714 scans and both transcriptions read; no second independent Kirzhnits exposition occurs at the heading.',typ='provenance')
correction('P000713','Unknown-sign counterfeit puzzle','13 coins in three weighings',
    'Keep 13 when identifying the counterfeit coin alone; 12 is the bound if its heavier/lighter sign must also be determined.',
    'P713 scan confirms 13. Complete independent balanced-ternary construction, upper bound and physical-pan check are in coin_annotation.tex and coin_check_output.json; this is an ambiguity in the success criterion, not a digit error.',typ='ambiguity')
correction('P000714','Binary entropy','H=p log p+(1-p) log(1-p)',
    'H=-p log p-(1-p) log(1-p)',
    'P714 scan confirms the missing leading negative sign in the original notebook. Shannon1948 §6 and positivity at p=1/2 verify the emendation.')
correction('P000714','Acquiring information','The wording says that acquiring information decreases information.',
    'It decreases the remaining uncertainty or entropy, under the stated conditioning model.',
    'P714 scan and adjoining conditional-information discussion; Shannon1948 §6 properties5--6. This is a conceptual slip preserved by the transcription.')
correction('P000714','Ideal-gas entropy schematic formula','S=ln(V/N)',
    'Treat this as the volume-dependent entropy per particle in units k_B, up to temperature-dependent and additive terms; use Delta S/N=k_B ln(V_f/V_i) at fixed temperature.',
    'P714 scan; source omits normalization and fixed-temperature assumptions. The item supplies the elementary thermodynamic interpretation rather than replacing the handwritten formula wholesale.',typ='ambiguity')
correction('P000715','Solar-mass Schwarzschild radius','Approximately 7 km',
    'Approximately 2.95 km for one solar mass.',
    'P715 scan confirms 7. Evaluation 2(GM_sun)/c^2 with nominal GM_sun from Prsa et al.2016 Table1 gives 2.95325 km; the notebook error is faithfully transcribed.')
correction('P000715','Black-hole parameters','Mass, radius and charge are the only remembered data.',
    'For the appropriate stationary four-dimensional electrovac uniqueness theorem, use mass, angular momentum and electric charge; radius is not an independent fourth parameter.',
    'P715 scan; Chrusciel--Costa--Heusler2012 Theorem3.3 read with hypotheses. The broad notebook slogan is not a theorem for all black holes.')
correction('P000715','Area increase','Black-hole area always increases.',
    'Apply the classical area theorem under its energy and global-causality hypotheses; quantum evaporation is outside that claim.',
    'P715 scan; Hawking1971 abstract and Hawking1975 §1 and §3 distinguish classical area increase from evaporation.')
correction('P000715','Bekenstein supervisor','Bekenstein is described as Hawking\'s student.',
    'Bekenstein was John Archibald Wheeler\'s doctoral student.',
    'P715 scan confirms the attribution. Wald2015 personal recollection explicitly describes their graduate study under Wheeler.')
correction('P000715','Ground-state ket','H|Phi>=E_0|phi>',
    'Use the same state symbol on both sides of the eigenvalue equation.',
    'P715 scan and transcriptions inspected; capitalization changes in the displayed equation should not be interpreted as two eigenstates.',typ='ambiguity')
correction('P000716','Acceleration temperature','kT=ha/c',
    'k_B T= hbar a/(2 pi c), with hbar explicitly distinguished from Planck h.',
    'P716 scan and transcribed TikZ formula inspected. Crispino--Higuchi--Matsas2008 thermal formulas verify the coefficient; if h means ordinary Planck constant the denominator is 4 pi^2 c.')
correction('P000716','Cosmological horizon','Light has not yet arrived from a region, so it is called an event horizon and assigned a temperature.',
    'Distinguish a particle horizon from a future event horizon; a temperature requires a specified spacetime, state and observer.',
    'P716 scan. The definitions have different time limits; no definite cosmological model in the passage resolves the proposed temperature. This is a conceptual correction, not an invented de Sitter assertion.')
correction('P000717','Schwartz local-functional exercise','Integral over R of a differential polynomial is used without restricting its constant term.',
    'Require f(0)=0 for this integral on all Schwartz tuples; ker(Euler derivative)=C+D(A), and constants must be separated.',
    'P717 scan and Gelfand--Dikii1977 §1 read. A nonzero constant density is not integrable on R; the formal kernel also includes constants.')
correction('P000718','Hamiltonian-matrix line continuation','A subtraction sign appears at the end of one line and again at the start of the continuation.',
    'Read a single subtraction between the two binomial differential-operator terms.',
    'P718 scan compared with the displayed formula and Gelfand--Dikii1977 §2 Eq8; treating the line-wrap marks as two negatives would violate formal skew-adjointness.',typ='ambiguity')
correction('P000718','End of record426','Catalogue page range ends at P717.',
    'Include P718 in record426; the next speaker starts at P719.',
    'Both transcriptions and P717--P718 scans read; the definitions, theorem, simpler-proof request and Novikov intervention form one continuation.',typ='provenance')
from repair_corrections_tex import repair_rows
rows = repair_rows(rows)
with (OUT/'corrections.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type'])
    w.writeheader();w.writerows(rows)
(OUT/'development.tex').write_text('% No new C/D theorem is claimed for records419--427.\n'+(OUT/'coin_annotation.tex').read_text())
print(f'Wrote {len(entries)} bibliography entries, {len(audit)} audit records and {len(rows)} correction rows.')
