# Language Comparison
[![Docker Repository on Quay.io](https://quay.io/repository/passmcr/languagecomparison/status "Docker Repository on Quay.io")](https://quay.io/repository/passmcr/languagecomparison)

This is a collection of programs written in various languages to perform the exact same tasks as a demonstration of both the syntactic differences between these languages as well as the run-time speeds of their respective compiled (or interpreted) outputs.

## Running the examples:
There are two ways to run the code examples:
#### Direct (install all the runtimes locally)
+ Make sure you have the compilers/interpreters for these languages installed correctly.
+ Clone this repo (`git clone https://github.com/luke5542/LanguageComparison`).
+ Change directories to the example you want to run (e.g. `cd sieve-of-eratosthenes`)
+ Run the `make runall` to run all tests in that directory

#### Inside a docker container (no installation required):
+ Ensure you have [docker installed](https://docs.docker.com/installation/)
+ Pull the latest prebuilt docker image using `docker pull quay.io/passmcr/languagecomparison`
+ To run the tests, execute the container directly: `docker run quay.io/passmcr/languagecomparison`
+ To view/edit the code yourself, drop into a docker shell using `docker run -it quay.io/passmcr/languagecomparison /bin/bash`

*Note: Running docker on Windows or MacOSX (currently) requires the use of a [boot2docker VM](http://boot2docker.io/) or something similar. This obviously has an overhead associated with it - however as long as the tests are all run in a container, the results should be roughly consistent with those obtained outside of a container.*

## Generating HTML Output:
A HTML page can be generated in order to visualise the various run timings.
+ Run the script in `output` using `python3 ./generate_data.py`.
+ This runs all examples and optionally compiles if you pass the `-b` flag.
+ A HTML page (`benchmark.html`) with the results is generated and placed in the root directory of the project.
