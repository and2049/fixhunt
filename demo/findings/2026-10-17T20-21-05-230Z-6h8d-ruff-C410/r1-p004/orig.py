lst = []
f = lambda: list((y for y in [lst.append(i) or i for i in range(2)]))
print('First call:', f())
print('Second call:', f())
