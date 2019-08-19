BUILD=build
TMP=/tmp/unet-doc
ADOCS=$(shell find . -name '*.adoc')
HTML_OPTS=

.PHONY: all clean pdf html publish

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
	cat redirect.html | sed 's/URL/unet-handbook_preface.html/' > ${BUILD}/index.html

publish: html pdf
	rm -rf ${TMP}
	mkdir -p ${TMP}
	cd ${TMP}/..; git clone git@github.com:org-arl/unet-doc.git
	cd ${TMP}; git checkout gh-pages
	rm -rf ${TMP}/handbook
	mkdir -p ${TMP}/handbook
	cp -r ${BUILD}/* ${TMP}/handbook/
	cd ${TMP}; git add --all; git commit --amend --no-edit
	cd ${TMP}; git push origin --force

clean:
	rm -rf ${BUILD}

