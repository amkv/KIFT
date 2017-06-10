/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   kift.h                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: akalmyko <akalmyko@student.42.us.org>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/06/05 11:59:32 by akalmyko          #+#    #+#             */
/*   Updated: 2017/06/05 11:59:41 by akalmyko         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef KIFT_H
# define KIFT_H
# define MODELDIR "model/"
# include "../lib/libft/libft.h"
# include <pocketsphinx.h>
# include <err.h>
# pragma GCC diagnostic ignored "-Wunused-variable" /* delete */

# define EXIT_SUCCESS 0
# define DEBUG	True
# define SPHINX_DEBUG_DISABLED 0

typedef enum	e_bool
{
	False,
	True
}				t_bool;


/*
** Client (bla) functions
*/




/*
** Server functions
*/




/*
** Shared function
*/

void					ft_debug(char *message);

#endif