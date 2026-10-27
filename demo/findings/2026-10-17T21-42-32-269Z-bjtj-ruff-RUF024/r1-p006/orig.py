class Buffer:
    def __init__(self):
        self.data = []
    def write(self, s):
        self.data.append(s)
buf = Buffer()
d = dict.fromkeys(['a','b'], buf)
d['a'].write('X')
print(buf.data)
