class A:
    x = 1
    @property
    def prop(self):
        return self.x + 1

def f():
    a = A()
    a.x = 2
    return a.prop

print(f())
