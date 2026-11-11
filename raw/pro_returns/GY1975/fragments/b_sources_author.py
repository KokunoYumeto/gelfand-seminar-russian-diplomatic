"""Construct the auditable source ledger for the assigned block only."""
from pathlib import Path
import json
P=Path(__file__).parent
items=json.loads((P/'b_items.json').read_text())
S=[]
def source(key,verification,locators,urls,refs,scope,chronology='',limits=''):
 S.append(dict(key=key,verification=verification,read_locators=locators,
   opened_urls=urls,source_result_refs=refs,scope=scope,chronology=chronology,
   limitations=limits,checked_on='2026-11-10',
   occurrences=[i['id'] for i in items if key in i['refs']]))

source('dubrovinmatveevnovikov1976nonlinear','read the result',
 ['Chapter III, Section 2, pp.114--125; theorem on p.117'],
 ['https://people.sissa.it/~dubrovin/Papers/1976/dubrovin_matveev_novikov_1976.pdf','https://www.mathnet.ru/eng/rm3642'],
 ['turn3view4','turn5view4','turn5view5'],
 'Matrix hierarchy, stationary spectral curve and integrability announcement.',
 'Received 1975-06-02; journal publication1976. Submission does not establish public circulation before1975-10-27.',
 'The full phase space/Poisson theorem is not reproduced; 375.7 is explicitly a partial identification. Regular reconstruction chart is distinguished from the source quotient notation.')
source('dubrovin1977matrix','read the result',
 ['Section1, Lemmas1--4; theorem on p.269; article heading and receipt line'],
 ['https://people.sissa.it/~dubrovin/Papers/1977/dubrovin_1977_fan.pdf','https://people.sissa.it/~dubrovin/bd_papers.html'],
 ['turn6view2','turn8view1','turn23view5','turn58view2','turn59view1','turn122view2'],
 'Normalized formal resolvents, commuting flows and matrix/Jacobian construction.',
 'Received1976-12-07; volume11(4),1977; translation copyright1978 is separately labelled.',
 'The source states M_Gamma/pi=J(Gamma); the open regular-potential locus in the item is editorial reconstruction, not verbatim theorem wording.')
source('drinfeld1977commutative','read the result',
 ['Entire four-page Russian original, pp.11--14; Propositions1--2, Corollaries1--2, proof of Corollary2'],
 ['https://www.mathnet.ru/eng/faa2040','https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2040&what=fullt'],
 ['turn3view1','turn5view0','turn6view0','turn8view0','turn113view2','turn114view1'],
 'Filtered modules/sheaves and rank-one smooth-germ correspondence; publication explicitly credits Krichever and the seminar.',
 'Received1976-04-14; published1977.',
 'The fixed smooth-curve theorem does not justify the notebook claim that all subrings have smooth spectral curves. Germ hypotheses and the additional principal-part generator are retained.')
source('krichever1976zakharov','read the result',
 ['Conditions1--2 before Theorem1; Theorem1; Corollary1; stationary discussion, pp.291--294'],
 ['https://www.mathnet.ru/eng/dan40219','https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=40219&what=fullt'],
 ['turn3view2','turn5view1','turn6view1','turn58view1'],
 'Baker--Akhiezer conditions, nonspecial divisor, normalized wave and Zakharov--Shabat construction.',
 'Received1975-10-08; presented to the Academy1975-10-24; journal1976. These dates alone do not prove public circulation before the recorded talks.',
 'The notebook Akhiezer attribution is preserved; the exact multiparameter modern construction is matched to this publication.')
source('bernstein1972continuation','read the result',
 ['Theorem1-prime, p.26 of Russian original; publisher bibliographic record'],
 ['https://www.mathnet.ru/eng/faa2532','https://www.mathnet.ru/php/getFT.phtml?jrnid=faa&option_lang=eng&paperid=2532&what=fullt'],
 ['turn34view0','turn53view0'],
 'Polynomial-parameter differential functional equation.',
 'Received1972-06-21; published1972, before the1975 talk.',
 'The operator may depend polynomially on the exponent; the supplied formula uses a shifted exponent convention.')
