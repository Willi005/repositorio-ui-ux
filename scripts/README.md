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

## Customer Journey de Guillermo

La composición se edita en la [plantilla completada de Google Drawings](https://docs.google.com/drawings/d/1HmiUZjjn4FukMQQF9UjHnj1F81ZRwnVklLkbzSECMUQ/edit). La ficha textual [guillermo.md](../customer-journey/guillermo.md) se mantiene junto al dibujo; los scripts del benchmark no generan mapas de personas ni sobrescriben esta entrega.

La copia SVG vigente conserva la geometría y el texto del dibujo visible, incorpora los símbolos de la plantilla original y utiliza Liberation Sans para renderizar localmente. PNG y PDF se reproducen con librsvg (`rsvg-convert`):

```bash
rsvg-convert -w 2216 -h 2564 customer-journey/guillermo.svg -o customer-journey/guillermo.png
rsvg-convert -f pdf customer-journey/guillermo.svg -o customer-journey/guillermo.pdf
```

Para cambios de composición, editar el Google Drawing, usar Archivo → Descargar cuando esté disponible y reemplazar las copias locales tras revisar textos y recortes. La edición de contenido requiere actualizar también la ficha Markdown. [Detalle de la copia local y de la plantilla](../customer-journey/README.md).
