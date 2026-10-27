items = [('a', 1), ('b', 2)]
d = {k: v*2 for k, v in items}
print('transformed:', d)
l = [x+1 for x in [0, 1, 2]]
print('incremented:', l)
s = {x for x in [1, 2, 3] if x > 1}
print('filtered set:', s)
