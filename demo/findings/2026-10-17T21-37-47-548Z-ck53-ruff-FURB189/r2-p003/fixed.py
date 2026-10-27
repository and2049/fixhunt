class A(dict):
    def __setitem__(self, k, v):
        super().__setitem__(k, v * 2)
    def __hash__(self):
        return id(self)
a = A()
a[1] = 2
a[1] = 3
print('a[1]:', a[1])
print('len(a):', len(a))
print('dict(a):', dict(a))
