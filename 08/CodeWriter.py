########################################################################################################################
# FILE: CodeWriter.py                                                                                                  #
# WRITERS: Snir Sharristh                                                                                              #
# DESCRIPTION: This Beast Translates VM commands into Hack assembly code.                                              #
########################################################################################################################
########################################################################################################################
#                                                     CONSTANTS                                                        #
########################################################################################################################
DEBUG = False
VM_SUFFIX = '.vm'
COMMANDS = {'add': 'M+D', 'sub': 'M-D', 'neg': 'D-M', 'eq': 'JEQ', 'gt': 'JGT', 'lt': 'JLT', 'and': 'M&D', 'or': 'M|D',
            'not': '!M'}
BINARY_OPS = ['add', 'sub', 'and', 'or']
UNARY_OPS = ['neg', 'not']
COMP_OPS = ['gt', 'lt', 'eq']
POP_OR_PUSH = ['pop', 'push']
ARITHMETIC_OPS = BINARY_OPS + UNARY_OPS + COMP_OPS
DOT_FORMAT = '{}.{}'
SEGMENTS = {'local': 'LCL', 'argument': 'ARG', 'this': 'THIS', 'that': 'THAT', 'static': DOT_FORMAT, 'pointer': 3,
            'temp': 5}
POINTERS = ['local', 'argument', 'this', 'that']
A_CMD = 0
C_CMD = 1
L_CMD = 2
NEWLINE = '\n'
SEMICOL = ';'
AT_SIGN = '@'
SP = 'SP'
TEMP_REG1 = 'R13'
TEMP_REG2 = 'R14'
COMP_ARG = 'R2'
LABEL_REGEX = '({})'
ANNOTATION_PREFIX = '//'
TRUE = 0
FALSE = -1
NEITHER = 1
FIRST_NUMBER_IS_NEGETIVE = 'FNEG.'
SECOND_NUMBER_IS_NEGETIVE = 'SNEG.'
FIRST_NUMBER_IS_POS = 'FPOS.'
SECOND_NUMBER_IS_POS = 'SPOS.'
IF_STATEMENT_TRUE = 'IF.'
IF_STATEMENT_FALSE = 'ELSE.'
CHECK_SUM = 'CHCK.'
CHECK_ALL = 'ANS.'
CHOOSE_A = True
CHOOSE_AM = False
DOT = '.'
SLASH = '/'
WRITE_MODE = 'w'
BLANK = ''
INIT_RAM = 256
UNCONDITIONAL_JUMP = [None, '0', 'JMP']
CONDITIONAL_JNE = [None, 'D', 'JNE']


########################################################################################################################


