########################################################################################################################
#                                                   JackTokenizer                                                      #
# programmer : Snir Sharristh                                                                                          #
#                                                                                                                      #
# Removes all comments and white space from the input stream and breaks it into Jack-language tokens, as specified by  #
# the Jack grammar.                                                                                                    #
#                                                                                                                      #
########################################################################################################################
import re

KEYWORDS = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean',
            'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
SYMBOLS = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', ',', '<', '>', '=', ' ~ ']
IDENTIFIER_REGEX = re.compile("^[\\D](\\w)+(\\S)")  # not starting with num any char and _ without whitespaces
INTEGER_CONST_REGEX = re.compile("\\d{1,5}")  # any digits of size 1 to 5 chars that contain any of 0-9
STRING_CONST_REGEX = re.compile("^[\\\"]([^\n\\\"]+)[$\\\"]")  # anything but " and \n that is wrapped in double quotes


class JackTokenizer(object):

    def __init__(self, input_file):
        """
        opens the input file/stream and gets ready to tokenize it.
        :param input_file: input file/stream
        """
        self.tokens = []
        with open(input_file, 'r') as jack_file:
            for line in jack_file.readlines():
                if line.startswith("/**"):
                    continue
                self.tokens.append(line.strip().split('//')[0])
        self.line_number = 0
        self.current_token = ""

    def hasMoreTokens(self):
        """
        this function checks if we have more tokens in the input
        :return: Boolean
        """
        return self.line_number > 0

    def advance(self):
        """
        this function gets the next token from the input and makes it the current token.
        this method should only be called if hasMoreTokens() is true.
        initially there is no current token.
        :return:
        """
        self.current_token = self.tokens[self.line_number].strip().split('//')[0]
        self.line_number += 1

    def tokenType(self):
        """
        returns the type of the current token
        :return: a string: KEYWORD, SYMBOL, IDENTIFIER, INT_CONST, STRING_CONST, INVALID_TOKEN_TYPE
        """
        if self.current_token in KEYWORDS:
            return 'KEYWORD'
        elif self.current_token in SYMBOLS:
            return 'SYMBOL'
        elif IDENTIFIER_REGEX.match(self.current_token) is not None:
            return 'IDENTIFIER'
        elif INTEGER_CONST_REGEX.match(self.current_token) is not None:
            return 'INT_CONST'
        elif STRING_CONST_REGEX.match(self.current_token) is not None:
            return 'STRING_CONST'
        else:
            return 'INVALID_TOKEN_TYPE'

    def keyWord(self):
        """
        returns the keyword which is the current token. should be called only when tokenType() is KEYWORD
        :return: one of the strings in KEYWORD_TYPES
        """
        return self.current_token.upper()

    def symbol(self):
        """
        returns the character which is the current token. should be called only when tokenType() is SYMBOL
        :return: Char
        """
        return self.current_token

    def identifier(self):
        """
        returns the identifier which is the current token. shuold be called only when tokenType() is IDENTIFIER
        """
        return self.current_token

    def intVal(self):
        """
        returns the integer value which is the current token. shuold be called only when tokenType() is INT_CONST
        """
        return self.current_token

    def stringVal(self):
        """
        returns the string value which is the current token. shuold be called only when tokenType() is STRING_CONST
        """
        return self.current_token
