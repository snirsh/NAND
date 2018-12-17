import glob
import sys

from CompilationEngine import *


def main():
    if len(sys.argv) != 2:
        print(' Usage error - please insert file or directory.')
        return
    input_path = os.path.abspath(sys.argv[1])
    if input_path.endswith('.jack'):
        input_path = [input_path]
    else:
        input_path = glob.glob(input_path + '/*.jack')
    for _ in input_path:
        out_xml = _.replace('.jack', '.xml')
        CompilationEngine(_, out_xml)


if __name__ == '__main__':
    main()
