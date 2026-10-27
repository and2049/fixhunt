s = 'suffixfix'
if s.endswith(s):
    s = s.removesuffix(s)
print(repr(s))
