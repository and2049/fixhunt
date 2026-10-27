class MyBool:
    def __init__(self, val):
        self.val = val
    def __bool__(self):
        return bool(self.val)
    def __eq__(self, other):
        return self.val == other
x = MyBool(0)
s = {x}
print('x is False:', x is False)
print('x == False:', x == False)
print('bool(x):', bool(x))
if x in s:  # This checks equality, not identity
    s.remove(x)
print('Set after remove:', s)
# Now test with None
s2 = {None}
if None in s2:
    s2.remove(None)
print('Set with None after remove:', s2)
