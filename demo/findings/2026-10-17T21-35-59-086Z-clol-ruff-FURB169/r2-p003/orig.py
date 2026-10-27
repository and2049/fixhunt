class Writer:
    def __init__(self):
        self.data = ''
    def write(self, s):
        self.data += s

w = Writer()
if type(w) is type(None):
    w.write('unreachable')
else:
    w.write('reached')
print(w.data)
