#!/usr/bin/env sh
# Publish the current HEAD tree to the submission repository as a single commit.
# Development stays in fixhunt-dev (origin); and2049/fixhunt (public remote) only ever holds one squashed commit.
set -eu
cd "$(dirname "$0")/.."
[ -z "$(git status --porcelain --untracked-files=no)" ] || { echo "commit or stash your changes first" >&2; exit 1; }
tree=$(git rev-parse HEAD^{tree})
commit=$(git commit-tree "$tree" -m "upload project")
git push --force public "$commit:refs/heads/main"
echo "published $commit (tree of $(git rev-parse --short HEAD)) to public/main"
