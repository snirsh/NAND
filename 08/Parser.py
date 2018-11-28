########################################################################################################################
# FILE: Parser.py                                                                                                      #
# WRITERS: Snir Sharristh                                                                                              #
# DESCRIPTION: Handles the parsing of a single .vm file, and encapsulates access to the input code. It reads VM        #
# commands, parses them, and provides convenient access to their components. In addition, it removes all               #
# white space and comments                                                                                             #
########################################################################################################################
########################################################################################################################
#                                                     IMPORTS                                                          #
########################################################################################################################
from CodeWriter import ARITHMETIC_OPS as ARITHMETIC_CMDS

########################################################################################################################
#                                                     CONSTANTS                                                        #
########################################################################################################################
ANNOTATION_PREFIX = '//'
NEWLINE = '\n'
C_ARITHMETIC = 0
C_LABEL = 1
C_GOTO = 2
C_IF = 3
C_PUSH = 5
C_POP = 6
C_CALL = 7
C_RETURN = 8
C_FUNCTION = 9
cmd_types = {'add': C_ARITHMETIC, 'sub': C_ARITHMETIC, 'neg': C_ARITHMETIC,
              'eq': C_ARITHMETIC, 'gt': C_ARITHMETIC, 'lt': C_ARITHMETIC,
              'and': C_ARITHMETIC, 'or': C_ARITHMETIC, 'not': C_ARITHMETIC,
              'label': C_LABEL, 'goto': C_GOTO, 'if-goto': C_IF,
              'push': C_PUSH, 'pop': C_POP,
              'call': C_CALL, 'return': C_RETURN, 'function': C_FUNCTION}

########################################################################################################################


class Parser:

    def __init__(self, input_file):
        """
        Opens the input file/stream and gets ready to parse it.
        :param input_file:
        """
        self._commands = []
        self._commands_init(input_file)
        self._counter = 0

    def has_more_commands(self):
        """
        Are there more commands in the input?
        :return:
        """
        return self._counter < len(self._commands)

    def advance(self):
        """
        Reads the next command from the input and makes it the current command. Should be called only if
        hasMoreCommands() is true. Initially there is no current command.
        :return:
        """
        self._counter += 1

    def commandType(self):
        """
        Returns the type of the current VM command. C_ARITHMETIC is returned for all the arithmetic commands.
        :return:
        """
        return cmd_types[self.get_type()]

    def arg1(self):
        """
        Returns the first argument of the current
        command. In the case of C_ARITHMETIC,
        the command itself (add, sub, etc.) is
        returned. Should not be called if the current
        command is C_RETURN
        :return:
        """
        cmd_type = self.get_type()
        cmd = self._get_cmd()
        if cmd_type in ARITHMETIC_CMDS:
            return cmd[0]
        return cmd[1]

    def arg2(self):
        """
        Returns the second argument of the current command. Should be called only if the current command is C_PUSH,
        C_POP, C_FUNCTION, or C_CALL.
        :return:
        """
        cmd = self._commands[self._counter].rsplit()
        return int(cmd[2])

    def _commands_init(self, input_file):
        """
        this gets a file and reads a line
        :param input_file:
        :return:
        """
        with open(input_file, mode='r') as file:
            for line in file:
                try:
                    pos = line.index(ANNOTATION_PREFIX)
                except:
                    pos = len(line)
                line = line[:pos]
                line = line.strip()
                if line:
                    self._commands.append(line)

    def _get_cmd(self):
        """
        this returns current command that is being processed
        :return:
        """
        return self._commands[self._counter].rsplit()

    def get_type(self):
        """
        returns command type as string
        :return:
        """
        return self._commands[self._counter].rsplit()[0]
