###############################################################################
#
# Makefile for a script (e.g. Python), project 11
#
# Students:
#   Snir Sharristh 305500001 snir.sharristh@mail.huji.ac.il
#
###############################################################################
FILES = JackAnalyzer.py Makefile JackTokenizer.py README JackCompiler CompilationEngine.py SymbolTable.py VMWriter.py

all:
	chmod a+x JackCompiler

tar:
	tar -cvf project11.tar $(FILES)

clean:
	rm project11.tar

test:
	chmod 700 $(FILES)
	test11.sh
