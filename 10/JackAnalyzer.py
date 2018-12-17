from CompilationEngine import *
import ntpath
import sys
import os

if __name__ == '__main__':
    input_path = sys.argv[1]
    files = [file.rstrip() for file in os.listdir(input_path) if file.endswith('.jack')]
    for file in files:
        output_name = str(ntpath.basename(file).split('.jack')[0]) + '.xml'
        output_name = os.path.join(os.path.abspath(input_path), output_name)
        input_file = os.path.join(os.path.abspath(input_path), file)
        CompilationEngine(input_file, output_name)