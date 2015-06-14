build: bin/sieve_csharp.exe

run: bin/sieve_csharp.exe
	@echo "Running csharp sieve"
	mono bin/sieve_csharp.exe ${SIEVESIZE}

bin/sieve_csharp.exe: bin sieve_csharp.cs 
	mcs sieve_csharp.cs -out:bin/sieve_csharp.exe

bin:
	mkdir bin

clean: 
	@rm -rf bin/