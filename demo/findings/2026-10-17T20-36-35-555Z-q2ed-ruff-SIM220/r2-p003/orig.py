y = 0
lst = [(y := i) and not (y := i) for i in range(2)]
print(lst)
print(y)
