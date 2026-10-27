s = 'hello'
if s.endswith(s[-1:]):  # s appears in condition
    s = s[:-1]
print(s)
