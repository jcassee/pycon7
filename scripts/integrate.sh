#!/bin/bash

set -e

dirname=$(dirname "$0")
cd "$dirname/.."

# Determine repository tag
if [ "$TRAVIS_PULL_REQUEST" -a "$TRAVIS_PULL_REQUEST" != "false" ]; then
  DOCKER_TAG="pr$TRAVIS_PULL_REQUEST"
elif [ "$TRAVIS_BRANCH" ]; then
  DOCKER_TAG="$TRAVIS_BRANCH"
else
  DOCKER_TAG=$(git rev-parse --abbrev-ref HEAD)
fi
if [ "$DOCKER_TAG" = "master" ]; then
  DOCKER_TAG="latest"
fi

DOCKER_IMAGE="jcassee/registronavale.com:$DOCKER_TAG"
export DOCKER_TAG DOCKER_IMAGE
echo "########## Building $DOCKER_IMAGE ##########"

i=0
section() {
  [ -z "$TRAVIS" ] || echo -en "travis_fold:start:$1\\r"
  i=$((i+1))
  echo "---------- Step $i: $1 ----------"
  scripts/integrate/"$1".sh
  [ -z "$TRAVIS" ] || echo -en "travis_fold:end:$1\\r"
}

section setup
section build
section test
section publish
section deploy
section relish
