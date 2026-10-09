"""Render the Markdown benchmark and comparison tables as standalone HTML."""
from pathlib import Path
import base64
import re
import markdown

ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT/'benchmark'


def render_markdown(path):
    content = markdown.markdown(path.read_text(), extensions=['tables', 'fenced_code'])
    def embed_image(match):
        target = (path.parent / match.group(1)).resolve()
        mime = 'image/png' if target.suffix == '.png' else 'image/jpeg'
        encoded = base64.b64encode(target.read_bytes()).decode()
        return f'src="data:{mime};base64,{encoded}"'
    content = re.sub(r'src="([^\"]+)"', embed_image, content)
    content = re.sub(r'<p>(<img[^>]+>)</p>\s*<p><em>(.*?)</em></p>',r'<figure>\1<figcaption>\2</figcaption></figure>',content,flags=re.S)
    content = re.sub(r'<p>(<img[^>]+>)\s*<em>(.*?)</em></p>',r'<figure>\1<figcaption>\2</figcaption></figure>',content,flags=re.S)
    return content


CSS = '''
@page {size: A4; margin: 16mm 17mm 17mm;
 @bottom-left {content: "UFRO · Human-Computer Interface Design · OCT 05, 2026"; font-size: 8pt; color:#53717E;}
 @bottom-right {content: counter(page); font-size: 8pt; color:#53717E;}}
@page comparison {size: A3 landscape; margin:16mm;
 @bottom-left {content:"Benchmark · Comparison matrix · Proposal pending validation"; font-size:8pt;}
 @bottom-right {content:counter(page);font-size:8pt;}}
body {font: 10.5pt/1.48 "Liberation Sans", sans-serif; color:#14344A;}
h1 {font-size:27pt;line-height:1.15;color:#14344A;margin:0 0 7mm;}
h2 {font-size:17pt;line-height:1.2;color:#087E8B;margin:8mm 0 4mm;break-after:avoid;}
h3 {font-size:13pt; color:#087E8B; break-after:avoid;}
a {color:#087E8B;overflow-wrap:anywhere;}
p {margin:0 0 4mm;orphans:3;widows:3;}
figure {break-before:page;break-after:page;break-inside:avoid;margin:0;text-align:center;}
figure img {display:block;width:176mm;height:auto;margin:0 auto;}
figcaption {font-size:9pt;text-align:left;margin-top:3mm;color:#53717E;}
table {width:100%;border-collapse:collapse;table-layout:fixed;margin:5mm 0;font-size:8.5pt;line-height:1.28;}
th {background:#14344A;color:white;text-align:left;}
th,td {border:0.3mm solid #D4E0E6;padding:2.3mm;vertical-align:top;overflow-wrap:anywhere;}
tr:nth-child(even) td {background:#F0F5F7;}
thead {display:table-header-group;}
tr {break-inside:avoid;}
.comparison {page:comparison;break-before:page;}
.comparison h1 {font-size:24pt;}
.comparison h2 {break-before:page;}
.comparison table {font-size:9.5pt;line-height:1.3;}
.comparison td:first-child {font-weight:bold;color:#087E8B;}
@media screen {body {max-width:1150px;margin:35px auto;padding:30px;background:white;}
html {background:#EDF3F6;}figure{margin:35px 0;}figure img {width:100%;max-width:866px;height:auto;}
.comparison {margin-top:50px;}table {font-size:13px;}.comparison table{font-size:13px;}}
'''

if __name__ == '__main__':
    report = render_markdown(BENCHMARK/'README.md')
    matrix = render_markdown(BENCHMARK/'tabla-comparativa.md')
    document=f'<!DOCTYPE html><html lang="en"><meta charset="UTF-8"><title>Labor guidance benchmark</title><style>{CSS}</style><body><main>{report}</main><section class="comparison">{matrix}</section></body></html>'
    (BENCHMARK/'benchmark.html').write_text(document)
    print('Generated standalone benchmark HTML. Build the APA PDF with scripts/build_benchmark.py.')
