"""Generate academic UX artifacts from local evidence and journey data."""
from pathlib import Path
from html import escape
import json
import subprocess
from PIL import Image, ImageDraw, ImageFont
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
FONT = '/usr/share/fonts/liberation/LiberationSans-Regular.ttf'
BOLD = '/usr/share/fonts/liberation/LiberationSans-Bold.ttf'
NAVY = '#14344A'
TEAL = '#087E8B'
RUST = '#AF492C'


def wrap(text, width, size, bold=False):
    font = ImageFont.truetype(BOLD if bold else FONT, size)
    lines = []
    line = ''
    for word in text.split():
        candidate = f'{line} {word}'.strip()
        if font.getlength(candidate) > width and line:
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    return lines


def text_block(x, y, text, width, size=23, color=NAVY, bold=False, max_lines=None):
    lines = wrap(text, width, size, bold)
    if max_lines and len(lines) > max_lines:
        raise ValueError(f'Text overflow: {text}')
    weight = '700' if bold else '400'
    return ''.join(f'<text x="{x}" y="{y+i*size*1.25}" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(line)}</text>' for i,line in enumerate(lines))


def rect(x, y, width, height, color, stroke='none', radius=0):
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{color}" stroke="{stroke}"/>'


def svg_document(width, height, content, title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img"><title>{escape(title)}</title><style>text {{font-family: Liberation Sans, Arial, sans-serif;}}</style>{content}</svg>'


def save_svg(path, svg):
    path.write_text(svg)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(path.with_suffix('.png')))
    cairosvg.svg2pdf(bytestring=svg.encode(), write_to=str(path.with_suffix('.pdf')))


def create_journey(person, phases):
    content = rect(0, 0, 1800, 1620, '#F7FAFB')
    content += rect(0, 0, 1800, 163, NAVY)
    content += text_block(40, 48, f'Customer Journey · {person["name"]}', 1700, 36, '#FFFFFF', True)
    content += text_block(40, 83, person['profile'], 1680, 24, '#CDE6EE')
    content += text_block(40, 120, person['goal'], 1680, 26, '#FFFFFF')
    content += text_block(40, 150, 'RECORRIDO PROPUESTO · HIPÓTESIS PARA VALIDAR · 05 OCT 2026', 1680, 18, '#CDE6EE')
    content += text_block(30, 198, 'EMOCIONES', 145, 19, TEAL, True)
    content += text_block(30, 237, 'Satisfacción', 145, 18)
    content += text_block(30, 413, 'Frustración', 145, 18)
    content += text_block(180, 188, 'Escala cualitativa: −2 a +2; posiciones estimadas, sin medición de usuarios.', 1570, 19)
    for value in [-2,-1,0,1,2]:
        y = 322 - value*40
        content += f'<line x1="180" y1="{y}" x2="1760" y2="{y}" stroke="#D4E0E6" stroke-dasharray="5 6"/>'
    centers = [278 + 198*i for i in range(8)]
    points = [(x,322-v*40) for x,v in zip(centers,person['emotions'])]
    content += f'<polyline points="{" ".join(f"{x},{y}" for x,y in points)}" fill="none" stroke="{TEAL}" stroke-width="5"/>'
    for i, (x,y) in enumerate(points):
        content += f'<circle cx="{x}" cy="{y}" r="10" fill="{TEAL}"/>'
        content += text_block(x-85, y-22, person['emotion_labels'][i], 185, 19, NAVY, True)
    key_x, key_y = points[person['key_index']]
    content += f'<circle cx="{key_x}" cy="{key_y}" r="19" fill="none" stroke="{RUST}" stroke-width="4"/>'
    content += text_block(180, 445, person['key'], 1580, 22, RUST, True, 1)
    content += text_block(30, 490, 'ACCIONES Y', 145, 19, TEAL, True)
    content += text_block(30, 516, 'CONTACTOS', 145, 19, TEAL, True)
    for i, point in enumerate(person['points']):
        x = 180 + 198*i
        content += rect(x, 465, 188, 375, '#FFFFFF', '#D4E0E6', 8)
        content += text_block(x+10, 489, f'{i+1}. {point[0]}', 168, 21, NAVY, True, 3)
        content += text_block(x+10, 568, point[1], 168, 19, TEAL, max_lines=5)
        content += text_block(x+10, 679, person['short_actions'][i], 168, 20, max_lines=6)
    for i,phase in enumerate(phases):
        x = 180 + i*396
        content += rect(x, 856, 386, 56, TEAL, radius=6)
        content += text_block(x+12, 891, phase, 364, 23, '#FFFFFF', True, 1)
    rows = [('VALOR', 'values', 928, 188), ('BARRERAS', 'barriers', 1132, 155), ('OPORTUNIDADES', 'opportunities', 1303, 194)]
    for title, key, y, height in rows:
        content += text_block(22, y+30, title, 152, 17, TEAL, True)
        for i,value in enumerate(person[key]):
            x=180+i*396
            content += rect(x,y,386,height,'#FFFFFF','#D4E0E6',8)
            content += text_block(x+16,y+31,value,354,23,max_lines=5 if key=='barriers' else 6)
    content += text_block(40, 1540, 'Lectura: el alivio final expresa una expectativa de control; no garantiza pago, aprobación ni resolución favorable.', 1700, 22)
    content += text_block(40, 1577, 'Adaptación de la plantilla del docente: acciones, emociones, valor, barreras, oportunidades y momento clave.', 1700, 20)
    save_svg(ROOT/'customer-journey'/f'{person["id"]}.svg',svg_document(1800,1620,content,person['goal']))


