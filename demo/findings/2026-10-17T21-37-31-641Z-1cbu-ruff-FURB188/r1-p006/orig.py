s = 'suffixfix'
if s.endswith(s):
    s = s[:-len(s)] if s.endswith(s) else s
print(repr(s))
