build: bin/sieve_cpp_gcc bin/sieve_cpp_clang

run: bin/sieve_cpp_gcc bin/sieve_cpp_clang
	@echo "Running clang++ sieve"
	bin/sieve_cpp_clang ${SIEVESIZE}

	@echo "Running g++ sieve"
	bin/sieve_cpp_gcc ${SIEVESIZE}

bin/sieve_cpp_clang: CC=clang++
bin/sieve_cpp_clang: sieve_cpp.cpp bin/
	$(CC) -std=c++11 -Ofast sieve_cpp.cpp -o bin/sieve_cpp_clang

bin/sieve_cpp_gcc: CC=g++
bin/sieve_cpp_gcc: sieve_cpp.cpp bin/
	$(CC) -std=c++11 -Ofast sieve_cpp.cpp -o bin/sieve_cpp_gcc

bin:
	mkdir bin

clean: 
	@rm -rf bin/