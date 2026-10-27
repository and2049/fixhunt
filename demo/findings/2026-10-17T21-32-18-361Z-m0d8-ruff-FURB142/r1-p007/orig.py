vals = [1, 2.0, 3, 2]
s = set()
for v in vals:
    s.add(v)
print('mixed:', sorted(s))
# all same value
s2 = set()
for v in [2, 2.0, 2]:
    s2.add(v)
print('all 2:', sorted(s2))
# bool
sb = set()
for v in [True, 1, False, 0]:
    sb.add(v)
print('bool/int:', sorted(sb))
