#!/bin/bash
set -e

check_version_changes(){
    git diff  HEAD^ HEAD -- aiolambda/__init__.py | grep --quiet +__version__;
};

if ! check_version_changes; then
    echo "Not version changed"
    exit
fi
VERSION=$(grep version aiolambda/__init__.py | cut -d= -f2 | tr -d '[:space:]'| tr -d "'")

git tag -a $VERSION -m "version $VERSION"
git push --follow-tags "https://$GITHUB_TOKEN@github.com/$TRAVIS_REPO_SLUG" HEAD:$TRAVIS_BRANCH
