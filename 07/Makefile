###############################################################################
#
# Makefile for a script (e.g. Python), project 7
#
# Students:
# Aviv Yaish, ID 011111111, master.of.nand@cs.huji.ac.il
# Lisa Simpson, ID 022222222, lisa@cs.huji.ac.il
#
###############################################################################
FILES = CodeWriter.py Makefile Parser.py README VMtranslator VMtranslator.py

all:
	chmod 700 $(FILES)
	chmod a+x VMtranslator

tar:
	tar -cvf project7.tar $(FILES)

clean:
	rm project7.tar

test:
	test7.sh