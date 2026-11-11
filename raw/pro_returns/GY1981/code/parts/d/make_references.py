"""Reuse cumulative keys; add only checked root-block bibliographic records."""
import re
from pathlib import Path
root=Path(__file__).resolve().parent
source=(root.parents[1]/'references_cumulative.bib').read_text()
entries={}
for match in re.finditer(r'(?m)^@(\w+)\s*\{\s*([^,]+),',source):
    start=match.start();pos=source.index('{',start);depth=1;i=pos+1
    while i<len(source) and depth:
        if source[i]=='{' and source[i-1]!='\\':depth+=1
        if source[i]=='}' and source[i-1]!='\\':depth-=1
        i+=1
    entries.setdefault(match.group(2).strip(),source[start:i])

reused={
 'atiyah1982convexity':'Full primary PDF opened; introduction and Theorems 1--2 read. Received 27 March 1981. Earlier seminar item 1980-508.15 records circulation.',
 'atiyahbottpatodi1973heat':'Publisher DOI page and author bibliography opened; metadata verified. Exact local-density scope also checked against the Gilkey book and APS I.',
 'atiyahpatodisinger1973spectral':'Author bibliography opened; the 1973 announcement is also listed in the full APS I reference list. Publisher DOI returned 403. Metadata verification only.',
 'atiyahpatodisinger1975spectral1':'Full original PDF opened. Introduction, Theorem (3.10), Theorem (4.14) and the final cobordism discussion read. Received 25 March 1974, published 1975.',
 'gilkey1981residue':'Full author-hosted PDF opened; Introduction and Theorem 0.1 read for all-dimensional global regularity and possibly nonzero local residue.',
 'gilkey1984invariance':'Complete author-hosted first-edition electronic reprint opened. Chapters 1.7, 1.10 and the geometric index sections consulted. The electronic reprint date is not the original 1984 publication.',
 'kirillov1968characters':'Math-Net metadata and complete Russian original opened. Section 3, Theorem 2 and equations (26)--(28), pp.52--53, explicitly use the lambda-plus-rho orbit and its dimension/volume identity.',
 'mahler1958interpolation':'Original author-archive scan opened, but no usable text layer was returned. Used for the established binomial-basis antecedent; no claim of a spectral p-adic interpolation theorem.',
 'seeley1968powers':'Math-Net bibliographic page opened. This is the 1968 Russian translation, not a new 1982 result. Original sign conventions were not checked sufficiently to endorse the notebook allegation of a sign error.'
}
parts=[]
for key,ann in reused.items():
    e=entries[key]
    e=re.sub(r'(?m)^\s*annote\s*=.*?(?=\n\s*\}|\n\s*\w+\s*=)', '', e, flags=re.S)
    e=e.rstrip()[:-1].rstrip().rstrip(',')+',\n  annote = {'+ann+'}\n}'
    if key=='gilkey1984invariance':e=re.sub(r'url\s*=\s*\{[^}]*\}',r'url = {https://pages.uoregon.edu/gilkey/dirPDF/InvarianceTheory1Ed.pdf}',e)
    if key=='atiyahpatodisinger1975spectral1':e=re.sub(r'url\s*=\s*\{[^}]*\}',r'url = {https://webhomes.maths.ed.ac.uk/~v1ranick/papers/aps001.pdf}',e)
    parts.append(e)