CAPTURES = {
'direccion-trabajo': [
 ('DT · Entrada por tipo de usuario', 'https://www.dt.gob.cl/portal/1626/w3-channel.html', [(160,160,680,432,TEAL),(4,61,850,121,RUST)], ['1. Acceso visible para trabajadores: permite reconocerse por perfil.', '2. Aviso de Clave Tributaria: antecede a la tarea del trabajador (H8).']),
 ('DT · Explicación y requisitos del finiquito', 'https://www.dt.gob.cl/portal/1626/w3-article-117245.html', [(45,420,804,518,TEAL),(43,339,803,379,RUST)], ['1. Distingue trámite web y presencial; permite elegir canal.', '2. «Ministro de fe» aparece sin explicación inmediata (H2).']),
 ('DT · Ayuda y fundamento normativo', 'https://www.dt.gob.cl/portal/1626/w3-article-117245.html', [(40,325,810,428,TEAL),(38,450,810,517,TEAL)], ['1. Ofrece consulta y teléfono: puente visible a atención humana.', '2. Vincula el artículo aplicable, aunque al final de la ficha extensa.'])
],
'suseso': [
 ('SUSESO · Acción y seguimiento separados', 'https://www.suseso.gob.cl/606/w3-propertyvalue-610.html', [(28,294,838,406,TEAL),(15,772,838,901,TEAL)], ['1. Reclamar y seguir un reclamo se presentan como tareas distintas.', '2. El orientador explica que prepara antecedentes para el reclamo.']),
 ('SUSESO · Orientación por perfil', 'https://www.suseso.gob.cl/606/w3-propertyname-509.html', [(15,319,835,374,TEAL),(15,166,835,194,TEAL)], ['1. Permite elegir la orientación para trabajadores antes del motivo.', '2. La ruta visible ayuda a reconocer la ubicación en el sitio.']),
 ('SUSESO · Clasificar el problema de licencia', 'https://www.suseso.gob.cl/606/w3-propertyvalue-586.html', [(19,363,834,419,RUST),(765,463,852,541,RUST)], ['1. «Pronunciada por COMPIN» exige vocabulario institucional (H2).', '2. Los controles de texto cubren parte de «Volver» en esta vista (H3/H8).'])
],
'chileatiende': [
 ('ChileAtiende · Ficha y acción principal', 'https://www.chileatiende.gob.cl/fichas/33522', [(69,348,770,390,TEAL),(1,784,846,918,RUST)], ['1. Muestra actualización: hace visible la fecha del contenido.', '2. «Ratificar» domina sobre «Ayuda» antes de verificar el caso (H5/H8).']),
 ('ChileAtiende · Elegir canal de ratificación', 'https://www.chileatiende.gob.cl/fichas/33522', [(105,527,744,648,TEAL),(75,411,765,499,TEAL)], ['1. Explica acceso web con ClaveÚnica y alternativa presencial.', '2. Acordeón por tarea: despliega la información cuando se solicita.']),
 ('ChileAtiende · Red de atención', 'https://www.chileatiende.gob.cl/red-de-atencion', [(14,425,835,689,TEAL),(1,1,846,65,RUST)], ['1. Tarjetas comparan videoatención, teléfono y formulario por canal.', '2. Cabecera y tipografía cambian respecto de la ficha CA01 (H4).'])
]}


