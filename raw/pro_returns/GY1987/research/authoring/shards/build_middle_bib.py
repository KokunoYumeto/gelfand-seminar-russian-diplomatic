import json, re
from pathlib import Path

BASE = Path(__file__).parent
WORK = BASE.parent

def entries(text):
    result = {}
    for m in re.finditer(r'(?m)^@(\w+)\s*\{\s*([^,\s]+)\s*,', text):
        start, i, depth = m.start(), m.end(), 1
        while i < len(text) and depth:
            if text[i] == '{' and (i == 0 or text[i-1] != '\\'):
                depth += 1
            elif text[i] == '}' and (i == 0 or text[i-1] != '\\'):
                depth -= 1
            i += 1
        if depth:
            raise ValueError(m.group(2))
        result.setdefault(m.group(2), text[start:i])
    return result

def setfield(entry, field, value):
    m = re.search(r'(?i)\b'+re.escape(field)+r'\s*=\s*\{', entry)
    if m:
        i, depth = m.end(), 1
        while depth:
            if entry[i] == '{' and entry[i-1] != '\\':
                depth += 1
            elif entry[i] == '}' and entry[i-1] != '\\':
                depth -= 1
            i += 1
        return entry[:m.end()] + value + entry[i-1:]
    head = entry[:-1].rstrip()
    if not head.endswith(','):
        head += ','
    return head + '\n  '+field+' = {'+value+'}\n}'

catalog = entries((WORK/'references_cumulative.bib').read_text())
catalog.update(entries((BASE/'middle_new_references.bib').read_text()))
used = set()
for name in ['items', 'problems']:
    for obj in json.loads((BASE/f'middle_{name}.json').read_text()):
        used.update(obj['refs'])

