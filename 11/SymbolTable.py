########################################################################################################################
#                                                  SymbolTable                                                         #
# programmer : Snir Sharristh                                                                                          #
#                                                                                                                      #
# Provides a symbol table abstraction. the symbol table associates the identifier names found in the program with      #
# identifier names found in the program with identifier properties needed for compilation: type, kind and running index#
# The symbol table for jack programs has two nested scopes Class/Subroutine                                            #
########################################################################################################################


from collections import namedtuple

Symbol = namedtuple('Symbol', ['kind', 'type', 'index'])


class JackClass:
    """A Jack class representation for the Jack compiler"""

    def __init__(self, class_name_input):
        self.class_name = class_name_input
        self.symbols = {}
        self.static_c = 0
        self.field_c = 0

    def add_var(self, name, var_type, kind):
        if kind == 'field':
            self.symbols[name] = Symbol('field', var_type, self.field_c)
            self.field_c += 1
        elif kind == 'static':
            self.symbols[name] = Symbol('static', var_type, self.static_c)
            self.static_c += 1

    def get_symbol(self, name):
        return self.symbols.get(name)


class JackSubroutine:
    def __init__(self, name, subroutine_type, return_type, jack_class):
        self.name = name
        self.jack_class = jack_class
        self.subroutine_type = subroutine_type
        self.return_type = return_type
        self.symbols = {}
        self.args_c = 0
        self.var_c = 0
        if subroutine_type == 'method':
            self.add_arg('this', self.jack_class.class_name)

    def add_arg(self, name, var_type):
        self.symbols[name] = Symbol('arg', var_type, self.args_c)
        self.args_c += 1

    def add_var(self, name, var_type):
        self.symbols[name] = Symbol('var', var_type, self.var_c)
        self.var_c += 1

    def get_symbol(self, name):
        symbol = self.symbols.get(name)
        if symbol is not None:
            return symbol

        return self.jack_class.get_symbol(name)