source('regge1961relativity','publisher metadata checked',
 ['Publisher abstract and bibliographic/receipt metadata'],
 ['https://link.springer.com/article/10.1007/BF02733251'],['turn19view0'],
 'Prior polyhedral formulation of general relativity and curvature concentration.',
 'Received1960-10-17; printed1961; later online date is not original publication.',
 'Full proof was not read. Does not verify every part of the notebook ant/torsion analogy or settle an unspecified convergence problem.')
source('halperintoledo1972stiefel','read the result',
 ['Theorem1 and mod-two corollary pp.511--512; C_0/Euler-characteristic discussion p.512; PL remark'],
 ['https://annals.math.princeton.edu/1972/96-3/p05','https://webhomes.maths.ed.ac.uk/~v1ranick/papers/halperin.pdf'],
 ['turn23view2','turn23view3','turn29view2','turn79view1'],
 'All-simplex cycles of first barycentric subdivision and their Stiefel--Whitney dual classes.',
 'Annals96(3),November1972, before both relevant seminars.',
 'Closed smooth manifold hypotheses and class index w_(n-p) are required. Arbitrary singular polyhedra and boundary versions are not silently included.')
source('garcia1972connections','read the result',
 ['Section2 Theorems1--2 pp.234--236; Section3 Theorem3 pp.238--240'],
 ['https://www.numdam.org/item/RSMUP_1972__47__227_0.pdf'],
 ['turn23view1','turn29view1','turn78view2'],
 'Affine bundle of connections and the canonical connection on the pullback principal bundle.',
 'Received1972-01-11; published1972, before Losik1976.',
 'Jet-language theorem is translated into the notebook pointwise connection-form language; the principal base is the quotient C(P)/G.')
source('gelfandkirillov1966corps','read the result',
 ['Introduction and Section1'],
 ['https://www.numdam.org/item/PMIHES_1966__31__5_0.pdf'],['turn78view0'],
 'Historical noncommutative division-ring framework.',
 'Published1966.',
 'Does not identify the unspecified extension problem; no later conjecture is substituted for missing quantifiers.')
source('gellmann1964schematic','publisher metadata checked',
 ['Caltech author-repository bibliographic record'],
 ['https://authors.library.caltech.edu/records/d4jws-7eh11'],['turn19view1'],
 'Pre-talk quark-model publication.',
 'Received1964-01-04; published1964-02-01.',
 'Full paper not read. Representation identities are already explicit in the supplied notebook and reconstructed by elementary tensor symmetry.')
source('hannambu1965triplet','publisher metadata checked',
 ['Publisher abstract and metadata'],
 ['https://journals.aps.org/pr/abstract/10.1103/PhysRev.139.B1006'],['turn37view1'],
 'Prior three-triplet/double-SU(3) model.',
 'Received1965-04-12; published1965-08-23.',
 'Historical model is not asserted to be literally modern QCD; no full-paper reading claimed.')
source('greenberg1964paraquark','publisher metadata checked',
 ['Publisher bibliographic and publication-date fields'],
 ['https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.13.598'],['turn53view2'],
 'Prior paraquark response to the spin/statistics issue.',
 'Received1964-10-27; published1964-11-16.',
 'Full text not read; used as a documented historical precursor, not an exact equivalence claim.')
source('glashowiliopoulosmaiani1970weak','publisher metadata checked',
 ['Publisher abstract and metadata'],
 ['https://journals.aps.org/prd/abstract/10.1103/PhysRevD.2.1285'],['turn53view3'],
 'Pre-talk four-quark weak-current model.',
 'Received1970-03-05; published1970-10-01.',
 'Does not establish the notebook percentages or precise informal chronology; no full-paper reading claimed.')
