@echo off

set SCRIPTPATH=%~dp0

pushd "%SCRIPTPATH%/github.com/actor-framework"
git fetch
git checkout develop
git submodule foreach git fetch
popd