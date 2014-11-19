# -*- coding: utf-8 -*-

import pytest
from yarr_client.app import configurate_app


@pytest.fixture
def app():
    app, _, _ = configurate_app()
    return app