source('levinfrankfurt1968quark','read the result',
 ['Introduction pp.107--108: spin multiplets and sigma_pp/sigma_pi-p ratio; SectionVII located by contents'],
 ['https://ufn.ru/en/articles/1968/1/h/','https://ufn.ru/ufn68/ufn68_1/ufn681h.pdf'],
 ['turn53view1','turn54view0','turn55view4'],
 'Spin-3/2 baryons, spin-one mesons and additive-quark cross-section ratio with its asymptotic assumption.',
 'Published1968, before the1975 talk.',
 'The notebook ten-percent estimate has no identified dataset. The full SectionVII was not read; the exact supporting ratio is in the read introduction.')
source('lhcb2015pentaquark','read the result',
 ['Primary abstract and arXiv submission history'],
 ['https://arxiv.org/abs/1507.03414'],['turn37view0','turn54view2'],
 'Observation of resonances consistent with pentaquark minimal valence content.',
 'First arXiv submission2015-07-13; revised2015-07-25; PRL115,072001(2015).',
 'Read abstract-level result only. This is not evidence for a unique compact rather than molecular microscopic structure.')
source('wilson1974confinement','read the result',
 ['SectionII Wilson loops, static sources and nearby vacuum-loop screening; SectionIII lattice action; SectionIV strong-coupling expansion pp.2454--2455'],
 ['https://journals.aps.org/prd/abstract/10.1103/PhysRevD.10.2445','https://hep.physics.uoc.gr/Erasmus-IP-2013/files/lectures/Rabinovici/Wilson.pdf'],
 ['turn19view2','turn34view1','turn54view1'],
 'Pre-talk loop criterion, static-energy interpretation, compact lattice gauge theory and strong-coupling mechanism.',
 'Received1974-06-12; printed1974-10-15. The cumulative bibliography additionally notes an INSPIRE preprint; that earlier preprint was not independently reopened in this block.',
 'Leading strong-coupling mechanism is distinguished from a rigorous four-dimensional continuum area law. The notebook itself explicitly contains d^4x.')
source('jaffewitten2000yangmills','read the result',
 ['Sections1 and5 of the official standalone problem description; book contents pp.129--152'],
 ['https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf','https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf'],
 ['turn19view3','turn23view4','turn122view0','turn124view0'],
 'Distinction between classical masslessness, the quantum mass-gap problem and additional confinement properties.',
 'The opened standalone PDF is undated. The key uses the Millennium announcement year, not a verified publication date of this file. BibTeX year is n.d.',
 'The current mass-gap status is independently checked on the Clay live page; it is not equated with confinement.')
source('clay2026yangmills','read the result',
 ['Official current problem overview'],
 ['https://www.claymath.org/millennium/yang-mills-the-maths-gap/'],
 ['turn55view0','turn123search2'],
 'Current official unsolved status of Yang--Mills existence and mass gap.',
 'Checked2026-11-10 with a fresh official-site search and opened page.',
 'This does not by itself establish a logical equivalence with the Wilson-loop area-law question.')
source('mulase1990geometric','read the result',
 ['Section2 Main Theorem; Section3 equations(2)--(3), pp.5--6 of author PDF; Section4 formal roots'],
 ['https://www.math.ucdavis.edu/~mulase/texfiles/nato.pdf'],
 ['turn55view1','turn58view3','turn59view2','turn59view3','turn112view1','turn113view3'],
 'Modern primary construction, allowance for singular spectral curves, classical commuting order-two/three example and formal pseudodifferential roots.',
 'Published1990; its historical attribution reaches Wallenberg1903 and Schur1905.',
 'Historical originals were not opened; that chronology is indirect. The displayed modern formulas were read and independently checked. No theorem for arbitrary unspecified Shabat subrings is identified.')
source('brodskii1976spectral','read the result',
 ['Entire pp.253--254; equations(1)--(6), Theorems1--2 and necessary-condition corollary'],
 ['https://www.mathnet.ru/eng/rm3810','https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=3810&what=fullt'],
 ['turn16view0','turn19view4','turn23view0','turn29view0','turn78view1','turn122view1'],
 'Exact scalar radial equation, fixed endpoint condition, high-frequency sampling and monotone-profile inversion.',
 'Received1975-06-18; published1976. A related1975 Computational Seismology8 article is attested by Levshin2004 ref91; its exact overlap is unverified.',
 'B records different named author from seminar reporter Novikov, not a claim that the work arose after the talk. Earliest-publication chronology remains provisional. A necessary range condition is not a full exact spectral-array range theorem.')
