# caf-workspace
[CAF](https://github.com/actor-framework/actor-framework) build with [SNocs](https://github.com/osblinnikov/snocs)

    git clone --recursive https://github.com/osblinnikov/caf-workspace.git
    
or if you already have your workspace with own projects add one more remote repository to your git repo

    git remote add cafws https://github.com/osblinnikov/caf-workspace.git
    git pull --recurse-submodules cafws master
    git submodule update --init --recursive

if you already installed libedit, libprotobuf, protoc, libcurl, SCons, python (make sure you are running the correct platform, because libedit for x86 may not be installed if you are running on x64)

    QTVER=5.4 caf-workspace/build.bash platform=x64 configuration=Debug shared=1 test install

or

    caf-workspace/build.bash compiler=clangpp platform=x86 test install
    
in case of the build problems see FAQ at the bottom of the page and/or ask for help in the issue tracker.

these commands will compile all caf libraries, unit-tests, nexus and cash using SNocs (wrapper of SCons) also it will run tests, and install all executables and libraries into the `build` directory. All options can be found at [snocs](https://github.com/osblinnikov/snocs) documentation page

Here some options which were used

shared=1|0 means to build project based on shared libraries rather than static libs

configuration=Release|Debug

platform=x64|x86

All results of the builds will be stored in `build` directory and files will have the names like: 

    nexus_run_static_actor_framework_github_com_gpp_x64
    
    libcaf_io_static_actor_framework_github_com_gpp_x64.a


Specific to CAF available macro definitions:

    define=CAF_NO_MEM_MANAGEMENT
    define=CAF_ENABLE_RUNTIME_CHECKS
    define="CAF_LOG_LEVEL=0" define="LOG_LEVEL_STR=\"ERROR\""

Enable memory sanitizer:

    cppflag=-fsanitize=address cppflag=-fno-omit-frame-pointer


FAQ:
---

1. `libcaf_opencl` can't find my opencl headers, howto fix this?
    
    Install OpenCL implementation from your GPU/CPU vendor and add CPPPATH to installed headers e.g: `./build.bash CPPPATH=~/AMDAPPSDK-3.0-0-Beta/include`. You probably need to add path to the opencl shared libraries to the LD_LIBRARY_PATH environment variable if the installer of opencl didn't do it for you.

2. Got "Did not find libedit.a or edit.lib! Will skip `Cash` altogether!" during compilation, how to install libedit?

    On Ubuntu execute `sudo apt-get install libedit-dev` and recompile the project. 
    Note: Sometimes scons required clearing the cache before recompilation with newly installed packages:
    `rm .sconsign.dblite`

3. Got "Did not find libprotobuf.a or protobuf.lib! Will skip `protobuf_broker` altogether!", what am I gonna do?

    On Ubuntu, install libprotobuf and protoc: `sudo apt-get install libprotobuf-dev protobuf-compiler` and recompile project again. Notice the note in FAQ#2.

4. Got "Did not find libcurl.a or curl.lib! Will skip...."

    On Ubuntu, install one of libcurl-dev packages e.g: `sudo apt-get install libcurl4-openssl-dev`. Notice the note in FAQ#2.

5. Clang++ doesn't find some headers e.g `<cstdio>` etc:

    On Ubuntu, install libc++-dev : `sudo apt-get install libc++-dev`
    
6. Howto build with MinGW?

    a) Download MinGW with the C++ threads from [here for 32 bit](http://sourceforge.net/projects/mingwbuilds/files/host-windows/releases/4.8.1/32-bit/threads-posix/dwarf/) or from [here for 64 bit](http://sourceforge.net/projects/mingwbuilds/files/host-windows/releases/4.8.1/64-bit/threads-posix/dwarf/), or as an alternative you can install mingw during installation of [qt5.4](http://www.qt.io/download-open-source/) 

    b) unpack and add the bin folder from the archieve (with Qt C:\QT\5.4\Tools\mingw...) to the PATH environment variable: 

        `PATH=%PATH%;UNPACKED_ARCHIEVE/bin`
