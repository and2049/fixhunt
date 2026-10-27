# Simulates writing via buffer-like object affected by F401 rename
class Buffer:
    def __init__(self):
        self.data = ''
    def write(self, s):
        self.data += s
    # Missing close() - relies on GC
buf = Buffer()
def foo(x):
    return x  # unused-import equivalent -> F401 triggers
print(buf.write(str(foo(42))))