source('paternainsalouhlmann2022geometric','read the result',
 ['Theorems2.2.1 and2.2.3; Remark2.2.2; pp.32--35, including Abel composition proof'],
 ['https://users.jyu.fi/~salomi/lecturenotes/GIP2D_driver.pdf'],
 ['turn80view0','turn81view0','turn81view1','turn122view3'],
 'Classical radial travel-time inversion and Abel integral inversion, used to delimit the novelty of Brodskii spectral sampling.',
 'Book2022; historical remark identifies Herglotz1907 and Bateman1910.',
 'Original1907/1910 papers were not opened. Their history is indirect; the modern theorem and Abel proof were read. This book is not an exact match for indexed spectral data.')
source('forster1981riemann','publisher metadata checked',
 ['Publisher description and metadata; author table of contents, ChapterII Sections16--21 and ChapterIII Section29'],
 ['https://link.springer.com/book/10.1007/978-1-4612-5961-9','https://www.math.lmu.de/~forster/books/riem/riemsurf.html'],
 ['turn111view1','turn113view1'],
 'Later reference for classical Riemann--Roch, divisors, periods, Abel--Jacobi and inversion background.',
 'English edition1981; author site identifies fourth corrected printing1999. These are exposition dates, not dates of the classical results.',
 'Full-text attempts at the CNRS-hosted PDF returned502. No full theorem-level reading is claimed; elementary reconstructions derive from notebook formulas and standard mathematics.')

source('noether1918invariant','read the result',
 ['Section 1, Theorems I--II, p. 3 of the English arXiv reproduction; opening publication note'],
 ['https://arxiv.org/abs/physics/0503066','https://arxiv.org/pdf/physics/0503066'],
 ['turn153view0','turn153view1'],
 'Finite-parameter variational symmetries yield divergence relations; arbitrary-function symmetries yield Euler--Lagrange identities.',
 'Original 1918; Tavel English translation 1971; repository first upload 2005 and version 3 in 2018 are later access events.',
 'The English primary translation was read, not the German original. Global charges and converse classifications require additional boundary/equivalence conditions.')

