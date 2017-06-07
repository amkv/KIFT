#include <pocketsphinx.h>
#include <stdio.h>

int
main(int argc, char *argv[])
{
	ps_decoder_t *ps = NULL;
	cmd_ln_t *config = NULL;

	config = cmd_ln_init(NULL, ps_args(), TRUE,
						 "-hmm", MODELDIR "/en-us/en-us",
			"-lm", MODELDIR "/en-us/en-us.lm.bin",
			"-dict", MODELDIR "/en-us/cmudict-en-us.dict",
			NULL);

	printf("test\n");
	return 0;
}

// gcc -o test main.c -DMODELDIR=\"`pkg-config --variable=modeldir pocketsphinx`\" `pkg-config --cflags --libs pocketsphinx sphinxbase`