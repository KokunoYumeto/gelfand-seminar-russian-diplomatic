"""Create the batch bibliography, retaining established cumulative keys."""
from pathlib import Path
import re
P=Path(__file__).parent
root=P.parent.parent
entries={}
def entry(key,typ="article",**fields):
    entries[key]="@"+typ+"{"+key+",\n"+",\n".join(
        "  "+k+" = {"+str(v)+"}" for k,v in fields.items())+"\n}\n"
def reuse(key,annote):
    source=(root/"references_cumulative.bib").read_text()
    m=re.search(r"(?ms)^@\w+\{"+re.escape(key)+r",.*?^\}",source)
    assert m,key
    text=m.group(0)
    # All cumulative entries selected here have an annote field occupying one line.
    text=re.sub(r"(?m)^\s*annote\s*=\s*\{.*\}(,?)\s*$",
                lambda m:"  annote = {"+annote+"}"+m.group(1),text)
    entries[key]=text+"\n"

reuse("berezinleites1975supermanifolds",
      "Primary Math-Net metadata opened on 2026-11-10; volume, pages and received date 24 March 1975 checked. This batch did not reread the full original paper; the Berezinian comparison is indirect and independently checked algebraically.")
reuse("bernsteingelfandgelfand1978bundles",
      "Author-hosted English original opened on 2026-11-10. Sections 2--7, Theorems 1--4, proper modules and stable equivalence inspected. Received 10 January 1978; Russian volume 1978; English translation imprint 1979. The notes' unrestricted instanton identification is stronger than the bundle theorem.")
reuse("eisenbudfloystadschreyer2003exterior",
      "Full author preprint https://arxiv.org/pdf/math/0104203 opened on 2026-11-10; checked v2 dated 8 June 2001. First joint version 20 April 2001; journal 2003. Theorems 4.1 and 6.1 and Section 5 provide Tate resolution and actual monad maps.")
reuse("gilkey1979recursion",
      "Primary Numdam metadata opened on 2026-11-10; exact title, 38(2), pages 201--240 and 1979 date checked. This batch used the author's 1984 monograph for explicit heat-coefficient formulas and did not claim a new full reading of this paper.")
reuse("woit2021euclidean",
      "Full author-institution PDF dated 11 April 2021 opened on 2026-11-10. Only classical geometry in Sections 3.1 and 3.3.2 is used: real forms, graph coordinates, determinant metric, incidence and U(2) compactification. The speculative unification proposal is not used as established physics.")
reuse("zakharovshabat1974scheme",
      "Primary Math-Net metadata opened on 2026-11-10. Received 14 March 1974; original Russian pages 43--53, translation 226--235. The broad dressing identification is metadata-level in this batch; notebook linearizations are independently checked, not represented as a full rereading of the original proof.")

entry("hawking1978foam",author="Hawking, S. W.",title="Space-time foam",
      journal="Nuclear Physics B",year=1978,volume=144,pages="349--362",
      doi="10.1016/0550-3213(78)90375-9",url="https://www.hawking.org.uk/in-print",
      note="verified",annote="Author-estate bibliography opened on 2026-11-10; exact publication identified. Metadata only. Its January 1979 report listing is not taken as first circulation of the 1978 journal article. No rigorous measure or topology-sum convergence theorem is claimed as read.")
entry("hawkingpope1978symmetry",author="Hawking, S. W. and Pope, C. N.",
      title="Symmetry breaking by instantons in supergravity",
      journal="Nuclear Physics B",year=1978,volume=146,number=2,pages="381--392",
      doi="10.1016/0550-3213(78)90073-1",url="https://www.hawking.org.uk/in-print",
      note="verified",annote="Author bibliography opened; publisher search-result abstract read on 2026-11-10. Publication 25 December 1978. Abstract restricts nonzero-mode pairing and one-loop cancellation to self-dual instanton backgrounds and discusses boundary-sensitive zero modes. Full original article not retrieved.")
