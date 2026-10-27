outer = [[1], [2]]
inner = outer
lst = inner[::-1]
print('Before:', [x[0] for x in outer])
lst[0].append(99)
print('After modification through lst:', [x[0] for x in outer])
