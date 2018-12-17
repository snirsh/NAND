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
import ntpath
import sys
from lxml import etree as ET
from JackTokenizer import *

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
        self.xml_file = ET
        self.CompileClass()
        __tree = self.xml_file.ElementTree(self._root)
        __tree.write(output_path, method='xml', pretty_print=True, encoding='utf-8')

    def CompileClass(self):
        """
        Compiles a complete class.
        """
        self._root = self.xml_file.Element('class')
        self.tokenizer.advance()
        self._write_line(self._root, self.tokenizer.keyWord())
        self.tokenizer.advance()
        self._write_line(self._root, self.tokenizer.identifier())
        self.tokenizer.advance()
        self._write_line(self._root, self.tokenizer.symbol())
        self.CompileClassVarDec()
        self.CompileSubroutine()
        self.tokenizer.advance()
        self._write_line(self._root, self.tokenizer.symbol())

    def _write_line(self, node, name):
        """
        writes the current node to the output file
        :param name: the name of the node
        """
        self.xml_file.SubElement(node, TYPES[self.tokenizer.tokenType()]).text = ' ' + name + ' '

    def CompileClassVarDec(self):
        """
        Compiles a static declaration or a field declaration.
        """
        peek = self.tokenizer.peek()
        if 'static' in peek or 'field' in peek:
            _classVarNode = self.xml_file.SubElement(self._root, 'classVarDec')
        while 'static' in peek or 'field' in peek:
            self.tokenizer.advance()
            self._write_line(_classVarNode, self.tokenizer.keyWord())  # field/static
            self.tokenizer.advance()
            self._write_line(_classVarNode, self.tokenizer.keyWord())  # type
            self.tokenizer.advance()
            self._write_line(_classVarNode, self.tokenizer.identifier())  # name
            self.tokenizer.advance()
            while self.tokenizer.symbol() == ',':
                self._write_line(_classVarNode, self.tokenizer.symbol())  # ,
                self.tokenizer.advance()
                self._write_line(_classVarNode, self.tokenizer.identifier())  # name
                self.tokenizer.advance()
            self._write_line(_classVarNode, self.tokenizer.symbol())  # ;
            peek = self.tokenizer.peek()
            if 'static' in peek or 'field' in peek:
                _classVarNode = self.xml_file.SubElement(self._root, 'classVarDec')

    def CompileSubroutine(self):
        """
        Compiles a complete method, function, or constructor.
        """
        _last_node = self._current_node
        _subroutineNode = self.xml_file.SubElement(self._root, 'subroutineDec')
        self._current_node = _subroutineNode
        peek = self.tokenizer.peek()
        while 'function' in peek or 'constructor' in peek or 'method' in peek:
            self.tokenizer.advance()
            self._write_line(_subroutineNode, self.tokenizer.keyWord())  # const/func/method
            self.tokenizer.advance()
            self._write_line(_subroutineNode, self.tokenizer.current_token)  # void/type
            self.tokenizer.advance()
            self._write_line(_subroutineNode, self.tokenizer.identifier())  # name
            self.tokenizer.advance()
            self._write_line(_subroutineNode, self.tokenizer.symbol())  # '('
            self.CompileParameterList()
            self.tokenizer.advance()
            self._write_line(_subroutineNode, self.tokenizer.symbol())  # ')'
            self.tokenizer.advance()
            self._current_node = self.xml_file.SubElement(_subroutineNode, 'subroutineBody')
            self._write_line(self._current_node, self.tokenizer.symbol())  # '{'
            peek = self.tokenizer.peek()
            if 'var' in peek:
                self.CompileVarDec()
            self.CompileStatements()
            self.tokenizer.advance()
            self._write_line(self._current_node, self.tokenizer.symbol())  # '}'
            peek = self.tokenizer.peek()
            if 'function' in peek or 'constructor' in peek or 'method' in peek:
                _subroutineNode = self.xml_file.SubElement(self._root, 'subroutineDec')
                self._current_node = _subroutineNode

    def CompileParameterList(self):
        """
        Compiles a (possibly empty) parameter list, not including the enclosing ‘‘ () ’’.
        """
        param_list = self.xml_file.SubElement(self._current_node, 'parameterList')
        peek = self.tokenizer.peek()
        if peek != ')':
            self.tokenizer.advance()
            self._write_line(param_list, self.tokenizer.keyWord())  # type
            self.tokenizer.advance()
            self._write_line(param_list, self.tokenizer.identifier())  # name
            peek = self.tokenizer.peek()
        while peek == ',':
            self.tokenizer.advance()
            self._write_line(param_list, self.tokenizer.symbol())  # ','
            self.tokenizer.advance()
            self._write_line(param_list, self.tokenizer.keyWord())  # type
            self.tokenizer.advance()
            self._write_line(param_list, self.tokenizer.identifier())  # name
            peek = self.tokenizer.peek()
        if not param_list.text:
            param_list.text = '\n'

    def CompileVarDec(self):
        """
        Compiles a var declaration.
        """
        _varDecNode = self.xml_file.SubElement(self._current_node, 'varDec')
        peek = self.tokenizer.peek()
        while 'var' in peek:
            self.tokenizer.advance()
            self._write_line(_varDecNode, self.tokenizer.keyWord())
            self.tokenizer.advance()
            self._write_line(_varDecNode, self.tokenizer.keyWord())
            self.tokenizer.advance()
            self._write_line(_varDecNode, self.tokenizer.identifier())
            self.tokenizer.advance()
            while self.tokenizer.symbol() == ',':
                self._write_line(_varDecNode, self.tokenizer.symbol())  # ,
                self.tokenizer.advance()
                self._write_line(_varDecNode, self.tokenizer.identifier())  # name
                self.tokenizer.advance()
            self._write_line(_varDecNode, self.tokenizer.symbol())  # ;
            peek = self.tokenizer.peek()
            if peek == 'var':
                _varDecNode = self.xml_file.SubElement(self._current_node, 'varDec')

    def CompileStatements(self):
        """
        Compiles a sequence of statements, not including the enclosing ‘‘{}’’.
        """
        peek = self.tokenizer.peek()
        _parent = self._current_node
        self._current_node = ET.SubElement(self._current_node, 'statements')
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
        self._current_node = _parent

    def CompileDo(self):
        """
        Compiles a do statement.
        """
        _last_node = self._current_node
        _statement = self.xml_file.SubElement(self._current_node, 'doStatement')
        self._current_node = _statement
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.keyWord())
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.identifier())
        peek = self.tokenizer.peek()
        while peek == '.':
            self.tokenizer.advance()
            self._write_line(_statement, self.tokenizer.symbol())
            self.tokenizer.advance()
            self._write_line(_statement, self.tokenizer.identifier())
            peek = self.tokenizer.peek()
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.symbol())  # '('
        self.CompileExpressionList()
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.symbol())  # ')'
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.symbol())  # ';'
        self._current_node = _last_node

    def CompileLet(self):
        """
        Compiles a let statement.
        """
        _last_node = self._current_node
        _statement = self.xml_file.SubElement(self._current_node, 'letStatement')
        self._current_node = _statement
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.keyWord())
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.identifier())
        peek = self.tokenizer.peek()
        if peek == '[':
            self.tokenizer.advance()
            self._write_line(_statement, self.tokenizer.symbol())  # '['
            self.tokenizer.advance()
            self.CompileExpression()
            self.tokenizer.advance()
            self._write_line(_statement, self.tokenizer.symbol())  # ']'
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.symbol())  # '='
        self.tokenizer.advance()
        self.CompileExpression()
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.symbol())  # ';'
        self._current_node = _last_node

    def CompileWhile(self):
        """
        Compiles a while statement.
        """
        _last_node = self._current_node
        _statement = self.xml_file.SubElement(self._current_node, 'whileStatement')
        self._current_node = _statement
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.keyWord())  # while
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.symbol())  # '('
        self.tokenizer.advance()
        self.CompileExpression()
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.symbol())  # ')'
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.symbol())  # '{'
        self.CompileStatements()
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.symbol())  # '}'
        self._current_node = _last_node

    def CompileReturn(self):
        """
        Compiles a return statement.
        """
        _last_node = self._current_node
        _statement = self.xml_file.SubElement(self._current_node, 'returnStatement')
        self._current_node = _statement
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.keyWord())  # return
        peek = self.tokenizer.peek()
        if peek != ';':
            self.tokenizer.advance()
            self.CompileExpression()
            self.tokenizer.advance()
        else:
            self.tokenizer.advance()
        self._write_line(self._current_node, self.tokenizer.symbol())  # ';'
        self._current_node = _last_node

    def CompileIf(self):
        """
        Compiles an if statement, possibly with a trailing else clause.
        """
        _last_node = self._current_node
        _statement = self.xml_file.SubElement(self._current_node, 'ifStatement')
        self._current_node = _statement
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.keyWord())  # if
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.symbol())  # '('
        self.tokenizer.advance()
        self.CompileExpression()
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.symbol())  # ')'
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.symbol())  # '{'
        self.CompileStatements()
        self.tokenizer.advance()
        self._write_line(_statement, self.tokenizer.symbol())  # '}'
        peek = self.tokenizer.peek()
        if peek == 'else':
            self.tokenizer.advance()
            self._write_line(_statement, self.tokenizer.keyWord())  # else
            self.tokenizer.advance()
            self._write_line(_statement, self.tokenizer.symbol())  # '{'
            self.CompileStatements()
            self.tokenizer.advance()
            self._write_line(_statement, self.tokenizer.symbol())  # '}'
        self._current_node = _last_node

    def CompileExpression(self):
        """
        Compiles an expression.
        """
        _last_node = self._current_node
        self._current_node = self.xml_file.SubElement(self._current_node, 'expression')
        self.CompileTerm()
        peek = self.tokenizer.peek()
        while peek in OPS:
            self.tokenizer.advance()
            self._write_line(self._current_node, self.tokenizer.symbol())
            self.tokenizer.advance()
            self.CompileTerm()
            peek = self.tokenizer.peek()
        self._current_node = _last_node

    def CompileTerm(self):
        """
        Compiles a term. This routine is faced with a slight difficulty when trying to decide between some of the
        alternative parsing rules. Specifically, if the current token is an identifier, the routine must distinguish
        between a variable, an array entry, and a subroutine call. A single look-ahead token, which may be one
        of ‘‘[’’, ‘‘(’’, or ‘‘.’’ suffices to distinguish between the three possibilities. Any other token is not
        part of this term and should not be advanced over.
        """
        term_branch = self.xml_file.SubElement(self._current_node, 'term')
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
        self._current_node = self.xml_file.SubElement(self._current_node, 'expressionList')
        peek = self.tokenizer.peek()
        while peek != ')':
            self.tokenizer.advance()
            if peek == ',':
                self._write_line(self._current_node, self.tokenizer.symbol())
                self.tokenizer.advance()
            self.CompileExpression()
            peek = self.tokenizer.peek()
        if not self._current_node.text:
            self._current_node.text = '\n'
        self._current_node = last_node
