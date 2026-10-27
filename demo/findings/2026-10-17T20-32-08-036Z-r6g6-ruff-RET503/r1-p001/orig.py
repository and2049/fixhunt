class Ctx:
    def __enter__(self):
        return self
    def __exit__(self, *exc):
        print('exit', exc[0] is not None)
    def write(self, s):
        print('write:', s)
def f():
    with Ctx() as c:
        if True:
            return c.write('hello')
print(f())