def annotate_captures():
    manifest=[]
    for tool,items in CAPTURES.items():
        for i,(title,url,boxes,comments) in enumerate(items,1):
            original=ROOT/'benchmark/capturas'/tool/f'{i:02}-original.jpg'
            source=Image.open(original).convert('RGB')
            width,height=source.size
            result=Image.new('RGB',(width,height+145),'#F7FAFB')
            result.paste(source,(0,72))
            draw=ImageDraw.Draw(result)
            draw.text((18,11),title,font=ImageFont.truetype(BOLD,22),fill=NAVY)
            draw.text((18,43),f'{tool} · 05/10/2026 · {width}×{height} · vista pública',font=ImageFont.truetype(FONT,15),fill=NAVY)
            for number,(left,top,right,bottom,color) in enumerate(boxes,1):
                draw.rectangle((left,top+72,right,bottom+72),outline=color,width=4)
                draw.ellipse((left+3,top+75,left+29,top+101),fill=color)
                draw.text((left+11,top+78),str(number),font=ImageFont.truetype(BOLD,18),fill='white')
            for j,comment in enumerate(comments):
                if len(wrap(comment,width-36,16))>1:
                    raise ValueError(f'Caption overflow {comment}')
                draw.text((18,height+86+j*24),comment,font=ImageFont.truetype(FONT,16),fill=NAVY)
            path=original.with_name(f'{i:02}-anotada.png')
            result.save(path)
            manifest.append({'id':f'{tool}-{i:02}','url':url,'date':'2026-10-05','viewport':[width,height],'original':str(original.relative_to(ROOT)),'annotated':str(path.relative_to(ROOT)),'comments':comments})
    (ROOT/'benchmark/capturas/registro.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')


FEATURES = [
 ('Consulta pública sin cuenta','Consulta y ficha laboral','Orientador público','Ficha informativa','Entrada por situación','Estándar observado'),
 ('Organización por necesidad','Rol y temas laborales','Perfil y motivo','Ficha por trámite','Tres situaciones iniciales','Estándar observado'),
 ('Canal humano u oficial','SUAC, teléfono, oficina','Reclamo y oficinas','Red de atención','Destino según materia','Estándar observado'),
 ('Preparar antecedentes','Requisitos del finiquito','Orientador del reclamo','Instrucciones por tarea','Checklist del caso','Estándar documentado'),
 ('Fundamento de la orientación','Artículo en ficha DT','Compendio vinculado*','Institución y ficha','Fuente por afirmación','Implementación variable'),
 ('Estado de una gestión formal','Seguimiento documentado*','Botón seguimiento','Mi ChileAtiende*','Solo comprobante externo','Diferenciadora'),
 ('Estimación de un beneficio','Fuera de esta muestra','Simulador SIL*','Fuera de esta muestra','Sin cálculo universal','Diferenciadora'),
 ('Verificación contextual','No observada integrada','No observada integrada','No observada integrada','Datos faltantes + respaldo','Oportunidad hipotética'),
 ('Límite en cada respuesta','No observado conversacional','SIL declara estimación*','No observado conversacional','Explicación de alcance','Oportunidad hipotética'),
 ('Resumen para derivación','No observado integrado','Antecedentes por motivo','Instrucciones generales','Preguntas y pendientes','Oportunidad hipotética')
]


