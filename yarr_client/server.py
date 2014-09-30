# -*- coding: utf-8 -*-

from flask import Flask, request, g, redirect, url_for, abort, \
     render_template, flash
from flask.ext.assets import Environment, Bundle


"""
Setup Flask
"""

app = Flask(__name__)

# Load config
app.config.from_object('app.config.Development')

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


"""
Routes
"""

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/search')
def search():
    return 'Search'
