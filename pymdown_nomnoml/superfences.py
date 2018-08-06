import os

from subprocess import run, PIPE
from base64 import b64encode


def nomnoml_to_svg(source: str) -> str:
    """Format pymdown_nomnoml as svg (requires helper)"""

    path = os.path.realpath(os.path.join(__file__, '..', 'js', 'pymdown_nomnoml.js'))

    p = run(['node', path], stdout=PIPE, input=source, encoding='utf-8')
    svg = p.stdout.encode('utf-8')

    return svg


def fence_nomnoml_svg_b64(source: str, language: str, css_class: str):
    """Format pymdown_nomnoml as svg using base64 encoded img tag (requires helper)"""

    svg = nomnoml_to_svg(source)

    # Encode as base64 since an inline SVG is not supported by weasyprint

    return '<img src="data:image/svg+xml;charset=utf-8;base64,' + b64encode(svg).decode('ascii') + '">'
