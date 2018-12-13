#!/bin/bash
set -e

check_version_changes(){
    git diff  HEAD^ HEAD -- aiolambda/__init__.py | grep --quiet +__version__;
};

if ! check_version_changes; then
    echo "Not version changed"
    exit
fi
VERSION=$(python -c 'import aiolambda; print(aiolambda.__version__)')

git tag -a $VERSION -m "version $VERSION"
git push "https://$GITHUB_TOKEN@github.com/$TRAVIS_REPO_SLUG" $VERSION
