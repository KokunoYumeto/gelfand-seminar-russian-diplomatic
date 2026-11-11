"""Run after compile_shard.py. Final substantive normalization and audit."""
from pathlib import Path
import json,re,csv,collections,hashlib
D=Path(__file__).resolve().parent
I=json.loads((D/'items.json').read_text())
T=json.loads((D/'talks.json').read_text())
P=json.loads((D/'problems.json').read_text())
C=list(csv.DictReader((D/'corrections.csv').open()))
B=(D/'references.bib').read_text()
byid={x['id']:x for x in I}
for x in P:
    if x['id']=='GP-1982-07':
        x['statement']=r'For three nonrelativistic quantum particles in \(\mathbb R^3\) with positive finite masses and pair Coulomb interactions, remove the center of mass. Do the Dollard-modified channel wave operators exhaust the continuous spectral subspace of the resulting Schrödinger Hamiltonian?'
byid['1982-571.20']['statement']=byid['1982-571.20']['statement'].replace(r'For three nonrelativistic particles in \(\mathbb R^3\) with pair Coulomb potentials',r'For three nonrelativistic particles in \(\mathbb R^3\) with positive finite masses and pair Coulomb potentials')
for t in T:
    if t['record'] in [562,567,569,573]:t['speaker']='A. B. Zamolodchikov'
    if t['record']==570:t['speaker']='V. L. Ginzburg'
    if t['record'] in [571,572]:t['speaker']='J. Fröhlich'
    if t['record']==565:t['pages']='P001037-P001042'
# Remove accidental doubled text-macro escapes; preserve matrix row separators.
for x in I:
    for k,v in list(x.items()):
        if isinstance(v,str):
            x[k]=v.replace(r'\\ours',r'\ours').replace(r'\\textquotesingle',r'\textquotesingle')
byid['1982-568.2']['fate']+=r' The exact earlier incidence-resolution occurrence is 1971-231.2; 1971-231.5 concerns the related Springer-fiber dimension.'
byid['1982-568.5']['fate']=byid['1982-568.5']['fate'].replace('verified here by writing',r'verified here \ours by writing')
byid['1982-568.6']['statement']=r'At the critical level \(c=0\), the pullback distribution cannot be handled by an ordinary Taylor expansion: \(d(xy)=0\) at the crossing. Asymptotics involve logarithmic terms and finite-part distributions on the axes. Writing a finite coefficient through axis integrals requires a finite-part prescription; changing that prescription is compensated by a multiple of the point delta distribution. The coefficient of the fixed distribution family itself is not arbitrary.'
byid['1982-569.10']['statement']=byid['1982-569.10']['statement'].replace('Integrating \\(d\\) scalar matter fields',r'Writing \(\Delta_g\) for the nonnegative scalar Laplacian, integrating \(d\) scalar matter fields')
# A single Virasoro convention in every modern field of record 573.
for x in I:
    if x['record']==573:
        for fld in ['statement','reconstruction','fate','present_status']:
            x[fld]=x[fld].replace('L_n',r'\ell_n').replace('L_m',r'\ell_m').replace('L_0',r'\ell_0').replace('L_{',r'\ell_{')
