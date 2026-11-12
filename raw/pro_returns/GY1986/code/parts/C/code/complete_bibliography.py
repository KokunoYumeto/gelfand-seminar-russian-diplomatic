"""Complete the slice bibliography, reusing exact cumulative keys.

The full-text/metadata distinction is recorded in annote and the item data.
No network requests are made by this reproducible assembly step.
"""
from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
workspace=root.parents[1]
target=root/'references.bib'
text=target.read_text()
cumulative=(workspace/'work/references_cumulative.bib').read_text()

def extract_entries(s):
    result={}
    for m in re.finditer(r'@\w+\s*\{\s*([^,\s]+)\s*,',s):
        depth=1;i=m.end()
        while i<len(s) and depth:
            if s[i]=='{' and (i==0 or s[i-1]!='\\'): depth+=1
            elif s[i]=='}' and (i==0 or s[i-1]!='\\'): depth-=1
            i+=1
        if not depth: result[m.group(1)]=s[m.start():i]
    return result

entries=extract_entries(text)
old=extract_entries(cumulative)
for key in ['beilinsonmanin1986mumford','borel1977zeta','connes1986indice',
            'kubotaleopoldt1964','makeenkomigdal1979exact',
            'zagier2007dilogarithm','zakharovshabat1974scheme']:
    entries[key]=old[key]

