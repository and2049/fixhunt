def splitter(s, sep=None, /, *, maxsplit=-1):  # positional-only sep, keyword-only maxsplit
    return s.split(sep, maxsplit)
result = splitter('a b c', None)[0]  # rule triggers on split() inside
print(result)
