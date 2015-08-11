include ../Makefile.mk

EXECUTABLES = ocamlopt opam

build: $(dependenciesInstalled) sieve_ocaml.native

run: sieve_ocaml.native
	@echo "Running rust sieve"
	./sieve_ocaml.native ${SIEVESIZE}

sieve_ocaml.native: sieve_ocaml.ml
	opam install core
	corebuild sieve_ocaml.native

clean:
	@rm -rf target
