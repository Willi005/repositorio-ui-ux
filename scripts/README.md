# Reproducción de los artefactos

Requisitos: Python, `uv`, bibliotecas Cairo/Pango para renderizar y Poppler (`pdfunite`, `pdfinfo`, `pdftoppm`) para unir y revisar PDF. Las versiones de Python utilizadas y el alcance de revisión figuran en [la comprobación](../docs/verificacion-actividades.md).

Desde la raíz del repositorio:

```bash
uv venv .venv-artifacts
uv pip install --python .venv-artifacts/bin/python -r scripts/requirements.txt
.venv-artifacts/bin/python scripts/generate_artifacts.py
.venv-artifacts/bin/python scripts/render_benchmark.py
```

`generate_artifacts.py` utiliza capturas originales, anotaciones de evidencia y `customer-journey/journeys.json`. Genera nueve PNG anotados, un mapa comparativo, tres mapas de experiencia y sus fichas Markdown; cada mapa se exporta a PNG, SVG y PDF. Une los recorridos en un PDF de tres páginas. Comprueba el número máximo de líneas al generar bloques de texto.

`render_benchmark.py` compone el análisis y la tabla comparativa como informe HTML autónomo y PDF, con las imágenes embebidas. No realiza búsquedas, gestiones ni cargas a servicios externos.

La edición se realiza en los Markdown, las anotaciones del generador y `journeys.json`; los PNG/PDF son exportaciones. No editar a mano las fichas individuales de Journey si se va a regenerar: su contenido se toma del JSON. El archivo `customer-journey/README.md` conserva la metodología y se mantiene por separado.
