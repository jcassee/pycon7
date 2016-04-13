#!/bin/sh

docker login -e="$DOCKER_EMAIL" -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
docker build -t "$DOCKER_IMAGE" .
docker push "$DOCKER_IMAGE"
