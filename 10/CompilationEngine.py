########################################################################################################################
#                                               CompilationEngine                                                      #
# programmer : Snir Sharristh                                                                                          #
#                                                                                                                      #
# Effects the actual compilation output. Gets its input from a JackTokenizer and emits its parsed structure into an    #
# Ouput file /stream. the output is generated by a series of compilexxx() routines, one for every syntactic element    #
# xxx of the Jack grammer. The contract between these routines is that each compilexxx() routine should read the       #
# syntactic construct xxx from the input, advance() the tokenizer exactly beyond xxx, and output the parsing of xxx.   #
# Thus, compilexxx() may only be called if indeed xxx is the next syntactic element of the input.                      #
#                                                                                                                      #
########################################################################################################################

class CompilationEngine:
    def __init__(self, input, output):
        """
        creates a new compilation engine with the given input and output. the next routine called must be compileClass()
        :param input: input stream/file
        :param output: output stream/file
        """
        pass
