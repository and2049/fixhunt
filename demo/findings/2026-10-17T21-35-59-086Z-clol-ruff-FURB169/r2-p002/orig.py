class FakeNone:
    def __bool__(self):
        return False
    def __eq__(self, other):
        return other is None

obj = FakeNone()
print('obj is None:', obj is None)
print('obj == None:', obj == None)
print('type(obj) is type(None):', type(obj) is type(None))
