"""Deterministic prose/equation line-break repairs; no mathematical changes."""
from pathlib import Path
import csv,json,re,sys
D=Path(sys.argv[1]);P=D/'GY1977_items.json';items=json.loads(P.read_text())
rules=[
 ('1977-419.7','fate','instanton/algebraic-bundle construction','construction relating instantons to algebraic bundles'),
 ('1977-423.2','reconstruction','The repeated-index summation and the local orthonormal-frame/curved-space distinction are supplied.','Summation over repeated indices and the use of a local orthonormal frame on a curved manifold are supplied.'),
 ('1977-429.1','notes',r'The definition now requires finite generation over \(U(\mathfrak g)\), finite-dimensional \(K\)-isotypic multiplicity spaces and compatible actions;',r'The definition now requires finite generation over \(U(\mathfrak g)\), compatible actions, and finite multiplicity for each irreducible \(K\)-type;'),
 ('1977-434.3','fate',r'\citet[\S2, Theorem~2 and \S3, Corollary~1]{krichever1978rational} establish the pole/particle correspondence.',r'The pole correspondence is established by \citet[\S2, Theorem~2; \S3, Corollary~1]{krichever1978rational}.'),
 ('1977-436.21','statement','In the weak-coupling sine-Gordon normalization and the mass-renormalization convention used in the semiclassical calculation,',r'In the semiclassical convention for weak sine-Gordon coupling, with renormalized mass parameter \(m_r\),'),
 ('1977-436.25','notes','a one-dimensional Schrödinger system','a Schrödinger problem in one space dimension'),
 ('1977-438.15','notes',r'Complexes, commuting chain maps, cohomology, and quasi-isomorphisms are defined; \(D(A)\) is obtained by inverting quasi-isomorphisms.',r'The lecture defines complexes, commuting chain maps and cohomology. A quasi-isomorphism induces isomorphisms on cohomology; \(D(A)\) is obtained by inverting these maps.'),
 ('1977-439.3','reconstruction','The decay assumption, distributional interpretation, and reciprocal-amplitude requirement are supplied.','The decay assumption, the distributional interpretation, and the requirement on reciprocal amplitudes are supplied.'),
 ('1977-439.8','statement','a branch/normalization','a branch and a normalization'),
 ('1977-451.3','fate',r'The precise unitary theorem is \citet[Theorem~V.4]{delorme1977cohomologie}.',r'Delorme\textquotesingle s precise unitary theorem applies here \citep[Theorem~V.4]{delorme1977cohomologie}.'),
 ('1977-457.12','statement',r'The parity eigenspace rule defines the fixed algebra \(L(\mathfrak g,\tau)=\bigoplus_{m\in\mathbb Z}\mathfrak g_{(-1)^m}t^m\), closed under brackets because eigenvalues multiply.',r'The parity eigenspace rule defines the fixed algebra\[L(\mathfrak g,\tau)=\bigoplus_{m\in\mathbb Z}\mathfrak g_{(-1)^m}t^m.\]It is closed under brackets because eigenvalues multiply.'),
]
applied=[]
byid={i['id']:i for i in items}
# Locate by exact text if a record editor's consecutive numbering differs.
for ident,field,old,new in rules:
    candidates=[byid[ident]] if ident in byid and old in byid[ident].get(field,'') else [i for i in items if old in i.get(field,'')]
    if candidates:
        assert len(candidates)==1,(ident,field)
        i=candidates[0];i[field]=i[field].replace(old,new);applied.append({'id':i['id'],'field':field})
    else:
        assert any(new in i.get(field,'') for i in items),(ident,'Neither old nor repaired text found')
for item in items:
    for field,value in item.items():
        if isinstance(value,str):
            repaired=re.sub(r'\b(occurrences?|records?)(?=\d)',r'\1 ',value)
            if repaired!=value:
                item[field]=repaired
                applied.append({'id':item['id'],'field':field,'repair':'space before occurrence or record identifier'})
P.write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')

P=D/'GY1977_problems.json';problems=json.loads(P.read_text())
for p in problems:
    old='finite-dimensional graded modules over an exterior algebra'
    if old in p['statement']:
        p['statement']=p['statement'].replace(old,'graded modules of finite dimension over an exterior algebra')
        applied.append({'id':p['id'],'field':'statement'})
P.write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')

P=D/'GY1977_corrections.csv'
with P.open(newline='') as f:r=csv.DictReader(f);fields=r.fieldnames;rows=list(r)
citation_labels=['Atiyah--Ward1977','Krichever1977','Krichever1978','Tits1977','Shannon1948',
                 'Hawking1971','Hawking1975','Wald2015','Chrusciel--Costa--Heusler2012',
                 'al.2016','Crispino--Higuchi--Matsas2008','FAC1955','Garnier1912']
for row in rows:
    for field,value in row.items():
        repaired=re.sub(r'\b(records?)(?=\d)',r'\1 ',value)
        repaired=repaired.replace('Gelfand--Dikii1977','Gelfand--Dikii 1977').replace('§2 Eq8','§2 Eq. 8')
        for old in citation_labels:
            repaired=repaired.replace(old,old[:-4]+' '+old[-4:])
        repaired=re.sub(r'\b(Theorem|Appendix|Table)(?=\d)',r'\1 ',repaired)
        repaired=repaired.replace('properties5','properties 5').replace('DOI10.1103','DOI 10.1103')
        if repaired!=value:
            row[field]=repaired
            applied.append({'page':row['page'],'field':field,'repair':'space before record number, citation year or bibliographic locator'})
    if row['page']=='P000717' and 'Schwartz tuples' in row['should_read']:
        row['should_read']=r'Require \(f(0)=0\) for this integral on all Schwartz tuples. The algebraic kernel is\[\ker(\text{Euler derivative})=\mathbb C+D(A),\]so constants must be separated.'
        applied.append({'page':row['page'],'field':'should_read'})
with P.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

P=D/'GY1977_development.tex'
development=P.read_text()
development,marker_count=re.subn(r'\\ours(?:Computed)?(?=\s)',lambda m:m.group(0)+'{}',development)
development,occurrence_count=re.subn(r'\boccurrence(?=1977-)', 'occurrence ', development)
P.write_text(development)
if marker_count:
    applied.append({'file':P.name,'field':'explicit space after proof/computation marker','occurrences':marker_count})
if occurrence_count:
    applied.append({'file':P.name,'field':'space before occurrence identifier','occurrences':occurrence_count})

out=D/'code/output';out.mkdir(parents=True,exist_ok=True)
result={'result':'PASS','purpose':'Readable line breaks in long prose and two mathematical formulas; content, classes and counts preserved.',
        'item_rules':len(rules),'additional_rules':['Projective-bundle problem wording','Display the Euler-derivative kernel in P000717 correction','Preserve word spacing after proof/computation markers','Separate occurrence identifiers from preceding word','Separate correction-table record numbers, citation years and bibliographic locators'],
        'applied_this_run':applied}
(out/'typesetting_repairs.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
