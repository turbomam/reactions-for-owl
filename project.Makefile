## Add your own custom Makefile targets here

.PHONY: examples-output-cleanup all-with-examples
examples-output-cleanup:
	rm -rf examples/output


all-with-examples: clean examples-output-cleanup all test
