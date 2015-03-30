#!/bin/bash

#TERMINATE ON ERRORS
set -e

# ------------------
# Absolute path to this script. /home/user/bin/foo.sh
SCRIPT=$(readlink -f $0)
# Absolute path this script is in. /home/user/bin
SCRIPTPATH=`dirname $SCRIPT`

cd $SCRIPTPATH
git checkout develop
cd $SCRIPTPATH/github.com/actor-framework
git checkout develop
cd $SCRIPTPATH