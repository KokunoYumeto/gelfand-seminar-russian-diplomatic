"""Write only bibliography entries cited by the authored block."""
import json,re
from pathlib import Path
BASE=Path(__file__).resolve().parent.parent
OUT=BASE/'fragments'
source=(BASE/'references_cumulative.bib').read_text()
entries={}
for m in re.finditer(r'@\w+\s*\{\s*([^,\s]+)\s*,',source):
    pos=m.end(); depth=1
    while pos<len(source) and depth:
        ch=source[pos]
        if ch=='{' and (pos==0 or source[pos-1]!='\\'): depth+=1
        elif ch=='}' and (pos==0 or source[pos-1]!='\\'): depth-=1
        pos+=1
    entries[m.group(1)]=source[m.start():pos]
new=r"""
@misc{cannas2007introduction,
 author={Cannas da Silva, Ana}, title={Introduction to Symplectic and Hamiltonian Geometry},
 year={2007}, howpublished={Notes for the February2002 IMPA course, revised November2007},
 url={https://www.math.ist.utl.pt/~acannas/Books/impa.pdf}, note={verified},
 annote={Full author PDF opened; Section4.4 Theorem4.11, Section4.5, and AppendixC.4 checked.}
}
@article{henon1974integrals,
 author={Hénon, Michel}, title={Integrals of the {Toda} lattice},
 journal={Physical Review B}, volume={9}, number={4}, year={1974}, pages={1921--1923},
 doi={10.1103/PhysRevB.9.1921}, url={https://journals.aps.org/prb/abstract/10.1103/PhysRevB.9.1921}, note={verified},
 annote={Publisher abstract and metadata opened. Published15February1974; received13August1973. Full PDF inaccessible.}
}
@article{kawasaki1976involution,
 author={Kawasaki, Kyozi}, title={Involution Property of Integrals in the {Toda} Lattice},
 journal={Progress of Theoretical Physics}, volume={55}, number={5}, year={1976}, pages={1668--1669},
 doi={10.1143/PTP.55.1668}, url={https://academic.oup.com/ptp/article/55/5/1668/1925490}, note={verified},
 annote={Publisher metadata opened. Received8January1976; published1May1976. Proof not accessed; no earliest-priority assertion made.}
}
@article{fradkinfradkina1978quantization,
 author={Fradkin, E. S. and Fradkina, T. E.},
 title={Quantization of relativistic systems with boson and fermion first- and second-class constraints},
 journal={Physics Letters B}, volume={72}, number={3}, year={1978}, pages={343--348},
 doi={10.1016/0370-2693(78)90135-1},
 url={https://www.sciencedirect.com/science/article/pii/0370269378901351}, note={unverified},
 annote={Publisher abstract and bibliographic data returned in search, but opening the publisher gave403 and the INSPIRE page was an empty JavaScript shell. Used only as an explicitly indirect publication lead. Publisher search dates publication2January1978; INSPIRE search identifies an August1977 report, Print-77-0793.}
}
@article{vey1975deformation,
 author={Vey, Jacques}, title={Déformation du crochet de {Poisson} sur une variété symplectique},
 journal={Commentarii Mathematici Helvetici}, volume={50}, year={1975}, pages={421--454},
 doi={10.1007/BF02565761}, url={https://eudml.org/doc/139633}, note={verified},
 annote={EuDML bibliographic record opened. The original obstruction theorem was not read; the exact H3 hypothesis remains indirectly verified.}
}
@article{kirillov1976local,
 author={Kirillov, A. A.}, title={Local {Lie} algebras},
 journal={Russian Mathematical Surveys}, volume={31}, number={4}, year={1976}, pages={55--75},
 doi={10.1070/RM1976v031n04ABEH001556}, url={https://www.mathnet.ru/eng/rm3760}, note={verified},
 annote={Publisher metadata and abstract read; full proof not obtained. Received 25 November1975 does not establish prior public circulation.}
}
@misc{emmrichweinstein1993differential,
 author={Emmrich, Claudio and Weinstein, Alan}, title={The differential geometry of {Fedosov}'s quantization},
 year={1993}, eprint={hep-th/9311094}, archivePrefix={arXiv}, url={https://arxiv.org/abs/hep-th/9311094}, note={verified},
 annote={Full author preprint opened; Sections1--2 read for the Weyl model and general symplectic construction.}
}
@misc{kostant2003euler,
 author={Kostant, Bertram}, title={Powers of the {Euler} product and commutative subalgebras of a complex simple {Lie} algebra},
 year={2003}, eprint={math/0309232}, archivePrefix={arXiv}, url={https://arxiv.org/abs/math/0309232}, note={verified},
 annote={First arXiv submission14September2003. Theorems0.1 and2.1 restate the original1976 theorem and were read in full text.}
}
@article{gelfanddikii1976fractional,
 author={Gel'fand, I. M. and Dikii, L. A.}, title={Fractional powers of operators and {Hamiltonian} systems},
 journal={Functional Analysis and Its Applications}, volume={10}, number={4}, year={1976}, pages={259--273},
 doi={10.1007/BF01076025}, url={https://www.mathnet.ru/eng/faa2188}, note={verified},
 annote={Metadata and original Russian PDF opened; Sections8--12, especially Section10 equation24, read. Received22June1976.}
}
@misc{tong2006qft,
 author={Tong, David}, title={Lectures on Quantum Field Theory}, year={2006},
 url={https://davidtong.org/teaching/quantum-field-theory/}, note={verified},
 annote={Author PDFs qft3--qft6 opened; cited sections read for Wick expansion, spinors, the Dirac propagator, Maxwell fields, and QED.}
}
@article{weinberg1967leptons,
 author={Weinberg, Steven}, title={A Model of Leptons}, journal={Physical Review Letters},
 volume={19}, year={1967}, pages={1264--1266}, doi={10.1103/PhysRevLett.19.1264},
 url={https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.19.1264}, note={verified},
 annote={Publisher metadata and full PDF opened; equations1--4 and8--16 read. Published20November1967.}
}
@article{grosswilczek1973ultraviolet,
 author={Gross, David J. and Wilczek, Frank}, title={Ultraviolet Behavior of Non-Abelian Gauge Theories},
 journal={Physical Review Letters}, volume={30}, year={1973}, pages={1343--1346},
 doi={10.1103/PhysRevLett.30.1343}, url={https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.30.1343}, note={verified},
 annote={Publisher metadata and full PDF opened; p1344 equations8--9 read. Published25June1973.}
}
@article{fukuda1998oscillation,
 author={Fukuda, Y. and others}, title={Evidence for Oscillation of Atmospheric Neutrinos},
 journal={Physical Review Letters}, volume={81}, year={1998}, pages={1562--1567},
 doi={10.1103/PhysRevLett.81.1562}, url={https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.81.1562}, note={verified},
 annote={Publisher metadata and abstract read; cited only for the observational conclusion, not the detailed analysis.}
}
@incollection{deligne1971modulaires,
 author={Deligne, Pierre}, title={Formes modulaires et représentations \(\ell\)-adiques},
 booktitle={Séminaire Bourbaki, 1968/69, exposé355}, series={Lecture Notes in Mathematics}, volume={179},
 publisher={Springer}, year={1971}, pages={139--172},
 url={https://www.numdam.org/item/SB_1968-1969__11__139_0.pdf}, note={verified},
 annote={Full text opened; Sections3--5, Theorem4.9 and Theorem5.6 read. The talk was in February1969; collected publication1971.}
}
@article{deligne1974weil,
 author={Deligne, Pierre}, title={La conjecture de {Weil}. {I}},
 journal={Publications Mathématiques de l'IHÉS}, volume={43}, year={1974}, pages={273--307},
 doi={10.1007/BF02684373}, url={https://www.numdam.org/item/PMIHES_1974__43__273_0/}, note={verified},
 annote={Publisher record and full PDF opened; the purity theorem used with Deligne1969/1971 was checked. Received20September1973; public publication28December1974.}
}
@misc{milne2017modular,
 author={Milne, James S.}, title={Modular Functions and Modular Forms}, year={2017},
 howpublished={Version1.31,22March2017}, url={https://www.jmilne.org/math/CourseNotes/MF.pdf}, note={verified},
 annote={Full author PDF opened. Proposition4.16 and Corollary5.20 read. The E12 coefficient is independently normalized; a printed coefficient in this edition is not used.}
}
@article{degosson1990maslov,
 author={de Gosson, Maurice}, title={Maslov indices on the metaplectic group {Mp}(n)},
 journal={Annales de l'Institut Fourier}, volume={40}, number={3}, year={1990}, pages={537--555},
 doi={10.5802/aif.1223}, url={https://www.numdam.org/articles/10.5802/aif.1223/}, note={verified},
 annote={Publisher metadata and full paper opened. Section1 equations1.1--1.5 and Theorems1--2 read; this section reviews the earlier Weil--Leray construction.}
}
@article{khastgirsasaki2001liouville,
 author={Khastgir, S. P. and Sasaki, R.}, title={Liouville integrability of classical {Calogero--Moser} models},
 journal={Physics Letters A}, volume={279}, number={3--4}, year={2001}, pages={189--193},
 doi={10.1016/S0375-9601(00)00842-2}, url={https://arxiv.org/abs/hep-th/0005278}, note={verified},
 annote={First public arXiv version30May2000; published29January2001. Full preprint pp3--5 and TableI read. Its scope excludes harmonic confinement.}
}
@article{sasaki2006explicit,
 author={Sasaki, R. and Takasaki, K.}, title={Explicit solutions of the classical {Calogero} and {Sutherland} systems for any root system},
 journal={Journal of Mathematical Physics}, volume={47}, number={1}, year={2006}, pages={012701},
 url={https://arxiv.org/abs/hep-th/0510035}, note={verified},
 annote={Full author preprint opened; Sections2--4 read for rational, harmonically confined, and trigonometric or hyperbolic systems. Public preprint2005; journal2006.}
}
@article{olshanetskyperelomov1978radial,
 author={Olshanetsky, M. A. and Perelomov, A. M.}, title={Quantum systems related to root systems, and radial parts of {Laplace} operators},
 journal={Functional Analysis and Its Applications}, volume={12}, number={2}, year={1978}, pages={121--128},
 doi={10.1007/BF01076255}, url={https://www.mathnet.ru/eng/faa1984}, note={verified},
 annote={Publisher metadata and full Russian PDF opened; Section2, Section3 Lemma1, Theorems1--2 and Corollary1 read for domains, radial conjugation, and group-coupling integrability. Received16June1977.}
}
@article{coleman1975equivalence,
 author={Coleman, Sidney}, title={Quantum sine-{Gordon} equation as the massive {Thirring} model},
 journal={Physical Review D}, volume={11}, number={8}, year={1975}, pages={2088--2097},
 doi={10.1103/PhysRevD.11.2088}, url={https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.2088}, note={verified},
 annote={Publisher abstract and metadata opened. Published15April1975, received6January1975. The full PDF was not accessible in this check.}
}
@article{amitsur1958commutative,
 author={Amitsur, S. A.}, title={Commutative linear differential operators},
 journal={Pacific Journal of Mathematics}, volume={8}, number={1}, year={1958}, pages={1--10},
 url={https://msp.org/pjm/1958/8-1/pjm-v8-n1-p01-p.pdf}, note={verified},
 annote={Full primary paper opened. Theorem1 on the centralizer, its commutativity and its finite free module structure was read. PublishedMarch1958; received14November1957.}
}
@article{krichever1976zakharov,
 author={Krichever, I. M.}, title={Algebraic-geometric construction of the {Zakharov--Shabat} equations and their periodic solutions},
 journal={Doklady Akademii Nauk SSSR}, volume={227}, number={2}, year={1976}, pages={291--294},
 url={https://www.mathnet.ru/eng/dan40219}, note={verified},
 annote={Metadata and full Russian PDF opened; Baker--Akhiezer lemma and differential-operator construction read. Received8October1975 and presented24October1975; neither date alone proves public circulation before the20October seminar.}
}
@article{krichever1977methods,
 author={Krichever, I. M.}, title={Methods of algebraic geometry in the theory of non-linear equations},
 journal={Russian Mathematical Surveys}, volume={32}, number={6}, year={1977}, pages={185--213},
 url={https://www.math.columbia.edu/department/krichever/pdfs/1975-1979/1977-MOAGITTONE0.pdf}, note={verified},
 annote={Full author PDF opened. Sections1--2, Theorems2.1--2.2, corollaries and theta formula read. Introduction dates related seminar discussions to November--December1975, while the supplied notebook places this occurrence on20October.}
}
"""
for m in re.finditer(r'@\w+\s*\{\s*([^,\s]+)\s*,',new):
    pos=m.end();depth=1
    while pos<len(new) and depth:
        if new[pos]=='{' and new[pos-1]!='\\':depth+=1
        elif new[pos]=='}' and new[pos-1]!='\\':depth-=1
        pos+=1
    entries[m.group(1)]=new[m.start():pos]
keys=set()
for name in ['a_items.json','a_problems.json']:
    for row in json.loads((OUT/name).read_text()):
        keys.update(row.get('refs',[]))
missing=keys-entries.keys()
if missing: raise RuntimeError(f'Missing bibliography: {missing}')
chosen=[]
for k in sorted(keys):
    entry=entries[k]
    if k!='fradkinfradkina1978quantization':
        entry=re.sub(r'\bnote\s*=\s*\{(?:unverified|verified)\}', 'note = {verified}',entry)
    chosen.append(entry)
(OUT/'a_references.bib').write_text('\n\n'.join(chosen)+'\n')
print(f'Wrote {len(chosen)} cited references.')
