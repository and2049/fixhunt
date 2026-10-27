class D:
    attr = [('x', 1)]
    @property
    def items(self):
        return self.attr if hasattr(self, 'attr') else [('y', 2)]
d1 = D()
print('comp:', {k: v for k, v in d1.items})
d1.attr = [('z', 3)]
print('comp after set:', {k: v for k, v in d1.items})
d2 = D()
print('dict constr:', dict(d2.items))
