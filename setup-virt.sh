#!/bin/bash

# Get the absolute path to this script and move ourselves there to start
    DIR="`dirname \"$0\"`"
    DIR="`cd \"$DIR\" && pwd -P`"
    cd "$DIR"

# Return the first program from the argument list that exists in the execution path
  find_program() {
    for file in $*; do
      if which "$file" &>/dev/null; then
        echo "$file"
        return
      fi
    done
  }

# Clean up anything old
    rm -rf lib64 include bin build lib/python2.7/

# Rebuild the virtualenv
    VIRTUALENV=`find_program virtualenv-2.7 virtualenv`
    cd ..
    $VIRTUALENV --no-site-packages --distribute `basename "$DIR"`
    if [[ $? != 0 ]]; then
        echo "Command failed at line:  $LINENO"
        exit
    fi
    # Would be nice if we could just use this but it doesn't work as well as
    # it should -- and for now creates more trouble than it's worth.
    #$VIRTUALENV --relocatable `basename "$DIR"`
    cd "$DIR"

# Source the local environment
    source bin/activate
    if [[ $? != 0 ]]; then
        echo "Command failed at line:  $LINENO"
        exit
    fi

# Package install

    # Issues with pyes setup.py mean this needs to be installed manually first.
    pip install --upgrade requests

    # Required
    PKG="flask flask-sqlalchemy"
    PKG="$PKG alembic"
    PKG="$PKG psycopg2"
    #PKG="$PKG git+git://github.com/pythonforfacebook/facebook-sdk.git"

    # Packages to help development
    PKG="$PKG ipython"

    # Do the install/upgrade, grouping everything onto a single CLI call so
    # that pip only has to build shared dependencies once.
    pip install --upgrade $PKG
    if [[ $? != 0 ]]; then
        echo "Command failed at line:  $LINENO"
        exit
    fi