entry("christensenduff1979indices",author="Christensen, S. M. and Duff, M. J.",
      title="New gravitational index theorems and super theorems",
      journal="Nuclear Physics B",year=1979,volume=154,number=2,pages="301--342",
      doi="10.1016/0550-3213(79)90516-9",
      url="https://www.sciencedirect.com/science/article/pii/0550321379905169",
      note="unverified",annote="Original URL was attempted repeatedly on 2026-11-10 and returned 403. Primary publisher abstract was available in search and read; metadata and scope are also corroborated by Duff's opened 1982 lectures. July 23 1979 publication. Exact numerical spin-index coefficients and operator normalizations were not verified from full text.")
entry("kallosh1980selfduality",author="Kallosh, R. E.",
      title="Self-duality in superspace",journal="Nuclear Physics B",year=1980,
      volume=165,number=1,pages="119--128",doi="10.1016/0550-3213(80)90309-0",
      url="https://www.sciencedirect.com/science/article/pii/0550321380903090",
      note="unverified",annote="Publisher URL attempted on 2026-11-10, inaccessible; primary search abstract read. Its self-dual superspace scope and bibliography are corroborated by Duff1982. Exact all-loop hypotheses and proof were not read. It does not justify unrestricted supergravity finiteness.")
entry("duff1982ultraviolet",typ="misc",author="Duff, M. J.",
      title="Ultraviolet divergences in extended supergravity",year=1982,
      howpublished="CERN preprint TH.3232; lectures for Supergravity '81",
      url="https://arxiv.org/pdf/1201.0386",note="verified",
      annote="Full primary text opened on 2026-11-10. Header dates CERN preprint 22 January 1982; lectures delivered at ICTP in April 1981; repository deposit January 2012 is not first circulation. Sections 2.3, 4.1 and 4.4 and historical bibliography inspected for self-dual restrictions, anomalies, boundary/gauge caveats and Kallosh's distinct 1979 letters.")
entry("aragonedeser1979hypergravity",author="Aragone, C. and Deser, S.",
      title="Consistency problems of hypergravity",journal="Physics Letters B",
      year=1979,volume=86,number=2,pages="161--163",
      doi="10.1016/0370-2693(79)90808-6",
      url="https://www.sciencedirect.com/science/article/pii/0370269379908086",
      note="unverified",annote="Original publisher URL attempted on 2026-11-10, returned 403. Primary search abstract and metadata read: published 24 September 1979, with an identified May 1979 Brandeis preprint lead. Abstract states the Weyl-curvature obstruction and self-dual exception. Full proof not read; no universal no-interaction theorem asserted.")
entry("gilkey1984invariance",typ="book",author="Gilkey, Peter B.",
      title="Invariance theory, the heat equation, and the Atiyah--Singer index theorem",
      year=1984,publisher="Publish or Perish",
      url="https://darkwing.uoregon.edu/~gilkey/dirPDF/InvarianceTheory1Ed.pdf",
      note="verified",annote="Full author PDF opened on 2026-11-10; electronic reprint 1996 of the 1984 first edition. Sections 1.5--1.7, 1.10, 2.2, 2.4, 3.1--3.4 and 4.8 consulted for elliptic/Hodge setting, heat/zeta identity, spin and characteristic-number formulas. The S4 rational example is independently computed.")
entry("baez2002octonions",author="Baez, John C.",title="The octonions",
      journal="Bulletin of the American Mathematical Society",year=2002,
      volume=39,number=2,pages="145--205",
      doi="10.1090/S0273-0979-01-00934-X",
      url="https://math.ucr.edu/home/baez/octonions/octonions.pdf",
      note="verified",annote="Full author PDF opened on 2026-11-10. Sections 2.2--2.3 and Section 4.2, Theorem 5, inspected. The compact F4 automorphism theorem is explicitly historical; no 2002 novelty is inferred. Real division versus split octonions must be distinguished.")
