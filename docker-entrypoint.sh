#!/bin/bash

set -e

if [ "$1" = 'runserver' ]; then
    exec yarr.client "$@"
fi

exec "$@"
