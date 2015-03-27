
from helper import *
#           Environment
Import( 'env' )

# def add_dependencies(env):
    # AddPthreads(env)
    # AddNetwork(env)

c = {}
c['PROG_NAME'] = 'libcaf_core'
#c['sourceFiles'] = ['libcaf_core.c']
#c['testFiles'] = ['libcaf_coreTest.c']
#c['runFiles'] = ['main.c']
#c['CPPDEFINES'] = []
#c['inclDepsDynamic'] = add_dependencies
#c['inclDepsStatic'] = add_dependencies
#c['inclDepsStatic_tests'] = add_dependencies
#c['inclDepsStatic_run'] = add_dependencies
DefaultLibraryConfig(env, c)
