BUILD=../docs/handbook
TMP=/tmp/unet-doc
ADOCS=$(shell find . -name '*.adoc')
HTML_OPTS=
UNET_LIB=../../unet/lib

.PHONY: all clean pdf html cmdref

html: ${BUILD}/unet-handbook.html
pdf: ${BUILD}/unet-handbook.pdf
all: pdf html

${BUILD}/unet-handbook.pdf: handbook.adoc ${ADOCS}
	mkdir -p ${BUILD}
	asciidoctor-pdf -a pdf-style=custom-theme.yml -o $@ $<

${BUILD}/unet-handbook.html: handbook.adoc ${ADOCS}
	mkdir -p ${BUILD}
	rsync -a images ${BUILD}
	asciidoctor ${HTML_OPTS} -o $@ $<
	python bin/chunk-adoc-html.py ${BUILD} unet-handbook
	cat redirect.html | sed 's/URL/unet-handbook_preface.html/' > ${BUILD}/index.html

cmdref:
	rm -f cmdref.adoc
	python bin/doc2adoc.py ${UNET_LIB} > cmdref.adoc

clean:
	rm -rf ${BUILD}

