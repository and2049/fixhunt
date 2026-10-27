class A:
    @property
    def x(self):
        print('get')
        return 1

def f():
    a = A()
    if True:
        return a.x

print(f())
