# Reproducing the artifacts

Benchmark requirements: Python, `uv`, Cairo/Pango libraries, and TeX Live with `pdflatex`. Poppler supports PDF inspection. From the repository root:

```bash
uv venv .venv-artifacts
uv pip install --python .venv-artifacts/bin/python -r scripts/requirements.txt
.venv-artifacts/bin/python scripts/generate_artifacts.py
.venv-artifacts/bin/python scripts/render_benchmark.py
python scripts/build_benchmark.py
```

`generate_artifacts.py` uses original screenshots and evidence annotations. It generates nine annotated PNGs and the feature map in SVG, PNG, and PDF. `render_benchmark.py` combines the analysis and comparison matrix into standalone HTML with embedded images. `build_benchmark.py` compiles `benchmark/latex/` and produces the submission PDF with an APA 7 body and an adapted UFRO cover. The HTML renderer does not overwrite that PDF. [Formatting, sources, and editing](../benchmark/latex/README.md). These scripts do not access or modify external services.

The main README's cover preview is rendered from the report PDF with Poppler. Regenerate it after changing the report:

```bash
pdftoppm -f 1 -l 1 -png -singlefile -scale-to 1600 benchmark/benchmark.pdf benchmark/portada-informe
```

## Definitive Customer Journey

The [Customer Journey · William PDF](../customer-journey/Customer%20Journey%20%C2%B7%20William.pdf) is the user's definitive submission and is preserved without modification. Generate its GitHub preview with Poppler from the repository root:

```bash
pdftoppm -png -singlefile -scale-to 2800 'customer-journey/Customer Journey · William.pdf' customer-journey/definitivo
```

Benchmark scripts do not generate or overwrite the Journey. Earlier copies were removed from the current submission and remain recoverable in Git. [Submission description](../customer-journey/README.md).
