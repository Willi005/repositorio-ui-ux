"""Generate benchmark artifacts from local evidence."""
from pathlib import Path
from html import escape
import json
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


CAPTURES = {
'direccion-trabajo': [
 ('DT · Entry by user profile', 'https://www.dt.gob.cl/portal/1626/w3-channel.html', [(160,160,680,432,TEAL),(4,61,850,121,RUST)], ['1. Visible worker entry helps users recognize their profile.', '2. Tax credential notice appears before the worker task (H8).']),
 ('DT · Settlement explanation and requirements', 'https://www.dt.gob.cl/portal/1626/w3-article-117245.html', [(45,420,804,518,TEAL),(43,339,803,379,RUST)], ['1. Separates online and in-person procedures to support channel choice.', '2. The term for an attesting official lacks an immediate explanation (H2).']),
 ('DT · Help and legal evidence', 'https://www.dt.gob.cl/portal/1626/w3-article-117245.html', [(40,325,810,428,TEAL),(38,450,810,517,TEAL)], ['1. Consultation and phone options provide a visible route to human help.', '2. Links the relevant article, but at the end of a long information page.'])
],
'suseso': [
 ('SUSESO · Separate action and tracking', 'https://www.suseso.gob.cl/606/w3-propertyvalue-610.html', [(28,294,838,406,TEAL),(15,772,838,901,TEAL)], ['1. Filing and tracking a complaint are presented as separate tasks.', '2. The guidance tool explains its role in preparing complaint evidence.']),
 ('SUSESO · Guidance by profile', 'https://www.suseso.gob.cl/606/w3-propertyname-509.html', [(15,319,835,374,TEAL),(15,166,835,194,TEAL)], ['1. Worker guidance can be selected before the reason for the request.', '2. The visible navigation path helps identify the current location.']),
 ('SUSESO · Classify the medical leave problem', 'https://www.suseso.gob.cl/606/w3-propertyvalue-586.html', [(19,363,834,419,RUST),(765,463,852,541,RUST)], ['1. Wording about a COMPIN decision requires institutional vocabulary (H2).', '2. Text controls partly cover Back in this view (H3/H8).'])
],
'chileatiende': [
 ('ChileAtiende · Information and primary action', 'https://www.chileatiende.gob.cl/fichas/33522', [(69,348,770,390,TEAL),(1,784,846,918,RUST)], ['1. The displayed update makes the content date visible.', '2. Ratify dominates Help before the case has been verified (H5/H8).']),
 ('ChileAtiende · Choose a ratification channel', 'https://www.chileatiende.gob.cl/fichas/33522', [(105,527,744,648,TEAL),(75,411,765,499,TEAL)], ['1. Explains online access with ClaveÚnica and an in-person alternative.', '2. Task-based accordion reveals information on request.']),
 ('ChileAtiende · Service network', 'https://www.chileatiende.gob.cl/red-de-atencion', [(14,425,835,689,TEAL),(1,1,846,65,RUST)], ['1. Cards compare video, phone, and form-based service channels.', '2. Header and typography differ from the CA01 information page (H4).'])
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
            draw.text((18,43),f'{tool} · 05/10/2026 · {width}×{height} · public view',font=ImageFont.truetype(FONT,15),fill=NAVY)
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
 ('Public access without account','Labor guidance pages','Public guidance tool','Information pages','Situation-based entry','Observed baseline'),
 ('Organization by need','Role and labor topics','Profile and reason','Procedure information','Three initial situations','Observed baseline'),
 ('Human or official channel','SUAC, phone, office','Complaints and offices','Service network','Subject-based referral','Observed baseline'),
 ('Prepare supporting evidence','Settlement requirements','Complaint guidance','Task instructions','Case checklist','Documented baseline'),
 ('Basis for guidance','Article linked in page','Compendium linked*','Institution and page','Source for each claim','Varies by service'),
 ('Formal procedure status','Documented tracking*','Tracking button','Mi ChileAtiende*','External receipt only','Distinctive feature'),
 ('Benefit estimate','Outside this sample','SIL simulator*','Outside this sample','No universal calculation','Distinctive feature'),
 ('Contextual verification','Not observed integrated','Not observed integrated','Not observed integrated','Missing data + evidence','Hypothesized opportunity'),
 ('Limit for each answer','No dialogue observed','SIL declares estimate*','No dialogue observed','Explain scope','Hypothesized opportunity'),
 ('Referral summary','Not observed integrated','Evidence by reason','General instructions','Questions and next steps','Hypothesized opportunity')
]


def create_feature_map():
    content=rect(0,0,1800,1450,'#F7FAFB')+rect(0,0,1800,145,NAVY)
    content+=text_block(40,55,'Benchmark · Feature comparison map',1720,36,'#FFFFFF',True)
    content+=text_block(40,101,'Verified AI-assisted labor guidance · Three-service sample · OCT 05, 2026',1720,24,'#CDE6EE')
    widths=[380,270,270,270,270,260]
    headers=['Feature','Labor Directorate (DT)','SUSESO','ChileAtiende','Team proposal','Sample interpretation']
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
    content+=text_block(40,1279,'* Documented in official sources; authenticated flows and the simulator were not completed.',1720,23)
    content+=text_block(40,1320,'Unobserved refers only to reviewed screens; it does not establish that a feature is absent from the product.',1720,23)
    content+=text_block(40,1361,'Baseline describes this sample. Opportunities and the proposal require user and team validation.',1720,23)
    content+=text_block(40,1402,'Evidence and sources: benchmark/README.md and tabla-comparativa.md. The proposal is not yet implemented.',1720,22)
    save_svg(ROOT/'benchmark/feature-map.svg',svg_document(1800,1450,content,'Benchmark feature comparison map'))


if __name__ == '__main__':
    annotate_captures()
    create_feature_map()
    print('Generated 9 annotated captures and the benchmark feature map (SVG/PNG/PDF).')
