class Echo:
    def __enter__(self):
        self.buffer = []
        return self
    def __exit__(self, *exc):
        return False
    def write(self, data):
        self.buffer.append(data)

class F(object):
    def log(self):
        with Echo() as e:
            e.write('test')
            return ''.join(e.buffer)

f = F()
print(f.log())
