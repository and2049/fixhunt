class A:
    x = 1  # noqa: FAKE

def test():
    a = A()
    print(a.x, hasattr(A, 'x'))
    a.x = 2
    print(a.x, A.x)

test()
