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
# include "../lib/libft/libft.h"

typedef enum	e_bool
{
	False,
	True
}				t_bool;

#define DEBUG	True

void					ft_debug(char *message);

#endif