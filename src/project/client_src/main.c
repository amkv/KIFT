/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: akalmyko <akalmyko@student.42.us.org>      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2017/06/05 11:51:20 by akalmyko          #+#    #+#             */
/*   Updated: 2017/06/05 11:58:58 by akalmyko         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../kift.h"

//int				main(void)
//{
//	ft_debug("main function");
//	return (0);
//}

int
main(int argc, char *argv[])
{
	ps_decoder_t *ps = NULL;
	cmd_ln_t *config = NULL;

	config = cmd_ln_init(NULL, ps_args(), True,
						 "-hmm", MODELDIR "/en-us/en-us",
			"-lm", MODELDIR "/en-us/en-us.lm.bin",
			"-dict", MODELDIR "/en-us/cmudict-en-us.dict",
			NULL);

	return 0;
}
