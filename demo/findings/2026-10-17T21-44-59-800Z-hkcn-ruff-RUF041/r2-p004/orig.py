from typing import Literal
from io import StringIO

class WriteOnly:
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass
    def write(self, s):
        self.data = s

x = Literal[Literal['stdout'], Literal['stderr']]
with WriteOnly() as w:
    w.write(str(x))
print(w.data)
