from pathlib import Path
import hashlib
import re

here = Path(__file__).resolve().parent
bib_path = here.parents[2] / 'deliverable' / 'GY1969_references.bib'
# The segment directory is work/parts/middle; the workspace is three parents up.
if not bib_path.exists():
    bib_path = here.parents[3] / 'deliverable' / 'GY1969_references.bib'
bib = bib_path.read_text()
blocks = re.split(r'(?m)(?=^@)', bib)

entries = [
    ('artin1968analytic', 'Artin, M. (1968). On the solutions of analytic equations. *Inventiones Mathematicae, 5*, 277–291.'),
    ('bourgain1988uncertainty', 'Bourgain, J. (1988). A remark on the uncertainty principle for Hilbertian basis. *Journal of Functional Analysis, 79*(1), 136–143.'),
    ('gelfandponomarev1971quadruples', "Gel’fand, I. M., & Ponomarev, V. A. (1971). Quadruples of subspaces of a finite-dimensional vector space. *Doklady Akademii Nauk SSSR, 197*(4), 762–765."),
    ('griffiths1970periods', 'Griffiths, P. A. (1970). Periods of integrals on algebraic manifolds: Summary of main results and discussion of open problems. *Bulletin of the American Mathematical Society, 76*, 228–296.'),
    ('grochenigmalinnikova2013localization', 'Gröchenig, K., & Malinnikova, E. (2013). Phase space localization of Riesz bases for $L^2(\\mathbb{R}^d)$. *Revista Matemática Iberoamericana, 29*(1), 115–134.'),
    ('hewittross1970abstract', 'Hewitt, E., & Ross, K. A. (1970). *Abstract harmonic analysis* (Vol. II; Grundlehren der mathematischen Wissenschaften, Vol. 152). Springer.'),
    ('ismagilov1976unitary', 'Ismagilov, R. S. (1976). On unitary representations of the group $C_0^\\infty(X,G)$, $G=SU_2$. *Mathematics of the USSR-Sbornik, 29*(1), 105–117.'),
    ('ismagilov1981segment', 'Ismagilov, R. S. (1981). Representations of the group of smooth mappings of a segment into a compact Lie group. *Functional Analysis and Its Applications, 15*(2), 134–135.'),
    ('janssensneeb2015norm', 'Janssens, B., & Neeb, K.-H. (2015). Norm continuous unitary representations of Lie algebras of smooth sections. *International Mathematics Research Notices, 2015*(18), 9081–9137.'),
    ('mcduff1969uncountably', 'McDuff, D. (1969). Uncountably many II₁ factors. *Annals of Mathematics, 90*(2), 372–377.'),
    ('meyer1987uncertainty', 'Meyer, Y. (1987). Principe d’incertitude, bases hilbertiennes et algèbres d’opérateurs. In *Séminaire Bourbaki, 1985–1986* (Exposé No. 662, pp. 209–223). *Astérisque, 145–146*.'),
    ('perelomov1971completeness', 'Perelomov, A. M. (1971). On the completeness of a system of coherent states. *Theoretical and Mathematical Physics, 6*(2), 156–164.'),
    ('russo1974fourier', 'Russo, B. (1974). The norm of the $L^p$-Fourier transform on unimodular groups. *Transactions of the American Mathematical Society, 192*, 293–305.'),
]

output = [
    '## Selected references for this report',
    '',
    'The full bibliography is `GY1969_references.bib`. The entries below use its publication metadata and link to the access points recorded as opened. Publication years are distinguished from lecture, manuscript, and later archival-posting dates in the discussion above.',
    '',
]
for key, entry in entries:
    matches = [b for b in blocks if re.match(r'@\w+\{' + re.escape(key) + r',', b)]
    assert len(matches) == 1, key
    block = matches[0]
    assert 'note = {verified}' in block, key
    url = re.search(r'(?m)^\s*url\s*=\s*\{([^\n]+)\},?', block).group(1)
    # Use the verified URL itself, without asserting that a separate DOI resolver was opened.
    output.extend([f'{entry} [{url}]({url})', ''])
    print(key, url)

target = here / 'report_selected_references.md'
target.write_text('\n'.join(output))
assert len(entries) == 13
print('Entries:', len(entries))
print('Source bibliography SHA-256:', hashlib.sha256(bib.encode()).hexdigest())
print('Written:', target)
print('Shortlist corrections: replace Gelfand–Ponomarev title with the exact 1971 announcement title; restore the Griffiths subtitle. No year changes required.')
