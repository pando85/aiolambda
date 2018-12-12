#!/bin/bash
set -e

check_version_changes(){
    git diff  HEAD^ HEAD -- aiolambda/__init__.py | grep +__version__;
};

check_version_changes
VERSION=$(python -c 'import aiolambda; print(aiolambda.__version__)')

git tag -a $VERSION -m "version $VERSION"
git push --follow-tags "https://$GITHUB_TOKEN@github.com/$TRAVIS_REPO_SLUG" HEAD:$TRAVIS_BRANCH