entry("zakharovschulman1980degenerative",author="Zakharov, V. E. and Schulman, E. I.",
      title="Degenerative dispersion laws, motion invariants and kinetic equations",
      journal="Physica D: Nonlinear Phenomena",year=1980,volume=1,number=2,pages="192--202",
      doi="10.1016/0167-2789(80)90011-1",url="https://zakharov.itp.ac.ru/pub/",
      note="verified",annote="Author publication list opened on 2026-11-10; 1980 metadata checked. Full original not read. The detailed theorem and limitations were read in the authors' 1988 paper. The October/September 1979 notebook is earlier oral circulation of the programme.")
entry("zakharovschulman1988invariants",author="Zakharov, V. E. and Schulman, E. I.",
      title="On additional motion invariants of classical Hamiltonian wave systems",
      journal="Physica D: Nonlinear Phenomena",year=1988,volume=29,number=3,pages="283--320",
      doi="10.1016/0167-2789(88)90033-4",
      url="https://zakharov.itp.ac.ru/pub/data/1988/1988-13-1988_PD_ZS.pdf",
      note="verified",annote="Full author-hosted original opened on 2026-11-10. Received 14 April 1986, revised 20 January 1987, published 1988. Sections 1--3, Theorem 3.1, equations 3.8--3.11, classification caveat near p.295, and Section 6 inspected. Distinguishes partial/complete degeneracy and quadratic-leading analytic invariants; does not prove the universal difference-curve classification.")
entry("arnold1989mechanics",typ="book",author="Arnold, V. I.",
      title="Mathematical methods of classical mechanics",edition=2,
      year=1989,publisher="Springer",series="Graduate Texts in Mathematics",volume=60,
      doi="10.1007/978-1-4757-2063-1",
      url="https://link.springer.com/book/10.1007/978-1-4757-2063-1",
      note="verified",annote="Publisher metadata and contents opened on 2026-11-10, identifying Russian original 1974 and second edition 1989. An academic-hosted complete scan was found but exceeded reader size limit. Appendix 7 context is cited at metadata level; the formal homological elimination and first-order necessary condition are independently derived.")
entry("penrose1976nonlinear",author="Penrose, Roger",
      title="Nonlinear gravitons and curved twistor theory",
      journal="General Relativity and Gravitation",year=1976,volume=7,pages="31--52",
      doi="10.1007/BF00762011",
      url="https://link.springer.com/article/10.1007/BF00762011",
      note="verified",annote="Publisher page opened on 2026-11-10; January 1976 date, title, author, volume and pages verified. Full original theorem not read; used only to qualify the blanket historical claim that no curved twistor theory existed.")
entry("sanabria2017symplectic",typ="misc",author="Sanabria Malag{\\'o}n, Camilo",
      title="An elementary proof of the symplectic spectral theorem",year=2017,
      eprint="1710.00697",archivePrefix="arXiv",
      url="https://arxiv.org/pdf/1710.00697",note="verified",
      annote="Full author preprint v1 dated 29 September 2017 opened on 2026-11-10. Theorem 1 and Corollary 11 inspected, including split-eigenvalue and perfect-field hypotheses. Introduction explicitly cites previous canonical-form results; the paper is a later exact proof, not evidence that the 1979 exercise was then open.")
entry("berezin1987superanalysis",typ="book",author="Berezin, F. A.",
      editor="Kirillov, A. A.",title="Introduction to superanalysis",
      year=1987,publisher="D. Reidel",series="Mathematical Physics and Applied Mathematics",
      volume=9,doi="10.1007/978-94-017-1963-6",
      url="https://link.springer.com/book/10.1007/978-94-017-1963-6",
      note="verified",annote="Publisher metadata and contents opened on 2026-11-10. Grassmann algebra pp.29--73 and graded linear algebra pp.90--130 identified. Full chapter not retrieved; elementary identities and the simple-spectrum lifting argument are checked directly in the companion.")
