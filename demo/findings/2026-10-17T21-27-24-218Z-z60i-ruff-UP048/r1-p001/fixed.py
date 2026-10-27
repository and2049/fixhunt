class Dummy:
    def __enter__(self):
        return self
    def __exit__(self, *exc):
        pass
    def write(self, s):
        self.data += s
        return len(s)

out = []
with Dummy() as d:
    d.data = ''
    i = 0
    while True:
        if i >= 2:
            break
        d.write(str(i))
        i += 1
    out.append(d.data)
print(''.join(out))
