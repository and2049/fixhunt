class Writer:
    def __init__(self):
        self.data = ''
    def write(self, s):
        self.data += s

w = Writer()
if w is None:
    w.write('unreachable')
else:
    w.write('reached')
print(w.data)