entry("gelfandponomarev1979model",author="Gel'fand, I. M. and Ponomarev, V. A.",
      title="Model algebras and representations of graphs",
      journal="Functional Analysis and Its Applications",year=1979,volume=13,number=3,
      pages="157--166",doi="10.1007/BF01077482",
      url="https://www.mathnet.ru/eng/faa1912",note="verified",
      annote="Math-Net metadata and full Russian PDF opened on 2026-11-10; received 23 March 1979; original pp.1--12. Exact volume/issue match to Gelfand's citation. No theorem identifying the notebook's incomplete all-Dynkin Grassmann prescription was verified; match remains thematic.")
entry("kapranov1984grassmann",author="Kapranov, M. M.",
      title="On the derived category of coherent sheaves on Grassmann manifolds",
      journal="Izvestiya Akademii Nauk SSSR. Seriya Matematicheskaya",
      year=1984,volume=48,number=1,pages="192--202",
      doi="10.1070/IM1985v024n01ABEH001221",
      url="https://www.mathnet.ru/eng/im1423",note="verified",
      annote="Primary Math-Net page opened on 2026-11-10. Russian original 1984; English translation Math. USSR-Izvestiya 24(1) (1985), 183--192. Received 12 January 1983. DOI is for English translation. Metadata checked; theorem content read in Kapranov1988.")
entry("kapranov1988homogeneous",author="Kapranov, M. M.",
      title="On the derived categories of coherent sheaves on some homogeneous spaces",
      journal="Inventiones Mathematicae",year=1988,volume=92,pages="479--508",
      doi="10.1007/BF01393744",
      url="https://www.math.ucdavis.edu/~egorskiy/InformalAG/f20/Kapranov.pdf",
      note="verified",annote="Full original paper opened on 2026-11-10. Section 3, Theorem 3.4 and preceding description of canonical homotopy class but noncanonical differential inspected. Complex Grassmannian derived-category model is exact for the reconstructed request, not a finite list classifying every vector bundle.")
entry("sergeichuk2000canonical",author="Sergeichuk, Vladimir V.",
      title="Canonical matrices for linear matrix problems",
      journal="Linear Algebra and its Applications",year=2000,volume=317,pages="53--102",
      doi="10.1016/S0024-3795(00)00150-6",
      url="https://arxiv.org/pdf/0709.2485",note="verified",
      annote="Full author version opened on 2026-11-10. Theorems 1.1 and 1.3 and matrix-algebra similarity framework checked independently by root; this batch also opened the original and read its setup. Reference32 records Bielefeld SFB343 preprint99-070 in1999; journal2000; arXiv deposit16September2007. Application to the finite even Grassmann matrix algebra is the companion's explicit reduction.")
entry("little1983translation",author="Little, John",
      title="Translation manifolds and the converse of Abel's theorem",
      journal="Compositio Mathematica",year=1983,volume=49,number=2,pages="147--171",
      url="https://www.numdam.org/article/CM_1983__49_2_147_0.pdf",
      note="verified",annote="Full original opened on 2026-11-10. Definitions2.1--2.2, Corollary3.5, Proposition3.7 condition(*), Theorem3.9, hyperelliptic discussion after Example4.1 and Theorem5.1 inspected. Gives precise genericity and generalized-Jacobian version; no universal smoothability theorem inferred.")
entry("albeveriohoeghkrohn1978energy",author="Albeverio, Sergio and H{\\o}egh-Krohn, Raphael",
      title="The energy representation of Sobolev-Lie groups",
      journal="Compositio Mathematica",year=1978,volume=36,number=1,pages="37--51",
      url="https://www.numdam.org/article/CM_1978__36_1_37_0.pdf",
      note="verified",annote="Full original opened on 2026-11-10. Sections2--4 inspected for Sobolev/path-group construction, Gaussian realization and Brownian relationship. The qualified preexisting construction is kept distinct from the later irreducibility theorem.")
