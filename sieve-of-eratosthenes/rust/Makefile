include ../Makefile.mk

EXECUTABLES = rust cargo

build: $(dependenciesInstalled) target/release/sieve_rust

run: target/release/sieve_rust
	@echo "Running rust sieve"
	target/release/sieve_rust ${SIEVESIZE}

target/release/sieve_rust: 
	cargo build --release

clean: 
	@rm -rf target