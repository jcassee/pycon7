#!/bin/sh

set -e

docker_image=jcassee/registronavale

docker login -e="$DOCKER_EMAIL" -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
docker build -t "$docker_image" .
docker push "$docker_image"
