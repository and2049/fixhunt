d = {}
d[eval('1')] = 'a'  # noqa: PGH001
d[eval('1')] = 'b'
print(d)
