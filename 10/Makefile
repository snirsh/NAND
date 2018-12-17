###############################################################################
#
# Makefile for a script (e.g. Python), project 10
#
# Students:
#   Snir Sharristh 305500001 snir.sharristh@mail.huji.ac.il
#
###############################################################################
FILES = JackAnalyzer.py Makefile JackTokenizer.py README JackAnalyzer CompilationEngine.py

all:
	chmod 700 $(FILES)
	chmod a+x VMtranslator

tar:
	tar -cvf project10.tar $(FILES)

clean:
	rm project10.tar

test:
	test10.sh