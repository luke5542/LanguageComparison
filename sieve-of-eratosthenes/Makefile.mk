dependenciesInstalled = $(foreach exec,$(EXECUTABLES),$(if $(shell command -v $(exec)),,$(error "No $(exec) in PATH - error in $(CURDIR))))

checkdeps: $(dependenciesInstalled)