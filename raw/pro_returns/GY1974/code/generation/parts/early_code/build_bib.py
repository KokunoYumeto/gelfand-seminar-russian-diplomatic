from pathlib import Path
import re,json
root=Path(__file__).resolve().parents[2]
s=(root/'references_cumulative.bib').read_text()
entries={}
for m in re.finditer(r'@\w+\s*\{\s*([^,\s]+)\s*,',s):
 i=m.end(); depth=1
 while i<len(s) and depth:
  if s[i]=='{' and (i==0 or s[i-1]!='\\'):depth+=1
  elif s[i]=='}' and (i==0 or s[i-1]!='\\'):depth-=1
  i+=1
 entries[m.group(1)]=s[m.start():i]
used={k for v in json.loads((root/'parts/early_items.json').read_text()) for k in v['refs']}
boundary={'shabat1973kdv','shabat2014interpolation','mckeansinger1967curvature','gilkey1979recursion','sakai1971eigenvalues','balianbloch1972oscillations','colindeverdiere1973geodesicsii','duistermaathormander1972fourierii','duistermaatguillemin1975spectrum','shnirelman1975multiplicity'}
new=r'''
@inproceedings{anderson1967special,
 author={Anderson, R. D.}, title={Some special methods of homeomorphism theory in infinite-dimensional topology},
 booktitle={General Topology and its Relations to Modern Analysis and Algebra II: Proceedings of the Second Prague Topological Symposium, 1966},
 publisher={Academia}, address={Prague}, year={1967}, pages={31--38},
 url={https://dml.cz/manakin/bitstream/handle/10338.dmlcz/700850/Toposym_02-1966-1_9.pdf}, note={verified},
 annote={Primary proceedings read, p.31 infinite-dimensional separable Frechet classification and Theorem4/Corollary4 pp.37--38 on Z-set unknotting. The theorem requires infinite dimension.}
}
@article{andersonchapman1971extending,
 author={Anderson, R. D. and Chapman, T. A.}, title={Extending homeomorphisms to Hilbert cube manifolds},
 journal={Pacific Journal of Mathematics}, year={1971}, volume={38}, number={2}, pages={281--293},
 url={https://msp.org/pjm/1971/38-2/pjm-v38-n2-p01-p.pdf}, note={verified},
 annote={Primary full paper opened; introduction p.281 states the earlier Hilbert-cube Z-set extension theorem. Theorem6.1 concerns ambient isotopy and proper homotopy on Q-manifolds. Received1June1970.}
}
@article{dubrovinnovikov1974periodicity,
 author={Dubrovin, B. A. and Novikov, S. P.}, title={A periodicity problem for the Korteweg--de Vries and Sturm--Liouville equations. Their connection with algebraic geometry},
 journal={Doklady Akademii Nauk SSSR}, year={1974}, volume={219}, number={3}, pages={531--534},
 url={https://people.sissa.it/~dubrovin/Papers/1974/dubrovin_novikov_1974_dan.pdf}, note={verified},
 annote={Author-hosted English text read in full. Received3June1974. Section2 attributes stationary-to-finite-gap to Novikov; section3 gives the converse and divisor description; section4 gives the genus-two Hamiltonian. Its quartic coefficient is5/8 after expansion. Apparent typographical omissions in the available transcription and a conditional constant-term sign mismatch prohibit treating every printed formula as authoritative normalization.}
}
@article{dubrovinnovikov1974periodic,
 author={Dubrovin, B. A. and Novikov, S. P.}, title={Periodic and conditionally periodic analogs of the many-soliton solutions of the Korteweg--de Vries equation},
 journal={Soviet Physics JETP}, year={1974}, volume={40}, number={6}, pages={1058--1063},
 url={https://www.jetp.ras.ru/cgi-bin/dn/e_040_06_1058.pdf}, note={verified},
 annote={Primary English full text opened. Submitted5July1974; Russian ZhETF67,2131--2144,December1974; English printing bears1975copyright. Finite-gap curve, normalized Bloch divisor and linearization checked; the translation's year convention is retained in the key.}
}
@article{giusti1969partial,
 author={Giusti, Enrico}, title={Regolarit\`a parziale delle soluzioni di sistemi ellittici quasi-lineari di ordine arbitrario},
 journal={Annali della Scuola Normale Superiore di Pisa, Classe di Scienze}, series={3}, year={1969}, volume={23}, number={1}, pages={115--141},
 url={https://www.numdam.org/article/ASNSP_1969_3_23_1_115_0.pdf}, note={verified},
 annote={Primary scan opened. Received6July1968. The text confirms arbitrary-order partial regularity, but formula extraction does not establish the exact handwritten higher-order dimension claim. Used as a partial historical match, not an exact theorem verification.}
}
@article{giusti1976boundary,
 author={Giusti, Enrico}, title={Boundary value problems for non-parametric surfaces of prescribed mean curvature},
 journal={Annali della Scuola Normale Superiore di Pisa, Classe di Scienze}, series={4}, year={1976}, volume={3}, number={3}, pages={501--548},
 url={https://www.numdam.org/article/ASNSP_1976_4_3_3_501_0.pdf}, note={verified},
 annote={Primary paper read, introduction and section1 on BV area, relaxed boundary data and perimeter inequalities. Received16February1976, revised8March1976. Intro credits pre1974 variational work; later mixed-boundary existence results are not backdated into the elementary notebook definitions.}
}
@inproceedings{giusti1982basic,
 author={Giusti, Enrico}, title={Basic regularity of the minima of variational integrals},
 editor={Gregu\v{s}, Michal}, booktitle={Equadiff 5}, series={Teubner-Texte zur Mathematik}, volume={47},
 publisher={Teubner}, year={1982}, pages={111--114},
 url={https://dml.cz/bitstream/handle/10338.dmlcz/702271/Equadiff_05-1982-1_26.pdf}, note={verified},
 annote={Primary text read, growth assumptions and the distinction between minima and stationary solutions. Conference Bratislava24--28August1981. Does not turn the abbreviated1974 scalar remark into an unrestricted theorem.}
}
@article{mingione2006regularity,
 author={Mingione, Giuseppe}, title={Regularity of minima: an invitation to the Dark Side of the Calculus of Variations},
 journal={Applications of Mathematics}, year={2006}, volume={51}, number={4}, pages={355--426},
 doi={10.1007/s10778-006-0110-3}, url={https://dml.cz/bitstream/handle/10338.dmlcz/134645/AplMat_51-2006-4_4.pdf}, note={verified},
 annote={Author's review read, especially section3.2 equations3.3--3.5 and Theorem4.1. The reproduced Giusti--Miranda tensor has4/(n-2) in both factors. This is indirect verification of the1968 original; existence for the corrected homogeneous system is also proved directly in the companion, without asserting uniqueness or variational minimality.}
}
@incollection{milne1986jacobian,
 author={Milne, J. S.}, title={Jacobian varieties}, editor={Cornell, Gary and Silverman, Joseph H.},
 booktitle={Arithmetic Geometry}, publisher={Springer}, year={1986}, pages={167--212},
 url={https://www.jmilne.org/math/xnotes/JVs.pdf}, note={verified},
 annote={Author's corrected online version dated12June2021 opened; section2 analytic Jacobian and Theorem5.1 Abel map read. The degree-g symmetric product maps birationally onto the Jacobian, with exceptional fibres linear systems, not by a global isomorphism.}
}
@misc{milne2008abelian,
 author={Milne, J. S.}, title={Abelian varieties}, year={2008}, howpublished={Course notes, version2.0},
 url={https://www.jmilne.org/math/CourseNotes/AV.pdf}, note={verified},
 annote={Primary author course notes opened. ChapterI section2, Lemma2.4 and Theorem2.8 on Riemann forms and polarizable complex tori read; section18 gives analytic Jacobians. These are classical results, not2008novelties. The exact period-matrix quotient is a standard reconstruction from a symplectic marking.}
}
@inproceedings{johnstara1990regularity,
 author={John, Old\v{r}ich and Star\'a, Jana}, title={On the regularity and non-regularity of elliptic and parabolic systems},
 editor={Kurzweil, Jaroslav}, booktitle={Equadiff 7}, series={Teubner-Texte zur Mathematik}, volume={118},
 publisher={Teubner}, year={1990}, pages={28--36},
 url={https://dml.cz/bitstream/handle/10338.dmlcz/702382/Equadiff_07-1990-1_5.pdf}, note={verified},
 annote={Primary authors' survey read, pp.28--30 for scalar and two-dimensional energy regularity and the different classes of nonlinear systems. Conference Prague1989. Used with explicit class restrictions.}
}
@techreport{frehse2007irregular,
 author={Frehse, Jens}, title={An irregular complex valued solution to a scalar uniformly elliptic equation},
 institution={Universit\"at Bonn, SFB611}, number={343}, year={2007},
 url={https://webdoc.sub.gwdg.de/ebook/serien/e/sfb611/343.pdf}, note={verified},
 annote={Primary author preprint dated16July2007 read. Theorem3.1 gives a complex scalar equation with measurable spatial coefficients in n>=3; as a real system it has two components. This is not an exact match for analytic coefficients depending only on the unknown. Theorem3.2 concerns a different semilinear example.}
}
@misc{defilippismingionenowak2026partial,
 author={De Filippis, Cristiana and Mingione, Giuseppe and Nowak, Simon}, title={Partial regularity in nonlocal systems I},
 year={2026}, eprint={2501.08405}, archivePrefix={arXiv},
 url={https://arxiv.org/abs/2501.08405}, note={verified},
 annote={Primary author manuscript first posted14January2025, revised8July2026, opened and read. Introduction equations1.1--1.2 restates classical local partial regularity with strict Hausdorff dimension below n-2 for uniformly elliptic bounded coefficients uniformly continuous in x,u. Used only for that precisely delimited recalled local theorem, not as the first proof.}
}
'''
# The explicit entries above supersede any cumulative duplicate of the same key.
newkeys=set(re.findall(r'@\w+\{([^,]+),',new))
missing=(used|boundary)-newkeys-set(entries)
assert not missing,missing
updates={
 'novikov1974periodic':'Current audit: full Russian original read at pp.56--65, especially Theorem2.1 and equations18--19. Received18February1974; publisher records publication July1974, before the September talks. Stationary-to-finite-gap and explicit genus-two Hamiltonian are therefore expository in the current chapter; the converse is attributed to Dubrovin--Novikov.',
 'dubrovinmatveevnovikov1976nonlinear':'Current audit: Math-Net metadata and author-hosted English full text opened at https://people.sissa.it/~dubrovin/Papers/1976/dubrovin_matveev_novikov_1976.pdf. ChapterII sections1--4 read for Floquet theory, Riccati construction, divisor linearization and marked total family. Page105 gives q1=u,q2=u_xx-5u^2/2,p1=q2_x,p2=u_x; spectral signs are retained as a normalization caveat.',
 'duistermaathormander1972fourierii':'Current audit: full primary article opened; the exact Theorem6.1.1 statement was recovered from the indexed primary PDF after repeated direct pinpoint opens timed out. Publisher confirms received3September1971, publicationJuly1972. The proof was not re-read in full in this current audit.',
 'shnirelman1975multiplicity':'Current audit: both primary pages reopened and read via Math-Net getFT option_lang=eng. The theorem is for every k>1, not only a positive-density subsequence; manuscript received7May1974, publication1975.',
 'shabat2014interpolation':'Current audit: complete primary Russian PDF opened, introductionp305 and section3 Theorem1 read. The text explicitly recalls1974Gelfand seminar; theorem imposes normalization p0q0=1 and nondegenerate interpolation equations. This does not validate the notebook arbitrary-data or ratio-at-infinity convention.'
}
for k,v in updates.items():
 if k in entries:entries[k]=entries[k].rstrip()[:-1]+',\n verificationrecord={'+v+'}\n}'

out='%% Early records: verified bibliography checkpoint, 9 November 2026.\n'
for k in sorted((used|boundary)-newkeys):out+=entries[k]+'\n\n'
out+=new
(root/'parts/early_references.bib').write_text(out)
print(len((used|boundary)|newkeys),'entries written')
