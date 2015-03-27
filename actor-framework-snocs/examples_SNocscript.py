
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
    env['prj_env'].Append( CPPPATH = cppPaths )
    add_dependencies(env)
    enableQtModules(env,c,False)
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




#   find_package(Qt5 COMPONENTS Core Gui Widgets)
#   if(Qt5_FOUND)
#     message(STATUS "Found Qt5")
#     #include(${QT_USE_FILE})
#     QT5_ADD_RESOURCES(GROUP_CHAT_RCS )
#     QT5_WRAP_UI(GROUP_CHAT_UI_HDR qtsupport/chatwindow.ui)
#     QT5_WRAP_CPP(GROUP_CHAT_MOC_SRC qtsupport/chatwidget.hpp)
#     # generated headers will be in cmake build directory
#     #include_directories(. qtsupport ${CMAKE_CURRENT_BINARY_DIR} ${CPPA_INCLUDE})
#     include_directories(qtsupport
#                         ${CMAKE_CURRENT_BINARY_DIR}
#                         ${Qt5Core_INCLUDE_DIRS}
#                         ${Qt5Gui_INCLUDE_DIRS}
#                         ${Qt5Widgets_INCLUDE_DIRS})
#     set(GROUP_CHAT_SRC qtsupport/qt_group_chat.cpp qtsupport/chatwidget.cpp)
#     add_executable(qt_group_chat
#                    ${GROUP_CHAT_SRC}
#                    ${GROUP_CHAT_MOC_SRC}
#                    ${GROUP_CHAT_UI_HDR})
#     target_link_libraries(qt_group_chat
#                           ${CMAKE_DL_LIBS}
#                           ${LIBCAF_LIBRARIES}
#                           Qt5::Core
#                           Qt5::Gui
#                           Qt5::Widgets)
#     add_dependencies(qt_group_chat all_examples)
#   else()
#     find_package(Qt4)
#     if(QT4_FOUND)
#       message(STATUS "Found Qt4")
#       include(${QT_USE_FILE})
#       QT4_ADD_RESOURCES(GROUP_CHAT_RCS )
#       QT4_WRAP_UI(GROUP_CHAT_UI_HDR qtsupport/chatwindow.ui)
#       QT4_WRAP_CPP(GROUP_CHAT_MOC_SRC qtsupport/chatwidget.hpp)
#       # generated headers will be in cmake build directory
#       #include_directories(. qtsupport ${CMAKE_CURRENT_BINARY_DIR} ${CPPA_INCLUDE})
#       include_directories(qtsupport ${CMAKE_CURRENT_BINARY_DIR})
#       set(GROUP_CHAT_SRCS qtsupport/qt_group_chat.cpp qtsupport/chatwidget.cpp)
#       add_executable(qt_group_chat
#                      ${GROUP_CHAT_SRCS}
#                      ${GROUP_CHAT_MOC_SRC}
#                      ${GROUP_CHAT_UI_HDR})
#       target_link_libraries(qt_group_chat
#                             ${CMAKE_DL_LIBS}
#                             ${LIBCAF_LIBRARIES}
#                             ${QT_LIBRARIES})
#       add_dependencies(qt_group_chat all_examples)
#     endif()
#   endif()
# endif()

# if(NOT CAF_NO_CURL_EXAMPLES)
#   find_package(CURL)
#   if(CURL_FOUND)
#     add_executable(curl_fuse curl/curl_fuse.cpp)
#     include_directories(${CURL_INCLUDE_DIRS})
#     target_link_libraries(curl_fuse ${CMAKE_DL_LIBS} ${LIBCAF_LIBRARIES} ${PTHREAD_LIBRARIES} ${CURL_LIBRARY})
#     add_dependencies(curl_fuse all_examples)
#   endif(CURL_FOUND)
# endif()