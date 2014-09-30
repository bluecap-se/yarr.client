#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as f:
    readme = f.read()
with open('HISTORY.md') as f:
    history = f.read()
with open('LICENSE') as f:
    license = f.read()

VERSION = '0.0.1'

setup(
    name='yarr.client',
    description='Web-based client for Yarr!',
    long_description=readme,
    version=VERSION,
    author_email='hello@bluecap.se',
    url='https://github.com/bluecap-se/yarr.client',
    license=license,
    zip_safe=False
)
