# caf-workspace
Example of CAF build with SNocs

    git clone --recursive https://github.com/osblinnikov/caf-workspace.git

if you already installed libedit, scons, python:

    caf-workspace/build.bash -all platform=x64 test install

or

    caf-workspace/build.bash -all platform=x86 test install 

this commands will compile all caf libraries, unit-tests, nexus and cash using SNocs (wrapper of SCons) also it will run tests, and install all executables and libraries into the `build` directory. All options can be found at [snocs](https://github.com/osblinnikov/snocs) documentation page
