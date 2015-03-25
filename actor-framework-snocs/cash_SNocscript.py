
from helper import *
#           Environment
Import( 'env', 'args' )

def add_dependencies(env, args):
    AddDependency(args,'com_github_actor_framework_libcaf_riac','github.com/actor-framework/libcaf_riac')
    AddDependency(args,'com_github_actor_framework_libcaf_io','github.com/actor-framework/libcaf_io')
    AddDependency(args,'com_github_actor_framework_libcaf_core','github.com/actor-framework/libcaf_core')
    AddPthreads(env, args)
    # AddNetwork(args)
    conf = Configure(env)
    if not conf.CheckLibWithHeader('edit', 'histedit.h', 'c'):
        print 'Did not find libedit.a or edit.lib, exiting!'
        Exit(1)
    env = conf.Finish()


c = {}
c['PROG_NAME'] = 'com_github_actor_framework_cash'
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
