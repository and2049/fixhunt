class X:
    def __eq__(self, other):
        return other is None
x = X()
print(isinstance(x, type(None)))  # Should become x is None
print('Result:', isinstance(x, type(None)))
