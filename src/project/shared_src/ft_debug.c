/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_debug.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: akalmyko <akalmyko@student.42.us.org>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/06/05 13:31:50 by akalmyko          #+#    #+#             */
/*   Updated: 2017/06/05 13:32:28 by akalmyko         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../kift.h"

void			ft_debug(char *message)
{
	static int i = 0;

	if (!DEBUG)
		return ;
	ft_printf("[%d] %s\n", ++i, message);
}
