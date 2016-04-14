#!/bin/sh

set -e

# Determine repository tag
if [ "$TRAVIS_PULL_REQUEST" -a "$TRAVIS_PULL_REQUEST" != "false" ]; then
  tag="pr$TRAVIS_PULL_REQUEST"
elif [ "$TRAVIS_BRANCH" ]; then
  tag="$TRAVIS_BRANCH"
else
  tag=$(git rev-parse --abbrev-ref HEAD)
fi
if [ "$tag" = "master" ]; then
  tag="latest"
fi

docker tag --force jcassee/registronavale jcassee/registronavale:"$tag"
docker push jcassee/registronavale:"$tag"
