@echo off

set SCRIPTPATH=%~dp0

pushd "%SCRIPTPATH%/github.com/actor-framework"
git fetch
git checkout master
git submodule foreach git fetch
popd