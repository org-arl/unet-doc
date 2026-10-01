Prerequisites
-------------

* ruby, python3
* `gem install asciidoctor`
* `gem install asciidoctor-pdf --pre`
* `gem install rouge`
* `pip install beautifulsoup4`
* `pip install lxml`

One-time installation
---------------------

* `make install` (or `sudo make install`) -- install rouge unet lexer

Documentation generation
------------------------

* `make cmdref` -- creates command reference from unet jars in `../../unet/lib` (compiled with `gradle all`)
* `make html` -- generates html handbook
* `make pdf` -- generates pdf handbook
