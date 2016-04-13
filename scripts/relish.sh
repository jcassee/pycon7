#!/bin/sh

set -e

gem install relish
echo "api_token: $RELISH_TOKEN" > ~/.relish
relish push
