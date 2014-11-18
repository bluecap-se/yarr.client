# -*- coding: utf-8 -*-

import requests

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


def create_request(query):

    yarr_url = app.config.get('YARR_URL', False)
    if not yarr_url:
        raise('No URL to Yarr! server specified in config.')

    api_token = app.config.get('YARR_API_TOKEN', False)
    headers = {'X-API-KEY': api_token} if api_token else {}
    payload = {'q': query}
    url = '%s/search' % yarr_url

    return requests.get(url, params=payload, headers=headers)


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

    yarr_request = create_request(query)

    if yarr_request.status_code is not 200:
        return redirect(url_for('index'))

    data = yarr_request.json()

    params = {
        'torrent_name': data.get('name', 'No name'),
        'torrent_link': data.get('magnet', '')
    }

    return render_template('search.html', **params)
