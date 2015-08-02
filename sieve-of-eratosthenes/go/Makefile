include ../Makefile.mk

EXECUTABLES = go

build: $(dependenciesInstalled) bin/SieveGo

run: bin/SieveGo
	@echo "Running golang"
	bin/SieveGo ${SIEVESIZE}

bin/SieveGo: bin
	go build -o bin/SieveGo

bin:
	mkdir bin

clean:
	@rm -rf bin/
