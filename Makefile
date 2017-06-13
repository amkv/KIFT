# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    birds                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalmyko <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/03/17 22:34:25 by akalmyko          #+#    #+#              #
#    Updated: 2017/03/17 22:34:35 by akalmyko         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

.PHONY: all clean fclean re c

NAME = bla
SRCF = src/
SERVER = $(SRCF)server_src/

PRJBLA = $(SRCF)bla_src
DMOD =  `pkg-config --cflags pocketsphinx sphinxbase`
DMOD2 = `pkg-config --libs pocketsphinx sphinxbase`

RMF = /bin/rm -rf
CC = /usr/bin/gcc
FLAGS = -Wall -Wextra -Werror

CFILES = $(shell find $(PRJBLA) -name "*.c")
OFILES = $(CFILES:$(PRJBLA)/%.c=%.o)

GRN = \033[1;32m
RED = \033[1;31m
WHT = \033[1;37m
CLN = \033[m

all: $(NAME)

$(NAME):
	@echo "$(NAME) compiling... \c"
	@$(CC) $(CFILES) $(FLAGS) $(DMOD) -c
	@mv $(OFILES) $(PRJBLA)/
	@$(CC) -o $(NAME) $(PRJBLA)/$(OFILES) $(DMOD2)
	@echo "$(GRN)created$(CLN)"

clean:
	@echo "cleaning... \c"
	@$(RMF) $(PRJBLA)/$(OFILES)
	@echo "$(WHT)cleaned$(CLN)"

fclean:
	@echo "fcleaning... \c"
	@$(RMF) $(PRJBLA)/$(OFILES)
	@$(RMF) $(NAME)
	@echo "$(WHT)fcleaned$(CLN)"

c:
	# @$(RMF) $(PRJBLA)/$(OFILES)
	# @$(RMF) $(NAME)
	# @make $(NAME)
	# @echo "$(WHT)done$(CLN)"

re: fclean all
