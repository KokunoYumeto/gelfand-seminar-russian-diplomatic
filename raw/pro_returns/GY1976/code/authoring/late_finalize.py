from pathlib import Path
p=Path('work/late_author.py')
s=p.read_text()
start=s.index("item(412,'P000691-P000693','remark','Rank-one solitons")
end=s.index("\ncorrection('P000690'",start)
replacement=r"""
item(412,'P000691-P000693','construction','The rank-one nodal construction includes KdV multisolitons',
 r'''The notes identify the rank-one case with \(N\)-soliton solutions of KdV and its hierarchy.''',
 r'''Take scalar coefficients \(\ell=1\), spectral rank \(r=1\), paired spectral points with a common sum, and the nodal gluing data of the preceding construction. On any parameter domain where the interpolation determinant is nonzero, the quadratic spectral function gives a second-order scalar differential operator. Choosing the compatible cubic time flow yields the KdV Lax equation after the usual normalization; its nodal specialization includes the classical multisoliton family.''',
 r'''This does not assert that every arbitrary gluing matrix yields a globally smooth real soliton. The real multisoliton subclass needs real spectral choices and a nonvanishing real denominator; the notebook states neither global regularity nor those restrictions.''',
 cls='E',fate=r'''The identification is explicit in \citet[Ch.~III, \S5.13]{manin1978algebraic}. The rank-one multisoliton family is treated there as known, whereas the uniform higher-rank module construction is the newer part.''',
 status='the stated local construction includes the established rank-one soliton family.',
 match='exact',refs=MANIN)

item(412,'P000693','question','The unqualified question about N-soliton behaviour',
 r'''The talk ends with \ru{Вопрос: поведение \(N\)-солит. решения?}.''',
 r'''No equation, spectral rank, reality or nonsingularity conditions, time direction, or requested observable is specified in the final question.''',
 r'''It cannot be equated with the earlier two-soliton phase-shift problem GP-1973-54 or promoted to a new higher-rank scattering conjecture merely because of the preceding examples.''',
 cls='F',fate=r'''The surrounding soliton construction is matched by \citet[Ch.~III, \S5.13 and \S6]{manin1978algebraic}, but no definite final question was identified.''',
 status='the final question is too underspecified to support an open-problem claim.',
 literal='not determinable',match='thematic only',development='annotated',refs=MANIN,confidence='medium')
"""
s=s[:start]+replacement+s[end:]
s=s.replace("The English PDF's OCR also gives an unreliable plus in its displayed theorem; the commutator derivation determines the sign.",
"Independent visual inspection of the published English Theorem~2.6, p.~83, confirms a printed plus rather than an OCR artifact. Its connection conventions likewise require a difference; the notebook and publication both need a mathematical sign correction.")
s+=r"""

# Exact recurrence of the scalar filtered-module mechanism; share the audited definition.
for it in items:
    if it['id']=='1976-412.3':
        it['problem']='GP-1975-26'
        it['reconstruction']+=r''' The scalar specialization \(\ell=1\) is the filtered-module reconstruction mechanism in GP-1975-26; the occurrence does not replace its pointed-curve and local-data hypotheses by a bare curve and bundle. Matrix coefficients and the later explicit nodal examples are additional scope, not a changed definition of that earlier problem.'''
shared=next(p for p in json.loads((WORK/'middle_problems.json').read_text()) if p['id']=='GP-1975-26')
shared['occurrences']=list(dict.fromkeys(shared['occurrences']+['1976-412.3']))
shared['refs']=list(dict.fromkeys(shared['refs']+MANIN))
problems.append(shared)
checkpoint()
print(json.dumps({'talks':len(talks),'items':len(items),'problems':len(problems),'classes':dict(Counter(x['class'] for x in items)),'by_record':dict(Counter(str(x['record']) for x in items)),'corrections':len(corrections)},indent=2))
"""
p.write_text(s)
