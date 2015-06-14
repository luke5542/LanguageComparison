build: bin/sieve_scala.class

run: bin/sieve_scala.class
	@echo "Running scala sieve"
	scala -cp bin sieve_scala ${SIEVESIZE}

bin/sieve_scala.class: bin sieve_scala.scala
	scalac sieve_scala.scala -d bin

bin:
	mkdir bin

clean: 
	@rm -rf bin/