byid['1982-573.1']['statement']=r'Reserve \(L_n\) for the notebook and write \(\ell_n=-L_n\), so the modern highest weight is \(h=-\Delta\). Use \([\ell_n,\ell_m]=(n-m)\ell_{n+m}+\frac{c}{12}(n^3-n)\delta_{n+m,0}\mathbf1\), with \(\ell_n\) for \(n>0\) annihilating the highest-weight vector. In notebook generators this has the reverse Witt term \((m-n)L_{n+m}\) and the same cubic central term. The written constant delta term is not antisymmetric, already giving \([L_0,L_0]=c\mathbf1/12\). The neighboring primary law needs the corresponding overall sign change.'
byid['1982-573.1']['reconstruction']=r'Throughout the modern statements use \(\ell_n=-L_n\) and \(h=-\Delta\); retain the notebook symbols in quotations. Restoring the cubic factor is a mathematical emendation.'
byid['1982-573.2']['statement']=r'For fixed \(c,h\), the induced Verma module \(M(c,h)\) has basis \(\ell_{-n_1}\cdots\ell_{-n_k}|h\rangle\), \(n_1\ge\cdots\ge n_k\ge1\), and level-\(N\) dimension \(p(N)\). Every cyclic highest-weight representation with these parameters is its quotient. Here \(h=-\Delta\) under \(\ell_n=-L_n\). The recorded generation assertion does not say whether the quotient is already irreducible. A general highest-weight vector is not the conformally invariant vacuum: the latter also has \(h=0\) and \(\ell_{-1}|0\rangle=0\).'
byid['1982-573.3']['statement']=r'In the modern convention, a primary field of weight \(\delta\) obeys \([\ell_n,\varphi(z)]=[z^{n+1}\partial_z+(n+1)\delta z^n]\varphi(z)\). Because \(L_n=-\ell_n\), the notebook reverse-bracket generators require the negative of that right-hand side. The field weight need not equal the source-module weight \(h=-\Delta\). Covariance does not determine an operator uniquely: scalar multiplication preserves it, and module channels, multiplicities and normalization must be specified. For fixed generic source and target Verma modules, formal descendant matrix elements can be recursively fixed from a compatible leading matrix element.'
byid['1982-573.3']['reconstruction']=r'The covariance sign, field weight, source and target data and normalization are made consistent. No unrestricted existence or uniqueness of intertwiners is asserted.'
byid['1982-573.6']['statement']=r'For the reverse Witt bracket of the notebook, set \(\ell_n=-L_n\) and \(h=-\Delta\). In the corresponding central normalization, write \(c=13-6(t+t^{-1})\), \(t\ne0\). Reducibility means \(h=((rt-s)^2-(t-1)^2)/(4t)\) for some \(r,s\ge1\), and the first singular level is the least such \(rs\). Thus the recorded \(-\Delta\) is exactly \(h\), and its two-factor polynomial has the correct Kac form. At level two the Gram determinant is \(2h[16h^2+(2c-10)h+c]\): at \(c=0\), \(h=5/8\) corresponds to the recorded \(\Delta=-5/8\).'
byid['1982-573.6']['reconstruction']=r'The recorded polynomial is preserved under \(h=-\Delta\), \(\ell_n=-L_n\). The first-level assertion requires a minimum over coincident degeneracy conditions.'
byid['1982-573.17']['statement']=r'For the modern generators, the stress-field convention is \[\ell_n=\frac{1}{2\pi i}\oint z^{n+1}T(z)\,dz,\qquad T(z)=\sum_{n\in\mathbb Z}\ell_nz^{-n-2}.\] Since the earlier notebook generators are \(L_n=-\ell_n\), its final coefficients cannot be silently identified with these modes. Keeping the written exponent \(n-2\) requires reindexing coefficients; keeping the earlier notebook generator identification gives \(T(z)=-\sum_nL_nz^{-n-2}\). Classically these modes have Poisson brackets. Quantum Virasoro commutators require a quantum stress field and its operator product and normal ordering; a Laurent expansion alone does not provide them.'
byid['1982-573.17']['reconstruction']=r'Both the sign identification \(\ell_n=-L_n\) and the required coefficient reindexing are stated explicitly. Classical extraction and quantum commutators are separated.'
# Revise linked ledger cells without changing their stable page/place identity.
for row in C:
    if row['place']=='Opening Virasoro commutator':
        row['should_read']=r'Retain the reverse Witt term for notebook \(L_n\), but restore \(\frac{c}{12}(n^3-n)\delta_{n+m,0}\mathbf1\). Modern generators are \(\ell_n=-L_n\), with \(h=-\Delta\).'
        row['evidence']=r'Scan checked: no cubic factor is present. The written central term violates antisymmetry even at \(n=m=0\). The reverse Witt sign itself is a convention, not an independent error.'
    if row['place']=='Final Laurent series':
        row['should_read']=r'For modern \(\ell_n\), use \(T(z)=\sum_n\ell_nz^{-n-2}\). With earlier notebook \(L_n=-\ell_n\), this is \(-\sum_nL_nz^{-n-2}\); retaining the final exponent requires reindexing the coefficients.'
        row['evidence']=r'Scan confirms \(n-2\). Standard residue extraction is \(\ell_n=(2\pi i)^{-1}\oint z^{n+1}T(z)\,dz\). One cannot use the same labels unaltered in all three notebook formulas.'
