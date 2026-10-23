"""Generate the navigation flow diagram from the wireframed structure."""
from pathlib import Path
from html import escape
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'structure'
FONT_STACK = 'Liberation Sans, Arial, sans-serif'
INK = '#1F2933'
MUTED = '#6B7A85'
LINE = '#9AA7B0'
PROPOSAL = '#B4532A'
SECTION, SCREEN, STEP = '#FFD12E', '#E2CCFF', '#FFC7C2'

WIDTH, HEIGHT = 1200, 850
BOX_WIDTH, BOX_HEIGHT, GAP = 250, 52, 32
COLUMNS = {'assistant': 220, 'profile': 600, 'privacy': 980}
SECTIONS = [
    ('assistant', 'My assistant'),
    ('profile', 'My work profile'),
    ('privacy', 'Privacy and data'),
]

# Each chain reads top to bottom: (label, fill, proposed). Labels follow the wireframes.
CHAINS = {
    'assistant': [
        ('Choose a topic or ask', SCREEN, False),
        ('Attach a document (optional)', STEP, False),
        ('Conversation', SCREEN, False),
        ('Read the cited answer', STEP, False),
        ('Open the source (external)', STEP, False),
        ('Referral to the Labor Directorate', STEP, True),
    ],
    'profile': [
        ('Work history form', SCREEN, False),
        ('Fill in the current job', STEP, False),
        ('Fill in the contract terms', STEP, False),
        ('Describe what to resolve', STEP, False),
        ('Save or clear the profile', STEP, False),
    ],
    'privacy': [
        ('Privacy policy', SCREEN, False),
        ('Switch session history', STEP, False),
        ('Delete all session data', STEP, False),
        ('Go to my assistant', STEP, False),
    ],
}


def text(x, y, label, size=15, weight='600', fill=INK, anchor='middle'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{FONT_STACK}" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}">{escape(label)}</text>')


def box(center, top, label, fill, width=BOX_WIDTH, proposed=False):
    stroke = f' stroke="{PROPOSAL}" stroke-width="2.5" stroke-dasharray="7 5"' if proposed else ''
    return (f'<rect x="{center - width / 2}" y="{top}" width="{width}" height="{BOX_HEIGHT}" rx="3" fill="{fill}"{stroke}/>'
            + text(center, top + BOX_HEIGHT / 2 + 5.5, label))


def connector(path, arrow=True):
    marker = ' marker-end="url(#arrow)"' if arrow else ''
    return f'<path d="{path}" fill="none" stroke="{LINE}" stroke-width="2"{marker}/>'


def legend(top):
    items = [(SECTION, 'Main section', False), (SCREEN, 'Screen', False),
             (STEP, 'Step or action', False), (STEP, 'Proposed, not in the wireframes', True)]
    widths = [150, 120, 160, 280]
    x = (WIDTH - sum(widths)) / 2
    parts = []
    for (fill, label, proposed), width in zip(items, widths):
        stroke = f' stroke="{PROPOSAL}" stroke-width="2" stroke-dasharray="5 3"' if proposed else ''
        parts.append(f'<rect x="{x}" y="{top}" width="22" height="14" rx="2" fill="{fill}"{stroke}/>')
        parts.append(text(x + 32, top + 12, label, size=14, weight='400', fill=MUTED, anchor='start'))
        x += width
    return ''.join(parts)


def build_svg():
    parts = [f'<rect width="{WIDTH}" height="{HEIGHT}" fill="#FFFFFF"/>', box(600, 30, 'Onboarding', SECTION, width=300)]
    for key, label in SECTIONS:
        parts.append(box(COLUMNS[key], 150, label, SECTION))

    parts.append(connector('M600 86 V150'))
    for target in (COLUMNS['assistant'], COLUMNS['privacy']):
        side = 1 if target > 600 else -1
        parts.append(connector(f'M600 86 V104 Q600 118 {600 + side * 14} 118 H{target - side * 14} Q{target} 118 {target} 132 V150'))

    # The line between sections stands for the sidebar shown on every app screen.
    for start, end in ((345, 475), (725, 855)):
        parts.append(connector(f'M{start} 178 H{end}', arrow=False))
        parts.append(text((start + end) / 2, 168, 'sidebar', size=12.5, weight='400', fill=MUTED))

    for key, items in CHAINS.items():
        center, top = COLUMNS[key], 270
        parts.append(connector(f'M{center} 206 V{top}'))
        for index, (label, fill, proposed) in enumerate(items):
            parts.append(box(center, top, label, fill, proposed=proposed))
            if index < len(items) - 1:
                parts.append(connector(f'M{center} {top + BOX_HEIGHT} V{top + BOX_HEIGHT + GAP}'))
            top += BOX_HEIGHT + GAP

    parts.append(legend(HEIGHT - 52))
    description = ('Navigation structure of Justiciano. The onboarding page leads to three sections, '
                   'My assistant, My work profile and Privacy and data, linked by the sidebar.')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-label="{description}">'
            f'<title>Justiciano navigation flow</title>'
            f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="#8C99A3"/></marker></defs>'
            + ''.join(parts) + '</svg>')


if __name__ == '__main__':
    OUTPUT.mkdir(exist_ok=True)
    svg = build_svg()
    (OUTPUT / 'navigation-flow.svg').write_text(svg + '\n')
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(OUTPUT / 'navigation-flow.png'), scale=2)
    print('Generated the navigation flow diagram (SVG/PNG).')
