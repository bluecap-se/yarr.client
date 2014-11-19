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


setup(
    name=yarr_client.__title__,
    description='Web-based client for Yarr!',
    long_description=readme,
    version=yarr_client.__version__,
    author='bluecap-se',
    author_email='hello@bluecap.se',
    url='https://github.com/bluecap-se/yarr.client',
    license=yarr_client.__license__,
    zip_safe=False,
    platforms='any',
    packages=['yarr_client'],
    scripts=['bin/yarr.client'],
    keywords=['yarr', 'the pirate bay', 'web based', 'client'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2 :: Only",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search"
    ]
)
