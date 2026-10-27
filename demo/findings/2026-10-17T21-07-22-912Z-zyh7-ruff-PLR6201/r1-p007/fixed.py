class Buffer:
    def __init__(self):
        self.data = ''
    def write(self, s):
        self.data += s
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass
buf = Buffer()
with buf as b:
    b.write('test')
    if 'test' in ['test', 'foo']:
        print('Found in list')
    if 'test' in {'test', 'foo'}:
        print('Found in set')
