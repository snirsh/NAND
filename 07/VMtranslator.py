########################################################################################################################
# FILE: VMtranslator.py                                                                                                #
# WRITERS: Snir Sharristh                                                                                              #
# DESCRIPTION: The main program constructs a Parser to parse the VM input file and a CodeWriter to generate code       #
# into the corresponding output file. then march through the VM commands in the input file,                            #
# and generate assembly code for each one of them. If the program’s argument is a directory name                       #
# rather than a file name, the main program will process all the .vm files in this directory.                          #
########################################################################################################################
########################################################################################################################
#                                                     IMPORTS                                                          #
########################################################################################################################
import glob
import os
import sys
from os.path import join as osjoin

from CodeWriter import *
from Parser import *
########################################################################################################################
#                                                     CONSTANTS                                                        #
########################################################################################################################
ASM_SUFFIX = '.asm'

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
    else:
        print('ERR IN FILE')


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
        output_file_name = path.replace(VM_SUFFIX, ASM_SUFFIX)
        files = [path]
    else:
        files = [vm for vm in glob.glob(osjoin(path, '*' + VM_SUFFIX))]
        output_file_name = files[0].replace(VM_SUFFIX, ASM_SUFFIX)
    writer = CodeWriter(output_file_name, files[0], len(files))
    for file in files:
        writer.setFileName(file)
        parse_single_file(file, writer)
    writer.close()


def main():
    """
    our main function that calls parse_files to parse all the files and write the correct asm file
    :return:
    """
    if len(sys.argv) != 2:
        print('ERR IN ARGUMENTS')
        return
    input_path = os.path.abspath(sys.argv[1])
    parse_files(input_path)


if __name__ == '__main__':
    main()
