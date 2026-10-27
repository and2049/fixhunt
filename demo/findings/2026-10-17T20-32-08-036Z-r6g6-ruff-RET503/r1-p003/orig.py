class Ctx:
    def __enter__(self):
        return self
    def __exit__(self, t, v, tb):
        print('__exit__ called,', t is not None)
    def write(self, s):
        pass
def f():
    with Ctx() as c:
        raise ValueError('bad')
    return None
try:
    f()
except Exception as e:
    print(type(e).__name__, str(e))
