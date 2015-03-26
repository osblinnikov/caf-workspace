
from helper import *
#           Environment
Import( 'env', 'args' )

def add_dependencies(env, args):
    AddDependency(args,'libcaf_riac_actor_framework_github_com','github.com/actor-framework/libcaf_riac')
    AddDependency(args,'libcaf_io_actor_framework_github_com','github.com/actor-framework/libcaf_io')
    AddDependency(args,'libcaf_core_actor_framework_github_com','github.com/actor-framework/libcaf_core')
    AddPthreads(env, args)
    # AddNetwork(args)

c = {}
c['PROG_NAME'] = 'nexus_actor_framework_github_com'
#c['sourceFiles'] = ['libcaf_core.c']
#c['testFiles'] = ['libcaf_coreTest.c']
c['runFiles'] = ['main.cpp']
#c['defines'] = []
c['inclDeps'] = add_dependencies
#c['inclDepsDynamic'] = add_dependencies
#c['inclDepsStatic'] = add_dependencies
#c['inclDepsStatic_tests'] = add_dependencies
#c['inclDepsStatic_run'] = add_dependencies
DefaultLibraryConfig(c, env, args)
