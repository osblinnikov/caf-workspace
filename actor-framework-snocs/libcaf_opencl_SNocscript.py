
from helper import *
#           Environment
Import( 'env' )

def add_dependencies(env):
    AddDependency(env,'libcaf_core','github.com/actor-framework/libcaf_core')
    # AddPthreads(env)
    # AddNetwork(env)


conf = Configure(env['scons'])
OPENCL_AVAILABLE = conf.CheckHeader('CL/opencl.h')
if not OPENCL_AVAILABLE:
    print '******\nDid not find CL/opencl.h! Will skip `libcaf_opencl` altogether!\n******'
env['scons'] = conf.Finish()

if OPENCL_AVAILABLE:
	c = {}
	c['PROG_NAME'] = 'libcaf_opencl'
	#c['sourceFiles'] = ['libcaf_io.c']
	#c['testFiles'] = ['libcaf_ioTest.c']
	#c['runFiles'] = ['main.c']
	#c['CPPDEFINES'] = []
	c['inclDeps'] = add_dependencies
	#c['inclDepsDynamic'] = add_dependencies
	#c['inclDepsDynamic_tests'] = add_dependencies
	#c['inclDepsDynamic_run'] = add_dependencies
	#c['inclDepsStatic'] = add_dependencies
	#c['inclDepsStatic_tests'] = add_dependencies
	#c['inclDepsStatic_run'] = add_dependencies
	DefaultLibraryConfig(env, c)
