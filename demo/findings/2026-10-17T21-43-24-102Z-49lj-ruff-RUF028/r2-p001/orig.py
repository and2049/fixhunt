# fmt: off
class Writer:
    def __init__(self):
        self.data = ''
    def write(self, s):
        self.data += s
w = Writer()
with w:
    w.write('hello')
print(w.data)
