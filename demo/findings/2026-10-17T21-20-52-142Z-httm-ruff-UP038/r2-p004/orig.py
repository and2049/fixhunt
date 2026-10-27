class Writer:
    def write(self, s): print(s)
with Writer() as w:
    w.write('hello')
