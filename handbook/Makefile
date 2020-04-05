BUILD=../docs/handbook
TMP=../tmp
ADOCS=$(shell find . -name '*.adoc')
HTML_OPTS=
UNET_LIB=../../unet/lib

.PHONY: all clean pdf html cmdref rouge-unet

html: ${BUILD}/unet-handbook.html
pdf: ${BUILD}/unet-handbook.pdf

${BUILD}/unet-handbook.pdf: handbook.adoc ${ADOCS}
	mkdir -p ${BUILD}
	mkdir -p ${TMP} ${TMP}/images
	cp custom-theme.yml ${TMP}
	rsync -a ${ADOCS} ${TMP}
	rsync -a images ${TMP}
	cd ${TMP}; sed -i -- 's/⤇/⇒/g' *.adoc
	cd ${TMP}; asciidoctor-pdf -a pdf-style=custom-theme.yml -o $@ $<

${BUILD}/unet-handbook.html: handbook.adoc ${ADOCS}
	mkdir -p ${BUILD}
	rsync -a images ${BUILD}
	asciidoctor ${HTML_OPTS} -o $@ $<
	python bin/chunk-adoc-html.py ${BUILD} unet-handbook
	cat redirect.html | sed 's/URL/unet-handbook_preface.html/' > ${BUILD}/index.html

# generate command reference from unet & fjage jars
# need to ensure jars are compiled and available in UNET_LIB folder
cmdref:
	rm -f cmdref.adoc
	python bin/doc2adoc.py ${UNET_LIB} > cmdref.adoc

# install rouge unet lexer
# might need to run with with sudo, if you don't have permissions
install:
	RB=`head -1 \`which rougify\` | sed 's/^..//'` && \
	RPATH=`dirname \`$$RB -e "require 'rubygems'; print Gem.bin_path('rouge', 'rougify', '>= 0.a')"\`` && \
	cp unet.rb $$RPATH/../lib/rouge/lexers/

clean:
	rm -rf ${BUILD} ${TMP}
