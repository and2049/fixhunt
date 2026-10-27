import io
class Writer:
    def __init__(self):
        self.buf = ''
    def write(self, s):
        self.buf += s
w = Writer()
with w:
    if TYPE_CHECKING:
        pass
print(w.buf)
