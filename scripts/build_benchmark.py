"""Compile the editable LaTeX benchmark and publish its validated PDF."""
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'benchmark' / 'latex'
DESTINATION = ROOT / 'benchmark' / 'benchmark.pdf'


def build_report():
    if shutil.which('pdflatex') is None:
        raise SystemExit('pdflatex is required to build the benchmark.')
    with tempfile.TemporaryDirectory(prefix='ui-ux-benchmark-') as directory:
        output = Path(directory)
        previous_state = None
        for attempt in range(4):
            result = subprocess.run(
                ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                 '-file-line-error', f'-output-directory={output}', 'main.tex'],
                cwd=SOURCE, capture_output=True, text=True, errors='replace',
            )
            log = (output / 'main.log').read_text(errors='replace')
            if result.returncode:
                raise SystemExit(result.stdout[-5000:])
            state = tuple((output / f'main.{suffix}').read_bytes()
                          for suffix in ('aux', 'out'))
            if state == previous_state:
                break
            previous_state = state
        else:
            raise SystemExit('Cross-references did not stabilize after four passes.')
        if re.search(r'undefined|Rerun to get cross-references', log, re.I):
            raise SystemExit('Unresolved references remain in the LaTeX report.')
        overflows = [float(value) for value in re.findall(
            r'Overfull \\[hv]box \(([\d.]+)pt too (?:wide|high)\)', log)]
        if any(value > 1 for value in overflows):
            raise SystemExit(f'Material layout overflow: {overflows}')
        shutil.copyfile(output / 'main.pdf', DESTINATION)
        pages = re.search(r'Output written on .*?\((\d+) pages', log)
        print(f'Built {DESTINATION.relative_to(ROOT)} '
              f'({pages.group(1) if pages else "unknown"} pages; '
              f'{attempt + 1} compilation passes).')


if __name__ == '__main__':
    build_report()
