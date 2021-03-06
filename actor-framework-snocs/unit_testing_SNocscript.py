
from helper import *
#           Environment
Import( 'env' )

def add_dependencies(env):
    #AddDependency(env,'libcaf_opencl','github.com/actor-framework/libcaf_opencl')
    AddDependency(env,'libcaf_riac','github.com/actor-framework/libcaf_riac')
    AddDependency(env,'libcaf_io','github.com/actor-framework/libcaf_io')
    AddDependency(env,'libcaf_core','github.com/actor-framework/libcaf_core')
    if env['COMPILER'] != 'mingw':
        AddPthreads(env)
    AddNetwork(env)

def add_unit_test(testName, additionalFiles=[]):
    initEnv(env,  testName+'_libcaf_unit_testing')
    add_dependencies(env)
    env['scons'].Default(PrefixTest(env, '', ['test_'+testName+'.cpp','test.cpp']+additionalFiles))

add_unit_test('ripemd_160')
add_unit_test('variant')
add_unit_test('atom')
add_unit_test('metaprogramming')
#add_unit_test(intrusive_containers)
add_unit_test('match')
add_unit_test('message')
add_unit_test('serialization')
add_unit_test('uniform_type')
add_unit_test('fixed_vector')
add_unit_test('intrusive_ptr')
add_unit_test('spawn', ['ping_pong.cpp'])
add_unit_test('simple_reply_response')
add_unit_test('serial_reply')
add_unit_test('or_else')
add_unit_test('either')
add_unit_test('constructor_attach')
add_unit_test('custom_exception_handler')
add_unit_test('typed_spawn')
add_unit_test('actor_lifetime')
add_unit_test('message_lifetime')
add_unit_test('local_group')
add_unit_test('sync_send')
add_unit_test('broker')
add_unit_test('remote_actor', ['ping_pong.cpp'])
add_unit_test('typed_remote_actor')
add_unit_test('unpublish')
add_unit_test('optional')
add_unit_test('fixed_stack_actor')
add_unit_test('actor_pool')
if env['MSVC_VERSION'] == None and env['COMPILER'] != 'mingw':
  add_unit_test('profiled_coordinator')
