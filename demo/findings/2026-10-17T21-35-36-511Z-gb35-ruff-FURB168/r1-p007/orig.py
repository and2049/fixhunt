class FakeNone:
    def __eq__(self, other):
        return None
obj = FakeNone()
print(isinstance(obj, type(None)))  # False
print(obj is None)                # False
print(obj == None)                # None
