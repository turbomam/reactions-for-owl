## Add your own custom Makefile targets here

.PHONY: examples-output-cleanup all-with-examples
examples-output-cleanup:
	rm -rf examples/output


all-with-examples: clean examples-output-cleanup all # test

.PHONY: plantuml-cleanup plantuml-all
plantuml-cleanup:
	rm -rf plantuml
plantuml-all: plantuml-cleanup plantuml.md
plantuml.md: src/reactions_for_owl/schema/reactions_for_owl.yaml
	$(RUN) echo '```plantuml' > $@ ; \
		gen-plantuml $< >> $@ ; \
		echo '```' >> $@

#local/meta.owl.ttl:
#	curl --output $@ "https://raw.githubusercontent.com/linkml/linkml-model/main/linkml_model/owl/meta.owl.ttl"
#
#.PHONY: robot-convert-schema
## todo this makes robot a system dependency for this project
##  provide installation instructions or provide a docker container
## todo create local directory and gitignore
## todo merge in skos, xsd...
#local/reactions_for_owl.converted.owl.ttl: project/owl/reactions_for_owl.owl.ttl
##	robot merge \
##		--input $(word 1, $^) \
##		--input $(word 2, $^) \
##		--output $@.tmp.ttl
##		--check true \
##		--strict
#	robot convert \
#		--input $< \
#		--output $@
#
#local/named_thing.owl.ttl: local/reactions_for_owl.converted.owl.ttl
#	robot extract \
#		--input $< \
#		--term "https://w3id.org/turbomam/reactions-for-owl/NamedThing" \
#		--method STAR \
#		--output $@
#
#local/named_thing.yaml: local/named_thing.owl.ttl
#	robot convert -i $< -o $<.ofn
#	$(RUN) schemauto import-owl $<.ofn > $@
#
#local/schemaorg.owl:
#	curl --output $@ "https://schema.org/docs/schemaorg.owl"
#
#local/schemaorg.ofn: local/schemaorg.owl
#	robot convert -i $< -o $@
#
#local/schemaorg.yaml: local/schemaorg.ofn
#	$(RUN) schemauto import-owl $< > $@
#	# INVALID ONTOLOGY FILE ERROR Could not load a valid ontology from file: schema.org.ttl