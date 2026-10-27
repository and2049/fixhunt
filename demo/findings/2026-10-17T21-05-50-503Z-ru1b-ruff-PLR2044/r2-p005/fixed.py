class A:
    attr = 1
    @property
    def prop(self):
        return self.attr
a = A()
print(a.prop)
a.attr = 2
print(a.prop)
