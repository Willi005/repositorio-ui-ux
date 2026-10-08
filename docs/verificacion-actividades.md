# Comprobación de benchmarking y Customer Journey

Benchmark: **5 de octubre de 2026**. Corrección del Customer Journey: **8 de octubre de 2026**. Rama de trabajo: `feature/benchmark-customer-journey`, creada desde `develop` conforme a Gitflow.

## Pauta de benchmarking

| Requisito | Evidencia preparada |
| --- | --- |
| Ecosistema inicial con plataformas y enlaces | Inventario de cinco candidatos en `benchmark/README.md`. |
| Directo, análogo y referencia; selección justificada | DT, SUSESO y ChileAtiende, con categorías y límites de comparación. |
| Diez dimensiones base, comparables | Cuatro tablas temáticas en `benchmark/tabla-comparativa.md`. |
| Entre dos y cuatro dimensiones del dominio | Cuatro: trazabilidad, límites, derivación competente y privacidad/control. |
| Dos positivos y dos problemas por herramienta | Fichas de análisis con heurísticas e imágenes que sustentan la interpretación. |
| Tres capturas anotadas por herramienta | Nueve PNG con título, dos anotaciones y comentario de dos líneas; originales preservados. |
| Mapa de funcionalidades | PNG/SVG/PDF: distingue estándares de la muestra, diferencias y oportunidades hipotéticas. |
| Propuesta del grupo como fila completa | Fila en cada una de las cuatro tablas, calificada como propuesta aún no implementada. |
| Patrones adoptados/rechazados y restricciones | Sección de decisiones del análisis; al menos tres vínculos con personas y prototipo. |
| Relación con Garrett | Estrategia y Alcance explicitados. |
| Fuentes y contexto temporal | Enlaces oficiales junto a afirmaciones; registro de capturas con fecha, URL y tamaño de ventana. |

**Alcance pendiente de validación:** no se completaron cuentas ni trámites autenticados, pruebas de errores/confirmaciones de expedientes o reseñas de usuarios. La pauta recomienda esa exploración: el documento declara la limitación y no simula evidencia. El mapa requiere revisión colaborativa del equipo; no se afirma haber realizado esa reunión. El benchmarking es una base documental y una inspección pública para profundizar, no una evaluación de desempeño ni auditoría de accesibilidad.

## Plantilla y Customer Journey

| Requisito | Evidencia preparada |
| --- | --- |
| Formato del profesor | Google Drawing completado directamente, conservando su composición y objetos editables. |
| Alcance corregido | Una sola entrega de Guillermo, conductor de carga de 51 años en Temuco. |
| Puntos de contacto y actividades | Dieciséis acciones distribuidas en búsqueda, verificación, orientación y seguimiento. |
| Canales y dispositivos | Detallados por acción en la ficha Markdown; celular como supuesto por validar. |
| Curva y descripción de emociones | Línea cualitativa y leyenda de nueve emociones; detalle inferido por acción, sin puntuaciones medidas. |
| Valor, barreras y oportunidades | Doce recuadros completos: cuatro de cada dimensión. |
| Momento clave | Identificar régimen de jornada y antecedentes faltantes antes de interpretar pagos. |
| Trazabilidad y validación | Relación entre persona, Canvas, benchmark, decisiones y preguntas de validación. |
| Archivos | Fuente editable en Google Drawings; copia SVG, PNG, PDF de una página, ficha Markdown y captura del documento guardado. |

El mapa es una experiencia propuesta. La curva no procede de entrevistas ni expresa una medición. No se inventan montos, plazos ni resultados individuales. La persona original usa «William» en el título y «Guillermo» en la descripción; se adopta el nombre solicitado por el usuario.

## Revisión técnica y visual

La revisión inicial del 5 de octubre comprobó nueve capturas anotadas, mapa de funcionalidades e informe de benchmarking de 22 páginas. Esa evidencia conserva su fecha de observación.

La corrección del 8 de octubre se revisó contra el dibujo guardado en Google Drive: cuatro etapas, dieciséis acciones y doce recuadros completos, sin ejemplos turísticos ni marcadores «Actividad» o «Escribir». Se revisaron visualmente la copia PNG y una página renderizada del PDF, además de comprobar los destinos de los enlaces locales y ejecutar `git diff --check`.

La descarga de Google Drawings no produjo archivos. La copia SVG se obtuvo del contenido visible, con los símbolos del respaldo de la plantilla original y sustitución local de fuentes web por Liberation Sans. PNG/PDF se renderizan con librsvg; la composición original continúa editable en Google Drawings. Los scripts del benchmark ya no generan ni recuperan los tres mapas anteriores.

El PDF del Journey tiene una página. Las copias locales anteriores se retiraron de la entrega; permanecen recuperables en Git. Se actualizó la bóveda de Obsidian con este alcance.

La inspección de accesibilidad del benchmark se limita a controles visibles. Los PDF no se presentan como PDF/UA certificados; la ficha Markdown ofrece una alternativa textual a la imagen.

## Informe LaTeX y APA 7: 8 de octubre de 2026

El informe de entrega se compila desde `benchmark/latex/`. La portada recicla la identidad UFRO del informe de Redes y actualiza equipo, docente y asignatura; se documenta su adaptación institucional. Se aplicaron doble interlineado, márgenes de 2,54 cm, sangría de 1,27 cm, tipografía Times de 12 puntos, encabezado con número de página, citas autor-fecha y referencias alfabéticas con sangría francesa. La matriz usa celdas a 10 puntos e interlineado simple para mantener legibilidad.

El PDF final tiene 27 páginas. Se verificó la compilación con 27 referencias bibliográficas citadas y referencias cruzadas resueltas, cinco tablas y diez figuras (nueve capturas más el mapa). Se corrigieron notas separadas de sus tablas y se revisaron las páginas renderizadas. El comando rechaza errores de compilación, referencias sin resolver y desbordamientos mayores a 1 punto. Se comprobaron sintaxis de los scripts y enlaces locales; regenerar el HTML conservó el hash del PDF de LaTeX. La fecha de observación se mantiene en 5 de octubre de 2026.
