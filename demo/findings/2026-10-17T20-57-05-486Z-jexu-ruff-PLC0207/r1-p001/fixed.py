def f(*, sep=None):
    return 'a b'.split(sep, maxsplit=1)[0]
f()
