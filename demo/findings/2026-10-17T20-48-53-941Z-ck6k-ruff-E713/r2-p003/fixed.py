class A:
    attr = [1, 2]
    @property
    def prop(self):
        print('prop called')
        return [3]
a = A()
print(1 not in a.attr)  # triggers
print(3 not in a.prop)  # triggers
print(a.attr)
