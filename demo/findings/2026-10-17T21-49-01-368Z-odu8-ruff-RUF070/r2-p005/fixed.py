class A:
    val = 100
    @property
    def prop(self):
        return self.val * 2
def gen():
    a = A()
    x = a.prop
    yield x
print(list(gen()))
