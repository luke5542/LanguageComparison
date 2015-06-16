include ../Makefile.mk

EXECUTABLES = javac java

build: $(dependenciesInstalled) bin/sieve_java.class

run: bin/sieve_java.class
	@echo "Running java sieve"
	java -cp bin sieve_java ${SIEVESIZE}

bin/sieve_java.class: bin
	javac sieve_java.java -d bin

bin:
	mkdir bin

clean: 
	@rm -rf bin/