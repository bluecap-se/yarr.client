# -*- coding: utf-8 -*-

"""
Main CLI entry point
"""

from docopt import docopt

from . import __doc__, __title__, __version__
from app import configurate_app


def cli(run=True):
    version = '%s %s' % (__title__, __version__)
    args = docopt(__doc__, version=version)

    config = args.get('--config') or ''

    app, host, port = configurate_app(config)

    if run:
        app.run(port=port, host=host)
