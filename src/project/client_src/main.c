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

static void			ft_error_exit(char *message)
{
	if (DEBUG)
		ft_printf("%s\n", message);
	exit(EXIT_FAILURE);
}

static cmd_ln_t		*ft_cmd_ln_init(void)
{
	cmd_ln_t		*config;

	config = cmd_ln_init(NULL, ps_args(), TRUE,
						"-hmm", MODELDIR "/en-us/en-us",
						"-lm", MODELDIR "/en-us/en-us.lm.bin",
						"-dict", MODELDIR "/en-us/cmudict-en-us.dict",
						NULL);
	if (!config)
		ft_error_exit("Failed to create config object");
	return (config);
}

static void			ft_read_wav(char *argv, ps_decoder_t **ps)
{
	int				rv;
	FILE			*fh;
	int16			buf[512];
	size_t			nsamp;

	fh = fopen(argv, "rb");
	if (!fh)
		ft_error_exit("Unable to open input file");
	rv = ps_start_utt(*ps);
	while (!feof(fh))
	{
		nsamp = fread(buf, 2, 512, fh);
		rv = ps_process_raw(*ps, buf, nsamp, FALSE, FALSE);
	}
	rv = ps_end_utt(*ps);
	fclose(fh);
}

int					main(int argc, char **argv)
{
	ps_decoder_t	*ps;
	cmd_ln_t		*config;
	char const		*hyp;
	int32			score;

	if (argc != 2)
		exit(EXIT_FAILURE);
	err_set_logfp(NULL);
	err_set_debug_level(SPHINX_DEBUG_DISABLED);
	config = ft_cmd_ln_init();
	if (!(ps = ps_init(config)))
		ft_error_exit("Failed to create recognizer");
	ft_read_wav(argv[1], &ps);
	hyp = ps_get_hyp(ps, &score);
	ft_printf("%s\n", hyp);
	ps_free(ps);
	cmd_ln_free_r(config);
	return (EXIT_SUCCESS);
}
