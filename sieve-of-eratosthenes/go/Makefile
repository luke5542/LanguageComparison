include ../Makefile.mk

EXECUTABLES = go

GOPATH := $(shell pwd)

build: $(dependenciesInstalled) bin/LanguageComparison

run: bin/LanguageComparison
	@echo "Running golang"
	bin/LanguageComparison ${SIEVESIZE}

bin/LanguageComparison:
	cd src
	go get github.com/luke5542/LanguageComparison/

clean:
	@rm -rf bin/*
	@rm -rf pkg/*
	@rm -rf src/github.com/fatih
