BUILD=build
ADOCS=$(shell find . -name '*.adoc')

.PHONY: all clean

all: ${BUILD}/unet-handbook.pdf

${BUILD}/unet-handbook.pdf: handbook.adoc ${ADOCS}
	mkdir -p build
	asciidoctor-pdf -o $@ $<

${BUILD}/unet-handbook.html: handbook.adoc ${ADOCS}
	mkdir -p build
	asciidoctor -o $@ $<

clean:
	rm -rf build
