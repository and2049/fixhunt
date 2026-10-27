def g(*, cut='ab', s='abcd'):
    if s.startswith(cut):
        s = s[len(cut):]
    return s
print(g())
print(g(s='abab'))
