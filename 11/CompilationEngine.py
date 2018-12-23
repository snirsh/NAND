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
from lxml import etree as ET
from JackTokenizer import *
from SymbolTable import SymbolTable

TYPES = {'KEYWORD': 'keyword', 'SYMBOL': 'symbol', 'IDENTIFIER': 'identifier', 'INT_CONST': 'integerConstant',
         'STRING_CONST': 'stringConstant', 'INVALID_TOKEN_TYPE': 'INVALID_TOKEN_TYPE'}
OPS = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
UNARY_OP = ['-', '~']


class CompilationEngine:
    def __init__(self, input_path, output_path):
        """
        creates a new compilation engine with the given input and output. the next routine called must be compileClass()
        :param input_path: input stream/file
        :param output_path: output stream/file
        """
        self._root = None
        self._current_node = None
        self.tokenizer = JackTokenizer(input_path)
        self._class_name = ''
        self._if_ct = 0
        self._while_ct = 0
        self._symbols = SymbolTable()
        self.CompileClass()

    def CompileClass(self):
        """
        Compiles a complete class.
        """
        # self._root = ET.Element('class')
        # self._write_line(self._root, self.tokenizer.keyWord())
        self.tokenizer.advance()  # skip the keyword class
        self.tokenizer.advance()
        self._class_name = self.tokenizer.identifier()
        self.tokenizer.advance()  # skip '{'
        self.CompileClassVarDec()
        self.CompileSubroutine()
        self.tokenizer.advance()  # skip '}' and end the class compilation

    def _write_line(self, node, name):
        """
        writes the current node to the output file
        :param name: the name of the node
        """
        _ = ET.SubElement(node, TYPES[self.tokenizer.tokenType()])
        _.text = ' ' + name + ' '

    def CompileClassVarDec(self):
        """
        Compiles a static declaration or a field declaration.
        """
        peek = self.tokenizer.peek()
        while 'static' in peek or 'field' in peek:
            self.tokenizer.advance()
            kind = self.tokenizer.keyWord()  # field/static
            self.tokenizer.advance()
            type = self.tokenizer.keyWord()  # type
            self.tokenizer.advance()
            name = self.tokenizer.identifier()  # name
            self.tokenizer.advance()
            self._symbols.Define(name, type, kind)
            while self.tokenizer.symbol() == ',':
                self.tokenizer.advance()  # skip ','
                self._symbols.Define(self.tokenizer.identifier(), type, kind)  # name
                self.tokenizer.advance()
            peek = self.tokenizer.peek()  # skip ';'

    def CompileSubroutine(self):
        """
        Compiles a complete method, function, or constructor.
        """
        peek = self.tokenizer.peek()
        while 'function' in peek or 'constructor' in peek or 'method' in peek:
            self._symbols.startSubroutine()
            self.tokenizer.advance()
            # kind = self.tokenizer.keyWord()  # const/func/method
            self.tokenizer.advance()
            # type = self.tokenizer.current_token  # void/type
            self.tokenizer.advance()
            # name = self.tokenizer.identifier()  # name
            # self._symbols.Define(name, type, kind)
            self.tokenizer.advance()  # skip '('
            self.CompileParameterList()
            self.tokenizer.advance()  # skip ')'
            self.tokenizer.advance()  # skip '{'
            peek = self.tokenizer.peek()
            if 'var' in peek:
                self.CompileVarDec()
            self.CompileStatements()
            self.tokenizer.advance()  # skip '}'

    def CompileParameterList(self):  # TODO : VM_WRITER of function name
        """
        Compiles a (possibly empty) parameter list, not including the enclosing ()
        """
        # param_list = ET.SubElement(self._current_node, 'parameterList')
        kind = 'argument'
        peek = self.tokenizer.peek()
        if peek != ')':
            self.tokenizer.advance()
            type = self.tokenizer.keyWord()  # type
            self.tokenizer.advance()
            name = self.tokenizer.identifier()  # name
            peek = self.tokenizer.peek()
            self._symbols.Define(name, type, kind)
        while peek == ',':
            self.tokenizer.advance()
            self.tokenizer.advance()  # skip ','
            type = self.tokenizer.keyWord()  # type
            self.tokenizer.advance()
            name = self.tokenizer.identifier()  # name
            peek = self.tokenizer.peek()
            self._symbols.Define(name, type, kind)

    def CompileVarDec(self):
        """
        Compiles a var declaration.
        """
        peek = self.tokenizer.peek()
        while 'var' in peek:
            self.tokenizer.advance()
            type = self.tokenizer.keyWord()
            self.tokenizer.advance()
            kind = self.tokenizer.keyWord()
            self.tokenizer.advance()
            name = self.tokenizer.identifier()
            self.tokenizer.advance()
            self._symbols.Define(name, type, kind)
            while self.tokenizer.symbol() == ',':
                self.tokenizer.advance()  # skip ','
                name = self.tokenizer.identifier()  # name
                self.tokenizer.advance()
                self._symbols.Define(name, type, kind)
            peek = self.tokenizer.peek()

    def CompileStatements(self):  # TODO: add VM to each ones
        """
        Compiles a sequence of statements, not including the enclosing "{}"
        """
        peek = self.tokenizer.peek()
        while 'let' in peek or 'if' in peek or 'while' in peek or 'do' in peek or 'return' in peek:
            if 'let' in peek:
                self.CompileLet()
            elif 'if' in peek:
                self.CompileIf()
            elif 'while' in peek:
                self.CompileWhile()
            elif 'do' in peek:
                self.CompileDo()
            elif 'return' in peek:
                self.CompileReturn()
            peek = self.tokenizer.peek()

    def CompileDo(self):
        """
        Compiles a do statement.
        """
        self.tokenizer.advance()  # skip 'do' statement
        self.tokenizer.advance()
        name = self.tokenizer.identifier()  # name of what to call
        peek = self.tokenizer.peek()
        while peek == '.':
            self.tokenizer.advance()  # skip '.'
            name += '.'
            self.tokenizer.advance()
            name += self.tokenizer.identifier()
            peek = self.tokenizer.peek()
        self.tokenizer.advance()  # skip '('
        self.CompileExpressionList()
        self.tokenizer.advance()  # skip ')'
        self.tokenizer.advance()  # skip ';

    def CompileLet(self):
        """
        Compiles a let statement.
        """
        self.tokenizer.advance()  # skip 'let'
        self.tokenizer.advance()
        name = self.tokenizer.identifier()
        peek = self.tokenizer.peek()
        if peek == '[':
            self.tokenizer.advance()  # skip '['
            self.tokenizer.advance()
            self.CompileExpression()
            self.tokenizer.advance()  # skip ']'
        self.tokenizer.advance()  # skip '='
        self.tokenizer.advance()
        self.CompileExpression()
        self.tokenizer.advance()  # skip ';'

    def CompileWhile(self):
        """
        Compiles a while statement.
        """
        self.tokenizer.advance()  # skip while
        self.tokenizer.advance()
        self.tokenizer.advance()  # skip '('
        self.CompileExpression()
        self.tokenizer.advance()
        self.tokenizer.advance()  # skip '){'
        self.CompileStatements()
        self.tokenizer.advance()  # skip '}'

    def CompileReturn(self):
        """
        Compiles a return statement.
        """
        self.tokenizer.advance()    # skip 'return'
        peek = self.tokenizer.peek()
        if peek != ';':
            self.tokenizer.advance()
            self.CompileExpression()
            self.tokenizer.advance()
        else:
            self.tokenizer.advance()

    def CompileIf(self):
        """
        Compiles an if statement, possibly with a trailing else clause.
        """
        _last_node = self._current_node
        _statement = ET.SubElement(self._current_node, 'ifStatement')
        self._current_node = _statement
        self.tokenizer.advance()
        self.tokenizer.advance()    # skip if
        self.tokenizer.advance()    # skip '('
        self.CompileExpression()
        self.tokenizer.advance()    # skip ')'
        self.tokenizer.advance()    # skip '{'
        self.CompileStatements()
        self.tokenizer.advance()    # skip '}'
        peek = self.tokenizer.peek()
        if peek == 'else':
            self.tokenizer.advance()
            self.tokenizer.advance()    # skip 'else{'
            self.CompileStatements()
            self.tokenizer.advance()    # skip '}'

    def CompileExpression(self):    # TODO: VMWRITER Support
        """
        Compiles an expression.
        """
        self.CompileTerm()
        peek = self.tokenizer.peek()
        while peek in OPS:
            self.tokenizer.advance()
            self.tokenizer.advance()    # 'op'
            self.CompileTerm()
            peek = self.tokenizer.peek()

    def CompileTerm(self):  # TODO: VMWRITER Support
        """
        Compiles a term. This routine is faced with a slight difficulty when trying to decide between some of the
        alternative parsing rules. Specifically, if the current token is an identifier, the routine must distinguish
        between a variable, an array entry, and a subroutine call. A single look-ahead token, which may be one
        of [, (, or . suffices to distinguish between the three possibilities. Any other token is not
        part of this term and should not be advanced over.
        """
        term_branch = ET.SubElement(self._current_node, 'term')
        # self.tokenizer.advance()
        if self.tokenizer.tokenType() == 'INT_CONST' or self.tokenizer.tokenType() == 'KEYWORD':
            self._write_line(term_branch, self.tokenizer.current_token)
        elif self.tokenizer.tokenType() == 'STRING_CONST':
            self._write_line(term_branch, self.tokenizer.stringVal())
        elif self.tokenizer.current_token in UNARY_OP:
            self._write_line(term_branch, self.tokenizer.symbol())
            last_node = self._current_node
            self._current_node = term_branch
            self.tokenizer.advance()
            self.CompileTerm()
            self._current_node = last_node
        elif self.tokenizer.current_token in SYMBOLS:
            self._write_line(term_branch, self.tokenizer.symbol())
            self.tokenizer.advance()
            last_node = self._current_node
            self._current_node = term_branch
            self.CompileExpression()
            self._current_node = last_node
            self.tokenizer.advance()
            self._write_line(term_branch, self.tokenizer.symbol())
        else:
            self._write_line(term_branch, self.tokenizer.identifier())
            peek = self.tokenizer.peek()
            if '[' in peek or '(' in peek:
                self.tokenizer.advance()
                self._write_line(term_branch, self.tokenizer.symbol())
                self.tokenizer.advance()
                last_node = self._current_node
                self._current_node = term_branch
                self.CompileExpression()
                self._current_node = last_node
                self.tokenizer.advance()
                self._write_line(term_branch, self.tokenizer.symbol())
            elif '.' in peek:
                self.tokenizer.advance()
                self._write_line(term_branch, self.tokenizer.symbol())
                self.tokenizer.advance()
                self._write_line(term_branch, self.tokenizer.identifier())
                self.tokenizer.advance()
                self._write_line(term_branch, self.tokenizer.symbol())
                last_node = self._current_node
                self._current_node = term_branch
                self.CompileExpressionList()
                self._current_node = last_node
                self.tokenizer.advance()
                self._write_line(term_branch, self.tokenizer.symbol())

    def CompileExpressionList(self):
        """
        Compiles a (possibly empty) comma-separated list of expressions.
        """
        last_node = self._current_node
        self._current_node = ET.SubElement(self._current_node, 'expressionList')
        peek = self.tokenizer.peek()
        while peek != ')':
            self.tokenizer.advance()
            if peek == ',':
                self._write_line(self._current_node, self.tokenizer.symbol())
                self.tokenizer.advance()
            self.CompileExpression()
            peek = self.tokenizer.peek()
        self._current_node = last_node
