class D:
    def f(self="D"):
        return self
x = D().f()
print(type(x).__name__ if isinstance(x, str) else x)
