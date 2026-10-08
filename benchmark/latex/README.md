# Informe del benchmark en LaTeX

El PDF de entrega es [benchmark.pdf](../benchmark.pdf). La composición editable comienza en [main.tex](main.tex); se compila desde la raíz del repositorio:

```bash
python scripts/build_benchmark.py
```

El comando necesita `pdflatex` y los paquetes indicados en `preamble.tex`, disponibles en una instalación de TeX Live con los paquetes de LaTeX recomendados y adicionales. No necesita BibTeX ni Biber: las citas y las referencias se mantienen explícitas en las fuentes. Compila hasta estabilizar referencias cruzadas y rechaza referencias sin resolver o desbordamientos mayores a 1 punto. Los archivos auxiliares quedan en un directorio temporal.

## Edición

- `sections/cover.tex`: portada UFRO, autores, asignatura, docente y fecha del informe.
- `sections/analysis.tex`: metodología, análisis, figuras, decisiones y matriz comparativa.
- `sections/references.tex`: referencias alfabéticas y destinos de citas autor-fecha.
- `preamble.tex`: formato, tipografía, márgenes, tablas y notas.
- `assets/logo_ufro.png`: logo reutilizado del informe de Redes indicado por el usuario.

Las imágenes se leen directamente de `benchmark/capturas/` y el mapa de `benchmark/feature-map.pdf`. LaTeX no vuelve a investigar ni sustituye las capturas. Las fuentes Markdown y el HTML se conservan como lectura alternativa; una edición de contenido debe reflejarse también en el LaTeX, porque no se sincronizan automáticamente.

## Criterio de formato

Se aplicó la [guía oficial de trabajos estudiantiles APA 7](https://apastyle.apa.org/instructional-aids/student-paper-setup-guide.pdf): papel carta, márgenes de 2,54 cm, familia Times a 12 puntos, cuerpo y referencias a doble espacio, alineación izquierda, sangría de primera línea y francesa de 1,27 cm, número de página desde la portada y títulos sin numeración. Tablas sin líneas verticales; números en negrita, títulos en cursiva y notas de fuente. Las celdas densas de la matriz usan 10 puntos e interlineado simple en páginas horizontales; las notas mantienen doble espacio.

La portada conserva el logo, la identidad UFRO y las reglas horizontales del informe de Redes como **adaptación institucional solicitada**; esos elementos adicionales no pertenecen a la portada estudiantil básica de APA. Los autores y el docente proceden del proyecto UX. La fecha mostrada corresponde a la elaboración del informe, no a un plazo de entrega inventado.

Las capturas y los hallazgos conservan la observación del **5 de octubre de 2026**. La edición de formato es del **8 de octubre de 2026**. Se normalizaron títulos y fechas bibliográficas usando las fuentes oficiales; cuando no se conoce una fecha se emplea «s. f.», con sufijos coherentes y fecha de recuperación para páginas cambiantes. No se presentan como resultados nuevos ni como pruebas con usuarios.
