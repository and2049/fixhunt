from functools import cmp_to_key
def cmp(a, b):
    return (a > 0) - (b > 0)
data = [-1, 1, -2, 2]
r1 = list(reversed(sorted(data, key=cmp_to_key(cmp))))
r2 = sorted(data, key=cmp_to_key(cmp), reverse=True)
print(r1, r2, sep='\n')
