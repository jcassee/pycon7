#!/bin/sh

set -e

docker run \
    --env RELISH_API_TOKEN=$RELISH_API_TOKEN \
    --volume "$PWD":/src:ro \
    --tty \
     jcassee/relish \
     relish push
