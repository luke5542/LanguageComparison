include ../Makefile.mk

EXECUTABLES = lua luac

build: $(dependenciesInstalled) bin/sieve_lua.luac

run: bin/sieve_lua.luac
	@echo "Running lua sieve"
	lua sieve_lua.lua ${SIEVESIZE}

	@echo "Running luac sieve"
	lua bin/sieve_lua.luac ${SIEVESIZE}

bin/sieve_lua.luac: bin
	luac -s -o bin/sieve_lua.luac sieve_lua.lua

bin:
	mkdir bin

clean: 
	@rm -rf bin/