new=r'''
@article{auffingerchen2017ground,
 author={Auffinger, Antonio and Chen, Wei-Kuo}, title={Parisi formula for the ground state energy in the mixed p-spin model},
 journal={Annals of Probability}, year={2017}, volume={45}, number={6B}, pages={4617--4631},
 doi={10.1214/16-AOP1173}, url={https://arxiv.org/pdf/1606.05335}, note={verified},
 annote={Original preprint opened and Theorem 1 read. First arXiv version June 2016; journal issue November 2017.}
}
@article{baranovmaninfrolovschwarz1987selberg,
 author={Baranov, M. A. and Manin, Yu. I. and Frolov, I. V. and Schwarz, A. S.},
 title={A superanalog of the {Selberg} trace formula and multiloop contributions for fermionic strings},
 journal={Communications in Mathematical Physics}, year={1987}, volume={111}, pages={373--392},
 doi={10.1007/BF01238904}, url={https://link.springer.com/article/10.1007/BF01238904}, note={verified},
 annote={Publisher abstract and metadata opened; September 1987 issue. Original proof not inspected. Author initial differs in some publisher indexing; Math-Net Manin bibliography uses M. A.}
}
@article{beilinsonmacphersonschechtman1987motivic,
 author={Beilinson, A. A. and MacPherson, Robert D. and Schechtman, V. V.}, title={Notes on motivic cohomology},
 journal={Duke Mathematical Journal}, year={1987}, volume={54}, number={2}, pages={679--710},
 doi={10.1215/S0012-7094-87-05430-5}, url={https://www.math.ias.edu/files/rdm/publications.pdf}, note={verified},
 annote={MacPherson's institutional bibliography, entry 38, opened and checked. Direct DOI full-text access failed. Exact mathematical comparison is therefore indirect, with low-weight formulas checked separately in Goncharov 2016.}
}
@article{brezinitzyksonparisizuber1978planar,
 author={Br{\'e}zin, Edouard and Itzykson, Claude and Parisi, Giorgio and Zuber, Jean-Bernard}, title={Planar diagrams},
 journal={Communications in Mathematical Physics}, year={1978}, volume={59}, pages={35--51},
 doi={10.1007/BF01614153}, url={https://www.lpthe.jussieu.fr/~zuber/MesPapiers/bipz_CMP78.pdf}, note={verified},
 annote={Full author-hosted original opened; planar eigenvalue/resolvent construction read.}
}
@article{burtsevzakharovmikhailov1987variable,
 author={Burtsev, S. P. and Zakharov, V. E. and Mikhailov, A. V.}, title={Inverse scattering method with variable spectral parameter},
 journal={Theoretical and Mathematical Physics}, year={1987}, volume={70}, number={3}, pages={227--240},
 doi={10.1007/BF01040999}, url={https://zakharov.itp.ac.ru/pub/data/1987/1987-04-Russian-tmf4658.pdf}, note={verified},
 annote={Full Russian original opened: Teoreticheskaya i Matematicheskaya Fizika 70 (1987), 323--341. Received 6 February 1986. Introductory spectral-vector-field operators and gravity specialization inspected.}
}
@misc{cornelissenlorscheid2011toroidal,
 author={Cornelissen, Gunther and Lorscheid, Oliver}, title={Toroidal automorphic forms, {Waldspurger} periods and double {Dirichlet} series},
 year={2011}, eprint={0906.5284}, archivePrefix={arXiv}, url={https://arxiv.org/pdf/0906.5284}, note={verified},
 annote={First preprint 29 June 2009, revised 15 August 2011. Main Theorem and Sections 4--6 read; temperedness, not unitarity alone, is the RH-relevant spectral restriction.}
}
@article{cranerabin1988uniformization,
 author={Crane, Louis and Rabin, Jeffrey M.}, title={Super {Riemann} surfaces: Uniformization and {Teichm{\"u}ller} theory},
 journal={Communications in Mathematical Physics}, year={1988}, volume={113}, pages={601--623},
 url={https://mathweb.ucsd.edu/~jrabin/publications/Uniformization.pdf}, note={verified},
 annote={Full author-hosted original opened. Sections 2--5 and the distinction from Rogers topology in Section 6 inspected.}
}
@techreport{esnaultviehweg1987deligne,
 author={Esnault, H{\'e}l{\`e}ne and Viehweg, Eckart}, title={Deligne--Beilinson cohomology},
 institution={Max-Planck-Institut f{\"u}r Mathematik}, number={MPI 87-2}, year={1987},
 url={https://archive.mpim-bonn.mpg.de/id/eprint/2980/1/preprint_1987_2.pdf}, note={verified},
 annote={Full original preprint, explicitly named in the notebook, opened. Sections 1--3, 7, and Proposition 8.2 read; cited as the 1987 circulation version.}
}
@article{fokaszakharov1992dressing,
 author={Fokas, A. S. and Zakharov, V. E.}, title={The dressing method and nonlocal {Riemann--Hilbert} problems},
 journal={Journal of Nonlinear Science}, year={1992}, volume={2}, number={1}, pages={109--134},
 doi={10.1007/BF02429853}, url={https://zakharov75.itp.ac.ru/static/local/zve75/zakharov/1992/1992-04-art3A10.10072FBF02429853.pdf}, note={verified},
 annote={Full original opened; introductory distinction between nonlocal Riemann--Hilbert and d-bar formulations read. Received 22 May 1991, accepted 17 October 1991.}
}
@article{garkusha2023semilocal,
 author={Garkusha, Grigory}, title={Semilocal {Milnor} {K}-theory},
 journal={International Mathematics Research Notices}, year={2023}, volume={2023}, number={24}, pages={22069--22095},
 doi={10.1093/imrn/rnac343}, url={https://arxiv.org/pdf/2007.09044}, note={verified},
 annote={Full author preprint opened; Section 4, Theorem 4.1 states criteria for Beilinson--Soule vanishing. Initial preprint July 2020; revised November 2022; publisher search record confirms online publication 20 December 2022, December 2023 issue, volume 2023, pages 22069--22095 and DOI.}
}
@misc{gelbart2012reciprocal,
 author={Gelbart, Stephen and Miller, Stephen D. and Pantchichkine, Alexei and Shahidi, Freydoon},
 title={A p-adic integral for the reciprocal of {L}-functions}, year={2012},
 eprint={1001.1913}, archivePrefix={arXiv}, url={https://arxiv.org/pdf/1001.1913}, note={verified},
 annote={First preprint January 2010; inspected version dated 19 December 2012. Equations 2.1 and 2.12--2.13 give the bounded-measure regularization and its difference from the Bernoulli distribution.}
}
@article{goncharov2016exponential,
 author={Goncharov, Alexander B.}, title={Exponential complexes, period morphisms, and characteristic classes},
 journal={Annales de la Facult{\'e} des Sciences de Toulouse. Math{\'e}matiques}, year={2016}, volume={25}, number={2--3}, pages={619--681},
 doi={10.5802/afst.1507}, url={https://www.numdam.org/item/AFST_2016_6_25_2-3_619_0.pdf}, note={verified},
 annote={Full original opened. Proposition 1.7 and Sections 1.5, 1.7, 1.8, 4 inspected. Rational/exterior-square conventions and the limits of all-weight polylogarithmic formulas distinguished.}
}
@article{gunhazrasahu2025artin,
 author={Gun, Sanoli and Hazra, Suhita and Sahu, Dhananjaya}, title={On holomorphy and non-vanishing of {Artin} {L}-functions},
 journal={Monatshefte f{\"u}r Mathematik}, year={2025}, volume={206}, pages={853--883},
 doi={10.1007/s00605-025-02060-7}, url={https://link.springer.com/article/10.1007/s00605-025-02060-7}, note={verified},
 annote={Full open-access article opened. Definition and current-status statements in the Introduction read. Published 17 February 2025.}
}
@article{haagerup1987bicentralizer,
 author={Haagerup, Uffe}, title={Connes' bicentralizer problem and uniqueness of the injective factor of type {III$_1$}},
 journal={Acta Mathematica}, year={1987}, volume={158}, pages={95--148},
 doi={10.1007/BF02392257}, url={https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-haagerup/1980s/1987_Connes_bicentralizer_problem_and_uniqueness_of_the_injective_factor_of_type_III_1.pdf}, note={verified},
 annote={Full original opened. Section 2 uniqueness result inspected. Received 21 January 1985; printed April 1987.}
}
@article{jones1987hecke,
 author={Jones, Vaughan F. R.}, title={Hecke algebra representations of braid groups and link polynomials},
 journal={Annals of Mathematics}, year={1987}, volume={126}, number={2}, pages={335--388},
 doi={10.2307/1971403}, url={https://ymsc.tsinghua.edu.cn/__local/3/3F/62/1293A0A1D1BE2BC710A48385251_F41A5764_34E7A6.pdf}, note={verified},
 annote={Full original opened. Sections 2, 4--6, 12, Theorem 5.1 and the explicit discussion of roots of unity after Theorem 4.5 read. The 1985 circulation is separately witnessed by Connes.}
}
@incollection{kudla2003tate,
 author={Kudla, Stephen S.}, title={Tate's thesis}, editor={Bernstein, Joseph and Gelbart, Stephen},
 booktitle={An Introduction to the Langlands Program}, publisher={Birkh{\"a}user}, year={2003}, pages={109--131},
 url={https://u.cs.biu.ac.il/~reznikov/courses/kudla-1.pdf}, note={verified},
 annote={Full lecture text opened, local zeta integrals and functional equation inspected. Lectures March 2001; publisher page gives softcover publication 20 May 2003 and a separate 2004 copyright label.}
}
@article{makeenko2008cusped,
 author={Makeenko, Yuri}, title={Topics in cusped/lightcone {Wilson} loops},
 journal={Acta Physica Polonica B}, year={2008}, volume={39}, number={12}, pages={3047--3080},
 url={https://www.actaphys.uj.edu.pl/fulltext?page=3047&series=Reg&vol=39}, note={verified},
 annote={Full author review opened; Section 3.1 equation 3.2 and Section 3.3 regularization read. Received 20 October 2008.}
}
@article{mantillasoler2019equivalence,
 author={Mantilla-Soler, Guillermo}, title={On a question of {Perlis} and {Stuart} regarding arithmetic equivalence},
 journal={New York Journal of Mathematics}, year={2019}, volume={25}, pages={558--573},
 url={https://nyjm.albany.edu/j/2019/25-25p.pdf}, note={verified},
 annote={Full original opened. Theorem 2.5, Corollary 2.8 and Section 3 examples inspected; used to verify representation versus field determination, not as an origin claim.}
}
@book{mazzavoevodskyweibel2006motivic,
 author={Mazza, Carlo and Voevodsky, Vladimir and Weibel, Charles}, title={Lecture Notes on Motivic Cohomology},
 series={Clay Mathematics Monographs}, volume={2}, publisher={American Mathematical Society and Clay Mathematics Institute}, year={2006},
 url={https://www.claymath.org/wp-content/uploads/2022/03/Motivic-Cohomology.pdf}, note={verified},
 annote={Full original book opened. Based on 1999--2000 IAS lectures. Motivic constructions, Milnor comparison and explicit distinction from Beilinson--Soule vanishing inspected.}
}
@article{panchenko2013ultrametricity,
 author={Panchenko, Dmitry}, title={The {Parisi} ultrametricity conjecture},
 journal={Annals of Mathematics}, year={2013}, volume={177}, number={1}, pages={383--393},
 doi={10.4007/annals.2013.177.1.8}, url={https://arxiv.org/pdf/1112.1003}, note={verified},
 annote={Theorem 1 and the exact Ghirlanda--Guerra hypotheses read. First preprint December 2011; original publication 2013; retrieved arXiv revision March 2015.}
}
@article{parisiwu1981perturbation,
 author={Parisi, Giorgio and Wu, Yong-Shi}, title={Perturbation theory without gauge fixing},
 journal={Scientia Sinica}, year={1981}, volume={24}, pages={483--496},
 doi={10.1360/YA1981-24-4-483}, url={https://inspirehep.net/literature/9589}, note={unverified},
 annote={Bibliographic search matches author bibliography and INSPIRE; direct author page timed out and the opened INSPIRE page was JavaScript-only. Original text not obtained.}
}
@article{roslyschwarzvoronov1988geometry,
 author={Rosly, A. A. and Schwarz, A. S. and Voronov, A. A.}, title={Geometry of superconformal manifolds},
 journal={Communications in Mathematical Physics}, year={1988}, volume={119}, number={1}, pages={129--152},
 doi={10.1007/BF01218264}, url={https://experts.umn.edu/en/publications/geometry-of-superconformal-manifolds}, note={verified},
 annote={Publisher and author-institution metadata and abstract opened; original full proof not recovered. March 1988 publication. Exact technical qualifications checked in the separately opened Witten notes.}
}
@article{salamon1986quaternionic,
 author={Salamon, Simon M.}, title={Differential geometry of quaternionic manifolds},
 journal={Annales Scientifiques de l'{\'E}cole Normale Sup{\'e}rieure}, year={1986}, volume={19}, number={1}, pages={31--55},
 doi={10.24033/asens.1503}, url={https://www.numdam.org/item/10.24033/asens.1503.pdf}, note={verified},
 annote={Full original opened. Sections 1--3 and Corollary 7.4 inspected; published before the lecture.}
}
@incollection{soule1986regulateurs,
 author={Soul{\'e}, Christophe}, title={R{\'e}gulateurs}, booktitle={S{\'e}minaire Bourbaki, 1984/85},
 series={Ast{\'e}risque}, volume={133--134}, number={644}, publisher={Soci{\'e}t{\'e} Math{\'e}matique de France}, year={1986}, pages={237--253},
 url={https://www.numdam.org/article/SB_1984-1985__27__237_0.pdf}, note={verified},
 annote={Full original opened; title page confirms February 1985 lecture separately from 1986 publication.}
}
@misc{soule2026interview,
 author={Soul{\'e}, Christophe}, title={An interview with {Christophe Soul{\'e}}},
 howpublished={Institut des Hautes {\'E}tudes Scientifiques}, year={2026},
 url={https://www.ihes.fr/en/interview-soule/}, note={verified},
 annote={Institutional interview dated 4 November 2026 opened. Soul{\'e}'s direct statement that the Beilinson--Soule conjecture remains open is used for near-cutoff status, not for a proof.}
}
@article{sudbery1979quaternionic,
 author={Sudbery, Anthony}, title={Quaternionic analysis},
 journal={Mathematical Proceedings of the Cambridge Philosophical Society}, year={1979}, volume={85}, number={2}, pages={199--225},
 url={https://dougsweetser.github.io/Q/Stuff/pdfs/Quaternionic-analysis.pdf}, note={verified},
 annote={Full author's text opened. Section 3 Theorem 1 proves the affine-rigidity statement; publisher metadata confirms March 1979 issue.}
}
@article{suslin1991bloch,
 author={Suslin, Andrei A.}, title={K$_3$ of a field, and the {Bloch} group},
 journal={Proceedings of the Steklov Institute of Mathematics}, year={1991}, volume={183}, pages={217--239},
 url={https://www.maths.dur.ac.uk/users/herbert.gangl/Suslin_K3_Bloch_group.pdf}, note={verified},
 annote={Original scanned English text opened; introduction p. 217 and Theorem 5.2 p. 237 read using local OCR and scan. Russian original Trudy Matematicheskogo Instituta Steklova 183 (1990), 180--199. English issue is dated 1991, copyright 1992. Suslin states that most results were obtained in 1982; the 1987 notebook also witnesses prior circulation. The theorem requires an infinite field.}
}
@article{talagrand2006parisi,
 author={Talagrand, Michel}, title={The {Parisi} formula},
 journal={Annals of Mathematics}, year={2006}, volume={163}, number={1}, pages={221--263},
 doi={10.4007/annals.2006.163.221}, url={https://annals.math.princeton.edu/2006/163-1/p04}, note={verified},
 annote={Publisher metadata and result description opened; original full proof not read. Received March 2003, accepted December 2004, published 2006.}
}
@misc{witten2012superriemann,
 author={Witten, Edward}, title={Notes on super {Riemann} surfaces and their moduli}, year={2012},
 eprint={1209.2459}, archivePrefix={arXiv}, url={https://arxiv.org/pdf/1209.2459}, note={verified},
 annote={Full original author notes opened, inspected version 5 dated 20 May 2017. Sections 2.1--2.2, 3.4--3.6, and 8 used for precise definitions and qualifications.}
}
@book{wright1989uniqueness,
 author={Wright, Steve}, title={Uniqueness of the Injective {III$_1$} Factor},
 series={Lecture Notes in Mathematics}, volume={1413}, publisher={Springer}, year={1989},
 doi={10.1007/BFb0090178}, url={https://link.springer.com/book/10.1007/BFb0090178}, note={verified},
 annote={Publisher description opened; it records that the proof was lectured in winter 1985--1986, independently confirming circulation before the 1987 seminar.}
}
@article{zakharovmanakov1984multidimensional,
 author={Zakharov, V. E. and Manakov, S. V.}, title={Multidimensional nonlinear integrable systems and methods for constructing their solutions},
 journal={Zapiski Nauchnykh Seminarov LOMI}, year={1984}, volume={133}, pages={77--91},
 url={https://zakharov.itp.ac.ru/pub/data/1984/1984-05-Russian-znsl4411.pdf}, note={verified},
 annote={Full Russian original opened. Section 1 normalized solvability assumption and d-bar extension discussion inspected. English translation Journal of Soviet Mathematics 31 (1985), 3307--3316, DOI 10.1007/BF02107232.}
}
'''
entries.update(extract_entries(new))
entries['zakharovshabat1974scheme']=re.sub(r'\s*annote\s*=\s*\{[^}]*\}', ' annote={Original Russian full text opened on 12 November 2026 through Math-Net. Section 1 factorization, unique-solvability condition and Theorems 1--2 read; Section 2 scalar KdV and KP examples and Section 3 finite-rank soliton construction inspected. Received 14 March 1974. The notebook conventions are reconstructed explicitly rather than silently identified with the original normalization.}', entries['zakharovshabat1974scheme'])
target.write_text('\n\n'.join(entries.values())+'\n')
print('Bibliography entries:',len(entries))
