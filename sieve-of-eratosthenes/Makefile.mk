dependenciesInstalled = $(foreach exec,$(EXECUTABLES),$(if command -v $(exec),,$(error "No $(exec) in PATH - error in $(CURDIR))))

checkdeps: $(dependenciesInstalled)
