include ../Makefile.mk

EXECUTABLES = perl

build: $(dependenciesInstalled)

run: build sieve_perl.pl
	@echo "Running perl sieve"
	perl sieve_perl.pl ${SIEVESIZE}

clean:

.PHONY: run 