def add_corr(page,place,reads,should,evidence,typ='faithful_error'):
    if any(x['page']==page and x['place']==place for x in C):return
    C.append(dict(page=page,place=place,transcription_reads=reads,should_read=should,evidence=evidence,applies_to='both',type=typ))
add_corr('P001037','Agenda item 7, large-rank equality',r'\(u(\infty)=sp(\infty)=O(\infty)\).',r'Interpret only as an informal leading-planar comparison after fixing theories and coupling normalizations; do not identify the direct-limit classical Lie algebras.',r'Scan P001037 and Russian checked. The equality occurs in the physics agenda. The classical matrix series have different Lie-algebra structures and nonorientable corrections; no exact algebra isomorphism follows.', 'ambiguity')
add_corr('P001039-P001040','Conjugated noise and spacetime covariance',r'Finite matrix noise transported as \(J(x,\tau)=e^{ipx}\bar J(\tau)e^{-ipx}\) replaces the spacetime noise.',r'Keep this as a regulated quenched planar prescription; it is not an exact realization of independent spacetime white noise at finite \(N\).',r'Each fixed pair of matrix entries has a single spatial phase \(e^{i(p_i-p_j)x}\), so its covariance cannot equal a spatial delta distribution before the specified large-rank and momentum-averaging limits.','ambiguity')
add_corr('P001058','Primary covariance sign with the reverse Witt bracket',r'\([L_n,\varphi]=[z^{n+1}\partial_z+(n+1)\Delta z^n]\varphi\).',r'For notebook \(L_n=-\ell_n\), use the negative of the standard primary differential operator, with the field weight specified separately.',r'Jacobi applied to two mode commutators gives the standard \((n-m)\) bracket for the printed positive primary law, contrary to the notebook \((m-n)\) term. The sign conversion repairs this independently of the scalar-normalization ambiguity.')
# Metadata verification completed in this shard after the sibling supplied the exact institutional URL.
B=B.replace('Published 2024 metadata separately checked in the author institutional record by the collaborating shard; direct publisher DOI inaccessible here.', 'Published 2024 metadata independently opened at the University of Helsinki institutional record; direct publisher DOI inaccessible here.')
# Repair accumulated BibTeX accent escapes, and unsupported Math-Net macro.
B=re.sub(r'\\{2,}(["\'^])',lambda m:'\\'+m.group(1),B).replace(r'{\cprime}',"'")
for f,obj in [('items',I),('talks',T),('problems',P)]:
    (D/(f+'.json')).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
with (D/'corrections.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type'])
    w.writeheader();w.writerows(C)
(D/'references.bib').write_text(B)
# Parse braced BibTeX fields even when several fields occupy one line.
def field(e,name):
    m=re.search(r'\b'+name+r'\s*=\s*\{',e,re.I)
    if not m:return None
    start=m.end();depth=1;pos=start
    while pos<len(e):
        ch=e[pos]
        if ch=='{' and (pos==0 or e[pos-1]!='\\'):depth+=1
        if ch=='}' and (pos==0 or e[pos-1]!='\\'):
            depth-=1
            if depth==0:return e[start:pos]
        pos+=1
    raise ValueError((name,e[:100]))
entries={}
for e in re.split(r'(?=^@)',B,flags=re.M):
    m=re.match(r'@\w+\{([^,]+),',e)
    if m:entries[m.group(1)]=e
