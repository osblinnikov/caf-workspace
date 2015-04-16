
from helper import *
#           Environment
Import( 'env' )

def add_dependencies(env):
    AddDependency(env,'libcaf_core','github.com/actor-framework/libcaf_core')
    # AddPthreads(env)
    AddNetwork(env)

c = {}
c['PROG_NAME'] = 'libcaf_io'
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
