"""Apply explicit final editorial decisions after assembling the research blocks.

The complete before/after log is saved. Canonical problem IDs are assigned
in order of first occurrence; no earlier-year problem IDs were supplied.
"""
from pathlib import Path
import json
import re
import sys
import csv
from assemble_data import bib_entries

WORK=Path(__file__).resolve().parents[1]
OUT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else WORK/'output'

def main():
    items=json.loads((OUT/'GY1964_items.json').read_text())
    talks=json.loads((OUT/'GY1964_talks.json').read_text())
    problems=json.loads((OUT/'GY1964_problems.json').read_text())
    changes=[]
    byid={x['id']:x for x in items}
    byproblem={p['id']:p for p in problems}
    if 'GP-1964-A01' not in byproblem:
        raise RuntimeError('Run assemble_data.py first: finalization requires the provisional research-block problem IDs and must not be applied twice.')
    def edit(obj,field,value,reason):
        if obj.get(field)!=value:
            changes.append({'id':obj.get('id',obj.get('record')),'field':field,
                            'before':obj.get(field),'after':value,'reason':reason})
            obj[field]=value
    x=byid['1964-3.12']
    addition=r''' The later published bound is \(\mu\le2.662343\),
from \citet{couronne2025bound} (preprint first posted 29 November 2022;
journal publication 31 October 2025). An author-posted preprint of
21 October 2026, \citet{tomar2026connective}, claims \(\mu\le2.6586513\);
its certificate was not independently rerun here. Neither value is an exact
determination of the square-lattice constant.'''.replace('\n',' ')
    edit(x,'present_status',x['present_status']+addition,
         'Add current primary-source bounds, keeping the 2026 certificate a preprint claim.')
    edit(x,'refs',list(dict.fromkeys(x['refs']+['couronne2025bound','tomar2026connective'])),
         'References for the added current-status comparison.')
    p=byproblem['GP-1964-01']
    edit(p,'status',p['status']+addition,'Keep problem status consistent with occurrence 3.12.')
    edit(p,'refs',list(dict.fromkeys(p['refs']+['couronne2025bound','tomar2026connective'])),
         'Current bounds in problem status.')
    p=byproblem['GP-1964-02']
    edit(p,'statement',r'''Does every bounded linear operator on a separable
infinite-dimensional complex Hilbert space \(H\) admit a closed invariant
subspace \(M\) with \(0\ne M\ne H\)?'''.replace('\n',' '),
         'Merge the repeated occurrence into one precise question.')
    edit(p,'status',r'''As of 12 November 2026, no generally accepted solution
was verified in the literature checked. \citet[Introduction]{marcoux2026generators},
first posted 21 August 2026, explicitly states this Hilbert-space question as
unsolved. The 1964 announcement \citep{debrangesrovnyak1964existence} was
retracted in 1965 \citep{debrangesrovnyak1965correction}; these records are
bibliographically verified, not treated as valid proofs. Polynomially compact
and other special classes in record 50 do not settle the unrestricted question.'''.replace('\n',' '),
         'Resolve differing block status formulations using the checked current primary source.')
    edit(p,'refs',list(dict.fromkeys(p['refs']+['marcoux2026generators',
         'debrangesrovnyak1964existence','debrangesrovnyak1965correction'])),
         'Union of sources needed for the merged historical/current status.')
    x=byid['1964-50.20']
    edit(x,'literal_correctness','false as written',
         'The unrestricted no-invariant-subspace suggestion fails in verified arithmetic classes; the literal every-vector formulation also includes zero.')
    edit(x,'reconstruction',r'''The universal affirmative invariant-subspace
question is a modern reformulation. The source suggests a counterexample
without precisely delimiting the parameter set; its statement that every
vector is cyclic must in any case exclude the zero vector.'''.replace('\n',' '),
         'Keep the source conjecture separate from the modern residual question.')

    x=byid['1964-44.2']
    edit(x,'statement',r'For \(n\ge2\), the brightness function '+x['statement'].removeprefix('The brightness function '),
         'Independent spring review: dimension one is a counterexample to brightness uniqueness.')
    x=byid['1964-50.7']
    edit(x,'fate',x['fate'].replace(
        'Thus both arguments circulated before this May 1965 lecture although publication followed it.',
        'Both manuscripts had been submitted before this May 1965 lecture, although publication followed it; the receipt dates alone do not establish public circulation.'),
         'Independent spring review: submission is not evidence of public circulation.')

    # Explicit mathematical displays avoid overflowing long inline expressions.
    edit(byid['1964-3.1'],'statement',r'''Let \(\Lambda\subset\mathbb Z^\nu\)
be finite and choose \(N\in\{0,\ldots,|\Lambda|\}\). For
\(\eta_x\in\{0,1\}\) with \(\sum_{x\in\Lambda}\eta_x=N\), set
\[
H_\Lambda(\eta)=-\sum_{\substack{\{x,y\}\subset\Lambda\\|x-y|_1=1}}
\eta_x\eta_y,\qquad
Z_{\Lambda,N}=\sum_{\eta:\,\sum_x\eta_x=N}e^{-H_\Lambda(\eta)/T}.
\]
Here \(T>0\), each unordered nearest-neighbor pair is counted once,
and the canonical law is the normalized weight. With
\(\eta_x=(1+\sigma_x)/2\) this is an Ising model with the corresponding
fixed magnetization and boundary terms.'''.replace('\n',' '),
         'Display the energy and partition function; make admissible particle counts and pair-counting explicit.')
    x=byid['1964-9.2']
    edit(x,'statement',x['statement'].replace(
        r'\(Z_N=(N!h^{dN})^{-1}\int e^{-H_N/T}\,dq\,dp\).',
        r'\[Z_N=(N!h^{dN})^{-1}\int e^{-H_N/T}\,dq\,dp.\]'),
         'Place the partition integral on a separate line to avoid an overfull box.')
    x=byid['1964-11.1']
    edit(x,'statement',x['statement'].replace('normalized positive-definite conjugation-invariant functions',
        'normalized positive-definite functions invariant under conjugation'),
         'Equivalent wording with natural line breaks.')
    x=byid['1964-15.1']
    edit(x,'notes',x['notes'].replace(r'\ae=',r'\text{\ae}='),
         'Preserve the source index symbol using a text glyph inside mathematics.')
    x=byid['1964-29.1']
    edit(x,'fate',x['fate'].replace('the compact-perturbation framework',
        'the framework for perturbations by compact operators'),
         'Equivalent wording with natural line breaks.')
    x=byid['1964-22.1']
    edit(x,'statement',r'''Let \(d\ge1\), \(V\in C^\infty(\mathbb R^d;\mathbb R)\),
and \(V(x)\to+\infty\) as \(|x|\to\infty\). Let \(P_h=-h^2\Delta/2+V\)
be its self-adjoint Schr\"odinger realization on \(L^2(\mathbb R^d)\),
and let \(N_h(E)\) count eigenvalues below \(E\), with multiplicity.
For \(E>\min V\) a regular value of \(|p|^2/2+V(x)\),
\[
N_h(E)\sim(2\pi h)^{-d}
\operatorname{vol}\{(x,p):|p|^2/2+V(x)<E\}\quad(h\downarrow0).
\]
The phase volume is finite and positive.'''.replace('\n',' '),
         'Independent winter review: asymptotic equivalence needs nonzero phase volume; specify the operator, eigenvalue count, and energy range.')
    x=byid['1964-30.7']
    edit(x,'statement',r'For integers \(n\ge2\) and \(0\le k\le n-2\), the map '+
         x['statement'].removeprefix('The map '),
         'Independent winter review: avoid undefined negative-dimensional projective-space endpoints.')
    x=byid['1964-47.2']
    edit(x,'fate',x['fate'].replace('gives the relative-resolvent/logarithmic-Jost-derivative identity',
        'gives the identity between the relative resolvent trace and the logarithmic derivative of the Jost function'),
         'Equivalent prose avoids an unbreakable slash compound in the printed citation paragraph.')
    edit(byid['1964-38.1'],'statement',r'''Over a field \(k\) of characteristic
zero, let \(A_n(k)\) be the unital associative \(k\)-algebra generated by
\(x_1,\ldots,x_n,\partial_1,\ldots,\partial_n\), with relations
\[
[x_i,x_j]=[\partial_i,\partial_j]=0,\qquad
[\partial_i,x_j]=\delta_{ij}1\quad(1\le i,j\le n).
\]
Are \(A_1(k)\) and \(A_2(k)\) isomorphic as \(k\)-algebras? They are not:
more generally, \(A_m(k)\cong A_n(k)\) implies \(m=n\).'''.replace('\n',' '),
         'Replace an overflowing inline quotient presentation by the equivalent explicit generators and relations.')

    # A definite historical research question remains indexed after its solution.
    brown_problem={
      'id':'GP-1964-BROWN',
      'title':'Invariant subspaces for subnormal operators',
      'statement':r'''Does every bounded subnormal operator on a complex
Hilbert space of dimension greater than one admit a nonzero proper closed
invariant subspace?'''.replace('\n',' '),
      'occurrences':['1964-50.5'],
      'status':r'''As of November 2026: solved affirmatively by
\citet{brown1978subnormal}, published in September 1978. The publisher's
abstract explicitly states the affirmative theorem; the full subscription
article was not read in this audit. The notebook's then-open special-class
question is distinct from the unrestricted Hilbert-space problem.'''.replace('\n',' '),
      'status_date':'2026-11',
      'refs':['brown1978subnormal'],
    }
    problems.append(brown_problem)
    changes.append({'id':'GP-1964-BROWN','field':'problem entry','before':None,
                    'after':brown_problem.copy(),
                    'reason':'Independent problem-index review identified a definite question explicitly posed as open and subsequently solved.'})
    edit(byid['1964-50.5'],'problem','GP-1964-BROWN',
         'Index the historical subnormal invariant-subspace question and its later solution.')

    # Preserve every actual occurrence in a shared problem and restore stable order.
    order=lambda s:tuple(map(int,re.fullmatch(r'1964-(\d+)\.(\d+)',s).groups()))
    for p in problems:
        actual=[x['id'] for x in items if x.get('problem')==p['id']]
        combined=sorted(set(p['occurrences'])|set(actual),key=order)
        edit(p,'occurrences',combined,'Merge all current-year back-links in source-record order.')
    problems.sort(key=lambda p:min(order(s) for s in p['occurrences']))
    mapping={p['id']:f'GP-1964-{i:02d}' for i,p in enumerate(problems,1)}
    for x in items:
        if x.get('problem'):
            edit(x,'problem',mapping[x['problem']],'Assign canonical new problem IDs in order of first occurrence.')
    for p in problems:
        edit(p,'id',mapping[p['id']],'Assign canonical new problem ID.')
    # Replace any prose mentions simultaneously, without cascading identifier changes.
    pattern=re.compile('|'.join(re.escape(k) for k in sorted(mapping,key=len,reverse=True)))
    for collection in [items,talks,problems]:
        for obj in collection:
            for k,v in list(obj.items()):
                if k not in {'id','problem'} and isinstance(v,str):
                    updated=pattern.sub(lambda m:mapping[m.group()],v)
                    edit(obj,k,updated,'Update an in-text problem-ID cross-reference.')
    for name,value in [('items',items),('talks',talks),('problems',problems)]:
        (OUT/f'GY1964_{name}.json').write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    cp=OUT/'GY1964_corrections.csv'
    with cp.open(newline='') as handle:
        reader=csv.DictReader(handle);columns=reader.fieldnames;rows=list(reader)
    for row in rows:
        for field in ['place','transcription_reads','should_read','evidence']:
            original=row[field]
            replacement=original.replace('or state a right/antirepresentation convention.',
                'or use a right action, with the antirepresentation convention stated consistently.').replace(
                'The sheaf epimorphism/local-lifting distinction gives the actual obstruction.',
                'The distinction between an epimorphism of sheaves and lifting sections locally gives the actual obstruction.')
            if original!=replacement:
                changes.append({'id':row['page']+': '+row['place'],'field':field,
                    'before':original,'after':replacement,
                    'reason':'Equivalent prose avoids an overfull correction-ledger line.'})
                row[field]=replacement
    with cp.open('w',newline='') as handle:
        writer=csv.DictWriter(handle,fieldnames=columns);writer.writeheader();writer.writerows(rows)
    bibliography=bib_entries((OUT/'GY1964_references.bib').read_text())
    for key in ['segal1965erratum','segal1965variete']:
        before=bibliography[key]
        after=before.replace('  number =', '  volume = {1964--1965},\n  number =',1)
        bibliography[key]=after
        changes.append({'id':key,'field':'bibliography','before':before,'after':after,
            'reason':'The checked source identifies the academic-year volume 1964--1965; print it with the talk number.'})
    key='sakhnovich1959triangular';before=bibliography[key]
    after=before.replace('@article{','@misc{',1).replace('  number =',
        '  howpublished = {Izvestiya Vysshikh Uchebnykh Zavedenii. Matematika, no.~1(8), pp.~180--186},\n  number =',1)
    bibliography[key]=after
    changes.append({'id':key,'field':'bibliography','before':before,'after':after,
        'reason':'Use a complete issue-and-page publication description for this volumeless periodical; do not invent a volume to satisfy the BibTeX style.'})
    key='serre1968congruence';before=bibliography[key]
    after=before.replace('  number = {330},', "  type = {Expos{\\'e}},\n  chapter = {330},")
    bibliography[key]=after
    changes.append({'id':key,'field':'bibliography','before':before,'after':after,
        'reason':'330 is the Bourbaki expose locator, not a series number.'})
    for key,entry in list(bibliography.items()):
        match=re.search(r'\btitle\s*=\s*\{',entry)
        if not match:continue
        depth=1;end=match.end();escaped=False
        while depth:
            ch=entry[end]
            if ch=='{' and not escaped:depth+=1
            elif ch=='}' and not escaped:depth-=1
            escaped=ch=='\\' and not escaped
            if ch!='\\':escaped=False
            end+=1
        original=entry[match.end():end-1]
        # Preserve the recorded title's capital letters, including personal
        # names, German nouns and mathematical acronyms, under plainnat.
        bibliography[key]=entry[:match.end()]+'{'+original+'}'+entry[end-1:]
        changes.append({'id':key,'field':'title capitalization',
                        'before':original,'after':'{'+original+'}',
                        'reason':'Protect the recorded title capitalization from BibTeX sentence-case conversion.'})
    (OUT/'GY1964_references.bib').write_text('\n\n'.join(bibliography[k] for k in sorted(bibliography))+'\n')
    (WORK/'evidence/editorial_changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
    (WORK/'evidence/problem_id_map.json').write_text(json.dumps(mapping,indent=2)+'\n')
    reviewed=[]
    for conflict in json.loads((WORK/'evidence/merge_conflicts.json').read_text()):
        if conflict.get('key') in {'debrangesrovnyak1964existence',
                                  'debrangesrovnyak1965correction',
                                  'marcoux2026generators'}:
            reviewed.append({'key':conflict['key'],'decision':'retain the first merged entry',
              'reason':'Author, year, title, pagination and source status agree. Differences are typography, redundant arXiv metadata and access annotations; the item prose records access scope.'})
        elif conflict.get('problem')=='GP-1964-02':
            reviewed.append({'problem':mapping['GP-1964-02'],'decision':'explicit merged statement and status',
              'reason':'The repeated general Hilbert-space invariant-subspace question has one entry, unioned references and both source occurrences; editorial_changes.json preserves the exact decision.'})
        else:
            raise ValueError('An unreviewed merge conflict remains: '+str(conflict.get('key',conflict.get('problem'))))
    (WORK/'evidence/merge_review.json').write_text(json.dumps(reviewed,indent=2)+'\n')
    print(f'Applied {len(changes)} explicit field changes; assigned {len(mapping)} canonical problem IDs.')
    print(json.dumps(mapping,indent=2))

if __name__=='__main__':main()