full=set('dirac1950generalized tong2009string bahns2004string bahnsmeinecke2011string enriquezhalbout2010quantization yangmills1954conservation thooft1971massive lanford1982feigenbaum golbergsinaikhanin1983tripling jakobson1980invariant thooft1974planar collinsguionnetmaurel2009asymptotics maeta2026regularized gelfandfuchs1968circle feiginfuchs1982invariant neretin1983highest polyakov1981quantum ginzburg1983integrals davidkupiainenrhodesvargas2016liouville ginzburg1983symplectic hormander1971fourier homanzhou2017radon donaldson1983selfdual thom1954globales witten1982supersymmetry enss1989longrange frohlichspencer1981transition frohlichpfisterspencer1982surfaces cheegermullerschrader1984curvature belavinpolyakovzamolodchikov1984infinite guillarmoukupiainenrhodesvargas2024bootstrap'.split())
S={}
for key,e in entries.items():
    S[key]=dict(opened_url=field(e,'url'),verification='read the result' if key in full else 'publisher metadata checked',locator_and_scope=field(e,'annote'),checked='2026-11-11')
S['guillarmoukupiainenrhodesvargas2024bootstrap']['additional_opened_urls']=['https://arxiv.org/abs/2005.11530','https://researchportal.helsinki.fi/en/publications/conformal-bootstrap-in-liouville-theory/']
S['guillarmoukupiainenrhodesvargas2024bootstrap']['locator_and_scope']+=' Theorem 6.25, preprint pp.62--63, states the spectral resolution and absolute continuity. Theorem 1.1 requires alpha_i<Q and alpha_1+alpha_2>Q, alpha_3+alpha_4>Q; no unrestricted charge statement.'
S['frohlichpfisterspencer1982surfaces']['additional_opened_urls']=['https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/FROHLICH/1981-2002/P_82_20/P_82_20_web.pdf']
S['ginzburg1983integrals']['additional_opened_urls']=['https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=rus&paperid=10001&what=fullt']
S['alfarosakita1983quenched']['locator_and_scope']+=' July preprint evidence was an indexed INSPIRE record; original preprint full text not read. Do not elevate this to full theorem verification.'
S['neretin1983highest']['additional_opened_urls']=['https://www.mathnet.ru/eng/faa1567']
(D/'source_audit.json').write_text(json.dumps(S,ensure_ascii=False,indent=2)+'\n')
# Stable existing row positions plus exact new places; output page/place pairs for final sorting.
M={
'561.1':[1],'561.2':[2,3],'561.4':[4],'561.10':[5,6],
'562.1':[7],'562.2':[8],'562.3':[9],'562.4':[10,11],'562.8':[12],
'563.1':[13],'563.7':[14],'564.2':[15],'564.4':[16],
'565.1':[18,76],'565.2':[19],'565.4':[20,77],'565.5':[21,22],
'566.4':[24],'566.5':[25],'566.7':[26],'566.9':[27],
'567.5':[28],'567.6':[29],'567.7':[30],'567.8':[31],'567.12':[33],
'568.6':[35],'569.7':[38],'569.8':[39],'569.10':[41],'570.5':[44],
'571.2':[45],'571.7':[49],'571.10':[50],'571.12':[51],'571.14':[52],'571.15':[53],
'572.5':[57],'572.12':[60],'572.13':[61],
'573.1':[65],'573.3':[66,78],'573.9':[69,70],'573.12':[71],'573.15':[72],'573.16':[73,74],'573.17':[75]
}
mapping={'1982-'+k:[[C[n-1]['page'],C[n-1]['place']] for n in ns] for k,ns in M.items()}
false={x['id'] for x in I if x['literal_correctness']=='false as written'}
assert set(mapping)==false,(set(mapping)-false,false-set(mapping))
ids={x['id'] for x in I}; keys=set(entries); problems={p['id'] for p in P}
errors=[]
for t in T:
    its=[x for x in I if x['record']==t['record']]
    if [x['id'] for x in its]!=[f"1982-{t['record']}.{n}" for n in range(1,len(its)+1)]:errors.append('nonconsecutive '+str(t['record']))
