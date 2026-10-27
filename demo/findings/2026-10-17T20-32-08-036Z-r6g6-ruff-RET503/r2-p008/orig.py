def f():
    def gen():
        yield 1
        yield 2
    g = gen()
    if True:
        return list(g)

print(f())
print(f())  # second call redefines g, so same output
