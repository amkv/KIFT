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

.PHONY: all clean fclean re libft

NAME0 = shared.a
NAME1 = bla
NAME2 = server

SRCF = src/

PRJSHARED = $(SRCF)project/shared_src
PRJCLIENT = $(SRCF)project/client_src
PRJSERVER = $(SRCF)project/server_src
DMOD = "-DMODELDIR=\"`pkg-config --variable=modeldir pocketsphinx`\" `pkg-config --cflags --libs pocketsphinx sphinxbase`"

RMF = /bin/rm -rf
CC = /usr/bin/gcc
LIBFT = $(SRCF)lib/
LIB = $(LIBFT)libft.a
SLIB = $(PRJSHARED)/$(NAME0)
FLAGS = -Wall -Wextra -Werror

CFILES1 = $(shell find $(PRJCLIENT) -name "*.c")
OFILES1 = $(CFILES1:$(PRJCLIENT)/%.c=%.o)

CFILES2 = $(shell find $(PRJSERVER) -name "*.c")
OFILES2 = $(CFILES2:$(PRJSERVER)/%.c=%.o)

GRN = \033[1;32m
RED = \033[1;31m
WHT = \033[1;37m
CLN = \033[m

all: libft $(NAME0) $(NAME1) $(NAME2)

libft:
	@make -C $(LIBFT)

$(NAME0):
	@make -C $(PRJSHARED)

$(NAME1):
	@echo "$(NAME1) compiling... \c"
	@$(CC) $(FLAGS) $(CFILES1)  -c
	@mv $(OFILES1) $(PRJCLIENT)/
	@$(CC) $(FLAGS) $(PRJCLIENT)/$(OFILES1) $(LIB) $(SLIB) -o $(NAME1)
	@echo "$(GRN)created$(CLN)"

$(NAME2):
	@echo "$(NAME2) compiling... \c"
	@$(CC) $(FLAGS) $(CFILES2) -c
	@mv $(OFILES2) $(PRJSERVER)/
	@$(CC) $(FLAGS) $(PRJSERVER)/$(OFILES2) $(LIB) $(SLIB) $(DMOD) -o $(NAME2)
	@echo "$(GRN)created$(CLN)"

clean:
	@make -C $(LIBFT) clean
	@make -C $(PRJSHARED) clean
	@echo "cleaning... \c"
	@$(RMF) $(PRJCLIENT)/$(OFILES1)
	@$(RMF) $(PRJSERVER)/$(OFILES2)
	@echo "$(WHT)cleaned$(CLN)"

fclean:
	@make -C $(LIBFT) fclean
	@make -C $(PRJSHARED) fclean
	@echo "fcleaning... \c"
	@$(RMF) $(PRJCLIENT)/$(OFILES1)
	@$(RMF) $(PRJSERVER)/$(OFILES2)
	@$(RMF) $(NAME1)
	@$(RMF) $(NAME2)
	@echo "$(WHT)fcleaned$(CLN)"

re: fclean all
