str = lambda x: x.upper()
s = 'prefix'
p = 'pre'
if s.startswith(p):
    s = s[:-len(p)] if s.startswith(p) else s
print(str(s))
