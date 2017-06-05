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

add_executable(${PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(
		${PROJECT_NAME}
		${CMAKE_CURRENT_SOURCE_DIR}/src/lib/libft.a
)
