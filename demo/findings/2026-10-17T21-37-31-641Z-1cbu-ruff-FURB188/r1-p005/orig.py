p = 'pre'
s = 'prefix'
# This comment should be preserved
if s.startswith(p):
    s = s[:-len(p)]  # TODO: verify
    if s.startswith(p) else s
print(s)
