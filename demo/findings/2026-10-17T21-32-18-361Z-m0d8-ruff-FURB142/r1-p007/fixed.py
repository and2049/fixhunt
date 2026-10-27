vals = [1, 2.0, 3, 2]
s = set()
s.update(vals)
print('mixed:', sorted(s))
# all same value
s2 = set()
s2.update([2, 2.0, 2])
print('all 2:', sorted(s2))
# bool
sb = set()
sb.update([True, 1, False, 0])
print('bool/int:', sorted(sb))
