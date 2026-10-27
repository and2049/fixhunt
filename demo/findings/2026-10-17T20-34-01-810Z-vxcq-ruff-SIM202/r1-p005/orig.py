class A:
    def __eq__(self, other):
        return True
    def __ne__(self, other):
        return NotImplemented
class B:
    pass
a = A()
b = B()
print('not a != b:', not a != b)
print('a == b:', a == b)
