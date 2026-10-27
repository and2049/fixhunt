class X:
    def __eq__(self, other):
        return other is None
x = X()
print((x is None))  # Should become x is None
print('Result:', (x is None))
