class W:
    def write(self, s):
        print(s, end='')
    def __enter__(self):
        return self
    def __exit__(self, *e):
        pass
w = W()
flag = False
with w if flag or True:
    w.write('x')
with w if (flag or True):
    w.write('y')
print()
