# -*- coding: utf-8 -*-

import pytest

from flask import url_for


def test_config(app):

    assert app.debug, 'App is in debug mode'

    assert not app.config.get('MINIFY_HTML'), 'App does minify html'

    assert app.config.get('ASSETS_DEBUG'), 'App does build assets'

    assert app.config.get('YARR_URL'), 'App doesn\'t have Yarr! URL specified'


def test_routes(client):

    assert client.get(url_for('index')).status_code == 200

    assert client.get(url_for('search')).status_code == 302, 'Empty query should throw redirect'
