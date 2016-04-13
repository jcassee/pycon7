#!/bin/sh

set -e

docker run \
    --volume "$PWD":/src:ro \
    --workdir /src \
    --tty \
    python:3.5 \
    sh -c "pip install -r requirements.txt && python manage.py behave"
