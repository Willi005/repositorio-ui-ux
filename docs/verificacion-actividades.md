# Comprobación de benchmarking y Customer Journey

Fecha: **5 de octubre de 2026**. Rama de trabajo: `feature/benchmark-customer-journey`, creada desde `develop` conforme a Gitflow.

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
| Plantilla revisada | Documento Google Drawings leído en navegador; correspondencia de componentes documentada. |
| Perspectiva de las personas existentes | Tres mapas; Joseph como caso principal, William y Benjamin complementarios. |
| Puntos de contacto y actividades | Ocho por persona, distribuidos en cuatro fases; detalle Markdown y acciones en la imagen. |
| Canales y dispositivos | Indicados por contacto; uso del celular marcado como supuesto por validar. |
| Curva y descripción de emociones | Ocho emociones por mapa y curva cualitativa, explícitamente inferidas. |
| Valor, barreras y oportunidades | Cuatro bloques de cada dimensión por mapa. |
| Momento clave | Contacto destacado en la curva y descrito en texto. |
| Trazabilidad y validación | Tabla evidencia → decisión → contacto → comprobación y plan de sesiones. |
| Exportaciones | PNG, SVG editable, PDF individual y PDF conjunto de tres páginas. |

Los mapas son recorridos propuestos. La curva emocional no procede de entrevistas ni expresa una medición. Los organismos de destino se seleccionan por materia/etapa, y no se inventan montos, plazos ni resultados individuales.

## Revisión técnica y visual

- Se verificó la estructura: nueve capturas anotadas; tres mapas con ocho contactos/emociones y cuatro bloques por dimensión.
- Se regeneraron los artefactos y se revisaron visualmente los tres mapas, el mapa de funcionalidades y páginas del informe PDF. Se corrigieron recortes de contenido y composición de las capturas en la exportación.
- Se comprobó la existencia de los destinos locales de todos los enlaces Markdown y el tamaño/número de páginas de los PDF: 22 páginas del informe y tres del conjunto de mapas. Los enlaces externos respaldan la investigación de la fecha; no se garantiza su permanencia.
- Se ejecutó `git diff --check`. No se requieren pruebas de aplicación porque el trabajo incorpora documentación, evidencia y generadores de artefactos, sin implementar un producto.
- Entorno de generación: Python 3.14.7; Pillow 12.3.0, CairoSVG 2.9.1, Markdown 3.11 y WeasyPrint 70.0. Dependencias fijadas en `scripts/requirements.txt`; Poppler utilizado para unir y renderizar.

La inspección visual de accesibilidad del benchmark se limita a los controles visibles. Los PDF no se presentan como documentos PDF/UA certificados; las fichas Markdown conservan una alternativa textual a los mapas e imágenes.
