#!/usr/bin/env python3
"""Apply documented final typography and notation fixes to assembled data.

These changes preserve the mathematical assessments and source locators.
They place long formulas in displays, restore escaped macros, and separate
joined bibliographic prose. Every actual change is recorded with before/after
text. Run after assembly, before building; already-applied changes are skipped.
"""
from pathlib import Path
import argparse
import csv
import json
import re
from chapter_checks import bib_entries,bib_field


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory',type=Path,nargs='?',default=Path('.'))
    args=parser.parse_args()
    root=args.directory
    items=json.loads((root/'GY1982_items.json').read_text())
    problems=json.loads((root/'GY1982_problems.json').read_text())
    talks=json.loads((root/'GY1982_talks.json').read_text())
    corrections=list(csv.DictReader((root/'GY1982_corrections.csv').open()))
    changes=[]
    def setfield(obj,field,new,location,reason):
        old=obj[field]
        if old!=new:
            obj[field]=new
            changes.append({'location':location+'.'+field,'reason':reason,'before':old,'after':new})
    def prose(value):
        value=value.replace('\\\\ours',r'\ours')
        value=re.sub(r'\b(Theorems?|Lemmas?|Propositions?|Corollaries?|Remark|Sections?|sections?|Equations?|equations?)(?=\d)',r'\1~',value)
        value=value.replace('inApril1981','in April 1981')
        value=value.replace('receivedApril1987','received April 1987').replace('publishedJune1988','published June 1988')
        value=re.sub(r'\b(and|predates|in|The|is|on|level|near|cutoff)(?=\d)',r'\1 ',value)
        value=value.replace('pp208','pp. 208')
        value=re.sub(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)(?=\d{4})',r'\1 ',value)
        value=re.sub(r'\b(Pohlmeyer|Bahns|Schwarz|Lanford|Fuchs|Polyakov)(?=\d{4})',r'\1 ',value)
        value=re.sub(r'\b([Ss]cans?|Russian)(?=\d)',r'\1 ',value)
        value=value.replace('records596 and598','records 596 and 598')
        for old,new in [('circulated2008','circulated in 2008'),('published2010','published in 2010'),
                        ('received28June1982','received 28 June 1982'),('published1983','published in 1983')]:
            value=value.replace(old,new)
        return value
    for container in [items,problems,talks]:
        for obj in container:
            for field in ['notes','statement','reconstruction','fate','present_status','worth','status','summary']:
                if field in obj:
                    setfield(obj,field,prose(obj[field]),obj.get('id',str(obj.get('record'))),'Macro/prose spacing repair')
    by_id={x['id']:x for x in items}
    for talk in talks:
        if talk['record'] in {562,567,569,573}:
            setfield(talk,'speaker','A. B. Zamolodchikov',str(talk['record']),
                     'The supplied catalog explicitly says Al-dr.B. for Alexander in all four records; avoid conflation with Alexei')
        if talk['record'] in {570,583,593,596}:
            setfield(talk,'speaker','V. L. Ginzburg',str(talk['record']),
                     'Preserve the catalog initials consistently; related publications do not identify the speaker')
        if talk['record']==570:
            summary=r'The actual entry occupies P001050 and the upper part of P001051, before Fröhlich. The catalogue attribution to V. L. Ginzburg is retained; the notebook gives only V. Ginzburg and explicitly presents the material after Guillemin--Sternberg. The full speaker identity has not been independently resolved from another dated seminar source. V. A. Ginzburg’s 1983 paper is used for mathematical comparison, without identifying its author as this speaker. The talk relates a regular coisotropic quotient to a symmetric idempotent canonical relation and an operator algebra, then Shmelyov gives the conormal embedding condition for a double fibration.'
            setfield(talk,'summary',summary,'570','Withdraw an unsupported speaker-identity inference; retain catalog and manuscript evidence')
    edits={
        '1982-561.6':{'reconstruction':'Irreducibility, integrability, level and the quotient qualification make the notebook’s “most economical” precise.'},
        '1982-562.1':{
            'notes':r'The target metric is \(\operatorname{diag}(1,-1,\ldots,-1)\), while the written integrand is \[\sqrt{\dot X^2(X^{\prime})^2-(\dot X\cdot X^{\prime})^2}.\]',
            'statement':r'For a timelike immersed worldsheet with induced metric \(h_{ab}=\partial_aX\cdot\partial_bX\), a real action, with \(T>0\), is \[\begin{aligned} S&=-T\int\sqrt{-\det h}\,d\tau\,d\sigma\\ &=-T\int\sqrt{(\dot X\cdot X^{\prime})^2-\dot X^2(X^{\prime})^2}\,d\tau\,d\sigma.\end{aligned}\] Degenerate worldsheets need separate treatment.'},
        '1982-562.2':{'fate':r'Dirac developed the framework in August 1949 lectures and \citet[Sections~2--4]{dirac1950generalized}. The string specialization is checked by differentiating the action.'},
        '1982-565.6':{
            'notes':r'Equation (19) asks for \[\lim_{N\to\infty}N^{-2}\log\int\exp\!\left[-\beta N\sum_{\mu,\nu=1}^4\operatorname{tr}(U_\mu U_\nu U_\mu^\dagger U_\nu^\dagger)\right]\prod_{\mu=1}^4dU_\mu.\] The minus sign and the complete ordered double sum are visible in the scan.',
            'statement':r'With normalized Haar measures on \(U(N)\), set \[Z_N(\beta)=\int_{U(N)^4}\exp\!\left[-\beta N\sum_{\mu,\nu=1}^4\operatorname{tr}(U_\mu U_\nu U_\mu^\dagger U_\nu^\dagger)\right]dU.\] Determine \(F(\beta)=\lim_{N\to\infty}N^{-2}\log Z_N(\beta)\) for real \(\beta\), including existence, analytic branches and transition values. The sum is real because ordered off-diagonal terms are conjugate pairs; diagonal terms contribute \(4N\).'},
        '1982-567.2':{'reconstruction':'We add the bounded smooth planar domain, regularity and harmonicity assumptions, and exclude branch points when claiming immersion.'},
        '1982-568.2':{'reconstruction':'The statement specifies a complex algebraic group and properness. It also distinguishes the group construction from the Lie algebra construction.'},
        '1982-569.3':{'notes':r'A margin says:\par\ru{В \(\infty\)-мерном пр-ве почти \(\forall\) две меры взаимно сингулярны}.'},
        '1982-569.6':{'notes':r'Equation (6) gives the two formal quadratic expressions \[\|\delta x\|^2=\int\sqrt g\,|\delta x|^2,\] \[\|\delta g\|^2=\int\sqrt g\,(g^{aa\prime}g^{bb\prime}+c\,g^{ab}g^{a\prime b\prime})\delta g_{ab}\delta g_{a\prime b\prime}.\]'},
        '1982-571.3':{'reconstruction':'We specify closedness, smoothness, orientation and cohomology coefficients, as well as the sign relating charge to self-duality.'},
        '1982-577.6':{'fate':r'See \citet[section~1]{zograftakhtajan1988liouville} for the normalization of the projective connection.'},
        '1982-581.8':{'notes':r'Gelfand asks:\par\ru{Построить p-адич. аналог предст. группы диффеоморфизмов}.'},
        '1982-583.14':{'fate':r'\citet[sections 2--4]{vergne1979rossmann} proves Rossmann’s character formula using oscillators and intertwining operators. The manuscript was received in March 1979, revised in July 1979, and published in 1979.'},
        '1982-591.4':{'fate':r'\citet[\S3.7 and \S6]{drinfeldsokolov1985lie} develops the Miura transformation and generalized hierarchies. Its introduction identifies \citet{drinfeldsokolov1981equations} as the earlier Doklady announcement; the latter’s publication metadata was checked. Thus this is pre-talk mathematics despite the full survey’s 1984 Russian and 1985 English publication dates.'},
    }
    for item_id,fields in edits.items():
        if item_id not in by_id:continue
        for field,value in fields.items():
            setfield(by_id[item_id],field,value,item_id,'Display long formulas or reflow prose without changing scope')
    for p in problems:
        if p['id']=='GP-1982-02':
            new=r'For four independent probability-Haar matrices in \(U(N)\), set \[Z_N(\beta)=\mathbb E\exp\!\left[-\beta N\sum_{\mu,\nu=1}^4\operatorname{tr}(U_\mu U_\nu U_\mu^\dagger U_\nu^\dagger)\right].\] Determine the existence and value of \(F(\beta)=\lim_{N\to\infty}N^{-2}\log Z_N(\beta)\) for all real \(\beta\), including analytic branches and transition values. The full ordered sum and negative exponent are retained.'
            setfield(p,'statement',new,p['id'],'Display the exact integral and make its normalization explicit')
    raw_replacements=[
        ('t^{-1}',r'\(t^{-1}\)'),
        ('tr(B_{2k+1}dB_{2l+1})=(2l+1)t^{k+l}dt',r'\(\operatorname{tr}(B_{2k+1}dB_{2l+1})=(2l+1)t^{k+l}dt\)'),
        ('k+l=-1',r'\(k+l=-1\)'),
        ('x_k and x_{2k+1}',r'\(x_k\) and \(x_{2k+1}\)'),
        ('(p+X prime)^2=(p-X prime)^2=0',r'\((p+X^{\prime})^2=(p-X^{\prime})^2=0\)'),
        ('Every written F_k kills1',r'Every written \(F_k\) kills \(1\)'),
        ('commutator on1 is0','commutator on \\(1\\) is \\(0\\)'),
        ('Neretin1983 Theorem2','Neretin (1983), Theorem 2'),
        ('(2d)^N',r'\((2d)^N\)'),
        ('Kinetic coefficient1/2','Kinetic coefficient \\(1/2\\)'),
        ('|p|^2/2',r'\(|p|^2/2\)'),
        ('gives generator \\(|p|^2/2\\)','gives positive kinetic symbol \\(|p|^2/2\\)'),
        ('Scans1030–31','Scans 1030–31'),('Scan1042','Scan 1042'),('Russian1044','Russian page 1044'),
    ]
    for n,row in enumerate(corrections,1):
        if row['page']=='P001050' and row['place']=='Speaker heading and catalogue attribution':
            setfield(row,'should_read',
                     'Retain V. L. Ginzburg as the catalogue attribution and V. Ginzburg as the notebook reading. Do not expand the manuscript initial to V. A. without direct identity evidence.',
                     f'corrections data row {n}','Withdraw an unsupported speaker-identity inference')
            setfield(row,'evidence',
                     r'The scan reads only \ru{В. Гинзбург} and labels the presentation as following Guillemin--Sternberg. The cited 1983 paper is by V. A. Ginzburg, but its authorship and mathematical relevance do not identify the speaker. No independent dated identification was found.',
                     f'corrections data row {n}','Keep author identification separate from speaker identification')
        for field in ['place','transcription_reads','should_read','evidence']:
            value=prose(row[field])
            for old,new in raw_replacements:
                if old in value and new not in value:value=value.replace(old,new)
            setfield(row,field,value,f'corrections data row {n}','Put mathematical notation in valid LaTeX math mode')
    for suffix,container in [('talks',talks),('items',items),('problems',problems)]:
        (root/f'GY1982_{suffix}.json').write_text(json.dumps(container,ensure_ascii=False,indent=2)+'\n')
    with (root/'GY1982_corrections.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type'])
        writer.writeheader();writer.writerows(corrections)
    bib=root/'GY1982_references.bib'
    before=bib.read_text()
    after=before.replace('{\\cprime}',"'").replace('\\cprime',"'").replace('Teichm"uller','Teichmüller')
    if after!=before:
        changes.append({'location':'GY1982_references.bib','reason':'Use standard apostrophe instead of unsupported cprime macro and render Teichmüller with its Unicode umlaut'})
    entries=bib_entries(after)
    gee=entries.get('gee2026modularity','')
    if gee and not bib_field(gee,'publisher'):
        amended=gee.replace('  author =', '  publisher = {Society for Industrial and Applied Mathematics},\n  editor = {Friedlander, Susan and Tschinkel, Yuri},\n  author =',1)
        after=after.replace(gee,amended)
        changes.append({'location':'gee2026modularity.publisher/editor',
                        'reason':'Verified in the SIAM page Information/Authors section: publisher, editors, and online date 13 July 2026',
                        'source':'https://epubs.siam.org/doi/full/10.1137/25M1806697'})
    if after!=before:bib.write_text(after)
    audit_path=root/'code/editorial_edits.json'
    audit_path.parent.mkdir(exist_ok=True)
    previous=json.loads(audit_path.read_text()) if audit_path.exists() else []
    previous.extend(changes)
    audit_path.write_text(json.dumps(previous,ensure_ascii=False,indent=2)+'\n')
    print('Recorded',len(changes),'editorial changes.')


if __name__=='__main__':main()
