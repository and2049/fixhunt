class SilentWriter:
    def __init__(self):
        self.data = ''
    def write(self, s):
        self.data += s
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass

w = SilentWriter()
with w as f:
    f.write('test')
# Simulate a comparison involving the object
class CmpObj:
    def __init__(self, val):
        self.val = val
    def __ne__(self, other):
        return self.val != other.val
    def __eq__(self, other):
        return self.val == other.val

a = CmpObj(1)
b = CmpObj(1)
print('not a != b:', not a != b)
print('After fix (a == b):', a == b)
assert (not a != b) == (a == b)
print('Context manager and comparison stable')
