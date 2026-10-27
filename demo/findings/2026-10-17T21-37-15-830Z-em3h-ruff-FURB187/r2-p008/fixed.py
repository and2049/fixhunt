l = [0.1, 0.2, 0.3]
s1 = sum(l)
l = l[::-1]
s2 = sum(l)
print('sum before:', s1)
print('sum after:', s2)
print('equal?', s1 == s2)
