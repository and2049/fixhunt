class D:
    def gen(self):
        yield 1
        yield 2

    @property
    def values(self):
        return list(self.gen())

d = D()
print(d.values)