leads=[
 {'key':'krichever1977methods','status':'read contextual source; not cited in this block',
  'opened_urls':['https://www.math.columbia.edu/department/krichever/pdfs/1975-1979/1977-MOAGITTONE0.pdf'],
  'source_result_refs':['turn96view0'],'locators':['Introduction; Section1 Lemma1.1 and Theorem1.1'],
  'finding':'Introduction recalls November--December1975 seminar reports, whereas notebook predecessor dates20October1975. Retain notebook date and flag provenance difference; sibling block handles citation.'},
 {'key':'brodskiilevshin1979inversion','status':'publisher abstract/metadata checked; not cited in final block',
  'opened_urls':['https://academic.oup.com/gji/article/58/3/631/676060'],
  'source_result_refs':['turn3view3'],'locators':['Abstract; publication record'],
  'finding':'Geophysical Journal RAS58(3),631--654,1979; DOI10.1111/j.1365-246X.1979.tb04799.x. Supports broader later programme, not used to claim exact scalar range theorem. A later repeat-open failed.'},
 {'key':'levshin2004retrospective','status':'opened; historical reference lead',
  'opened_urls':['https://www.itpz-ran.ru/wp-content/vs-open/35/v35_007_Levshin.pdf'],
  'source_result_refs':['turn136search1','turn137view0'],'locators':['Reference91, printedp20'],
  'finding':'Lists M.A.Brodskii, On the application of asymptotic methods to the inverse problem of torsional oscillations, Computational Seismology8(1975),162--168. Full1975 article not obtained; do not infer exact theorem equality from its title.'},
 {'key':'mironov2021commuting','status':'opened supplementary lead; not cited',
  'opened_urls':['https://www.mathnet.ru/PresentFiles/30912/Mironov%209.06.2021.pdf'],
  'source_result_refs':['turn55view3'],'locators':['Opening examples'],
  'finding':'Rational commuting pair also appears in this lecture. Final citation uses the read Mulase primary paper and independent check.'}
]
queries=[
 {'items':['1975-377.8'],'queries':['"Гельфанд" "некоммутативная электротехника"','Gelfand Polyakov noncommutative electrical engineering'],
  'engines':['system2','system1'],'result_refs':['turn60search','turn67search'],
  'finding':'No precise circuit assertion or exact later theorem recovered. The missing network/equation specification prevents a D or C claim.'},
 {'items':['1975-379.6'],'queries':['Krichever Gelfand quasianalyticity algebraic operator 1976','"Krichever" "quasianalyticity"'],
  'engines':['system2','system1'],'result_refs':['turn60search','turn67search'],
  'finding':'No exact statement recovered; function class and asymptotic growth/sector assumptions are missing.'},
 {'items':['1975-380.2'],'queries':['"Шабат" "коммутативных подколец" дифференциальных операторов','"Шабат" "коммутативные подкольца" операторы'],
  'engines':['system2','system1'],'result_refs':['turn60search','turn67search'],
  'finding':'Later Krichever literature surfaced, but no exact Shabat theorem with the notebook smooth-curve quantifiers. Literal universal formulation fails by the supplied cusp example.'},
 {'items':['1975-380.3','1975-380.4'],'queries':['"Гельфанд" "расширения" "тел" "Кириллова" Дринфельд','Drinfeld extensions Gelfand Kirillov division rings'],
  'engines':['system2'],'result_refs':['turn60search'],
  'finding':'Framework located; no precise extension category, arithmetic reciprocity map or quantified theorem recovered.'},
 {'items':['1975-381.1','1975-381.2'],'queries':['"Бродский" "1975" "Вычислительная сейсмология" "162"','"Brodskii" "1975" "162" "168"','Бродский О применении асимптотических методов обратной задаче крутильных колебаний 1975 pdf','site:itpz-ran.ru "Выпуск 8" "1975"','site:itpz-ran.ru "vs-open/8/"'],
  'engines':['system1','system2'],'result_refs':['turn136search1','turn136search2','turn136search3','turn137search12','turn137search0'],
  'finding':'1975 precursor is bibliographically attested; primary text not recovered. Some secondary English page ranges conflict (162--174); the Russian institutional retrospective gives162--168. Exact content/chronology remains unresolved.'}
]
attempts=[
 {'url':'https://ronan.terpereau.perso.math.cnrs.fr/Master_Class_2023_Dijon/FORSTER_Lectures%20on%20Riemann%20Surfaces.pdf',
  'result_refs':['turn111view0','turn113view0'],'result':'502; not read'},
 {'url':'https://ronan.terpereau.perso.math.cnrs.fr/Master_Class_2023_Dijon/GUNNING_Lectures%20on%20Riemann%20Surfaces.pdf',
  'result_refs':['turn114view0'],'result':'502; not read or cited'},
 {'url':'https://academic.oup.com/gji/article/58/3/631/676060',
  'result_refs':['turn136view0'],'result':'Later find/reopen failed via publisher CDN; original abstract-level opening remains recorded above.'}
]
# Earlier searches are identified by call family when exact per-hit identifiers
# were not retained. These are log labels, never offered as web citations.
for q in queries:
 q['query_call_labels']=[v for v in q['result_refs'] if v in ['turn60search','turn67search']]
 q['result_refs']=[v for v in q['result_refs'] if v not in ['turn60search','turn67search']]
 q['query_result_ref_note']='Call-family labels are audit labels only; exact result references appear separately when retained.'

out=dict(block='records375--385',academic_year=1975,status_date='2026-11-10',
 method='Primary sources preferred. Opened metadata, read theorem text and unresolved leads are distinguished. Receipt dates are not treated as public circulation.',
 sources=S,additional_opened_leads=leads,unresolved_queries=queries,failed_access_attempts=attempts)
(P/'b_sources.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f'{len(S)} cited sources; {len(leads)} additional opened leads; {len(queries)} unresolved-query groups')
