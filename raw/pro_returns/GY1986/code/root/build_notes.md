# Build and typography notes

The supplied chapter builder, format specification, and style are preserved
under code/kit_original. The top-level builder has one typography adjustment:
the standalone driver's emergency stretch is 4 em instead of 2 em, permitting
better breaks in dense scholarly paragraphs. The style and its macros are
unchanged.

The assembly step moves five long inline formulas into display mathematics and
names the intermediate Jacobian before the long exact sequence. These are
presentation changes with the same mathematical content. Plain correction
cells have text-mode special characters escaped because the supplied builder
inserts them as raw LaTeX; explicit mathematical delimiters remain intact.
Two bibliographic series identifiers are moved between BibTeX fields so that
plainnat preserves them without its incompatible-volume-and-number warning.
The bibliography records still identify the same works.

The installed execution image initially lacked generated TeX filename
databases and a XeLaTeX format. tex_environment.py uses its existing package
trees with a writable local format cache and the installed Computer Modern/AMS
font maps. It makes no changes to system directories. Russian locale metadata
is available, while the image has no Russian hyphenation patterns; Russian
quotations are therefore unhyphenated and are checked for overflow.

The font cache and intermediate TeX format are environment-specific build
products and are not distributed. The setup program and its output are
included. A complete normal TeX installation uses its own existing format.
