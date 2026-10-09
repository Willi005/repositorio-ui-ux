# Customer Journey definitivo

Entrega definitiva proporcionada por el equipo: **Customer Journey · William.pdf**. Sustituye las versiones anteriores del recorrido. El perfil corresponde al conductor de carga que figura como William en el título de la persona UX y como Guillermo en su descripción; se conserva el nombre y el contenido del PDF recibido.

[Ver el PDF definitivo](Customer%20Journey%20%C2%B7%20William.pdf) · [Vista previa PNG](definitivo.png) · [Persona UX](../ux-personas/2.png).

[![Customer Journey definitivo de William](definitivo.png)](Customer%20Journey%20%C2%B7%20William.pdf)

## Lectura del recorrido

El mapa, escrito en inglés, representa la búsqueda de orientación sobre horas que el conductor considera impagas y la preparación de una consulta a la Dirección del Trabajo. Incluye doce acciones, una curva emocional y filas de valor, barreras y oportunidades.

| Etapa | Acciones del documento |
| --- | --- |
| Search | Revisar liquidaciones; consultar a un colega; buscar en internet y encontrar fuentes contradictorias. |
| Verification | Describir transporte, jornada y pagos; revisar la norma citada y la confianza; reconocer información faltante y límites. |
| Guidance | Organizar documentos; elegir un canal discreto de la DT; preparar la consulta. |
| Follow-up | Contactar a la DT; guardar el resumen y comprobante; revisar pendientes y retomar la orientación. |

El momento clave consiste en identificar la regla de jornada aplicable, con su cita y nivel de confianza, antes de interpretar el pago. El propio documento declara que el recorrido es propuesto, las emociones son hipótesis y los resultados no están garantizados.

## Archivos

El **PDF proporcionado por el usuario es la fuente de entrega** y se conserva sin modificaciones. `definitivo.png` es una renderización de su única página para mostrarla directamente en GitHub. El enlace al dibujo de Google y las copias anteriores se retiraron de la entrega vigente; Git conserva su historial.

Para reproducir la imagen se usa Poppler:

```bash
pdftoppm -png -singlefile -scale-to 2800 'customer-journey/Customer Journey · William.pdf' customer-journey/definitivo
```

Ejecutar desde la raíz del repositorio. Una nueva versión debe reemplazar el PDF y regenerar la imagen para que ambos representen la misma entrega.
