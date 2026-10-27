def gen_from_u(s):
    yield from s.split()
g = gen_from_u('one two three')
first = list(g)
second = list(g)  # exhausted
print('first:', first)
print('second:', second)
