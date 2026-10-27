class MockArray:
    def __init__(self, val):
        self.val = val
x = MockArray(5)
print(x is 5)   # False
