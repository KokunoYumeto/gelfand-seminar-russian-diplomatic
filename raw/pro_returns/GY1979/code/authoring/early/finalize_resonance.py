"""Apply the late primary-source classification evidence to the authoring files."""
from pathlib import Path
p=Path(__file__).parent
f=p/'build_early.py'
s=f.read_text()
a=s.index('resonanceid=add(463,')
b=s.index('\nadd(463,',a+1)
s=s[:a]+r'''resonanceid=add(463,"P000843","problem","Is the difference-curve construction universal?",
 r"The page first asks for one additional additive function, then frames the construction as obtaining equations with infinitely many first integrals, and finally asks whether it is general.",
 r"In the infinitely-many-invariants reading, ask whether a regular local two-dimensional three-wave dispersion law admitting infinitely many independent smooth collision invariants can be represented by \((p,q,\omega)=(\xi_1-\xi_2,a(\xi_1)-a(\xi_2),b(\xi_1)-b(\xi_2))\), with an invertible momentum parametrization and compatible resonance branches.",
 r"The initial one-extra-invariant question and the subsequent infinitely-many-invariants programme are different quantifiers. The former cannot silently replace the latter. Additivity on a selected local component must also be distinguished from additivity on the entire resonance set and from nonlinear conserved quantities of the full wave equation.",
 r"The speaker's construction is published in \citet[Sec.~3]{zakharovschulman1988invariants}. Later \citet[abstract]{balkferapontov1994invariants} explicitly classifies three-wave interactions with infinitely many independent invariants using web geometry; the original theorem and its hypotheses were not retrieved, so this remains a partial publication match. The earlier none-or-infinitely-many expectation is contradicted by the finite-invariant examples announced in \citet[Secs.~4--6]{balknazarenkozakharov1991drift}. Their uniqueness proof is deferred there; \citet[Sec.~2.1]{balk2014rossby} confirms the Rossby uniqueness result and cites \citet{balkferapontov1998web}.",["zakharovschulman1988invariants","balkferapontov1994invariants","balknazarenkozakharov1991drift","balk2014rossby","balkferapontov1998web"],cls="B",status=r"As of November 2026, the infinitely-many-invariants classification has an identified later publication. An exact hypothesis-by-hypothesis comparison with the handwritten parametrization remains unverified because the 1994 theorem was inaccessible. The broader one-invariant reading is distinct; finite-extra-invariant systems occur in the published literature. No current open problem is inferred from the access limit.",literal="not determinable",match="partial",verification="indirect",problem="GP-1979-05",confidence="medium")''' +s[b:]
a=s.index('prob("GP-1979-05"')
b=s.index('\n',a)
s=s[:a]+r'''prob("GP-1979-05","Universality of the difference-curve resonance construction",r"Does every regular local two-dimensional three-wave dispersion law with infinitely many independent collision invariants admit the difference-curve parametrization on compatible resonance branches? This reconstructs the immediately preceding infinitely-many-first-integrals programme; it is not the earlier, broader request for one additional invariant.",[resonanceid],r"As of November 2026, Balk--Ferapontov's 1994 publication explicitly gives a classification of three-wave interactions with infinitely many invariants. Its full theorem was not retrieved, so exact local and branch hypotheses are unverified. The one-extra-invariant reading is distinct: finite-invariant examples were announced in 1991 and their uniqueness is discussed in the 1998 web-geometry development and Balk2014, Sec.2.1. This is a developed historical question with partial publication matching, not a claim of current openness.",["zakharovschulman1988invariants","balkferapontov1994invariants","balknazarenkozakharov1991drift","balkferapontov1998web","balk2014rossby"])''' +s[b:]
s=s.replace('The precise subsequent development is Zakharov--Schulman, first published in 1980 and expanded in 1988; its hypotheses prevent reading every integrable equation as having a degenerate scalar dispersion law.', 'The subsequent programme appears in Zakharov--Schulman (1980, 1988) and the later Balk--Ferapontov web classification (1994); one additional collision invariant and infinitely many are distinct hypotheses. None of these statements identifies every notion of nonlinear integrability with degenerate scalar dispersion.')
f.write_text(s)
f=p/'build_bibliography.py'
s=f.read_text()
a=s.index('(P/"references.bib").write_text')
new=r'''entry("balknazarenkozakharov1991drift",
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

'''
s=s[:a]+new+s[a:]
f.write_text(s)
