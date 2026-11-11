from pathlib import Path
import json,re,collections,csv
P=Path(__file__).resolve().parent
items=json.loads((P/'items.json').read_text());talks=json.loads((P/'talks.json').read_text());problems=json.loads((P/'problems.json').read_text());refs=json.loads((P/'references.json').read_text())
d={x['id']:x for x in items}
for ident,marker in [('1977-431.2',' The rank-one pointed-curve data also recur'),('1977-435.6',' Earlier occurrence 1975-382.5')]:
    value=d[ident]['fate']
    if value.count(marker)>1:
        start=value.index(marker);end=value.index(marker,start+len(marker));d[ident]['fate']=value[:end]
d['1977-436.11']['notes']=r'Glimm, Jaffe and Fröhlich are invoked for rigorous small-coupling quantization, beside the expression \(m^2\gamma^{-1}(1-\cos\gamma u)\). Equation (26) writes \([\pi(x),u(y)]=i\delta(x-y)\), in the opposite order to the earlier Poisson bracket.'
for x in items:
    for k,v in x.items():
        if isinstance(v,str):x[k]=v.replace('\textquotesingle',r'\textquotesingle')
for p in problems:
    p['status']=p['status'].replace('Theorem3','Theorem 3').replace('Theorem1.2','Theorem 1.2').replace('section3.3','section 3.3').replace('preprint2020','preprint 2020').replace('version2022','version 2022').replace('of1978','of 1978')
    if p['id']=='GP-1977-22':p['status']='As of 10 November 2026, '+p['status'][0].lower()+p['status'][1:]
    if p['id']=='GP-1977-24':
        p['statement']=r'For each charge \(k\), describe all \(SU(2)\) instantons on \(S^4\) up to gauge and determine whether their moduli space is path-connected.'
        p['status']='As of 10 November 2026, '+p['status'][0].lower()+p['status'][1:]

