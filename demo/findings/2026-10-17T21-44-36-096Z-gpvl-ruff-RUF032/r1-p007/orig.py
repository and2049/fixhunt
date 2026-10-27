class LogCtx:
    def __enter__(self):
        self.log = []
        return self
    def __exit__(self, *exc):
        pass
    def write(self, s):
        self.log.append(s)
with LogCtx() as ctx:
    ctx.write('start')
    x = 1.5
    d = Decimal(x)  # does not trigger because x is variable
    ctx.write(f'd={d}')
print(''.join(ctx.log))
