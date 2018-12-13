#!/bin/bash
set -e

if [ -z "${WORKON_HOME}" ]; then
    PYTHON='python3'
else
    PYTHON=${WORKON_HOME}/aiolambda/bin/python3
fi


check_version_changes(){
    git diff  HEAD^ HEAD -- aiolambda/__init__.py | grep --quiet +__version__;
};

if ! check_version_changes; then
    echo "Not version changed"
    exit
fi
VERSION=$(${PYTHON} -c 'import aiolambda; print(aiolambda.__version__)')

git tag -a $VERSION -m "version $VERSION"
git push --follow-tags "https://$GITHUB_TOKEN@github.com/$TRAVIS_REPO_SLUG" HEAD:$TRAVIS_BRANCH
