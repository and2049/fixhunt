class A:
    @property
    def x(self):
        print('prop accessed')
        return 1
print('before inst')
a = A()
print(a.x)
