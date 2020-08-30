cmake_minimum_required(VERSION 2.8.12)
project(sdl2_net)

include(conanbuildinfo.cmake)
conan_basic_setup()

set(SOURCES
source_subfolder/SDLnet.c
source_subfolder/SDLnetselect.c
source_subfolder/SDLnetTCP.c
source_subfolder/SDLnetUDP.c
)

set(HEADERS
source_subfolder/SDL_net.h
source_subfolder/SDLnetsys.h
)

add_library(${PROJECT_NAME} ${SOURCES} ${HEADERS})

target_include_directories(${PROJECT_NAME} PRIVATE "source_subfolder")
target_link_libraries(${PROJECT_NAME} PRIVATE ${CONAN_LIBS})
set_target_properties(${PROJECT_NAME} PROPERTIES PUBLIC_HEADER source_subfolder/SDL_net.h)

if(WIN32)
  target_link_libraries(${PROJECT_NAME} PUBLIC ws2_32.lib iphlpapi.lib)
endif()

install(TARGETS ${PROJECT_NAME}
  ARCHIVE DESTINATION "lib"
  LIBRARY DESTINATION "lib"
  RUNTIME DESTINATION "bin"
  PUBLIC_HEADER DESTINATION "include/SDL2"
)
