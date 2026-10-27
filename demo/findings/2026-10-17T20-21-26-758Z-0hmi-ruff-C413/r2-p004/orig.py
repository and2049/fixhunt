data = [(1, 'a'), (2, 'b'), (1, 'c')]
r1 = list(reversed(sorted(data, key=lambda x: x[0])))
r2 = sorted(data, key=lambda x: x[0], reverse=True)
print(r1)
print(r2)
