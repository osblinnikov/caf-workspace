# caf-workspace
Example of CAF build with SNocs

    git clone --recursive https://github.com/osblinnikov/caf-workspace.git

if you already installed libedit, scons, python:

    caf-workspace/build.bash -all platform=x64 configuration=Debug shared=1 test install

or

    caf-workspace/build.bash -all platform=x86 configuration=Release shared=0 test install 

these commands will compile all caf libraries, unit-tests, nexus and cash using SNocs (wrapper of SCons) also it will run tests, and install all executables and libraries into the `build` directory. All options can be found at [snocs](https://github.com/osblinnikov/snocs) documentation page

Here some options which are used

shared=1|0 means to build project based on shared libraries rather than static libs

configuration=Release|Debug

platform=x64|x86

All results of the builds will be stored in `build` directory and files will have the names like: 

    com_github_actor_framework_nexus_static_run_gpp_cpp11_x64
    
    libcom_github_actor_framework_libcaf_io_static_gpp_cpp11_x64.a
    
    
