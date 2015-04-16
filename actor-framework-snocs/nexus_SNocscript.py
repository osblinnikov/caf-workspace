
from helper import *
#           Environment
Import( 'env' )

def add_dependencies(env):
    AddDependency(env,'libcaf_riac','github.com/actor-framework/libcaf_riac')
    AddDependency(env,'libcaf_io','github.com/actor-framework/libcaf_io')
    AddDependency(env,'libcaf_core','github.com/actor-framework/libcaf_core')
    if env['COMPILER'] != 'mingw':
        AddPthreads(env)
    AddNetwork(env)

c = {}
c['PROG_NAME'] = 'nexus'
#c['sourceFiles'] = ['libcaf_core.c']
#c['testFiles'] = ['libcaf_coreTest.c']
c['runFiles'] = ['main.cpp']
#c['CPPDEFINES'] = []
c['inclDeps'] = add_dependencies
#c['inclDepsDynamic'] = add_dependencies
#c['inclDepsStatic'] = add_dependencies
#c['inclDepsStatic_tests'] = add_dependencies
#c['inclDepsStatic_run'] = add_dependencies
DefaultLibraryConfig(env, c)
