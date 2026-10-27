p = 'pre'
s = 'prefix'
if s.startswith(p):
    p = 'x'  # mutate p after check
    s = s[:-len(p)] if s.startswith(p) else s
print(s)
