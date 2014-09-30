# -*- coding: utf-8 -*-

class Config(object):
    DEBUG = False
    ASSETS_DEBUG = False
    TESTING = False
    SECRET_KEY = 'PmwGsaKKA14hqgpzbvgK+txDEiw='
    MINIFY_HTML = False

class Production(Config):
    MINIFY_HTML = True

class Development(Config):
    DEBUG = True
    ASSETS_DEBUG = True

class Testing(Config):
    TESTING = True
