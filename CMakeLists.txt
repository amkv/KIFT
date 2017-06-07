cmake_minimum_required(VERSION 3.6)
project(kift)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fsanitize=address -Wall -Wextra -Werror")
#-DMODELDIR=${CMAKE_CURRENT_SOURCE_DIR}/src/pocketsphinx/share/pocketsphinx/model
#set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -Werror")

#file (GLOB SOURCE_FILES
#		${CMAKE_CURRENT_SOURCE_DIR}/src/project/client_src/*.c
#		${CMAKE_CURRENT_SOURCE_DIR}/src/project/server_src/*.c
#		${CMAKE_CURRENT_SOURCE_DIR}/src/project/shared_src/*.c
#		)

INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR}/src/pocketsphinx/include
					${CMAKE_CURRENT_SOURCE_DIR}/src/pocketsphinx/include/sphinxbase
					${CMAKE_CURRENT_SOURCE_DIR}/src/pocketsphinx/include/pocketsphinx
					${CMAKE_CURRENT_SOURCE_DIR}/src/sphinxbase/include
					${CMAKE_CURRENT_SOURCE_DIR}/src/sphinxbase/include/sphinxbase)
LINK_DIRECTORIES(	${CMAKE_CURRENT_SOURCE_DIR}/src/pocketsphinx/lib
					${CMAKE_CURRENT_SOURCE_DIR}/src/sphinxbase/lib)

set (SOURCE_FILES
					src/project/client_src/main.c
					src/project/shared_src/ft_debug.c

					#src/project/server_src/main.c

					#src/project/shared_src/ft_debug.c
)

add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(
		${PROJECT_NAME}
		${EXTRA_LIBS}
		${CMAKE_CURRENT_SOURCE_DIR}/src/lib/libft.a
		${CMAKE_CURRENT_SOURCE_DIR}/src/pocketsphinx/lib/libpocketsphinx.a
		${CMAKE_CURRENT_SOURCE_DIR}/src/sphinxbase/lib/libsphinxbase.a
)
