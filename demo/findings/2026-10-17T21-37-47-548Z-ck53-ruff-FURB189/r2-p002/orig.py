class A(dict):
    __slots__ = ('x',)
    def __init__(self):
        super().__init__()
        self.x = 1
try:
    a = A()
    print('a.x:', a.x)
except Exception as e:
    print(type(e).__name__, ':', e)
