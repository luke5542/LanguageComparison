include ../Makefile.mk

EXECUTABLES = python2 python3 pypy

build: $(dependenciesInstalled)

run: build sieve_python.py
	@echo "Running python2 sieve"
	python2 sieve_python.py ${SIEVESIZE}

	@echo "Running python3 sieve"
	python3 sieve_python.py ${SIEVESIZE}

	@echo "Running pypy sieve"
	pypy sieve_python.py ${SIEVESIZE}

	@echo "Running pypy3 sieve"
	pypy3 sieve_python.py ${SIEVESIZE}

clean:

.PHONY: run
