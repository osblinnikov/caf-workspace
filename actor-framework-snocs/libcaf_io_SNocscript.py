
from helper import *
#           Environment
Import( 'env', 'args' )

def add_dependencies(env, args):
    AddDependency(args,'com_github_actor_framework_libcaf_core',join(args['PROJECTS_ROOT_PATH'],'src/github.com/actor-framework/libcaf_core'))
    # AddPthreads(env, args)
    # AddNetwork(args)

c = {}
c['PROG_NAME'] = 'com_github_actor_framework_libcaf_io'
#c['sourceFiles'] = ['libcaf_io.c']
#c['testFiles'] = ['libcaf_ioTest.c']
#c['runFiles'] = ['main.c']
#c['defines'] = []
c['inclDeps'] = add_dependencies
#c['inclDepsDynamic'] = add_dependencies
#c['inclDepsDynamic_tests'] = add_dependencies
#c['inclDepsDynamic_run'] = add_dependencies
#c['inclDepsStatic'] = add_dependencies
#c['inclDepsStatic_tests'] = add_dependencies
#c['inclDepsStatic_run'] = add_dependencies
DefaultLibraryConfig(c, env, args)
