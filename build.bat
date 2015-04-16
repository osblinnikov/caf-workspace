@echo off
set SCRIPTPATH=%~dp0

echo "SCRIPTPATH: %SCRIPTPATH%"

copy %SCRIPTPATH%\actor-framework-snocs\libcaf_core_SNocscript.py %SCRIPTPATH%\github.com\actor-framework\libcaf_core\SNocscript.py 
copy %SCRIPTPATH%\actor-framework-snocs\libcaf_io_SNocscript.py %SCRIPTPATH%\github.com\actor-framework\libcaf_io\SNocscript.py
copy %SCRIPTPATH%\actor-framework-snocs\libcaf_opencl_SNocscript.py %SCRIPTPATH%\github.com\actor-framework\libcaf_opencl\SNocscript.py
copy %SCRIPTPATH%\actor-framework-snocs\libcaf_riac_SNocscript.py %SCRIPTPATH%\github.com\actor-framework\libcaf_riac\SNocscript.py
copy %SCRIPTPATH%\actor-framework-snocs\nexus_SNocscript.py %SCRIPTPATH%\github.com\actor-framework\nexus\SNocscript.py
copy %SCRIPTPATH%\actor-framework-snocs\cash_SNocscript.py %SCRIPTPATH%\github.com\actor-framework\cash\SNocscript.py
copy %SCRIPTPATH%\actor-framework-snocs\unit_testing_SNocscript.py %SCRIPTPATH%\github.com\actor-framework\unit_testing\SNocscript.py
copy %SCRIPTPATH%\actor-framework-snocs\examples_SNocscript.py %SCRIPTPATH%\github.com\actor-framework\examples\SNocscript.py

set SNOCS_PROJECTS_SRC_PATH=%SCRIPTPATH%
set SNOCS_INSTALL_LIB_PATH="%SCRIPTPATH%\\build"
set SNOCS_INSTALL_BIN_PATH="%SCRIPTPATH%\\build"

:: IF "%QTVER%"=="" set QTVER=5.4
set QTVER=
:: set QTDIR=C:\Qt\%QTVER%\msvc2012_opengl
set QTDIR=
echo "QTVER: %QTVER%"
echo "QTDIR: %QTDIR%"

pushd %SCRIPTPATH%

%SCRIPTPATH%\github.com\osblinnikov\snocs\snocs.bat %SCRIPTPATH% --more-warnings compiler=mingw platform=x64 verbose=0 define="_WIN32_WINNT=0x0600" -all %*

popd
