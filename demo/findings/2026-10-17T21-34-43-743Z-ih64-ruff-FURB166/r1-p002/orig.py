class Writer:
    def __init__(self):
        self.buf = ''
    def write(self, data):
        self.buf += str(data)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass
w = Writer()
with w as f:
    f.write(int('0b1010', 2))
# Fix would merge: int('0b1010'[2:], 2) -> int('0b1010', 0) but only if rule fired here
# But we need the rule to fire on a slice version
with w as f:
    f.write(int('0b1010'[2:], 2))  # Rule fires here
print('Writer buffer:', repr(w.buf))