for x in I:
    if not set(x['refs'])<=keys:errors.append('missing refs '+x['id'])
    if x['class'] in ['C','D'] and not x['worth']:errors.append('missing worth '+x['id'])
    if x['problem'] and x['problem'] not in problems:errors.append('missing problem '+x['id'])
    cited=set()
    for v in x.values():
        if isinstance(v,str):
            for m in re.finditer(r'\\cite\w*(?:\[[^\]]*\])?\{([^}]+)\}',v):cited.update(z.strip() for z in m.group(1).split(','))
    if not cited<=set(x['refs']):errors.append('citation/refs mismatch '+x['id']+' '+str(cited-set(x['refs'])))
for key in keys:
    if not S[key]['opened_url'] or not S[key]['locator_and_scope']:errors.append('missing audit '+key)
for p in P:
    if not set(p['refs'])<=keys:errors.append('problem refs '+p['id'])
    for occurrence in p['occurrences']:
        if occurrence.startswith('1982-') and occurrence not in ids:errors.append('missing occurrence '+occurrence)
catalog=(D.parents[1].parent/'upload/GY1982_talks.md').read_text()
for t in T:
    expected=re.search(r'record '+str(t['record'])+r':.*?pages ([^;]+)',catalog).group(1)
    if t['pages']!=expected:errors.append('catalog range '+str(t['record']))
report=dict(records=len(T),items=len(I),problems=len(P),corrections=len(C),references=len(keys),items_by_class=dict(collections.Counter(x['class'] for x in I)),false_as_written_to_corrections=mapping,validation_errors=errors,status_date='2026-11',notes=['Record 573.6 preserves the Neretin polynomial under ell_n=-L_n, h=-Delta; it is not labelled false.','Modern generators in record 573 use ell_n; notebook quotations retain L_n.','Bibliography access levels are in source_audit.json; receipt dates are not public circulation dates.','The sole class C is the exact Migdal four-unitary all-coupling integral, developed by root.','Root handles the complete chapter build and final typography.'])
(D/'validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
assert not errors,errors
print(json.dumps({k:v for k,v in report.items() if k not in ['false_as_written_to_corrections','notes']},ensure_ascii=False,indent=2))
note='''\n## Final convention and audit pass\nAll 13 records are complete: 147 items, 9 problem identifiers, 78 correction rows and 54 bibliography entries. Source-audit verification distinguishes full original/preprint reading from publisher or institutional metadata and indirect antecedents. The supplied catalogue range for565 is restored to P001037--P001042; fine item pages retain actual boundaries. Speakers562/567/569/573 are A.B.Zamolodchikov,570 retains catalogueV.L.Ginzburg with the V.A. identification caveat in its body;571/572 use J.Fröhlich (the primary author is Jürg, not Jürgen). Exact previous Springer occurrences1971-231.2 and1971-231.5 added. Scans1037 and1044 inspected in the final pass for the agenda equality and endpoint/Jacobian formula. Hyperbola finite-part wording corrected: the fixed distribution family determines its coefficient; the axis representation requires a consistent prescription. The full modern notation of573 is ell_n=-L_n,h=-Delta. Neretin's polynomial is correct with that convention; a separate ledger row records the incompatible positive primary covariance law. The final Laurent labels need coherent sign/index conversion. Theorem6.25 of the Liouville preprint was read directly on pp62--63; it explicitly states absolute continuity. Helsinki institutional metadata independently opened at https://researchportal.helsinki.fi/en/publications/conformal-bootstrap-in-liouville-theory/ confirms Acta233(1),33--194(2024),DOI10.4310/ACTA.2024.v233.n1.a2. All47 false-as-written items map to exact page/place ledger pairs. Final-audit code is reproducible by running compile_shard.py followed by finalize_audit.py. Root handles build/upload and typography.\n'''
log=(D/'research_notes.md').read_text()
if '## Final convention and audit pass' in log:log=log.split('## Final convention and audit pass')[0]
(D/'research_notes.md').write_text(log+note)
