class A:
    lst = [1, 2, 3]
    def meth(self):
        self.lst = self.lst[::-1]
a = A()
a.meth()
print('class:', A.lst)
print('instance:', a.lst)
