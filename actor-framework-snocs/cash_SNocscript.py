
from helper import *
#           Environment
Import( 'env', 'args' )

def add_dependencies(env, args):
    AddDependency(args,'libcaf_riac_actor_framework_github_com','github.com/actor-framework/libcaf_riac')
    AddDependency(args,'libcaf_io_actor_framework_github_com','github.com/actor-framework/libcaf_io')
    AddDependency(args,'libcaf_core_actor_framework_github_com','github.com/actor-framework/libcaf_core')
    AddPthreads(env, args)
    # AddNetwork(args)
    conf = Configure(env)
    if not conf.CheckLibWithHeader('edit', 'histedit.h', 'c'):
        print 'Did not find libedit.a or edit.lib, exiting!'
        Exit(1)
    env = conf.Finish()


c = {}
c['PROG_NAME'] = 'cash_actor_framework_github_com'
c['paths'] = ['sash']
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