audit={
'bernsteingelfandgelfand1978local1':('pp.435--437, Theorems 1--2 and Propositions 1--2','Primary author-hosted PDF opened, downloaded as bgg1.pdf, and all three rendered pages visually read. Presented 9 January 1978; issue dated 13 March 1978.'),
'bernsteingelfandgelfand1978local2':('pp.495--497, Theorem 1 and sections 5--6','Primary author-hosted PDF opened, downloaded as bgg2.pdf, and all three rendered pages visually read. Presented 9 January 1978; issue dated 20 March 1978. The actual PDF pagination was used rather than an erroneous repeated range in the author bibliography.'),
'krichever1978commutative':('Introduction; Theorem 1.1 with proof; sections 1--2','Full primary author-hosted text opened and the indicated results read. Received 15 February 1977; Russian publication 1978; English PDF copyright 1979. Cumulative bibliography key reused.'),
'sznagy1976diagonalization':('Lemma 2, pp.224--225; Main Lemma in section 2; scope of section 3','Full 16-page primary PDF opened. Lemma 2 and its proof, the Main Lemma and the matrix quasi-equivalence scope were read. Received 1 November 1975; published 1976.'),
'drinfeld1977commutative':('Metadata, abstract record and received date','Math-Net metadata page opened. Received 14 April 1976; Functional Analysis and Its Applications 11(1), 9--12 (1977); DOI 10.1007/BF01135527. This record editor did not infer a theorem on all Weyl skew fields from the title. The cumulative bibliography records an earlier full-text check, which is separate from this item identification.'),
'uhlenbeck1982removable':('Publisher abstract, bibliography item 15, received and issue dates','Publisher page opened. Abstract explicitly states removal and compactification for finite-energy Yang--Mills fields; 1979 announcement cited there. Received 25 March 1981; published February 1982. Full Euclid article and AMS announcement were not successfully retrieved.'),
'dayapremawaldron2026parabolic':('Theorems 1.1--1.2; section 3.3; historical discussion and bibliography','Open-access full primary article read at the cited statements and connectedness proof. Published 2 March 2026. The historical distinction between Taubes for SU(2)/SU(3) and Donaldson for general SU(r) was explicitly checked. Reopened in turn151view2.'),
'drinfeldmanin1978selfdual':('Sections 1--7, especially theorem in section 4 and Gram matrices in section 6; Russian pp.78--79','Full primary two-page Russian article opened through Math-Net and read. Received 27 November 1977; published 1978. Tensor, orthogonal-projection and Gram-matrix conditions checked against the notebook.'),
'drinfeldmanin1979instantons':('Sections 0.2--0.4 and 1.6--1.9; Theorem 2.1 and proof 2.2--2.13; section 3','Metadata and full 16-page primary Russian paper opened. Received 26 May 1978; published 1979. Full PDF: https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=1899&what=fullt. Evidence turn81view0 and turn100view3; title checked again in turn151view1.'),
'narasimhan1962universal':('p.286, theorem and canonical Stiefel connection','Primary one-page author announcement opened and read in full (turn75view3). Presented at Prague in September 1961; proceedings published 1962. Joint work with Ramanan is explicitly acknowledged.'),
'gelfandponomarev1971quadruples':('Title, authors, publication and received date','Primary Math-Net metadata opened (turn100view0). Received 21 October 1970; published 1971. This check does not verify the notebook reference to unpublished extra automorphism and Hermitian conditions.'),
'takhtajanfaddeev1974nonlinear':('Russian pp.160--161, assumptions in section 1, section 4 on pp.170--173','Metadata and full primary 15-page PDF opened. Hamiltonian definitions, finite/simple scattering zeros, spectral energy, and kink/breather formulas read. Full PDF: https://www.mathnet.ru/php/getFT.phtml?jrnid=tmf&option_lang=eng&paperid=3879&what=fullt. Evidence turn117view0 and turn121view0.'),
'korepinfaddeev1975quantization':('Sections 1--3; section 4, equations (27)--(30); section 5, equation (32)','Full primary 17-page Russian PDF opened and the cited parts read: zero-mode exclusion, determinant, mass renormalization, phase and level condition (turn127view0--3). Received 2 April 1975; Russian issue November 1975. PDF: https://www.mathnet.ru/php/getFT.phtml?jrnid=tmf&option_lang=eng&paperid=4060&what=fullt.'),
'chenliulu2020sinegordon':('Theorems 1.1 and 10.1; Definition 2.6; Remarks 1.2--1.3 and weighted spaces (1.11)','Primary 100-page version 2 opened; theorem statements and precise hypotheses read, not every page. First posted 8 September 2020; version read dated 15 February 2022. Generic finite simple zeros, distinct speeds and modified scattering explicitly checked (turn114view3 and turn123view3).'),
'sklyaninfaddeev1978quantum':('Sections 2--4, explicit nonlinear-Schrodinger operators and stated sine-Gordon limitation','Full four-page primary Russian article opened and read (turn105view3 and turn116view1). Received 28 July 1978; published December 1978. PDF: https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=42231&what=fullt.'),
'zamolodchikov1977jetp':('Equations (2) and (4)--(10): masses, two channels and reflectionless values','Primary four-page JETP Letters article in a university-hosted PDF opened and read (turn106view0 and turn119view2). Submitted 14 April 1977; published 20 May 1977. Some OCR formulas are malformed; only unambiguous mass, channel and coupling statements were used.'),
'zamolodchikov1977exact':('Publisher abstract, received and publication dates','Publisher page opened (turn114view1). Received 4 January 1977; published June 1977; CMP 55, 183--186. Full CMP paper not read. A separate primary JETP Letters article was read for formulas.'),
'yafaev2004lectures':('Section 1 definitions; Theorem 2.4 with proof; equation (2.8)','Primary author lecture notes opened (turn130view0 and turn132view0). Lectures delivered October--November 2001; arXiv posting 12 March 2004. Precise short-range hypotheses and wave asymptotic read.'),
'froehlich1975quantized':('Publisher abstract and dates','Primary APS metadata and abstract opened (turn114view0). Received 11 February 1975; published 31 March 1975. Part of the abstract mathematics rendered incompletely, so no exact coupling threshold or complete Hamiltonian theorem is claimed.'),
'coleman1975equivalence':('Publisher abstract, received and publication dates','Cumulative bibliography key reused. Primary APS page opened (turn105view2). Received 6 January 1975; published 15 April 1975. Full text was not accessed in this check.'),
'pohlmeyer1976integrable':('Publisher abstract and dates','Publisher page opened (turn121view1). Received 28 August 1975; published October 1976. Full paper not read; attribution of the sphere-model Lax representation is independently explicit in the primary Zakharov--Mikhailov introduction.'),
'zamolodchikovzamolodchikov1978on':('Introduction and sections 2--3; field-theory identification and CDD ambiguity','Primary 1978 article opened and cited parts read (turn130view1). Received 22 August 1977; revised 14 November 1977. The algebraic factorized matrix is explicit; the authors give evidence, rather than a full axiomatic construction, for its sigma-model identification.'),
}
for a in refs:
    if a['key'] in audit:a['locator'],a['opened_url_evidence']=audit[a['key']]
    if a['key']=='faddeevkorepin1978quantum':
        if 'scribd' in a['url']:
            a['locator']='Original article reproduction: introduction, pp.4--6, and section 2.1, equations (1.3)--(1.11)'
            a['opened_url_evidence']='Public full-text reproduction of the primary 1978 article opened (turn129view0 and turn131view0). Original title, authors, page headers and received date 4 July 1977 visible. Mathematical OCR is sometimes damaged; exact normalization is not certified from OCR alone.'
        else:
            a['locator']='Institutional bibliographic record and abstract'
            a['opened_url_evidence']='Primary institutional metadata opened (turn64view2): Physics Reports 42(1), 1--87, June 1978. The direct publisher PDF returned HTTP 403.'
