class B:
    def __init__(self, val):
        self.val = val
    def __bool__(self):
        print('__bool__ called')
        return self.val > 0

b = B(-1)
print(b or not b)
b = B(1)
print(b or not b)
