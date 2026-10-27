def g(*, cut='ab', s='abcd'):
    s = s.removeprefix(cut)
    return s
print(g())
print(g(s='abab'))
