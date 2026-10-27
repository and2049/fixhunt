#!/bin/sh
# Tag a release. Not run by the tests.
set -e
version="$1"
[ -n "$version" ] || { echo "usage: release.sh <version>" >&2; exit 2; }
git tag -a "v$version" -m "toolbox $version"
