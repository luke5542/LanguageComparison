include ../Makefile.mk

EXECUTABLES = dub dmd

build: $(dependenciesInstalled) bin/sieve_dlang

run: bin/sieve_dlang
	@echo "Running dlang sieve"
	bin/sieve_dlang ${SIEVESIZE}

bin/sieve_dlang: 
	dub build --config=release --build=release-nobounds

clean: 
	@rm -rf bin/ .dub