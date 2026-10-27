class Flag(object):
    def __init__(self, v):
        self.v = v
    def __bool__(self):
        return self.v is not None

f = Flag(None)
print(bool(f))
f.v = 0
print(bool(f))
