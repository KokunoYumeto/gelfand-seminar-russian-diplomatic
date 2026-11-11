from pathlib import Path
import re

p=Path(__file__).resolve().parent
text=(p.parents[1]/'source_inputs/references_cumulative.bib').read_text()
keys=['malgrange1966ideals','boardman1967singularities','arnold1968singularities',
      'mather1969stability','mather1970topological','mather1971nice']
entries=[]
for key in keys:
    start=re.search(r'@\w+\{'+re.escape(key)+r',',text).start()
    opening=text.index('{',start)
    depth=0
    for end in range(opening,len(text)):
        if text[end]=='{':depth+=1
        if text[end]=='}':depth-=1
        if depth==0:break
    entry=text[start:end+1]
    if key=='arnold1968singularities':
        entry=re.sub(r'  annote = \{[^\n]*\}',r'  annote = {English full text opened and relevant results read: section 1, Examples 3--6 and Theorems 1--4; section 2, Examples 4 and 6; section 3, intrinsic derivatives, pencils, and moduli; section 4, local algebras and preparation. Based on 1966 lectures; received 4 September 1967.}',entry)
    if key=='malgrange1966ideals':
        entry=re.sub(r'  annote = \{[^\n]*\}',r'  annote = {Full text opened; preface and chapter context checked. The preface identifies lectures delivered in 1964 and is dated July 1965. Chapters III and V provide the analytic and smooth preparation context; the exact finite-module formulation used here was read in Arnold 1968, section 4, Theorems 1--2.}',entry)
    entries.append(entry)

entries.append(r'''@article{mather1969algebras,
  author = {Mather, John N.},
  title = {Stability of {C}$^\infty$ mappings, {IV}. Classification of stable germs by {R}-algebras},
  journal = {Publications Math\'ematiques de l'IH\'ES},
  volume = {37},
  pages = {223--248},
  year = {1969},
  doi = {10.1007/BF02684889},
  url = {https://www.numdam.org/item/PMIHES_1969__37__223_0.pdf},
  note = {verified},
  annote = {Primary full text opened. Introduction and Theorems A and B, pp.223--225, read; Proposition 1.6 and the closing proof checked. The paper uses stable as shorthand for infinitesimally stable and announces a later equivalence proof. Received 1 June 1968; journal volume dated 1969; scanned printing colophon dated 1970.}
}''')
entries.append(r'''@article{thom1956singularites,
  author = {Thom, Ren\'e},
  title = {Les singularit\'es des applications diff\'erentiables},
  journal = {Annales de l'Institut Fourier},
  volume = {6},
  year = {1956},
  pages = {43--87},
  doi = {10.5802/aif.60},
  url = {https://www.numdam.org/item/AIF_1956__6__43_0.pdf},
  note = {verified},
  annote = {Primary full text opened; Part I and its generic-rank and transversality statements checked. This verifies pre-lecture provenance, not every later generalization attributed to Thom.}
}''')
entries.append(r'''@article{whitney1955plane,
  author = {Whitney, Hassler},
  title = {On singularities of mappings of {Euclidean} spaces, {I}: Mappings of the plane into the plane},
  journal = {Annals of Mathematics},
  volume = {62},
  number = {3},
  year = {1955},
  pages = {374--410},
  doi = {10.2307/1970070},
  url = {https://celebratio.org/Whitney_H/article/219/},
  note = {verified},
  annote = {Publication metadata and abstract checked in the author's curated bibliography, entry 102. The original JSTOR endpoint did not expose the article. The mathematical normal forms were read in Arnold 1968, section 1; the original proof is not claimed as inspected.}
}''')
entries.append(r'''@article{mather1972stratifications,
  author = {Mather, John N.},
  title = {Stratifications and mappings},
  journal = {Uspekhi Matematicheskikh Nauk},
  volume = {27},
  number = {5(167)},
  year = {1972},
  pages = {85--118},
  url = {https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&option_lang=eng&paperid=5110&what=fullt},
  note = {verified},
  annote = {Russian translation by A. N. Varchenko of the Harvard 1971 preprint, as stated on p.85. Primary full text opened. Introduction, especially the finite generic topological-classification theorem on p.88, read. The author calls the proof an outline; it is not presented here as exact verification of the 1966 infinite-codimension partition announcement.}
}''')
(p/'references.bib').write_text('\n\n'.join(entries)+'\n')
