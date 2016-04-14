#!/bin/sh

set -e

docker run \
    --tty \
    "$DOCKER_IMAGE" \
    python manage.py behave --quiet --no-timings
