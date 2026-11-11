from pathlib import Path
import re
p=Path(__file__).resolve().parents[1]
s=(p.parent/'references_cumulative.bib').read_text()
out=[]
for k in ('hormander1971fourier','duistermaathormander1972fourierii'):
 m=re.search(r'@\w+\{'+k+r',.*?(?=\n@|\Z)',s,re.S)
 assert m,k
 out.append(m.group().strip())
out.append(r"""
@article{dobrushin1968conditional,
  author = {Dobrushin, R. L.},
  title = {The description of a random field by means of conditional probabilities and conditions of its regularity},
  journal = {Theory of Probability and Its Applications},
  year = {1968}, volume = {13}, number = {2}, pages = {197--224},
  doi = {10.1137/1113026},
  url = {https://www.mathnet.ru/eng/tvp839},
  note = {verified},
  annote = {Math-Net metadata and Russian full text opened; Section 1 and Theorems 1--2 read. Received 20 April 1967. Russian original pp.201--229.}
}
@article{dobrushin1968uniqueness,
  author = {Dobrushin, R. L.},
  title = {The problem of uniqueness of a {Gibbsian} random field and the problem of phase transitions},
  journal = {Functional Analysis and Its Applications},
  year = {1968}, volume = {2}, number = {4}, pages = {302--312},
  doi = {10.1007/BF01075682},
  url = {https://www.mathnet.ru/eng/faa2795},
  note = {verified},
  annote = {Publisher-platform metadata checked; full theorem text not read for this entry. Received 23 February 1968. Russian original pp.44--57.}
}
@article{ruelle1970superstable,
  author = {Ruelle, David},
  title = {Superstable interactions in classical statistical mechanics},
  journal = {Communications in Mathematical Physics},
  year = {1970}, volume = {18}, pages = {127--159},
  url = {https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B28%5D.pdf},
  note = {verified},
  annote = {Author-hosted full text opened; Section 5 and Theorems 5.5--5.7 read. Received 11 March 1970.}
}
@article{pirogovsinai1975phase,
  author = {Pirogov, S. A. and Sinai, Ya. G.},
  title = {Phase diagrams of classical lattice systems},
  journal = {Theoretical and Mathematical Physics},
  year = {1975}, volume = {25}, number = {3}, pages = {1185--1192},
  doi = {10.1007/BF01040127},
  url = {https://www.mathnet.ru/eng/tmf4080},
  note = {verified},
  annote = {Russian full text opened; Definitions 1.2--1.4 and Theorem 1 read. Received 21 April 1975. Russian original TMF 25(3), 358--369.}
}
@article{pirogovsinai1976phase,
  author = {Pirogov, S. A. and Sinai, Ya. G.},
  title = {Phase diagrams of classical lattice systems: Continuation},
  journal = {Theoretical and Mathematical Physics},
  year = {1976}, volume = {26}, number = {1}, pages = {39--49},
  doi = {10.1007/BF01038255},
  url = {https://www.mathnet.ru/eng/tmf3169},
  note = {verified},
  annote = {Russian full text opened; continuation and contour-model scope checked; not every proof read. Received 21 April 1975. Russian original TMF 26(1), 61--76.}
}
@article{rokhlin1949measure,
  author = {Rokhlin, V. A.},
  title = {On the fundamental ideas of measure theory},
  journal = {Matematicheskii Sbornik (N.S.)},
  year = {1949}, volume = {25(67)}, number = {1}, pages = {107--150},
  url = {https://www.mathnet.ru/eng/sm5995},
  note = {verified},
  annote = {Russian full text and metadata opened; Section 3.1, pp.125--129, canonical conditional measures, essential uniqueness, measurable partitions, and countable observables read. Received 15 July 1947.}
}
@article{minlos1959generalized,
  author = {Minlos, R. A.},
  title = {Generalized random processes and their extension in measure},
  journal = {Trudy Moskovskogo Matematicheskogo Obshchestva},
  year = {1959}, volume = {8}, pages = {497--518},
  url = {https://www.mathnet.ru/eng/mmo94},
  note = {verified},
  annote = {Russian full text opened; introduction and Section 1 definitions read. Received 7 April 1958; first-page note reports the main results at a meeting on 11 April 1958.}
}
@misc{loustausanders2017bilagrangian,
  author = {Loustau, Brice and Sanders, Andrew},
  title = {Bi-{Lagrangian} structures and {Teichm{\"u}ller} theory},
  year = {2017},
  eprint = {1708.09145}, archivePrefix = {arXiv}, primaryClass = {math.DG},
  url = {https://arxiv.org/abs/1708.09145},
  note = {verified},
  annote = {ArXiv metadata and author-hosted full text opened; Proposition 1.9 and Theorems 1.10 and 1.13 read. First posted 30 August 2017; version 4 dated 23 August 2020. The introduction attributes the affine-leaf result to Weinstein (1971); that original was not directly verified.}
}
@article{heifetz1985padic,
  author = {Heifetz, D. B.},
  title = {p-adic oscillatory integrals and wave front sets},
  journal = {Pacific Journal of Mathematics},
  year = {1985}, volume = {116}, number = {2}, pages = {285--305},
  url = {https://msp.org/pjm/1985/116-2/pjm-v116-n2-p06-s.pdf},
  note = {verified},
  annote = {Publisher full text opened; Sections 1--2, including Proposition 1.2 and the non-Archimedean wavefront construction, read. This is only a thematic match to the unspecified notebook FIO request.}
}
@article{bernstein1971modules,
  author = {Bernstein, I. N.},
  title = {Modules over a ring of differential operators: A study of the fundamental solutions of equations with constant coefficients},
  journal = {Functional Analysis and Its Applications},
  year = {1971}, volume = {5}, number = {2}, pages = {89--101},
  doi = {10.1007/BF01076413},
  url = {https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/bernstein-mod-dif-FAN.pdf},
  note = {verified},
  annote = {Author-hosted full text opened; Section 1, Definition 1.6, and Section 3 filtration/dimension formalism read. This supplies the framework, not the exact 1972 dimension-inequality locator.}
}
@article{bernstein1972continuation,
  author = {Bernstein, I. N.},
  title = {The analytic continuation of generalized functions with respect to a parameter},
  journal = {Functional Analysis and Its Applications},
  year = {1972}, volume = {6}, number = {4}, pages = {273--285},
  doi = {10.1007/BF01077645},
  url = {https://www.mathnet.ru/eng/faa2532},
  note = {verified},
  annote = {Math-Net metadata and author-hosted English full text opened; Theorem 1.3 and its proof in Section 5 read. Received 21 June 1972. Russian original pp.26--40.}
}
@misc{mustata2023dmodules,
  author = {Musta{\c{t}}{\u{a}}, Mircea},
  title = {D-modules and singularities},
  year = {2023},
  howpublished = {Lecture notes, Math 732, University of Michigan, Winter 2023},
  url = {https://public.websites.umich.edu/~mmustata/DmodulesNotes.pdf},
  note = {verified},
  annote = {Author-hosted notes opened; Theorem 3.38 on order characteristic varieties and Theorem 4.9 on the Bernstein filtration read; Section 6.3 proof route inspected.}
}
@article{polyakov1974particle,
  author = {Polyakov, A. M.},
  title = {Particle spectrum in quantum field theory},
  journal = {JETP Letters},
  year = {1974}, volume = {20}, number = {6}, pages = {194--195},
  url = {https://www.itp.ac.ru/en/publications/1974/},
  note = {verified},
  annote = {Author-institution publication list, item 58, checked. Journal full text was not accessible. Russian version Pisma ZhETF 20, 430--433. The notebook gives only a thematic match, not a specified model or theorem.}
}
@article{griffithsking1973nevanlinna,
  author = {Griffiths, Phillip A. and King, James},
  title = {Nevanlinna theory and holomorphic mappings between algebraic varieties},
  journal = {Acta Mathematica},
  year = {1973}, volume = {130}, pages = {145--220},
  url = {https://publications.ias.edu/sites/default/files/nevanlinna.pdf},
  note = {verified},
  annote = {IAS metadata and full text opened; Propositions 1.1, 1.14--1.15 and 5.11, equation 5.12, and the surrounding growth discussion read.}
}
@article{griffiths1971canonical,
  author = {Griffiths, Phillip A.},
  title = {Holomorphic mappings into canonical algebraic varieties},
  journal = {Annals of Mathematics},
  year = {1971}, volume = {93}, number = {3}, pages = {439--458},
  url = {https://publications.ias.edu/sites/default/files/holomorphicmapping71.pdf},
  note = {verified},
  annote = {Author-institution full text opened; Section 2, Lemma 2.3 and Proposition 2.7, including the maximum-principle proof, read. Received 27 March 1970; issue May 1971.}
}
@article{lelong1957integration,
  author = {Lelong, Pierre},
  title = {Int{\'e}gration sur un ensemble analytique complexe},
  journal = {Bulletin de la Soci{\'e}t{\'e} Math{\'e}matique de France},
  year = {1957}, volume = {85}, pages = {239--262},
  doi = {10.24033/bsmf.1488},
  url = {https://www.numdam.org/article/BSMF_1957__85__239_0.pdf},
  note = {verified},
  annote = {Numdam metadata and full text opened; introduction and Theorems 7--8 on integration-current extension and additivity read. The precise notebook attribution to 1953 remains unverified.}
}
@article{bohrlefeuvrepaternain2024invariant,
  author = {Bohr, Jan and Lefeuvre, Thibault and Paternain, Gabriel P.},
  title = {Invariant distributions and the transport twistor space of closed surfaces},
  journal = {Journal of the London Mathematical Society},
  year = {2024}, volume = {109}, number = {5}, pages = {e12894},
  doi = {10.1112/jlms.12894},
  url = {https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.12894},
  note = {verified},
  annote = {Publisher full text opened; Appendix A, equation A.4 and the following one-sided wavefront calculation, read as an independent Fourier-sign check. First published 16 April 2024. No new historical priority claim is inferred.}
}
""".strip())
(p/'late_references.bib').write_text('\n\n'.join(out)+'\n')
print('Wrote',len(re.findall(r'(?m)^@','\n'.join(out))),'references')
with (p/'late_references.bib').open('a') as f:
 f.write(r"""
@article{cowengriffiths1976curves,
  author = {Cowen, Michael and Griffiths, Phillip},
  title = {Holomorphic curves and metrics of negative curvature},
  journal = {Journal d'Analyse Math{\'e}matique},
  year = {1976}, volume = {29}, pages = {93--153},
  url = {https://publications.ias.edu/sites/default/files/holomorphiccurvesandmetrics.pdf},
  note = {verified},
  annote = {IAS metadata and full text opened; introduction pp.93--95 read, including its account of H. and J. Weyl. This supports a bibliographical interpretation of the closing note, not an exact eigenfunction theorem.}
}
@article{rozikovkhakimov2013padic,
  author = {Rozikov, U. A. and Khakimov, O. N.},
  title = {p-Adic {Gibbs} measures and {Markov} random fields on countable graphs},
  journal = {Theoretical and Mathematical Physics},
  year = {2013}, volume = {175}, number = {1}, pages = {518--525},
  doi = {10.1007/s11232-013-0042-0},
  url = {https://www.mathnet.ru/eng/tmf8428},
  note = {verified},
  annote = {Publisher-platform abstract and metadata opened; full theorem text not read. Received 16 October 2012. This concerns p-adic probability-valued graph models and is only a thematic lead for the unspecified 1975 question.}
}
""")
print('Final bibliography entries:',len(re.findall(r'(?m)^@',(p/'late_references.bib').read_text())))
