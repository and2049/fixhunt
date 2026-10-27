vals = [1, 2, 2, 3]
s = set()
s.update(vals)
# f-string evaluates now
out = f'Set: {sorted(s)}'
# but we mutate after
s.add(99)
print(out)
print('Now:', sorted(s))
