# -*- coding: utf-8 -*-

import requests

from flask import Flask, request, redirect, url_for, render_template
from flask.ext.assets import Environment, Bundle

app = Flask(__name__)


"""
Setup Flask app
"""


def configurate_app(config_file=''):
    """
    Configures Flask app

    :param config_file: Absolute path to Py config file, optional
    :returns: App object, host and port
    """
    # Load config
    app.config.from_pyfile('defaults.cfg')
    app.config.from_pyfile(config_file, silent=True)

    if app.config.get('MINIFY_HTML', False):
        app.jinja_env.add_extension('flask_utils.jinja2htmlcompress.HTMLCompress')

    # Setup web assets
    assets = Environment(app)

    js = Bundle('common.js', filters='closure_js', output='gen/main.%(version)s.js')
    css = Bundle('common.css', filters='cssmin', output='gen/main.%(version)s.css')

    assets.register('js_all', js)
    assets.register('css_all', css)

    # Set host and port
    port = app.config.get('PORT', 5000)
    host = app.config.get('HOST', '127.0.0.1')

    return app, host, port


def create_request(query):
    """
    Creates a GET request to Yarr! server

    :param query: Free-text search query
    :returns: Requests object
    """
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
        'torrent_name': data.get('name', 'None found'),
        'torrent_link': data.get('magnet', '')
    }

    return render_template('search.html', **params)
