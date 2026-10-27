from typing import Literal
class Writer:
    def __init__(self):
        self.data = []
    def write(self, s):
        self.data.append(s)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass
w = Writer()
with w as f:
    f.write('test')
x = Literal['a', 'b']
print(w.data, x.__args__)