for name,data in [('items',items),('talks',talks),('problems',problems),('references',refs)]:
    (P/(name+'.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
bib=(P/'references.bib').read_text()
bib=bib.replace('volume={29}, number={12}', 'volume={29}, eid={12}')
(P/'references.bib').write_text(bib)

fields={'id','record','pages','kind','title','notes','statement','reconstruction','class','fate','present_status','literal_correctness','publication_match','verification','development','problem','worth','refs','confidence'}
errors=[]
for r in range(428,437):
    z=[x for x in items if x['record']==r]
    if [x['id'] for x in z]!=[f'1977-{r}.{n}' for n in range(1,len(z)+1)]:errors.append(('ids',r))
for x in items:
    if fields-set(x):errors.append(('fields',x['id'],sorted(fields-set(x))))
    if x['class'] in ['C','D'] and not x['worth']:errors.append(('worth',x['id']))
    if x['literal_correctness'] not in ['correct','correct with missing hypotheses','false as written','not determinable']:errors.append(('literal',x['id']))
    for k,v in x.items():
        if isinstance(v,str) and re.search(r'[\x00-\x1f]',v):errors.append(('control',x['id'],k))
        if isinstance(v,str):
            for match in re.finditer(r'\\cite[tp](?:\[[^\]]*\])?\{([^}]*)\}',v):
                for key in match.group(1).split(','):
                    if key not in x['refs']:errors.append(('citation absent refs',x['id'],key))
required={key for x in items+problems for key in x['refs']}
available=set(re.findall(r'@\w+\{([^,]+),',bib))
audited={x['key'] for x in refs}
if required-available:errors.append(('missing bib',sorted(required-available)))
if required-audited:errors.append(('missing audit',sorted(required-audited)))
areas=json.loads((P/'areas.json').read_text())
if set(areas)!={x['id'] for x in items}:errors.append(('areas mismatch',))
report={'items':len(items),'records':len(talks),'by_record':dict(collections.Counter(x['record'] for x in items)),'by_class':dict(collections.Counter(x['class'] for x in items)),'problems':len(problems),'corrections':len(list(csv.DictReader((P/'corrections.csv').open()))),'references':len(available),'audits':len(refs),'errors':errors}
(P/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
