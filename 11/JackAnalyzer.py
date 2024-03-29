import glob
import sys
import os

from CompilationEngine import *


def main():
    if len(sys.argv) != 2:
        print('ERR SYS ARGS')
        return
    input_path = os.path.abspath(sys.argv[1])
    if input_path.endswith('.jack'):
        input_path = [input_path]
    else:
        input_path = glob.glob(input_path + '/*.jack')
    for _ in input_path:
        out_vm = _.replace('.jack', '.vm')
        CompilationEngine(_, out_vm)


if __name__ == '__main__':
    main()
