#!/bin/sh

set -e

docker run \
    --tty \
    jcassee/registronavale \
    python manage.py behave --quiet --no-timings
