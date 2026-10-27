d = {'a': 42}
for k, v in d.items():
    s = '%d' % v  # uses v directly
    print(s)
