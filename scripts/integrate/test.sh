#!/bin/sh

set -e

docker run \
    --tty \
    "$IMAGE" \
    python manage.py behave --quiet --no-timings
