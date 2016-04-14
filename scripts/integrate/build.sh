#!/bin/sh

set -e

docker build -t "$DOCKER_IMAGE" .
