d = {}
d[eval('1')] = 'a'  # noqa: S307
d[eval('1')] = 'b'
print(d)
