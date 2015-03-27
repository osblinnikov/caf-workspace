#!/bin/bash

# ------------------
# Absolute path to this script. /home/user/bin/foo.sh
SCRIPT=$(readlink -f $0)
# Absolute path this script is in. /home/user/bin
SCRIPTPATH=`dirname $SCRIPT`

#COPY BUILD FILES REQUIRED FOR SNOCS
cp $SCRIPTPATH/actor-framework-snocs/libcaf_core_SNocscript.py $SCRIPTPATH/github.com/actor-framework/libcaf_core/SNocscript.py 
cp $SCRIPTPATH/actor-framework-snocs/libcaf_io_SNocscript.py $SCRIPTPATH/github.com/actor-framework/libcaf_io/SNocscript.py
cp $SCRIPTPATH/actor-framework-snocs/libcaf_opencl_SNocscript.py $SCRIPTPATH/github.com/actor-framework/libcaf_opencl/SNocscript.py
cp $SCRIPTPATH/actor-framework-snocs/libcaf_riac_SNocscript.py $SCRIPTPATH/github.com/actor-framework/libcaf_riac/SNocscript.py
cp $SCRIPTPATH/actor-framework-snocs/nexus_SNocscript.py $SCRIPTPATH/github.com/actor-framework/nexus/SNocscript.py
cp $SCRIPTPATH/actor-framework-snocs/cash_SNocscript.py $SCRIPTPATH/github.com/actor-framework/cash/SNocscript.py
cp $SCRIPTPATH/actor-framework-snocs/unit_testing_SNocscript.py $SCRIPTPATH/github.com/actor-framework/unit_testing/SNocscript.py
cp $SCRIPTPATH/actor-framework-snocs/examples_SNocscript.py $SCRIPTPATH/github.com/actor-framework/examples/SNocscript.py

#CHANGE THE DEFAULT SOURCE AND INSTALL PATHS
export SNOCS_PROJECTS_SRC_PATH=$SCRIPTPATH
export SNOCS_INSTALL_LIB_PATH="$SCRIPTPATH/build"
export SNOCS_INSTALL_BIN_PATH="$SCRIPTPATH/build"

mkdir $SCRIPTPATH/build

#START COMPILATION, INCLUDING ARGUMENTS PROVIDED TO THE SCRIPT, WITH G++ COMPILER (with -std=gnu++11 flag)
$SCRIPTPATH/github.com/osblinnikov/snocs/snocs $SCRIPTPATH -j 8 compiler=gpp platform=x64 verbose=0 -all ${*:1}
