include ../Makefile.mk

EXECUTABLES = ruby

build: $(dependenciesInstalled)

run: build sieve_ruby.rb
	@echo "Running ruby sieve"
	ruby sieve_ruby.rb ${SIEVESIZE}

clean:

.PHONY: run 