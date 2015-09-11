# Yarr! client

[![Circle CI](https://img.shields.io/circleci/project/bluecap-se/yarr.client.svg?style=flat-square)](https://circleci.com/gh/bluecap-se/yarr.client)
[![Dependency Status](https://img.shields.io/gemnasium/bluecap-se/yarr.client.svg?style=flat-square)](https://gemnasium.com/bluecap-se/yarr.client)
[![PyPI version](https://img.shields.io/pypi/v/yarr.client.svg?style=flat-square)](https://pypi.python.org/pypi/yarr.client/0.1.0)
[![Docker pulls](https://img.shields.io/docker/pulls/bluecap/yarr.client.svg?style=flat-square)](https://registry.hub.docker.com/u/bluecap/yarr.client/)

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

 * Running on http://0.0.0.0:5000/
 * Restarting with reloader
```

### Options

The configuration file params are defined in the [Flask documentation](http://flask.pocoo.org/docs/0.10/config/#builtin-configuration-values).

Additional, app-specific params are `YARR_URL` and `YARR_API_TOKEN`. `YARR_URL` is the path to the [Yarr!](https://github.com/bluecap-se/yarr)
server, and `YARR_API_TOKEN` needs to be set if the server has a corresponding token specified in its config.

```console
$ yarr.client -h

Yarr.client - Web Client for Yarr!

Usage:
      yarr.client runserver [--config FILE] [options]

Options:
  -c, --config FILE         Path to Flask config file (params: bit.ly/1uamUo1)
  -h, --help                Output this help and exit
  -v, --version             Output version and exit

Examples:
  yarr.client runserver
  yarr.client runserver -c /etc/production.cfg

```

## Run tests

```console
$ pip install -r test_requirements.txt
$ py.test
```

### Watch for changes

To run the tests continuously, run the test command with the watch or follow flag `-f`:

```console
$ py.test -f
```

### Test coverage

```console
$ coverage run --source yarr_client -m py.test
$ coverage html
$ open htmlcov/index.html
```

## License

Published under [MIT License](https://github.com/bluecap-se/yarr.client/blob/master/LICENSE).
