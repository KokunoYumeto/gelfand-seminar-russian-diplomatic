from pathlib import Path
import re,json
P=Path(__file__).resolve().parent
s=(P/'references.bib').read_text()
cum=(P.parents[1]/'references_cumulative.bib').read_text()
def entry(text,key):
    m=re.search(r'@\w+\{'+re.escape(key)+r'\s*,',text)
    if not m:raise KeyError(key)
    start=m.start();i=text.index('{',start);depth=0
    for j in range(i,len(text)):
        if text[j]=='{' and (j==0 or text[j-1]!='\\'):depth+=1
        if text[j]=='}' and (j==0 or text[j-1]!='\\'):
            depth-=1
            if not depth:return text[start:j+1]
    raise ValueError(key)
for key in ['gelfandponomarev1971quadruples','coleman1975equivalence','krichever1976zakharov','krichever1977methods']:
    if not re.search(r'@\w+\{'+key+r',',s):s+='\n\n'+entry(cum,key)+'\n'
new=r'''
@article{atiyahhitchinsinger1977deformations,
 author={Atiyah, Michael F. and Hitchin, Nigel J. and Singer, Isadore M.},
 title={Deformations of instantons},
 journal={Proceedings of the National Academy of Sciences}, year={1977}, volume={74}, number={7}, pages={2662--2663},
 doi={10.1073/pnas.74.7.2662}, url={https://pmc.ncbi.nlm.nih.gov/articles/PMC431234/}, note={verified},
 annote={Both primary scanned pages read, including the theorem, deformation-complex proof and charge-one paragraph. Contributed 20 April 1977; published July 1977.}
}
@article{atiyahward1977instantons,
 author={Atiyah, Michael F. and Ward, Richard S.}, title={Instantons and algebraic geometry},
 journal={Communications in Mathematical Physics}, year={1977}, volume={55}, number={2}, pages={117--124},
 doi={10.1007/BF01626514}, url={https://link.springer.com/article/10.1007/BF01626514}, note={verified},
 annote={Publisher abstract and metadata opened; full paper not read. Received 31 May 1977; published June 1977.}
}
@article{uhlenbeck1982removable,
 author={Uhlenbeck, Karen K.}, title={Removable singularities in {Yang--Mills} fields},
 journal={Communications in Mathematical Physics}, year={1982}, volume={83}, number={1}, pages={11--29},
 doi={10.1007/BF01947068}, url={https://link.springer.com/article/10.1007/BF01947068}, note={verified},
 annote={Publisher abstract and metadata read, including the finite-energy removal statement. Full paper not accessed. Received 25 March 1981; published February 1982.}
}
@article{dayapremawaldron2026parabolic,
 author={Dayaprema, Anuk and Waldron, Alex}, title={Parabolic Gap Theorems for the {Yang--Mills} Energy},
 journal={Mathematical Physics, Analysis and Geometry}, year={2026}, volume={29}, number={12},
 doi={10.1007/s11040-026-09549-z}, url={https://link.springer.com/article/10.1007/s11040-026-09549-z}, note={verified},
 annote={Open-access full article read at Theorems 1.1--1.2 and the connectedness proof in section 3.3. Published 2 March 2026. Article 12, not an issue number.}
}
@article{drinfeldmanin1978selfdual,
 author={Drinfeld, Vladimir G. and Manin, Yuri I.}, title={Self-dual {Yang--Mills} fields over a sphere},
 journal={Functional Analysis and Its Applications}, year={1978}, volume={12}, number={2}, pages={140--142},
 doi={10.1007/BF01076262}, url={https://www.mathnet.ru/eng/faa1991}, note={verified},
 annote={Full primary Russian text, pp.78--79, read. Theorem in section 4 and explicit Gram-matrix construction in section 6. Received 27 November 1977.}
}
@article{drinfeldmanin1979instantons,
 author={Drinfeld, Vladimir G. and Manin, Yuri I.}, title={Instantons and bundles on {$\mathbb{CP}^3$}},
 journal={Functional Analysis and Its Applications}, year={1979}, volume={13}, number={2}, pages={124--134},
 doi={10.1007/BF01077244}, url={https://www.mathnet.ru/eng/faa1899}, note={verified},
 annote={Full primary Russian PDF opened; admissibility definitions, Theorem 2.1 and its proof, and section 3 read. Received 26 May 1978.}
}
@inproceedings{narasimhan1962universal,
 author={Narasimhan, Mudumbai S.}, title={Existence of universal connections},
 booktitle={General Topology and its Relations to Modern Analysis and Algebra: Proceedings of the Symposium held in Prague in September 1961},
 publisher={Academia}, address={Prague}, year={1962}, pages={286},
 url={https://dmlcz-proxy.ics.muni.cz/bitstream/handle/10338.dmlcz/700905/Toposym_01-1961-1_68.pdf}, note={verified},
 annote={Primary one-page author announcement read in full. Joint work with Ramanan is explicitly acknowledged.}
}
@article{takhtajanfaddeev1974nonlinear,
 author={Takhtadzhyan, Leon A. and Faddeev, Ludvig D.}, title={Essentially nonlinear one-dimensional model of classical field theory},
 journal={Theoretical and Mathematical Physics}, year={1974}, volume={21}, number={2}, pages={1046--1057},
 doi={10.1007/BF01035551}, url={https://www.mathnet.ru/eng/tmf3879}, note={verified},
 annote={Full primary Russian PDF opened; Hamiltonian definitions, scattering-data assumptions and section 4 kink and breather masses read. Received 31 May 1974; Russian issue November 1974.}
}
@article{korepinfaddeev1975quantization,
 author={Korepin, Vladimir E. and Faddeev, Ludvig D.}, title={Quantization of solitons},
 journal={Theoretical and Mathematical Physics}, year={1975}, volume={25}, number={2}, pages={1039--1049},
 doi={10.1007/BF01028946}, url={https://www.mathnet.ru/eng/tmf4060}, note={verified},
 annote={Primary Russian article opened and sections 1--5 read at the cited equations: zero-mode removal, one-loop mass, renormalization, phase and level condition. Received 2 April 1975; Russian issue November 1975.}
}
@article{faddeevkorepin1978quantum,
 author={Faddeev, Ludvig D. and Korepin, Vladimir E.}, title={Quantum theory of solitons},
 journal={Physics Reports}, year={1978}, volume={42}, number={1}, pages={1--87},
 doi={10.1016/0370-1573(78)90058-3}, url={https://researchconnect.stonybrook.edu/en/publications/quantum-theory-of-solitons/}, note={verified},
 annote={Primary institutional metadata opened. Original article reproduced publicly on Scribd was also opened and introduction and section 2.1 read; mathematical OCR is imperfect. Received 4 July 1977; published June 1978. Exact normalization is not certified from damaged OCR.}
}
@misc{chenliulu2020sinegordon,
 author={Chen, Gong and Liu, Jiaqi and Lu, Bingying}, title={Long-time asymptotics and stability for the sine-{Gordon} equation},
 year={2020}, eprint={2009.04260}, archivePrefix={arXiv}, primaryClass={math.AP},
 url={https://arxiv.org/abs/2009.04260}, note={verified},
 annote={First submitted 8 September 2020; version 2 dated 15 February 2022 read. Theorems 1.1 and 10.1 and Definition 2.6 verified for generic weighted Sobolev data and modified radiation.}
}
@article{sklyaninfaddeev1978quantum,
 author={Sklyanin, Evgeny K. and Faddeev, Ludvig D.}, title={Quantum-mechanical approach to the entirely integrable models of the field theory},
 journal={Doklady Akademii Nauk SSSR}, year={1978}, volume={243}, number={6}, pages={1430--1433},
 url={https://www.mathnet.ru/eng/dan42231}, note={verified},
 annote={Full primary four-page Russian article read. Explicit nonlinear-Schrodinger construction and stated incompleteness of the sine-Gordon comparison distinguished. Received 28 July 1978; published December 1978. English translation: Soviet Physics Doklady 23, 902--904.}
}
@article{zamolodchikov1977exact,
 author={Zamolodchikov, Alexander B.}, title={Exact two-particle {$S$}-matrix of quantum sine-{Gordon} solitons},
 journal={Communications in Mathematical Physics}, year={1977}, volume={55}, number={2}, pages={183--186},
 doi={10.1007/BF01626520}, url={https://link.springer.com/article/10.1007/BF01626520}, note={verified},
 annote={Publisher abstract and metadata opened; full CMP article not read. Received 4 January 1977; published June 1977. Separate primary JETP Letters article read for formulas.}
}
@article{zamolodchikov1977jetp,
 author={Zamolodchikov, Alexander B.}, title={Exact two-particle {$S$} matrix of quantum solitons of the sine-{Gordon} model},
 journal={JETP Letters}, year={1977}, volume={25}, number={10}, pages={468--471},
 url={https://users.physik.fu-berlin.de/~kamecke/ps/zamolodchikov.pdf}, note={verified},
 annote={Primary university-hosted four-page PDF read. Equation 2 gives masses; equations 4--10 distinguish transmission/reflection and reflectionless couplings. Submitted 14 April 1977; published 20 May 1977.}
}
@misc{yafaev2004lectures,
 author={Yafaev, Dmitri}, title={Lectures on scattering theory}, year={2004}, eprint={math/0403213}, archivePrefix={arXiv},
 url={https://arxiv.org/abs/math/0403213}, note={verified},
 annote={Primary lecture notes opened and Theorem 2.4 with proof, wave-operator definitions and equation 2.8 read. Lectures delivered October--November 2001; posted 12 March 2004. Used for precise hypotheses, not historical priority.}
}
@article{froehlich1975quantized,
 author={Fr{\"o}hlich, J{\"u}rg}, title={Quantized ``Sine-{Gordon}'' Equation with a Nonvanishing Mass Term in Two Space-Time Dimensions},
 journal={Physical Review Letters}, year={1975}, volume={34}, number={13}, pages={833--836},
 doi={10.1103/PhysRevLett.34.833}, url={https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.34.833}, note={verified},
 annote={Publisher abstract and metadata read. Received 11 February 1975; published 31 March 1975. Full article and exact coupling hypotheses not verified from the partially rendered abstract.}
}
@article{pohlmeyer1976integrable,
 author={Pohlmeyer, Klaus}, title={Integrable {Hamiltonian} systems and interactions through quadratic constraints},
 journal={Communications in Mathematical Physics}, year={1976}, volume={46}, pages={207--221},
 doi={10.1007/BF01609119}, url={https://link.springer.com/article/10.1007/BF01609119}, note={verified},
 annote={Publisher abstract and metadata opened. Received 28 August 1975; published October 1976. The full paper was not read; sphere-model attribution is independently explicit in Zakharov--Mikhailov.}
}
@article{zakharovmikhailov1978relativistic,
 author={Zakharov, Vladimir E. and Mikhailov, Alexander V.},
 title={Relativistically invariant two-dimensional models of field theory which are integrable by means of the inverse scattering problem method},
 journal={Soviet Physics JETP}, year={1978}, volume={47}, number={6}, pages={1017--1027},
 url={https://zakharov75.itp.ac.ru/static/local/zve75/zakharov/1978/1978-03-e_047_06_1017.pdf}, note={verified},
 annote={Full primary author-archive PDF opened; introduction and sections 1--3 read, with section 6 scope checked. Submitted 4 January 1978; Russian publication June 1978; English PDF copyright 1979.}
}
@article{zamolodchikovzamolodchikov1978on,
 author={Zamolodchikov, Alexander B. and Zamolodchikov, Alexey B.}, title={Relativistic factorized {$S$}-matrix in two dimensions having {$O(N)$} isotopic symmetry},
 journal={Nuclear Physics B}, year={1978}, volume={133}, number={3}, pages={525--535},
 doi={10.1016/0550-3213(78)90239-0}, url={https://kamecke.userpage.physik.fu-berlin.de/ps/zam3.pdf}, note={verified},
 annote={Primary PDF introduction and sections 2--3 read; CDD ambiguity and the authors' limited claim for sigma-model identification retained. Received 22 August 1977, revised 14 November 1977, published 27 February 1978.}
}
'''
for m in re.finditer(r'@\w+\{([^,]+),',new):
    if not re.search(r'@\w+\{'+re.escape(m.group(1))+r',',s):s+='\n'+entry(new,m.group(1))+'\n'
(P/'references.bib').write_text(s)
required={k for i in json.loads((P/'items.json').read_text()) for k in i['refs']}
required|={k for i in json.loads((P/'problems.json').read_text()) for k in i['refs']}
available=set(re.findall(r'@\w+\{([^,]+),',s))
print('Bib entries:',len(available),'required:',len(required),'missing:',sorted(required-available))
