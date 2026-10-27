class Buffer:
    def __init__(self):
        self.data = []
    def write(self, x):
        self.data.append(x)
buf = Buffer()
s = {1, 2}
with buf:
    for x in s:
        buf.write(x)
        s.add(3)
print('buffer:', buf.data)
print('set:', s)
