KINDS = {'static': 'static',
         'field': 'this',
         'arg': 'argument',
         'var': 'local'}


class VMWriter:

    def __init__(self, file):
        self._output_file = open(file, mode='w')

    def push(self, segment, index=None, kind=None):
        if not kind and not index:
            kind = segment.kind
            index = segment.index
            segment = KINDS[kind]
        print('push {} {}'.format(segment, index), file=self._output_file)

    def pop(self, segment, index=None, kind=None):
        if not index and not kind:
            kind = segment.kind
            index = segment.index
            segment = KINDS[kind]
        print('pop {} {}'.format(segment, index), file=self._output_file)

    def write_cmd(self, command):
        print(command, file=self._output_file)

    def write_label(self, label):
        print('label {}'.format(label), file=self._output_file)

    def write_goto(self, label):
        print('goto {}'.format(label), file=self._output_file)

    def write_if(self, label):
        print('if-goto {}'.format(label), file=self._output_file)

    def write_call(self, name, num_args):
        print('call {} {}'.format(name, num_args), file=self._output_file)

    def write_function(self, name, num_locals):
        print('function {} {}'.format(name, num_locals), file=self._output_file)

    def write_return(self):
        print('return', file=self._output_file)

    def write(self, inp):
        print(inp, file=self._output_file)

    def close(self):
        self._output_file.close()