class CodeWriter:
    """
    a class that will help us Translate VM commands into Hack assembly code.
    """

    def __init__(self, output_file, curr_input, num_of_files):
        """
        initializing
        :param output_file: file to be written to
        :param curr_input: the current file that is read (multiple files can be read for a single output file)
        :param num_of_files: the number of files that will be processed
        """
        self._file = open(output_file, mode=WRITE_MODE)
        # both of the file name and number of files are used for static variables
        self._file_name = curr_input.split(DOT)[0].split(SLASH)[-1]
        self._num_of_files = num_of_files
        self.setFileName(curr_input)
        self._labels = 0
        self._calls = 0
        self._scope = 'global'

    def setFileName(self, file_name):
        """
        this function sets the name of the current file that is being processed and clears regs R13-15 just to be sure
        :param file_name:
        :return:
        """
        if self._num_of_files > 1:
            self._file_name += str(self._num_of_files)

    def setNumOfFiles(self, num):
        """
        this sets the number of files that will be processed this is for extra caution
        :param num: number of files
        :return:
        """
        self._num_of_files = num

    def _inc_dec_m(self, inc=True):
        """
        this function writes the line M=M+1 or M=M-1 according to Inc
        :param inc: boolean that represents if we wand an increment or decrement
        :return:
        """
        if inc:
            self._write_cmd(['M', 'M+1'], C_CMD)
        elif not inc:
            self._write_cmd(['M', 'M-1'], C_CMD)

    def _load_sp(self):
        """
        @SP
        :return:
        """
        self._write_cmd([SP], A_CMD)

    def _load_from_m(self, target):
        """
        target = M
        :param target:
        :return:
        """
        self._write_cmd([target, 'M'], C_CMD)

    def _save_to_m(self, comp):
        """
        M=comp
        :param comp:
        :return:
        """
        self._write_cmd(['M', comp], C_CMD)

    def _write_cmd(self, adr, c_type):
        """
        writes a given command by the command type c_type
        :param adr: represents the address that we want to work on
        :param c_type:  represents the command type either C-Inst A-Inst or Lable
        :return:
        """
        if c_type == A_CMD:  # A instruction, @given_address
            self._file.write(AT_SIGN + str(adr[0]) + NEWLINE)
        elif c_type == C_CMD:  # C instruction
            if adr[0]:
                self._file.write(adr[0] + '=')
            self._file.write(adr[1])
            if len(adr) > 2 and adr[2]:
                self._file.write(SEMICOL + adr[2])
            self._file.write(NEWLINE)
        elif c_type == L_CMD:  # LABEL
            label = LABEL_REGEX.format(adr[0])
            self._file.write(label + '\n')

    def _load_to_reg(self, reg_to_load):
        """
        @SP
        AM=M-1
        D=M
        @reg_to_load
        M=D
        :param reg_to_load: register that we want to load
        :return:
        """
        self._dec_sp(flag_A_or_AM=CHOOSE_AM)
        self._write_cmd([reg_to_load], A_CMD)
        self._save_to_m('D')

    def _dec_sp(self, if_answer=NEITHER, flag_A_or_AM=CHOOSE_A):
        """
        saving to M after A or AM decrementation
        :param if_answer:   If it's for an if statement we choose TRUE = 0 or FALSE = -1
        :param flag_A_or_AM: CHOOSE A OR CHOOSE AM to save to
        :return:
        """
        self._load_sp()
        if flag_A_or_AM:
            self._write_cmd(['A', 'M-1'], C_CMD)
        elif not flag_A_or_AM:
            self._write_cmd(['AM', 'M-1'], C_CMD)
        if if_answer == NEITHER:
            self._load_from_m('D')
        elif if_answer == TRUE:
            self._save_to_m(str(TRUE))
        elif if_answer == FALSE:
            self._save_to_m(str(FALSE))

    def _check_overflow(self, op):
        """
        this function checks overflow by checking the signs of given inputs.
        it's based on the idea that if we compare A and B then the only hazard is when both have different signs.
        meaning if A<0 and B>0 or A>0 and B<0
        thus we are checking which one is positive and which one is negative and by that we now how to avoid overflow.

        :param op:
        :return:
        """
        self._load_to_reg(TEMP_REG2)
        self._write_cmd([FIRST_NUMBER_IS_NEGETIVE + self._file_name + str(self._labels)], A_CMD)
        self._write_cmd([None, 'D', 'JLT'], C_CMD)
        self._dec_sp(flag_A_or_AM=CHOOSE_A)
        self._write_cmd([SECOND_NUMBER_IS_NEGETIVE + self._file_name + str(self._labels)], A_CMD)
        self._write_cmd([None, 'D', 'JLT'], C_CMD)
        self._write_cmd([CHECK_SUM + self._file_name + str(self._labels)], A_CMD)
        self._write_cmd([None, '0', 'JMP'], C_CMD)
        self._write_cmd([FIRST_NUMBER_IS_NEGETIVE + self._file_name + str(self._labels)], L_CMD)
        self._dec_sp(flag_A_or_AM=CHOOSE_A)
        self._write_cmd([SECOND_NUMBER_IS_POS + self._file_name + str(self._labels)], A_CMD)
        self._write_cmd([None, 'D', 'JGT'], C_CMD)
        self._write_cmd([CHECK_SUM + self._file_name + str(self._labels)], A_CMD)
        self._write_cmd([None, '0', 'JMP'], C_CMD)
        self._write_cmd([SECOND_NUMBER_IS_POS + self._file_name + str(self._labels)], L_CMD)
        self._write_cmd([COMP_ARG], A_CMD)
        self._write_cmd(['D', 'A'], C_CMD)
        self._write_cmd([CHECK_ALL + self._file_name + str(self._labels)], A_CMD)
        self._write_cmd([None, '0', 'JMP'], C_CMD)
        self._write_cmd([SECOND_NUMBER_IS_NEGETIVE + self._file_name + str(self._labels)], L_CMD)
        self._write_cmd([COMP_ARG], A_CMD)
        self._write_cmd(['D', '-A'], C_CMD)
        self._write_cmd([CHECK_ALL + self._file_name + str(self._labels)], A_CMD)
        self._write_cmd([None, '0', 'JMP'], C_CMD)
        self._write_cmd([CHECK_SUM + self._file_name + str(self._labels)], L_CMD)
        self._write_cmd([TEMP_REG2], A_CMD)
        self._write_cmd(['D', 'D-M'], C_CMD)
        self._write_cmd([CHECK_ALL + self._file_name + str(self._labels)], L_CMD)
        self._write_cmd([IF_STATEMENT_TRUE + self._file_name + str(self._labels)], A_CMD)
        self._write_cmd([None, 'D', COMMANDS[op]], C_CMD)
        self._dec_sp(if_answer=TRUE)
        self._write_cmd([IF_STATEMENT_FALSE + self._file_name + str(self._labels)], A_CMD)
        self._write_cmd([None, '0', 'JMP'], C_CMD)

    def _write_op(self, op):
        """
        this function write a given operation, either binary unary or compare.
        :param op:
        :return:
        """
        if op in BINARY_OPS:
            self._write_annotation('BINARY OP:' + op)
            self._dec_sp(flag_A_or_AM=CHOOSE_AM)
            self._write_cmd(['A', 'A-1'], C_CMD)
            self._save_to_m(COMMANDS[op])
        elif op in UNARY_OPS:
            self._write_annotation('UNARY OP:' + op)
            if op == 'neg':
                self._write_cmd(['D', '0'], C_CMD)
            self._load_sp()
            self._write_cmd(['A', 'M-1'], C_CMD)
            self._save_to_m(COMMANDS[op])
        elif op in COMP_OPS:
            self._write_annotation('COMP OP:' + op)
            if op != 'eq':
                self._write_annotation('CHECKING FOR OVERFLOW ON CMD')
                self._check_overflow(op)
            if op == 'eq':
                self._write_annotation('CHECKING VALIDITY OF EQ')
                self._dec_sp(flag_A_or_AM=CHOOSE_AM)
                self._write_cmd(['A', 'A-1'], C_CMD)
                self._write_cmd(['D', COMMANDS['sub']], C_CMD)
                self._write_cmd([IF_STATEMENT_TRUE + self._file_name + str(self._labels)], A_CMD)
                self._write_cmd([None, 'D', 'JEQ'], C_CMD)
                self._dec_sp(if_answer=TRUE)
                self._write_cmd([IF_STATEMENT_FALSE + self._file_name + str(self._labels)], A_CMD)
                self._write_cmd([None, '0', 'JMP'], C_CMD)
            self._write_cmd([IF_STATEMENT_TRUE + self._file_name + str(self._labels)], L_CMD)
            self._dec_sp(if_answer=FALSE)
            self._write_cmd([IF_STATEMENT_FALSE + self._file_name + str(self._labels)], L_CMD)
            self._labels += 1

    def _pop(self, seg, i):
        """
        this function pops i from the given segment
        :param seg: segment
        :param i: index
        :return:
        """
        self._write_annotation('POPPING: ' + seg + ' ' + str(i))
        if seg == 'static':
            seg = SEGMENTS[seg].format(self._file_name, str(i))
            self._write_cmd([seg], A_CMD)
        else:
            self._write_cmd([SEGMENTS[seg]], A_CMD)
            if seg == 'temp' or seg == 'pointer':
                self._write_cmd(['D', 'A'], C_CMD)
            else:
                self._load_from_m('D')
            self._write_cmd([str(i)], A_CMD)
            self._write_cmd(['D', 'D+A'], C_CMD)
        self._write_cmd(['R13'], A_CMD)
        self._save_to_m('D')
        self._load_sp()
        self._inc_dec_m(False)
        self._load_sp()
        self._load_from_m('A')
        self._load_from_m('D')
        self._write_cmd(['R13'], A_CMD)
        self._load_from_m('A')
        self._save_to_m('D')

    def _push(self, seg, i):
        """
        this function pushes i to the given segment
        :param seg:
        :param i:
        :return:
        """
        self._write_annotation('PUSHING: ' + seg + ' ' + str(i))
        if seg == 'constant':
            self._write_cmd([i], A_CMD)
            self._write_cmd(['D', 'A'], C_CMD)
        elif seg == 'static':
            seg = SEGMENTS[seg].format(self._file_name, str(i))
            self._write_cmd([seg], A_CMD)
            self._load_from_m('D')
        else:
            self._write_cmd([SEGMENTS[seg]], A_CMD)
            if seg == "temp" or seg == "pointer":
                self._write_cmd(['D', 'A'], C_CMD)
            else:
                self._load_from_m('D')
            self._write_cmd([str(i)], A_CMD)
            self._write_cmd(['A', 'D+A'], C_CMD)
            self._load_from_m('D')
        self._load_sp()
        self._load_from_m('A')
        self._save_to_m('D')
        self._load_sp()
        self._inc_dec_m()

    def _write_annotation(self, annotation):
        """
        writes an annotation line with given comment that we want to have, this is helpful for debugging long lines
        :param annotation:
        :return:
        """
        if DEBUG == True:
            self._file.write(ANNOTATION_PREFIX + annotation + NEWLINE)

    def push_or_pop(self, seg, i, push=True):
        """
        this function is a small helper that chooses if we want to pop or push from given command
        :param seg: segment
        :param i: index
        :param push: boolean that represents if this is a push or pop command
        :return:
        """
        if push:
            self._push(seg, i)
        else:
            self._pop(seg, i)

    def write(self, input_command):
        """
        writing an operator by given input command (vm command)
        :param input_command:
        :return:
        """
        self._write_op(input_command)

    def close(self):
        """
        closes file
        :return:
        """
        self._file.close()

    def push_global_stack(self):
        """
        @SP
        A=M
        M=D
        @SP
        M=M+1
        :param val: value to push to global stack
        :return:
        """
        self._load_sp()
        self._load_from_m('A')
        self._save_to_m('D')
        self._load_sp()
        self._inc_dec_m()

    def writeInit(self):
        """
        @256
        D=A
        @SP
        M=D
        :return:
        """
        self._write_cmd([INIT_RAM], A_CMD)
        self._write_cmd(['D', 'A'], C_CMD)
        self._load_sp()
        self._save_to_m('D')
        self.writeCall('Sys.init', 0)

    def writeLabel(self, label):
        """
        this function effects the label command
        (label)
        :param label:
        :return:
        """
        label = DOT_FORMAT.format(self._scope, label)
        self._write_cmd([label], L_CMD)

    def writeGoto(self, label):
        """
        this function effects to goto command
        @label
        0;JMP
        :param label:
        :return:
        """
        label = DOT_FORMAT.format(self._scope, label)
        self._write_cmd([label], A_CMD)
        self._write_cmd(UNCONDITIONAL_JUMP, C_CMD)

    def writeIf(self, label):
        """
        @SP
        M=M-1
        @SP
        AD=M
        @scope.label
        D;JNE
        :param label:
        :return:
        """
        self._load_sp()
        self._inc_dec_m(False)
        self._load_sp()
        self._load_from_m('A')
        self._load_from_m('D')
        label = DOT_FORMAT.format(self._scope, label)
        self._write_cmd([label], A_CMD)
        self._write_cmd(CONDITIONAL_JNE, C_CMD)

    def writeCall(self, functionName, numArgs):
        """
        Wrutes assembly code that effects the if-goto command.
        :param functionName: function name as string
        :param numArgs: function arguemnt number as integer
        :return:
        """
        self._write_annotation('STARTING CALL')
        total_to_decrease = numArgs + 5
        ret_label = DOT_FORMAT.format('return_addr', self._calls)
        self._write_cmd([ret_label], A_CMD)
        self._write_cmd(['D', 'A'], C_CMD)
        self.push_global_stack()
        for ptr in POINTERS:
            """
            @PTR
            D=M
            push D
            """
            self._write_cmd([SEGMENTS[ptr]], A_CMD)
            self._load_from_m('D')
            self.push_global_stack()
        self._load_sp()
        self._load_from_m('D')
        self._write_cmd([total_to_decrease], A_CMD)
        self._write_cmd(['D', 'D-A'], C_CMD)
        self._write_cmd(['ARG'], A_CMD)
        self._save_to_m('D')
        self._load_sp()
        self._load_from_m('D')
        self._write_cmd(['LCL'], A_CMD)
        self._save_to_m('D')
        self._write_cmd([functionName], A_CMD)
        self._write_cmd(UNCONDITIONAL_JUMP, C_CMD)
        self._write_cmd([ret_label], L_CMD)
        self._calls += 1

    def writeReturn(self):
        """
        writes an assembly code that effects the return command
        :return:
        """
        self._write_annotation('RETURNING')
        self._write_cmd(['LCL'], A_CMD)
        self._load_from_m('D')
        self._write_cmd(['R15'], A_CMD)
        self._save_to_m('D')

        self._write_cmd(['5'], A_CMD)
        self._write_cmd(['D', 'A'], C_CMD)
        self._write_cmd(['R15'], A_CMD)
        self._write_cmd(['A', 'M-D'], C_CMD)
        self._load_from_m('D')
        self._write_cmd(['R14'], A_CMD)
        self._save_to_m('D')

        self._load_sp()
        self._write_cmd(['AM', 'M-1'], C_CMD)
        self._load_from_m('D')
        self._write_cmd(['ARG'], A_CMD)
        self._load_from_m('A')
        self._save_to_m('D')

        self._write_cmd(['ARG'], A_CMD)
        self._load_from_m('D')
        self._load_sp()
        self._write_cmd(['M', 'D+1'], C_CMD)

        self._write_cmd(['R15'], A_CMD)
        self._write_cmd(['A', 'M-1'], C_CMD)
        self._load_from_m('D')
        self._write_cmd(['THAT'], A_CMD)
        self._save_to_m('D')

        self._write_cmd(['2'], A_CMD)
        self._write_cmd(['D', 'A'], C_CMD)
        self._write_cmd(['R15'], A_CMD)
        self._write_cmd(['A', 'M-D'], C_CMD)
        self._load_from_m('D')
        self._write_cmd(['THIS'], A_CMD)
        self._save_to_m('D')

        self._write_cmd(['3'], A_CMD)
        self._write_cmd(['D', 'A'], C_CMD)
        self._write_cmd(['R15'], A_CMD)
        self._write_cmd(['A', 'M-D'], C_CMD)
        self._load_from_m('D')
        self._write_cmd(['ARG'], A_CMD)
        self._save_to_m('D')

        self._write_cmd(['4'], A_CMD)
        self._write_cmd(['D', 'A'], C_CMD)
        self._write_cmd(['R15'], A_CMD)
        self._write_cmd(['A', 'M-D'], C_CMD)
        self._load_from_m('D')
        self._write_cmd(['LCL'], A_CMD)
        self._save_to_m('D')

        self._write_cmd(['R14'], A_CMD)
        self._load_from_m('A')
        self._write_cmd(UNCONDITIONAL_JUMP, C_CMD)

    def writeFunction(self, functionName, numArgs):
        """

        :param functionName:
        :param numArgs:
        :return:
        """
        self._write_cmd([functionName], L_CMD)
        for i in range(numArgs):
            self._push('constant', 0)
        self._scope = functionName