entry("albeveriohoeghkrohntestard1981irreducibility",
      author="Albeverio, Sergio and H{\\o}egh-Krohn, Raphael and Testard, Daniel",
      title="Irreducibility and reducibility for the energy representation of the group of mappings of a Riemannian manifold into a compact semisimple Lie group",
      journal="Journal of Functional Analysis",year=1981,volume=41,number=3,pages="378--396",
      doi="10.1016/0022-1236(81)90082-3",
      url="https://www.sciencedirect.com/science/article/pii/0022123681900823",
      note="unverified",annote="Publisher endpoint attempted on 2026-11-10, inaccessible; primary search abstract read. Full result and restrictions independently corroborated in opened Wallach1987 Introduction and Theorem6.2. Conference footnote points to November1979 and September1980; the October1979 notebook precedes those. Original full proof not read.")
entry("wallach1987gauge",author="Wallach, Nolan R.",
      title="On the irreducibility and inequivalence of unitary representations of gauge groups",
      journal="Compositio Mathematica",year=1987,volume=64,number=1,pages="3--29",
      url="https://www.numdam.org/article/CM_1987__64_1_3_0.pdf",
      note="verified",annote="Full original opened on 2026-11-10; Introduction and Theorem6.2 with proof inspected. Theorem page22 checked visually to verify root bound sqrt(8 pi |rho(x)|). Received19December1986, accepted2March1987; introductory lecture provenance Fall1986. General dimension>=3 result and parameter-restricted dimension2 result are distinguished.")
entry("shimada2005irreducibility",author="Shimada, Yoshihito",
      title="On irreducibility of the energy representation of the gauge group and the white noise distribution theory",
      journal="Infinite Dimensional Analysis, Quantum Probability and Related Topics",
      year=2005,volume=8,number=2,pages="153--177",
      doi="10.1142/S0219025705001913",
      url="https://arxiv.org/pdf/math-ph/0404042",note="verified",
      annote="Full primary preprint opened on 2026-11-10, v2 dated1February2005; first version18April2004. The all-dimensional claim is not accepted as proved: Hasebe2010, checked2011v3 p1, identifies a false nonabelian differential identity used in Lemma4.6/equation4.28. Bibliographic verification does not certify the claimed theorem.")
entry("hasebe2010white",author="Hasebe, Takahiro",
      title="White noise analysis on manifolds and the energy representation of a gauge group",
      journal="Infinite Dimensional Analysis, Quantum Probability and Related Topics",
      year=2010,volume=13,number=4,pages="619--627",
      doi="10.1142/S0219025710004243",
      url="https://arxiv.org/pdf/0805.1329",note="verified",
      annote="Full primary v3 PDF opened on2026-11-10; first preprint9May2008, journal2010, checked revision15January2011. Page1 explicitly discusses unresolved general2D irreducibility and the flaw in Shimada's proof. Abstract metadata still repeats the earlier claim and is not used to infer a solution. Author homepage independently confirms journal metadata.")
entry("ando2010local",author="Ando, Hiroshi",
      title="On the local structure of the representation of a local gauge group",
      journal="Infinite Dimensional Analysis, Quantum Probability and Related Topics",
      year=2010,volume=13,number=2,pages="223--242",
      doi="10.1142/S0219025710004036",url="https://arxiv.org/pdf/0904.2222",
      note="verified",annote="Full primary preprint opened on2026-11-10; submitted14April2009. Introduction and type-S commutant result inspected. Does not promote scalar intersection with the type-S operators to a scalar full commutant. Publisher URL was blocked; journal metadata is corroborative, theorem reading is from the author preprint.")
entry("albeverioetal2015brownian",typ="misc",
      author="Albeverio, Sergio and Driver, Bruce K. and Gordina, Maria and Vershik, A. M.",
      title="Equivalence of the Brownian and energy representations",year=2015,
      eprint="1511.07378",archivePrefix="arXiv",
      url="https://arxiv.org/pdf/1511.07378",note="verified",
      annote="Full primary preprint v1 dated23November2015 opened on2026-11-10. Sections2 and5, Theorems4.6 and5.8 inspected for finite-energy path hypotheses, stochastic logarithms, commuting left/right actions and explicit unitary equivalence. References1--2 distinguish1983factorial paper and its separate correction.")
