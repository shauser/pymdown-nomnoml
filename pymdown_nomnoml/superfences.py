import os

from subprocess import run, PIPE
from base64 import b64encode


def fence_nomnoml_svg_b64(source, language, css_class):
    """Format pymdown_nomnoml as svg (requires helper)"""

    path = os.path.realpath(os.path.join(__file__, '..', '..', 'js', 'pymdown_nomnoml.js'))

    p = run(['node', path], stdout=PIPE, input=source, encoding='utf-8')
    svg = p.stdout.encode('utf-8')

    # Encode as base64 since an inline SVG is not supported by weasyprint

    return '<img src="data:image/svg+xml;charset=utf-8;base64,' + b64encode(svg).decode('ascii') + '">'
