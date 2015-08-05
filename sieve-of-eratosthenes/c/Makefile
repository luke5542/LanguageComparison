include ../Makefile.mk

EXECUTABLES = gcc clang

run: $(dependenciesInstalled) bin/sieve_c_gcc bin/sieve_c_clang
	@echo "Running clang sieve"
	bin/sieve_c_clang ${SIEVESIZE}

	@echo "Running gcc sieve"
	bin/sieve_c_gcc ${SIEVESIZE}

build: bin/sieve_c_clang bin/sieve_c_gcc

bin/sieve_c_gcc: bin
	gcc -std=c99 -Ofast sieve_c.c -o bin/sieve_c_gcc -lm

bin/sieve_c_clang: bin
	clang -std=c99 -Ofast sieve_c.c -o bin/sieve_c_clang -lm

bin:
	mkdir bin

clean:
	@rm -rf bin/