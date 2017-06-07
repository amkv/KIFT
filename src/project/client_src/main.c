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
//
//	return (0);
//}

int
main(int argc, char *argv[])
{
	ps_decoder_t *ps = NULL;
	cmd_ln_t *config = NULL;

	ft_debug("main function");
	config = cmd_ln_init(NULL, ps_args(), TRUE,
						 "-hmm", MODELDIR "/en-us/en-us",
			"-lm", MODELDIR "/en-us/en-us.lm.bin",
			"-dict", MODELDIR "/en-us/cmudict-en-us.dict",
			NULL);

	if (argc > 1)
		ft_printf("%s\n", argv[1]);
	ft_printf("test_bla\n");
	ps = NULL;
	return 0;
}
