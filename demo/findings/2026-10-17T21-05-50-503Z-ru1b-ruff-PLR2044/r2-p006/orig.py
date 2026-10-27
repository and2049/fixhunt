class Writer:
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass
    def write(self, s):
        print(s, end='')
with Writer() as w:
    w.write('test')  #
print('done')
