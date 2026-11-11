from pathlib import Path

here = Path(__file__).resolve().parent
p = here / 'build_middle.py'
s = p.read_text()
old = "refs=['stacks2026projective','stacks2026affine'],literal='correct with missing hypotheses')"
new = "refs=['stacks2026projective','stacks2026affine'],literal='correct')"
assert s.count(old) == 1
s = s.replace(old, new)
old = "corr('P000323','General-base removed locus',r'\\(\\{0\\}=(x_1,\\ldots,x_n)\\) as a single point for an arbitrary coefficient ring.',r'The removed closed subscheme is the zero section \\(V(x_1,\\ldots,x_n)\\cong\\operatorname{Spec}A\\).',r'The source has already generalized from a field to a ring. The ideal need not be a maximal ideal.')"
new = "corr('P000320','General-base zero notation',r'The notation \\(\\{0\\}\\) denotes the ideal \\((x_1,\\ldots,x_n)\\) and, explicitly, all prime ideals containing it.',r'In modern notation the removed closed subscheme is the zero section \\(V(x_1,\\ldots,x_n)\\cong\\operatorname{Spec}A\\).',r'The Russian text and scan P320 explicitly include all containing primes and distinguish the field case. This is a clarification of notation already correctly explained in the source, not a mathematical error.',typ='ambiguity')"
assert old in s
s = s.replace(old, new)
old = "'1970-201.1':r'The notation for a point is replaced by the zero section over an arbitrary base ring.',"
new = "'1970-201.1':r'The zero-section notation makes explicit the set of containing prime ideals already specified in the source on P320.',"
assert old in s
s = s.replace(old, new)
s = s.replace('P302,304–305,308,311–313,315–317,319,323,325–331.', 'P302,304–305,308,311–320,323,325–331.')
s = s.replace('P302,304,305,308,311,312,313,315,316,317,319,323,324,325,328,329,330,331.', 'P302,304,305,308,311,312,313,314,315,316,317,318,319,320,323,324,325,326,328,329,330,331.')
s = s.replace('For arbitrary coefficient rings, the removed locus is the zero section, not one maximal point.', 'For arbitrary coefficient rings, the removed locus is the zero section. The source already specifies all primes containing the coordinate ideal on P320 and distinguishes the field case, so modernizing its zero notation is a clarification, not a faithful mathematical error.')
p.write_text(s)
print('Clarified P320 zero-section provenance; mathematical formulas unchanged.')
