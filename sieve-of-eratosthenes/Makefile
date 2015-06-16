test = date

DIRS := ${shell find * -maxdepth 0 -type d -print}
SIEVESIZE := 10000000

buildall:
	@$(foreach dir, $(DIRS), $(MAKE) -C $(dir) build && echo "\n\n" &&) true

cleanall:
	@$(foreach dir, $(DIRS), $(MAKE) -C $(dir) clean && echo "\n\n" &&) true

runall:
	@$(foreach dir, $(DIRS), $(MAKE) SIEVESIZE=$(SIEVESIZE) -C $(dir) run && echo "\n\n" &&) true