DIRS := ${shell ./getBuildableSolutions.sh}
SIEVESIZE := 10000000

buildall:
	@$(foreach dir, $(DIRS), $(MAKE) -C $(dir) build &&) true

cleanall:
	@$(foreach dir, $(DIRS), $(MAKE) -C $(dir) clean &&) true

runall:
	@$(foreach dir, $(DIRS), $(MAKE) SIEVESIZE=$(SIEVESIZE) -C $(dir) run && echo "\n\n" &&) true
