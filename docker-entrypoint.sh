#!/bin/bash

set -e

if [ "$1" = 'runserver' ]; then
    exec yarr.client "$@" --config /yarr.config.cfg
fi

exec "$@"
