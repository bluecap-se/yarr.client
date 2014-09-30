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
$ pip install --pre -r requirements.txt
$ pip install -e .
```

## Usage

### Quickstart

```console
$ yarr.client

Server started on localhost:8080
```

### Options

```console
$ yarr.client -h

Yarr.client - Web Client for Yarr!

Usage:
      yarr.client [--config TYPE] [options]
      yarr.client [--host HOST] [--port PORT] [options]

Options:
  -c --config TYPE          Production or testing, defaults to development
  --host HOST               Server listen on host
  --port PORT               Server listen on port
  -h, --help                Output this help and exit
  -v, --version             Output version and exit

Examples:
  yarr.client -c production
  yarr.client --host=localhost --port=8099

```

## Run tests

```Bash
$ py.test
```
