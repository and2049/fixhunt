s = {1, 2, 3}
x = 1.0  # float, but equals int 1
if x in s:
    s.remove(x)  # removes int 1 due to hash equality
print('Set after remove(1.0):', s)
print('Type of elements:', [type(e) for e in s])
