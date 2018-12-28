########################################################################################################################
#                                               CodeGenerator                                                          #
# programmer : Snir Sharristh                                                                                          #
#                                                                                                                      #
########################################################################################################################
from CompilationEngine import CompilationEngine
from SymbolTable import SymbolTable
from VMWriter import VMWriter

class CodeGenerator:
    def __init__(self, input_path):
        cp = CompilationEngine(input_path)
        self.tree = cp.tree
        self._symbols = SymbolTable()
        self._writer = VMWriter()

