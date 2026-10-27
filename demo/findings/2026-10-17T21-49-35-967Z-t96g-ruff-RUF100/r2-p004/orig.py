class C:
    attr = 1  # noqa: F841
    @property
    def prop(self):
        return self.attr
c = C()
print(c.prop)
