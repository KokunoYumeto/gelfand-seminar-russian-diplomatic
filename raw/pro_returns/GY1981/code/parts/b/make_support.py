from pathlib import Path
import re,json,csv
p=Path(__file__).resolve().parent
items=json.loads((p/'items.json').read_text())
keys=sorted({k for i in items for k in i['refs']})
s=(p.parents[1]/'references_cumulative.bib').read_text()
chunks=re.split(r'(?m)(?=^@\w+\{)',s)
entries={}
for k in keys:
    found=[c.strip() for c in chunks if re.match(r'@\w+\{'+re.escape(k)+r'\s*,',c)]
    if found: entries[k]=found[0]
entries['gonshor1986surreal']=r'''@book{gonshor1986surreal,
 author={Gonshor, Harry}, title={An Introduction to the Theory of Surreal Numbers},
 publisher={Cambridge University Press}, series={London Mathematical Society Lecture Note Series}, volume={110}, year={1986},
 doi={10.1017/CBO9780511629143},
 url={https://www.cambridge.org/core/books/an-introduction-to-the-theory-of-surreal-numbers/312AE504A3E88E804054BFB390446374},
 note={verified},
 annote={Publisher metadata and contents opened on 11 November 2026. Chapters 2--5 cover definition, operations, reals/ordinals and normal forms. Full book not read in this run; mathematical checking uses the readable Mantova--Matusinski preprint and explicit canonical-cut reasoning.}
}'''
entries['gabberjoseph1981towards']=r'''@article{gabberjoseph1981towards,
 author={Gabber, Ofer and Joseph, Anthony}, title={Towards the {Kazhdan--Lusztig} conjecture},
 journal={Annales Scientifiques de l'\'Ecole Normale Sup\'erieure}, series={4}, year={1981}, volume={14}, number={3}, pages={261--302},
 doi={10.24033/asens.1406}, url={https://www.numdam.org/item/10.24033/asens.1406.pdf}, note={verified},
 annote={Primary full text opened; introduction and section 1 read for finite length, the Jantzen deformation and the relation between the then conjectural filtration refinement and KL. The prior cumulative key is retained.}
}'''
entries.update({
'beilinsonbernstein1993jantzen':r'''@incollection{beilinsonbernstein1993jantzen,
 author={Beilinson, Alexander A. and Bernstein, Joseph}, title={A proof of {Jantzen} conjectures},
 booktitle={I. M. Gel'fand Seminar}, series={Advances in Soviet Mathematics}, volume={16, Part 1}, pages={1--50},
 publisher={American Mathematical Society}, year={1993},
 url={https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/Ber-Beil_ProofJatzenConj.pdf}, note={verified},
 annote={Author-hosted full scanned PDF opened. Introduction and main-result setup visually inspected; not all proofs read. Exact dominant-direction consequences also checked in Williamson section 1.4. Author bibliography confirms 1993 publication; no earlier circulation date verified.}
}''',
'bernsteingelfandgelfand1976category':r'''@article{bernsteingelfandgelfand1976category,
 author={Bernstein, Joseph N. and Gel'fand, Israel M. and Gel'fand, Sergei I.},
 title={Category of {\(\mathfrak g\)}-modules}, journal={Functional Analysis and Its Applications},
 volume={10}, number={2}, pages={87--92}, year={1976}, doi={10.1007/BF01077933},
 url={https://www.mathnet.ru/eng/faa2144}, note={verified},
 annote={Math-Net metadata and full Russian text opened; section 1 inspected for category O, finite generation, weight decomposition and duality. Russian original 10(2), 1--8; received 22 December 1975.}
}''',
'shapovalov1972bilinear':r'''@article{shapovalov1972bilinear,
 author={Shapovalov, Nikolai N.}, title={On a bilinear form on the universal enveloping algebra of a complex semisimple {Lie} algebra},
 journal={Functional Analysis and Its Applications}, volume={6}, number={4}, pages={307--312}, year={1972},
 doi={10.1007/BF01077650}, url={https://www.mathnet.ru/eng/faa2537}, note={verified},
 annote={Publisher metadata opened: Russian original 6(4), 65--70; received 15 March 1972. Full-text link redirected to metadata, so the original proof was not read. The form and deformation are checked in Gabber--Joseph and Williamson.}
}''',
'jantzen1979moduln':r'''@book{jantzen1979moduln,
 author={Jantzen, Jens Carsten}, title={Moduln mit einem h\"ochsten Gewicht},
 publisher={Springer}, series={Lecture Notes in Mathematics}, volume={750}, year={1979},
 doi={10.1007/BFb0069521}, url={https://link.springer.com/book/10.1007/BFb0069521}, note={verified},
 annote={Publisher record and chapter ranges opened. Translation principle pp.42--77; modules over parameter algebras pp.112--143; filtrations pp.144--181. Full book not read.}
}''',
'williamson2016local':r'''@article{williamson2016local,
 author={Williamson, Geordie}, title={Local {Hodge} theory of {Soergel} bimodules},
 journal={Acta Mathematica}, volume={217}, number={2}, pages={341--404}, year={2016},
 doi={10.1007/s11511-017-0146-8}, url={https://arxiv.org/abs/1410.2028}, note={verified},
 annote={Full arXiv v3 and publisher metadata opened. Sections 1.4--1.6 and 8.4 read, including the explicit A3 counterexample. First preprint 8 October 2014; v3 14 September 2016. Journal volume dated 2016; Springer online publication date 7 July 2017.}
}''',
'lusztig1983singularities':r'''@incollection{lusztig1983singularities,
 author={Lusztig, George}, title={Singularities, character formulas, and a {\(q\)}-analog of weight multiplicities},
 booktitle={Analyse et topologie sur les espaces singuliers (II--III)}, series={Ast\'erisque}, volume={101--102},
 pages={208--229}, publisher={Soci\'et\'e Math\'ematique de France}, year={1983},
 url={https://www.numdam.org/item/AST_1983__101-102__208_0.pdf}, note={verified},
 annote={Full primary text read at section 2 (extended affine group and maximal double-coset elements), Theorems 3.1, 4.1 and 6.1. Proceedings concern the meeting of 6--10 July 1981; this is not assumed to establish the exact first-circulation date of every theorem.}
}''',
'krattenthaler1999determinant':r'''@article{krattenthaler1999determinant,
 author={Krattenthaler, Christian}, title={Advanced determinant calculus},
 journal={S\'eminaire Lotharingien de Combinatoire}, volume={42}, pages={B42q}, year={1999},
 url={https://arxiv.org/abs/math/9902004}, note={verified},
 annote={Full paper opened; section 2.1 and equation (2.7) read for Cauchy's double alternant and the sign convention. Preprint 1 February 1999, final version 31 May 1999. Used as a checked modern exposition of a classical identity, not as its origin.}
}''',
'elashvili1982frobenius':r'''@article{elashvili1982frobenius,
 author={\'Elashvili, Alexander G.}, title={Frobenius {Lie} algebras},
 journal={Functional Analysis and Its Applications}, volume={16}, number={4}, pages={326--328}, year={1982},
 doi={10.1007/BF01077870}, url={https://www.mathnet.ru/eng/faa1687}, note={verified},
 annote={Complete two-page Russian original inspected, including the table and receipt date 30 November 1981: Funktsional. Anal. i Prilozhen. 16(4), 94--95. Section 0 quotes the Ooms 1976 theorem; section 1 gives the abelian-radical stabilizer criterion; section 2 gives castling and ten reduced families.}
}''',
'cartier1982perturbations':r'''@incollection{cartier1982perturbations,
 author={Cartier, Pierre}, title={Perturbations singuli\`eres des \'equations diff\'erentielles ordinaires et analyse non-standard},
 booktitle={S\'eminaire Bourbaki, 1981--1982}, series={Ast\'erisque}, volume={92--93}, pages={21--44},
 publisher={Soci\'et\'e Math\'ematique de France}, year={1982},
 url={https://www.numdam.org/item/SB_1981-1982__24__21_0.pdf}, note={verified},
 annote={Expos\'e 580 delivered November 1981. Full text opened; introduction, section 2 assumptions (a)--(c), and section 5 nos.21--23 and figures inspected, several formula pages visually. Confirms Cartier as speaker, Reeb-school provenance, zero-one finitely additive measure, and van der Pol/Rayleigh relaxation analysis.}
}''',
'krichever1983elliptic':r'''@article{krichever1983elliptic,
 author={Krichever, Igor M.}, title={Nonlinear equations and elliptic curves},
 journal={Itogi Nauki i Tekhniki. Seriya Sovremennye Problemy Matematiki}, volume={23}, pages={79--136}, year={1983},
 url={https://www.math.columbia.edu/department/krichever/pdfs/1980-1984/1983-NEAEC0.pdf}, note={verified},
 annote={The author-hosted full English translation was inspected: Journal of Soviet Mathematics 28(1), 51--90 (1985). Section 1.3, equations (1.91)--(1.94), defines the elliptic matrix-function algebra and sigma kernels. Author/institutional bibliographies verify the Russian 1983 original. This is a partial mathematical match to the short seminar fragment.}
}''',
'brazovskiidzyaloshinskiikrichever1982peierls':r'''@article{brazovskiidzyaloshinskiikrichever1982peierls,
 author={Brazovskii, Sergei A. and Dzyaloshinskii, Igor E. and Krichever, Igor M.},
 title={Discrete {Peierls} models with exact solutions}, journal={Soviet Physics JETP},
 volume={56}, number={1}, pages={212--225}, year={1982},
 url={https://www.math.columbia.edu/department/krichever/pdfs/1980-1984/1982-DPMWES.pdf}, note={verified},
 annote={Full author-hosted English PDF opened; submitted 9 February 1982. Used only to verify collaboration and thematic context. The translated title page prints N. E. Dzyaloshinskii, while the Russian original and Landau Institute bibliography identify I. E.; the bibliographic identity is normalized accordingly. Russian original ZhETF 83(1), 389--415 (1982).}
}'''
})
missing=set(keys)-set(entries)
assert not missing,missing
(p/'references.bib').write_text('\n\n'.join(entries[k] for k in keys)+'\n')
problems=[
 dict(id='GP-1979-41',title='Kazhdan--Lusztig multiplicity and cohomological conjectures',
 statement=r'For ordinary Verma modules of a finite-dimensional complex semisimple Lie algebra, identify Jordan--Hölder multiplicities with Kazhdan--Lusztig values, and determine the coefficient refinements from local intersection cohomology and the Jantzen filtration with its correct grading.',
 occurrences=['1979-483.6','1979-484.4','1981-538.5','1981-538.8','1981-538.9','1981-540.6','1981-540.7'],
 status=r'As of November 2026, the ungraded theorem and geometric interpretation were already established before the November 1981 talk; the dominant-direction filtration refinement was proved in the 1993 Beilinson--Bernstein publication. Arbitrary-direction invariance is separately indexed as GP-1981-10, because it is false and has different quantifiers.',status_date='2026-11',refs=['beilinsonbernstein1981localisation','brylinskikashiwara1981holonomic','kazhdanlusztig1980schubert','beilinsonbernstein1993jantzen']),
 dict(id='GP-1981-10',title='Dependence of Jantzen-layer multiplicities on deformation direction',
 statement=r'For a fixed regular-integral Verma module, are the multiplicities in each layer of the Jantzen filtration independent of the regular direction used to deform its highest weight?',
 occurrences=['1981-540.5'],status=r'As of November 2026: false without a dominant-cone restriction. Williamson, \S8.4, gives an explicit type-A3 example with a 13-dimensional weight space whose layer dimensions change from \((7,3,2,1)\) to \((7,2,4,0)\). First arXiv circulation was 8 October 2014; the journal volume is dated 2016 and its online release 7 July 2017. Dominant deformations satisfy the established Jantzen theorem. No unresolved residue is asserted for the literal seminar question.',status_date='2026-11',refs=['williamson2016local','beilinsonbernstein1993jantzen']),
 dict(id='GP-1981-12',title='Primitivity of enveloping algebras of algebraic Lie algebras',
 statement=r'Characterize finite-dimensional algebraic Lie algebras over an algebraically closed field of characteristic zero whose universal enveloping algebra has a faithful simple module.',
 occurrences=['1964-37.1','1964-37.2','1981-542.2'],status=r'As of November 2026: already settled by the 1976 Ooms criterion, quoted exactly in Elashvili, \S0. Primitivity is equivalent to an open coadjoint orbit, equivalently a nondegenerate Kirillov form. Elashvili\textquotesingle s 1982 paper further classifies specified reduced semidirect-product families. The earlier supplied index gives no existing GP identifier for 1964-37.1, so a new problem ID is assigned while retaining its earlier occurrence.',status_date='2026-11',refs=['elashvili1982frobenius']),
 dict(id='GP-1981-13',title='Van der Pol relaxation limit and matching of slow branches',
 statement=r'Describe the limit as \(\varepsilon\downarrow0\) of the attracting periodic orbit of \(\varepsilon\ddot x+(x^2-1)\dot x+x=0\), including the connection of its slow branches by rapid transitions.',
 occurrences=['1981-543.1','1981-543.3'],status=r'As of November 2026: established in the classical relaxation setting. Cartier\textquotesingle s November 1981 Bourbaki exposition, printed in 1982, gives a nonstandard-analysis treatment and the matched cycle. The notebook does not specify an additional unresolved initial-value, rate, or canard problem; those are not silently added.',status_date='2026-11',refs=['cartier1982perturbations'])
]
(p/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')
rows=[]
def corr(page,place,reads,should,evidence,typ='faithful_error',applies='both'):
 rows.append(dict(page=page,place=place,transcription_reads=reads,should_read=should,evidence=evidence,applies_to=applies,type=typ))
corr('P000995','simple-generator diagram','e_1,...,e_n bracketed as n_+','Read as Lie generators of n_+, not a vector-space basis.','Russian and scan show only the n simple generators; n is the rank. Root spaces for nonsimple positive roots are additionally needed.','ambiguity')
corr('P000995','first highest-vector definition','E_j x=0 defines highest-weight vector','Also require a common Cartan eigenvector; or call the kernel a space of singular vectors.','Scan first gives only annihilation, then later explicitly writes h v=chi(h)v.','ambiguity')
corr('P000995','after finite composition series','Any subquotient has this form','Every simple subquotient / composition factor has the form L(psi).','Russian wording любой подфактор and scan agree; an arbitrary subquotient need not be simple.')
corr('P000995','multiplicity question','Multiplicity of M(psi) in a composition series','Multiplicity of L(psi).','Scan confirms M(psi); the very next multiplicity formula uses L(psi).')
corr('P000996','dominant integral condition','Condition on lambda after defining chi','Use the same weight variable chi, or explicitly rename it lambda.','Russian, English and scan contain the variable switch; this is a notational slip.')
corr('P000996','category O marginal correction','Here only n_+, and not n_-, but this makes no difference','Changing the Borel gives an equivalent convention; the two local-nilpotence conditions are not equivalent on a fixed module.','Scan confirms both signs and margin wording. Generic Verma modules distinguish the two conditions.','ambiguity')
corr('P000996','dual module construction','The dual representation / Cartan-finite functions','Use the restricted weight-space dual and a Chevalley anti-involution to preserve the chosen category O.','The manuscript singles out Cartan-finite functionals but does not state the action or twisting.','ambiguity')
corr('P000996-P000997','bilinear form orthogonality','Different unordered sets of generator indices give zero','Different total root weights; for simple-root words this means different multisets of indices.','Discarding repetitions loses weight data. The displayed shorthand is faithfully copied.')
corr('P000996','bilinear form numerator','e carrying the same index sequence as the lowering monomial','The anti-involution reverses product order: e_{i_k}...e_{i_1}.','Scan has compressed multiindices, not a clear ordered product; modern contravariance fixes the interpretation.','ambiguity')
corr('P000997','first line','Form invariant with respect to the Lie algebra','Contravariant under the Chevalley anti-involution.','Russian reads инвар. отн. алг. Ли; ordinary bilinear invariance is different.')
corr('P000997','PBW identification','Identify all M(chi)','Identify underlying PBW vector spaces, not g-module structures.','The monomial map in the scan fixes negative-root vectors and changes highest weight.','ambiguity')
corr('P000997','definition of M_i','Fixed x has pairing O(t^i) against every fixed y','There exists a parameter-dependent lift of x whose pairing with the deformed lattice is divisible by t^i.','Scan confirms fixed-vector shorthand. The standard Jantzen lattice definition requires moving lifts.')
corr('P000997','change rho question','Apparently layer multiplicities do not change','True under appropriate dominant deformation hypotheses; false for all regular directions.','Question is explicit in Russian and scan. Williamson section 8.4 supplies a type-A3 counterexample.')
corr('P000997','polynomial multiplicity bracket','[L_psi : M_i/M_{i+1}]','[M_i/M_{i+1} : L_psi] in standard composition-multiplicity notation.','Scan specifically confirms the reversed order.')
corr('P000997','polynomial grading','P(q)=sum q^i times multiplicity in layer i','Layer j corresponds to q^{(length(y)-length(x)-j)/2}.','Even sl2 has P_{e,s}=1 while the lower constituent lies in layer 1; this is a faithful normalization error.')
corr('P000997','Schubert-cell cohomology','H^i of one Schubert cell near another; cell contained in other cell','Even-degree stalk intersection cohomology of a Schubert closure at a smaller cell.','Russian and scan omit intersection and closure. Distinct cells are disjoint; Lusztig Theorem 4.1 fixes the interpretation.')
corr('P000997','weight-space annotation','L(chi)_lambda is a weight space of weight chi','Weight lambda.','The scan confirms chi in the annotation, while the subscript and next-page formula use lambda.')
corr('P000997-P000998','alternant character formula','chi=(a_1,...,a_n) with denominator powers 0,...,n-1','Use shifted exponents a_i=lambda_{n+1-i}+i-1 for descending dominant lambda.','The trivial representation already disproves unshifted repeated zero exponents. Source determinants and statement were visually inspected.')
corr('P000998','affine-polynomial formula','m(lambda,chi)=P_{n_lambda,n_chi}(1), after m(chi,lambda)=dim L(chi)_lambda','Keep highest weight and weight argument order consistent; dim L(lambda)_mu=P_{n_mu,n_lambda}(1).','The manuscript reverses m arguments. Lusztig 1983 Theorem 6.1 gives the exact intended formula.')
corr('P000998','Kac--Moody conjecture','The same for all Kac--Moody algebras; crossed-out character expression','Retain as an unidentified conjectural extension; do not restore the erased expression as an established theorem.','Russian and scan show the full formula crossed out and leave the indices undefined.','ambiguity')
corr('P000998','Jacobson attribution','Last year below Jacobson','Do not infer a first proposal in 1980.','The question occurs in supplied 1964-37.1; Elashvili 1982 cites Jacobson and explicitly dates Ooms answer 1976. The marginal phrase may refer to an unrecorded occasion.','provenance')
corr('P000998','excluded algebras','All semisimple and nilpotent algebras unsuitable','All nonzero such algebras; the zero algebra has enveloping algebra C.','Faithful wording needs this elementary edge case.')
corr('P000998','affine example','Last column zero','Retain: a valid row/column convention, isomorphic via minus transpose to the customary last-row-zero realization.','Scan confirms column. This is an ambiguity resolution, not a transcription correction.','ambiguity')
corr('P000998','four-dimensional irreducible representation','Unique four-dimensional irreducible gl(2) representation','Unique sl(2) type Sym^3(C^2), with a specified nonzero scalar-center action.','The center acts by a free scalar on irreducible gl2 modules. Zero scalar makes the semidirect product non-Frobenius.')
corr('P000998','classification theorem','R simple','The matching publication uses R reductive and/or [R,R] simple, plus reduction and specified radical conditions.','Scan has a cancelled word before simple. The paper received 30 November 1981 has a broader ten-family theorem; exact recovery of the erased word is impossible.','ambiguity')
corr('P000999','Bourbaki heading','Reeb talk, November 1981; Cartier survey','Cartier was the Bourbaki speaker reporting work of Reeb and his school.','Original exposé 580 title page reads par Pierre Cartier, Novembre 1981. Manuscript attribution is retained diplomatically.','provenance')
corr('P000999','separated reduced equation','Divide by x without exclusions','Work away from x=0 and x=+-1; restore the solution x=0.','Direct differentiation confirms the displayed integral but division loses the equilibrium.','ambiguity')
corr('P000999','probability codomain','p:2^Omega -> (0,1)','For the intended Cartier construction: p:2^Omega -> {0,1}, with p(Omega)=1.','The scan truly uses round brackets. Finite additivity forces p(empty)=0, equality requires 1, and Cartier section 2 assumptions (a)-(c) explicitly require zero-one values.')
corr('P000999','equivalence probability symbol','Capital P in P(x prime=x double-prime)=1 after lowercase p definition','Read P as the same finitely additive p, absent a newly defined probability.','Scan confirms capital P. This is a harmless notational switch.','ambiguity')
corr('P001000','Kruskal numbers heading','Kruskal numbers, simplest field extending R','Identify as surreal sign expansions; retain Kruskal as the notebook attribution and distinguish proper-class No from set-sized ultrapowers.','Visible arrows match surreal arithmetic; Conway 1976 predates the talk, and Gonshor gives the systematic sign-sequence treatment.','provenance')
corr('P001000','finite-arrow explanatory rule','Step halves when direction changes','After the first change, halve the step at every subsequent sign.','Scan confirms the conditional wording. The sequence +-- equals 1/4, not 0.')
corr('P001000','infinite-arrow notation','Infinity, double-hatted up, epsilon','Use omega for an omega-long positive block, omega^2 for an omega^2-long block, and omega^{-1} for + followed by omega minuses.','The hats do not themselves specify ordinal lengths. They must be fixed before the field identities have a precise meaning.','ambiguity')
corr('P001000','no predecessor parenthesis','There is no predecessor','Specify ordinal predecessor, or clarify that the ordered field has no immediate neighbors.','The same passage correctly writes omega-1; lack of an ordinal predecessor is distinct from lack of a predecessor in field arithmetic.','ambiguity')
corr('P001000','joint-work first surname','Brozovskii / Брозовского','Bibliographic identification: Brazovskii / Бразовского; preserve the written o in a diplomatic transcription.','The scan visibly has o. The exact collaborator list is confirmed by the 1982 joint paper and Krichever institutional bibliography.','provenance')
corr('P001000','ascending union G=union G_n','Editorial marker group-chain-tail may suggest groups','The manuscript defines no group law; later work suggests a filtered associative algebra.','Only inclusions and a union are written. Krichever 1983 equation (1.91) defines an infinite-dimensional algebra, giving a partial identification.','ambiguity')
# The prose-authored cells below contain mathematical formulas. Protect
# recognized formulas with math delimiters, then escape only surrounding prose.
MATH_REPLACEMENTS = {'e_1,...,e_n': 'e_1,\\ldots,e_n',
 'E_j x=0': 'E_jx=0',
 'h v=chi(h)v': 'hv=\\chi(h)v',
 'M(psi)': 'M(\\psi)',
 'L(psi)': 'L(\\psi)',
 'M(chi)': 'M(\\chi)',
 'e_{i_k}...e_{i_1}': 'e_{i_k}\\cdots e_{i_1}',
 '[L_psi : M_i/M_{i+1}]': '[L_\\psi:M_i/M_{i+1}]',
 '[M_i/M_{i+1} : L_psi]': '[M_i/M_{i+1}:L_\\psi]',
 'M_i/M_{i+1}': 'M_i/M_{i+1}',
 'P(q)=sum q^i': 'P(q)=\\sum_iq^i',
 'q^{(length(y)-length(x)-j)/2}': 'q^{(\\ell(y)-\\ell(x)-j)/2}',
 'P_{e,s}=1': 'P_{e,s}=1',
 'L(chi)_lambda': 'L(\\chi)_\\lambda',
 'chi=(a_1,...,a_n)': '\\chi=(a_1,\\ldots,a_n)',
 '0,...,n-1': '0,\\ldots,n-1',
 'a_i=lambda_{n+1-i}+i-1': 'a_i=\\lambda_{n+1-i}+i-1',
 'm(lambda,chi)=P_{n_lambda,n_chi}(1)': 'm(\\lambda,\\chi)=P_{n_\\lambda,n_\\chi}(1)',
 'm(chi,lambda)=dim L(chi)_lambda': 'm(\\chi,\\lambda)=\\dim L(\\chi)_\\lambda',
 'dim L(lambda)_mu=P_{n_mu,n_lambda}(1)': '\\dim L(\\lambda)_\\mu=P_{n_\\mu,n_\\lambda}(1)',
 'Sym^3(C^2)': '\\operatorname{Sym}^3(\\mathbb C^2)',
 'gl(2)': '\\mathfrak{gl}_2',
 'sl(2)': '\\mathfrak{sl}_2',
 'gl2': '\\mathfrak{gl}_2',
 'sl2': '\\mathfrak{sl}_2',
 '[R,R]': '[R,R]',
 'x=0': 'x=0',
 'x=+-1': 'x=\\pm1',
 'p:2^Omega -> (0,1)': 'p:2^\\Omega\\to(0,1)',
 'p:2^Omega -> {0,1}': 'p:2^\\Omega\\to\\{0,1\\}',
 'p(Omega)=1': 'p(\\Omega)=1',
 'p(empty)=0': 'p(\\varnothing)=0',
 'P(x prime=x double-prime)=1': 'P(x^{\\prime}=x^{\\prime\\prime})=1',
 'omega^{-1}': '\\omega^{-1}',
 'omega^2': '\\omega^2',
 'omega-1': '\\omega-1',
 'G=union G_n': 'G=\\bigcup_nG_n',
 'G_n': 'G_n',
 'G(Gamma,z)': 'G(\\Gamma,z)',
 'O(t^i)': 'O(t^i)',
 't^i': 't^i',
 'q^i': 'q^i',
 'M_i': 'M_i',
 'H^i': 'H^i',
 'n_+': '\\mathfrak n_+',
 'n_-': '\\mathfrak n_-',
 'chi': '\\chi',
 'lambda': '\\lambda',
 'rho': '\\rho',
 'omega': '\\omega',
 'epsilon': '\\varepsilon',
 '+--': '+\\!-\\!-',
 '1/4': '\\tfrac14',
 'A3': 'A_3',
 'R': 'R',
 'V': 'V',
 'C': '\\mathbb C',
 'n': 'n',
 'x': 'x',
 'p': 'p',
 'P': 'P'}
def correction_tex_escape(value):
    value=str(value)
    protected=[]
    pattern=re.compile(r'(?<![A-Za-z0-9_])(?:'+ '|'.join(re.escape(k) for k in sorted(MATH_REPLACEMENTS,key=len,reverse=True)) +r')(?![A-Za-z0-9_])')
    def keep(match):
        protected.append(r"\("+MATH_REPLACEMENTS[match.group(0)]+r"\)")
        return "@@MATH"+str(len(protected)-1)+"@@"
    value=pattern.sub(keep,value)
    mapping={"\\":r"\textbackslash{}","&":r"\&","%":r"\%","$":r"\$","#":r"\#","_":r"\_","{":r"\{","}":r"\}","~":r"\textasciitilde{}","^":r"\textasciicircum{}"}
    value=''.join(mapping.get(ch,ch) for ch in value)
    for n,formula in enumerate(protected):value=value.replace("@@MATH"+str(n)+"@@",formula)
    return value
for row in rows:
    for field in ('place','transcription_reads','should_read','evidence'):
        row[field]=correction_tex_escape(row[field])
with (p/'corrections.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['page','place','transcription_reads','should_read','evidence','applies_to','type']);w.writeheader();w.writerows(rows)
print('items',len(items),'bib',len(keys),'problems',len(problems),'corrections',len(rows))
