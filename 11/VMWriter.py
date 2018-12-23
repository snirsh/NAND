from CompilationEngine import CompilationEngine


class VMWriter:
    def __init__(self, input, output):
        self._engine = CompilationEngine(input)
        self._tree = self._engine.get_tree()
        self._file = open(output, mode='w')
        self._xml_to_vm()
        self.close()

    def _xml_to_vm(self):
        pass

    def close(self):
        self._file.close()
