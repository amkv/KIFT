# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: akalmyko <akalmyko@student.42.us.org>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/06/05 14:01:15 by akalmyko          #+#    #+#              #
#    Updated: 2017/06/05 14:01:45 by akalmyko         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

.PHONY: all clean fclean re

NAME = shared.a

CFILES = $(shell find . -name "*.c")
OFILES = $(CFILES:%.c=%.o)
DMOD = -DMODELDIR=\"`pkg-config --variable=modeldir pocketsphinx`\" `pkg-config --cflags pocketsphinx sphinxbase`
DMOD2 = `pkg-config --libs pocketsphinx sphinxbase`

RMF = /bin/rm -rf
CC = /usr/bin/gcc
FLAGS = -Wall -Wextra -Werror
GRN = \033[1;32m
RED = \033[1;31m
WHT = \033[1;37m
CLN = \033[m

all: $(NAME)

$(NAME):
	@echo "$(NAME) compiling... \c"
	@$(CC) $(FLAGS) $(DMOD) $(CFILES) -c
	@ar rc $(NAME) $(OFILES)
	@ranlib $(NAME)
	@echo "$(GRN)created$(CLN)"

clean:
	@$(RMF) $(shell find . -name "*.o")

fclean:
	@$(RMF) $(shell find . -name "*.o")
	@$(RMF) $(NAME)

re: fclean all