entry("albeverioetal1983factorial",
      author="Albeverio, Sergio and H{\\o}egh-Krohn, Raphael and Testard, Daniel and Vershik, A. M.",
      title="Factorial representations of path groups",
      journal="Journal of Functional Analysis",year=1983,volume=51,number=1,pages="115--131",
      doi="10.1016/0022-1236(83)90030-7",
      url="https://www.sciencedirect.com/science/article/pii/0022123683900307",
      note="unverified",annote="Original URL attempted on2026-11-10, returned403. Authors and metadata verified indirectly in opened Albeverioetal2015 references1--2; a separate Note appears in JFA52(1)(1983),148. Full paper and correction not read. TypeIII path-group result is only thematic for the notebook's different algebra (L-infinity union W) double commutant.")

entry("balknazarenkozakharov1991drift",
      author="Balk, A. M. and Nazarenko, S. V. and Zakharov, V. E.",
      title="New invariant for drift turbulence",journal="Physics Letters A",
      year=1991,volume=152,number="5--6",pages="276--280",
      doi="10.1016/0375-9601(91)90105-H",
      url="https://zakharov.itp.ac.ru/pub/data/1991/1991-02-1-s2.0-037596019190105H-main.pdf",
      note="verified",annote="Full original opened on 2026-11-10. Received 11 October 1990, accepted 14 November 1990, published 21 January 1991. Sections 4--5 verify explicit additional collision invariants for limiting drift/Rossby laws. Section 6 announces uniqueness but expressly defers its proof. This is not a proof of full nonlinear integrability.")
entry("balkferapontov1994invariants",author="Balk, A. and Ferapontov, E.",
      title="Wave systems with an infinite number of invariants",
      journal="Physica D: Nonlinear Phenomena",year=1994,volume=70,number="1--2",pages="100--114",
      doi="10.1016/0167-2789(94)90059-0",
      url="https://www.itp.ac.ru/en/persons/balk-alexander-markovich/",
      note="verified",annote="Author-institution publication list opened on 2026-11-10 and exact metadata checked. Primary publisher abstract read in search: classification of all three-wave interactions with infinitely many independent invariants via web geometry. Publisher article URL returned 403; full theorem, equivalences and regularity hypotheses not read. Publication 1 January 1994; 1993 companion article already lists it as forthcoming. Verification is metadata and abstract, not proof.")
entry("balkferapontov1998web",typ="incollection",
      author="Balk, A. M. and Ferapontov, E. V.",
      title="Invariants of wave systems and web geometry",
      booktitle="Nonlinear waves and weak turbulence",editor="Zakharov, V. E.",
      series="American Mathematical Society Translations, Series 2",volume=182,
      year=1998,pages="1--30",publisher="American Mathematical Society",
      url="https://www.itp.ac.ru/en/persons/balk-alexander-markovich/",
      note="verified",annote="Author-institution publication list opened on 2026-11-10: title, authors, collection, volume and pages checked. Linked original chapter https://www.ams.org/books/trans2/182/01 returned 403. Rossby uniqueness content is corroborated in the opened primary Balk2014 article, Section 2.1, but the 1998 proof was not retrieved.")
entry("balk2014rossby",author="Balk, A. M.",
      title="The Rossby wave extra invariant in the dynamics of 3-D fluid layers and the generation of zonal jets",
      journal="Nonlinear Processes in Geophysics",year=2014,volume=21,number=1,pages="49--59",
      doi="10.5194/npg-21-49-2014",
      url="https://npg.copernicus.org/articles/21/49/2014/npg-21-49-2014.pdf",
      note="verified",annote="Full primary PDF opened on 2026-11-10. Received 28 February 2013, revised 22 September, accepted 9 November, published 10 January 2014. Sections 1.2 and 2.1 inspected: exact collision-invariant relation versus an approximate invariant of the nonlinear PDE; Rossby invariant uniqueness is attributed to Balk--Ferapontov1998. Not a claim to classify every degenerate law or prove nonlinear integrability.")

(P/"references.bib").write_text("\n".join(entries[k] for k in sorted(entries)))
print("Wrote",len(entries),"bibliography entries.")
