# -*- coding: utf-8 -*-

from flask import Flask, request, g, redirect, url_for, abort, \
     render_template, flash
from flask.ext.assets import Environment, Bundle


app = Flask(__name__)


"""
Setup Flask
"""

def run_app(config):

    # Load config
    app.config.from_pyfile('defaults.cfg')
    app.config.from_pyfile(config, silent=True)

    if app.config.get('MINIFY_HTML', False):
        app.jinja_env.add_extension('jinja2htmlcompress.HTMLCompress')


    """
    Setup webassets
    """

    assets = Environment(app)

    js = Bundle('common.js', filters='closure_js', output='gen/main.%(version)s.js')
    css = Bundle('common.css', filters='cssmin', output='gen/main.%(version)s.css')

    assets.register('js_all', js)
    assets.register('css_all', css)

    app.run()


"""
Routes
"""

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/search')
def search():

    query = request.args.get('q', None)

    if not query:
        return redirect(url_for('index'))

    params = {
        'torrent_name': 'fake',
        'torrent_link': 'fake'
    }

    return render_template('search.html', **params)
