
from helper import *
#           Environment
Import( 'env', 'args' )

# def add_dependencies(env, args):
    # AddPthreads(env, args)
    # AddNetwork(args)

c = {}
c['PROG_NAME'] = 'libcaf_core_actor_framework_github_com'
#c['sourceFiles'] = ['libcaf_core.c']
#c['testFiles'] = ['libcaf_coreTest.c']
#c['runFiles'] = ['main.c']
#c['defines'] = []
#c['inclDepsDynamic'] = add_dependencies
#c['inclDepsStatic'] = add_dependencies
#c['inclDepsStatic_tests'] = add_dependencies
#c['inclDepsStatic_run'] = add_dependencies
DefaultLibraryConfig(c, env, args)
