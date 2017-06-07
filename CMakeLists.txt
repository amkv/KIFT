cmake_minimum_required(VERSION 3.6)
project(kift)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fsanitize=address -Wall -Wextra -Werror")
#set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -Werror")

#file (GLOB SOURCE_FILES
#		${CMAKE_CURRENT_SOURCE_DIR}/src/project/client_src/*.c
#		${CMAKE_CURRENT_SOURCE_DIR}/src/project/server_src/*.c
#		${CMAKE_CURRENT_SOURCE_DIR}/src/project/shared_src/*.c
#		)

set (SOURCE_FILES
		src/project/client_src/main.c
		src/project/shared_src/ft_debug.c

		#src/project/server_src/main.c

		#src/project/shared_src/ft_debug.c
)

#FIND_LIBRARY(POCKETSPHINX_LIBRARY pocketsphinx)
#FIND_LIBRARY(BASESPHINX_LIBRARY sphinxbase)
#MARK_AS_ADVANCED(${POCKETSPHINX_LIBRARY} ${BASESPHINX_LIBRARY})
#SET(EXTRA_LIBS ${POCKETSPHINX_LIBRARY} ${BASESPHINX_LIBRARY})

add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(
		${PROJECT_NAME}
#		${EXTRA_LIBS}
		${CMAKE_CURRENT_SOURCE_DIR}/src/lib/libft.a
#		${CMAKE_CURRENT_SOURCE_DIR}/src/pocketsphinx/lib/libpocketsphinx.a
#		${CMAKE_CURRENT_SOURCE_DIR}/src/sphinxbase/lib/libsphinxbase.a

)
