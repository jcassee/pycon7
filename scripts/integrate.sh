#!/bin/bash

set -e

dirname=$(dirname "$0")
cd "$dirname/.."

section() {
  [ -z "$TRAVIS" ] || echo -en "travis_fold:start:$1\\r"
  scripts/integrate/"$1".sh
  [ -z "$TRAVIS" ] || echo -en "travis_fold:end:$1\\r"
}

section setup
section build
section test
section publish
section deploy
section relish
