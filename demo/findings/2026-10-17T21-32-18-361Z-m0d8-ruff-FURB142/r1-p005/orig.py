vals = [1, 2, 2, 3]
s = set()
for v in vals:
    s.add(v)
# f-string evaluates now
out = f'Set: {sorted(s)}'
# but we mutate after
s.add(99)
print(out)
print('Now:', sorted(s))
