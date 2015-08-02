include ../Makefile.mk

EXECUTABLES = node

build: $(dependenciesInstalled)

run: build sieve_javascript.js
	@echo "Running node sieve"
	node --max-old-space-size=8192 sieve_javascript.js ${SIEVESIZE}

clean:

.PHONY: run 