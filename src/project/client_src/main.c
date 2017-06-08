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

int main(int argc, char *argv[])
{
	if (argc != 2)
	{
		ft_printf("bad input\n");
		exit(0);
	}

	ps_decoder_t *ps;
	cmd_ln_t *config;
	FILE *fh;
	char const *hyp, *uttid;
	int16 buf[512];
	int rv;
	int32 score;

//	-inmic yes -hmm  model\en-us\en-us -lm model\en-us\en-us.lm.bin -dict  model\en-us\cmudict-en-us.dict

	config = cmd_ln_init(NULL, ps_args(), TRUE,
						 "-hmm", MODELDIR "/en-us/en-us",
						 "-lm", MODELDIR "/en-us/en-us.lm.bin",
						 "-dict", MODELDIR "/en-us/cmudict-en-us.dict",
						 NULL);
	if (config == NULL) {
		fprintf(stderr, "Failed to create config object, see log for  details\n");
		return -1;
	}

	ps = ps_init(config);
	if (ps == NULL) {
		fprintf(stderr, "Failed to create recognizer, see log for  details\n");
		return -1;
	}

	fh = fopen(argv[1], "rb");
	if (fh == NULL) {
		fprintf(stderr, "Unable to open input file goforward.raw\n");
		return -1;
	}

	rv = ps_start_utt(ps);

	while (!feof(fh)) {
		size_t nsamp;
		nsamp = fread(buf, 2, 512, fh);
		rv = ps_process_raw(ps, buf, nsamp, FALSE, FALSE);
	}

	rv = ps_end_utt(ps);
	hyp = ps_get_hyp(ps, &score);
	printf("Recognized: %s\n", hyp);

	fclose(fh);
	ps_free(ps);
	cmd_ln_free_r(config);


	ft_printf("test_bla\n");
	return 0;
}
