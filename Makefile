
.DEFAULT_GOAL := all

.PHONY: all linux-setup

EXTERNALS = python3 date asdf catlify

missing_deps := $(foreach exec,$(EXTERNALS),$(if $(shell which $(exec)),,$(exec)))

help:	## prints available targets and why they exist
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

linux-setup:	## setup linux
	apt install $(missing_deps)

A := did $(C)
B = did $(C)
C = you understand?

all:	## will do it all
	$(info $(A))
	$(info $(B))
	$(info target is '$@')
	#$(info $(missing_dependencies))
