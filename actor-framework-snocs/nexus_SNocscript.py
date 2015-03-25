
from helper import *
#           Environment
Import( 'env', 'args' )

def add_dependencies(env, args):
    AddDependency(args,'com_github_actor_framework_libcaf_core',join(args['PROJECTS_ROOT_PATH'],'src/github.com/actor-framework/libcaf_core'))
    AddDependency(args,'com_github_actor_framework_libcaf_io',join(args['PROJECTS_ROOT_PATH'],'src/github.com/actor-framework/libcaf_io'))
    AddDependency(args,'com_github_actor_framework_libcaf_riac',join(args['PROJECTS_ROOT_PATH'],'src/github.com/actor-framework/libcaf_riac'))
    AddPthreads(env, args)
    # AddNetwork(args)

c = {}
c['PROG_NAME'] = 'com_github_actor_framework_nexus'
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
