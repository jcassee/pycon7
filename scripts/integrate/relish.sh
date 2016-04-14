#!/bin/sh

set -e

if [ "$DOCKER_TAG" = "latest" ]; then
  docker run \
      --env RELISH_API_TOKEN=$RELISH_API_TOKEN \
      --volume "$PWD":/src:ro \
      --tty \
       jcassee/relish \
       relish push
else
  echo "Not building latest tag, skipping Relish docs."
fi
