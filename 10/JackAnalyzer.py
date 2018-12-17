from CompilationEngine import *
import sys
import glob
from os.path import join as osjoin


def main():
    input_path = sys.argv[1]
    files = [_ for _ in glob.glob(osjoin(input_path, '*' + '.jack'))]
    for input_file in files:
        output_name = input_file.split('.jack')[0]
        output_name += '.xml'
        CompilationEngine(input_file, output_name)


if __name__ == '__main__':
    main()
