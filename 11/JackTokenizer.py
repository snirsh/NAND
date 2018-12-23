########################################################################################################################
#                                                   JackTokenizer                                                      #
# programmer : Snir Sharristh                                                                                          #
#                                                                                                                      #
# Removes all comments and white space from the input stream and breaks it into Jack-language tokens, as specified by  #
# the Jack grammar.                                                                                                    #
#                                                                                                                      #
########################################################################################################################
import os
import re


KEYWORDS = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean',
            'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
SYMBOLS = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '<', '>', '=', '~', '|']
BRACKETS = SYMBOLS[:6]
IDENTIFIER_REGEX = re.compile('[\\D](\\w\\S)*')  # not starting with num any char and _ without whitespaces
INTEGER_CONST_REGEX = re.compile('\\d{1,5}')  # any digits of size 1 to 5 chars that contain any of 0-9
STRING_CONST_REGEX = re.compile('\"[^\n\"]*\"')  # anything but " and \n that is wrapped in double quotes


class JackTokenizer(object):

    def __init__(self, input_file):
        """
        opens the input file/stream and gets ready to tokenize it.
        :param input_file: input file/stream
        """
        self.tokens = []
        self.__lines = []
        self.__file_name = ""
        if '.jack' in input_file:
            curr_file = os.path.abspath(input_file)
            self.__single_jack_tokenizer(curr_file)
            self.token_number = 0
            self.current_token = ""
            self.__tokenize()
        else:
            for dir_path, _, filenames in os.walk(input_file):
                for file in filenames:
                    self.__lines = []
                    self.tokens = []
                    if not file.endswith('.jack'):
                        continue
                    curr_file = os.path.abspath(os.path.join(dir_path, file))
                    self.__single_jack_tokenizer(curr_file)
                    self.token_number = 0
                    self.current_token = ""
                    self.__tokenize()

    def __single_jack_tokenizer(self, curr_file):
        self.__file_name = curr_file.split('.jack')[0]
        with open(curr_file, 'r') as jack_file:
            for line in jack_file.read().splitlines():
                line = line.strip()
                prefix = ['/**', '//', '*', '*/']
                if line.startswith(tuple(prefix)) or not line:
                    continue
                self.__lines.append(line.strip().split('//')[0])

    def hasMoreTokens(self):
        """
        this function checks if we have more tokens in the input
        :return: Boolean
        """
        return len(self.tokens) - self.token_number > 0

    def advance(self):
        """
        this function gets the next token from the input and makes it the current token.
        this method should only be called if hasMoreTokens() is true.
        initially there is no current token.
        :return:
        """
        self.current_token = self.tokens[self.token_number]
        self.token_number += 1

    def tokenType(self):
        """
        returns the type of the current token
        :return: a string: KEYWORD, SYMBOL, IDENTIFIER, INT_CONST, STRING_CONST, INVALID_TOKEN_TYPE
        """
        if self.current_token in KEYWORDS:
            return 'KEYWORD'
        elif self.current_token in SYMBOLS:
            return 'SYMBOL'
        elif STRING_CONST_REGEX.match(self.current_token) is not None:
            return 'STRING_CONST'
        elif IDENTIFIER_REGEX.match(self.current_token) is not None:
            return 'IDENTIFIER'
        elif INTEGER_CONST_REGEX.match(self.current_token) is not None:
            return 'INT_CONST'
        else:
            return 'INVALID_TOKEN_TYPE'

    def keyWord(self):
        """
        returns the keyword which is the current token. should be called only when tokenType() is KEYWORD
        :return: one of the strings in KEYWORD_TYPES
        """
        return self.current_token

    def symbol(self):
        """
        returns the character which is the current token. should be called only when tokenType() is SYMBOL
        :return: Char
        """
        return self.current_token

    def identifier(self):
        """
        returns the identifier which is the current token. should be called only when tokenType() is IDENTIFIER
        """
        return self.current_token

    def intVal(self):
        """
        returns the integer value which is the current token. should be called only when tokenType() is INT_CONST
        """
        return self.current_token

    def stringVal(self):
        """
        returns the string value which is the current token. should be called only when tokenType() is STRING_CONST
        """
        return self.current_token.strip('"')

    def peek(self):
        return self.tokens[self.token_number]

    def __tokenize(self):
        reg = re.compile('\"[^\n\"]*\"|[{}()\\[\\]+\\-*/&<>,;.=~|]|\\w+')
        for line in self.__lines:
            for token in reg.findall(line):
                self.tokens.append(token)
