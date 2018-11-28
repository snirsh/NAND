########################################################################################################################
# FILE: VMtranslator.py                                                                                                #
# WRITERS: Snir Sharristh                                                                                              #
########################################################################################################################
########################################################################################################################
#                                                     IMPORTS                                                          #
########################################################################################################################
import glob
import os
import sys
import inspect
from os.path import join as osjoin

from CodeWriter import *
from Parser import *

########################################################################################################################
#                                                     CONSTANTS                                                        #
########################################################################################################################
ASM_SUFFIX = '.asm'
METHOD_SELECTOR = {'function': 'writeFunction', 'call': 'writeCall', 'goto': 'writeGoto', 'if-goto': 'writeIf',
                   'return': 'writeReturn', 'label': 'writeLabel'}


########################################################################################################################


def parse_command(parser, writer):
    """
    this function will parse one command line
    :param parser:
    :param writer:
    :return:
    """
    cmd_type = parser.get_type()
    if cmd_type in ARITHMETIC_CMDS:
        writer.write(cmd_type)
    elif cmd_type in POP_OR_PUSH:
        push_or_pop_bool = bool(POP_OR_PUSH.index(cmd_type))
        seg = parser.arg1()
        i = parser.arg2()
        writer.push_or_pop(seg, i, push_or_pop_bool)
    elif cmd_type in list(METHOD_SELECTOR.keys())[:2]:  # function or call
        functionName = parser.arg1()
        num_args = parser.arg2()
        writer_func = METHOD_SELECTOR[cmd_type]
        writer.__getattribute__(writer_func)(functionName, num_args)
    elif cmd_type == 'return':
        writer.writeReturn()
    else:
        label = parser.arg1()
        writer_func = METHOD_SELECTOR[cmd_type]
        writer.__getattribute__(writer_func)(label)


def parse_single_file(filename, writer):
    """
    this function will parse one file by each command using parse_command
    :param filename:
    :param writer:
    :return:
    """
    parser = Parser(filename)
    while parser.has_more_commands():
        parse_command(parser, writer)
        parser.advance()


def parse_files(path):
    """
    this function will parse given files in path (even if single file) by using parse_single_file
    :param path:
    :return:
    """
    if VM_SUFFIX in path:
        files = [os.path.basename(path)]
    else:
        files = [vm for vm in glob.glob(osjoin(path, '*' + VM_SUFFIX))]
    if os.path.isdir(path):
        output_file_path = path + "/" + path.rsplit('/', 1)[1]
    else:
        output_file_path = path.rsplit('.', 1)[0]
    output_file_path = output_file_path + ".asm"
    is_init = False
    for file in files:
        with open(file, mode='r') as curr_file:
            for line in curr_file.readlines():
                if 'Sys.init' in line:
                    is_init = True
        curr_file.close()
    writer = CodeWriter(output_file_path, files[0], len(files))
    if is_init:
        writer.writeInit()
    for file in files:
        writer.setFileName(file)
        parse_single_file(file, writer)
    writer.close()


def main():
    """
    our main function that calls parse_files to parse all the files and write the correct asm file
    :return:
    """
    input_path = os.path.abspath(sys.argv[1])
    parse_files(input_path)



if __name__ == '__main__':
    main()
