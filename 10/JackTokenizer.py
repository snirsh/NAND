class JackTokenizer:
    KEYWORDS = []
    SYMBOLS = []

    TOKEN_TYPES = {'KEYWORD':KEYWORDS, 'SYMBOL':SYMBOLS, 'IDENTIFIER':'_', 'INT_CONST':'\d', 'STRING_CONST':'\"_\"'} # TODO: identifier regex
    KEYWORD_TYPES = ['CLASS','METHOD','FUNCTION','CONSTRUCTOR','INT','BOOLEAN','CHAR','VOID','VAR','STATIC','FIELD',
                     'LET','DO','IF','ELSE','WHILE','RETURN','TRUE','FALSE','NULL','THIS']

    def __init__(self, input_file):
        with open(input_file) as jack_file:
            self.tokens = jack_file.readlines()
        self.line_number = 0
        self.current_token = self.tokens[0]

    def hasMoreTokens(self):
        return self.line_number > 0

    def advance(self):
        self.line_number += 1
        self.current_token = self.tokens[self.line_number]

    def tokenType(self):
