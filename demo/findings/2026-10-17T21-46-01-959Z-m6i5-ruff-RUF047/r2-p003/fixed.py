class A:
    x = 1
    def __init__(self):
        if hasattr(self, 'y'):
            self.z = self.x
    @property
    def y(self):
        return 99
a = A()
print(a.z)
