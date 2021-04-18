.PHONY: clean
files=%.py %.md examples Makefile tags
curr_dir=$(shell pwd | ls)

clean:
	rm -rf $(filter-out $(files),$(curr_dir))

