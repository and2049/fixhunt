class A:
    val = 10
    @property
    def prop(self):
        print('prop accessed')
        return self.val
a = A()
d = dict([(k, getattr(a, k)) for k in ['val', 'prop']])
print(dict(d))