updates = {
 'baire1900nouvelle': {
  'url': 'https://www.numdam.org/article/BSMF_1900__28__173_0.pdf',
  'annote': 'Current-task verification on11November2026: full original Numdam PDF opened. The theorem on p173 and its explicit reference to the 1899 thesis read; the article gives a new proof of sufficiency for continuous pointwise approximation. Historical source, not a new1988 result.'
 },
 'belavinpolyakovzamolodchikov1984infinite': {
  'url': 'https://qft.itp.ac.ru/BPZ.pdf',
  'annote': 'Current-task verification on11November2026: complete original48-page article opened. Introduction equations1.6--1.17, Section2 stress tensor and equations2.17--2.29, Section3 equations3.1--3.13, and Section6 equations6.11--6.18 on the Ising model read. Received22November1983, published1984. The unregularized path-integral existence and full Euclidean reflection-positivity theorem are not claimed to follow merely from this source.'
 },
 'gelfandponomarev1971quadruples': {
  'url': 'https://www.mathnet.ru/eng/dan36010',
  'annote': 'Current-task verification on11November2026: MathNet metadata and full original four-page Russian paper opened and read. Section1 operator-graph examples, Section2 Assertions1--2, Section3 Theorem1 and Section4 special cases checked. The field is algebraically closed of characteristic zero; received21October1970, published1971. Cumulative bibliography key retained.'
 },
 'osterwalderschrader1975euclidean': {
  'url': 'https://link.springer.com/article/10.1007/BF01608978',
  'annote': 'Current-task verification on11November2026: publisher metadata and abstract opened. The abstract states that the reconstruction result extends and corrects the earlier paper. PublishedOctober1975, received3December1974 and revised16January1975. Full-text retrieval from Project Euclid was blocked; verification is metadata/abstract only, not a claim to have read the proof.'
 },
 'krattenthaler1999determinant': {
  'url': 'https://arxiv.org/pdf/math/9902004',
  'annote': 'Current-task verification on11November2026: full primary arXiv paper opened; Section2 equation2.7, the classical Cauchy determinant evaluation, read. First submitted1February1999; version3 dated31May1999. It is cited for an established classical identity, not as its original discovery.'
 },
 'nist2026dlmf': {
  'title': '{NIST Digital Library of Mathematical Functions}',
  'url': 'https://dlmf.nist.gov/',
  'annote': 'Current-task verification on11November2026: NIST pages25.4,18.5 and18.2 opened. Equations25.4.3--4, Rodrigues equation18.5.5 and Table18.5.1, and Section18.2(vi) statement that the zeros are simple and inside the orthogonality interval read. Current reference formulation of classical results;2026 is the consultation year.'
 },
 'gelfanddikii1976fractional': {
  'url': 'https://www.mathnet.ru/eng/faa2188',
  'annote': 'Current-task verification on11November2026: MathNet metadata and full original17-page Russian article opened. Section1 formal local-functional quotient and variational derivative, Section2 symbolic composition, and Sections10--11 Lie-bracket and Poisson constructions read. Received22June1976. Cumulative key retained; this is not substituted for the separate1978 second-bracket proof.'
 },
 'gelfanddikii1978jets': {
  'doi': '10.1007/BF01076250',
  'url': 'https://www.mathnet.ru/eng/faa1979',
  'annote': 'Current-task verification on11November2026: MathNet metadata and full original16-page Russian paper opened. Introduction and Section1 read for differential-polynomial algebra, total derivative, jet calculus and Euler derivative. Received26December1977. Cumulative key retained; no claim that the entire paper was read.'
 },
 'gelfanddorfman1979hamiltonian': {
  'url': 'https://www.mathnet.ru/eng/faa1933',
  'annote': 'Current-task verification on11November2026: full original18-page Russian paper opened. Sections1--2 and Theorems1.1,1.3,2.1 read for Lie-algebra/module Cartan calculus and Hamiltonian operators without a multiplication on local functionals. Section3 criteria and Section5 Theorem5.1 also inspected. Received16April1979. Cumulative key retained.'
 },
 'laumon1987fourier': {
  'annote': 'Current-task verification on11November2026: full primary PDF opened. Introduction pp131--134 and Theorem3.2.1.1 with Remarks3.2.1.3 pp187--188 read for the Fourier-transform and epsilon-factor product programme. The l-adic finite-field theorem is not substituted for an unnormalized complex determinant-line identity.'
 },
 'lukyanov1988quantization': {
  'annote': 'Current-task verification on11November2026: MathNet metadata and full original Russian paper opened. Section1 Theorem1 and equations1.1--1.9, Section2 Proposition2, equations2.11--2.21 and closure proof, Section3 Theorem2 read. Equation2.15 exactly identifies the notebook conjugated O(1) relation. Received25February1988 before the seminar; original22(4),1--10. No exact R-matrix theorem is inferred from the final notebook analogy.'
 },
 'sergeichuk1990pairs': {
  'doi': '10.1007/BF01071340',
  'annote': 'Current-task verification on11November2026: original author-hosted English translation opened; introduction and Theorem1 read for finite-dimensional pairs, characteristic not two and possibly degenerate forms. Received13September1988; original42(4),549--554. Subsequent reopening of the Kiev URL redirected to Kyiv and failed, but the earlier successful opening and result reading are recorded in the evidence log. No infinite-dimensional claim is made.'
 }
}
for key, fields in updates.items():
    for field, value in fields.items():
        catalog[key] = setfield(catalog[key], field, value)
for key in used:
    if key not in catalog:
        raise ValueError('Missing reference: '+key)
    catalog[key] = setfield(catalog[key], 'note', 'verified')
    if not re.search(r'\b(url|doi)\s*=', catalog[key]):
        raise ValueError('Missing URL/DOI: '+key)
    if not re.search(r'\bannote\s*=', catalog[key]):
        raise ValueError('Missing verification scope: '+key)

(BASE/'middle_references.bib').write_text(
    '% Current-task bibliography and verification scopes, checked 2026-11-11.\n\n'
    + '\n\n'.join(catalog[key] for key in sorted(used)) + '\n'
)
print(f'{len(used)} cited keys written with current-task verification scopes.')
