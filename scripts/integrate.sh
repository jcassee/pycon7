#!/bin/bash

set -e

dirname=$(dirname "$0")
cd "$dirname/.."

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
