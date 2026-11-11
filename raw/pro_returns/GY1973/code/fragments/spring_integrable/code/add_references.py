from pathlib import Path
p=Path(__file__).resolve().parent/'make_references.py'
s=p.read_text()
new=r'''
@article{lax1968integrals,
 author={Lax, Peter D.}, title={Integrals of nonlinear equations of evolution and solitary waves},
 journal={Communications on Pure and Applied Mathematics}, year={1968}, volume={21}, number={5}, pages={467--490},
 doi={10.1002/cpa.3160210503}, url={https://www.mathnet.ru/eng/mat529}, note={verified},
 annote={Primary Math-Net metadata and complete Russian translation, Matematika13(5),1969,128--150, opened. One-soliton derivation and section2 two-wave discussion read; older normalization is explicitly converted.}
}
@article{miura1968transformation,
 author={Miura, Robert M.}, title={{Korteweg--de Vries} equation and generalizations. {I}. A remarkable explicit nonlinear transformation},
 journal={Journal of Mathematical Physics}, year={1968}, volume={9}, number={8}, pages={1202--1204},
 doi={10.1063/1.1664700}, url={https://pubs.aip.org/aip/jmp/article-pdf/9/8/1202/19287336/1202_1_online.pdf}, note={unverified},
 annote={Historical reference located through bibliographies and catalogue metadata. Direct primary DOI and AIP PDF opening failed. No claim to have read the paper; the transformation identity in this chapter is derived and independently checked algebraically.}
}
@misc{bonnemaindoyonel2022hydrodynamics,
 author={Bonnemain, Thibault and Doyon, Benjamin and El, Gennady A.},
 title={Generalized hydrodynamics of the {KdV} soliton gas},
 year={2022}, howpublished={arXiv:2203.08551}, doi={10.1088/1751-8121/ac8253},
 url={https://arxiv.org/abs/2203.08551}, note={verified},
 annote={Primary author preprint full text read, equations2.3--2.5 for one-soliton normalization and pairwise phase shifts. First posted16March2022; version2 dated21July2022. Cited only as a precise modern restatement of the classical collision shift, not as its origin.}
}
@article{colindeverdiere1973geodesicsii,
 author={Colin de Verdi{\`e}re, Yves},
 title={Spectre du laplacien et longueurs des g{\'e}od{\'e}siques p{\'e}riodiques. {II}},
 journal={Compositio Mathematica}, year={1973}, volume={27}, number={2}, pages={159--184},
 url={https://www.numdam.org/item/CM_1973__27_2_159_0/}, note={verified},
 annote={Primary Numdam metadata and full PDF opened; introduction and scope of the complex-time periodic-geodesic expansion read. This is a closed-manifold result, not an exact match for the notebook's billiard boundary problem.}
}
@article{duistermaathormander1972fourierii,
 author={Duistermaat, J. J. and H{\"o}rmander, Lars},
 title={Fourier integral operators. {II}}, journal={Acta Mathematica},
 year={1972}, volume={128}, pages={183--269}, doi={10.1007/BF02392165},
 url={https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6131-11511_2006_Article_BF02392165.pdf},
 note={verified}, annote={Primary full article opened; Theorem6.1.1 and proof, pp.196--201, read. Real-principal bicharacteristic propagation predates the seminar.}
}
@article{shnirelman1975multiplicity,
 author={Shnirel'man, A. I.}, title={The asymptotic multiplicity of the spectrum of the {Laplace} operator},
 journal={Uspekhi Matematicheskikh Nauk}, year={1975}, volume={30}, number={4(184)}, pages={265--266},
 url={https://www.mathnet.ru/eng/rm4279}, note={verified},
 annote={Both primary Russian pages read via getFT with option_lang=rus. Received by the Moscow Mathematical Society7May1974. Theorem explicitly quantifies every k greater than1 and every N for the square root of the Laplacian on a smooth sufficiently near-flat two-torus; Lemmas1--3 sketch the proof. It explicitly distinguishes Lazutkin's positive-density subsequence result.}
}
@article{balianbloch1972oscillations,
 author={Balian, Roger and Bloch, Claude},
 title={Distribution of eigenfrequencies for the wave equation in a finite domain: {III}. Eigenfrequency density oscillations},
 journal={Annals of Physics}, year={1972}, volume={69}, number={1}, pages={76--160},
 doi={10.1016/0003-4916(72)90006-1},
 url={https://www.sciencedirect.com/science/article/pii/0003491672900061}, note={unverified},
 annote={Primary publisher search result supplied metadata and abstract, including numerical sphere comparison and stationary reflected paths. Direct opening returned403; full theorem and formulas not read. This is a precise thematic lead, not a verified exact infinite-series formula.}
}
'''
if '@article{lax1968integrals,' not in s:
 s=s.replace("\n'''\n(P/'references.bib')",new+"\n'''\n(P/'references.bib')")
s=s.replace('Primary Math-Net metadata and abstract read. Received 2 June 1975. Finite-zone isospectral Jacobians are explicitly stated in the abstract; scope not generalized to arbitrary periodic potentials.','Primary Math-Net metadata and full Russian PDF opened. Chapter2 section3 pp.84--87 read: sheet-labelled gap divisor, trace formula2.3.11, Dubrovin equations2.3.12, and stationary converse statement3. Received2June1975. Scope not generalized to arbitrary periodic potentials.')
p.write_text(s)
