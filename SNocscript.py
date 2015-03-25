
from helper import *
#           Environment
Import( 'env', 'args' )

def add_dependencies(env, args):
  AddDependency(args,'com_github_actor_framework_libcaf_core','github.com/actor-framework/libcaf_core')
  AddDependency(args,'com_github_actor_framework_libcaf_io','github.com/actor-framework/libcaf_io')
  AddDependency(args,'com_github_actor_framework_libcaf_opencl','github.com/actor-framework/libcaf_opencl')
  AddDependency(args,'com_github_actor_framework_libcaf_riac','github.com/actor-framework/libcaf_riac')
  AddDependency(args,'com_github_actor_framework_nexus','github.com/actor-framework/nexus')
  AddDependency(args,'com_github_actor_framework_cash','github.com/actor-framework/cash')
  AddDependency(args,'com_github_actor_framework_unit_testing','github.com/actor-framework/unit_testing')

c = {}
c['PROG_NAME'] = 'parent'
c['inclDeps'] = add_dependencies
DefaultParentConfig(c, env, args)
