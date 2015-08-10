include ../Makefile.mk

EXECUTABLES = php

build: $(dependenciesInstalled)

run: build sieve_php.php
	@echo "Running php sieve"
	php sieve_php.php ${SIEVESIZE}

clean:

.PHONY: run
