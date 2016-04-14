#!/bin/sh

set -e

docker tag --force jcassee/registronavale jcassee/registronavale:"$TAG"
docker push jcassee/registronavale:"$TAG"
