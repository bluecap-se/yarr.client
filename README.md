# Yarr! client

[![Build Status](https://travis-ci.org/bluecap-se/yarr.client.svg?branch=master)](https://travis-ci.org/bluecap-se/yarr.client)
[![Dependency Status](https://gemnasium.com/36afc2c2d60de6f5c8cbfea3142376a5.svg)](https://gemnasium.com/bluecap-se/yarr.client)
[![PyPI version](https://badge.fury.io/py/yarr.client.svg)](http://badge.fury.io/py/yarr.client)

Web client for [Yarr!](https://github.com/bluecap-se/yarr) in Python.

## Install

### Using a package manager

```console
$ pip install yarr.client
```

### From source

```console
$ git clone https://github.com/bluecap-se/yarr.client.git
$ cd yarr.client
$ pip install -r requirements.txt
$ pip install -e .
```

## Usage

### Quickstart

```console
$ yarr.client

 * Running on http://127.0.0.1:5000/
```

### Options

The configuration file params are defined in the [Flask documentation](http://flask.pocoo.org/docs/0.10/config/#builtin-configuration-values).

```console
$ yarr.client -h

Yarr.client - Web Client for Yarr!

Usage:
      yarr.client [--config FILE] [options]

Options:
  -c, --config FILE         Path to Flask config file (params: bit.ly/1uamUo1)
  -h, --help                Output this help and exit
  -v, --version             Output version and exit

Examples:
  yarr.client
  yarr.client -c /etc/production.cfg

```

## Run tests

```Bash
$ py.test
```

## License

Published under [MIT License](https://github.com/bluecap-se/yarr.client/blob/master/LICENSE).
