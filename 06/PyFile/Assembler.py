########################################################################################################################
#                                                     IMPORTS                                                          #
########################################################################################################################
from glob import glob
from os.path import join
import re
from sys import argv

########################################################################################################################
#                                                     CONSTANTS                                                        #
########################################################################################################################
R = 'R'
FIRST_FREE_ADDR = 17
EOL = '\n'
ANNOTATION = '//'
LEFT_BR = '('
RIGHT_BR = ')'
AT_SIGN = '@'
DEC_A_INST = 0
SYMBOL_A_INST = 1
C_INST = 2
ZERO_TWO_BYTES = '{0:0>16}'
SYMBOLS = {"SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "SCREEN": 16384, "KBD": 24576}
for i in range(16):
    SYMBOLS[R + str(i)] = i
DESTS = {'': '000', 'M': '001', 'D': '010', 'MD': '011', 'A': '100', 'AM': '101', 'AD': '110', 'AMD': '111'}
COMPS = {'0': '0101010', '1': '0111111', '-1': '0111010', 'D': '0001100', 'A': '0110000', '!D': '0001101',
         '!A': '0110001', '-D': '0001111', '-A': '0110011', 'D+1': '0011111', 'A+1': '0110111', 'D-1': '0001110',
         'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011', 'A-D': '0000111', 'D&A': '0000000', 'D|A': '0010101',
         'M': '1110000', '!M': '1110001', '-M': '1110011', 'M+1': '1110111', 'M-1': '1110010', 'D+M': '1000010',
         'D-M': '1010011', 'M-D': '1000111', 'D&M': '1000000', 'D|M': '1010101', 'D<<': '0110000', 'D>>': '0010000',
         'A<<': '0100000', 'A>>': '0000000', 'M<<': '1100000', 'M>>': '1000000'}
JUMPS = {'': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011', 'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'}
BLANK = ''
EQ = '='
SHFTL = '<<'
SHFTR = '>>'
SCOL = ';'
COMMA = ','
DOT = '.'
SLASH = '/'
WHITE_SPACE = ' '
SHFT_PREFIX = '101'
C_PREFIX = '111'
HACK = '.hack'
ASM = '.asm'
WRITE = 'w'
UTF_ENCODING = 'utf-8'
INPUT_PATH = argv[1]


########################################################################################################################

class Parser(INPUT_PATH):
    """
    This is my parser that will get a *.asm file and will hold a table of all of it's commands and a table of all of
    their binary representation.
    """

    def __init__(self, input_path):
        """
        initializing a parse, by given input path.
        the parser will initialize a symbols commands and binary lists.
        the commands list will create itself via the _read_asm function.
        the parsed commands will generate via the _parse function.
        :param input_path:
        """
        self._symbols = SYMBOLS
        self._instructions = []
        self._binary_commands = []
        self._read_asm(input_path)

    def binary_commands(self):
        """
        binary commands getter
        :return: binary commands list
        """
        return self._binary_commands

    def _read_asm(self, input_path):
        """
        this function will generate to self._instructions a list of all the input's commands.
        :param input_path: the path of the asm file that needs to be read
        """
        curr_var_index = FIRST_FREE_ADDR  # =17
        with open(input_path) as asm_file:
            for curr_line in asm_file:
                if curr_line == EOL or curr_line.startswith(ANNOTATION):  # line is empty or just an annotation
                    pass
                # ignoring annotations like you are going to do with this one :) if there are non take \n as line's end
                curr_line = curr_line.split(ANNOTATION)[0]
                curr_line = curr_line.strip(EOL).strip
                if curr_line.startswith(LEFT_BR):  # line is (xxx)
                    line_end = curr_line.index(RIGHT_BR)
                    symbol = curr_line[1:line_end]
                    if symbol not in self._symbols.keys():
                        self._symbols[symbol] = curr_var_index
                        curr_var_index += 1
                    pass
                if curr_line.startswith(AT_SIGN):  # @ line
                    value = curr_line[1:]  # ignore @ sign
                    if value.isdigit():
                        instruction = AT_SIGN + value
                    elif value in self._symbols.keys():
                        instruction = AT_SIGN + str(self._symbols[value])
                    elif not is_int(value):
                        self._symbols[value] = curr_var_index
                        instruction = AT_SIGN + curr_var_index
                        curr_var_index += 1
                    self._instructions.append(instruction)
                else:  # c-inst
                    self._instructions.append(curr_line)

    @staticmethod
    def _instruction_type(inst):
        """
        checking the instruction type of given command
        :param inst: command to be checked
        :return: instruction type, either an
        """
        if inst.startswith(AT_SIGN):
            # definitely an a instruction thus need to check if its symbolic or decimal
            if inst[1].isdigit():
                return DEC_A_INST
            else:
                return SYMBOL_A_INST
        return C_INST

    @staticmethod
    def _c_instruction_parser(inst):
        """
        parsing a c instruction into destination comparator and jump
        :param inst: a command to be inspected
        :return:    comp dest and jump fields
        """
        c, d, j = BLANK, BLANK, BLANK
        if SCOL in inst and EQ in inst:
            inst = re.split(EQ + SCOL, inst)
            d, c, j = inst[0], inst[1], inst[2]
        elif EQ in inst:
            inst = inst.split(EQ)
            d, c = inst[0], inst[1]
        elif SCOL in inst:
            inst = inst.split(SCOL)
            c, j = inst[0], inst[1]
        return c, d, j

    def _binary_parsing(self, instruction):
        """
        parsing the commands list to a list of binary representations
        :param instruction:
        :return:
        """
        instruction_type = self._instruction_type(instruction)
        if instruction_type is C_INST:
            c, d, j = self._c_instruction_parser(instruction)
            if SHFTL or SHFTR in c:
                prefix = SHFT_PREFIX
            else:
                prefix = C_PREFIX
            b_inst = prefix + COMPS[c.strip()] + DESTS[d.strip()] + JUMPS[j.strip()]
        else:
            addr = instruction[1:] if instruction is DEC_A_INST else self._symbols[instruction[:]]
            b_inst = bin_repr(addr)
        return b_inst + EOL

    def parse(self):
        """
        this function will parse the commands to binary commands for the hack file and save every command to the binary
        list
        :return:
        """
        for cmd in self._instructions:
            self._binary_commands.append(self._binary_parsing(cmd))


def is_int(s):
    """
    check if s is a string that represents an integer or not
    :param s:
    :return:
    """
    try:
        int(s)
        return True
    except ValueError:
        return False


def bin_repr(instruction):
    """
    given an a-instruction this will generate a 16-bit representation of the instruction, meaning this will start with
    0000000000000000 - 16 zeroes and will change the relevant points.
    :param instruction: given a-instruction to compute
    :return:    the binary representation of the a-instruction
    """
    return ZERO_TWO_BYTES.format(str(bin(int(instruction)))[2:])


if __name__ == '__main__':
    paths = []
    if INPUT_PATH.endswith(ASM):
        paths.append(INPUT_PATH)
    else:  # its a folder of asms
        paths = [asm for asm in glob(join(INPUT_PATH, '*' + ASM))]
    for file in paths:
        hack_name = file[:file.index(DOT)] + HACK
        parser = Parser(file)
        parser.parse()
        with open(hack_name, mode=WRITE, encoding=UTF_ENCODING) as hack_file:
            for line in parser.binary_commands():
                hack_file.write(line)
        hack_file.close()
    pass
