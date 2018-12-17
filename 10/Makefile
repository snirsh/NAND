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
	chmod a+x JackAnalyzer

tar:
	tar -cvf project10.tar $(FILES)

clean:
	rm project10.tar

test:
	chmod 700 $(FILES)
	test10.sh
