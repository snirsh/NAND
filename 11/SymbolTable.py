########################################################################################################################
#                                                  SymbolTable                                                         #
# programmer : Snir Sharristh                                                                                          #
#                                                                                                                      #
# Provides a symbol table abstraction. the symbol table associates the identifier names found in the program with      #
# identifier names found in the program with identifier properties needed for compilation: type, kind and running index#
# The symbol table for jack programs has two nested scopes Class/Subroutine                                            #
########################################################################################################################


class SymbolTable:

    def __init__(self):
        """
        create a new empty symbol table
        """
        self._class_scope = {}
        self._subroutine_scope = {}
        self._var_ct = 0
        self._static_ct = 0
        self._field_ct = 0
        self._arg_ct = 0
        self._CTS = {'static': locals()['self']._static_ct, 'var': locals()['self']._var_ct,
                 'arg': locals()['self']._arg_ct,
                 'field': locals()['self']._field_ct}

    def startSubroutine(self):
        """
        starts a new subroutine scope (i.e, resets the subroutine's symbol table)
        """
        self._subroutine_scope = {}
        self._arg_ct = 0
        self._var_ct = 0

    def Define(self, name, type, kind):
        """
        defines a new identifier of a given name type and kind and assigns it a running index STATIC and FIELD
        identifiers have a class scope while ARG and VAR identifiers have a subroutine scope
        :param name: String
        :param id_type: String
        :param kind: (STATIC,FIELD,ARG, VAR)
        """
        index = self._CTS[kind]
        self._CTS[kind] += 1
        if kind == 'static' or kind == 'field':
            self._class_scope[name] = (index, type, kind)
        else:   # arg or var
            self._subroutine_scope[name] = (index, type, kind)

    def VarCount(self, kind):
        """
        Returns the number of variables of the given kind already defined in the current scope.
        :param kind: (STATIC,FIELD,ARG, VAR)
        :return: int
        """
        return self._CTS[kind]

    def KindOf(self, name):
        """
        Returns the kind of the named identifier in the current scope. if the identifier is unknown in the current
        scope, returns NONE
        :param name: String
        :return: (STATIC,FIELD,ARG, VAR, NONE)
        """
        if name in self._class_scope.keys():
            return self._class_scope[name][2]
        elif name in self._subroutine_scope.keys():
            return self._subroutine_scope[name][2]
        return None

    def TypeOf(self, name):
        """
        returns the type of the named identifier in the current scope.
        :param name: String
        :return: String
        """
        if name in self._class_scope.keys():
            return self._class_scope[name][1]
        return self._subroutine_scope[name][1]

    def IndexOf(self, name):
        """
        returns the index assigned to the named identifier
        :param name: String
        :return: int
        """
        if name in self._class_scope.keys():
            return self._class_scope[name][0]
        return self._subroutine_scope[name][0]


