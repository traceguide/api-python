#!/usr/bin/env bash

PYTHONDIR=$GOPATH/../python

CYAN='\033[1;36m'
NOCOLOR='\033[0m'
function println {
    echo -e "${CYAN}$1${NOCOLOR}"
}

# Make a one-off copy that we'll push without history and with
# some files dropped to the public repo
pushd $PYTHONDIR
println "Cloning public repo..."
git clone git@github.com:traceguide/api-python

println "Overlaying current source from reslabs..."
cp -RH instrument/ api-python/

# The set of files in the published repo is not quite the same.
#
# For example:
# - We do want the generated thrift files to be there
# - We do not want our internal build stuff making this repo look
#   more complicated than it is.

println "Modifying one-off with slight file variations..."
pushd api-python
rm traceguide/crouton/.gitignore
rm -rf docs/
rm -rf sample/
rm -rf scripts/
rm -rf tests/
rm rbuildfile.js
rm pylintrc
rm setup.cfg
rm tox.ini
rm BUILD.md


# Clean repo commit
println "Publishing to public repo..."
git add .
git add -u
git commit -m "Automated commit"

# Use a distinct remote name to reduce chance of errors
git remote add api-python-origin git@github.com:traceguide/api-python
git push -u api-python-origin master
popd

# Clean-up the temp copy
println "Cleaning up one-off copy..."
rm -rf api-python

# Let slack know about it
if which curl > /dev/null; then
    curl --data "${USER} published a new revision of the python instrumentation lib to https://github.com/traceguide/api-python" $'https://reslabs.slack.com/services/hooks/slackbot?token=eez50tsY4wc8GHutnyHbX3KG&channel=%23deploy'
fi

println "Done."
popd
