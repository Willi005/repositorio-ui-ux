# LaTeX benchmarking report

The submission PDF is [benchmark.pdf](../benchmark.pdf). The editable document starts in [main.tex](main.tex). Build from the repository root:

```bash
python scripts/build_benchmark.py
```

This command requires `pdflatex` and the packages listed in `preamble.tex`, available in TeX Live with recommended and additional LaTeX packages. It needs neither BibTeX nor Biber: citations and references are maintained explicitly in the sources. Compilation continues until cross-references stabilize and rejects unresolved references or overflow greater than one point. Auxiliary files remain in a temporary directory.

## Editing

- `sections/cover.tex`: UFRO cover, authors, course, instructor, and report date.
- `sections/analysis.tex`: methodology, analysis, figures, decisions, and comparison matrix.
- `sections/references.tex`: alphabetical references and author-date citation targets.
- `preamble.tex`: formatting, typography, margins, tables, and notes.
- `assets/logo_ufro.png`: logo reused from the Networks report specified by the user.

Images are read directly from `benchmark/capturas/`, and the map from `benchmark/feature-map.pdf`. LaTeX neither repeats the research nor replaces screenshots. Markdown sources and HTML provide alternative reading formats; content edits must also be reflected in LaTeX because these sources do not synchronize automatically.

The main README displays `benchmark/portada-informe.png` as a preview linked to the complete PDF. After recompilation, [regenerate the cover with Poppler](../../scripts/README.md) to keep it current.

## Formatting approach

The [official APA 7 student paper guide](https://apastyle.apa.org/instructional-aids/student-paper-setup-guide.pdf) informs the layout: letter paper, one-inch margins, 12-point Times family, double-spaced body and references, left alignment, half-inch first-line and hanging indents, page numbers from the cover, and unnumbered headings. Tables have no vertical rules, with bold numbers, italic titles, and source notes. Dense matrix cells use 10-point text and single spacing on landscape pages; notes remain double-spaced.

The cover retains the UFRO logo, identity, and horizontal rules from the Networks report as the **requested institutional adaptation**. These additional elements are not part of APA's basic student title page. Authors and instructor come from the UX project. The displayed date indicates report preparation, not an invented submission deadline.

Screenshots and findings retain the **October 5, 2026** observation date. The format revision is dated **October 8, 2026**. Unknown dates use `n.d.`, with consistent suffixes and retrieval dates for changing pages. Spanish webpage titles are translated into English in the bibliography; official institution names and linked source pages identify the originals. This language correction adds no new research findings or user tests. Original screenshots remain authentic evidence; added annotations and the feature map are in English.
