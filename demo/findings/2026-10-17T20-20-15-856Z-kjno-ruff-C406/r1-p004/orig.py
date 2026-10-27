pairs = [('a', 1)]
d = dict(pairs)
pairs.append(('b', 2))
print('pairs:', pairs)
print('d:', d)
pairs = [('a', 1)]
d = {k: v for k, v in pairs}
pairs.append(('b', 2))
print('pairs:', pairs)
print('d:', d)
