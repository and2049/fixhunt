class A:
    x = False if 2 + 2 == 4 else True
    @property
    def prop(self):
        print('prop accessed')
        return self.x

a = A()
print('class x:', A.x)
print('instance prop:', a.prop)