parts.append(r'''
@incollection{arnoldgivental1990symplectic,
 author = {Arnol'd, V. I. and Givental', A. B.},
 title = {Symplectic geometry},
 editor = {Arnol'd, V. I. and Novikov, S. P.},
 booktitle = {Dynamical Systems IV: Symplectic Geometry and Its Applications},
 series = {Encyclopaedia of Mathematical Sciences}, volume = {4},
 publisher = {Springer}, year = {1990}, pages = {1--136},
 url = {https://webhomes.maths.ed.ac.uk/~v1ranick/papers/arnogive.pdf},
 note = {verified},
 annote = {Full English primary chapter opened; Chapter 2 section 1.3, pp.24--25, relative Darboux and extension theorems and proofs read. Math-Net intf33 verifies the Russian original in 1985, pp.5--135. Springer first-edition metadata verifies 1990 English publication.}
}

@article{berezingelfand1956spherical,
 author = {Berezin, F. A. and Gel'fand, I. M.},
 title = {Some remarks on the theory of spherical functions on symmetric {Riemannian} manifolds},
 journal = {Trudy Moskovskogo Matematicheskogo Obshchestva},
 volume = {5}, year = {1956}, pages = {311--351},
 url = {https://www.mathnet.ru/eng/mmo51}, note = {verified},
 annote = {Math-Net metadata and full Russian original opened. Received 28 June 1955; the first-page footnote records a 6 December 1955 Moscow Mathematical Society presentation. The notebook attribution is a partial historical match, not a claim that the 1982 quantization formula occurs here.}
}

@article{givental1983lagrangian,
 author = {Givental', A. B.},
 title = {{Lagrangian} varieties with singularities and irreducible sl2-modules},
 journal = {Russian Mathematical Surveys}, year = {1983},
 volume = {38}, number = {6}, pages = {121--122},
 doi = {10.1070/RM1983v038n06ABEH003459},
 url = {https://www.mathnet.ru/eng/rm3010}, note = {verified},
 annote = {Math-Net metadata and both pages of the English original read, especially Examples 1--2 and the Theorem/Corollary. Received 19 July 1982. Russian original pp.109--110.}
}

@article{guilleminsternberg1982multiplicities,
 author = {Guillemin, Victor and Sternberg, Shlomo},
 title = {Geometric quantization and multiplicities of group representations},
 journal = {Inventiones Mathematicae}, volume = {67},
 year = {1982}, pages = {515--538},
 doi = {10.1007/BF01398934},
 url = {https://link.springer.com/article/10.1007/BF01398934},
 note = {verified},
 annote = {Publisher metadata opened: October 1982 publication. Notebook P1015 supplies evidence of circulation as a preprint by March 1982. Full original theorem was not read; its scope is corroborated by Meinrenken--Sjamaar.}
}

@article{meinrenkensjamaar1999singular,
 author = {Meinrenken, Eckhard and Sjamaar, Reyer},
 title = {Singular reduction and quantization},
 journal = {Topology}, volume = {38}, number = {4},
 year = {1999}, pages = {699--762},
 doi = {10.1016/S0040-9383(98)00012-3},
 url = {https://arxiv.org/abs/dg-ga/9707023}, note = {verified},
 annote = {Full July 1997 preprint opened, including introduction and sections 2.1--2.4. The desingularized Riemann--Roch definition and the precise reduced-space index are distinguished from the notebook level set.}
}

@article{gelfandzelevinskykapranov1989hypergeometric,
 author = {Gel'fand, I. M. and Zelevinskii, A. V. and Kapranov, M. M.},
 title = {Hypergeometric functions and toral manifolds},
 journal = {Functional Analysis and Its Applications},
 volume = {23}, number = {2}, year = {1989}, pages = {94--106},
 doi = {10.1007/BF01078777}, url = {https://www.mathnet.ru/eng/faa1015},
 note = {verified},
 annote = {Math-Net primary metadata and bibliography opened. This is a thematic successor to the unformulated multivariable programme, not an exact solution of a notebook conjecture.}
}

@misc{nist2026hypergeometric,
 author = {{National Institute of Standards and Technology}},
 title = {{Digital Library of Mathematical Functions}, Section 15.6: Integral representations},
 year = {2026}, url = {https://dlmf.nist.gov/15.6}, note = {verified},
 annote = {Equation 15.6.1 and its convergence and branch conditions opened and read on 11 November 2026. The source uses the regularized hypergeometric function; the companion converts explicitly to ordinary 2F1.}
}

@article{mehrmannpoloni2012doubling,
 author = {Mehrmann, Volker and Poloni, Federico},
 title = {Doubling algorithms with permuted {Lagrangian} graph bases},
 journal = {SIAM Journal on Matrix Analysis and Applications},
 volume = {33}, number = {3}, year = {2012}, pages = {780--805},
 doi = {10.1137/110850773},
 url = {https://fph.altervista.org/publications/files2/MehP12a_permutedLagrangian.pdf},
 note = {verified},
 annote = {Full author-hosted published PDF opened; Theorems 3.1 and 3.4 and their proofs read. The square-root-of-two off-diagonal entry bound is not a dimension-independent operator-norm gap bound.}
}

@book{karraskreckneumannossa1973cutting,
 author = {Karras, Ulrich and Kreck, Matthias and Neumann, Walter D. and Ossa, Erich},
 title = {Cutting and Pasting of Manifolds; {SK}-Groups},
 series = {Mathematics Lecture Series}, volume = {1},
 publisher = {Publish or Perish}, year = {1973},
 url = {https://ncatlab.org/nlab/files/Karras-Kreck-Neumann-Ossa_CutNPaste.pdf},
 note = {verified},
 annote = {Complete original scan opened. Preface dates the study group to summer 1971 and a precursor lecture to December 1970. Chapter 1 definition and Corollary (1.4), p.7, read. Closed-manifold SK axioms are not identified with unspecified boundary additivity.}
}

@article{wodzicki1982spectral,
 author = {Wodzicki, Mariusz},
 title = {Spectral asymmetry and zeta functions},
 journal = {Inventiones Mathematicae}, volume = {66},
 year = {1982}, pages = {115--135},
 doi = {10.1007/BF01404760},
 url = {https://link.springer.com/article/10.1007/BF01404760},
 note = {verified},
 annote = {Publisher metadata opened: published February 1982, before both April seminar talks. Full original text was not available. Later exact statements checked in Ponge 2006; that paper notes corrigenda in Wodzicki 1984 section 1.25. No equation-level priority claim is made.}
}

@article{wodzicki1984local,
 author = {Wodzicki, Mariusz},
 title = {Local invariants of spectral asymmetry},
 journal = {Inventiones Mathematicae}, volume = {75},
 year = {1984}, pages = {143--177},
 doi = {10.1007/BF01403095},
 url = {https://link.springer.com/article/10.1007/BF01403095},
 note = {verified},
 annote = {Publisher metadata opened: February 1984 publication. Full text not read. Ponge Theorem 4.3 explicitly attributes zero-value cut independence to section 1.24; Remarks 4.4--4.5 identify local limitations and the projection-residue theorem.}
}

@article{ponge2006spectral,
 author = {Ponge, Rapha{\"e}l},
 title = {Spectral asymmetry, zeta functions, and the noncommutative residue},
 journal = {International Journal of Mathematics},
 volume = {17}, number = {9}, year = {2006}, pages = {1065--1090},
 url = {https://arxiv.org/abs/math/0310102}, note = {verified},
 annote = {Full version 8, dated 25 January 2006, opened. First arXiv circulation October 2003; journal metadata corroborated on the author's bibliography. Section 4, Theorems 4.2--4.3 and Remarks 4.4--4.5 read. Theorem 6.3 is not used; its later corrections are noted in Loya--Moroianu--Ponge.}
}

@article{loyamoroianu2012singularities,
 author = {Loya, Paul and Moroianu, Sergiu},
 title = {Singularities of the eta function of first-order differential operators},
 journal = {Analele Stiintifice ale Universitatii Ovidius Constanta, Seria Matematica},
 volume = {20}, number = {2}, year = {2012}, pages = {59--70},
 doi = {10.2478/v10309-012-0040-5},
 url = {https://reference-global.com/download/article/10.2478/v10309-012-0040-5.pdf},
 note = {verified},
 annote = {Full primary paper opened. Section 4, pp.67--68, explicitly discusses negative poles and their generic occurrence for Dirac-type operators in odd dimensions. Received August 2011, accepted February 2012. Used to check the notebook's blanket cut-independence assertion, not to equate absolute-zeta poles with cut-zeta poles.}
}

@article{epstein1975natural,
 author = {Epstein, David B. A.}, title = {Natural tensors on {Riemannian} manifolds},
 journal = {Journal of Differential Geometry}, volume = {10}, number = {4},
 year = {1975}, pages = {631--645}, doi = {10.4310/jdg/1214432677},
 url = {https://doi.org/10.4310/jdg/1214432677}, note = {unverified},
 annote = {Original publisher/DOI and Project Euclid routes failed to open. Identity and page range corroborated in the opened primary Fegan--Steer bibliography. No original theorem claimed read.}
}

@article{stredder1975natural,
 author = {Stredder, Peter},
 title = {Natural differential operators on {Riemannian} manifolds and representations of the orthogonal and special orthogonal groups},
 journal = {Journal of Differential Geometry}, volume = {10}, number = {4},
 year = {1975}, pages = {647--660}, doi = {10.4310/jdg/1214432674},
 url = {https://doi.org/10.4310/jdg/1214432674}, note = {unverified},
 annote = {Original publisher/DOI and Project Euclid routes failed to open. Identity and page range corroborated in the opened primary Fegan--Steer bibliography. No original theorem claimed read.}
}

@article{fegansteer2005second,
 author = {Fegan, H. D. and Steer, B.},
 title = {Second order operators on a compact {Lie} group},
 journal = {Canadian Journal of Mathematics}, volume = {57}, number = {1},
 year = {2005}, pages = {99--113}, doi = {10.4153/CJM-2005-005-7},
 url = {https://www.cambridge.org/core/services/aop-cambridge-core/content/view/AAEFC8A04CB805974A263F05C6F3EB87/S0008414X00017430a.pdf/div-class-title-second-order-operators-on-a-compact-lie-group-div.pdf},
 note = {verified},
 annote = {Full publisher PDF opened. References 3 and 7 independently identify Epstein and Stredder. Used only as bibliographic corroboration for those notebook pointers.}
}
''')
(root/'references.bib').write_text('\n\n'.join(parts)+'\n')
print('Root bibliography written: reused',len(reused),'keys; added',len(re.findall(r'(?m)^@',parts[-1])),'entries.')
