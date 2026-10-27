class C:
    @staticmethod
    def f():
        return 9
    def g(x=f):
        return x()
print(C().g())
