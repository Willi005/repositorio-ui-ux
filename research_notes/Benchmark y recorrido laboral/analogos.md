# Análogos y referencias: SUSESO y ChileAtiende

Fecha de consulta: 5 de octubre de 2026. Investigación documental con fuentes oficiales y lectura del contenido público. No se ingresó a cuentas ni se enviaron trámites. Las inferencias son propuestas para el proyecto, no resultados de pruebas con usuarios. Personas de referencia proporcionadas por el equipo: Benjamin, 24 años, retail, Valdivia, primera licencia; William, 51 años, transporte, Temuco, horas extra; Joseph, 42 años, bodeguero, Concepción, finiquito tras ocho años.

## ¿Qué aporta SUSESO como análogo de orientación y seguimiento?

### Takeaway

SUSESO combina orientación por perfil, preparación de antecedentes y seguimiento de reclamos de seguridad social. Aporta patrones para preparar al usuario antes de un trámite, con límites explícitos sobre el alcance de una estimación. [Usuarios](https://www.suseso.gob.cl/606/w3-propertyvalue-610.html), [Orientador](https://www.suseso.gob.cl/606/w3-propertyname-509.html), [Simulador SIL](https://www.suseso.gob.cl/606/w3-article-711911.html).

### Cited Findings

- **Plataforma y versión:** sitio web público institucional, con enlaces a la plataforma PAE; no aparece un número de versión en las páginas consultadas. El acceso observado a PAE redirige al dominio `pae.suseso.gob.cl`. [Usuarios](https://www.suseso.gob.cl/606/w3-propertyvalue-610.html), [Ingreso PAE](https://pae.suseso.gob.cl/pae-web/loginCiudadano).
- **Perfil:** el orientador ofrece entradas para trabajadores, familias, reclamos contra una Caja y acceso a certificados/registros/formularios/resoluciones. La entrada de trabajadores declara el perfil de persona que cotiza regularmente y tiene empleador. [Orientador](https://www.suseso.gob.cl/606/w3-propertyname-509.html), [Orientación para trabajadores](https://www.suseso.gob.cl/606/w3-propertyvalue-34955.html).
- **Propuesta y autoridad:** resuelve apelaciones y reclamos sobre derechos de seguridad social relativos a las entidades que fiscaliza. Su competencia se describe por materias e instituciones. [Qué hacemos](https://www.suseso.gob.cl/601/w3-propertyvalue-10381.html), [Entidades fiscalizadas](https://www.suseso.gob.cl/609/w3-propertyname-535.html).
- **Funciones públicas:** reclamos, seguimiento, simulación del Subsidio por Incapacidad Laboral (SIL), trámites en línea, orientación, informe médico complementario y material educativo. [Usuarios](https://www.suseso.gob.cl/606/w3-propertyvalue-610.html).
- **Navegación:** una página separa tres intenciones: reclamar, consultar avance y preparar el reclamo. El orientador de trabajadores clasifica por problemas como licencias, accidentes y SIL; los detalles presentan recomendación, requisitos, tramitación y ayuda. [Todo sobre el reclamo](https://www.suseso.gob.cl/606/w3-article-689771.html), [Orientación para trabajadores](https://www.suseso.gob.cl/606/w3-propertyvalue-34955.html).
- **Observación visual aportada por el coordinador:** Usuarios muestra botones separados para reclamar y seguir, y el orientador presenta perfiles. La pantalla de licencia ofrece rechazo/modificación o “Aún no ha sido pronunciada por la COMPIN”; no se vio explicación inline de “pronunciada”. En viewport 866 × 922 el control de tamaño de texto cubría parcialmente “Volver”. Es una observación puntual, no una conclusión general de accesibilidad. [Usuarios](https://www.suseso.gob.cl/606/w3-propertyvalue-610.html), [Orientador](https://www.suseso.gob.cl/606/w3-propertyname-509.html), [Licencias](https://www.suseso.gob.cl/606/w3-propertyvalue-586.html).
- **Onboarding observado:** orientación y preparación se leen públicamente; la pantalla de PAE ofrece ClaveÚnica, Clave Tributaria y acceso con contraseña reservado a personas jurídicas. No se probó el flujo autenticado. [Ingreso PAE](https://pae.suseso.gob.cl/pae-web/loginCiudadano).
- **Preparación de datos:** el reclamo por reposo injustificado muestra ejemplos de resolución COMPIN, informe médico y licencia en papel; exige reposición previa ante COMPIN. [Reclame ante SUSESO](https://www.suseso.gob.cl/606/w3-article-40310.html).
- **Seguimiento y carga documental:** el tutorial describe ingreso, antecedentes, estudio y resolución; exige completar el resumen antes de ingresar. Documenta PDF/JPG, hasta 120 MB por archivo, confirmación “OK” y revisión con lupa. El estado de los expedientes se consulta en Mi Portal con ClaveÚnica/RUN. La demora depende de la complejidad; la página declara alta demanda. [Ciclo de vida del reclamo](https://www.suseso.gob.cl/606/w3-propertyvalue-562466.html).
- **Simulador y límites:** para licencias comunes de trabajadores dependientes privados, solicita las tres últimas liquidaciones y costo del plan Isapre cuando corresponde. Declara resultado estimado y exclusión de licencias previas/consecutivas. [Presentación SIL](https://www.suseso.gob.cl/606/w3-article-711911.html). El formulario público contiene renta imponible, días trabajados, remuneración ocasional y validación de montos; no se ingresaron datos. [Formulario SIL](https://www.suseso.gob.cl/606/w3-article-712302.html).
- **Derivación:** el compendio exige agotar las instancias previas de reclamo ante COMPIN antes de recurrir a SUSESO por rechazo/reducción de licencia. [Compendio LM SIL](https://www.suseso.cl/622/w3-propertyvalue-788701.html).

### Inferences

- Para Benjamin: separar “entender mi primera licencia”, “estimar el pago” y “reclamar una decisión” evita convertir una duda inicial en un reclamo prematuro. Mostrar por qué se necesita cada antecedente y qué entidad sigue, basándose en los límites del simulador y la derivación a COMPIN. No prometer un pago exacto. [Presentación SIL](https://www.suseso.gob.cl/606/w3-article-711911.html), [Compendio](https://www.suseso.cl/622/w3-propertyvalue-788701.html).
- Para William y Joseph: conservar SUSESO como referencia del patrón de seguimiento, sin presentar horas extra o finiquito como materias del simulador SIL. El alcance de las funciones observadas es de seguridad social. [Usuarios](https://www.suseso.gob.cl/606/w3-propertyvalue-610.html).
- Incorporar una revisión de antecedentes antes de confirmar y estados explicados en lenguaje cotidiano es transferible al producto. El patrón se apoya en la preparación documental y el ciclo publicado. [Reclame](https://www.suseso.gob.cl/606/w3-article-40310.html), [Ciclo](https://www.suseso.gob.cl/606/w3-propertyvalue-562466.html).

### Gaps

- El tutorial menciona crear contraseña si no se tiene ClaveÚnica; la pantalla actual reserva el acceso con contraseña a personas jurídicas. No asumir que un trabajador puede crear hoy una cuenta personal alternativa. [Tutorial](https://www.suseso.gob.cl/606/w3-propertyvalue-562466.html), [Pantalla actual](https://pae.suseso.gob.cl/pae-web/loginCiudadano).
- El HTML extraído del simulador muestra meses de 2023. Puede ser contenido inicial que cambia por JavaScript; hace falta observación visual antes de concluir que la interfaz usa fechas antiguas. [Formulario](https://www.suseso.gob.cl/606/w3-article-712302.html).
- No se verificaron usabilidad móvil, contraste, tiempos de tarea, éxito del cálculo, carga real de archivos ni pantalla de seguimiento autenticada. La extracción textual no permite afirmarlos.
- Tres pantallas para capturar: [Usuarios](https://www.suseso.gob.cl/606/w3-propertyvalue-610.html), [Orientador](https://www.suseso.gob.cl/606/w3-propertyname-509.html), [Presentación SIL](https://www.suseso.gob.cl/606/w3-article-711911.html). Alternativa transaccional pública: [Ingreso PAE](https://pae.suseso.gob.cl/pae-web/loginCiudadano).

## ¿Qué aporta ChileAtiende como referencia de información por necesidad y canal?

### Takeaway

ChileAtiende ofrece un acceso multiservicios con información sobre requisitos, pasos y canales, y ordena contenidos por temas y momentos de vida. Resulta especialmente pertinente para orientar a Joseph desde el evento de quedar sin trabajo. [Qué es](https://www.chileatiende.gob.cl/que-es-chileatiende), [Momentos de vida](https://www.chileatiende.gob.cl/momentos-de-vida).

### Cited Findings

- **Plataforma, versión y perfil:** portal web institucional para personas que buscan beneficios y servicios del Estado; lo administra IPS. No se obtuvo número de versión. Define su propuesta como información simple sobre cómo/dónde realizar trámites y requisitos. [Qué es ChileAtiende](https://www.chileatiende.gob.cl/que-es-chileatiende).
- **Acceso y funciones:** las fichas informativas son públicas; el centro de ayuda describe fichas con destinatarios, requisitos, documentos, pasos, costo, vigencia y marco legal. El portal y la orientación son gratuitos, aunque el trámite específico puede tener costo. [Centro de ayuda](https://www.chileatiende.gob.cl/ayuda/centro-de-ayuda).
- **Navegación por necesidad:** “Momentos de vida” incluye quedar sin trabajo, acceso a salud pública, tener un hijo, vivienda y jubilación. “Trabajo y cesantía” enumera servicios como finiquito e ingreso de reclamo por despido. [Momentos de vida](https://www.chileatiende.gob.cl/momentos-de-vida), [Trabajo y cesantía](https://www.chileatiende.gob.cl/temas/trabajo-y-cesantia).
- **Navegación por canal:** la red distingue atención presencial de no presencial, con sucursales, módulos, agenda, videoatención, 101 y formulario escrito. No se comprobó que todos los trámites estén disponibles en todos los canales. [Red de atención](https://www.chileatiende.gob.cl/red-de-atencion).
- **Licencia de Benjamin:** la ficha Fonasa describe gestión, consulta de estado y recurso de reposición, identifica COMPIN como institución informante y avisa al usuario antes de redirigirlo a su web. El estado se consulta con ClaveÚnica o RUT/folio en el destino. También ofrece recordatorio descargable `.ics` o guardado con ClaveÚnica. Esto documenta opciones; no fueron ejecutadas. [Ficha licencia](https://www.chileatiende.gob.cl/fichas/53052-estado-de-una-licencia-medica-solo-asegurados-de-fonasa).
- **Finiquito de Joseph:** la ficha utiliza secciones “Obtén”, “Ratifica” y “Solicita una copia”, y remite a DT/Inspección del Trabajo o notaría. La ratificación web requiere ClaveÚnica en DT; la ficha señala asesoría gratuita en Inspección. [Finiquito](https://www.chileatiende.gob.cl/fichas/33522).
- **Recorrido por evento:** “Enfrentar el despido” propone revisar el documento antes de ratificar, orienta al usuario a DT o Corporación de Asistencia Judicial ante inconsistencias y relaciona finiquito con ingresos, salud y búsqueda de empleo. [Enfrentar el despido](https://www.chileatiende.gob.cl/momentos-de-vida/Quedar%2Bsin%2Btrabajo/Revisa%2Bqu%C3%A9%2Bhacer%2Bsi%2Bquedaste%2Bsin%2Btrabajo).
- **Observación visual aportada por el coordinador:** la ficha de finiquito se abrió sin login y muestra actualización al 27 de enero de 2026, definición de causal como motivo, enlace de asesoría, acordeones y CTA fija “Ratificar finiquito”. Al expandir “Ratifica” aparecen instrucciones para Mi DT/ClaveÚnica, oficinas y notaría. Red de atención presenta tarjetas por canal; su cabecera, color y tipografía difieren de la ficha. El coordinador capturó CA01 (cabecera/CTA), CA02 (ratificación expandida) y CA03 (red de atención). [Finiquito](https://www.chileatiende.gob.cl/fichas/33522), [Red](https://www.chileatiende.gob.cl/red-de-atencion).
- **Autoridad y derivación:** las fichas identifican la entidad que proporciona información; el portal explica beneficios y conecta con canales/instituciones responsables. No inferir que ChileAtiende decide el caso laboral o emite un cálculo individualizado de indemnización. [Ficha licencia](https://www.chileatiende.gob.cl/fichas/53052-estado-de-una-licencia-medica-solo-asegurados-de-fonasa), [Qué es](https://www.chileatiende.gob.cl/que-es-chileatiende).

### Inferences

- Para Benjamin: empezar por el evento “tengo mi primera licencia”, preguntar el régimen necesario para una ruta pertinente y distinguir orientación pública de consulta del estado en COMPIN. Evitar pedir RUT o documentos médicos para una explicación general. [Ficha licencia](https://www.chileatiende.gob.cl/fichas/53052-estado-de-una-licencia-medica-solo-asegurados-de-fonasa).
- Para Joseph: un checklist de revisión antes de firmar y una derivación explícita conservan el modelo de acciones secuenciales de la ficha y el recorrido de despido. Sus ocho años de trabajo no bastan por sí solos para afirmar un monto; el producto debe reunir los antecedentes pertinentes antes de estimar. [Finiquito](https://www.chileatiende.gob.cl/fichas/33522), [Enfrentar despido](https://www.chileatiende.gob.cl/momentos-de-vida/Quedar%2Bsin%2Btrabajo/Revisa%2Bqu%C3%A9%2Bhacer%2Bsi%2Bquedaste%2Bsin%2Btrabajo).
- Para William: transferir el lenguaje por necesidad y la alternativa de atención humana. La navegación observada no demuestra una herramienta específica de cálculo de horas extra para transportistas; consultar DT como referencia temática complementaria. [Red](https://www.chileatiende.gob.cl/red-de-atencion), [Consultas DT](https://www.dt.gob.cl/portal/1628/w3-article-116464.html).

### Gaps

- El fetch directo de las páginas ChileAtiende devolvió 403; el dominio `portal` devolvió 502/no accesible. El contenido oficial indexado fue complementado con observación visual y capturas del coordinador en la ficha de finiquito y la red. No se probaron trámites, calendario, recordatorios ni formularios enviados.
- “Qué es” presenta 101 de lunes a viernes 8–18; algunas fichas muestran lunes a jueves hasta 20. No consolidar horarios en el proyecto sin verificar el canal y página vigente. [Qué es](https://www.chileatiende.gob.cl/que-es-chileatiende), [Finiquito](https://www.chileatiende.gob.cl/fichas/33522).
- No se verificó formulario de carga documental para orientación laboral dentro de ChileAtiende. La carga/presentación de antecedentes de licencia ocurre en la institución de destino según la ficha. No atribuir capacidad de analizar documentos al portal informativo. [Ficha licencia](https://www.chileatiende.gob.cl/fichas/53052-estado-de-una-licencia-medica-solo-asegurados-de-fonasa).
- Tres pantallas para capturar: [Trabajo y cesantía](https://www.chileatiende.gob.cl/temas/trabajo-y-cesantia), [Finiquito](https://www.chileatiende.gob.cl/fichas/33522), [Red de atención](https://www.chileatiende.gob.cl/red-de-atencion). Alternativa centrada en evento: [Momentos de vida](https://www.chileatiende.gob.cl/momentos-de-vida).

## ¿Cómo clasificar el ecosistema y justificar la selección?

### Takeaway

La comparación debe distinguir orientación laboral oficial, trámites de seguridad social, patrones de información pública, fuentes normativas y sustitutos conversacionales. No corresponde puntuar todas las alternativas como si cumplieran el mismo trabajo.

### Cited Findings

| Candidato bruto | Clasificación propuesta | Evidencia verificada y decisión metodológica |
|---|---|---|
| Dirección del Trabajo / Mi DT | Alternativa funcional de orientación y trámite laboral | Su centro de consultas clasifica temas laborales; Mi DT exige RUN/ClaveÚnica para trabajadores. Incluir como referencia cercana al problema. [DT](https://www.dt.gob.cl/portal/1628/w3-article-116464.html). |
| SUSESO | Análogo sectorial de preparación y seguimiento | Orientación y reclamos en seguridad social, simulador SIL y seguimiento. Incluir por correspondencia con licencias de Benjamin y patrones de proceso; no tratarlo como calculadora de finiquito/horas extra. [Usuarios](https://www.suseso.gob.cl/606/w3-propertyvalue-610.html). |
| ChileAtiende | Referencia de diseño de información y derivación | Portal multiservicios y múltiples canales. Incluir por orientación por necesidad y canales; no equiparar orientación informativa con resolución oficial del caso. [Qué es](https://www.chileatiende.gob.cl/que-es-chileatiende), [Red](https://www.chileatiende.gob.cl/red-de-atencion). |
| BCN / Ley Chile | Fuente normativa complementaria | El resultado oficial describe acceso libre a normas actualizadas y texto completo. Excluir de la matriz principal de experiencia de orientación/trámite, por foco documental; conservar para validar fuentes del producto. El fetch de la aplicación no expuso la consulta, por lo que no se afirma cómo funciona su UX. [Ley Chile](https://www.bcn.cl/leychile/Consulta/). |
| ChatGPT | Sustituto conversacional general | OpenAI reconoce errores, referencias inventadas y necesidad de verificación; documenta búsqueda con citas. Incluir para comparar conversación y confianza, sin atribuirle autoridad laboral institucional. [OpenAI](https://help.openai.com/en/articles/8313428-does-chatgpt-tell-the-truth). |

### Inferences

- Elegir DT como comparación funcional; SUSESO como análogo sectorial; ChileAtiende como referencia de diseño; ChatGPT como sustituto conductual. Mantener BCN como fuente de corroboración, sin excluir su valor informativo. Esta clasificación es una decisión del estudio, no una afirmación de mercado.
- La oportunidad del proyecto es reunir lenguaje cotidiano, fuente oficial visible, preguntas mínimas, checklist y derivación contextual. Su beneficio y usabilidad aún deben validarse con las tres personas; la presencia de estos patrones en referentes no demuestra demanda ni éxito del producto.

### Gaps

- La lista bruta no representa un censo completo de proveedores ni permite afirmar liderazgo, participación de mercado o ausencia de competidores privados. No se investigaron servicios comerciales de asesoría ni se compararon cuentas autenticadas.
- No se midieron tareas ni se entrevistó a usuarios. Las recomendaciones son hipótesis de diseño basadas en los escenarios del proyecto y en las funciones públicas documentadas.
