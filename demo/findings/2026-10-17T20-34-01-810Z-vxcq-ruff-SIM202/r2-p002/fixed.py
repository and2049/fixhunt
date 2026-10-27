class A:
    def __ne__(self, other):
        return 0  # falsey
    def __eq__(self, other):
        return None  # falsey

a = A()
b = A()
print('not a != b:', not a != b)
print('a == b:', a == b)
# After fix: not a != b  ->  a == b
print('Fixed value (a == b):', a == b)
# Original was True, fixed is False -> divergence
assert not a != b == True
assert a == b == None
print('Divergence detected')
