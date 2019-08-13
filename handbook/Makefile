BUILD=build
ADOCS=$(shell find . -name '*.adoc')
HTML_OPTS=

.PHONY: all clean pdf html

html: ${BUILD}/unet-handbook.html
pdf: ${BUILD}/unet-handbook.pdf
all: pdf html

${BUILD}/unet-handbook.pdf: handbook.adoc ${ADOCS}
	mkdir -p ${BUILD}
	asciidoctor-pdf -o $@ $<

${BUILD}/unet-handbook.html: handbook.adoc ${ADOCS}
	mkdir -p ${BUILD}
	rsync -a images ${BUILD}
	asciidoctor ${HTML_OPTS} -o $@ $<
	python bin/chunk-adoc-html.py ${BUILD} unet-handbook

clean:
	rm -rf ${BUILD}

