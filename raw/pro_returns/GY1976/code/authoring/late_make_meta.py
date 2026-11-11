from pathlib import Path
import json
from collections import Counter
w=Path('work')
items=json.loads((w/'late_items.json').read_text())
talks=json.loads((w/'late_talks.json').read_text())
areas={}
for it in items:
    r=it['record'];n=int(it['id'].split('.')[-1])
    if r==411: area='Symplectic geometry and Morse theory' if n<=10 else 'Spectral geometry and harmonic analysis'
    elif r==412: area='Integrable differential equations'
    elif r==413: area='Characteristic classes and topology'
    elif r==414: area='Integral geometry'
    elif r==416: area='Algebraic geometry' if n<=3 else 'Banach space geometry'
    elif r==415: area='Symmetric group representations' if n<=9 else 'Probability and asymptotic representation theory'
    elif r==417: area='Complex geometry and flat bundles' if n<=16 else 'Differential equations and projective geometry'
    areas[it['id']]=area
meta={
 'verification_date':'2026-11-10',
 'records':[411,412,413,414,416,415,417,418],
 'catalogue_order':[411,412,413,414,415,416,417,418],
 'source_order':[411,412,413,414,416,415,417,418],
 'actual_pages':{str(t['record']):t['pages'] for t in talks},
 'inspected_scan_pages':[f'P{i:06d}' for i in range(685,707)],
 'areas':areas,
 'class_counts':dict(Counter(x['class'] for x in items)),
 'area_counts':dict(Counter(areas.values())),
 'item_counts':{str(t['record']):sum(i['record']==t['record'] for i in items) for t in talks},
 'speaker_counts':{t['speaker'] or '(year heading)':sum(i['record']==t['record'] for i in items) for t in talks},
 'source_policy':'Russian diplomatic transcription controls. English checked in parallel; actual PNGs decide formulas and boundaries. All 22 supplied pages in this segment are accounted, including next-year context. Reconstruction and primary-source evidence are separate item fields.',
 'stage':'complete segment',
 'required_record_coverage':{str(t['record']):'present' for t in talks},
 'heading_records':[418],
 'problem_ids':['GP-1976-20','GP-1976-21','GP-1976-22','GP-1976-23','GP-1976-24','GP-1976-25','GP-1976-26','GP-1975-26'],
 'unused_reserved_problem_ids':[f'GP-1976-{n:02d}' for n in range(27,40)],
 'prior_occurrence_links':{
   '1976-411.6':['1964-21.3','1966-108.6'],
   '1976-411.7':['1973-317.1'],
   '1976-412.3':['1975-391.3','1975-391.4','1976-410.7'],
   '1976-412.2':['1975-380.6','1975-383.10','1975-385.1']
 },
 'prior_link_qualification':{
   'GP-1975-26':'Reused exactly for scalar filtered-module reconstruction; shared title, statement, status and status_date copied from middle_problems.json. Matrix coefficients and nodal constructions do not broaden that earlier problem.',
   'GP-1975-14':'Not reused: the full smooth pointed-curve rank-one inverse correspondence is not restated here. Earlier 380.6, 383.9--12, 385.1/4--6 are context.',
   'GP-1973-54':'Not reused for the unspecified N-soliton behaviour question; a two-soliton phase shift is a narrower question.'
 },
 'coverage':[
   {'pages':'P000685-P000689','allocation':'411','content':'General-boundary Morse index, Maslov crossings, symmetric spaces, spherical trace and spectrum.'},
   {'pages':'P000690-P000693','allocation':'412','content':'Filtered bimodules, compatibility equations, nodal interpolation, connection matrices and rank-one soliton identification; final vague behaviour question kept separate.'},
   {'pages':'P000694-P000696','allocation':'413','content':'Gelfand characteristic-class programme and Gabrielov degeneracy cycles, section-change chains, hypersimplices.'},
   {'pages':'P000697-P000698','allocation':'414','content':'Graev line transform, range/inversion forms, admissible complexes and Klein quadric.'},
   {'pages':'P000699 upper','allocation':'416','content':'Gelfand on Poncelet/Abel, elliptic translation, Figiel short Dvoretzky proof.'},
   {'pages':'P000699 lower-P000701','allocation':'415','content':'Vershik symmetric groups and probability, Young branching, Plancherel shape, Ulam and fluctuation discussion.'},
   {'pages':'P000702-P000704','allocation':'417','content':'Tyurin representation packets, logarithmic differentials, Torelli, Schwarzian derivative and projective monodromy.'},
   {'pages':'P000705 planning lines','allocation':'418 boundary only','content':'New academic year, thirty-fourth seminar year; proposed noncommutative algebraic geometry, Bernstein and the two Gelfands.'},
   {'pages':'P000705 Drinfeld heading-P000706','allocation':'adjacent 1977--78 context; not indexed as 1976 occurrences','content':'Self-duality on S4; conformal star on 2-forms; Hermitian connection; quantization and regularized-determinant heuristic; twistor CP3 to HP1=S4 with CP1 fibers; correspondence with holomorphic bundles trivial on twistor lines (notebook omits full reality/metric conditions); Grassmannian/Klein quadric; quaternionic antiholomorphic involution.'}
 ],
 'provenance_anomalies':[
  {'record':415,'catalogue_date':'1977-04-04','structured_date':'1977-03-28','evidence':'One clear 28/III-77 heading on P699 governs Gelfand then Vershik; no new date intervenes.'},
  {'record':417,'catalogue_speaker':'A. S. Tyurin','scan_speaker':'A. Tyurin','publication_identification':'A. N. Tyurin','evidence':'Both exactly matching primary papers signed A. N. Tyurin; scan does not itself spell the patronymic.'},
  {'record':418,'catalogue_scope':'1977--78 heading','visible_date':'5/IV-77','decision':'Month unresolved; retain transcription with anomaly, do not silently normalize to IX.'}
 ],
 'chronology_notes':[
  'Duistermaat Morse exposition publicly dated 29 May 1974; joint spectral paper received 11 July 1978 and published 1979.',
  'Manin Russian exposition 1978, English 1979; printed sign error in III Theorem 2.6 verified visually by middle agent.',
  'GGL papers 1975 precede Gabrielov talk; MacPherson Bourbaki lecture February 1977, proceedings 1978.',
  'Gelfand--Graev algebraic line-complex classification 1968 is an exact older source.',
  'Griffiths Abel paper 1976 and Figiel Dvoretzky proof 1976 match Gelfand intervention.',
  'Vershik--Kerov announcement received 14 December 1976, presented 17 December 1976, published 1977; receipt is not proof of earlier public circulation.',
  'Kerov Gaussian-field CLT announced 1993; reconstruction from 1999 notes in Ivanov--Olshanski 2002 volume, arXiv 2003.',
  'Tyurin survey 1978 nominal volume, English translation 1979 in author bibliography; text based on 1973 lectures. Exact 1977 paper received 11 April 1977.'
 ],
 'decision_on_development':'No C or D item. Elementary sign/index/dimension checks and the full rank-one packet counterexample are critical annotations, not invented open-problem developments.',
 'audit_proof':'work/late_checks.tex: full Tyurin rank-one counterexample, all hypotheses checked; independently rederived by universal-cover harmonic argument and reviewed by root and middle agent.',
 'verification_limits':[
  'Hook-graphs original full text unavailable; publisher date checked, formula read in other opened primary texts.',
  'Exact wording of P701 stationarity sentence and P702 related-bundles question not identifiable.',
  'P689 final remainder exponent not silently replaced by the weaker published theorem.',
  'Tyurin 1977 property 5 has a stronger meromorphic Schwarzian integrability claim that is not used.',
  'No D classification from absence of search hits.'
 ]
}
(w/'late_meta.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'items':len(items),'areas':dict(Counter(areas.values())),'covered_pages':len(meta['inspected_scan_pages'])},indent=2))
