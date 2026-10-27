class Ctx:
    def __enter__(self):
        return self
    def __exit__(self, *exc):
        pass
    def write(self, x):
        self.last = x
ctx = Ctx()
s = []
for x in list(ctx):
    ctx.write(x)
    s.append(('written', ctx.last))
print(s)
