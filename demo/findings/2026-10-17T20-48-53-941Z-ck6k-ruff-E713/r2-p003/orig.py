class A:
    attr = [1, 2]
    @property
    def prop(self):
        print('prop called')
        return [3]
a = A()
print(not 1 in a.attr)  # triggers
print(not 3 in a.prop)  # triggers
print(a.attr)
