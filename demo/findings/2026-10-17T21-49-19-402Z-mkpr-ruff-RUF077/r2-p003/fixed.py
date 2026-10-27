class E:
    def m(self=None):
        return self is None
try:
    print(E().m())
except Exception as ex:
    print(f'{type(ex).__name__}: {ex}')
