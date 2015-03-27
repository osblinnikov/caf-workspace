
from helper import *
#           Environment
Import( 'env' )

def add_dependencies(env):
  AddDependency(env,'libcaf_core','github.com/actor-framework/libcaf_core')
  AddDependency(env,'libcaf_io','github.com/actor-framework/libcaf_io')
  AddDependency(env,'libcaf_opencl','github.com/actor-framework/libcaf_opencl')
  AddDependency(env,'libcaf_riac','github.com/actor-framework/libcaf_riac')
  AddDependency(env,'nexus','github.com/actor-framework/nexus')
  AddDependency(env,'cash','github.com/actor-framework/cash')
  AddDependency(env,'libcaf_unit_testing','github.com/actor-framework/unit_testing')
  AddDependency(env,'libcaf_examples','github.com/actor-framework/examples')

c = {}
c['PROG_NAME'] = 'parent'
c['inclDeps'] = add_dependencies
DefaultParentConfig(env,c)
