class C:
    attr = 1
    @property
    def prop(self):
        return self.attr
c = C()
print(c.prop)
