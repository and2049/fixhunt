class A:
    attr = 1
    @property
    def prop(self):
        print('prop accessed')
        return 2
a = A()
print(isinstance(a.attr, int) or isinstance(a.prop, int))
