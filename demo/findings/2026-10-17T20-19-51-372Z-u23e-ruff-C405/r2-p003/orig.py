t = (1, 2)
s = set(t)
t = (3, 4)  # reassign t
print(f'set from original t: {s}')
print(f't after reassignment: {t}')
# s should still reflect (1,2), not (3,4)
