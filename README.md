# caf-workspace
Example of CAF build with SNocs

    git clone --recursive https://github.com/osblinnikov/caf-workspace.git

if you already installed libedit, scons, python (make sure you are running the correct platform, because libedit for x86 may not be installed if you are running on x64)

    caf-workspace/build.bash platform=x64 configuration=Debug shared=1 test install

or

    caf-workspace/build.bash platform=x86 configuration=Release shared=0 test install 

these commands will compile all caf libraries, unit-tests, nexus and cash using SNocs (wrapper of SCons) also it will run tests, and install all executables and libraries into the `build` directory. All options can be found at [snocs](https://github.com/osblinnikov/snocs) documentation page

Here some options which were used

shared=1|0 means to build project based on shared libraries rather than static libs

configuration=Release|Debug

platform=x64|x86

All results of the builds will be stored in `build` directory and files will have the names like: 

    nexus_run_static_actor_framework_github_com_gpp_x64
    
    libcaf_io_static_actor_framework_github_com_gpp_x64.a


FAQ:
---

1. `libcaf_opencl` can't find my opencl headers, howto fix this?
    
    Install OpenCL implementation from your GPU/CPU vendor and add CPPPATH to installed headers e.g: `./build.bash CPPPATH=~/AMDAPPSDK-3.0-0-Beta/include`. You probably need to add path to the opencl shared libraries to the LD_LIBRARY_PATH environment variable if the installer of opencl didn't do it for you.

2. Got "Did not find libedit.a or edit.lib! Will skip `Cash` altogether!" during compilation, how to install libedit?

    On Ubuntu execute `sudo apt-get install libedit-dev` and recompile the project. 
    Note: Sometimes scons required clearing the cache before recompilation with newly installed packages:
    `rm -r .scon*`

3. Got "Did not find libprotobuf.a or protobuf.lib! Will skip `protobuf_broker` altogether!", what am I gonna do?

    On Ubuntu, install libprotobuf and protoc: `sudo apt-get install libprotobuf-dev protobuf-compiler` and recompile project again. Notice the note in FAQ#2.




    
