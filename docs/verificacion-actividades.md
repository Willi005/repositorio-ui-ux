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

## Customer Journey definitivo

El usuario reemplazó los archivos del recorrido anterior por `customer-journey/Customer Journey · William.pdf` y declaró ese documento como definitivo. El PDF se conserva sin modificación; la imagen `definitivo.png` se renderiza desde él para mostrarlo en el README principal.

| Contenido | Evidencia del PDF definitivo |
| --- | --- |
| Persona | William, correspondiente al conductor de carga de la persona UX. |
| Idioma | Inglés en todo el mapa. |
| Etapas | Search, Verification, Guidance y Follow-up. |
| Acciones | Doce acciones numeradas, tres por etapa. |
| Emociones | Doce etiquetas y curva cualitativa; se declaran hipótesis. |
| Filas inferiores | Valor, barreras y oportunidades para cada etapa. |
| Momento clave | Identificar la regla de jornada aplicable con cita y confianza antes de interpretar pagos. |
| Entrega | PDF definitivo de una página y PNG para GitHub. |

Se revisaron la página completa, su texto y la vista previa; se comprobaron los enlaces locales y la coincidencia del hash del PDF antes y después de preparar la publicación. Las versiones anteriores se retiran del árbol vigente, conservando su historial en Git. El README principal mantiene una explicación breve y una imagen enlazada al PDF.

Las observaciones del benchmark son del 5 de octubre de 2026. El Journey es una experiencia propuesta y no acredita entrevistas, medición de emociones ni resolución favorable del caso. Los PDF no se presentan como certificados PDF/UA.

## Informe LaTeX y APA 7: 8 de octubre de 2026

El informe de entrega se compila desde `benchmark/latex/`. La portada recicla la identidad UFRO del informe de Redes y actualiza equipo, docente y asignatura; se documenta su adaptación institucional. Se aplicaron doble interlineado, márgenes de 2,54 cm, sangría de 1,27 cm, tipografía Times de 12 puntos, encabezado con número de página, citas autor-fecha y referencias alfabéticas con sangría francesa. La matriz usa celdas a 10 puntos e interlineado simple para mantener legibilidad.

El PDF final tiene 27 páginas. Se verificó la compilación con 27 referencias bibliográficas citadas y referencias cruzadas resueltas, cinco tablas y diez figuras (nueve capturas más el mapa). Se corrigieron notas separadas de sus tablas y se revisaron las páginas renderizadas. El comando rechaza errores de compilación, referencias sin resolver y desbordamientos mayores a 1 punto. Se comprobaron sintaxis de los scripts y enlaces locales; regenerar el HTML conservó el hash del PDF de LaTeX. La fecha de observación se mantiene en 5 de octubre de 2026.

El README principal muestra una portada PNG renderizada desde el informe, enlazada al PDF de 27 páginas, y conserva el mapa comparativo. Junto a la imagen del Journey definitivo, estas vistas previas presentan las dos actividades con explicaciones breves y acceso a sus documentos completos.