def create_feature_map():
    content=rect(0,0,1800,1450,'#F7FAFB')+rect(0,0,1800,145,NAVY)
    content+=text_block(40,55,'Benchmark · Mapa comparativo de funcionalidades',1720,36,'#FFFFFF',True)
    content+=text_block(40,101,'Orientación laboral con IA verificada · Muestra de tres herramientas · 05 OCT 2026',1720,24,'#CDE6EE')
    widths=[380,270,270,270,270,260]
    headers=['Funcionalidad','Dirección del Trabajo','SUSESO','ChileAtiende','Propuesta del grupo','Lectura de la muestra']
    x=40
    for width,header in zip(widths,headers):
        content+=rect(x,175,width,75,TEAL)
        content+=text_block(x+12,205,header,width-24,22,'#FFFFFF',True,max_lines=2)
        x+=width
    for i,row in enumerate(FEATURES):
        x=40;y=250+98*i
        color='#FFFFFF' if i%2==0 else '#EAF1F4'
        for j,(width,cell) in enumerate(zip(widths,row)):
            content+=rect(x,y,width,98,color,'#D4E0E6')
            content+=text_block(x+12,y+29,cell,width-24,23,TEAL if j==4 else NAVY,j==0,max_lines=3)
            x+=width
    content+=text_block(40,1279,'* Función documentada en fuentes oficiales; no se completó el flujo autenticado ni el simulador.',1720,23)
    content+=text_block(40,1320,'«No observada» se limita a las pantallas revisadas: no demuestra que una función no exista en el producto.',1720,23)
    content+=text_block(40,1361,'«Estándar» describe esta muestra. Oportunidades y propuesta requieren validación con usuarios y con el equipo.',1720,23)
    content+=text_block(40,1402,'Trazabilidad y fuentes: benchmark/README.md y tabla-comparativa.md. La propuesta todavía no está implementada.',1720,22)
    save_svg(ROOT/'benchmark/feature-map.svg',svg_document(1800,1450,content,'Mapa comparativo de funcionalidades del benchmarking'))


def create_journey_docs(data):
    for person in data['people']:
        lines=[f'# Customer Journey de {person["name"]}', '', f'**Perfil:** {person["profile"]}.', '', f'**Objetivo:** {person["goal"]}', '', f'**Escenario:** {person["scenario"]}', '', '**Tipo:** recorrido propuesto (to-be), construido a partir de la persona UX y del Canvas; hipótesis, no registro de una sesión ni entrevista. Uso del celular, canales y secuencia requieren validación.', '', f'![Mapa de {person["name"]}]({person["id"]}.png)', '', f'[PDF]({person["id"]}.pdf) · [SVG editable]({person["id"]}.svg)', '', '## Recorrido y puntos de contacto', '', '| Fase | Contacto | Canal y dispositivo | Acción del usuario | Fricción | Emoción estimada |', '| --- | --- | --- | --- | --- | --- |']
        for i,point in enumerate(person['points']):
            lines.append(f'| {data["phases"][i//2]} | {i+1}. {point[0]} | {point[1]} | {point[2]} | {point[3]} | {person["emotion_labels"][i]} ({person["emotions"][i]:+d}) |')
        lines += ['', '## Valor, barreras y oportunidades', '', '| Fase | Valor esperado y propuesto | Barrera | Oportunidad |', '| --- | --- | --- | --- |']
        for i,phase in enumerate(data['phases']):
            lines.append(f'| {phase} | {person["values"][i]} | {person["barriers"][i]} | {person["opportunities"][i]} |')
        lines += ['', '## Momento clave', '', person['key'], '', '## Qué validar', '', person['validation'], '', 'Observar comprensión, elección de canal, datos compartidos y reacción a la incertidumbre. Contrastar la curva con el relato de participantes; no usar los valores emocionales como métricas reales.', '', '## Trazabilidad', '', '[Personas UX](../README.md) · [Canvas de valor](../value_proposition.png) · [Benchmark y fuentes oficiales](../benchmark/README.md) · [Criterios y adaptación de la plantilla](README.md).', '']
        (ROOT/'customer-journey'/f'{person["id"]}.md').write_text('\n'.join(lines))
    subprocess.run(['pdfunite',*[str(ROOT/'customer-journey'/f'{p["id"]}.pdf') for p in data['people']],str(ROOT/'customer-journey/customer-journeys.pdf')],check=True)


if __name__=='__main__':
    data=json.loads((ROOT/'customer-journey/journeys.json').read_text())
    annotate_captures()
    create_feature_map()
    for person in data['people']:
        create_journey(person,data['phases'])
    create_journey_docs(data)
    print('Generated 9 annotated captures, feature map and 3 journeys (SVG/PNG/PDF/Markdown).')
