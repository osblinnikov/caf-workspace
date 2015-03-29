
from helper import *
#           Environment
Import( 'env' )

def add_dependencies(env):
    AddDependency(env,'libcaf_opencl','github.com/actor-framework/libcaf_opencl')
    AddDependency(env,'libcaf_riac','github.com/actor-framework/libcaf_riac')
    AddDependency(env,'libcaf_io','github.com/actor-framework/libcaf_io')
    AddDependency(env,'libcaf_core','github.com/actor-framework/libcaf_core')
    AddPthreads(env)
    # AddNetwork(env)

def addWithFiles(progName, path, files, cppPaths, c):
    initEnv(env,  progName+'_libcaf_examples')
    enableQtModules(env,c,True)
    env['prj_env'].Append( CPPPATH = cppPaths )
    add_dependencies(env)
    
    env['scons'].Default(PrefixProgram(env, path, [progName+".cpp"]+files))

def add(progName, path):
    addWithFiles(progName, path, [], [], {})

add('announce_1', 'type_system')
add('announce_2', 'type_system')
add('announce_3', 'type_system')
add('announce_4', 'type_system')
add('announce_5', 'type_system')
add('dancing_kirby', 'message_passing')
add('dining_philosophers', 'message_passing')
add('hello_world', '.')
add('aout', '.')
add('calculator', 'message_passing')
add('typed_calculator', 'message_passing')
add('distributed_calculator', 'remote_actors')
add('group_server', 'remote_actors')
add('group_chat', 'remote_actors')
add('simple_broker', 'brokers')
add('simple_http_broker', 'brokers')

# SEARCH FOR PROTOBUF
conf = Configure(env['scons'])
PROTOBUF_FOUND = conf.CheckLibWithHeader('protobuf', 'google/protobuf/message.h', 'c')
if not PROTOBUF_FOUND:
    print '******\nDid not find libprotobuf.a or protobuf.lib! Will skip `protobuf_broker` altogether!\n******'
env['scons'] = conf.Finish()
# END SEARCH FOR PROTOBUF

env['scons'].Tool('protoc')
if PROTOBUF_FOUND:
    proto_files = env['scons'].Protoc(
        [],
        "remote_actors/pingpong.proto",
        PROTOCPROTOPATH=['.'],
        PROTOCOUTDIR='.', 
        PROTOCPYTHONOUTDIR=None
        # PROTOCCPPOUTFLAGS = "dllexport_decl=PROTOCONFIG_EXPORT:", too
    )
    addWithFiles('protobuf_broker', 'brokers', [proto_files[0]], ['remote_actors'], {})



if env.has_key('QT_TOOL'):
    c = {}
    c['qt4modules'] = c['qt5modules'] = ['QtCore','QtGui','QtWidgets']
    c['qt4ui'] = c['qt5ui'] = ['qtsupport/chatwindow.ui']
    addWithFiles('qt_group_chat', 'qtsupport', ['chatwidget.cpp'], ['qtsupport'], c)


# SEARCH FOR CURL
conf = Configure(env['scons'])
CURL_FOUND = conf.CheckLibWithHeader('curl', 'curl/curl.h', 'c')
if not CURL_FOUND:
    print '******\nDid not find libcurl.a or curl.lib! Will skip `curl_fuse` altogether!\n******'
env['scons'] = conf.Finish()
# END SEARCH FOR CURL

if CURL_FOUND:
    add('curl_fuse', 'curl')
