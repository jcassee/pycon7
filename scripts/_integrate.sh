#!/bin/bash

set -e

dirname=$(dirname "$0")
cd "$dirname/.."

section() {
  [ -z "$TRAVIS" ] || echo -en "travis_fold:start:$1\\r"
  scripts/"$1".sh
  [ -z "$TRAVIS" ] || echo -en "travis_fold:end:$1\\r"
}

section test
section docker
section ansible
section relish
