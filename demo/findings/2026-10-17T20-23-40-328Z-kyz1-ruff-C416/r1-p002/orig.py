class C:
    @property
    def items(self):
        print('items called')
        return [('a', 1), ('b', 2)]
c = C()
print('before')
d = {k: v for k, v in c.items}
print('after comp:', d)
c2 = C()
print('before')
d2 = dict(c2.items)
print('after dict:', d2)
