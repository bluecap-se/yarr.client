#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yarr_client

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


setup(
    name=yarr_client.__title__,
    description='Web-based client for Yarr!',
    long_description=readme,
    version=yarr_client.__version__,
    author_email='hello@bluecap.se',
    url='https://github.com/bluecap-se/yarr.client',
    license=license,
    zip_safe=False,
    packages=['yarr_client'],
    scripts=['bin/yarr.client']
)
