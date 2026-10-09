# Reproducción de los artefactos

Requisitos del benchmark: Python, `uv`, bibliotecas Cairo/Pango y TeX Live con `pdflatex`. Poppler permite revisar los PDF. Desde la raíz del repositorio:

```bash
uv venv .venv-artifacts
uv pip install --python .venv-artifacts/bin/python -r scripts/requirements.txt
.venv-artifacts/bin/python scripts/generate_artifacts.py
.venv-artifacts/bin/python scripts/render_benchmark.py
python scripts/build_benchmark.py
```

`generate_artifacts.py` utiliza las capturas originales y las anotaciones de evidencia. Genera nueve PNG anotados y el mapa comparativo en SVG, PNG y PDF. `render_benchmark.py` compone el análisis y la tabla comparativa como HTML autónomo con imágenes embebidas. `build_benchmark.py` compila las fuentes de `benchmark/latex/` y genera el PDF de entrega con formato APA 7 y portada UFRO adaptada. El HTML no sobrescribe ese PDF. [Formato, fuentes y edición](../benchmark/latex/README.md). No consulta ni modifica servicios externos.

La portada visible en el README principal se renderiza desde el PDF con Poppler. Regenerarla después de cambiar el informe:

```bash
pdftoppm -f 1 -l 1 -png -singlefile -scale-to 1600 benchmark/benchmark.pdf benchmark/portada-informe
```

## Customer Journey definitivo

El PDF [Customer Journey · William](../customer-journey/Customer%20Journey%20%C2%B7%20William.pdf) es la entrega definitiva del usuario. Se conserva sin modificar. Su vista previa para GitHub se genera con Poppler desde la raíz del repositorio:

```bash
pdftoppm -png -singlefile -scale-to 2800 'customer-journey/Customer Journey · William.pdf' customer-journey/definitivo
```

Los scripts del benchmark no generan ni sobrescriben el Journey. Las copias anteriores se retiraron de la entrega vigente y permanecen recuperables en Git. [Descripción de la entrega](../customer-journey/README.md).
